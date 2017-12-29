import boto3
import unittest
import manipulate_s3_bucket
import lambda_conf

class LambdaFunctionTest(unittest.TestCase):

  def test_deleting_aws_s3_bucket(self):
      # Uli wants to delete his s3 bucket
      # No matter it is empty or not
      # His bucket name is defined as 's3_bucket' in 'lambda_conf.py'

      # Uli checks if the bucket exists
      # He then saves something in the bucket
      if(manipulate_s3_bucket.bucket_exists(lambda_conf.s3_bucket)):
          s3 = boto3.resource('s3')
          s3.meta.client.upload_file('/home/fli/lambda/README.md',lambda_conf.s3_bucket,'README.md')
          s3.meta.client.upload_file('/home/fli/lambda/.gitignore',lambda_conf.s3_bucket,'.gitignore')

      # He tries to delete the bucket 
      manipulate_s3_bucket.delete_bucket(lambda_conf.s3_bucket)

      # He wants to assert the bucket is gone.
      self.assertFalse(manipulate_s3_bucket.bucket_exists(lambda_conf.s3_bucket))

if __name__ == '__main__':
    unittest.main()
