#!/bin/bash


# create new bucket (size in bytes)
yc storage bucket create \
  --name my-first-bucket-by-cli \
  --max-size 2 

# update bucket (size = 100MB)
yc storage bucket update \
  --name my-first-bucket-by-cli \
  --max-size 104857600

# get list of buckets
yc storage bucket list

# get list of buckets
yc storage bucket list

# get info about bucket
yc storage bucket get my-first-bucket-by-cli

####
# upload file using AWS cli
# but before create service account, assign role and create static access key
####
# create a service account
yc iam service-account create --name my-service-account \
  --description "this is my service account"
# get list of roles
yc iam role list
# get list of folders
yc resource-manager folder list
# assigning roles to service account
# we will assign role to whole folder (bacause we can't assign role to bucket via cli)
yc resource-manager folder add-access-binding default \
  --role storage.uploader \
  --subject serviceAccount:ajedlav2drium5si0p21
# show assigned roles 
yc resource-manager folder list-access-binding default \
# create static key
yc iam access-key create --service-account-name my-service-account \
  --description "this key is for my bucket"

# infroramtion from previous command needed to configure AWS CLI
# aws cli configuration https://cloud.yandex.com/en-ru/docs/storage/tools/aws-cli
# upload all objects from a local directory
aws --endpoint-url=https://storage.yandexcloud.net \
  s3 cp --recursive ~/to_s3/app s3://my-first-bucket-by-cli/app/

# getting list of object 
aws --endpoint-url=https://storage.yandexcloud.net \
  s3 ls s3://my-first-bucket-by-cli/app/

# delete object (role "storage.uploader" is not enough for delete)
aws --endpoint-url=https://storage.yandexcloud.net \
  s3 rm s3://my-first-bucket-by-cli/app/loki.yml

# retrieving an object
aws --endpoint-url=https://storage.yandexcloud.net \
  s3 cp s3://my-first-bucket-by-cli/app/mongo.yml ~/to_s3/mongo.yml

# show bucket stats
yc storage bucket stats my-first-bucket-by-cli