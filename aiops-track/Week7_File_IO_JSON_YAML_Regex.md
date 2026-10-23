# Week 7: File I/O, JSON, YAML, and Regular Expressions

> 📍 **Part of:** [AI Ops Career Roadmap](AIOps_Roadmap.md) — Phase 1: DevOps Foundations

## 📋 Learning Objectives

| Topic | What You'll Learn |
|-------|-------------------|
| **File I/O** | Reading/writing text files, context managers |
| **JSON** | Parsing, creating, and manipulating JSON data |
| **YAML** | Config file handling (widely used in DevOps) |
| **Regex** | Pattern matching for log parsing, text extraction |

## 🎯 Why These Matter for AI Ops

- **YAML/JSON**: Most configuration files (Docker, Kubernetes, CI/CD pipelines) use these formats
- **File I/O**: You'll need to process logs, configs, and data exports
- **Regex**: Essential for parsing log files, extracting metrics, and alerting patterns

---

## 📚 Concept 1: File I/O in Python

### The Basics

```python
# Basic file reading
with open('filename.txt', 'r') as f:
    content = f.read()  # Reads entire file

# Reading lines one by one
with open('filename.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Writing to files
with open('output.txt', 'w') as f:
    f.write("Hello, Ops!")

# Appending to files
with open('log.txt', 'a') as f:
    f.write("New log entry\n")
```

### Key Points

- The `with` statement ensures the file is properly closed (even if errors occur)
- `'r'` = read mode, `'w'` = write mode (overwrites!), `'a'` = append mode
- Always close files or use `with` to avoid resource leaks

### Practice Task

```python
# Read a file and count lines
with open('log.txt', 'r') as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")
```

---

## 📚 Concept 2: YAML Handling

### The Why

Kubernetes, Docker Compose, GitHub Actions, Ansible, and many DevOps tools use YAML for configuration. You MUST be able to read and write YAML.

### Loading YAML

```python
import yaml

# Load YAML from a file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)  # Returns a Python dictionary!

# Access nested values
app_name = config['application']['name']
db_host = config['database']['host']
```

### Writing YAML

```python
import yaml

config = {
    'app': 'my-service',
    'version': '1.0',
    'features': ['a', 'b', 'c']
}

with open('output.yaml', 'w') as f:
    yaml.dump(config, f, default_flow_style=False)
```

### ⚠️ Security Note

**Always use `yaml.safe_load()`** - never use `yaml.load()` with untrusted files. The `load()` function can execute arbitrary Python code.

---

## 📚 Concept 3: JSON Handling

### The Why

APIs return JSON, many tools export data as JSON, and it's the standard data interchange format. You'll encounter JSON constantly in AI Ops.

### Loading JSON

```python
import json

# Load JSON from a file
with open('data.json', 'r') as f:
    data = json.load(f)  # Returns a Python dictionary!

# Access values
name = data['name']
items = data['items']
```

### Writing JSON

```python
import json

output = {
    'server': 'web-01',
    'status': 'healthy',
    'metrics': {
        'cpu': 45.2,
        'memory': 1024
    }
}

with open('output.json', 'w') as f:
    json.dump(output, f, indent=2)  # indent=2 for pretty printing
```

### Converting Between Formats

```python
# JSON string to Python dict
json_string = '{"name": "test"}'
data = json.loads(json_string)

# Python dict to JSON string
json_string = json.dumps(data)
```

---

## 📚 Concept 4: Regular Expressions (Regex)

### The Why

Parsing log files, extracting metrics from text, matching error patterns - regex is essential for log analysis in AI Ops.

### Basic Patterns

```python
import re

# Find all matches of a pattern
text = "Errors at 192.168.1.100 and 10.0.0.50"
ips = re.findall(r'\d+\.\d+\.\d+\.\d+', text)
print(ips)  # ['192.168.1.100', '10.0.0.50']

# Check if a pattern exists
if re.search(r'ERROR', text):
    print("Found an error!")

# Extract specific parts using groups
match = re.search(r'(\d+:\d+:\d+)', text)
if match:
    print(f"Time: {match.group(1)}")
```

### Common Patterns

| Pattern | Meaning | Example |
|---------|---------|---------|
| `\d` | Single digit | `5` |
| `\d+` | One or more digits | `123` |
| `\w` | Word character | `a`, `5`, `_` |
| `\w+` | One or more word characters | `hello` |
| `.` | Any character | `a`, `1`, `@` |
| `.*` | Any characters (greedy) | `anything` |
| `^start` | Starts with "start" | `start here` |
| `end$` | Ends with "end" | `the end` |
| `[abc]` | Any of a, b, or c | `a`, `b` |
| `[^abc]` | Not a, b, or c | `x`, `z` |

### Regex for Log Parsing

```python
# Parse a typical log line
# Example: "2024-01-15 14:32:05 ERROR [module] Something went wrong"
log_line = "2024-01-15 14:32:05 ERROR [auth] Invalid password for user admin"

# Extract timestamp
timestamp = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', log_line)
print(timestamp.group(1))  # 2024-01-15 14:32:05

# Extract log level
level = re.search(r'(ERROR|WARN|INFO|DEBUG)', log_line)
print(level.group(1))  # ERROR

# Extract module
module = re.search(r'\[(\w+)\]', log_line)
print(module.group(1))  # auth
```

---

## 📝 Weekly Project

### Task: YAML Config Parser

**Objective:** Parse the `app_config.yaml` file and print specific values in a formatted way.

This simulates real DevOps work - reading application configs and extracting key settings.

### Files Created

1. **Config file:** `~/projects/ai-operator-foundations/aiops-track/tools/python-scripts/app_config.yaml`
2. **Starter template:** `~/projects/ai-operator-foundations/aiops-track/tools/python-scripts/yaml_parser.py`

### The Config File (app_config.yaml)

```yaml
application:
  name: ai-ops-dashboard
  version: 2.1.0
  environment: production
  
database:
  host: db-prod-01.internal
  port: 5432
  name: aiops_metrics
  max_connections: 100
  timeout: 30

monitoring:
  enabled: true
  interval_seconds: 60
  alerting:
    email: ops-team@company.com
    slack_webhook: https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX

metrics:
  retention_days: 90
  aggregation_interval: 5
  exporters:
    - prometheus
    - datadog
    - cloudwatch

features:
  anomaly_detection: true
  predictive_scaling: false
  auto_remediation: true
  log_analysis: true
```

### The Template (yaml_parser.py)

```python
#!/usr/bin/env python3
"""
Week 7 Project: YAML Config Parser
Task: Parse the app_config.yaml file and print specific values in a formatted way
"""

import yaml

def load_config(filename):
    """Load and parse a YAML configuration file."""
    # TODO: Open the file and load YAML content
    pass

def print_app_info(config):
    """Print application name, version, and environment."""
    # TODO: Extract and print these values
    pass

def print_database_info(config):
    """Print database connection details."""
    # TODO: Extract and print host, port, name
    pass

def print_monitoring_info(config):
    """Print monitoring and alerting config."""
    # TODO: Extract alerting email and check if enabled
    pass

def main():
    config = load_config('app_config.yaml')
    
    print("=" * 50)
    print("APPLICATION CONFIGURATION")
    print("=" * 50)
    
    print_app_info(config)
    print_database_info(config)
    print_monitoring_info(config)
    
    # Bonus: Print all enabled features
    print("\n📋 Enabled Features:")
    # TODO: Loop through and list enabled features

if __name__ == "__main__":
    main()
```

### Hints

1. **YAML loads as a nested dictionary** - access values like:
   ```python
   config['application']['name']
   ```

2. **To load YAML:**
   ```python
   with open(filename, 'r') as f:
       return yaml.safe_load(f)
   ```

3. **To print database info:**
   ```python
   db = config['database']
   print(f"Host: {db['host']}")
   print(f"Port: {db['port']}")
   ```

### Expected Output

```
==================================================
APPLICATION CONFIGURATION
==================================================
📦 Application: ai-ops-dashboard
   Version: 2.1.0
   Environment: production

🗄️  Database Connection:
   Host: db-prod-01.internal
   Port: 5432
   Name: aiops_metrics

🔔 Monitoring:
   Enabled: True
   Check Interval: 60s
   Alert Email: ops-team@company.com

📋 Enabled Features:
   ✓ anomaly_detection
   ✗ predictive_scaling
   ✓ auto_remediation
   ✓ log_analysis
```

---

## ✅ Progress Log

```markdown
## Week 7: File I/O, JSON/YAML, Regex

### Progress
- [ ] Completed daily practice: __/__ days
- [ ] Finished weekly project (yaml_parser.py)
- [ ] Notes documented

### What I Learned
-

### Challenges Faced
-

### Questions for Next Week
-

### Readiness Check
- [ ] Can read/write files using context managers
- [ ] Can parse YAML config files
- [ ] Can work with JSON data
- [ ] Can use regex to extract patterns from text
- [ ] Ready to move on: Yes / No
```

---

## 📖 Resources

### YAML
- [PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)
- [YAML Tutorial (DigitalOcean)](https://www.digitalocean.com/community/tutorials/an-introduction-to-yaml-in-python)

### JSON
- [Python JSON Docs](https://docs.python.org/3/library/json.html)

### Regex
- [Regex One - Interactive Tutorial](https://regexone.com/)
- [Regex Cheat Sheet](https://www.rexegg.com/regex-quickstart.html)
- [Debuggex - Visual Regex Tester](https://www.debuggex.com/)

### Practice
- [Real Python - Working with Files](https://realpython.com/working-with-files-in-python/)
- [Automate the Boring Stuff - Files](https://automatetheboringstuff.com/2e/chapter9/)

---

## 🔜 Next Up (Week 8)

- [Working with APIs →](Week8_APIs_HTTP.md)
- HTTP methods (GET, POST, PUT, DELETE)
- Fetching and parsing JSON from APIs

---

*Week 7 - DevOps Foundations Phase*  
*Last Updated: May 2025*

---

**[← Back to AI Ops Roadmap](AIOps_Roadmap.md)**