from dict_to_markdown import dict_to_markdown
import pandas as pd
import boto3

data = []
profile=""

session = boto3.session.Session(profile_name=profile)
ec2 = session.client("ec2",region_name="ap-northeast-1")
vpcs = ec2.describe_vpcs()['Vpcs']
for i in range(len(vpcs)):
    dict_to_markdown(vpcs[i], title="VPC", format="md")