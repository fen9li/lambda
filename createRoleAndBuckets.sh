#!/bin/bash

# Run this script to create s3 buckets & AWSLambdaExecutionRole

# Get configuration variables
source lambda.conf

# Get current region
# If you want to setup this project in different region,
# specify it here
# region='ap-southeast-2'
region=`aws configure get region`

# Create s3 buckets
echo "Creating s3 buckets ..."
aws s3api create-bucket --bucket $s3BucketName --region $region --create-bucket-configuration LocationConstraint=$region

s3BucketName=${s3BucketName}out
aws s3api create-bucket --bucket $s3BucketName --region $region --create-bucket-configuration LocationConstraint=$region

# Create AWSLambdaExecutionRole
echo "Creating AWSLambdaExecutionRole ..."
aws iam create-role --role-name $serviceRoleName --assume-role-policy-document file://AWSLambdaExecutionRole-Trust.json

aws iam attach-role-policy --role-name $serviceRoleName --policy-arn arn:aws:iam::aws:policy/AWSLambdaExecute

exit 0
