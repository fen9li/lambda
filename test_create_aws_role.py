import unittest
import manipulate_aws_role
import lambda_conf

class LambdaFunctionTest(unittest.TestCase):

  # Uli tests if an aws role exists
  # He configures 'role_name' & 'role_policy'
  # in '$HOME/lambda/lambda_conf.py'

  def test_create_aws_role(self):

      # He asserts the role exists 
      self.assertTrue(manipulate_aws_role.role_exists(lambda_conf.role_name))

      # He confirms the role policy has been attached
      self.assertTrue( manipulate_aws_role.test_role_policy(
          lambda_conf.role_name,
          lambda_conf.attach_role_policy_arn))

if __name__ == '__main__':
    unittest.main()
