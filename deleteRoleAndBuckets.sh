#!/bin/bash

# Run this script to delete:
# s3 buckets
# AWSLambdaExecutionRole

# Get configuration variables
source lambda.conf

# Get current region
# If you want to delete this project in different region,
# specify it here
# region='ap-southeast-2'
region=`aws configure get region`

# Delete AWSLambdaExecutionRole
echo "Detaching AWSLambdaExecutionRole policy ..."
aws iam detach-role-policy --role-name $serviceRoleName --policy-arn arn:aws:iam::aws:policy/AWSLambdaExecute

echo "Deleting AWSLambdaExecutionRole ..."
aws iam delete-role --role-name $serviceRoleName

# Deleting s3 buckets
echo "Deleting s3 bucket ..."
aws s3 rm "s3://$s3BucketName" --recursive
aws s3api delete-bucket --bucket $s3BucketName --region $region

s3BucketName=${s3BucketName}out
aws s3 rm "s3://$s3BucketName" --recursive
aws s3api delete-bucket --bucket $s3BucketName --region $region

exit 0
