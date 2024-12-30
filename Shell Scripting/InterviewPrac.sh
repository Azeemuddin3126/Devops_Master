#!/bin/bash

set -x

# Commonly used Cmds
ls,cp,mv,mkdir,vi,
nano,clear,grep,find,top,df -h

#Shell script to list all processes
#/bin/bash
ps -ef
ps -ef | awk -F" " '{print $2}'

# Print only errors from remote logs
curl dummy.log | grep -i 'error'

shell script print numbers by 2 &5 not 15

# Printing Number Prcatice Note
for i in {1..50}; do
if (( (i % 3 == 0 || i % 5 == 0) && i % 15 != 0 ));then
        echo $i
fi;
done

# Script to print of S in mississipi
echo "mississipi" | grep -o 's' | wc -l

#Script example cron job 
crontab -e 
 * * * * * /bin/bash /path/to/script.sh

# Open a ro file in vi
vi -R test.txt

# Find all files with a specific extension
find . -type f -name "*.txt"

# Find all files with a specific extension and delete them
find . -type f -name "*.txt" -exec rm -f {} \;

# Find all files with a specific extension and move them to a specific directory
find . -type f -name "*.txt" -exec mv {} /path/to/directory \;

# Find all files with a specific extension and copy them to a specific directory
find . -type f -name "*.txt" -exec cp {} /path/to/directory \;

# Find all files with a specific extension and change their permissions
find . -type f -name "*.txt" -exec chmod 644 {} \;

# Find all files with a specific extension and change their owner
find . -type f -name "*.txt" -exec chown user:group {} \;

# Find all files with a specific extension and change their group
find . -type f -name "*.txt" -exec chgrp group {} \;

# grep command to search for a specific string in a file
grep "string" file.txt

# grep command to search for a specific string in all files in a directory
grep -r "string" /path/to/directory

# grep command to search for a specific string in all files in a directory and subdirectories
grep -r "string" /path/to/directory/*

# grep command to search for a specific string in all files in a directory and subdirectories and display the line number
grep -rn "string" /path/to/directory/*

# grep command to search for a specific string in all files in a directory and subdirectories and display the line number and file name
grep -rnl "string" /path/to/directory/*

# sort command to sort lines in a file
sort file.txt

# manage logs of a system that generates huge logs files every day
# Use logrotate to manage log files

logrotate -d /etc/logrotate.conf

logrotate -f /etc/logrotate.conf

logrotate -v /etc/logrotate.conf

logrotate gzip /etc/logrotate.conf
















