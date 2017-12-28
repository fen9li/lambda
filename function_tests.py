import os
import unittest
import boto3

class LambdaFunctionTest(unittest.TestCase):

  # Uli wants to save all his aws lambda related configuration 
  # in one place.
  # '$HOME/lambda/lambda_conf.py'

  def test_lambda_configration_file_exists(self):
      HOME = os.getenv("HOME")
      FNAME = HOME + '/lambda/lambda_conf.py'
      self.assertTrue(os.path.exists(FNAME))

  # Uli wants to create aws s3 bucket in a region
  # He configured 's3_bucket' & 'region' 
  # in '$HOME/lambda/lambda_conf.py'
  def test_aws_s3_bucket_exists(self):
      import lambda_conf

      s3 = boto3.resource('s3')
      check = s3.Bucket(lambda_conf.s3_bucket) in s3.buckets.all()
      self.assertTrue(check)

      self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
