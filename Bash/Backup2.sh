#!/bin/bash

# Prompt for backup directory, use default if empty
read -p "Enter backup directory (default: ~/backups): " BACKUP_DIR
BACKUP_DIR="${BACKUP_DIR:-$HOME/backups}"
mkdir -p "$BACKUP_DIR"

# Function to backup directory
backup() {
    local src="$1"
    local timestamp=$(date +"%Y%m%d_%H%M%S")
    if [ -d "$src" ]; then
        tar -czf "$BACKUP_DIR/$(basename "$src")_$timestamp.tar.gz" -C "$(dirname "$src")" "$(basename "$src")"
        echo "Backup of directory '$src' created."
    elif [ -f "$src" ]; then
        cp "$src" "$BACKUP_DIR/$(basename "$src")_$timestamp.bak"
        echo "Backup of file '$src' created."
    else
        echo "Error: '$src' is not a valid file or directory."
    fi
}

# Main script
echo "1. Backup Directory"
echo "2. Backup Single File"
read -p "Select option (1 or 2): " option

read -p "Enter path to backup: " PATH_TO_BACKUP
case "$option" in
    1) backup "$PATH_TO_BACKUP" ;;
    2) backup "$PATH_TO_BACKUP" ;;
    *) echo "Invalid option." ;;
esac

