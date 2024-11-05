#!/bin/bash

# Function to fetch and display webpage content
fetch_content() {
    echo "Fetching content from $URL..."
    curl -s "$URL" > webpage.html
    echo "Webpage content saved to webpage.html"
}

# Function to parse data based on user-provided pattern
parse_data() {
    echo "Parsing data based on the pattern: $PATTERN"
    grep -oP "$PATTERN" webpage.html | sed -E 's/<[^>]+>//g' | awk '{$1=$1};1' > parsed_data.txt
    echo "Parsed data saved to parsed_data.txt"
}

# Get user input for the URL and the data pattern to extract
read -p "Enter the URL to scrape: " URL
read -p "Enter the regex pattern to extract (e.g., product price or weather forecast): " PATTERN

# Fetch webpage content
fetch_content

# Parse the data based on the user-defined pattern
parse_data

echo "Scraping and parsing completed!"
