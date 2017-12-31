import unittest
import manipulate_s3_bucket
import lambda_conf

class LambdaFunctionTest(unittest.TestCase):

  # Uli tries to create an aws s3 bucket in a region
  # He configured 's3_bucket' & 'region'
  # in '$HOME/lambda/lambda_conf.py'

  def test_creating_aws_s3_bucket(self):

      # get bucket_in name
      bucket_in=lambda_conf.s3_bucket
      # create bucket_out name
      bucket_out=bucket_in + 'out'

      # He confirms the bucket pair exist.
      self.assertTrue(manipulate_s3_bucket.bucket_exists(bucket_in))
      self.assertTrue(manipulate_s3_bucket.bucket_exists(bucket_out))

if __name__ == '__main__':
    unittest.main()
