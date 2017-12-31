import manipulate_s3_bucket
import lambda_conf

# Uli needs to delete aws s3 bucket pair in a region
# So that he can clean up
# He configured 's3_bucket' & 'region'
# in '$HOME/lambda/lambda_conf.py'

# get bucket_in name
bucket_in=lambda_conf.s3_bucket
# create bucket_out name
bucket_out=bucket_in + 'out'

manipulate_s3_bucket.delete_bucket(bucket_in)
manipulate_s3_bucket.delete_bucket(bucket_out)
