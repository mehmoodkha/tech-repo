#!/usr/bin/env python
"""
Setup script to populate the database with sample courses.
Run with: python setup_courses.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devops_nexus.settings')
django.setup()

from courses.models import Course

def create_courses():
    """Create sample courses if they don't exist"""
    
    courses_data = [
        {
            'title': 'Linux - RHCSA and RHCE',
            'description': 'Complete Linux certification path covering Red Hat Certified System Administrator (RHCSA) and Red Hat Certified Engineer (RHCE). Master essential and advanced Linux administration skills including system configuration, shell scripting, user management, storage, networking, security, and automation.',
            'price': 6999.00,
            'duration': '12 Weeks',
            'topics': [
                "Understand and Use Essential Tools",
                "File System Navigation & Management",
                "User & Group Management",
                "File Permissions & Ownership",
                "Process Management",
                "Package Management (YUM/DNF)",
                "Systemd Services & Targets",
                "Networking Configuration",
                "Firewall Configuration (firewalld)",
                "Storage Management (LVM)",
                "File System Management (XFS, EXT4)",
                "NFS & Samba Configuration",
                "SELinux Configuration",
                "System Logging & Journald",
                "Kernel Management & Tuning",
                "Boot Process & GRUB",
                "Task Automation (Cron, At)",
                "Shell Scripting Fundamentals",
                "SSH & Remote Management",
                "Container Management (Podman)",
                "Performance Tuning and Monitoring",
                "Troubleshooting & Recovery",
                "RHCE: Ansible Automation",
                "RHCE: Advanced Networking",
                "RHCE: Security & Compliance"
            ]
        },
        {
            'title': 'DevOps Pre-Requisite',
            'description': 'Master the basics of Linux, Networking, and Git before diving into complex tools. This comprehensive course covers essential command-line skills, file system management, bash scripting, networking fundamentals, and version control with Git.',
            'price': 2999.00,
            'duration': '6 Weeks',
            'topics': [
                "Linux Command Line Basics",
                "File System & Directory Structure",
                "Text Editors (Vi/Vim, Nano)",
                "File Operations & Manipulation",
                "User & Permission Management",
                "Process Management Basics",
                "Package Management",
                "Bash Scripting Fundamentals",
                "Variables & Loops in Bash",
                "Networking Fundamentals",
                "TCP/IP & OSI Model",
                "DNS & DHCP Concepts",
                "SSH & Secure Connections",
                "Git Version Control Basics",
                "Git Branches & Merging",
                "GitHub & Remote Repositories",
                "Git Workflow Best Practices",
                "Basic Troubleshooting"
            ]
        },
        {
            'title': 'Docker for Beginners',
            'description': 'Learn how to build, ship, and run applications using containers. This hands-on course covers Docker basics, containerization concepts, Docker images, containers, volumes, networking, Docker Compose, and best practices for production deployments.',
            'price': 3499.00,
            'duration': '4 Weeks',
            'topics': [
                "Introduction to Containerization",
                "Docker Installation & Setup",
                "Docker Images & Registries",
                "Creating Custom Docker Images",
                "Dockerfile Best Practices",
                "Container Lifecycle Management",
                "Docker Volumes & Data Persistence",
                "Docker Networking Modes",
                "Docker Compose Basics",
                "Multi-Container Applications",
                "Environment Variables & Secrets",
                "Docker Security Best Practices",
                "Container Monitoring & Logs",
                "Docker Hub & Private Registries",
                "Docker in CI/CD Pipelines",
                "Production Deployment Strategies"
            ]
        },
        {
            'title': 'Kubernetes Administrator (CKA)',
            'description': 'Prepare for the CKA exam with deep dives into Kubernetes architecture and troubleshooting. This comprehensive course covers cluster setup, workload management, services & networking, storage, security, troubleshooting, and real-world scenarios.',
            'price': 5999.00,
            'duration': '8 Weeks',
            'topics': [
                "Kubernetes Architecture Overview",
                "Cluster Installation & Configuration",
                "kubectl Command Line Basics",
                "Pods, ReplicaSets & Deployments",
                "Services & Service Discovery",
                "Ingress Controllers & Rules",
                "ConfigMaps & Secrets Management",
                "Persistent Volumes & Claims",
                "Storage Classes & Dynamic Provisioning",
                "StatefulSets & DaemonSets",
                "Jobs & CronJobs",
                "Namespaces & Resource Quotas",
                "RBAC & Service Accounts",
                "Network Policies",
                "Pod Security Policies",
                "Cluster Monitoring & Logging",
                "Application Lifecycle Management",
                "Helm Package Manager",
                "Cluster Maintenance & Upgrades",
                "Backup & Disaster Recovery",
                "Troubleshooting Applications",
                "Troubleshooting Cluster Components"
            ]
        },
        {
            'title': 'Jenkins CI/CD Pipeline',
            'description': 'Build automated CI/CD pipelines with Jenkins. Learn pipeline as code, integrations with Git, Docker, Kubernetes, automated testing, deployment strategies, and production-grade pipeline implementations.',
            'price': 3999.00,
            'duration': '5 Weeks',
            'topics': [
                "Jenkins Installation & Setup",
                "Jenkins Architecture & Plugins",
                "Creating Freestyle Projects",
                "Jenkins Pipeline Basics",
                "Declarative vs Scripted Pipeline",
                "Pipeline as Code (Jenkinsfile)",
                "Source Control Integration (Git)",
                "Build Triggers & Webhooks",
                "Environment Variables & Parameters",
                "Docker Integration in Jenkins",
                "Kubernetes Deployment from Jenkins",
                "Automated Testing in Pipeline",
                "Code Quality & Security Scanning",
                "Artifact Management",
                "Multi-Branch Pipelines",
                "Pipeline Stages & Steps",
                "Email & Slack Notifications",
                "Blue-Green Deployments",
                "Canary Deployments",
                "Pipeline Best Practices"
            ]
        },
        {
            'title': 'Terraform Infrastructure as Code',
            'description': 'Master infrastructure automation with Terraform. Learn HCL syntax, state management, modules, providers for AWS/Azure/GCP, best practices, remote state, workspaces, and team collaboration workflows.',
            'price': 4499.00,
            'duration': '6 Weeks',
            'topics': [
                "Infrastructure as Code Concepts",
                "Terraform Installation & Setup",
                "HCL Syntax & Configuration",
                "Providers & Resources",
                "Variables & Outputs",
                "Data Sources",
                "State Management",
                "Remote State (S3, Azure, GCS)",
                "State Locking",
                "Modules & Module Registry",
                "Creating Reusable Modules",
                "Workspaces for Environments",
                "AWS Provider & Resources",
                "Azure Provider & Resources",
                "GCP Provider & Resources",
                "Multi-Cloud Deployments",
                "Terraform Import & State Manipulation",
                "Provisioners & Local-exec",
                "Terraform Cloud & Enterprise",
                "CI/CD Integration",
                "Security & Secrets Management",
                "Best Practices & Code Organization"
            ]
        },
        {
            'title': 'Ansible Automation',
            'description': 'Automate infrastructure configuration with Ansible. This course covers playbooks, roles, variables, templates, handlers, modules, Ansible Galaxy, best practices, and real-world automation scenarios.',
            'price': 3799.00,
            'duration': '5 Weeks',
            'topics': [
                "Ansible Architecture & Components",
                "Installation & Configuration",
                "Inventory Management",
                "Ad-hoc Commands",
                "Playbook Structure & Syntax",
                "Variables & Facts",
                "Conditionals & Loops",
                "Handlers & Notifications",
                "Templates (Jinja2)",
                "Roles & Role Structure",
                "Ansible Galaxy",
                "Common Modules (file, copy, apt, yum)",
                "User & Group Management Modules",
                "Service Management Modules",
                "Docker & Container Modules",
                "Cloud Modules (AWS, Azure)",
                "Ansible Vault for Secrets",
                "Dynamic Inventory",
                "Ansible Tower / AWX",
                "CI/CD Integration",
                "Best Practices & Optimization"
            ]
        },
        {
            'title': 'AWS Cloud Practitioner',
            'description': 'Get started with Amazon Web Services. Learn AWS fundamentals, core services (EC2, S3, RDS, VPC), IAM security, pricing models, architectural best practices, and prepare for the AWS Cloud Practitioner certification.',
            'price': 4999.00,
            'duration': '7 Weeks',
            'topics': [
                "Cloud Computing Fundamentals",
                "AWS Global Infrastructure",
                "IAM Users, Groups & Policies",
                "EC2 Instance Types & Pricing",
                "EC2 Security Groups & Key Pairs",
                "EBS Volumes & Snapshots",
                "S3 Buckets & Storage Classes",
                "S3 Security & Encryption",
                "VPC & Subnets",
                "Internet Gateway & NAT Gateway",
                "Route Tables & Network ACLs",
                "RDS Database Service",
                "DynamoDB NoSQL Database",
                "Lambda Serverless Functions",
                "CloudWatch Monitoring & Logs",
                "CloudFormation IaC",
                "Elastic Load Balancer (ALB/NLB)",
                "Auto Scaling Groups",
                "Route 53 DNS Service",
                "CloudFront CDN",
                "AWS Pricing & Cost Management",
                "Well-Architected Framework",
                "Security Best Practices",
                "AWS Support Plans"
            ]
        },
        {
            'title': 'Python for DevOps',
            'description': 'Learn Python scripting for DevOps automation. This course covers Python basics, file I/O, APIs, automation scripts, working with JSON/YAML, libraries like boto3, requests, paramiko, and building DevOps tools.',
            'price': 3299.00,
            'duration': '6 Weeks',
            'topics': [
                "Python Basics & Syntax",
                "Variables, Data Types & Operators",
                "Control Flow (if, loops)",
                "Functions & Modules",
                "File I/O Operations",
                "Exception Handling",
                "Working with JSON",
                "Working with YAML",
                "Regular Expressions",
                "OS & Subprocess Modules",
                "HTTP Requests with requests library",
                "API Integration",
                "Boto3 for AWS Automation",
                "Paramiko for SSH Automation",
                "Docker SDK for Python",
                "Kubernetes Python Client",
                "Building CLI Tools (Click, Argparse)",
                "Web Scraping Basics",
                "Database Connectivity",
                "DevOps Automation Scripts",
                "CI/CD Integration",
                "Best Practices & Code Organization"
            ]
        },
        {
            'title': 'Site Reliability Engineering (SRE)',
            'description': 'Master SRE practices and principles. Learn monitoring, alerting, incident response, SLIs/SLOs/SLAs, error budgets, chaos engineering, on-call best practices, and building reliable systems at scale.',
            'price': 5499.00,
            'duration': '8 Weeks',
            'topics': [
                "SRE Principles & Philosophy",
                "SLIs, SLOs & SLAs",
                "Error Budgets",
                "Toil Reduction Strategies",
                "Monitoring & Observability",
                "Prometheus Setup & Configuration",
                "Grafana Dashboards",
                "Alerting Best Practices",
                "Log Management (ELK Stack)",
                "Distributed Tracing",
                "Incident Management Process",
                "On-Call Rotations & Runbooks",
                "Post-Mortem Analysis",
                "Capacity Planning",
                "Load Testing & Performance",
                "Chaos Engineering Principles",
                "Fault Injection Testing",
                "High Availability Architecture",
                "Disaster Recovery Planning",
                "Backup & Restore Strategies",
                "Service Mesh (Istio)",
                "Automation & Self-Healing Systems",
                "SRE Team Structure & Culture"
            ]
        },
    ]
    
    created_count = 0
    updated_count = 0
    
    for course_data in courses_data:
        course, created = Course.objects.update_or_create(
            title=course_data['title'],
            defaults={
                'description': course_data['description'],
                'price': course_data['price'],
                'duration': course_data['duration'],
                'topics': course_data.get('topics', [])
            }
        )
        
        if created:
            created_count += 1
            print(f"✓ Created: {course.title}")
        else:
            updated_count += 1
            print(f"↻ Updated: {course.title}")
    
    print(f"\n{'='*60}")
    print(f"Course setup complete!")
    print(f"Created: {created_count} courses")
    print(f"Updated: {updated_count} courses")
    print(f"Total courses in database: {Course.objects.count()}")
    print(f"{'='*60}")

if __name__ == '__main__':
    create_courses()
    print("\n✅ All courses are now available on the home page!")
    print("🚀 Start your development server with: python manage.py runserver")
