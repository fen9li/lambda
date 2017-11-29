#!/bin/bash

# Create Lambda function append_line

# Get configuration variables
source lambda.conf

# Get current region
# If you want to setup this project in different region,
# specify it here
# region='ap-southeast-2'
region=`aws configure get region`

# Clean legacy lambda function zip file if exists
zipFile=${lambdaFunctionName}.zip
[ -e "$zipFile" ] && rm "$zipFile"

# Create lambda function zip file
zip -r9 ${lambdaFunctionName}.zip ${lambdaFunctionName}.py

# Create lambda function 

roleArn=`aws iam get-role --role-name $serviceRoleName --query 'Role.Arn' --output text`
#echo $roleArn

echo "Sleeping 10 seconds ..."
sleep 10

aws lambda create-function --function-name $lambdaFunctionName --runtime python2.7 --role $roleArn --handler ${lambdaFunctionName}.${lambdaFunctionName}_handler --zip-file fileb://${lambdaFunctionName}.zip --timeout 10 --memory-size 128 --region $region

exit 0
