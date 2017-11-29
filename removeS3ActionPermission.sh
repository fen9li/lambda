#!/bin/bash

# Remove permission to perform the lambda:InvokeFunction action from bucket $s3BucketName

# Get configuration variables
source lambda.conf

# Remove alias
aws lambda delete-alias --function-name $lambdaFunctionName --name ${s3BucketName}_${lambdaFunctionName}

exit 0
