
# Reference the existing AWS default VPC.

data "aws_vpc" "cloudops" {
  id = "vpc-08470bbf16994c634"
}

data "aws_subnet" "cloudops" {
  id = "subnet-01a7e5072589060f9"
}

output "cloudops_vpc_id" {
  description = "VPC containing the CloudOps server"
  value       = data.aws_vpc.cloudops.id
}

output "cloudops_subnet_id" {
  description = "Subnet containing the CloudOps server"
  value       = data.aws_subnet.cloudops.id
}

output "cloudops_subnet_cidr" {
  description = "CloudOps subnet network range"
  value       = data.aws_subnet.cloudops.cidr_block
}
