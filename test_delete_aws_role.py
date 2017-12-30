import unittest
import manipulate_aws_role
import lambda_conf

class LambdaFunctionTest(unittest.TestCase):

  # Uli tries to delete an aws role
  # He configures 'role_name' & 'detach_role_policy_arn'
  # in '$HOME/lambda/lambda_conf.py'

  def test_delete_aws_role(self):
      # He detaches the role policy
      # He then deletes the role
      manipulate_aws_role.detach_role_policy(
          lambda_conf.role_name,
          lambda_conf.detach_role_policy_arn)

      manipulate_aws_role.delete_role(
          lambda_conf.role_name)

      # He asserts the role doesn't exist
      self.assertFalse(
           manipulate_aws_role.role_exists(lambda_conf.role_name))

if __name__ == '__main__':
    unittest.main()
