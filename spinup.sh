#!/bin/bash

# create all
./createRoleAndBuckets.sh
./createLambdaFunction.sh
./addS3Notification.sh

exit 0
