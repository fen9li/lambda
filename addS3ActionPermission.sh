#!/bin/bash

# Grant perform the lambda:InvokeFunction action permission to bucket $s3BucketName

# Get configuration variables
source lambda.conf

# Get account id
accountId=`aws sts get-caller-identity --query 'Account' --output text`

# Grant permission
aws lambda add-permission --function-name $lambdaFunctionName --region $region --statement-id ${s3BucketName}_${lambdaFunctionName} --action "lambda:InvokeFunction" --principal s3.amazonaws.com --source-arn arn:aws:s3:::${s3BucketName} --source-account $accountId

exit 0
