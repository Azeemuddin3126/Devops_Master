#!/bin/bash

# Define Variables
NAMESPACE="default"
DEPLOYMENT_NAME="myapp"
CPU_THRESHOLD=75
MIN_REPLICAS=2
MAX_REPLICAS=10

# Get current CPU utilization for the deployment
CPU_UTILIZATION=$(kubectl top pods -n "$NAMESPACE" | grep "$DEPLOYMENT_NAME" | awk '{print $3}' | sed 's/%//g')

# Scale the deployment based on CPU usage
if [ "$CPU_UTILIZATION" -gt "$CPU_THRESHOLD" ]; then
  echo "CPU utilization is high ($CPU_UTILIZATION%). Scaling up the deployment."
  kubectl scale deployment "$DEPLOYMENT_NAME" -n "$NAMESPACE" --replicas=$MAX_REPLICAS
else
  echo "CPU utilization is normal ($CPU_UTILIZATION%). Scaling down the deployment."
  kubectl scale deployment "$DEPLOYMENT_NAME" -n "$NAMESPACE" --replicas=$MIN_REPLICAS
fi
