import unittest
import manipulate_aws_role
import lambda_conf

class LambdaFunctionTest(unittest.TestCase):

  # Uli tries to create an aws role
  # He configures 'role_name' & 'role_policy'
  # in '$HOME/lambda/lambda_conf.py'

  def test_create_aws_role(self):

      # He creates the role
      manipulate_aws_role.create_role(
          lambda_conf.role_name,
          lambda_conf.assume_role_policy_document)

      # He asserts the role exists 
      self.assertTrue(manipulate_aws_role.role_exists(lambda_conf.role_name))

      # He tries to attach a policy to the role

      # He confirms the role policy has been attached

if __name__ == '__main__':
    unittest.main()
