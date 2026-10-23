# Week 10: Git & Version Control

> 📍 **Part of:** [AI Ops Career Roadmap](AIOps_Roadmap.md) — Phase 1: DevOps Foundations

**← Previous Week:** [Virtual Environments, Modules](Week9_VirtualEnvs_Modules_ErrorHandling.md)

---

## 📋 Learning Objectives

| Topic | What You'll Learn |
|-------|-------------------|
| **Git Basics** | init, add, commit, status |
| **Remote Repositories** | push, pull, fetch, clone |
| **Branching** | branch, checkout, merge, rebase |
| **Git Workflows** | Branching strategies, code review |

## 🎯 Why These Matter for AI Ops

- **Config as Code**: Store infrastructure configs in Git
- **Collaboration**: Work with team members on automation scripts
- **Change Tracking**: Know who changed what and when
- **Rollback**: Revert to previous working state if needed

---

## 📚 Concept 1: Git Basics

### Initializing a Repository

```bash
# Create a new directory
mkdir my-aiops-project
cd my-aiops-project

# Initialize Git
git init

# Check status
git status
```

### Checking Status

```bash
# Shows current state
git status

# Short status
git status -s
```

### Staging and Committing

```bash
# Add a specific file
git add config.yaml

# Add all files
git add .

# Add all files with pattern
git add *.py

# Commit with message
git commit -m "Add initial configuration"

# Add and commit in one command (for tracked files)
git commit -am "Update config"
```

### Viewing History

```bash
# View commit history
git log

# One line per commit
git log --oneline

# With graph
git log --oneline --graph --all
```

### Undoing Changes

```bash
# Discard changes to a file
git checkout -- config.yaml

# Remove from staging
git reset HEAD config.yaml

# Amend last commit (if you forgot something)
git commit --amend -m "Updated message"
```

---

## 📚 Concept 2: Remote Repositories

### What is a Remote?

A remote is a version of your repository hosted somewhere else (GitHub, GitLab, etc.).

```bash
# List remotes
git remote -v

# Add a remote
git remote add origin https://github.com/username/repo.git

# Rename remote
git remote rename origin upstream
```

### Cloning a Repository

```bash
# Clone an existing repository
git clone https://github.com/kubernetes/kubernetes.git

# Clone with a specific folder name
git clone https://github.com/kubernetes/kubernetes.git k8s
```

### Pushing to Remote

```bash
# Push commits to remote
git push origin main

# Push and set upstream (tracks the branch)
git push -u origin feature/my-feature
```

### Pulling Changes

```bash
# Pull and merge in one command
git pull origin main

# Fetch first, then merge (cleaner)
git fetch origin
git merge origin/main
```

### Fetching

```bash
# Download changes but don't merge
git fetch origin

# Fetch all remotes
git fetch --all
```

---

## 📚 Concept 3: Branching

### Creating Branches

```bash
# Create a new branch
git branch feature/add-logging

# Create and switch to new branch
git checkout -b feature/add-logging

# List all branches
git branch -a

# List branches with last commit
git branch -v
```

### Switching Branches

```bash
# Switch to existing branch
git checkout main

# Switch to previous branch
git checkout -
```

### Merging Branches

```bash
# Ensure you're on main branch
git checkout main

# Merge feature branch into main
git merge feature/add-logging

# Delete branch after merge
git branch -d feature/add-logging
```

### Handling Merge Conflicts

```bash
# When merge conflicts occur:
# 1. Edit the files with conflicts
# 2. Mark as resolved
git add conflicted_file.py

# 3. Complete the merge
git commit -m "Resolve merge conflicts"
```

### Rebasing (Alternative to Merging)

```bash
# Rebase feature branch onto main
git checkout feature/my-feature
git rebase main

# This creates a cleaner linear history
```

---

## 📚 Concept 4: Git Workflows

### Basic Workflow

```
1. Clone repo (first time)
2. Create feature branch
3. Make changes
4. Commit changes
5. Push branch to remote
6. Create Pull Request
7. Review and merge
```

### Branching Strategies

#### Feature Branch Workflow
```
main ----●----●----●----●
          \
feature --●----●
```

#### GitFlow
```
main ----●----●----●----●----●----●
          \                   \
release --●----●             (hotfix)
            \                         
develop --●----●----●----●----●----●
              \           \
feature ----●----●----●----●
```

### Best Practices

| Practice | Why It Matters |
|----------|----------------|
| **Meaningful commit messages** | Future you will thank present you |
| **Small, focused commits** | Easier to review and rollback |
| **Never force push to main** | Can break shared history |
| **Use branches for everything** | Keeps main stable |
| **Review before merging** | Catches bugs early |

### Example Workflow

```bash
# 1. Start work
git checkout main
git pull origin main
git checkout -b feature/ai-logging

# 2. Make changes
echo "logging_level = INFO" >> config.py
git add config.py
git commit -m "Add logging configuration"

# 3. Push and create PR
git push -u origin feature/ai-logging
# Then go to GitHub to create Pull Request
```

---

## 📝 Weekly Project

### Task: Set Up Git Workflow for Your Lab

**Objective:** Initialize a Git repository for your sysadmin-toolkit, create meaningful commits, and push to GitHub.

### Project Requirements

1. Initialize a Git repo in your toolkit directory
2. Create a proper `.gitignore` file
3. Make at least 5 meaningful commits
4. Create a GitHub repo and push your code

### Steps

#### Step 1: Initialize and Configure

> The toolkit now lives inside the `ai-operator-foundations` repo, so copy it out
> to practice starting a repo from scratch:
> `cp -r ~/projects/ai-operator-foundations/aiops-track/tools/sysadmin-toolkit ~/sysadmin-toolkit`

```bash
cd ~/sysadmin-toolkit

# Configure Git (if not already)
git config user.name "Your Name"
git config user.email "your@email.com"

# Initialize
git init
```

#### Step 2: Create .gitignore

```bash
# Create .gitignore
cat > .gitignore << EOF
# Python
__pycache__/
*.pyc
*.pyo
.venv/
venv/
*.egg-info/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Secrets
*.key
.env
EOF
```

#### Step 3: Make Commits

```bash
# First commit - initial structure
git add .
git commit -m "Initial commit: Add sysadmin toolkit structure"

# Add files and commit
git add recent-changes.sh
git commit -m "Add recent-changes script for finding modified files"

# Continue with more commits...
```

#### Step 4: Push to GitHub

```bash
# Create GitHub repo first at github.com/new
# Then add remote and push

git remote add origin https://github.com/YOUR_USERNAME/sysadmin-toolkit.git
git branch -M main
git push -u origin main
```

---

## ✅ Progress Log

```markdown
## Week 10: Git & Version Control

### Progress
- [ ] Completed daily practice: __/__ days
- [ ] Set up Git config
- [ ] Created .gitignore
- [ ] Made meaningful commits
- [ ] Pushed to GitHub
- [ ] Notes documented

### What I Learned
-

### Challenges Faced
-

### Questions for Next Week
-

### Readiness Check
- [ ] Can initialize repos and create commits
- [ ] Can add remotes and push/pull
- [ ] Can create and merge branches
- [ ] Can resolve simple merge conflicts
- [ ] Ready to move on: Yes / No
```

---

## 📖 Resources

- [Pro Git Book - Free](https://git-scm.com/book)
- [GitHub Skills](https://github.com/skills)
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Common git mistakes and fixes
- [Git Interactive Cheatsheet](https://ndpsoftware.com/git-cheatsheet.html)

---

## 🔜 Next Up (Week 11)

- [Cloud & AWS Basics →](Week11_Cloud_AWS_Basics.md)

---

*Week 10 - DevOps Foundations Phase*  
*Last Updated: May 2025*

---

**[← Back to AI Ops Roadmap](AIOps_Roadmap.md)**