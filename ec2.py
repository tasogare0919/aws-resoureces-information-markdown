from dict_to_md import dict_to_markdown
import boto3

profile="default"

session = boto3.session.Session(profile_name=profile)
ec2_client = session.client("ec2",region_name="ap-northeast-1")
instance = sum([group['Instances'] for group in ec2_client.describe_instances()['Reservations']], [])
for i in range(len(instance)):
    print(dict_to_markdown(instance[i], title="EC2 Instance", format="md"))