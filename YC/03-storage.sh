#!/bin/bash


# create new bucket
yc storage bucket create \
  --name my-first-bucket-by-cli \
  --max-size 2 

# get list of buckets
yc storage bucket list

# get list of buckets
yc storage bucket list

# get info about bucket
yc storage bucket get my-first-bucket-by-cli

# upload file using AWS cli
