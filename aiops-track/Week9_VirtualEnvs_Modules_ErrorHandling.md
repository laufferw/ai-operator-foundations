# Week 9: Virtual Environments, Modules & Error Handling

> 📍 **Part of:** [AI Ops Career Roadmap](../AIOps_Roadmap.md) — Phase 1: DevOps Foundations

**← Previous Week:** [APIs & HTTP](Week8_APIs_HTTP.md)

---

## 📋 Learning Objectives

| Topic | What You'll Learn |
|-------|-------------------|
| **Virtual Environments** | Isolated Python environments per project |
| **pip** | Package management, requirements files |
| **Python Modules** | Creating and importing your own modules |
| **Error Handling** | Try/except, custom exceptions, logging |

## 🎯 Why These Matter for AI Ops

- **Virtual Environments**: Different projects need different package versions (e.g., ML projects vs. automation scripts)
- **pip**: Installing monitoring tools, API clients, data处理 libraries
- **Modules**: Reusable code across your automation scripts
- **Error Handling**: Critical for production scripts that run unattended

---

## 📚 Concept 1: Virtual Environments

### Why Use Virtual Environments?

Without venv, all projects share the same Python packages. This causes conflicts:
- Project A needs `requests==2.28.0`
- Project B needs `requests==2.31.0`

**Solution:** Each project gets its own isolated environment.

### Creating a Virtual Environment

```bash
# Create a new virtual environment
python3 -m venv myproject-env

# Activate it (Linux/macOS)
source myproject-env/bin/activate

# Activate it (Windows)
myproject-env\Scripts\activate
```

### Using the Virtual Environment

```bash
# Once activated, packages you install go here
pip install requests
pip install pandas

# See installed packages
pip list

# Freeze requirements to share
pip freeze > requirements.txt
```

### The requirements.txt File

```text
requests==2.31.0
pandas==2.1.0
pyyaml==6.0.1
```

### Installing from Requirements

```bash
# On another machine or new environment
pip install -r requirements.txt

# Deactivate when done
deactivate
```

### Best Practice for AI Ops

```bash
# Create a project-specific venv
cd ~/lab/tools/python-scripts/
python3 -m venv .venv

# Activate
source .venv/bin/activate

# Install packages
pip install requests pyyaml pandas

# Save dependencies
pip freeze > requirements.txt
```

---

## 📚 Concept 2: Python Modules

### What is a Module?

A Python file (`.py`) that can be imported into other scripts. This lets you reuse code across projects.

### Creating a Module

```python
# ~/lab/tools/python-scripts/mymodule.py

def greet(name):
    return f"Hello, {name}!"

def calculate_sum(numbers):
    return sum(numbers)

# Can also have variables
VERSION = "1.0.0"
```

### Importing a Module

```python
# Import the whole module
import mymodule

print(mymodule.greet("William"))
print(mymodule.calculate_sum([1, 2, 3]))

# Or import specific items
from mymodule import greet, VERSION
print(greet("Ops Team"))
print(f"Version: {VERSION}")
```

### Organizing Modules

```
~/lab/tools/python-scripts/
├── mymodule.py
├── another_module.py
└── scripts/
    ├── main.py
    └── helpers/
        ├── __init__.py  # Makes this a package
        └── utils.py
```

### The __init__.py File

```python
# scripts/helpers/__init__.py
# This makes 'helpers' a package that can be imported

from .utils import format_timestamp, parse_config
```

---

## 📚 Concept 3: Error Handling

### Try/Except Basics

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Catching Multiple Exceptions

```python
try:
    response = requests.get(url)
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### The Else and Finally

```python
try:
    file = open('config.yaml', 'r')
    data = yaml.safe_load(file)
except FileNotFoundError:
    print("Config file not found!")
else:
    print("Config loaded successfully!")
    print(data['app']['name'])
finally:
    # This always runs
    if 'file' in locals():
        file.close()
```

### Raising Exceptions

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")  # Error: Cannot divide by zero
```

### Custom Exceptions

```python
class ConfigurationError(Exception):
    """Raised when config file is invalid or missing."""
    pass

def load_config(filename):
    if not os.path.exists(filename):
        raise ConfigurationError(f"Config file not found: {filename}")
    # ... rest of loading code
```

---

## 📝 Weekly Project

### Task: Service Health Checker

**Objective:** Create a Python tool that checks if services are running and restarts them if not.

This simulates real AI Ops work - monitoring services and taking automated action.

### Project Requirements

1. Create a virtual environment
2. Create a module with helper functions
3. Write a script that:
   - Checks if specified services are running
   - Reports their status
   - Takes action if they're down

### Structure

```
~/lab/tools/python-scripts/
├── service_checker/
│   ├── __init__.py
│   ├── checker.py     # Module with checking functions
│   └── main.py        # Main script
└── requirements.txt
```

### Starter Code

```python
#!/usr/bin/env python3
"""
Week 9 Project: Service Health Checker
Task: Check if services are running and report status
"""

import subprocess
import sys
from checker import check_service, restart_service

def main():
    services = ['nginx', 'docker', 'ssh']
    
    print("🔍 Checking services...")
    print("=" * 40)
    
    for service in services:
        is_running = check_service(service)
        
        if is_running:
            print(f"✓ {service}: RUNNING")
        else:
            print(f"✗ {service}: NOT RUNNING")
            # TODO: Ask to restart or auto-restart
            response = input(f"  Restart {service}? (y/n): ")
            if response.lower() == 'y':
                restart_service(service)
    
    print("=" * 40)
    print("Check complete!")

if __name__ == "__main__":
    main()
```

### The checker.py Module

```python
# checker.py - Service checking module

import subprocess

def check_service(service_name):
    """
    Check if a systemd service is running.
    
    Returns:
        True if running, False otherwise
    """
    # TODO: Use systemctl to check service status
    # Hint: subprocess.run with check=True can work
    pass

def restart_service(service_name):
    """
    Restart a systemd service.
    """
    # TODO: Use systemctl to restart service
    pass

def get_service_status(service_name):
    """
    Get detailed status of a service.
    """
    # TODO: Return status information
    pass
```

### Hints

1. **Check service with systemctl:**
   ```bash
   systemctl is-active nginx
   ```

2. **Using subprocess safely:**
   ```python
   result = subprocess.run(
       ['systemctl', 'is-active', service_name],
       capture_output=True,
       text=True
   )
   return result.returncode == 0
   ```

3. **Remember to activate your venv!**

---

## ✅ Progress Log

```markdown
## Week 9: Virtual Environments, Modules, Error Handling

### Progress
- [ ] Created virtual environment
- [ ] Completed daily practice: __/__ days
- [ ] Finished weekly project (service_checker.py)
- [ ] Created requirements.txt
- [ ] Notes documented

### What I Learned
-

### Challenges Faced
-

### Questions for Next Week
-

### Readiness Check
- [ ] Can create and activate virtual environments
- [ ] Can use pip to manage packages
- [ ] Can create and import Python modules
- [ ] Can handle errors with try/except
- [ ] Ready to move on: Yes / No
```

---

## 📖 Resources

- [Python venv Documentation](https://docs.python.org/3/library/venv.html)
- [pip User Guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- [Real Python - Modules and Packages](https://realpython.com/python-modules-packages/)
- [Python Exception Handling](https://docs.python.org/3/tutorial/errors.html)

---

## 🔜 Next Up (Week 10)

- [Git & Version Control →](Week10_Git_VersionControl.md)

---

*Week 9 - DevOps Foundations Phase*  
*Last Updated: May 2025*

---

**[← Back to AI Ops Roadmap](../AIOps_Roadmap.md)**