import boto3
import manipulate_s3_bucket
import lambda_conf

manipulate_s3_bucket.create_bucket(lambda_conf.s3_bucket,lambda_conf.region)
