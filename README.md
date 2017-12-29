# Create AWS lambda Function in Agile Way

AWS Lambda is a serverless compute service that runs code in response to events and automatically manages the underlying compute resources. This project demos how to create a lambda function in an agile way. 

## AWS resources / services consumed / used in this project
* Lambda
* s3 buckets
* CloudWatch logs
* IAM role 

## Usage

### Prepare

Setup a linux host as management/dev host. The linux host can be an on-premise one or an aws ec2 instance; Can be a physical one or virtual.

* Install / configure AWS cli
* Install python 3.6, pip & boto3
* Install git

### Set up

* Clone repo 'https://github.com/fen9li/lambda.git' upon 'agile' branch.
* Change directory to 'lambda'.
* Expected files and directories structure showed below.

```sh
(dev36) [fli@python73 lambda]$ tree
.
├── function_tests.py
├── lambda_conf.py
├── manipulate_s3_bucket.py
├── README.md
├── test_create_s3_bucket.py
└── test_delete_s3_bucket.py

0 directory, 6 files
(dev36) [fli@python73 lambda]$
```

### Configure lambda.conf

1. region - unless you want to create in different region, dont change this. The current working region will be picked up automatically.
2. s3BucketName - define this bucket name as per your favour.
3. serviceRoleName - it is recommended that you keep it as is.
4. lambdaFunctionName - define your Lambda function name.
