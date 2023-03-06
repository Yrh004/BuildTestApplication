# Build an Application

## Objective
1. Build an application in <> that exposes a REST endpoint that returns the following JSON payload.

```
  {
  
    “message” :  “Automate all the things!”,
    “timestamp” : 1529729125 (current timestamp)
    
  }
```

1. Deploy the application on a Kubernetes cluster running in <> provider. 
1. The provisioning of the cluster as well as deployment of the application must be done through code.

## How it Run
My python script has a GET request to my application and then my application return a JSON dump to the HTTP. My test case checks if the JSON dump contains 'Message".

## What is running

## Cleanup

