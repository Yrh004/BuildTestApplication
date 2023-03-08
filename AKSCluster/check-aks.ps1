# Azure AKS Get Credentials with --admin
az aks get-credentials --resource-group terraform-aks-dev --name terraform-aks-dev-cluster --admin

# Get Full Cluster Information
az aks show --resource-group terraform-aks-dev --name terraform-aks-dev-cluster -o table

# Get AKS Cluster Information using kubectl
kubectl cluster-info

# List Kubernetes Nodes
kubectl get nodes