from dict_to_md import dict_to_markdown
import boto3

profile=""

session = boto3.session.Session(profile_name=profile)
route53_client = session.client("route53")

def listHostedZones():
    result = []
    response = route53_client.list_hosted_zones()
    for hostedZone in response["HostedZones"]:
        result.append(hostedZone)
    return result

def main():
    hostedZones = listHostedZones()
    if( not hostedZones ):
        print("Not found hostedzones.")
        exit()
    for hostedZone in hostedZones:
        response = route53_client.list_resource_record_sets(HostedZoneId=hostedZone['Id'])
        recordSets = response["ResourceRecordSets"]
        for i in range(len(recordSets)):
            print(dict_to_markdown(recordSets[i], title="Route53 Record Sets", format="md"))

if __name__ == '__main__':
    main()