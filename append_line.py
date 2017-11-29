from __future__ import print_function
import boto3
import os
import sys
import uuid
     
s3_client = boto3.client('s3')
     
def append_line(in_path, out_path):
    with open(in_path) as fin:
         with open(out_path, "a+") as fout:
              for line in fin:
                  fout.write(line)

              fout.write("This line is appended by Lambda function... \n")
         fout.close()
    fin.close()
     
def append_line_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key'] 
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        upload_path = '/tmp/out-{}'.format(key)
        
        s3_client.download_file(bucket, key, download_path)
        append_line(download_path, upload_path)
        s3_client.upload_file(upload_path, '{}out'.format(bucket), key)
