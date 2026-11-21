# CloudOps — AWS Cloud Infrastructure Portfolio

A hands-on cloud engineering project demonstrating the deployment, configuration, and monitoring of a Python web application on Amazon Web Services (AWS).

## Project Overview

CloudOps explores the fundamentals of cloud infrastructure, Linux systems administration, networking, web application deployment, and infrastructure monitoring.

The application is deployed on an Amazon EC2 virtual machine running Ubuntu Linux and served through an Nginx reverse proxy and Gunicorn application server.

## Architecture

**Client Browser → AWS EC2 Security Group → Nginx → Gunicorn → Flask Application**

- **AWS EC2:** Cloud virtual machine hosting the application.
- **Ubuntu 26.04 LTS:** Linux operating system.
- **Nginx:** Reverse proxy handling incoming HTTP requests.
- **Gunicorn:** Python WSGI application server.
- **Flask:** Python web framework providing the application and API.
- **AWS CloudWatch:** Infrastructure performance monitoring.
- **AWS VPC:** Virtual network and security group configuration.

## Infrastructure Monitoring

CloudOps uses Amazon CloudWatch to monitor CPU utilization,
network traffic, CPU credit balance, and EC2 instance health.

![CloudOps Monitoring Dashboard](docs/screenshots/cloudwatch-dashboard.png)

## Implemented Features

- Provisioned and configured an AWS EC2 instance.
- Configured security group rules and restricted SSH access.
- Established secure remote administration using SSH key authentication.
- Developed a Python Flask web application.
- Implemented a JSON health-check API at `/health`.
- Configured Gunicorn to run through a persistent systemd service.
- Configured Nginx to forward requests to the Flask application.
- Deployed and tested the application over the public internet.
- Verified EC2 performance metrics using Amazon CloudWatch.

## Current Status

**Core application deployment: Complete**

The application and its public health-check endpoint are working.

The project is actively being developed as a cloud infrastructure learning and portfolio exercise.

## Planned Improvements

- Custom AWS CloudWatch monitoring dashboard and alerts.
- HTTPS and TLS certificate configuration.
- Automated testing and deployment through GitHub Actions.
- Infrastructure provisioning using Terraform.
- Additional security and reliability improvements.

## Skills Demonstrated

Cloud Computing · AWS EC2 · Linux Administration · Networking · Python · Flask · Nginx · Gunicorn · SSH · CloudWatch · Infrastructure Deployment

## Project Purpose

This project was developed to strengthen practical cloud engineering skills and demonstrate hands-on knowledge of infrastructure deployment, monitoring, networking, and application hosting.
