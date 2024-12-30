#!/bin/bash

# Define Variables
KUBE_NAMESPACE="default"
EMAIL="admin@example.com"
SUBJECT="Kubernetes Pod Failure Alert"
BODY="Some Kubernetes pods are in a failed state. Please check the cluster."

# Get pod status
FAILED_PODS=$(kubectl get pods -n "$KUBE_NAMESPACE" --field-selector=status.phase==Failed -o custom-columns=":metadata.name")

if [ -n "$FAILED_PODS" ]; then
  echo "$BODY" | mail -s "$SUBJECT" "$EMAIL"
  echo "Pod failure alert sent to $EMAIL."
else
  echo "All pods are healthy."
fi

