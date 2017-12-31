import manipulate_aws_role
import lambda_conf

# Uli configures 'role_name' & 'detach_role_policy_arn'
# in '$HOME/lambda/lambda_conf.py'
# He then delete the aws role

manipulate_aws_role.detach_role_policy(
    lambda_conf.role_name,
    lambda_conf.detach_role_policy_arn)

manipulate_aws_role.delete_role(
     lambda_conf.role_name)
