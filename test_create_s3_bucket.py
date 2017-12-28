import boto3
import unittest
import manipulate_s3_bucket
import lambda_conf

class LambdaFunctionTest(unittest.TestCase):

  # Uli tries to create an aws s3 bucket in a region
  # He configured 's3_bucket' & 'region'
  # in '$HOME/lambda/lambda_conf.py'

  def test_creating_aws_s3_bucket(self):
      # He tries to create the bucket
      manipulate_s3_bucket.create_bucket(lambda_conf.s3_bucket,lambda_conf.region)

      # Test if the bucket exists.
      # This test will print nothing but OK if the bucket is created successfully. 
      # This test will print 'BucketAlreadyOwnedByYou' if the bucket
      # already exists and is owned by you. 

      s3 = boto3.resource('s3')
      check = s3.Bucket(lambda_conf.s3_bucket) in s3.buckets.all()
      self.assertTrue(check)

if __name__ == '__main__':
    unittest.main()
