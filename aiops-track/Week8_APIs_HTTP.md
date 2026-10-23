# Week 8: Working with APIs

> 📍 **Part of:** [AI Ops Career Roadmap](AIOps_Roadmap.md) — Phase 1: DevOps Foundations

**← Previous Week:** [File I/O, JSON/YAML, Regex](Week7_File_IO_JSON_YAML_Regex.md)

---

## 📋 Learning Objectives

| Topic | What You'll Learn |
|-------|-------------------|
| **HTTP Basics** | Methods, headers, status codes |
| **Requests Library** | Making GET, POST, PUT, DELETE requests |
| **API Response Handling** | Parsing JSON responses, error handling |
| **Real API Practice** | Working with real-world APIs (GitHub, etc.) |

## 🎯 Why These Matter for AI Ops

- **Monitoring APIs**: Pulling metrics from Prometheus, Datadog, cloud services
- **Incident Management**: Creating tickets in PagerDuty, ServiceNow
- **Automation**: Triggering workflows via webhooks
- **Data Collection**: Fetching operational data for ML pipelines

---

## 📚 Concept 1: HTTP Basics

### HTTP Methods

| Method | Purpose | Example |
|--------|---------|---------|
| **GET** | Retrieve data | Fetch server metrics |
| **POST** | Create new data | Create a support ticket |
| **PUT** | Update existing data | Update a config |
| **DELETE** | Remove data | Delete old logs |

### Status Codes

| Code | Meaning | AI Ops Use Case |
|------|---------|-----------------|
| 200 | OK | Successful API call |
| 201 | Created | Ticket created successfully |
| 400 | Bad Request | Invalid API parameters |
| 401 | Unauthorized | Missing/invalid API key |
| 404 | Not Found | Resource doesn't exist |
| 429 | Too Many Requests | Rate limited - retry later |
| 500 | Server Error | API is down |

---

## 📚 Concept 2: The Requests Library

### Installing

```bash
pip install requests
```

### Basic GET Request

```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # 200
print(response.text)  # Raw response
print(response.json())  # Parsed JSON
```

### GET with Parameters

```python
import requests

# Query parameters
params = {
    'page': 1,
    'per_page': 10,
    'sort': 'created'
}
response = requests.get('https://api.github.com/repos/python/cpython/commits', params=params)
commits = response.json()
```

### GET with Headers

```python
import requests

headers = {
    'Authorization': 'token YOUR_API_TOKEN',
    'Accept': 'application/vnd.github.v3+json'
}
response = requests.get('https://api.github.com/user', headers=headers)
user_data = response.json()
```

### POST Request

```python
import requests

data = {
    'title': 'Server down',
    'body': 'Production server at 192.168.1.100 is not responding',
    'priority': 'high'
}
response = requests.post('https://api.example.com/tickets', json=data)
print(response.status_code)  # 201
```

### Error Handling

```python
import requests

try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()  # Raises exception for 4xx/5xx errors
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

---

## 📚 Concept 3: Working with APIs in Practice

### Example: GitHub API

```python
import requests
import os

# Fetch repository info
def get_repo_info(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data['name'],
            'stars': data['stargazers_count'],
            'forks': data['forks_count'],
            'language': data['language'],
            'description': data['description']
        }
    return None

info = get_repo_info('kubernetes', 'kubernetes')
print(f"Stars: {info['stars']}")
```

### Example: JSONPlaceholder (Free Test API)

```python
import requests

# Get all posts
response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = response.json()

# Get specific post
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
post = response.json()
print(post['title'])

# Create a new post
new_post = {
    'title': 'My Post',
    'body': 'Content here',
    'userId': 1
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
print(response.json())
```

---

## 📝 Weekly Project

### Task: API Data Fetcher

**Objective:** Write a script that fetches JSON data from a public API and saves it to a file.

This simulates real AI Ops work - collecting data from monitoring APIs and storing it for processing.

### Project Requirements

1. Make a GET request to a public API (GitHub API, JSONPlaceholder, etc.)
2. Parse the JSON response
3. Save the data to a file (JSON format)
4. Handle errors gracefully

### Starter Template

```python
#!/usr/bin/env python3
"""
Week 8 Project: API Data Fetcher
Task: Fetch JSON data from an API and save it to a file
"""

import requests
import json
from datetime import datetime

def fetch_data(url, params=None, headers=None):
    """
    Fetch data from an API endpoint.
    
    Args:
        url: API endpoint URL
        params: Optional query parameters
        headers: Optional request headers
    
    Returns:
        JSON data or None on error
    """
    # TODO: Make the request with proper error handling
    pass

def save_to_file(data, filename):
    """Save data to a JSON file with timestamp."""
    # TODO: Write JSON data to file
    pass

def main():
    # Example: Fetch GitHub repository issues
    # TODO: Choose an API and fetch data
    # Hint: Try https://api.github.com/repos/{owner}/{repo}/issues
    
    print("Fetching data from API...")
    # TODO: Call fetch_data function
    
    print("Saving data...")
    # TODO: Call save_to_file function
    
    print("Done!")

if __name__ == "__main__":
    main()
```

### Expected Output

```
Fetching data from API...
Response status: 2024-01-15 14:32:05
Found 10 issues
Saving data...
Done!
Data saved to: github_issues_20240115.json
```

### Hints

1. **Use the `params` parameter** for query strings:
   ```python
   params = {'state': 'all', 'per_page': 30}
   ```

2. **Check status code** before processing:
   ```python
   if response.status_code == 200:
       data = response.json()
   ```

3. **Pretty print when saving:**
   ```python
   json.dump(data, f, indent=2)
   ```

---

## ✅ Progress Log

```markdown
## Week 8: APIs and HTTP

### Progress
- [ ] Completed daily practice: __/__ days
- [ ] Finished weekly project (api_fetcher.py)
- [ ] Notes documented

### What I Learned
-

### Challenges Faced
-

### Questions for Next Week
-

### Readiness Check
- [ ] Can make GET/POST requests with requests library
- [ ] Can handle API errors gracefully
- [ ] Can parse JSON responses
- [ ] Can save API data to files
- [ ] Ready to move on: Yes / No
```

---

## 📖 Resources

- [Requests Library Documentation](https://docs.python-requests.org/)
- [HTTP Methods Tutorial](https://www.restapitutorial.com/lessons/httpmethods.html)
- [GitHub REST API Docs](https://docs.github.com/en/rest)
- [JSONPlaceholder - Free Test API](https://jsonplaceholder.typicode.com/)

---

## 🔜 Next Up (Week 9)

- [Virtual Environments, Modules & Error Handling →](Week9_VirtualEnvs_Modules_ErrorHandling.md)

---

*Week 8 - DevOps Foundations Phase*  
*Last Updated: May 2025*

---

**[← Back to AI Ops Roadmap](AIOps_Roadmap.md)**