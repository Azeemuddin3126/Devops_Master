#!/bin/bash

# This script is used to track AWS resources and their changes over time

#######################################
#  Auther : Azeemuddin Shaik
#  Date : 10/10/2023
#  Version : 1.0
#  Aws S3, EC2, Lambda, IAM users.
########################################


# create a timestamp
timestamp=$(date '+%Y-%m-%d %H:%M:%S')

# list all S3 buckets
echo "Listing all S3 buckets..."
aws s3 ls > resources.txt
echo '-----------------------------------'


# list all EC2 instances with instance IDs only
echo "Listing all EC2 instances..."
aws ec2 describe-instances | jq '.Reservations[].Instances[].InstanceId' >>  resources.txt
echo '-----------------------------------'

# list all Lambda functions
echo "Listing all Lambda functions..."
aws lambda list-functions >> resources.txt
echo '-----------------------------------'

# list all IAM users
echo "Listing all IAM users..."
aws iam list-users >> resources.txt
echo '-----------------------------------'

# create a directory with the timestamp
mkdir $timestamp

# use contab to run this script every day at 6 pm
echo "0 18 * * * /bin/bash /path/to/script.sh" | crontab -

# 0 18 * * * /bin/bash /path/to/script.sh

# use logrotate to manage log files
# logrotate -d /etc/logrotate.conf

# End of script
echo "Script completed successfully."


