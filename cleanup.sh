#!/bin/bash

# clean up everything
./removeS3Notification.sh
./deleteLambdaFunction.sh
./deleteRoleAndBuckets.sh

# Clean legacy s3Notification.json file if exists
[ -e 's3Notification.json' ] && rm 's3Notification.json'

exit 0
