import os
import unittest

class LambdaFunctionTest(unittest.TestCase):

  # Uli wants to save all aws lambda features related configuration in one file
  # '$HOME/lambda/lambda.conf'
  # 
  def test_lambda_configration_file_exists(self):
      HOME = os.getenv("HOME")
      FNAME = HOME + '/lambda/lambda.conf'
      self.assertTrue(os.path.exists(FNAME))
      self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
