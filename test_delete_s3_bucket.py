import boto3
import unittest
import manipulate_s3_bucket
import lambda_conf

class LambdaFunctionTest(unittest.TestCase):

  def test_deleting_aws_s3_bucket(self):
      # Uli wants to delete his s3 bucket
      # No matter it is empty or not
      # His bucket name is defined as 's3_bucket' in 'lambda_conf.py'

      # get bucket_in name
      bucket_in=lambda_conf.s3_bucket
      # create bucket_out name
      bucket_out=bucket_in + 'out'

      s3 = boto3.resource('s3')

      # Uli checks if the bucket exists
      # He then saves something in the bucket
      if(manipulate_s3_bucket.bucket_exists(bucket_in)):
          s3.meta.client.upload_file('/home/fli/lambda/README.md',bucket_in,'README.md')
          s3.meta.client.upload_file('/home/fli/lambda/.gitignore',bucket_in,'.gitignore')

      if(manipulate_s3_bucket.bucket_exists(bucket_out)):
          s3.meta.client.upload_file('/home/fli/lambda/README.md',bucket_out,'README.md')
          s3.meta.client.upload_file('/home/fli/lambda/.gitignore',bucket_out,'.gitignore')

      # He tries to delete the bucket 
      manipulate_s3_bucket.delete_bucket(bucket_in)
      manipulate_s3_bucket.delete_bucket(bucket_out)

      # He wants to assert the bucket is gone.
      self.assertFalse(manipulate_s3_bucket.bucket_exists(bucket_in))
      self.assertFalse(manipulate_s3_bucket.bucket_exists(bucket_out))

if __name__ == '__main__':
    unittest.main()
