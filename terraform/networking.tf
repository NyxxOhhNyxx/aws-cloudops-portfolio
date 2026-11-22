
# Existing CloudOps EC2 security group
# Firewall rules will be managed as separate resources.

resource "aws_security_group" "cloudops" {
  name        = "cloudops-sg"
  description = "CloudOps web server security group"
  vpc_id      = "vpc-08470bbf16994c634"

  lifecycle {
    prevent_destroy = true
  }
}


# HTTP: public IPv4
resource "aws_vpc_security_group_ingress_rule" "http" {
  security_group_id = aws_security_group.cloudops.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "tcp"
  from_port         = 80
  to_port           = 80
}

# HTTPS: public IPv4
resource "aws_vpc_security_group_ingress_rule" "https" {
  security_group_id = aws_security_group.cloudops.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "tcp"
  from_port         = 443
  to_port           = 443
}

# SSH: restricted IPv4
resource "aws_vpc_security_group_ingress_rule" "ssh_ipv4" {
  security_group_id = aws_security_group.cloudops.id
  cidr_ipv4         = var.ssh_ipv4_cidr
  ip_protocol       = "tcp"
  from_port         = 22
  to_port           = 22
}

# SSH: existing IPv6 range
resource "aws_vpc_security_group_ingress_rule" "ssh_ipv6" {
  security_group_id = aws_security_group.cloudops.id
  cidr_ipv6         = var.ssh_ipv6_cidr
  ip_protocol       = "tcp"
  from_port         = 22
  to_port           = 22
}

# Outbound: all protocols over IPv4
resource "aws_vpc_security_group_egress_rule" "outbound_ipv4" {
  security_group_id = aws_security_group.cloudops.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1"
}
