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

# upload file using AWS cli
# but before create service account, assign role and create static access key
# create a service account
yc iam service-account create --name my-service-account \
  --description "this is my service account"
# get list of roles
yc iam role list
# assigning roles to service account
yc iam service-account set-access-bindings my-service-account \
  --access-binding role=storage.uploader,subject=serviceAccount:ajedlav2drium5si0p21 \
  --access-binding role=storage.viewer,subject=serviceAccount:ajedlav2drium5si0p21
# show roles of service account
yc iam service-account list-access-bindings my-service-account
# create static key
yc iam access-key create --service-account-name my-service-account \
  --description "this key is for my bucket"
# infroramtion from previous command needed for configure AWS CLI
# 