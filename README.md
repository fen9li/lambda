# AWS Lambda Use Case Study 01 - with S3

A text file uploaded to S3 bucket, which triggers Lambda function to process this file and save the result text file to another bucket.

## AWS resources / services consumed / used in this project
* Lambda
* 2 s3 buckets
* CloudWatch logs
* IAM role

## Usage

### Prepare

> Setup a linux host as management host, which is both aws cli and Github ready. The linux host can be an on-premise one or an aws ec2 instance; Can be a physical one or virtual.

### Set up
* Clone repo 'https://github.com/fen9li/lambda.git' upon 'usecase01' branch.
* Change directory to 'lambda'.
* Expected files and directories structure showed below.

```sh
]$ git clone -b usecase01 https://github.com/fen9li/lambda.git    Cloning into 'lambda'...
remote: Counting objects: 28, done.
remote: Compressing objects: 100% (20/20), done.
remote: Total 28 (delta 9), reused 22 (delta 7), pack-reused 0
Unpacking objects: 100% (28/28), done.
]$

]$ cd lambda/
lambda]$ tree
.
├── addS3Notification.sh
├── append_line.py
├── AWSLambdaExecutionRole-Trust.json
├── cleanup.sh
├── createLambdaFunction.sh
├── createRoleAndBuckets.sh
├── deleteLambdaFunction.sh
├── deleteRoleAndBuckets.sh
├── lambda.conf
├── LICENSE
├── README.md
├── removeS3Notification.sh
├── s3Notification.json.base
├── spinup.sh
└── test.txt

0 directories, 15 files
lambda]$

```

* Configure lambda.conf

1. region - unless you want to create in different region, dont change this. The current working region will be picked up automatically.
2. s3BucketName - define this bucket name as per your favour.
3. serviceRoleName - it is recommended that you keep it as is.
4. lambdaFunctionName - define your Lambda function name.

An example:

```sh
lambda]$ egrep -v '^#|^$' lambda.conf
region=`aws configure get region`
s3BucketName='fen9li'
serviceRoleName='AWSLambdaExecutionRole'
lambdaFunctionName='append_line'
lambda]$
``` 

### Run ./spinup.sh script

```sh
lambda]$ ./spinup.sh
Creating s3 buckets ...
{
    "Location": "http://fen9li.s3.amazonaws.com/"
}
{
    "Location": "http://fen9liout.s3.amazonaws.com/"
}
Creating AWSLambdaExecutionRole ...
{
    "Role": {
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Principal": {
                        "Service": "lambda.amazonaws.com"
                    },
                    "Effect": "Allow",
                    "Sid": ""
                }
            ]
        },
        "RoleId": "AROAI3J4M6X7B477CYGSS",
        "CreateDate": "2017-11-29T03:37:27.862Z",
        "RoleName": "AWSLambdaExecutionRole",
        "Path": "/",
        "Arn": "arn:aws:iam::nnnnnnnnnnnn:role/AWSLambdaExecutionRole"
    }
}
  adding: append_line.py (deflated 57%)
Sleeping 10 seconds ...
{
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "CodeSha256": "cgdymEK2Rwk96AEDeUcJgWbcur/gbnN/kCIDs9PHvGs=",
    "FunctionName": "append_line",
    "CodeSize": 559,
    "MemorySize": 128,
    "FunctionArn": "arn:aws:lambda:ap-southeast-2:nnnnnnnnnnnn:function:append_line",
    "Version": "$LATEST",
    "Role": "arn:aws:iam::nnnnnnnnnnnn:role/AWSLambdaExecutionRole",
    "Timeout": 10,
    "LastModified": "2017-11-29T03:37:43.428+0000",
    "Handler": "append_line.append_line_handler",
    "Runtime": "python2.7",
    "Description": ""
}
{
    "Statement": "{\"Sid\":\"fen9li_append_line\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"s3.amazonaws.com\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:ap-southeast-2:nnnnnnnnnnnn:function:append_line\",\"Condition\":{\"StringEquals\":{\"AWS:SourceAccount\":\"nnnnnnnnnnnn\"},\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:s3:::fen9li\"}}}"
}
[fli@python72 lambda]$

```

### Test
* Upload a text file to s3 bucket s3://fen9li
* Check s3 bucket s3://fen9liout
* Download the file in s3 bucket s3://fen9liout to local
* Check the last line of this file

```sh
lambda]$ cat test.txt
This is a test text.

Once this file is uploaded to s3 bucket 'fen9li'...

aws s3 cp test.txt s3://fen9li

The s3 bucket 'fen9li' would then trigger lambda function 'append_line', which would append a line to this test text file and save the result file to bucket 'fen9liout.
lambda]$ aws s3 cp test.txt s3://fen9li
upload: ./test.txt to s3://fen9li/test.txt
lambda]$ aws s3 ls s3://fen9liout
2017-11-29 14:44:30        322 test.txt
lambda]$ aws s3 cp s3://fen9liout/test.txt processed.txt
download: s3://fen9liout/test.txt to ./processed.txt
lambda]$ cat processed.txt
This is a test text.

Once this file is uploaded to s3 bucket 'fen9li'...

aws s3 cp test.txt s3://fen9li

The s3 bucket 'fen9li' would then trigger lambda function 'append_line', which would append a line to this test text file and save the result file to bucket 'fen9liout.
This line is appended by Lambda function...
[fli@python72 lambda]$

``` 

### Clean up everything
Run ./cleanup.sh script to clean up everything.

Where to go next
* Add other Lambda feature in.
