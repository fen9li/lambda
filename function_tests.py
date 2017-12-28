import os
import unittest

class LambdaFunctionTest(unittest.TestCase):

  # Uli wants to save all his aws lambda features related configuration 
  # in one place.
  # '$HOME/lambda/lambda_conf.py'

  def test_lambda_configration_file_exists(self):
      HOME = os.getenv("HOME")
      FNAME = HOME + '/lambda/lambda_conf.py'
      self.assertTrue(os.path.exists(FNAME))
      self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
