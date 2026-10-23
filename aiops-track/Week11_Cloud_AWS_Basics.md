# Week 11: Cloud & AWS Basics

> 📍 **Part of:** [AI Ops Career Roadmap](../AIOps_Roadmap.md) — Phase 1: DevOps Foundations

**← Previous Week:** [Git & Version Control](Week10_Git_VersionControl.md)

---

## 📋 Learning Objectives

| Topic | What You'll Learn |
|-------|-------------------|
| **Cloud Fundamentals** | IaaS, PaaS, SaaS concepts |
| **AWS Overview** | Core services (EC2, S3, RDS) |
| **EC2 Instances** | Launching, connecting, managing VMs |
| **AWS Networking** | Security groups, VPC basics |

## 🎯 Why These Matter for AI Ops

- **Infrastructure**: Most AI Ops tools run in the cloud
- **Compute**: You'll deploy models and automation scripts to cloud VMs
- **Storage**: Cloud storage for logs, metrics, and data
- **Managed Services**: Using cloud-native monitoring (CloudWatch, etc.)

---

## 📚 Concept 1: Cloud Fundamentals

### What is the Cloud?

| Model | Description | Examples |
|-------|-------------|----------|
| **IaaS** | Virtual machines, storage, networking | AWS EC2, Google Compute Engine |
| **PaaS** | Managed runtime for your code | Heroku, AWS Beanstalk |
| **SaaS** | Complete application over the internet | Gmail, Slack, Datadog |

### Why Cloud for AI Ops?

- **Elasticity**: Scale up/down based on load
- **Managed Services**: Don't reinvent infrastructure
- **Global Reach**: Deploy close to users
- **Pay-as-you-go**: No upfront hardware costs

---

## 📚 Concept 2: AWS Core Services

### EC2 (Elastic Compute Cloud)

Virtual servers in the cloud.

```
┌─────────────────────────────────────┐
│           AWS Region                 │
│  ┌─────────────────────────────┐   │
│  │      VPC                    │   │
│  │  ┌─────────────────────┐    │   │
│  │  │   Subnet            │    │   │
│  │  │  ┌──────────────┐   │    │   │
│  │  │  │   EC2        │   │    │   │
│  │  │  │  Instance    │   │    │   │
│  │  │  └──────────────┘   │    │   │
│  │  └─────────────────────┘    │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

### S3 (Simple Storage Service)

Object storage for files, data, backups.

```bash
# S3 use cases
- Store application logs
- Store ML model files
- Backup configurations
- Host static websites
```

### RDS (Relational Database Service)

Managed databases (PostgreSQL, MySQL, etc.).

### IAM (Identity and Access Management)

User management and permissions.

---

## 📚 Concept 3: Launching an EC2 Instance

### Step 1: Create an Account

1. Go to [aws.amazon.com](https://aws.amazon.com)
2. Create free tier account
3. Add payment method (required, but won't charge)

### Step 2: Launch an Instance

Navigate to EC2 → Launch Instance

| Setting | Value |
|---------|-------|
| **Name** | my-first-instance |
| **AMI** | Amazon Linux 2023 (Free tier eligible) |
| **Instance Type** | t2.micro or t3.micro (Free tier) |
| **Key Pair** | Create new or use existing |
| **Network** | Default VPC |
| **Security Group** | Allow SSH (port 22) |

### Step 3: Connect via SSH

```bash
# Connect to your instance
ssh -i your-key.pem ec2-user@your-public-ip

# Example
ssh -i ~/.ssh/aws-key.pem ec2-user@52.12.345.67
```

### Step 4: Install Software

```bash
# Update packages
sudo yum update -y

# Install Python
sudo yum install python3 -y

# Install Docker
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user
```

---

## 📚 Concept 4: Security Groups

### What are Security Groups?

Virtual firewalls that control inbound/outbound traffic.

### Default Rules

| Inbound | Outbound |
|---------|----------|
| None (deny all) | All allowed |

### Adding Rules

```
┌─────────────────────────────────────┐
│         Security Group             │
├─────────────────────────────────────┤
│  Inbound Rules:                     │
│  ─────────────────                  │
│  1. SSH    │ TCP  │ 22  │ My IP    │
│  2. HTTP   │ TCP  │ 80  │ 0.0.0.0/0│
│  3. HTTPS  │ TCP  │ 443 │ 0.0.0.0/0│
│  4. Custom │ TCP  │ 8080│ 10.0.0.0/16│
├─────────────────────────────────────┤
│  Outbound Rules:                   │
│  ─────────────────                  │
│  1. All Trafic│ ALL │ 0   │ 0.0.0.0/0│
└─────────────────────────────────────┘
```

### Best Practices

- **Least privilege**: Only open ports you need
- **Restrict SSH**: Use "My IP" for SSH access
- **No default inbound**: Don't allow all traffic
- **Tag resources**: Add names/descriptions for tracking

---

## 📝 Weekly Project

### Task: Launch EC2 and Deploy Script

**Objective:** Launch an EC2 instance, SSH into it, install Python, and run your script.

### Steps

#### 1. Launch EC2 Instance

- Use AWS Console to create t2.micro
- Select "Amazon Linux 2023" AMI
- Download the key pair (.pem file)

#### 2. Connect to Instance

```bash
# Fix key permissions (Linux/macOS)
chmod 400 your-key.pem

# SSH into instance
ssh -i your-key.pem ec2-user@PUBLIC_IP
```

#### 3. Install Dependencies

```bash
sudo yum update -y
sudo yum install python3 git -y

# Verify
python3 --version
git --version
```

#### 4. Transfer Your Script

```bash
# From YOUR local machine (not the EC2)
scp -i your-key.pem ~/lab/tools/python-scripts/disk_usage.py \
    ec2-user@PUBLIC_IP:~/

# Or use git clone if you've pushed to GitHub
```

#### 5. Run the Script

```bash
# On the EC2 instance
python3 disk_usage.py
```

---

## ✅ Progress Log

```markdown
## Week 11: Cloud & AWS Basics

### Progress
- [ ] Created AWS free tier account
- [ ] Launched EC2 instance
- [ ] Connected via SSH
- [ ] Installed Python
- [ ] Ran script on cloud instance
- [ ] Notes documented

### What I Learned
-

### Challenges Faced
-

### Questions for Next Week
-

### Readiness Check
- [ ] Can launch EC2 instance
- [ ] Can SSH into cloud instance
- [ ] Can install software on remote server
- [ ] Can transfer files via SCP
- [ ] Ready to move on: Yes / No
```

---

## 📖 Resources

- [AWS Free Tier](https://aws.amazon.com/free/)
- [EC2 Getting Started](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [Awesome AWS](https://github.com/donnieberg/awesome-aws)

---

## 🔜 Next Up (Week 12)

- [Docker Basics →](Week12_Docker_Basics.md)

---

*Week 11 - DevOps Foundations Phase*  
*Last Updated: May 2025*

---

**[← Back to AI Ops Roadmap](../AIOps_Roadmap.md)**