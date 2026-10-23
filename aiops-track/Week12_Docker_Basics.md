# Week 12: Docker Basics

> 📍 **Part of:** [AI Ops Career Roadmap](../AIOps_Roadmap.md) — Phase 1: DevOps Foundations

**← Previous Week:** [Cloud & AWS Basics](Week11_Cloud_AWS_Basics.md)

---

## 📋 Learning Objectives

| Topic | What You'll Learn |
|-------|-------------------|
| **Docker Concepts** | Images, containers, registries |
| **Docker Commands** | run, build, pull, ps, exec |
| **Dockerfiles** | Building custom images |
| **Docker Compose** | Multi-container applications |

## 🎯 Why These Matter for AI Ops

- **Consistency**: Same environment from dev to production
- **Isolation**: ML models run in their own containers
- **Portability**: Run anywhere Docker is installed
- **CI/CD**: Images get built and deployed automatically

---

## 📚 Concept 1: Docker Fundamentals

### What is Docker?

Docker packages applications with their dependencies into containers.

```
┌──────────────────────────────────────────────────┐
│                   Docker Host                     │
│                                                   │
│  ┌────────────────┐   ┌────────────────┐       │
│  │  Container 1   │   │  Container 2   │       │
│  │  Python App    │   │  Redis Cache   │       │
│  │  ───────────   │   │  ───────────   │       │
│  │  + Python 3.11│   │  + Redis 7.0   │       │
│  │  + Flask 2.3   │   │                │       │
│  │  + Pandas 2.1  │   │                │       │
│  └────────────────┘   └────────────────┘       │
│                                                   │
│  ┌──────────────────────────────────────────┐   │
│  │           Docker Engine                    │   │
│  └──────────────────────────────────────────┘   │
└──────────────────────────────────────────────────┘
```

### Key Terms

| Term | Definition |
|------|------------|
| **Image** | Template for a container (like a class) |
| **Container** | Running instance of an image (like an object) |
| **Dockerfile** | Script that defines how to build an image |
| **Registry** | Place to store and share images (Docker Hub) |

---

## 📚 Concept 2: Essential Docker Commands

### Pulling Images

```bash
# Pull official image
docker pull python:3.11

# Pull specific tag
docker pull python:3.11-slim

# Pull from different registry
docker pull redis:7-alpine
```

### Running Containers

```bash
# Run a container (creates and starts)
docker run python:3.11 python --version

# Run in background (detached)
docker run -d redis

# Run with port mapping
docker run -d -p 8080:80 nginx

# Run with volume mount
docker run -v /my/data:/data python:3.11

# Run with environment variables
docker run -d -e POSTGRES_PASSWORD=secret postgres
```

### Managing Containers

```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop container_id

# Remove a container
docker rm container_id

# View container logs
docker logs -f container_id

# Execute command in running container
docker exec -it container_id bash
```

### Managing Images

```bash
# List images
docker images

# Remove an image
docker rmi image_id

# Remove unused images
docker image prune
```

---

## 📚 Concept 3: Building Custom Images

### Dockerfile Basics

```dockerfile
# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files from host to container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Environment variables
ENV APP_ENV=production

# Expose port
EXPOSE 8080

# Default command
CMD ["python", "app.py"]
```

### Building an Image

```bash
# Build from Dockerfile in current directory
docker build -t my-app:latest .

# Build with specific dockerfile
docker build -f Dockerfile.dev -t my-app:dev .
```

### Example: Python Script Container

```dockerfile
# Dockerfile for disk_usage.py
FROM python:3.11-slim

WORKDIR /app

COPY disk_usage.py .

CMD ["python", "disk_usage.py"]
```

### Building and Running

```bash
# Build
docker build -t disk-usage:latest .

# Run
docker run --rm disk-usage:latest
```

---

## 📚 Concept 4: Docker Compose

### What is Docker Compose?

A tool for defining and running multi-container applications.

### docker-compose.yml

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgres://db:5432/mydb
    depends_on:
      - db
      - redis

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=mydb
    volumes:
      - db-data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  db-data:
```

### Compose Commands

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Scale a service
docker-compose up -d --scale app=3
```

---

## 📝 Weekly Project

### Task: Containerize Your Python Script

**Objective:** Create a Dockerfile for one of your Python scripts and run it as a container.

### Steps

#### 1. Create a Dockerfile

```bash
cd ~/lab/tools/python-scripts

# Create Dockerfile for disk_usage.py
cat > Dockerfile << 'EOF'
FROM python:3.11-slim

WORKDIR /app

# Install any dependencies if needed
# RUN pip install pyyaml

COPY disk_usage.py .

CMD ["python", "disk_usage.py"]
EOF
```

#### 2. Build the Image

```bash
docker build -t disk-usage:latest .
```

#### 3. Run the Container

```bash
# Run with default directory (/)
docker run --rm disk-usage:latest

# Run with specific directory
docker run --rm -v /var/log:/app disk-usage:latest /app
```

#### 4. (Bonus) Create docker-compose.yml

```yaml
version: '3.8'

services:
  disk-usage:
    build: .
    volumes:
      - /:/data
    command: ["python", "disk_usage.py", "/data"]
```

#### 5. (Bonus) Run with Compose

```bash
docker-compose up
```

---

## ✅ Progress Log

```markdown
## Week 12: Docker Basics

### Progress
- [ ] Completed daily practice: __/__ days
- [ ] Pulled Docker images
- [ ] Ran containers
- [ ] Created Dockerfile
- [ ] Built custom image
- [ ] (Bonus) Created docker-compose.yml
- [ ] Notes documented

### What I Learned
-

### Challenges Faced
-

### Questions for Next Week
-

### Readiness Check
- [ ] Can pull and run Docker images
- [ ] Can create a Dockerfile
- [ ] Can build custom images
- [ ] Can use Docker Compose
- [ ] Ready for Phase 2: Yes / No
```

---

## 📖 Resources

- [Docker Getting Started](https://docs.docker.com/get-started/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)
- [Awesome Docker](https://github.com/veggiemonk/awesome-docker)

---

## 🎉 Phase 1 Complete!

You've completed DevOps Foundations!

### What You've Learned

- Linux command line navigation
- Python automation scripting
- File I/O, JSON, YAML, Regex
- API interactions
- Virtual environments and modules
- Git version control
- Cloud computing (AWS EC2)
- Docker containerization

### What's Next

**Phase 2: Data Engineering for Ops** (Weeks 13-22)
- Time-series databases (InfluxDB, Prometheus)
- Log aggregation (ELK stack)
- Data pipelines (Airflow, Prefect)
- Feature engineering

---

*Week 12 - DevOps Foundations Phase*  
*Last Updated: May 2025*

---

**[← Back to AI Ops Roadmap](../AIOps_Roadmap.md)**