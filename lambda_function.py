import boto3

def lambda_handler(event, context):
    ec2_resource = boto3.resource('ec2')

    for elastic_ip in ec2_resource.vpc_addresses.all():
        if elastic_ip.instance_id is None:
            elastic_ip.release()
            print(f"{elastic_ip} not associated with any instance.Hence releasing.")
    
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
