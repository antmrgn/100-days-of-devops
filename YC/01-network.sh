#!/bin/bash

# create cloud network
yc vpc network create \
  --name network-by-cli \
  --description "my first network via yc cli"

# get list cloud networks
yc vpc network list --format yaml

# get informaton about a network
yc vpc network get \
  --name network-by-cli

# create subnet
yc vpc subnet create \
  --name my-subnet-a \
  --zone ru-central1-a \
  --range 10.49.93.0/24 \
  --network-name network-by-cli \
  --description "my first subnet via yc cli"

# get list subnets in network
yc vpc network list-subnets \
  --name network-by-cli

# get list subnets
yc vpc subnet list

# get informaton about a subnet
yc vpc subnet get \
  --name my-subnet-a


# delete default subnets
for id in $(yc vpc subnet list --format text | grep default | awk '{print $2}'); \
  do yc vpc subnet delete --id $id; \
  done
 
# delete default network
yc vpc network delete \
  --name default


# create security group
yc vpc security-group create \
  --name ssh-http-https \
  --network-name network-by-cli \
  "--rule" "description=ssh,direction=ingress,port=22,protocol=tcp,v4-cidrs=[185.252.63.21/32,10.49.93.0/24]" \
  "--rule" "description=http,direction=ingress,port=80,protocol=any,v4-cidrs=[0.0.0.0/0]" \
  "--rule" "description=https,direction=ingress,port=443,protocol=any,v4-cidrs=[0.0.0.0/0]" \
  "--rule" "description=allow-all-output,direction=egress,port=any,protocol=any,v4-cidrs=[0.0.0.0/0]" \
  --description "security group for access ssh and http(s)"

# get list security groups
yc vpc security-group list --format yaml