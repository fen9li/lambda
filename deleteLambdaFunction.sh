#!/bin/bash

# Create Lambda function append_line

# Get configuration variables
source lambda.conf

# Delete lambda function 
aws lambda delete-function --function-name $lambdaFunctionName 

exit 0
