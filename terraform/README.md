# EKS Cluster with Terraform

This directory contains Terraform configuration for deploying an Amazon EKS (Elastic Kubernetes Service) cluster across 3 subnets with the Kubernetes Cluster Autoscaler.

## Architecture

The infrastructure includes:

- A VPC with 3 private subnets and 3 public subnets across different availability zones
- An EKS cluster deployed in the private subnets
- A managed node group with autoscaling capabilities
- Cluster Autoscaler for automatically adjusting the size of the Kubernetes cluster based on resource demands
- IAM Roles for Service Accounts (IRSA) for secure pod-level access to AWS resources
- Necessary IAM roles and policies for the EKS cluster and Cluster Autoscaler

## IAM Roles for Service Accounts (IRSA)

This configuration uses IRSA to provide fine-grained access control for the Cluster Autoscaler. IRSA allows Kubernetes service accounts to assume IAM roles directly, which provides the following benefits:

- Improved security by using temporary credentials
- Fine-grained access control at the pod level
- Reduced need for node instance profiles with broad permissions
- Simplified management of AWS permissions for Kubernetes workloads

## Prerequisites

- AWS CLI configured with appropriate credentials
- Terraform >= 1.0.0
- kubectl
- helm

## Usage

1. Initialize Terraform:

```bash
terraform init
```

2. Review the execution plan:

```bash
terraform plan
```

3. Apply the configuration:

```bash
terraform apply
```

4. Configure kubectl to use the new cluster:

```bash
aws eks update-kubeconfig --region $(terraform output -raw aws_region) --name $(terraform output -raw cluster_name)
```

5. Verify the cluster is working:

```bash
kubectl get nodes
```

6. Verify the Cluster Autoscaler is running:

```bash
kubectl get pods -n kube-system | grep cluster-autoscaler
```

7. Verify the IRSA configuration:

```bash
kubectl describe serviceaccount cluster-autoscaler -n kube-system
```

## Customization

You can customize the deployment by modifying the variables in `variables.tf`. Key variables include:

- `aws_region`: AWS region to deploy resources
- `cluster_name`: Name of the EKS cluster
- `vpc_cidr`: CIDR block for the VPC
- `subnet_cidrs`: CIDR blocks for the subnets
- `node_instance_type`: EC2 instance type for the node group
- `node_min_size`: Minimum number of nodes in the node group
- `node_max_size`: Maximum number of nodes in the node group

## Cleanup

To destroy all resources created by Terraform:

```bash
terraform destroy
```
