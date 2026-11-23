# CloudOps — AWS Cloud Engineering & DevOps Portfolio

A hands-on cloud engineering and DevOps project demonstrating the deployment, security, monitoring, and automated delivery of a Python web application on Amazon Web Services (AWS).

CloudOps was developed to gain practical experience in cloud infrastructure, Linux system administration, networking, application deployment, infrastructure security, and CI/CD automation.

**Live Application:** https://cloudops-portfolio.duckdns.org

**Health Check API:** https://cloudops-portfolio.duckdns.org/health

**Project Status:** Active Development — Core Infrastructure and Automated CI/CD Operational; Terraform Adoption In Progress

---

## Project Overview

CloudOps is a Python Flask web application deployed on an Amazon EC2 instance running Ubuntu 26.04 LTS.

The infrastructure uses Nginx as a reverse proxy, Gunicorn as the application server, and AWS CloudWatch for infrastructure monitoring.

The project includes a GitHub Actions CI/CD pipeline with automated Python testing and application deployments. Changes to `app.py` on `main` trigger deployment through OpenID Connect (OIDC) authentication and AWS Systems Manager; manual deployment remains available. Existing AWS resources are also being adopted into Terraform for infrastructure-as-code management.

The objective is to demonstrate a practical understanding of cloud architecture, secure infrastructure management, deployment automation, and operational reliability.

## System Architecture

**Application Request Flow:**

Client Browser → AWS EC2 Security Group → Nginx (HTTPS) → Gunicorn → Flask Application

**Deployment Flow:**

`app.py` change on `main` (or manual trigger) → GitHub Actions → Automated Tests → AWS OIDC Authentication → AWS Systems Manager → EC2 Deployment → Local and Public Health Verification

**Infrastructure-as-Code Flow:**

Terraform HCL Configuration → Reviewed `terraform plan` → Existing AWS Resources Imported into Terraform State → Drift Checks

### Infrastructure Components

| Technology | Purpose |
|---|---|
| Amazon EC2 | Cloud virtual machine hosting the application |
| Ubuntu 26.04 LTS | Linux operating system |
| AWS VPC | Virtual networking and network isolation |
| EC2 Security Groups | Inbound and outbound traffic control |
| Nginx | Reverse proxy, HTTPS termination and HTTP redirection |
| Gunicorn | Python WSGI application server |
| Python / Flask | Web application and REST-style health-check endpoint |
| AWS CloudWatch | Infrastructure performance and health monitoring |
| AWS IAM | Role-based access control |
| AWS Systems Manager | Remote server management and command execution |
| GitHub Actions | Automated testing and deployment orchestration |
| GitHub OIDC | Secure AWS authentication using temporary credentials |
| Terraform / HCL | Configuration and state tracking of imported AWS infrastructure |
| Let's Encrypt / Certbot | TLS certificates and renewal |

---

## Infrastructure Deployment

Provisioned and configured an Amazon EC2 instance to host the CloudOps application.

### Implemented Features

- Launched and configured an EC2 instance in the AWS Europe (Ireland) region.
- Installed and configured Ubuntu Linux.
- Configured VPC networking and EC2 security group rules.
- Established remote server administration using SSH key authentication.
- Configured an isolated Python virtual environment.
- Developed and deployed a Python Flask application.
- Configured Gunicorn as the WSGI application server.
- Created a systemd service to manage the application.
- Configured Nginx to reverse-proxy incoming requests to Gunicorn.
- Configured public DNS using DuckDNS.
- Enabled HTTPS encryption using Let's Encrypt.
- Implemented application health checks.

### Application Health API

The `/health` endpoint returns a JSON response indicating application status.

Example response:

`{"service":"cloudops","status":"healthy","timestamp":"2026-11-21T23:01:21+00:00"}`

The endpoint is used for application availability verification and post-deployment health checks.

---

## Infrastructure Monitoring — AWS CloudWatch

Created a custom Amazon CloudWatch dashboard to monitor the performance and operational health of the EC2 instance.

### Monitored Metrics

- **CPU Utilization:** Tracks average processor usage over five-minute intervals.
- **Network Traffic:** Monitors incoming and outgoing network activity.
- **CPU Credit Balance:** Tracks accumulated CPU credits available for burstable instance performance.
- **Instance Health:** Monitors EC2 status-check failures.

### CloudWatch Dashboard

![CloudOps Infrastructure Monitoring Dashboard](docs/screenshots/cloudwatch-dashboard.png)

The monitoring dashboard provides visibility into resource utilization, network activity, and infrastructure health.

These metrics support performance analysis and infrastructure troubleshooting.

---

## HTTPS and Infrastructure Security

Implemented HTTPS encryption and foundational infrastructure security controls.

### Security Features

- TLS encryption using Let's Encrypt certificates.
- HTTP-to-HTTPS redirection through Nginx.
- Automated certificate renewal configured and tested.
- SSH key-based authentication for remote administration.
- SSH access limited by security-group CIDR rules; a broad IPv6 SSH CIDR remains a documented hardening item.
- Role-based AWS permissions using IAM.
- Gunicorn configured behind the Nginx reverse proxy.
- Sensitive local files excluded from Git tracking through `.gitignore`.
- Temporary AWS credentials for GitHub Actions through OIDC authentication.

### Secure Public Access

**Website:** https://cloudops-portfolio.duckdns.org

**Health Check:** https://cloudops-portfolio.duckdns.org/health

---

## CI/CD Pipeline — GitHub Actions

Implemented a GitHub Actions pipeline to automate application testing and coordinate deployments to AWS EC2.

The deployment workflow is triggered automatically when `app.py` changes on the `main` branch. It can also be started manually through GitHub Actions. Changes limited to documentation or Terraform files do not trigger this deployment workflow.

### Continuous Integration (CI)

The CI pipeline performs the following operations:

1. Checks out application source code from GitHub.
2. Configures the Python execution environment.
3. Installs application dependencies.
4. Runs automated tests using pytest.
5. Reports test results through GitHub Actions.

The dedicated Python test workflow runs on pushes and pull requests. Automated tests verify the Flask homepage and application health-check endpoint. The deployment workflow runs tests again before deploying.

### Continuous Delivery (CD)

The deployment workflow performs the following operations:

1. Triggers deployment when `app.py` is pushed to `main`, or manually through `workflow_dispatch`.
2. Executes automated Python tests.
3. Authenticates to AWS using GitHub OIDC.
4. Obtains temporary AWS credentials through IAM role assumption.
5. Sends a deployment command through AWS Systems Manager.
6. Retrieves the specified GitHub commit on the EC2 instance.
7. Creates a backup of the existing application file.
8. Updates the deployed Flask application.
9. Restarts the application using systemd.
10. Performs application health checks with retry logic.
11. Verifies the public HTTPS health endpoint.
12. Reports the deployment result in GitHub Actions.

### Deployment Security

The pipeline uses security controls including:

- GitHub OIDC authentication without permanent AWS access keys.
- IAM trust conditions restricting role assumption to the authorized GitHub repository and `main` branch.
- Systems Manager permissions scoped to the target EC2 instance and command document.
- Remote execution without storing the EC2 SSH private key in GitHub.
- Deployment serialization to prevent overlapping deployments.
- Application backup before deployment.
- Dependency-change detection requiring manual review.
- Application-file rollback on failed deployment, followed by a service restart and local health verification.

**Rollback testing:** A mocked rollback-function test verified backup restoration and preservation of the original failure status. A separate isolated Gunicorn test verified that an unhealthy Flask version (HTTP 503) could be replaced with the previous working version and return to a healthy state. Both tests passed without changing the production application. **A full end-to-end failure test of the production deployment script has not yet been completed.** Rollback is currently limited to `app.py`; dependency, database, and infrastructure rollbacks are outside the implemented scope.

**Deployment limitation:** The server-side deployment script at `/usr/local/sbin/cloudops-deploy` is not yet version-controlled in this repository. It rejects `requirements.txt` changes pending manual review.

### Verified Deployment

A manually triggered GitHub Actions deployment successfully updated the CloudOps homepage on EC2 and passed the public application health check.

An automatic-deployment smoke test then pushed a harmless `app.py` comment on `main` (commit [`a61e127`](https://github.com/NyxxOhhNyxx/aws-cloudops-portfolio/commit/a61e12716391485b35022a87387ed6d4784dcc4c)). The updated comment was confirmed in the live EC2 application file, and the public HTTPS `/health` endpoint returned `healthy`.

**Deployment triggers:** Automatic on `app.py` changes pushed to `main`; manual `workflow_dispatch` also available.

**Application:** https://cloudops-portfolio.duckdns.org
**GitHub Actions:** https://github.com/NyxxOhhNyxx/aws-cloudops-portfolio/actions

---

## AWS Systems Manager Integration

Configured AWS Systems Manager to securely administer the EC2 instance.

### Implemented Capabilities

- Installed and configured the AWS Systems Manager Agent.
- Assigned an IAM instance role with the required Systems Manager permissions.
- Registered the EC2 instance as an online managed node.
- Verified remote command execution using AWS Run Command.
- Integrated Systems Manager with GitHub Actions for application deployments.

This enables remote infrastructure administration and deployment operations without requiring direct SSH access from GitHub Actions.

---

## Infrastructure as Code — Terraform

Terraform (HCL) is used to describe and track existing AWS infrastructure. The project was initially configured through AWS and subsequently imported into Terraform state, rather than recreated from scratch.

### Resources Imported and Verified

- Existing EC2 instance (`cloudops-server`, `t3.micro`).
- Existing EC2 security group (`cloudops-sg`).
- Five individually managed security-group rules: HTTP (80), HTTPS (443), SSH over IPv4, SSH over IPv6, and IPv4 outbound access.
- Imported resources were checked with `terraform validate` and `terraform plan`, producing a **No changes** result after import and cleanup.
- `prevent_destroy = true` is configured on the managed EC2 instance and security group to help protect against accidental Terraform-driven replacement or deletion.

The instance uses the default VPC (`172.31.0.0/16`) and a subnet in `eu-west-1a` (`172.31.16.0/20`). **These networking components have been inspected but not yet imported as Terraform-managed resources.** Existing IAM resources are also not yet defined in Terraform.

### State and Repository Safety

- Terraform configuration and the provider lock file are committed to GitHub.
- Local Terraform state (`*.tfstate`), plans (`*.tfplan`), and variable values (`*.tfvars`) are excluded by `.gitignore`.
- SSH CIDR values are supplied through an ignored local `terraform.tfvars` file.
- A secure remote state backend, state locking, configuration parameterization, and fully reproducible provisioning remain future improvements.
- All infrastructure changes require review of `terraform plan` before any `terraform apply`.

---

## Repository Structure

| Path | Description |
|---|---|
| `app.py` | Flask application and health-check API |
| `requirements.txt` | Python application dependencies |
| `tests/` | Automated application tests |
| `.github/workflows/python-tests.yml` | Python CI testing workflow |
| `.github/workflows/aws-oidc-check.yml` | AWS OIDC authentication verification |
| `.github/workflows/ec2-command-test.yml` | GitHub-to-EC2 remote execution verification |
| `.github/workflows/deploy.yml` | AWS EC2 deployment workflow: automatic `app.py` push trigger and manual trigger |
| `terraform/main.tf` | AWS provider, existing-instance lookup, and outputs |
| `terraform/ec2.tf` | Imported EC2 instance configuration and lifecycle protection |
| `terraform/networking.tf` | Imported security group and five individual firewall rules |
| `terraform/variables.tf` | Terraform SSH CIDR variable declarations |
| `terraform/.terraform.lock.hcl` | Version lock for the Terraform AWS provider |
| `docs/screenshots/` | Infrastructure documentation and screenshots |
| `.gitignore` | Local file and sensitive-file exclusions |
| `README.md` | Project documentation |

Terraform state and `terraform.tfvars` remain local and are not committed. The live deployment script currently resides on EC2 at `/usr/local/sbin/cloudops-deploy`; version-controlling and testing that script end-to-end remain planned improvements.

---

## Completed Milestones

- [x] Provision AWS EC2 infrastructure.
- [x] Configure Ubuntu Linux and SSH access.
- [x] Deploy Python Flask application.
- [x] Configure Gunicorn and Nginx.
- [x] Implement application health-check API.
- [x] Configure DNS and HTTPS.
- [x] Test TLS certificate renewal.
- [x] Create custom CloudWatch monitoring dashboard.
- [x] Create GitHub repository and project documentation.
- [x] Implement automated Python testing.
- [x] Configure GitHub Actions OIDC authentication with AWS.
- [x] Integrate AWS Systems Manager.
- [x] Verify remote command execution.
- [x] Implement manually triggered CI/CD deployment workflow.
- [x] Successfully deploy and verify a live application update.
- [x] Enable automatic EC2 deployment for `app.py` pushes to `main`.
- [x] Confirm an automatically deployed application change reached EC2 and the public health check stayed healthy.
- [x] Verify mocked rollback-function recovery and isolated Gunicorn application recovery.
- [x] Import existing EC2 instance into Terraform with a no-change plan.
- [x] Import existing security group and five rules into Terraform with a no-change plan.

---

## Development Roadmap

### Infrastructure as Code

- [x] Implement Terraform configurations for existing EC2 and security-group resources.
- [x] Import the EC2 instance, security group, and existing firewall rules without modifying live infrastructure.
- [ ] Import or model the existing VPC and subnet safely.
- [ ] Define relevant IAM resources in Terraform using least-privilege permissions.
- [ ] Make infrastructure configuration reproducible and parameterized.
- [ ] Implement secure remote Terraform state storage and locking.

### CI/CD Improvements

- [x] Add automatic deployment on `app.py` changes to `main`, retaining manual deployment.
- [x] Run simulated rollback-function and isolated Gunicorn recovery tests.
- [ ] Perform an end-to-end failure/rollback test of the production deployment script under controlled conditions.
- [ ] Implement GitHub deployment environments and approval controls.
- [ ] Version-control the EC2 deployment script.
- [ ] Improve deployment logs and error reporting.
- [ ] Introduce additional automated tests.

### Monitoring and Reliability

- [ ] Configure CloudWatch alarms.
- [ ] Improve application-level availability monitoring.
- [ ] Add deployment notifications.
- [ ] Expand operational documentation.
- [ ] Review infrastructure costs and resource utilization.

### Security Enhancements

- [ ] Introduce automated dependency vulnerability scanning.
- [ ] Add secret scanning and additional repository security checks.
- [ ] Review IAM permissions for least-privilege access.
- [ ] Narrow the existing IPv6 SSH security-group CIDR while preserving administrative access.
- [ ] Implement additional infrastructure hardening.
- [ ] Document security controls and operational procedures.

---

## Skills Demonstrated

**Cloud Computing:** AWS EC2, VPC, IAM, CloudWatch, Systems Manager, Terraform

**Operating Systems:** Ubuntu Linux, System Administration, systemd

**Networking:** TCP/IP, DNS, HTTPS, TLS, SSH, Security Groups, Reverse Proxies

**Software Development:** Python, Flask, REST-style APIs, Automated Testing

**DevOps:** Git, GitHub, GitHub Actions, CI/CD, Deployment Automation, OIDC Authentication, Terraform / HCL

**Infrastructure Operations:** Server Configuration, Monitoring, Troubleshooting, Deployment Verification, Application Backup and Recovery

---

## Project Purpose

CloudOps is an independently developed cloud engineering portfolio project created to strengthen practical knowledge of AWS infrastructure, Linux administration, secure application hosting, monitoring, and deployment automation.

The project emphasizes hands-on implementation, technical problem-solving, infrastructure security, and operational practices.

It serves as an evolving demonstration of practical cloud engineering and DevOps capabilities. Current work includes automated deployment and imported Terraform configurations; future development focuses on reproducible infrastructure, operational reliability, security, and deployment safeguards.