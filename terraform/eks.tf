# EKS cluster configuration

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"

  cluster_name    = var.cluster_name
  cluster_version = "1.27"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  cluster_endpoint_private_access = true
  cluster_endpoint_public_access  = true

  # Enable EKS Cluster CloudWatch Logging
  cluster_enabled_log_types = ["api", "audit", "authenticator", "controllerManager", "scheduler"]

  # Add required tags for the cluster autoscaler
  tags = merge(
    var.tags,
    {
      "k8s.io/cluster-autoscaler/${var.cluster_name}" = "owned"
      "k8s.io/cluster-autoscaler/enabled"             = "true"
    }
  )

  # EKS Managed Node Group(s)
  eks_managed_node_group_defaults = {
    ami_type       = "AL2_x86_64"
    instance_types = [var.node_instance_type]

    attach_cluster_primary_security_group = true
  }

  eks_managed_node_groups = {
    main = {
      name = var.node_group_name

      min_size     = var.node_min_size
      max_size     = var.node_max_size
      desired_size = var.node_desired_capacity

      # Add required tags for the cluster autoscaler
      tags = merge(
        var.tags,
        {
          "k8s.io/cluster-autoscaler/${var.cluster_name}" = "owned"
          "k8s.io/cluster-autoscaler/enabled"             = "true"
        }
      )
    }
  }

  # aws-auth configmap
  manage_aws_auth_configmap = true
}
