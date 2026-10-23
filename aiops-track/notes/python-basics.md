# Python Basics Learning Notes

## Week 5-6: Python Fundamentals

### Variables & Data Types
```python
# Strings
name = "William"
greeting = 'Hello'

# Numbers
age = 30
temperature = 98.6
price = 19.99

# Booleans
is_aiops = True
has_linux_skills = True

# Lists (mutable)
skills = ["Linux", "Bash", "RevOps"]
skills.append("Python")

# Tuples (immutable)
coordinates = (10, 20)

# Dictionaries
person = {
    "name": "William",
    "role": "Revenue Ops",
    "target": "AI Operations"
}
```

### Control Flow
```python
# If/elif/else
if age < 25:
    print("Young professional")
elif age < 40:
    print("Mid-career")
else:
    print("Experienced professional")

# For loops
for skill in skills:
    print(f"Skill: {skill}")

# While loops
count = 0
while count < 5:
    print(count)
    count += 1

# List comprehension
squares = [x**2 for x in range(10)]
```

### Functions
```python
def greet(name):
    """Docstring - describes what function does"""
    return f"Hello, {name}!"

def calculate_disk_usage(path):
    """Calculate total disk usage for a path"""
    total = 0
    # ... implementation
    return total

# Default arguments
def greet_with_default(name="Guest"):
    return f"Hello, {name}!"

# Lambda functions
square = lambda x: x**2
```

### File I/O
```python
# Reading files
with open("file.txt", "r") as f:
    content = f.read()

# Writing files
with open("output.txt", "w") as f:
    f.write("Hello from Python!")

# JSON handling
import json
data = {"key": "value"}
json.dumps(data)  # dict to string
json.loads(string)  # string to dict
```

### Error Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("This always runs")
```

---

## Weekly Project: Disk Usage Analyzer

**Goal:** Write a script that calculates disk usage and prints top 5 largest files

**Approach:**
1. Use `os` module to walk directory tree
2. Use `os.path.getsize()` to get file sizes
3. Sort by size descending
4. Print top 5 with formatted output

**Readiness Check:** Can write a 50-line script without looking up basic syntax