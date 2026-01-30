#!/usr/bin/env python
"""
Update DevOps Full Course with topics
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devops_nexus.settings')
django.setup()

from courses.models import Course

# Get the DevOps Full Course
course = Course.objects.get(id=1)

# Add comprehensive topics
course.topics = [
    'Linux Fundamentals & Command Line',
    'File System Management & Permissions',
    'User & Group Administration',
    'Package Management & Software Installation',
    'Process Management & System Monitoring',
    'Shell Scripting & Automation Basics',
    'Networking Fundamentals (TCP/IP, DNS, HTTP)',
    'SSH & Remote System Access',
    'Version Control with Git & GitHub',
    'Git Branching Strategies & Workflows',
    'Introduction to CI/CD Concepts',
    'Jenkins Installation & Configuration',
    'Building CI/CD Pipelines with Jenkins',
    'Docker Fundamentals & Containerization',
    'Docker Images, Containers & Registries',
    'Docker Compose & Multi-Container Applications',
    'Kubernetes Architecture & Components',
    'Deploying Applications on Kubernetes',
    'Kubernetes Services, Ingress & Networking',
    'Configuration Management with Ansible',
    'Ansible Playbooks & Roles',
    'Infrastructure as Code with Terraform',
    'Terraform Providers & State Management',
    'AWS Cloud Services & EC2 Instances',
    'Cloud Storage Solutions (S3, EBS)',
    'Monitoring & Logging with Prometheus & Grafana',
    'Application Performance Monitoring',
    'Security Best Practices in DevOps',
    'DevOps Culture & Collaboration',
    'Final Project: Complete CI/CD Pipeline'
]

course.save()

print(f'✅ Updated {course.title} with {len(course.topics)} topics:')
print('-' * 60)
for i, topic in enumerate(course.topics, 1):
    print(f'{i}. {topic}')
print('-' * 60)
print(f'Course: {course.title}')
print(f'Duration: {course.duration}')
print(f'Total Topics: {len(course.topics)}')
