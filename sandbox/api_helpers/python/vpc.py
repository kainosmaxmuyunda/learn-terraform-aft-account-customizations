import boto3

# create VPC

def client_init():
    client = boto3.client('ec2', region_name='eu-west-2')
    return client

def vpc_creation(client):
    client.create_vpc(CidrBlock='172.16.0.0/24')

if __name__ == "__main__":
    client = client_init()
    vpc_creation(client)


