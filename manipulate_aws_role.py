import boto3
import botocore

# Uli wants to check if an IAM role exists or not
# He defines the 'role_name'
# in '$HOME/lambda/lambda_conf.py'
def role_exists(role_name):

    client = boto3.client('iam')
   
    # Try get the role
    try:
        role = client.get_role(RoleName=role_name)
        print('Role exists.')
        return True
    except Exception as error:
        print(error)
        return False

# to create new role
# Uli creates his AssumeRolePolicyDocument and save it to '$HOME/lambda/'
# He then defines the 'role_name' & 'assume_role_policy_document' 
# in '$HOME/lambda/lambda_conf.py'
def create_role(role_name,assume_role_policy_document):

    iam = boto3.resource('iam')

    # Check if the role exists
    if (role_exists(role_name)):
        return iam.Role(role_name)

    else: 
        with open(assume_role_policy_document, 'r') as jsonfile:
             policy=jsonfile.read()

        return iam.create_role(
                   RoleName=role_name,
                   AssumeRolePolicyDocument=policy
               )

# to delete a role
# Uli defines the 'role_name' & 'detach_role_policy_arn'
# in '$HOME/lambda/lambda_conf.py'
def delete_role(role_name):

    client = boto3.client('iam')

    # Check if the role exists
    if (role_exists(role_name)):
        response = client.delete_role(
            RoleName=role_name
        )
        print('Delete role successfully.')
        return True
    else:
        print('RoleNotExists') 
        return False

# to attach role policy to a role
# Uli defines the 'role_name' & 'attach_role_policy_arn'
# in '$HOME/lambda/lambda_conf.py'
def attach_role_policy(role_name,attach_role_policy_arn):

    client = boto3.client('iam')

    # Try attach  role policy
    try:
        client.attach_role_policy(
          PolicyArn=attach_role_policy_arn,
          RoleName=role_name
        )
        print('Attached role policy successfully.')
        return True
    except Exception as error:
        print(error)
        return False

# to detach role policy 
# Uli defines the 'role_name' & 'detach_role_policy_arn'
# in '$HOME/lambda/lambda_conf.py'
def detach_role_policy(role_name,detach_role_policy_arn):

    client = boto3.client('iam')

    # Try detach  role policy
    try:
        client.detach_role_policy(
          PolicyArn=detach_role_policy_arn,
          RoleName=role_name
        )
        print('Detached role policy successfully.')
        return True
    except Exception as error:
        print(error)
        return False

# to test if a policy has attached to a role
# Uli defines the 'role_name' & 'policy_arn'
# in '$HOME/lambda/lambda_conf.py'
def test_role_policy(role_name,policy_arn):

    client = boto3.client('iam')
    policies = client.list_attached_role_policies(RoleName=role_name)
    return(policies['AttachedPolicies'][0]['PolicyArn'] == policy_arn)
