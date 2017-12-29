import boto3, botocore

def bucket_exists(bucket_name):

    s3 = boto3.resource('s3')

    try:
        s3.meta.client.head_bucket(Bucket=bucket_name)
        # print("BucketAlreadyExists")
        return True
    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = int(e.response['Error']['Code'])
        if error_code == 403:
            # print("PrivateBucketForbiddenAccess")
            return True
        elif error_code == 404:
            # print("BucketNotExist")
            return False

def create_bucket(bucket_name,region):

    # Create a bucket. 
    s3 = boto3.resource('s3')

    # Check if the bucket exists 
    if(bucket_exists(bucket_name)):
        print('BucketAlreadyExists')
    else:
        # Try to create new bucket
        try:
            bucket = s3.create_bucket(
                Bucket=bucket_name,
                ACL='private', 
                CreateBucketConfiguration={
                   'LocationConstraint': region}
               )
        except Exception as error:
            print(error)
        return bucket

def delete_bucket(bucket_name):

    # Delete the bucket.
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    # Check if the bucket exists 
    if(bucket in s3.buckets.all()):
        try:
            # Delete any contents in the bucket if any
            for key in bucket.objects.all():
                key.delete()
            # Delete the bucket
            bucket.delete()
        except Exception as error:
            print(error)
    else:
        # The bucket doesn't exist
        print('BucketNotExists')
    return True
