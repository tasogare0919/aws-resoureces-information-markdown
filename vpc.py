from dict_to_md import dict_to_markdown
import boto3

profile=""

session = boto3.session.Session(profile_name=profile)
ec2 = session.client("ec2",region_name="ap-northeast-1")
vpcs = ec2.describe_vpcs()['Vpcs']
for i in range(len(vpcs)):
    print(dict_to_markdown(vpcs[i], title="VPC", format="md"))

# for vpc in vpcs:
#     # tags_filter = [t.get('Value') for t in vpc['Tags'] if t.get('Key') == "Name"]
#     # name = tags_filter[0] if tags_filter else ''
#     # Cidr 取得と buffer 格納
#     for assoc in vpc['CidrBlockAssociationSet']:
#         data.append([
#             vpc['VpcId'],
#             assoc['CidrBlock'],
#             vpc['InstanceTenancy'],
#             vpc['IsDefault']
#         ])

# df_vpcs = pd.DataFrame(data,  columns=["VpcId", "Cidr", "Tenancy", "IsDefault"])
# print(df_vpcs)