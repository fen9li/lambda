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
