from dict_to_markdown import dict_to_markdown
import boto3

ec2 = boto3.client("ec2")
vpcs = ec2.describe_vpcs()['Vpcs']
dict_to_markdown(vpcs[0], title="VPC", format="md")