#!/bin/bash



# add editor role for service account
yc resource-manager cloud add-access-binding cloud-tonchyk2006 \
    --role editor \
    --subject serviceAccount:ajedlav2drium5si0p21

# show available k8s version
yc managed-kubernetes list-versions

# create new k8s cluster
yc managed-kubernetes cluster create \
  --name my-first-k8s-cluster \
  --network-name network-by-cli \
  --zone ru-central1-a \
  --subnet-name my-subnet-a \
  --public-ip \
  --release-channel regular \
  --version 1.23 \
  --cluster-ipv4-range 10.1.0.0/16 \
  --service-ipv4-range 10.2.0.0/16 \
  --service-account-name my-service-account \
  --node-service-account-name my-service-account \
  --daily-maintenance-window start=22:00,duration=10h

# get list of k8s clusters
yc managed-kubernetes cluster list

# get info about k8s cluster
yc managed-kubernetes cluster get my-first-k8s-cluster

# stop k8s cluster
yc managed-kubernetes cluster stop my-first-k8s-cluster

# start k8s cluster
yc managed-kubernetes cluster start my-first-k8s-cluster

# delete k8s cluster 
yc managed-kubernetes cluster delete my-first-k8s-cluster



########################

# connect to cluster
# get cluster ID and set variable
yc managed-kubernetes cluster list
CLUSTER_ID=catjkitc4fhc5gao94h7

# connect via external ip address
yc managed-kubernetes cluster \
  get-credentials $CLUSTER_ID \
  --external

# get external ip of k8s cluster
yc managed-kubernetes cluster get --id $CLUSTER_ID \
  --format json | \
  jq -r .master.endpoints.external_v4_endpoint

# get info via kubectl
kubectl cluster-info

# get running pods list
kubectl get pods --all-namespaces

# get nodes list
kubectl get nodes

# run hello-minikube container
kubectl run hello-minikube --image=gcr.io/google_containers/echoserver:1.4 --port=8080