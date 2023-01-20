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

resource "yandex_compute_instance" "vm-by-terraform-2-ubuntu" {
  name = "vm-by-terraform-2-ubuntu"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd8b24tqvq7t2f8a1o1s"
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
  
  allow_stopping_for_update = true
}

resource "yandex_vpc_network" "network-by-terraform" {
  name = "network-by-terraform"
}

resource "yandex_vpc_subnet" "subnet-by-terraform" {
  name           = "subnet-by-terraform"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-by-terraform.id
  v4_cidr_blocks = ["192.168.11.0/24"]
}

output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-by-terraform-1-centos.network_interface.0.ip_address
}

output "internal_ip_address_vm_2" {
  value = yandex_compute_instance.vm-by-terraform-2-ubuntu.network_interface.0.ip_address
}


output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-by-terraform-1-centos.network_interface.0.nat_ip_address
}

output "external_ip_address_vm_2" {
  value = yandex_compute_instance.vm-by-terraform-2-ubuntu.network_interface.0.nat_ip_address
}