
terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "eu-west-1"
}

# Reference our existing EC2 server
data "aws_instance" "cloudops" {
  instance_id = "i-068fd3d6b09209381"
}

output "cloudops_instance_id" {
  description = "Existing CloudOps EC2 instance ID"
  value       = data.aws_instance.cloudops.id
}

output "cloudops_public_ip" {
  description = "Public IPv4 address of CloudOps"
  value       = data.aws_instance.cloudops.public_ip
}

output "cloudops_instance_type" {
  description = "EC2 instance type"
  value       = data.aws_instance.cloudops.instance_type
}
