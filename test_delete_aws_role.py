import unittest
import manipulate_aws_role
import lambda_conf

class LambdaFunctionTest(unittest.TestCase):

  # Uli configures 'role_name'
  # in '$HOME/lambda/lambda_conf.py'
  # He then confirms the role not exists

  def test_delete_aws_role(self):
      # He asserts the role doesn't exist
      self.assertFalse(
           manipulate_aws_role.role_exists(lambda_conf.role_name))

if __name__ == '__main__':
    unittest.main()
