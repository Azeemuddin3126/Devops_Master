#!/bin/bash

: '
This script is used to manage a GitHub repository, including listing collaborators,
viewing pull requests, and revoking access.
'

#######################################
#  Author   : Azeemuddin Shaik
#  Date     : 10/10/2023
#  Version  : 1.2
########################################

# GitHub API URL
API_URL="https://api.github.com"
ENV_FILE=".env"

# Function to prompt the user for input with a default value
function prompt {
    local message="$1"
    local default="$2"
    read -p "$message [$default]: " input
    echo "${input:-$default}"
}

# Load credentials from .env file or prompt for them if not available
function load_credentials {
    if [[ -f "$ENV_FILE" ]]; then
        source "$ENV_FILE"
    fi

    if [[ -z "$USERNAME" ]]; then
        USERNAME=$(prompt "Enter your GitHub username" "")
        echo "USERNAME=$USERNAME" >> "$ENV_FILE"
    fi

    if [[ -z "$TOKEN" ]]; then
        read -s -p "Enter your GitHub personal access token: " TOKEN
        echo
        echo "TOKEN=$TOKEN" >> "$ENV_FILE"
    fi
}

# Prompt users for repository information
function load_repository_info {
    REPO_OWNER=$(prompt "Enter the repository owner" "$USERNAME")
    REPO_NAME=$(prompt "Enter the repository name" "")
}

# Function to make a GET request to the GitHub API
function github_api_get {
    local endpoint="$1"
    local url="${API_URL}/${endpoint}"

    # Send a GET request to the GitHub API with authentication
    curl -s -u "${USERNAME}:${TOKEN}" "$url"
}

# Function to make a DELETE request to the GitHub API
function github_api_delete {
    local endpoint="$1"
    local url="${API_URL}/${endpoint}"

    # Send a DELETE request to the GitHub API with authentication
    curl -s -u "${USERNAME}:${TOKEN}" -X DELETE "$url"
}

# List collaborators of the repository
function list_collaborators {
    echo -e "\nFetching collaborators for the repository ${REPO_OWNER}/${REPO_NAME}..."
    response=$(github_api_get "repos/${REPO_OWNER}/${REPO_NAME}/collaborators")
    if [[ -z "$response" ]]; then
        echo "No collaborators found or failed to fetch collaborators."
        return
    fi
    echo "$response" | jq -r '.[] | "\(.login) - Permissions: Pull(\(.permissions.pull)) Push(\(.permissions.push)) Admin(\(.permissions.admin))"'
}

# View pull requests of the repository
function view_pull_requests {
    echo -e "\nFetching pull requests for the repository ${REPO_OWNER}/${REPO_NAME}..."
    response=$(github_api_get "repos/${REPO_OWNER}/${REPO_NAME}/pulls")
    if [[ -z "$response" ]]; then
        echo "No pull requests found or failed to fetch pull requests."
        return
    fi
    echo "$response" | jq -r '.[] | "PR #\(.number): \(.title) by \(.user.login) - State: \(.state)"'
}

# Revoke access for a collaborator
function revoke_access {
    local collaborator
    read -p "Enter the collaborator username to revoke access: " collaborator

    if [[ -z "$collaborator" ]]; then
        echo "No collaborator specified. Aborting."
        return
    fi

    echo "Revoking access for collaborator: $collaborator..."
    response=$(github_api_delete "repos/${REPO_OWNER}/${REPO_NAME}/collaborators/${collaborator}")

    if [[ -z "$response" ]]; then
        echo "Access successfully revoked for collaborator: $collaborator."
    else
        echo "Failed to revoke access. Response: $response"
    fi
}

# Main menu
function main_menu {
    while true; do
        echo -e "\n========== GitHub Repository Manager =========="
        echo "1. List collaborators"
        echo "2. View pull requests"
        echo "3. Revoke access for a collaborator"
        echo "4. Exit"
        echo "==============================================="
        read -p "Enter your choice: " choice

        case $choice in
            1)
                list_collaborators
                ;;
            2)
                view_pull_requests
                ;;
            3)
                revoke_access
                ;;
            4)
                echo "Exiting... Goodbye!"
                break
                ;;
            *)
                echo "Invalid choice. Please try again."
                ;;
        esac
    done
}

# Run the script
load_credentials
load_repository_info
main_menu
