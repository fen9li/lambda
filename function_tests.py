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

  def test_deleting_aws_s3_bucket(self):
      # Uli wants to delete his s3 bucket
      # No matter it is empty or not
      # His bucket name is defined as 's3_bucket' in 'lambda_conf.py'
      import lambda_conf
      import manipulate_s3_bucket

      # Save something in the bucket
      s3 = boto3.resource('s3')
      s3.meta.client.upload_file('/home/fli/lambda/README.md',lambda_conf.s3_bucket,'README.md')
      s3.meta.client.upload_file('/home/fli/lambda/.gitignore',lambda_conf.s3_bucket,'.gitignore')

      manipulate_s3_bucket.delete_bucket(lambda_conf.s3_bucket)

      # Test if the bucket exists.
      check = s3.Bucket(lambda_conf.s3_bucket) in s3.buckets.all()
      self.assertFalse(check)

      self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
