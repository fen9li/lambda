import boto3

def create_bucket(bucket_name,region):

    # Create a bucket. 
    s3 = boto3.resource('s3')

    # Check if the bucket has been created 
    if(s3.Bucket(bucket_name) in s3.buckets.all()):
        print('BucketAlreadyOwnedByYou')
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
