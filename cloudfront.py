from dict_to_md import dict_to_markdown
import boto3

profile=""

session = boto3.session.Session(profile_name=profile)
cf = session.client("cloudfront",region_name="ap-northeast-1")
cfs = cf.list_distributions()['DistributionList']['Items']
for i in range(len(cfs)):
    print(dict_to_markdown(cfs[i], title="CloudFront distributions", format="md"))