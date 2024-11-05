#!/bin/bash

# Prompt for user input
read -p "Enter your email for alerts: " ALERT_EMAIL
read -p "Enter your Slack webhook URL for alerts (press Enter to skip): " SLACK_WEBHOOK

# Print the system report header
echo "System Report for $(hostname)"

# Print the system information as a tab-separated table
printf "\tReport Date:\t%s\n" "$(printf "%(%Y-%m-%d)T")"
printf "\tKernel Release:\t%s\n" "$(uname -r)"
printf "\tBash Version:\t%s\n" "$BASH_VERSION"
printf "\tAvailable Storage:\t%s\n" "$(df -h / | awk 'NR==2 {print $4}')"
printf "\tAvailable Memory:\t%s\n" "$(free -h | awk '/^Mem:/ {print $7}')"
printf "\tFiles in Directory:\t%s\n" "$(ls | wc -l)"

# Set thresholds
CPU_THRESHOLD=80
MEMORY_THRESHOLD=80
DISK_THRESHOLD=90

# Function to send alerts
send_alert() {
    local message="$1"
    echo "$message" | mail -s "Server Health Alert" "$ALERT_EMAIL"
    if [ -n "$SLACK_WEBHOOK" ]; then  # Check if SLACK_WEBHOOK is not empty
        curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"$message\"}" "$SLACK_WEBHOOK"
    fi
}

# Get metrics
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}')
MEMORY_USAGE=$(free | awk '/Mem/{print $3/$2 * 100.0}')
DISK_USAGE=$(df / | awk '/\//{gsub("%",""); print $5}')

# Generate report
REPORT="Server Health Report:\nCPU: $CPU_USAGE%\nMemory: $MEMORY_USAGE%\nDisk: $DISK_USAGE%\n"

# Check thresholds and send alerts
(( $(echo "$CPU_USAGE > $CPU_THRESHOLD" | bc -l) )) && send_alert "High CPU usage: ${CPU_USAGE}%"
(( $(echo "$MEMORY_USAGE > $MEMORY_THRESHOLD" | bc -l) )) && send_alert "High Memory usage: ${MEMORY_USAGE}%"
(( DISK_USAGE > DISK_THRESHOLD )) && send_alert "High Disk usage: ${DISK_USAGE}%"

# Print report to console
echo -e "$REPORT"

