# Build an Application

## Objective
1. Build an application in python that exposes a REST endpoint that returns the following JSON payload.
1. Deploy the application on a Kubernetes cluster running in Azure public cloud provider. 
1. The provisioning of the cluster as well as deployment of the application must be done through code.
```
  {
  
    “message” :  “Automate all the things!”,
    “timestamp” : 1529729125 (current timestamp)
    
  }
```

## Overview of tools used
1. Python
1. Azure
1. GitHub Actions
1. VS Code

# How it Run
My python script has a GET request to my application and then my application return a JSON dump to the HTTP. My test case checks if the JSON dump contains 'Message". When it comes to building the Docker iamge of my app, I run the docker build and docker run command to verfiy that the Docker image actual returns the JSON.  

## Steps of the GitHub Actions Deployment
  1. Log into Docker Hub
  1. Setup Docker Buildx
  1. Build and Push Docker Image
  1. Log into Azure
  1. Install kubectl
  1. Deploy Docker Image
  1. Verify App
  1. Cleanup AKS Cluster

# What is running
There's a python app that is running on a Docker image and the Docker image is deployed to an AKS cluster in Azure.

# Cleanup
The runner cleans itself up from the steps/jobs I've created has ran, pass or fail. I created a step to clean up the AKS cluster by deleting the service and deployment.