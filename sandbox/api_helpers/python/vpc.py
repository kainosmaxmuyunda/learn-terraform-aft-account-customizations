import logging
import boto3
from botocorgit e.exceptions import ClientError
import json
AWS_REGION = 'eu-west-2'
# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')
vpc_client = boto3.client("ec2", region_name=AWS_REGION)

def create_default_vpc():
    """
    Creates a default VPC in the configured availability zone.
    """
    try:
        response = vpc_client.create_default_vpc()
    except ClientError:
        logger.exception('Could not create default vpc.')
        raise
    else:
        return response

if __name__ == '__main__':
    logger.info(f'Creating default VPC...')
    default_vpc = create_default_vpc()
    default_vpc_id = default_vpc['Vpc']['VpcId']
    logger.info(f'Default VPC is created with VPC ID: {default_vpc_id}')