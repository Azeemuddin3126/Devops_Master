#!/bin/bash

# Prompt for user input
read -p "Enter your email for alerts (leave blank to disable): " ALERT_EMAIL
read -p "Enter your Slack webhook URL for alerts (leave blank to disable): " SLACK_WEBHOOK


# Print system report header
echo -e "\n==================================="
echo -e "System Report for: $(hostname)"
echo -e "Report Generated On: $(date '+%Y-%m-%d %H:%M:%S')"
echo -e "===================================\n"

# Print system information
printf "%-25s %s\n" "Kernel Release:" "$(uname -r)"
printf "%-25s %s\n" "Kernel Release:" "$(uname -a)"
printf "%-25s %s\n" "Bash Version:" "$BASH_VERSION"
printf "%-25s %s\n" "Available Storage:" "$(df -h / | awk 'NR==2 {print $4}')"
printf "%-25s %s\n" "Available Memory:" "$(free -h | awk '/^Mem:/ {print $7}')"
printf "%-25s %s\n" "Files in Directory:" "$(ls | wc -l)"

# Set thresholds
CPU_THRESHOLD=80
MEMORY_THRESHOLD=80
DISK_THRESHOLD=90

# Get metrics
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}')
MEMORY_USAGE=$(free | awk '/Mem/{printf("%.0f", $3/$2 * 100)}')
DISK_USAGE=$(df / | awk '/\//{gsub("%",""); print $5}')

# Generate the health report
REPORT=$(cat <<EOF
===================================
Server Health Report:
===================================
CPU Usage:         ${CPU_USAGE}%
Memory Usage:      ${MEMORY_USAGE}%
Disk Usage:        ${DISK_USAGE}%
===================================
EOF
)

# Print the report
echo -e "$REPORT"


# Check thresholds and send alerts
if (( $(echo "$CPU_USAGE > $CPU_THRESHOLD" | bc -l) )); then
    send_alert "High CPU usage detected: ${CPU_USAGE}%"
fi

if (( $(echo "$MEMORY_USAGE > $MEMORY_THRESHOLD" | bc -l) )); then
    send_alert "High memory usage detected: ${MEMORY_USAGE}%"
fi

if (( DISK_USAGE > DISK_THRESHOLD )); then
    send_alert "High disk usage detected: ${DISK_USAGE}%"
fi


# Function to send alerts
send_alert() {
    local message="$1"
    log_message "ALERT: $message"

    # Send email alert
    if [ -n "$ALERT_EMAIL" ]; then
        echo "$message" | mail -s "Server Health Alert" "$ALERT_EMAIL"
    fi

    # Send Slack alert
    if [ -n "$SLACK_WEBHOOK" ]; then
        curl -X POST -H 'Content-type: application/json' \
             --data "{\"text\":\"$message\"}" "$SLACK_WEBHOOK"
    fi
}
