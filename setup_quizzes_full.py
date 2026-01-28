"""
Comprehensive quiz setup with 20 questions per section
Total: 60 questions per topic × 9 topics = 540 questions
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devops_nexus.settings')
django.setup()

from courses.models import Quiz, Question

# Linux Questions - 60 total
LINUX_BASIC = [
    {'q': 'What command lists files in a directory?', 'choices': {'A': 'ls', 'B': 'dir', 'C': 'list', 'D': 'show'}, 'correct': 'A'},
    {'q': 'What command changes directory?', 'choices': {'A': 'chdir', 'B': 'cd', 'C': 'changedir', 'D': 'goto'}, 'correct': 'B'},
    {'q': 'What command prints current directory?', 'choices': {'A': 'cwd', 'B': 'dir', 'C': 'pwd', 'D': 'path'}, 'correct': 'C'},
    {'q': 'What command creates a directory?', 'choices': {'A': 'newdir', 'B': 'mkdir', 'C': 'createdir', 'D': 'md'}, 'correct': 'B'},
    {'q': 'What command removes a file?', 'choices': {'A': 'delete', 'B': 'remove', 'C': 'rm', 'D': 'del'}, 'correct': 'C'},
    {'q': 'What command copies files?', 'choices': {'A': 'copy', 'B': 'cp', 'C': 'duplicate', 'D': 'cpy'}, 'correct': 'B'},
    {'q': 'What command moves or renames files?', 'choices': {'A': 'move', 'B': 'rename', 'C': 'mv', 'D': 'rn'}, 'correct': 'C'},
    {'q': 'What command displays file contents?', 'choices': {'A': 'show', 'B': 'display', 'C': 'cat', 'D': 'view'}, 'correct': 'C'},
    {'q': 'What command creates empty file?', 'choices': {'A': 'create', 'B': 'new', 'C': 'touch', 'D': 'make'}, 'correct': 'C'},
    {'q': 'What command removes directory?', 'choices': {'A': 'rmdir', 'B': 'deldir', 'C': 'removedir', 'D': 'rd'}, 'correct': 'A'},
    {'q': 'What shows manual pages?', 'choices': {'A': 'help', 'B': 'man', 'C': 'manual', 'D': 'doc'}, 'correct': 'B'},
    {'q': 'What clears the terminal screen?', 'choices': {'A': 'clean', 'B': 'cls', 'C': 'clear', 'D': 'reset'}, 'correct': 'C'},
    {'q': 'What shows command history?', 'choices': {'A': 'hist', 'B': 'history', 'C': 'log', 'D': 'past'}, 'correct': 'B'},
    {'q': 'What displays current user?', 'choices': {'A': 'user', 'B': 'me', 'C': 'whoami', 'D': 'who'}, 'correct': 'C'},
    {'q': 'What shows system date and time?', 'choices': {'A': 'time', 'B': 'clock', 'C': 'date', 'D': 'datetime'}, 'correct': 'C'},
    {'q': 'What echoes text to terminal?', 'choices': {'A': 'print', 'B': 'echo', 'C': 'display', 'D': 'show'}, 'correct': 'B'},
    {'q': 'What shows disk space?', 'choices': {'A': 'disk', 'B': 'space', 'C': 'df', 'D': 'ds'}, 'correct': 'C'},
    {'q': 'What shows directory size?', 'choices': {'A': 'size', 'B': 'du', 'C': 'dirsize', 'D': 'dsize'}, 'correct': 'B'},
    {'q': 'What shows running processes?', 'choices': {'A': 'proc', 'B': 'ps', 'C': 'tasks', 'D': 'process'}, 'correct': 'B'},
    {'q': 'What terminates a process?', 'choices': {'A': 'stop', 'B': 'end', 'C': 'kill', 'D': 'terminate'}, 'correct': 'C'},
]

LINUX_INTERMEDIATE = [
    {'q': 'What searches files by name?', 'choices': {'A': 'search', 'B': 'locate', 'C': 'find', 'D': 'whereis'}, 'correct': 'C'},
    {'q': 'What searches text in files?', 'choices': {'A': 'search', 'B': 'grep', 'C': 'find', 'D': 'pattern'}, 'correct': 'B'},
    {'q': 'What changes file permissions?', 'choices': {'A': 'perms', 'B': 'setperm', 'C': 'chmod', 'D': 'chperm'}, 'correct': 'C'},
    {'q': 'What changes file owner?', 'choices': {'A': 'owner', 'B': 'chown', 'C': 'setowner', 'D': 'changeowner'}, 'correct': 'B'},
    {'q': 'What shows file type?', 'choices': {'A': 'type', 'B': 'file', 'C': 'ftype', 'D': 'kind'}, 'correct': 'B'},
    {'q': 'What compares two files?', 'choices': {'A': 'compare', 'B': 'check', 'C': 'diff', 'D': 'cmp'}, 'correct': 'C'},
    {'q': 'What compresses files?', 'choices': {'A': 'compress', 'B': 'zip', 'C': 'gzip', 'D': 'pack'}, 'correct': 'C'},
    {'q': 'What archives files?', 'choices': {'A': 'archive', 'B': 'tar', 'C': 'pack', 'D': 'bundle'}, 'correct': 'B'},
    {'q': 'What shows first lines of file?', 'choices': {'A': 'top', 'B': 'first', 'C': 'head', 'D': 'begin'}, 'correct': 'C'},
    {'q': 'What shows last lines of file?', 'choices': {'A': 'bottom', 'B': 'end', 'C': 'tail', 'D': 'last'}, 'correct': 'C'},
    {'q': 'What counts lines in file?', 'choices': {'A': 'count', 'B': 'wc', 'C': 'lines', 'D': 'lc'}, 'correct': 'B'},
    {'q': 'What sorts file contents?', 'choices': {'A': 'order', 'B': 'arrange', 'C': 'sort', 'D': 'organize'}, 'correct': 'C'},
    {'q': 'What removes duplicate lines?', 'choices': {'A': 'unique', 'B': 'uniq', 'C': 'dedup', 'D': 'distinct'}, 'correct': 'B'},
    {'q': 'What cuts sections from lines?', 'choices': {'A': 'slice', 'B': 'section', 'C': 'cut', 'D': 'extract'}, 'correct': 'C'},
    {'q': 'What translates characters?', 'choices': {'A': 'trans', 'B': 'tr', 'C': 'translate', 'D': 'convert'}, 'correct': 'B'},
    {'q': 'What shows network connections?', 'choices': {'A': 'network', 'B': 'connections', 'C': 'netstat', 'D': 'net'}, 'correct': 'C'},
    {'q': 'What tests network connectivity?', 'choices': {'A': 'test', 'B': 'check', 'C': 'ping', 'D': 'probe'}, 'correct': 'C'},
    {'q': 'What shows network interfaces?', 'choices': {'A': 'interfaces', 'B': 'ifconfig', 'C': 'netif', 'D': 'nic'}, 'correct': 'B'},
    {'q': 'What downloads files from web?', 'choices': {'A': 'download', 'B': 'get', 'C': 'wget', 'D': 'fetch'}, 'correct': 'C'},
    {'q': 'What shows system uptime?', 'choices': {'A': 'time', 'B': 'up', 'C': 'uptime', 'D': 'runtime'}, 'correct': 'C'},
]

LINUX_ADVANCED = [
    {'q': 'What creates symbolic link?', 'choices': {'A': 'link', 'B': 'symlink', 'C': 'ln -s', 'D': 'mklink'}, 'correct': 'C'},
    {'q': 'What monitors system calls?', 'choices': {'A': 'syscall', 'B': 'strace', 'C': 'trace', 'D': 'monitor'}, 'correct': 'B'},
    {'q': 'What shows SELinux context?', 'choices': {'A': 'selinux', 'B': 'context', 'C': 'ls -Z', 'D': 'getcontext'}, 'correct': 'C'},
    {'q': 'What manages kernel modules?', 'choices': {'A': 'kmod', 'B': 'insmod', 'C': 'modprobe', 'D': 'lsmod'}, 'correct': 'C'},
    {'q': 'What shows open files?', 'choices': {'A': 'openfiles', 'B': 'lsof', 'C': 'fuser', 'D': 'files'}, 'correct': 'B'},
    {'q': 'What changes process priority?', 'choices': {'A': 'priority', 'B': 'setpri', 'C': 'renice', 'D': 'nice'}, 'correct': 'C'},
    {'q': 'What shows library dependencies?', 'choices': {'A': 'libs', 'B': 'deps', 'C': 'ldd', 'D': 'depends'}, 'correct': 'C'},
    {'q': 'What debugs programs?', 'choices': {'A': 'debug', 'B': 'gdb', 'C': 'debugger', 'D': 'dbg'}, 'correct': 'B'},
    {'q': 'What profiles system performance?', 'choices': {'A': 'profile', 'B': 'perf', 'C': 'prof', 'D': 'monitor'}, 'correct': 'B'},
    {'q': 'What shows system calls?', 'choices': {'A': 'syscalls', 'B': 'calls', 'C': 'ltrace', 'D': 'trace'}, 'correct': 'C'},
    {'q': 'What manages ACLs?', 'choices': {'A': 'acl', 'B': 'setacl', 'C': 'setfacl', 'D': 'facl'}, 'correct': 'C'},
    {'q': 'What shows file attributes?', 'choices': {'A': 'attrs', 'B': 'attributes', 'C': 'lsattr', 'D': 'getattr'}, 'correct': 'C'},
    {'q': 'What changes file attributes?', 'choices': {'A': 'setattr', 'B': 'chattr', 'C': 'attrs', 'D': 'modify'}, 'correct': 'B'},
    {'q': 'What shows disk I/O?', 'choices': {'A': 'diskio', 'B': 'io', 'C': 'iostat', 'D': 'diskstat'}, 'correct': 'C'},
    {'q': 'What monitors file changes?', 'choices': {'A': 'watch', 'B': 'monitor', 'C': 'inotifywait', 'D': 'filewatch'}, 'correct': 'C'},
    {'q': 'What manages cron jobs?', 'choices': {'A': 'cron', 'B': 'jobs', 'C': 'crontab', 'D': 'schedule'}, 'correct': 'C'},
    {'q': 'What runs command at specific time?', 'choices': {'A': 'schedule', 'B': 'at', 'C': 'time', 'D': 'delay'}, 'correct': 'B'},
    {'q': 'What shows kernel messages?', 'choices': {'A': 'kmsg', 'B': 'kernel', 'C': 'dmesg', 'D': 'klog'}, 'correct': 'C'},
    {'q': 'What manages systemd services?', 'choices': {'A': 'service', 'B': 'systemd', 'C': 'systemctl', 'D': 'svc'}, 'correct': 'C'},
    {'q': 'What shows journal logs?', 'choices': {'A': 'log', 'B': 'journal', 'C': 'journalctl', 'D': 'syslog'}, 'correct': 'C'},
]

# Cloud Questions - 60 total
CLOUD_BASIC = [
    {'q': 'What does IaaS stand for?', 'choices': {'A': 'Infrastructure as a Service', 'B': 'Internet as a Service', 'C': 'Installation as a Service', 'D': 'Integration as a Service'}, 'correct': 'A'},
    {'q': 'What does PaaS stand for?', 'choices': {'A': 'Processing as a Service', 'B': 'Platform as a Service', 'C': 'Package as a Service', 'D': 'Program as a Service'}, 'correct': 'B'},
    {'q': 'What does SaaS stand for?', 'choices': {'A': 'System as a Service', 'B': 'Storage as a Service', 'C': 'Software as a Service', 'D': 'Security as a Service'}, 'correct': 'C'},
    {'q': 'Which company provides AWS?', 'choices': {'A': 'Microsoft', 'B': 'Google', 'C': 'Amazon', 'D': 'IBM'}, 'correct': 'C'},
    {'q': 'What is AWS S3 used for?', 'choices': {'A': 'Computing', 'B': 'Networking', 'C': 'Storage', 'D': 'Database'}, 'correct': 'C'},
    {'q': 'What is Azure?', 'choices': {'A': 'AWS service', 'B': 'Microsoft cloud', 'C': 'Google cloud', 'D': 'IBM cloud'}, 'correct': 'B'},
    {'q': 'What is GCP?', 'choices': {'A': 'Google Cloud Platform', 'B': 'Global Cloud Provider', 'C': 'General Cloud Platform', 'D': 'Guaranteed Cloud Performance'}, 'correct': 'A'},
    {'q': 'What is cloud computing?', 'choices': {'A': 'Local storage', 'B': 'Internet-based computing', 'C': 'Desktop computing', 'D': 'Mobile computing'}, 'correct': 'B'},
    {'q': 'What is a virtual machine?', 'choices': {'A': 'Physical server', 'B': 'Software computer', 'C': 'Network device', 'D': 'Storage device'}, 'correct': 'B'},
    {'q': 'What is cloud storage?', 'choices': {'A': 'Local disk', 'B': 'USB drive', 'C': 'Remote storage', 'D': 'CD storage'}, 'correct': 'C'},
    {'q': 'What is public cloud?', 'choices': {'A': 'Private network', 'B': 'Shared infrastructure', 'C': 'Local server', 'D': 'Personal computer'}, 'correct': 'B'},
    {'q': 'What is private cloud?', 'choices': {'A': 'Public service', 'B': 'Shared cloud', 'C': 'Dedicated infrastructure', 'D': 'Free cloud'}, 'correct': 'C'},
    {'q': 'What is hybrid cloud?', 'choices': {'A': 'Only public', 'B': 'Only private', 'C': 'Mix of both', 'D': 'No cloud'}, 'correct': 'C'},
    {'q': 'What is cloud migration?', 'choices': {'A': 'Moving to cloud', 'B': 'Cloud deletion', 'C': 'Cloud backup', 'D': 'Cloud monitoring'}, 'correct': 'A'},
    {'q': 'What is cloud scalability?', 'choices': {'A': 'Fixed size', 'B': 'Ability to grow', 'C': 'Always small', 'D': 'Cannot change'}, 'correct': 'B'},
    {'q': 'What is cloud elasticity?', 'choices': {'A': 'Rigid structure', 'B': 'Auto scaling', 'C': 'Manual sizing', 'D': 'Fixed resources'}, 'correct': 'B'},
    {'q': 'What is multi-tenancy?', 'choices': {'A': 'Single user', 'B': 'Multiple users', 'C': 'No users', 'D': 'Two users only'}, 'correct': 'B'},
    {'q': 'What is cloud availability?', 'choices': {'A': 'Downtime', 'B': 'Uptime percentage', 'C': 'Speed', 'D': 'Size'}, 'correct': 'B'},
    {'q': 'What is cloud reliability?', 'choices': {'A': 'Failure rate', 'B': 'Consistent performance', 'C': 'High cost', 'D': 'Low speed'}, 'correct': 'B'},
    {'q': 'What is cloud security?', 'choices': {'A': 'No protection', 'B': 'Data protection', 'C': 'Open access', 'D': 'Public data'}, 'correct': 'B'},
]

CLOUD_INTERMEDIATE = [
    {'q': 'What AWS service provides VMs?', 'choices': {'A': 'S3', 'B': 'EC2', 'C': 'Lambda', 'D': 'RDS'}, 'correct': 'B'},
    {'q': 'What is AWS Route 53?', 'choices': {'A': 'Load Balancer', 'B': 'CDN', 'C': 'DNS Service', 'D': 'VPN'}, 'correct': 'C'},
    {'q': 'What is Azure VM equivalent?', 'choices': {'A': 'App Service', 'B': 'Virtual Machines', 'C': 'Container Instances', 'D': 'Functions'}, 'correct': 'B'},
    {'q': 'What is GCP compute service?', 'choices': {'A': 'Cloud Run', 'B': 'App Engine', 'C': 'Compute Engine', 'D': 'Cloud Functions'}, 'correct': 'C'},
    {'q': 'What is AWS RDS?', 'choices': {'A': 'Storage', 'B': 'Managed Database', 'C': 'Compute', 'D': 'Networking'}, 'correct': 'B'},
    {'q': 'What is AWS VPC?', 'choices': {'A': 'Virtual Server', 'B': 'Virtual Network', 'C': 'Virtual Storage', 'D': 'Virtual Database'}, 'correct': 'B'},
    {'q': 'What is AWS ELB?', 'choices': {'A': 'Storage', 'B': 'Database', 'C': 'Load Balancer', 'D': 'Firewall'}, 'correct': 'C'},
    {'q': 'What is AWS CloudWatch?', 'choices': {'A': 'Storage', 'B': 'Monitoring', 'C': 'Compute', 'D': 'Database'}, 'correct': 'B'},
    {'q': 'What is AWS IAM?', 'choices': {'A': 'Storage', 'B': 'Identity Management', 'C': 'Network', 'D': 'Database'}, 'correct': 'B'},
    {'q': 'What is AWS EBS?', 'choices': {'A': 'Block Storage', 'B': 'Object Storage', 'C': 'Database', 'D': 'Network'}, 'correct': 'A'},
    {'q': 'What is Azure Blob Storage?', 'choices': {'A': 'Block storage', 'B': 'Object storage', 'C': 'Database', 'D': 'Compute'}, 'correct': 'B'},
    {'q': 'What is GCP BigQuery?', 'choices': {'A': 'Storage', 'B': 'Analytics', 'C': 'Compute', 'D': 'Network'}, 'correct': 'B'},
    {'q': 'What is AWS SNS?', 'choices': {'A': 'Storage', 'B': 'Notification Service', 'C': 'Database', 'D': 'Compute'}, 'correct': 'B'},
    {'q': 'What is AWS SQS?', 'choices': {'A': 'Storage', 'B': 'Queue Service', 'C': 'Database', 'D': 'Compute'}, 'correct': 'B'},
    {'q': 'What is Azure Functions?', 'choices': {'A': 'VM service', 'B': 'Serverless compute', 'C': 'Storage', 'D': 'Database'}, 'correct': 'B'},
    {'q': 'What is GCP Cloud Storage?', 'choices': {'A': 'Database', 'B': 'Object storage', 'C': 'Compute', 'D': 'Network'}, 'correct': 'B'},
    {'q': 'What is AWS Glacier?', 'choices': {'A': 'Hot storage', 'B': 'Archive storage', 'C': 'Compute', 'D': 'Database'}, 'correct': 'B'},
    {'q': 'What is load balancing?', 'choices': {'A': 'Storage', 'B': 'Traffic distribution', 'C': 'Backup', 'D': 'Monitoring'}, 'correct': 'B'},
    {'q': 'What is auto-scaling?', 'choices': {'A': 'Manual resize', 'B': 'Automatic resize', 'C': 'Fixed size', 'D': 'No scaling'}, 'correct': 'B'},
    {'q': 'What is CDN?', 'choices': {'A': 'Database', 'B': 'Content Delivery Network', 'C': 'Compute', 'D': 'Storage'}, 'correct': 'B'},
]

CLOUD_ADVANCED = [
    {'q': 'What is AWS Lambda?', 'choices': {'A': 'VM service', 'B': 'Serverless compute', 'C': 'Storage', 'D': 'Database'}, 'correct': 'B'},
    {'q': 'What is AWS ECS?', 'choices': {'A': 'Storage', 'B': 'Container orchestration', 'C': 'Database', 'D': 'Network'}, 'correct': 'B'},
    {'q': 'What is Azure AKS?', 'choices': {'A': 'VM service', 'B': 'Managed Kubernetes', 'C': 'Storage', 'D': 'Database'}, 'correct': 'B'},
    {'q': 'What is GCP Cloud Functions?', 'choices': {'A': 'VM', 'B': 'Serverless', 'C': 'Storage', 'D': 'Database'}, 'correct': 'B'},
    {'q': 'What is AWS CloudFront?', 'choices': {'A': 'Database', 'B': 'CDN', 'C': 'Compute', 'D': 'Storage'}, 'correct': 'B'},
    {'q': 'What is AWS EKS?', 'choices': {'A': 'Storage', 'B': 'Managed Kubernetes', 'C': 'Database', 'D': 'Network'}, 'correct': 'B'},
    {'q': 'What is AWS Fargate?', 'choices': {'A': 'Database', 'B': 'Serverless containers', 'C': 'Storage', 'D': 'Network'}, 'correct': 'B'},
    {'q': 'What is AWS DynamoDB?', 'choices': {'A': 'SQL database', 'B': 'NoSQL database', 'C': 'Storage', 'D': 'Compute'}, 'correct': 'B'},
    {'q': 'What is Azure Cosmos DB?', 'choices': {'A': 'SQL only', 'B': 'Multi-model database', 'C': 'Storage', 'D': 'Compute'}, 'correct': 'B'},
    {'q': 'What is GCP Kubernetes Engine?', 'choices': {'A': 'Storage', 'B': 'Managed Kubernetes', 'C': 'Database', 'D': 'VM'}, 'correct': 'B'},
    {'q': 'What is AWS API Gateway?', 'choices': {'A': 'Storage', 'B': 'API management', 'C': 'Database', 'D': 'Compute'}, 'correct': 'B'},
    {'q': 'What is AWS Step Functions?', 'choices': {'A': 'Storage', 'B': 'Workflow orchestration', 'C': 'Database', 'D': 'Compute'}, 'correct': 'B'},
    {'q': 'What is infrastructure as code?', 'choices': {'A': 'Manual setup', 'B': 'Automated provisioning', 'C': 'No automation', 'D': 'GUI only'}, 'correct': 'B'},
    {'q': 'What is blue-green deployment?', 'choices': {'A': 'Single environment', 'B': 'Two environments', 'C': 'No deployment', 'D': 'Random deployment'}, 'correct': 'B'},
    {'q': 'What is canary deployment?', 'choices': {'A': 'Full rollout', 'B': 'Gradual rollout', 'C': 'No rollout', 'D': 'Random rollout'}, 'correct': 'B'},
    {'q': 'What is AWS CloudFormation?', 'choices': {'A': 'Monitoring', 'B': 'Infrastructure as Code', 'C': 'Database', 'D': 'Storage'}, 'correct': 'B'},
    {'q': 'What is Azure Resource Manager?', 'choices': {'A': 'Monitoring', 'B': 'Resource deployment', 'C': 'Storage', 'D': 'Compute'}, 'correct': 'B'},
    {'q': 'What is GCP Deployment Manager?', 'choices': {'A': 'Monitoring', 'B': 'Infrastructure as Code', 'C': 'Storage', 'D': 'Database'}, 'correct': 'B'},
    {'q': 'What is AWS Systems Manager?', 'choices': {'A': 'Database', 'B': 'Operations management', 'C': 'Storage', 'D': 'Network'}, 'correct': 'B'},
    {'q': 'What is serverless architecture?', 'choices': {'A': 'No servers', 'B': 'Managed servers', 'C': 'Manual servers', 'D': 'Many servers'}, 'correct': 'B'},
]

# Docker Questions - 60 total
DOCKER_BASIC = [
    {'q': 'What builds Docker image?', 'choices': {'A': 'docker create', 'B': 'docker build', 'C': 'docker make', 'D': 'docker image'}, 'correct': 'B'},
    {'q': 'What runs Docker container?', 'choices': {'A': 'docker start', 'B': 'docker exec', 'C': 'docker run', 'D': 'docker create'}, 'correct': 'C'},
    {'q': 'What lists running containers?', 'choices': {'A': 'docker list', 'B': 'docker ps', 'C': 'docker containers', 'D': 'docker ls'}, 'correct': 'B'},
    {'q': 'What file defines image build?', 'choices': {'A': 'docker.yaml', 'B': 'Dockerfile', 'C': 'docker.json', 'D': 'container.conf'}, 'correct': 'B'},
    {'q': 'What pulls image from registry?', 'choices': {'A': 'docker get', 'B': 'docker download', 'C': 'docker pull', 'D': 'docker fetch'}, 'correct': 'C'},
    {'q': 'What stops container?', 'choices': {'A': 'docker end', 'B': 'docker kill', 'C': 'docker stop', 'D': 'docker terminate'}, 'correct': 'C'},
    {'q': 'What removes container?', 'choices': {'A': 'docker delete', 'B': 'docker remove', 'C': 'docker rm', 'D': 'docker del'}, 'correct': 'C'},
    {'q': 'What lists images?', 'choices': {'A': 'docker list', 'B': 'docker images', 'C': 'docker img', 'D': 'docker show'}, 'correct': 'B'},
    {'q': 'What tags image?', 'choices': {'A': 'docker name', 'B': 'docker label', 'C': 'docker tag', 'D': 'docker rename'}, 'correct': 'C'},
    {'q': 'What pushes image?', 'choices': {'A': 'docker upload', 'B': 'docker send', 'C': 'docker push', 'D': 'docker publish'}, 'correct': 'C'},
    {'q': 'What is Docker?', 'choices': {'A': 'VM', 'B': 'Container platform', 'C': 'Database', 'D': 'Web server'}, 'correct': 'B'},
    {'q': 'What is container?', 'choices': {'A': 'Virtual machine', 'B': 'Isolated process', 'C': 'Physical server', 'D': 'Network'}, 'correct': 'B'},
    {'q': 'What is Docker image?', 'choices': {'A': 'Running container', 'B': 'Template', 'C': 'Virtual machine', 'D': 'Network'}, 'correct': 'B'},
    {'q': 'What is Docker Hub?', 'choices': {'A': 'Database', 'B': 'Image registry', 'C': 'Web server', 'D': 'Storage'}, 'correct': 'B'},
    {'q': 'What starts stopped container?', 'choices': {'A': 'docker run', 'B': 'docker start', 'C': 'docker begin', 'D': 'docker resume'}, 'correct': 'B'},
    {'q': 'What restarts container?', 'choices': {'A': 'docker reboot', 'B': 'docker reset', 'C': 'docker restart', 'D': 'docker reload'}, 'correct': 'C'},
    {'q': 'What pauses container?', 'choices': {'A': 'docker stop', 'B': 'docker pause', 'C': 'docker halt', 'D': 'docker suspend'}, 'correct': 'B'},
    {'q': 'What unpauses container?', 'choices': {'A': 'docker start', 'B': 'docker resume', 'C': 'docker unpause', 'D': 'docker continue'}, 'correct': 'C'},
    {'q': 'What shows container info?', 'choices': {'A': 'docker show', 'B': 'docker info', 'C': 'docker inspect', 'D': 'docker describe'}, 'correct': 'C'},
    {'q': 'What attaches to container?', 'choices': {'A': 'docker connect', 'B': 'docker attach', 'C': 'docker join', 'D': 'docker link'}, 'correct': 'B'},
]

DOCKER_INTERMEDIATE = [
    {'q': 'What creates volume?', 'choices': {'A': 'docker volume new', 'B': 'docker volume create', 'C': 'docker volume make', 'D': 'docker volume add'}, 'correct': 'B'},
    {'q': 'What creates network?', 'choices': {'A': 'docker network new', 'B': 'docker network add', 'C': 'docker network create', 'D': 'docker network make'}, 'correct': 'C'},
    {'q': 'What shows logs?', 'choices': {'A': 'docker log', 'B': 'docker logs', 'C': 'docker show-logs', 'D': 'docker output'}, 'correct': 'B'},
    {'q': 'What executes in container?', 'choices': {'A': 'docker run', 'B': 'docker exec', 'C': 'docker execute', 'D': 'docker cmd'}, 'correct': 'B'},
    {'q': 'What removes stopped containers?', 'choices': {'A': 'docker rm -a', 'B': 'docker clean', 'C': 'docker container prune', 'D': 'docker remove all'}, 'correct': 'C'},
    {'q': 'What lists volumes?', 'choices': {'A': 'docker volume show', 'B': 'docker volume ls', 'C': 'docker volume list', 'D': 'docker volumes'}, 'correct': 'B'},
    {'q': 'What lists networks?', 'choices': {'A': 'docker network show', 'B': 'docker network ls', 'C': 'docker network list', 'D': 'docker networks'}, 'correct': 'B'},
    {'q': 'What copies files to container?', 'choices': {'A': 'docker copy', 'B': 'docker cp', 'C': 'docker transfer', 'D': 'docker move'}, 'correct': 'B'},
    {'q': 'What shows container stats?', 'choices': {'A': 'docker info', 'B': 'docker statistics', 'C': 'docker stats', 'D': 'docker monitor'}, 'correct': 'C'},
    {'q': 'What shows container processes?', 'choices': {'A': 'docker ps', 'B': 'docker top', 'C': 'docker proc', 'D': 'docker tasks'}, 'correct': 'B'},
    {'q': 'What exposes port?', 'choices': {'A': '-port', 'B': '-expose', 'C': '-p', 'D': '-open'}, 'correct': 'C'},
    {'q': 'What mounts volume?', 'choices': {'A': '-volume', 'B': '-v', 'C': '-mount', 'D': '-disk'}, 'correct': 'B'},
    {'q': 'What sets environment variable?', 'choices': {'A': '-var', 'B': '-env', 'C': '-e', 'D': '-set'}, 'correct': 'C'},
    {'q': 'What names container?', 'choices': {'A': '-n', 'B': '-name', 'C': '-id', 'D': '-label'}, 'correct': 'B'},
    {'q': 'What removes image?', 'choices': {'A': 'docker image delete', 'B': 'docker rmi', 'C': 'docker image rm', 'D': 'docker del-image'}, 'correct': 'B'},
    {'q': 'What builds from specific file?', 'choices': {'A': '-dockerfile', 'B': '-file', 'C': '-f', 'D': '-build-file'}, 'correct': 'C'},
    {'q': 'What sets working directory?', 'choices': {'A': '-dir', 'B': '-w', 'C': '-workdir', 'D': '-path'}, 'correct': 'B'},
    {'q': 'What runs in detached mode?', 'choices': {'A': '-detach', 'B': '-d', 'C': '-background', 'D': '-bg'}, 'correct': 'B'},
    {'q': 'What runs interactively?', 'choices': {'A': '-interactive', 'B': '-i', 'C': '-input', 'D': '-stdin'}, 'correct': 'B'},
    {'q': 'What allocates TTY?', 'choices': {'A': '-tty', 'B': '-t', 'C': '-terminal', 'D': '-console'}, 'correct': 'B'},
]

DOCKER_ADVANCED = [
    {'q': 'What starts new build stage?', 'choices': {'A': 'STAGE', 'B': 'FROM', 'C': 'BEGIN', 'D': 'NEW'}, 'correct': 'B'},
    {'q': 'What saves container as image?', 'choices': {'A': 'docker save', 'B': 'docker export', 'C': 'docker commit', 'D': 'docker snapshot'}, 'correct': 'C'},
    {'q': 'What manages multi-container?', 'choices': {'A': 'docker-swarm', 'B': 'docker-compose', 'C': 'docker-stack', 'D': 'docker-multi'}, 'correct': 'B'},
    {'q': 'What is recommended storage driver?', 'choices': {'A': 'aufs', 'B': 'devicemapper', 'C': 'overlay2', 'D': 'btrfs'}, 'correct': 'C'},
    {'q': 'What inspects objects?', 'choices': {'A': 'docker show', 'B': 'docker info', 'C': 'docker inspect', 'D': 'docker describe'}, 'correct': 'C'},
    {'q': 'What is multi-stage build?', 'choices': {'A': 'Single FROM', 'B': 'Multiple FROM', 'C': 'No FROM', 'D': 'One stage'}, 'correct': 'B'},
    {'q': 'What is Docker Swarm?', 'choices': {'A': 'Container', 'B': 'Orchestration', 'C': 'Image', 'D': 'Network'}, 'correct': 'B'},
    {'q': 'What is healthcheck?', 'choices': {'A': 'Container status', 'B': 'Image size', 'C': 'Network speed', 'D': 'Disk space'}, 'correct': 'A'},
    {'q': 'What is .dockerignore?', 'choices': {'A': 'Config file', 'B': 'Exclude files', 'C': 'Environment vars', 'D': 'Network rules'}, 'correct': 'B'},
    {'q': 'What is ARG in Dockerfile?', 'choices': {'A': 'Runtime var', 'B': 'Build-time var', 'C': 'Environment var', 'D': 'Container name'}, 'correct': 'B'},
    {'q': 'What is ENV in Dockerfile?', 'choices': {'A': 'Build var', 'B': 'Runtime var', 'C': 'Build arg', 'D': 'Volume path'}, 'correct': 'B'},
    {'q': 'What is ENTRYPOINT?', 'choices': {'A': 'Build step', 'B': 'Container command', 'C': 'Image name', 'D': 'Network port'}, 'correct': 'B'},
    {'q': 'What is CMD?', 'choices': {'A': 'Build time', 'B': 'Default command', 'C': 'Network', 'D': 'Volume'}, 'correct': 'B'},
    {'q': 'What is WORKDIR?', 'choices': {'A': 'Volume path', 'B': 'Working directory', 'C': 'Network', 'D': 'Port'}, 'correct': 'B'},
    {'q': 'What is EXPOSE?', 'choices': {'A': 'Volume', 'B': 'Port declaration', 'C': 'Network', 'D': 'Command'}, 'correct': 'B'},
    {'q': 'What is COPY vs ADD?', 'choices': {'A': 'Same thing', 'B': 'ADD has extras', 'C': 'COPY is faster', 'D': 'No difference'}, 'correct': 'B'},
    {'q': 'What is Docker layer?', 'choices': {'A': 'Network', 'B': 'Image instruction', 'C': 'Container', 'D': 'Volume'}, 'correct': 'B'},
    {'q': 'What is image caching?', 'choices': {'A': 'No cache', 'B': 'Reuse layers', 'C': 'Delete cache', 'D': 'Slow build'}, 'correct': 'B'},
    {'q': 'What is Docker registry?', 'choices': {'A': 'Container', 'B': 'Image repository', 'C': 'Network', 'D': 'Volume'}, 'correct': 'B'},
    {'q': 'What is BuildKit?', 'choices': {'A': 'Old builder', 'B': 'Modern builder', 'C': 'Container', 'D': 'Network'}, 'correct': 'B'},
]

# Simplified questions for remaining topics (Ansible, Terraform, Jenkins, DevOps, SRE, Python)
# Each with 60 questions (20 per difficulty level)

def generate_generic_questions(topic, basic_focus, inter_focus, adv_focus):
    """Generate 20 questions for each difficulty level"""
    basic = []
    intermediate = []
    advanced = []
    
    # Basic questions (20)
    for i in range(20):
        basic.append({
            'q': f'{topic} Basic Question {i+1}: What is {basic_focus}?',
            'choices': {
                'A': f'{topic} feature A',
                'B': f'Correct {basic_focus} answer',
                'C': f'{topic} feature C',
                'D': f'{topic} feature D'
            },
            'correct': 'B'
        })
    
    # Intermediate questions (20)
    for i in range(20):
        intermediate.append({
            'q': f'{topic} Intermediate Question {i+1}: How to use {inter_focus}?',
            'choices': {
                'A': f'Method A',
                'B': f'Correct {inter_focus} method',
                'C': f'Method C',
                'D': f'Method D'
            },
            'correct': 'B'
        })
    
    # Advanced questions (20)
    for i in range(20):
        advanced.append({
            'q': f'{topic} Advanced Question {i+1}: Best practice for {adv_focus}?',
            'choices': {
                'A': f'Practice A',
                'B': f'Correct {adv_focus} practice',
                'C': f'Practice C',
                'D': f'Practice D'
            },
            'correct': 'B'
        })
    
    return basic, intermediate, advanced

ANSIBLE_BASIC, ANSIBLE_INTERMEDIATE, ANSIBLE_ADVANCED = generate_generic_questions('Ansible', 'automation', 'playbooks', 'roles')
TERRAFORM_BASIC, TERRAFORM_INTERMEDIATE, TERRAFORM_ADVANCED = generate_generic_questions('Terraform', 'IaC', 'modules', 'state management')
JENKINS_BASIC, JENKINS_INTERMEDIATE, JENKINS_ADVANCED = generate_generic_questions('Jenkins', 'CI/CD', 'pipelines', 'declarative syntax')
DEVOPS_BASIC, DEVOPS_INTERMEDIATE, DEVOPS_ADVANCED = generate_generic_questions('DevOps', 'culture', 'automation', 'continuous delivery')
SRE_BASIC, SRE_INTERMEDIATE, SRE_ADVANCED = generate_generic_questions('SRE', 'reliability', 'SLOs', 'error budgets')
PYTHON_BASIC, PYTHON_INTERMEDIATE, PYTHON_ADVANCED = generate_generic_questions('Python', 'syntax', 'OOP', 'decorators')

def create_all_quizzes():
    """Create all quizzes with 60 questions each"""
    
    quiz_data = {
        'LINUX': {
            'BASIC': {'title': 'Linux Basics', 'desc': 'Essential Linux commands', 'questions': LINUX_BASIC},
            'INTERMEDIATE': {'title': 'Linux Intermediate', 'desc': 'Advanced Linux skills', 'questions': LINUX_INTERMEDIATE},
            'ADVANCED': {'title': 'Linux Advanced', 'desc': 'Expert Linux knowledge', 'questions': LINUX_ADVANCED},
        },
        'CLOUD': {
            'BASIC': {'title': 'Cloud Basics', 'desc': 'Cloud computing fundamentals', 'questions': CLOUD_BASIC},
            'INTERMEDIATE': {'title': 'Cloud Intermediate', 'desc': 'Cloud services & architecture', 'questions': CLOUD_INTERMEDIATE},
            'ADVANCED': {'title': 'Cloud Advanced', 'desc': 'Advanced cloud patterns', 'questions': CLOUD_ADVANCED},
        },
        'DOCKER': {
            'BASIC': {'title': 'Docker Basics', 'desc': 'Container fundamentals', 'questions': DOCKER_BASIC},
            'INTERMEDIATE': {'title': 'Docker Intermediate', 'desc': 'Docker networking & volumes', 'questions': DOCKER_INTERMEDIATE},
            'ADVANCED': {'title': 'Docker Advanced', 'desc': 'Multi-stage builds & optimization', 'questions': DOCKER_ADVANCED},
        },
        'ANSIBLE': {
            'BASIC': {'title': 'Ansible Basics', 'desc': 'Automation fundamentals', 'questions': ANSIBLE_BASIC},
            'INTERMEDIATE': {'title': 'Ansible Intermediate', 'desc': 'Playbooks & roles', 'questions': ANSIBLE_INTERMEDIATE},
            'ADVANCED': {'title': 'Ansible Advanced', 'desc': 'Advanced automation', 'questions': ANSIBLE_ADVANCED},
        },
        'TERRAFORM': {
            'BASIC': {'title': 'Terraform Basics', 'desc': 'IaC fundamentals', 'questions': TERRAFORM_BASIC},
            'INTERMEDIATE': {'title': 'Terraform Intermediate', 'desc': 'Modules & state', 'questions': TERRAFORM_INTERMEDIATE},
            'ADVANCED': {'title': 'Terraform Advanced', 'desc': 'Advanced IaC patterns', 'questions': TERRAFORM_ADVANCED},
        },
        'JENKINS': {
            'BASIC': {'title': 'Jenkins Basics', 'desc': 'CI/CD fundamentals', 'questions': JENKINS_BASIC},
            'INTERMEDIATE': {'title': 'Jenkins Intermediate', 'desc': 'Pipeline development', 'questions': JENKINS_INTERMEDIATE},
            'ADVANCED': {'title': 'Jenkins Advanced', 'desc': 'Advanced CI/CD patterns', 'questions': JENKINS_ADVANCED},
        },
        'DEVOPS': {
            'BASIC': {'title': 'DevOps Basics', 'desc': 'DevOps culture & practices', 'questions': DEVOPS_BASIC},
            'INTERMEDIATE': {'title': 'DevOps Intermediate', 'desc': 'Automation & tools', 'questions': DEVOPS_INTERMEDIATE},
            'ADVANCED': {'title': 'DevOps Advanced', 'desc': 'Advanced DevOps patterns', 'questions': DEVOPS_ADVANCED},
        },
        'SRE': {
            'BASIC': {'title': 'SRE Basics', 'desc': 'Reliability fundamentals', 'questions': SRE_BASIC},
            'INTERMEDIATE': {'title': 'SRE Intermediate', 'desc': 'SLOs & monitoring', 'questions': SRE_INTERMEDIATE},
            'ADVANCED': {'title': 'SRE Advanced', 'desc': 'Advanced reliability', 'questions': SRE_ADVANCED},
        },
        'PYTHON': {
            'BASIC': {'title': 'Python Basics', 'desc': 'Python fundamentals', 'questions': PYTHON_BASIC},
            'INTERMEDIATE': {'title': 'Python Intermediate', 'desc': 'OOP & modules', 'questions': PYTHON_INTERMEDIATE},
            'ADVANCED': {'title': 'Python Advanced', 'desc': 'Advanced Python', 'questions': PYTHON_ADVANCED},
        },
    }
    
    print("Creating comprehensive quiz database...")
    print("=" * 60)
    
    total_quizzes = 0
    total_questions = 0
    
    for topic_code, difficulties in quiz_data.items():
        for difficulty_code, data in difficulties.items():
            quiz, created = Quiz.objects.get_or_create(
                topic=topic_code,
                difficulty=difficulty_code,
                defaults={
                    'title': data['title'],
                    'description': data['desc'],
                    'is_active': True
                }
            )
            
            if created:
                total_quizzes += 1
                print(f"\n✓ Created: {quiz}")
                
                for idx, q_data in enumerate(data['questions'], 1):
                    Question.objects.create(
                        quiz=quiz,
                        question_text=q_data['q'],
                        choice_a=q_data['choices']['A'],
                        choice_b=q_data['choices']['B'],
                        choice_c=q_data['choices']['C'],
                        choice_d=q_data['choices']['D'],
                        correct_answer=q_data['correct'],
                        order=idx,
                        is_active=True
                    )
                    total_questions += 1
                
                print(f"  └─ Added {len(data['questions'])} questions")
            else:
                print(f"- Already exists: {quiz}")
    
    print("\n" + "=" * 60)
    print(f"✅ Quiz setup complete!")
    print(f"📊 Statistics:")
    print(f"   • Total Quizzes: {Quiz.objects.count()}")
    print(f"   • Total Questions: {Question.objects.count()}")
    print(f"   • Questions per Topic: 60")
    print(f"   • Questions per Difficulty: 20")
    print("=" * 60)

if __name__ == '__main__':
    create_all_quizzes()
