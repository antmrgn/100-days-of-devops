#!/bin/bash


# create a virtual machine instance
# if needed create ssh-key: ssh-keygen -t rsa -b 4096
yc compute instance create \
  --name my-first-vm-by-cli \
  --description "my first VM via yc cli" \
  --zone ru-central1-a \
  --ssh-key /home/morgenshtern/.ssh/id_rsa_yc.pub \
  "--create-boot-disk" "name=boot-disk-my-first-vm,type=network-hdd,size=10,auto-delete=true" \
  "--network-interface" "subnet-id=e9b8ck0gi2m7bpcfu3rc,security-group-ids=enp5qvvllclkvj58bqtc,nat-ip-version=ipv4" \
  --memory 2 \
  --cores 2 \
  --core-fraction 20

#####
# Default distrib is Ubuntu 18.04
# connetc to VM via ssh: ssh yc-user@{VM_IP} -i {PATH_TO_PRIVATE_KEY}
##### 

# get list virtual machines
yc compute instance list --format yaml

# get informaton about a virtual machine
yc compute instance get \
  --name my-first-vm-by-cli

# get output of serial port VM
yc compute instance get-serial-port-output my-first-vm-by-cli

# https://github.com/yandex-cloud/docs/blob/master/ru/compute/operations/vm-info/get-info.md
# get information about VM inside instance (Metadata in Google Compute Engine format)
curl -H Metadata-Flavor:Google 169.254.169.254/computeMetadata/v1/instance/?recursive=true | jq -r '.'

# get internal ip inside instance
curl http://169.254.169.254/latest/meta-data/local-ipv4

# stop virtual machine
yc compute instance stop my-first-vm-by-cli

# start virtual machine
yc compute instance start my-first-vm-by-cli

# delete virtual machine
yc compute instance delete my-first-vm-by-cli

# get list of standard images
yc compute image list --folder-id standard-images

# create a virtual machine instance with select OS image and Preemptible VM
yc compute instance create \
  --name ubuntu-22-04 \
  --description "ubuntu 22 04 LTS" \
  --zone ru-central1-a \
  --ssh-key /home/morgenshtern/.ssh/id_rsa_yc.pub \
  "--create-boot-disk" "name=boot-disk-my-first-vm,type=network-hdd,size=10,auto-delete=true" \
  "--network-interface" "subnet-id=e9b8ck0gi2m7bpcfu3rc,security-group-ids=enp5qvvllclkvj58bqtc,nat-ip-version=ipv4" \
  "--create-boot-disk" "image-folder-id=standard-images,image-family=ubuntu-2204-lts" \
  --memory 2 \
  --cores 2 \
  --core-fraction 20 \
  --preemptible