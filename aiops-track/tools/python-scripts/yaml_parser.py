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