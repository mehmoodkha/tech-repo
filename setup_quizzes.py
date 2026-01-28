"""
Script to populate quiz questions for the 9 topics (Linux, Cloud, Docker, Ansible, Terraform, Jenkins, DevOps, SRE, Python)
Each topic has 3 difficulty levels: Basic, Intermediate, Advanced
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devops_nexus.settings')
django.setup()

from courses.models import Quiz, Question

def create_quizzes_and_questions():
    """Create quizzes with sample questions for all topics and difficulty levels"""
    
    quiz_data = {
        'LINUX': {
            'BASIC': {
                'title': 'Linux Basics',
                'description': 'Test your basic Linux knowledge',
                'questions': [
                    {'q': 'What command is used to list files in a directory?', 'a': 'ls'},
                    {'q': 'What command is used to change directory?', 'a': 'cd'},
                    {'q': 'What command is used to print working directory?', 'a': 'pwd'},
                    {'q': 'What command creates a new directory?', 'a': 'mkdir'},
                    {'q': 'What command removes a file?', 'a': 'rm'},
                ]
            },
            'INTERMEDIATE': {
                'title': 'Linux Intermediate',
                'description': 'Test your intermediate Linux skills',
                'questions': [
                    {'q': 'What command finds files by name?', 'a': 'find'},
                    {'q': 'What command searches text patterns in files?', 'a': 'grep'},
                    {'q': 'What command changes file permissions?', 'a': 'chmod'},
                    {'q': 'What command shows running processes?', 'a': 'ps'},
                    {'q': 'What command displays disk usage?', 'a': 'df'},
                ]
            },
            'ADVANCED': {
                'title': 'Linux Advanced',
                'description': 'Test your advanced Linux expertise',
                'questions': [
                    {'q': 'What command creates a symbolic link?', 'a': 'ln -s'},
                    {'q': 'What command monitors system calls?', 'a': 'strace'},
                    {'q': 'What command displays SELinux context?', 'a': 'ls -Z'},
                    {'q': 'What command manages kernel modules?', 'a': 'modprobe'},
                    {'q': 'What command shows open files by process?', 'a': 'lsof'},
                ]
            }
        },
        'CLOUD': {
            'BASIC': {
                'title': 'Cloud Computing Basics',
                'description': 'Fundamental cloud concepts',
                'questions': [
                    {'q': 'What does IaaS stand for?', 'a': 'Infrastructure as a Service'},
                    {'q': 'What does PaaS stand for?', 'a': 'Platform as a Service'},
                    {'q': 'What does SaaS stand for?', 'a': 'Software as a Service'},
                    {'q': 'Name a major cloud provider starting with A', 'a': 'AWS'},
                    {'q': 'What is cloud storage service in AWS?', 'a': 'S3'},
                ]
            },
            'INTERMEDIATE': {
                'title': 'Cloud Computing Intermediate',
                'description': 'Cloud architecture and services',
                'questions': [
                    {'q': 'What AWS service provides virtual servers?', 'a': 'EC2'},
                    {'q': 'What AWS service is used for DNS?', 'a': 'Route 53'},
                    {'q': 'What Azure service is equivalent to EC2?', 'a': 'Virtual Machines'},
                    {'q': 'What is GCP compute service called?', 'a': 'Compute Engine'},
                    {'q': 'What AWS service provides managed databases?', 'a': 'RDS'},
                ]
            },
            'ADVANCED': {
                'title': 'Cloud Computing Advanced',
                'description': 'Advanced cloud architecture',
                'questions': [
                    {'q': 'What AWS service provides serverless computing?', 'a': 'Lambda'},
                    {'q': 'What is AWS container orchestration service?', 'a': 'ECS'},
                    {'q': 'What Azure service manages Kubernetes?', 'a': 'AKS'},
                    {'q': 'What GCP service is for serverless?', 'a': 'Cloud Functions'},
                    {'q': 'What AWS service provides CDN?', 'a': 'CloudFront'},
                ]
            }
        },
        'DOCKER': {
            'BASIC': {
                'title': 'Docker Basics',
                'description': 'Docker fundamentals',
                'questions': [
                    {'q': 'What command builds a Docker image?', 'a': 'docker build'},
                    {'q': 'What command runs a Docker container?', 'a': 'docker run'},
                    {'q': 'What command lists running containers?', 'a': 'docker ps'},
                    {'q': 'What file defines Docker image build steps?', 'a': 'Dockerfile'},
                    {'q': 'What command pulls an image from registry?', 'a': 'docker pull'},
                ]
            },
            'INTERMEDIATE': {
                'title': 'Docker Intermediate',
                'description': 'Docker networking and volumes',
                'questions': [
                    {'q': 'What command creates a Docker volume?', 'a': 'docker volume create'},
                    {'q': 'What command creates a Docker network?', 'a': 'docker network create'},
                    {'q': 'What command shows Docker container logs?', 'a': 'docker logs'},
                    {'q': 'What command executes command in running container?', 'a': 'docker exec'},
                    {'q': 'What command removes stopped containers?', 'a': 'docker container prune'},
                ]
            },
            'ADVANCED': {
                'title': 'Docker Advanced',
                'description': 'Multi-stage builds and optimization',
                'questions': [
                    {'q': 'What is Docker multi-stage build keyword?', 'a': 'FROM'},
                    {'q': 'What command saves container as image?', 'a': 'docker commit'},
                    {'q': 'What tool manages multi-container apps?', 'a': 'docker-compose'},
                    {'q': 'What is Docker overlay storage driver?', 'a': 'overlay2'},
                    {'q': 'What command inspects Docker objects?', 'a': 'docker inspect'},
                ]
            }
        },
        'ANSIBLE': {
            'BASIC': {
                'title': 'Ansible Basics',
                'description': 'Ansible fundamentals',
                'questions': [
                    {'q': 'What file format does Ansible use for playbooks?', 'a': 'YAML'},
                    {'q': 'What is an Ansible playbook?', 'a': 'Automation script'},
                    {'q': 'What command runs Ansible playbook?', 'a': 'ansible-playbook'},
                    {'q': 'What file lists Ansible hosts?', 'a': 'inventory'},
                    {'q': 'What is smallest unit of Ansible?', 'a': 'task'},
                ]
            },
            'INTERMEDIATE': {
                'title': 'Ansible Intermediate',
                'description': 'Roles and variables',
                'questions': [
                    {'q': 'What is reusable Ansible code called?', 'a': 'role'},
                    {'q': 'What command checks playbook syntax?', 'a': 'ansible-playbook --syntax-check'},
                    {'q': 'What are Ansible facts?', 'a': 'System information'},
                    {'q': 'What module copies files to remote hosts?', 'a': 'copy'},
                    {'q': 'What module manages services?', 'a': 'service'},
                ]
            },
            'ADVANCED': {
                'title': 'Ansible Advanced',
                'description': 'Advanced Ansible patterns',
                'questions': [
                    {'q': 'What is Ansible Vault used for?', 'a': 'Encryption'},
                    {'q': 'What are Ansible handlers?', 'a': 'Triggered tasks'},
                    {'q': 'What is dynamic inventory?', 'a': 'Runtime inventory'},
                    {'q': 'What module runs arbitrary commands?', 'a': 'command'},
                    {'q': 'What is Ansible Galaxy?', 'a': 'Role repository'},
                ]
            }
        },
        'TERRAFORM': {
            'BASIC': {
                'title': 'Terraform Basics',
                'description': 'Infrastructure as Code basics',
                'questions': [
                    {'q': 'What language does Terraform use?', 'a': 'HCL'},
                    {'q': 'What command initializes Terraform?', 'a': 'terraform init'},
                    {'q': 'What command applies Terraform changes?', 'a': 'terraform apply'},
                    {'q': 'What command shows execution plan?', 'a': 'terraform plan'},
                    {'q': 'What file extension for Terraform files?', 'a': '.tf'},
                ]
            },
            'INTERMEDIATE': {
                'title': 'Terraform Intermediate',
                'description': 'Terraform state and modules',
                'questions': [
                    {'q': 'What stores Terraform resource state?', 'a': 'state file'},
                    {'q': 'What are reusable Terraform configurations?', 'a': 'modules'},
                    {'q': 'What command destroys resources?', 'a': 'terraform destroy'},
                    {'q': 'What command validates configuration?', 'a': 'terraform validate'},
                    {'q': 'What command formats code?', 'a': 'terraform fmt'},
                ]
            },
            'ADVANCED': {
                'title': 'Terraform Advanced',
                'description': 'Advanced Terraform concepts',
                'questions': [
                    {'q': 'What enables remote state storage?', 'a': 'backend'},
                    {'q': 'What manages resource dependencies?', 'a': 'depends_on'},
                    {'q': 'What creates multiple similar resources?', 'a': 'count'},
                    {'q': 'What is Terraform workspace?', 'a': 'Environment isolation'},
                    {'q': 'What imports existing resources?', 'a': 'terraform import'},
                ]
            }
        },
        'JENKINS': {
            'BASIC': {
                'title': 'Jenkins Basics',
                'description': 'CI/CD with Jenkins',
                'questions': [
                    {'q': 'What is Jenkins used for?', 'a': 'CI/CD'},
                    {'q': 'What is Jenkins job?', 'a': 'Automated task'},
                    {'q': 'What file defines Jenkins pipeline?', 'a': 'Jenkinsfile'},
                    {'q': 'What extends Jenkins functionality?', 'a': 'plugins'},
                    {'q': 'What triggers Jenkins build?', 'a': 'webhook'},
                ]
            },
            'INTERMEDIATE': {
                'title': 'Jenkins Intermediate',
                'description': 'Pipelines and automation',
                'questions': [
                    {'q': 'What are two types of Jenkins pipeline?', 'a': 'Declarative and Scripted'},
                    {'q': 'What keyword starts declarative pipeline?', 'a': 'pipeline'},
                    {'q': 'What is Jenkins agent?', 'a': 'Build executor'},
                    {'q': 'What are Jenkins stages?', 'a': 'Pipeline phases'},
                    {'q': 'What stores Jenkins credentials?', 'a': 'Credentials plugin'},
                ]
            },
            'ADVANCED': {
                'title': 'Jenkins Advanced',
                'description': 'Advanced Jenkins patterns',
                'questions': [
                    {'q': 'What is Jenkins shared library?', 'a': 'Reusable code'},
                    {'q': 'What is Blue Ocean?', 'a': 'Modern UI'},
                    {'q': 'What is multibranch pipeline?', 'a': 'Branch-based jobs'},
                    {'q': 'What is Jenkins master-slave architecture?', 'a': 'Distributed builds'},
                    {'q': 'What backs up Jenkins config?', 'a': 'Configuration as Code'},
                ]
            }
        },
        'DEVOPS': {
            'BASIC': {
                'title': 'DevOps Basics',
                'description': 'DevOps fundamentals',
                'questions': [
                    {'q': 'What does DevOps combine?', 'a': 'Development and Operations'},
                    {'q': 'What is CI?', 'a': 'Continuous Integration'},
                    {'q': 'What is CD?', 'a': 'Continuous Delivery'},
                    {'q': 'What is version control system?', 'a': 'Git'},
                    {'q': 'What is container technology?', 'a': 'Docker'},
                ]
            },
            'INTERMEDIATE': {
                'title': 'DevOps Intermediate',
                'description': 'DevOps practices',
                'questions': [
                    {'q': 'What is infrastructure as code?', 'a': 'IaC'},
                    {'q': 'What is blue-green deployment?', 'a': 'Zero downtime deployment'},
                    {'q': 'What is canary deployment?', 'a': 'Gradual rollout'},
                    {'q': 'What monitors applications?', 'a': 'Observability tools'},
                    {'q': 'What is GitOps?', 'a': 'Git-based operations'},
                ]
            },
            'ADVANCED': {
                'title': 'DevOps Advanced',
                'description': 'Advanced DevOps concepts',
                'questions': [
                    {'q': 'What is service mesh?', 'a': 'Network layer'},
                    {'q': 'What is chaos engineering?', 'a': 'Resilience testing'},
                    {'q': 'What is shift-left testing?', 'a': 'Early testing'},
                    {'q': 'What is immutable infrastructure?', 'a': 'Replace not modify'},
                    {'q': 'What are the three ways of DevOps?', 'a': 'Flow, Feedback, Learning'},
                ]
            }
        },
        'SRE': {
            'BASIC': {
                'title': 'SRE Basics',
                'description': 'Site Reliability Engineering basics',
                'questions': [
                    {'q': 'What does SRE stand for?', 'a': 'Site Reliability Engineering'},
                    {'q': 'What is SLI?', 'a': 'Service Level Indicator'},
                    {'q': 'What is SLO?', 'a': 'Service Level Objective'},
                    {'q': 'What is SLA?', 'a': 'Service Level Agreement'},
                    {'q': 'What measures system uptime?', 'a': 'Availability'},
                ]
            },
            'INTERMEDIATE': {
                'title': 'SRE Intermediate',
                'description': 'SRE practices',
                'questions': [
                    {'q': 'What is error budget?', 'a': 'Allowed downtime'},
                    {'q': 'What is toil in SRE?', 'a': 'Manual work'},
                    {'q': 'What is on-call rotation?', 'a': 'Support schedule'},
                    {'q': 'What is incident response?', 'a': 'Problem handling'},
                    {'q': 'What is postmortem?', 'a': 'Incident review'},
                ]
            },
            'ADVANCED': {
                'title': 'SRE Advanced',
                'description': 'Advanced SRE concepts',
                'questions': [
                    {'q': 'What is canary analysis?', 'a': 'Deployment validation'},
                    {'q': 'What is capacity planning?', 'a': 'Resource forecasting'},
                    {'q': 'What reduces toil?', 'a': 'Automation'},
                    {'q': 'What is cascading failure?', 'a': 'Domino effect'},
                    {'q': 'What is the golden signals?', 'a': 'Latency, Traffic, Errors, Saturation'},
                ]
            }
        },
        'PYTHON': {
            'BASIC': {
                'title': 'Python Basics',
                'description': 'Python programming basics',
                'questions': [
                    {'q': 'What prints output in Python?', 'a': 'print()'},
                    {'q': 'What is Python list syntax?', 'a': '[]'},
                    {'q': 'What is Python dictionary syntax?', 'a': '{}'},
                    {'q': 'What keyword defines function?', 'a': 'def'},
                    {'q': 'What keyword creates loop?', 'a': 'for'},
                ]
            },
            'INTERMEDIATE': {
                'title': 'Python Intermediate',
                'description': 'Python OOP and modules',
                'questions': [
                    {'q': 'What keyword defines class?', 'a': 'class'},
                    {'q': 'What is self in Python?', 'a': 'Instance reference'},
                    {'q': 'What imports module?', 'a': 'import'},
                    {'q': 'What handles exceptions?', 'a': 'try-except'},
                    {'q': 'What is list comprehension?', 'a': 'Compact list creation'},
                ]
            },
            'ADVANCED': {
                'title': 'Python Advanced',
                'description': 'Advanced Python concepts',
                'questions': [
                    {'q': 'What are Python decorators?', 'a': 'Function wrappers'},
                    {'q': 'What is generator in Python?', 'a': 'Lazy iterator'},
                    {'q': 'What is asyncio used for?', 'a': 'Asynchronous programming'},
                    {'q': 'What is context manager?', 'a': 'Resource management'},
                    {'q': 'What is metaclass?', 'a': 'Class creator'},
                ]
            }
        }
    }
    
    print("Creating quizzes and questions...")
    
    for topic_code, difficulties in quiz_data.items():
        for difficulty_code, data in difficulties.items():
            # Create or get quiz
            quiz, created = Quiz.objects.get_or_create(
                topic=topic_code,
                difficulty=difficulty_code,
                defaults={
                    'title': data['title'],
                    'description': data['description'],
                    'is_active': True
                }
            )
            
            if created:
                print(f"✓ Created quiz: {quiz}")
                
                # Create questions
                for idx, q_data in enumerate(data['questions'], 1):
                    Question.objects.create(
                        quiz=quiz,
                        question_text=q_data['q'],
                        answer=q_data['a'],
                        order=idx,
                        is_active=True
                    )
                print(f"  Added {len(data['questions'])} questions")
            else:
                print(f"- Quiz already exists: {quiz}")
    
    print("\n✅ Quiz setup complete!")
    print(f"Total quizzes: {Quiz.objects.count()}")
    print(f"Total questions: {Question.objects.count()}")

if __name__ == '__main__':
    create_quizzes_and_questions()
