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
            'duration': '12 Weeks'
        },
        {
            'title': 'DevOps Pre-Requisite',
            'description': 'Master the basics of Linux, Networking, and Git before diving into complex tools. This comprehensive course covers essential command-line skills, file system management, bash scripting, networking fundamentals, and version control with Git.',
            'price': 2999.00,
            'duration': '6 Weeks'
        },
        {
            'title': 'Docker for Beginners',
            'description': 'Learn how to build, ship, and run applications using containers. This hands-on course covers Docker basics, containerization concepts, Docker images, containers, volumes, networking, Docker Compose, and best practices for production deployments.',
            'price': 3499.00,
            'duration': '4 Weeks'
        },
        {
            'title': 'Kubernetes Administrator (CKA)',
            'description': 'Prepare for the CKA exam with deep dives into Kubernetes architecture and troubleshooting. This comprehensive course covers cluster setup, workload management, services & networking, storage, security, troubleshooting, and real-world scenarios.',
            'price': 5999.00,
            'duration': '8 Weeks'
        },
        {
            'title': 'Jenkins CI/CD Pipeline',
            'description': 'Build automated CI/CD pipelines with Jenkins. Learn pipeline as code, integrations with Git, Docker, Kubernetes, automated testing, deployment strategies, and production-grade pipeline implementations.',
            'price': 3999.00,
            'duration': '5 Weeks'
        },
        {
            'title': 'Terraform Infrastructure as Code',
            'description': 'Master infrastructure automation with Terraform. Learn HCL syntax, state management, modules, providers for AWS/Azure/GCP, best practices, remote state, workspaces, and team collaboration workflows.',
            'price': 4499.00,
            'duration': '6 Weeks'
        },
        {
            'title': 'Ansible Automation',
            'description': 'Automate infrastructure configuration with Ansible. This course covers playbooks, roles, variables, templates, handlers, modules, Ansible Galaxy, best practices, and real-world automation scenarios.',
            'price': 3799.00,
            'duration': '5 Weeks'
        },
        {
            'title': 'AWS Cloud Practitioner',
            'description': 'Get started with Amazon Web Services. Learn AWS fundamentals, core services (EC2, S3, RDS, VPC), IAM security, pricing models, architectural best practices, and prepare for the AWS Cloud Practitioner certification.',
            'price': 4999.00,
            'duration': '7 Weeks'
        },
        {
            'title': 'Python for DevOps',
            'description': 'Learn Python scripting for DevOps automation. This course covers Python basics, file I/O, APIs, automation scripts, working with JSON/YAML, libraries like boto3, requests, paramiko, and building DevOps tools.',
            'price': 3299.00,
            'duration': '6 Weeks'
        },
        {
            'title': 'Site Reliability Engineering (SRE)',
            'description': 'Master SRE practices and principles. Learn monitoring, alerting, incident response, SLIs/SLOs/SLAs, error budgets, chaos engineering, on-call best practices, and building reliable systems at scale.',
            'price': 5499.00,
            'duration': '8 Weeks'
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
                'duration': course_data['duration']
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
