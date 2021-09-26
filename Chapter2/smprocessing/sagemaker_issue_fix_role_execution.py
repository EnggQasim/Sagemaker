mport boto3
region = boto3.Session().region_name

def resolve_sm_role():
client = boto3.client('iam', region_name=region)
response_roles = client.list_roles(
PathPrefix='/',
# Marker='string',
MaxItems=999
)
for role in response_roles['Roles']:
if role['RoleName'].startswith('AmazonSageMaker-ExecutionRole-'):
#print('Resolved SageMaker IAM Role to: ' + str(role))
return role['Arn']
raise Exception('Could not resolve what should be the SageMaker role to be used')

#resolve_sm_role()
#role = get_execution_role()
role = resolve_sm_role()
role 
