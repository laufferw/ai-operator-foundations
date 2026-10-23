#!/usr/bin/env python3
"""
Python Basics - Week 5 Practice
Run this script to see Python fundamentals in action
"""

# ============================================
# VARIABLES AND DATA TYPES
# ============================================

# Strings
name = "William"
role = "Revenue Operations"
target_role = "AI Operations Engineer"

print("=" * 50)
print("VARIABLES AND DATA TYPES")
print("=" * 50)

print(f"\nName: {name}")
print(f"Current Role: {role}")
print(f"Target Role: {target_role}")

# Numbers
age = 30
years_experience = 15
learning_progress = 0.25  # 25% through Phase 1

print(f"\nAge: {age}")
print(f"Years Experience: {years_experience}")
print(f"Learning Progress: {learning_progress:.0%}")

# Booleans
is_learning = True
has_linux_skills = True
has_python_skills = False

print(f"\nCurrently Learning: {is_learning}")
print(f"Has Linux Skills: {has_linux_skills}")
print(f"Has Python Skills: {has_python_skills}")

# Lists
current_skills = ["Linux CLI", "Bash Scripting", "RevOps"]
skills_to_learn = ["Python", "Git", "Docker", "Cloud", "ML"]

print(f"\nCurrent Skills: {current_skills}")
print(f"Skills to Learn: {skills_to_learn}")

# Dictionaries
career_profile = {
    "name": name,
    "current_role": role,
    "target_role": target_role,
    "phase": "DevOps Foundations",
    "week": 5
}

print(f"\nCareer Profile: {career_profile}")

print("\n" + "=" * 50)
print("DATA TYPE CHECKS")
print("=" * 50)

print(f"\nType of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of is_learning: {type(is_learning)}")
print(f"Type of current_skills: {type(current_skills)}")
print(f"Type of career_profile: {type(career_profile)}")

# ============================================
# CONTROL FLOW
# ============================================

print("\n" + "=" * 50)
print("CONTROL FLOW - IF/ELIF/ELSE")
print("=" * 50)

# Check learning phase
phase = "Phase 1"
if phase == "Phase 1":
    print("\nCurrently in DevOps Foundations")
elif phase == "Phase 2":
    print("\nCurrently in Data Engineering")
elif phase == "Phase 3":
    print("\nCurrently in Applied AI/ML")
else:
    print("\nIn AI Ops Specialization")

print("\n" + "=" * 50)
print("CONTROL FLOW - FOR LOOPS")
print("=" * 50)

# Iterate through skills to learn
print("\nMy Learning Path:")
for i, skill in enumerate(skills_to_learn, 1):
    print(f"  {i}. {skill}")

print("\n" + "=" * 50)
print("LIST COMPREHENSIONS")
print("=" * 50)

# Create derived lists using comprehension
skill_lengths = [len(skill) for skill in skills_to_learn]
print(f"\nSkill lengths: {skill_lengths}")

# Square numbers 1-5
squares = [x**2 for x in range(1, 6)]
print(f"Squares (1-5): {squares}")

# ============================================
# FUNCTIONS
# ============================================

print("\n" + "=" * 50)
print("FUNCTIONS")
print("=" * 50)

def greet(person_name):
    """Greet a person by name."""
    return f"Hello, {person_name}! Welcome to your AI Ops journey."

def calculate_progress(weeks_complete, total_weeks):
    """Calculate learning progress percentage."""
    return (weeks_complete / total_weeks) * 100

def get_career_summary(name, current, target, phase):
    """Return a formatted career summary."""
    return f"""
    ╔══════════════════════════════════════════╗
    ║         CAREER SUMMARY                   ║
    ╠══════════════════════════════════════════╣
    ║ Name: {name:<30} ║
    ║ Current: {current:<28} ║
    ║ Target: {target:<27} ║
    ║ Phase: {phase:<30} ║
    ╚══════════════════════════════════════════╝
    """

# Test the functions
print(f"\n{greet(name)}")
progress = calculate_progress(4, 34)
print(f"\nProgress: {progress:.1f}%")
print(get_career_summary(name, role, target_role, "DevOps Foundations"))

# ============================================
# PRACTICE EXERCISES
# ============================================

print("\n" + "=" * 50)
print("PRACTICE OUTPUT")
print("=" * 50)

# Exercise 1: Use a dictionary
print("\n--- Exercise 1: Dictionary Access ---")
print(f"My name is {career_profile['name']}")
print(f"I'm in {career_profile['phase']}, Week {career_profile['week']}")

# Exercise 2: Modify a list
print("\n--- Exercise 2: List Manipulation ---")
current_skills.append("Python")
current_skills.append("Git")
print(f"Updated skills: {current_skills}")

# Exercise 3: String formatting
print("\n--- Exercise 3: String Formatting ---")
message = "I'm {} years old, transitioning from {} to {}"
formatted = message.format(age, role, target_role)
print(formatted)

print("\n" + "=" * 50)
print("PYTHON BASICS - COMPLETE!")
print("=" * 50)
print("\nNext: Build your disk usage analyzer!")
print("Edit: ~/lab/tools/python-scripts/disk_usage.py")