from dict_to_md import dict_to_markdown
import boto3

profile=""

session = boto3.session.Session(profile_name=profile)
s3 = session.client("s3",region_name="ap-northeast-1")
s3bucket = s3.list_buckets()['Buckets']
for i in range(len(s3bucket)):
    print(dict_to_markdown(s3bucket[i], title="S3 Bucket", format="md"))