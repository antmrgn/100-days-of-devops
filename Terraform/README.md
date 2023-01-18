## Terraform with Yandex Cloud

Create VMs, networks, s3 storage, k8s clusters using terraform

#### Installiation Terraform (ubuntu 20.04)

[Documentation](https://developer.hashicorp.com/terraform/downloads)

```bash
mkdir /home/antmrgn/ter && cd "$_"
wget https://hashicorp-releases.yandexcloud.net/terraform/1.3.7/terraform_1.3.7_linux_amd64.zip
unzip terraform_1.3.7_linux_amd64.zip
export PATH=$PATH:/home/antmrgn/ter/
rm terraform_1.3.7_linux_amd64.zip
# add variables to env
export YC_TOKEN=$(yc iam create-token)
export YC_CLOUD_ID=$(yc config get cloud-id)
export YC_FOLDER_ID=$(yc config get folder-id)
```