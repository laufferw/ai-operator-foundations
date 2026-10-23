# AI Ops Career Roadmap

A practical guide for transitioning from Revenue Operations to AI Operations Engineer

---

## Table of Contents

1. [Overview](#overview)
2. [Why This Path?](#why-this-path)
3. [Your Unique Advantage](#your-unique-advantage)
4. [The Roadmap](#the-roadmap)
   - [Phase 1: DevOps Foundations (Weeks 1-12)](#phase-1-devops-foundations-weeks-1-12)
   - [Phase 2: Data Engineering for Ops (Weeks 13-22)](#phase-2-data-engineering-for-ops-weeks-13-22)
   - [Phase 3: Applied AI/ML for Operations (Weeks 23-34)](#phase-3-applied-aiml-for-operations-weeks-23-34)
   - [Phase 4: AI Ops Specialization (Ongoing)](#phase-4-ai-ops-specialization-ongoing)
5. [Key Skills to Master](#key-skills-to-master)
6. [Recommended Resources](#recommended-resources)
7. [Weekly Tracking Template](#weekly-tracking-template)
8. [Next Steps](#next-steps)

---

## 🎯 Learning Philosophy: How This Roadmap Works

These directives guide every learning session:

### 1. Student Does, Mentor Guides
- **William writes the code** - Not the mentor
- **Mentor provides hints and explains concepts** - Does not write the solution
- **Debugging is part of learning** - Errors are opportunities to understand
- The goal is muscle memory and problem-solving, not watching someone else code

### 2. Always Explain the Why
- Every concept taught must include the business/practical reason
- "Here's how to do X" is never enough
- Must answer: "Why does this matter for AI Ops?"
- Connect technical skills to career trajectory

---

## Overview

**Starting Point:** Revenue Operations Specialist  
**Target Role:** AI Operations Engineer  
**Timeline:** 8-12 months to job readiness  

This roadmap provides a structured path to transition from Revenue Operations into AI Ops, leveraging your existing business understanding while building the technical foundation needed to apply machine learning to IT operations.

---

## Why This Path?

### The Career Trajectory

```
Revenue Ops (Current)
    │
    ├── Process optimization
    ├── Data analysis
    ├── Cross-functional collaboration
    ├── Systems thinking
    └── Understanding business impact
    
            ▼
        
DevOps (Bridge Role - 3-4 months)
    │
    ├── Infrastructure automation
    ├── Monitoring & observability
    ├── CI/CD pipelines
    └── Incident management
        
            ▼
        
AI Ops (Target Role)
    ├── Applying ML to operations data
    ├── Anomaly detection
    ├── Predictive maintenance
    ├── Alert correlation
    └── Automating incident response
```

### Why Not Direct to AI Ops?

You need the domain expertise in operations before you can apply AI to it. DevOps provides:
- Deep understanding of infrastructure
- Experience with monitoring and observability
- Familiarity with incident management
- Understanding of operational data types (logs, metrics, traces)

---

## Your Unique Advantage

Most AI Ops professionals come from one of two backgrounds:

| Background | Strength | Weakness |
|------------|----------|----------|
| Pure Technical (DevOps/SRE) | Strong technical skills | Limited business context |
| Pure Data/ML | ML expertise | Doesn't understand operations |

**Your advantage:** You understand business operations. Anomaly detection means nothing if you can't translate it to business impact. This differentiates you from purely technical candidates.

### How to Position This in Interviews

> "I'm coming from Revenue Operations where I learned to think about systems holistically—how technical decisions affect business outcomes. I'm building the technical foundation in DevOps and data engineering so I can apply AI to make operations more efficient. I want to work at the intersection of operations and intelligence."

---

## The Roadmap

### Phase 1: DevOps Foundations (Weeks 1-12)

**Purpose:** Build the technical foundation needed for operations work  
**Time Commitment:** 1-2 hours daily + weekend project time

#### Weekly Breakdown

| Weeks | Focus Area | Key Skills |
|-------|------------|------------|
| 1-4 | Linux Command Line | File management, permissions, processes, networking |
| 5-9 | Python for DevOps | Automation, scripting, APIs, data handling |
| 10 | Git & Version Control | Branching, merging, workflows |
| 11-12 | Cloud & Docker Basics | AWS/GCP, containers, Dockerfiles |

#### Detailed Weekly Plan

---

##### Weeks 1-4: Linux Command Line

**Objective:** Navigate and work in Linux entirely via command line

| Week | Topics | Daily Practice |
|------|--------|----------------|
| 1 | VirtualBox/Ubuntu setup, file system basics, commands (ls, cd, pwd, mkdir, rm) | 30 min |
| 2 | File manipulation (cat, less, grep, sed, awk), permissions (chmod, chown) | 30 min |
| 3 | Process management (ps, top, kill, systemctl), networking basics (ip, ping, curl, ssh) | 45 min |
| 4 | Package management (apt), scripting basics, redirection, pipes | 45 min |

**Weekly Projects:**
- Week 1: Install Ubuntu in VirtualBox, explore with ls and navigate
- Week 2: Create a script to find all files modified in last 24 hours
- Week 3: Set up SSH keys to connect to your VM without password
- Week 4: Write a backup script that copies files to a backup directory

**Readiness Check:** Can navigate Linux without GUI, debug "command not found" errors

---

##### Weeks 5-9: Python for DevOps

**Objective:** Write automation scripts for operational tasks

| Week | Topics | Focus |
|------|--------|-------|
| 5-6 | Python basics: variables, data types, control flow, functions | Syntax fluency |
| 7 | File I/O, JSON/YAML handling, regular expressions | Data manipulation |
| 8 | Working with APIs (requests library), HTTP | Integration skills |
| 9 | Virtual environments, pip, modules, error handling | Production basics |

**Weekly Projects:**
- Week 5-6: Write a script that calculates disk usage and prints top 5 largest files
- Week 7: Parse a YAML config file and print specific values in a formatted way
- Week 8: Write a script that fetches JSON data from an API (e.g., GitHub API) and saves it
- Week 9: Create a Python tool that checks if services are running and restarts them if not

**Readiness Check:** Can write a 50-line script without looking up basic syntax

---

##### Week 10: Git & Version Control

**Objective:** Manage code and configs with Git

| Topic | Skills to Build |
|-------|----------------|
| Basics | init, add, commit, status |
| Remote | push, pull, fetch, clone |
| Branching | branch, checkout, merge, rebase |
| Workflows | Branching strategies, PRs, code review |

**Project:** Initialize a git repo, create meaningful commits, push to GitHub

**Readiness Check:** Can create branches, resolve simple merge conflicts

---

##### Weeks 11-12: Cloud & Docker Introduction

**Objective:** Understand cloud basics and containerization

| Week | Focus |
|------|-------|
| 11 | AWS or GCP free tier: create account, launch EC2/VM, basic networking |
| 12 | Docker: images, containers, basic Dockerfile, Docker Compose |

**Projects:**
- Week 11: Launch an EC2 instance, SSH into it, install Python and run your script
- Week 12: Containerize one of your Python scripts with a Dockerfile

**Readiness Check:** Can launch a VM and SSH into it, run a container

---

### Phase 2: Data Engineering for Ops (Weeks 13-22)

**Purpose:** AI Ops is 80% data pipeline, 20% ML model

**Why This Phase Matters:**
- Operations generates massive amounts of data (logs, metrics, traces)
- You need to collect, store, process, and transform this data
- Most AI Ops failures are data problems, not model problems

#### Key Topics

```
Data Collection & Storage
├── Time-series databases (InfluxDB, Prometheus, TimescaleDB)
├── Log aggregation (ELK stack, Loki)
├── Data formats (Parquet, JSON, Protobuf)
└── Data retention policies

Data Pipelines
├── Apache Airflow
├── Prefect
├── dbt (data build tool)
└── Streaming vs batch processing

Feature Engineering
├── Feature stores (Feast)
├── Data validation (Great Expectations)
├── Time-series feature extraction
└── Handling missing data
```

#### Suggested Projects

- Build a data pipeline that collects system metrics and stores them in InfluxDB
- Create a log aggregation and parsing pipeline
- Build a feature extraction pipeline for time-series data

---

### Phase 3: Applied AI/ML for Operations (Weeks 23-34)

**Purpose:** Learn enough ML to apply it to operations—not to be a research scientist

**Focus:** Applied machine learning, not theory

#### Key Topics

```
Core ML Skills
├── Classification and clustering
├── Anomaly detection algorithms
│   ├── Isolation Forest
│   ├── LSTMs for time series
│   └── Bayesian change point detection
├── Time-series forecasting
├── Model evaluation metrics
└── Interpretability

ML for Operations Specific
├── Root cause analysis
├── Predictive alerting
├── Alert correlation
├── Capacity forecasting
└── Incident prediction

MLOps Basics
├── Model versioning
├── Model serving (MLflow, KServe, Triton)
├── Pipeline orchestration
└── Monitoring deployed models
```

#### Suggested Projects

- Build an anomaly detection model for CPU usage data
- Create a model that predicts when a service will fail
- Build a log clustering system to identify common patterns

---

### Phase 4: AI Ops Specialization (Ongoing)

**Purpose:** Differentiate yourself and land your target role

#### Tools to Learn

| Category | Tools |
|----------|-------|
| Commercial AI Ops | Splunk ITSI, Dynatrace Davis, Datadog AI, New Relic AI |
| Cloud AI Ops | AWS DevOps Guru, GCP Operations Suite, Azure AI |
| Open Source | Kubeflow, MLflow, Seldon, Prometheus + custom ML |
| Startups | BigPanda, Moogsoft, xMatters, BigEye |

#### Capstone Projects

1. Build an end-to-end ML pipeline: data collection → training → deployment → monitoring
2. Create a model serving system with A/B testing
3. Implement ML monitoring for data/model drift
4. Deploy an LLM with proper scaling (RAG-based ops assistant)

---

## Key Skills to Master

### Priority 1: Non-Negotiable

| Skill | Why It Matters |
|-------|----------------|
| **Linux CLI** | Everything in ops runs on Linux; this is your daily workspace |
| **Python** | Most DevOps tools are Python-based; automation essential |
| **Observability** | Understanding logs, metrics, traces is fundamental to AI Ops |

### Priority 2: Important

| Skill | Why It Matters |
|-------|----------------|
| **Cloud (AWS/GCP)** | Most workloads run in the cloud |
| **Docker/Kubernetes** | Container orchestration is standard |
| **Data Engineering** | AI Ops is 80% data preparation |

### Priority 3: Differentiators

| Skill | Why It Matters |
|-------|----------------|
| **Go** | Many modern DevOps tools written in Go (optional) |
| **Applied ML** | Enables AI Ops role |
| **Business Translation** | Your unique RevOps advantage |

---

## ✅ Progress Log

### Week 1: Linux Foundations (Completed) 
- [x] Set up learning lab at ~/lab/
- [x] Explored Linux commands (ls, cd, pwd, mkdir, rm)
- [x] Created sysadmin-toolkit directory structure

### Week 2: File Manipulation (Completed)
- [x] Created "recent-changes" script to find files modified in last N days
- [x] Learned about inodes and file metadata
- [x] Used `find -mtime` command

### Week 3: SSH & Security (Completed)
- [x] Generated Ed25519 SSH key
- [x] Added public key to authorized_keys
- [x] Tested passwordless SSH to localhost

### Week 4: Bash Scripting & Package Management (Completed)
- [x] Backup script created in ~/lab/tools/sysadmin-toolkit/
- [x] Learned apt package management (installed sl, cowsay)
- [x] Created multiple bash scripts (hello.sh, age.sh, greet.sh)

### Week 5-6: Python Basics (In Progress)
- [x] Set up Python workspace at ~/lab/tools/python-scripts/
- [x] Learned Python data types (strings, integers, booleans, lists, dicts)
- [x] Learned control flow (if/elif/else, for loops, comprehensions)
- [x] Created functions and practiced with career profile example
- [x] Built disk_usage.py - finds top 5 largest files in a directory
- [ ] Practice: Write more Python scripts

---

## Recommended Resources

### Linux

- [The Linux Command Line (TLCL)](https://linuxcommand.org/tlcl.php) — Free, comprehensive
- [Linux Basics for Hackers](https://nostarch.com/linuxbasicsforhackers) — Practical, hands-on
- [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) — Gamified practice

### Python

- [Automate the Boring Stuff](https://automatetheboringstuff.com/) — Free, practical
- [Python Crash Course](https://nostarch.com/pythoncrashcourse2e) — Structured learning
- [Real Python](https://realpython.com/) — Tutorials and articles

### Git

- [Pro Git Book](https://git-scm.com/book) — Free, comprehensive
- [GitHub Skills](https://github.com/skills) — Interactive labs

### Cloud

- [AWS Free Tier](https://aws.amazon.com/free/) — Free for 12 months
- [AWS Solutions Architect Cert](https://aws.amazon.com/certification/) — Industry standard

### Docker & Kubernetes

- [Docker Getting Started](https://docs.docker.com/get-started/) — Official docs
- [KodeKloud](https://kodekloud.com/) — DevOps courses

### MLOps / AI Ops

- [MLflow](https://mlflow.org/) — Open source ML lifecycle
- [Kubeflow](https://kubeflow.org/) — ML pipelines on Kubernetes
- [Weights & Biases](https://wandb.ai/) — Experiment tracking

### Books

- [Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/) — Free from Google
- [Machine Learning Engineering](https://www.mlebook.com/) — By Andriy Burkov
- [Designing Data-Intensive Applications](https://dataintensive.net/) — By Martin Kleppmann

---

## ✅ Progress Log

```markdown
## Week X: [Topic]

### Progress
- [ ] Completed daily practice: __/__ days
- [ ] Finished weekly project
- [ ] Notes documented

### What I Learned
-

### Challenges Faced
-

### Questions for Next Week
-

### Readiness Check
- [ ] Ready to move on: Yes / No
```

---

## Next Steps

1. **Start Week 1:** Set up your learning environment (VirtualBox + Ubuntu)
2. **Each Week:** Follow the daily practice + weekly project structure
3. **Monthly Review:** Assess progress, adjust pace
4. **After Phase 1:** Revisit this roadmap for Phase 2 details
5. **Keep Leveraging Your Advantage:** Always connect technical skills to business outcomes

---

## Quick Reference: Your Career Story

> "I'm transitioning from Revenue Operations to AI Operations. After years of optimizing revenue processes and understanding how business systems work, I'm building the technical foundation in DevOps and data engineering so I can apply AI to make IT operations more intelligent. My unique value is bringing business context to technical operations—understanding that every alert has a business impact."

---

*Last Updated: May 2025*  
*Timeline: 8-12 months to job readiness*

---

## 🔄 Current Progress

| Phase | Status | Notes |
|-------|--------|-------|
| Phase 1: DevOps Foundations | **In Progress** | Completed Weeks 1-4 |
| Week 1-4: Linux CLI | ✅ Complete | Lab setup, basic navigation |
| Week 2: find-modified script | ✅ Complete | `recent-changes` script in ~/lab/tools/ |
| Week 3: SSH Keys | ✅ Complete | Generated Ed25519 key, passwordless SSH working |
| Week 4: Bash Scripting | ✅ Complete | Created backup script, learned apt package management |
| Weeks 5-6: Python Basics | ✅ Complete | disk_usage.py works! |
| Week 7: File I/O, JSON, YAML, Regex | [📝 Workbook →](Week7_File_IO_JSON_YAML_Regex.md) | Starter template ready |
| Week 8: APIs, HTTP | [📝 Workbook →](Week8_APIs_HTTP.md) | Not started |
| Weeks 9: Virtual Environments | [📝 Workbook →](Week9_VirtualEnvs_Modules_ErrorHandling.md) | Not started |
| Week 10: Git | [📝 Workbook →](Week10_Git_VersionControl.md) | Not started |
| Weeks 11-12: Docker/Cloud | [📝 Workbook →](Week11_Cloud_AWS_Basics.md) + [📝 Workbook →](Week12_Docker_Basics.md) | Not started |
| Phase 2: Data Engineering | ⏳Pending | Not started |
| Phase 3: Applied AI/ML | ⏳Pending | Not started |
| Phase 4: AI Ops Specialization | ⏳Pending | Not started |

---

### Lab Environment
- **Server**: Ubuntu 24.04 (web-server) - 31GB RAM
- **Location**: ~/projects/ai-operator-foundations/aiops-track/ (moved from ~/lab/ in Oct 2026)
- **Toolkit**: ~/projects/ai-operator-foundations/aiops-track/tools/sysadmin-toolkit/
- **Notes**: ~/projects/ai-operator-foundations/aiops-track/notes/