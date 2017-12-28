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
