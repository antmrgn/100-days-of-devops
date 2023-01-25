// Provider
terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = "ru-central1-a"
}


locals {
  k8s_version = "1.22" # Set the Kubernetes version.
}


// VM1
resource "yandex_compute_instance" "vm-by-terraform-1-centos" {
  name = "vm-by-terraform-1-centos"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd8151sv1q69mchl804a"
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-by-terraform.id
    nat       = true
  }

  metadata = {
    user-data = "${file("./meta.txt")}"
  }

  scheduling_policy {
    preemptible = true
  }
}

// VM2
resource "yandex_compute_instance" "vm-by-terraform-2-ubuntu" {
  name = "vm-by-terraform-2-ubuntu"

  resources {
    cores         = 2
    memory        = 2
    core_fraction = 20
  }

  boot_disk {
    initialize_params {
      image_id = "fd8b24tqvq7t2f8a1o1s"
      size     = 17
    }
  }

  secondary_disk {
    disk_id = yandex_compute_disk.empty-disk.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-by-terraform.id
    nat       = true
  }

  metadata = {
    user-data = "${file("./meta.txt")}"
  }

  scheduling_policy {
    preemptible = true
  }

  allow_stopping_for_update = true
}

// Disk for VM2
resource "yandex_compute_disk" "empty-disk" {
  name       = "empty-disk"
  type       = "network-hdd"
  zone       = "ru-central1-a"
  size       = 8
  block_size = 4096
}

// network
resource "yandex_vpc_network" "network-by-terraform" {
  name = "network-by-terraform"
}

// subnet
resource "yandex_vpc_subnet" "subnet-by-terraform" {
  name           = "subnet-by-terraform"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-by-terraform.id
  v4_cidr_blocks = ["192.168.11.0/24"]
}

// get internal ip of VMs
output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-by-terraform-1-centos.network_interface.0.ip_address
}

output "internal_ip_address_vm_2" {
  value = yandex_compute_instance.vm-by-terraform-2-ubuntu.network_interface.0.ip_address
}

// get external ip of VMs
output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-by-terraform-1-centos.network_interface.0.nat_ip_address
}

output "external_ip_address_vm_2" {
  value = yandex_compute_instance.vm-by-terraform-2-ubuntu.network_interface.0.nat_ip_address
}

// create s3 bucket
// firstly add service account and create static key
resource "yandex_iam_service_account" "sa" {
  name = "service-account-via-terraform"
}

// Назначение роли сервисному аккаунту
resource "yandex_resourcemanager_folder_iam_member" "sa-editor" {
  folder_id = "b1g842fiiub76pl0ubak"
  role      = "storage.editor"
  member    = "serviceAccount:${yandex_iam_service_account.sa.id}"
}

// Создание статического ключа доступа
resource "yandex_iam_service_account_static_access_key" "sa-static-key" {
  service_account_id = yandex_iam_service_account.sa.id
  description        = "static access key for object storage"
}

// Создание бакета с использованием ключа
resource "yandex_storage_bucket" "test" {
  access_key = yandex_iam_service_account_static_access_key.sa-static-key.access_key
  secret_key = yandex_iam_service_account_static_access_key.sa-static-key.secret_key
  bucket     = "bucket-via-terraform"
}

// create k8s cluster
resource "yandex_kubernetes_cluster" "k8s-cluster-via-terraform" {
  network_id = yandex_vpc_network.network-by-terraform.id
  master {
    zonal {
      zone      = yandex_vpc_subnet.subnet-by-terraform.zone
      subnet_id = yandex_vpc_subnet.subnet-by-terraform.id
    }
    public_ip = true
    version   = local.k8s_version
  }
  service_account_id      = yandex_iam_service_account.sa-k8s.id
  node_service_account_id = yandex_iam_service_account.sa-k8s.id
  depends_on = [
    yandex_resourcemanager_folder_iam_binding.editor,
    yandex_resourcemanager_folder_iam_binding.images-puller
  ]
}

// create account for k8s cluster
resource "yandex_iam_service_account" "sa-k8s" {
  name        = "sa-k8s"
  description = "sa for k8s cluster"
}

// add role to sa
resource "yandex_resourcemanager_folder_iam_binding" "editor" {
  folder_id = "b1g842fiiub76pl0ubak"
  role      = "editor"
  members = [
    "serviceAccount:${yandex_iam_service_account.sa-k8s.id}"
  ]
}

// add role to sa
resource "yandex_resourcemanager_folder_iam_binding" "images-puller" {
  folder_id = "b1g842fiiub76pl0ubak"
  role      = "container-registry.images.puller"
  members = [
    "serviceAccount:${yandex_iam_service_account.sa-k8s.id}"
  ]
}

// add node group to k8s cluster
resource "yandex_kubernetes_node_group" "k8s-node-group-by-terraform" {
  description = "Node group for Managed Service for Kubernetes cluster"
  name        = "k8s-node-group"
  cluster_id  = yandex_kubernetes_cluster.k8s-cluster-via-terraform.id
  version     = local.k8s_version

  scale_policy {
    fixed_scale {
      size = 1 # Number of hosts
    }
  }

  allocation_policy {
    location {
      zone = "ru-central1-a"
    }
  }

  instance_template {
    platform_id = "standard-v2"

    network_interface {
      nat        = true
      subnet_ids = [yandex_vpc_subnet.subnet-by-terraform.id]
    }

    resources {
      memory = 2 # RAM quantity in GB
      cores  = 2 # Number of CPU cores
    }

    boot_disk {
      type = "network-hdd"
      size = 64 # Disk size in GB
    }

    scheduling_policy {
      preemptible = true
    }
  }
}