#!/bin/bash

# Backup Script - saves copies of important files!
# Made by a sixth grader (William) learning Linux

echo "Starting backup..."

# Create a timestamp (date and time)
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%s)

# Create a backup folder with today's date
BACKUP_DIR="$HOME/lab/backup/$TIMESTAMP"
mkdir -p "$BACKUP_DIR"

# Copy the sysadmin-toolkit to backup
cp -r ~/lab/tools/sysadmin-toolkit/* "$BACKUP_DIR/"

echo ":checkmark: Backup complete!"
echo ":folder: Files saved to: $BACKUP_DIR/"
ls -la "$BACKUP_DIR"
