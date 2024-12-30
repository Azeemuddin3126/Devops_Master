#!/bin/bash

# Configuration
SOURCE_DIR="/path/to/source/directory"    # Replace with the path of the directory you want to back up
BACKUP_DIR="/path/to/backup/directory"    # Replace with the path where backups should be stored
DATE=$(date +'%Y-%m-%d_%H-%M-%S')         # Timestamp for the backup file name
BACKUP_FILE="backup_$DATE.tar.gz"         # Backup file name with timestamp

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Perform the backup using tar
tar -czf "$BACKUP_DIR/$BACKUP_FILE" -C "$SOURCE_DIR" .

# Check if the backup was successful
if [ $? -eq 0 ]; then
    echo "Backup successful: $BACKUP_DIR/$BACKUP_FILE"
else
    echo "Backup failed!"
    exit 1
fi
