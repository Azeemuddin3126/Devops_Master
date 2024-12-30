#!/bin/bash

# Define Variables
LOG_DIR="/var/log/myapp"
LOG_FILE="app.log"
ARCHIVE_DIR="/var/log/myapp/archives"
DAYS_TO_KEEP=30

# Create archive directory if it doesn't exist
mkdir -p "$ARCHIVE_DIR"

# Rotate the logs (compress the current log file and move it to archives)
log_date=$(date +"%Y-%m-%d_%H-%M-%S")
mv "$LOG_DIR/$LOG_FILE" "$ARCHIVE_DIR/$LOG_FILE.$log_date.gz"
gzip "$ARCHIVE_DIR/$LOG_FILE.$log_date"

# Clean up old logs (older than $DAYS_TO_KEEP)
find "$ARCHIVE_DIR" -type f -name "*.gz" -mtime +$DAYS_TO_KEEP -exec rm {} \;

# Create a new empty log file
touch "$LOG_DIR/$LOG_FILE"

echo "Log rotation completed: $log_date."
