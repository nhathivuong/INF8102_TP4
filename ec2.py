import boto3

client = boto3.client('cloudformation')

response = client.create_stack(
    StackName='ec2-stack-pub-AZ1',
    TemplateURL='https://polystudents3-460783431840.s3.ca-central-1.amazonaws.com/ec2-pub-AZ1.json',
    Parameters=[
    ],
    DisableRollback=True,
    EnableTerminationProtection=False,
    RetainExceptOnCreate=True
)

response = client.create_stack(
    StackName='ec2-stack-pub-AZ2',
    TemplateURL='https://polystudents3-460783431840.s3.ca-central-1.amazonaws.com/ec2-pub-AZ2.json',
    Parameters=[
    ],
    DisableRollback=True,
    EnableTerminationProtection=False,
    RetainExceptOnCreate=True
)

response = client.create_stack(
    StackName='ec2-stack-priv-AZ1',
    TemplateURL='https://polystudents3-460783431840.s3.ca-central-1.amazonaws.com/ec2-priv-AZ1.json',
    Parameters=[
    ],
    DisableRollback=True,
    EnableTerminationProtection=False,
    RetainExceptOnCreate=True
)

response = client.create_stack(
    StackName='ec2-stack-priv-AZ2',
    TemplateURL='https://polystudents3-460783431840.s3.ca-central-1.amazonaws.com/ec2-priv-AZ2.json',
    Parameters=[
    ],
    DisableRollback=True,
    EnableTerminationProtection=False,
    RetainExceptOnCreate=True
)
