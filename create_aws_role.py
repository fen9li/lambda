import manipulate_aws_role
import lambda_conf

# Uli configures 'role_name' & 'role_policy'
# in '$HOME/lambda/lambda_conf.py'
# He then creates AWSLambdaExecutionRole-Trust.json,
manipulate_aws_role.create_role(
      lambda_conf.role_name,
      lambda_conf.assume_role_policy_document)
 
# He attaches a role policy
manipulate_aws_role.attach_role_policy(
      lambda_conf.role_name,
      lambda_conf.attach_role_policy_arn)
