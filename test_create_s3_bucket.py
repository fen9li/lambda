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

      # He confirms the bucket exists.
      self.assertTrue(manipulate_s3_bucket.bucket_exists(lambda_conf.s3_bucket))

if __name__ == '__main__':
    unittest.main()
