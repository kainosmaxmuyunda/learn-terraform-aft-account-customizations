import boto3

def create_vpc():
    ec2_client = boto3.client('ec2', region_name='eu-west-2')

    # Create VPC
    response = ec2_client.create_vpc(
        CidrBlock='10.0.0.0/16',
        AmazonProvidedIpv6CidrBlock=False
    )
    
    vpc_id = response['Vpc']['VpcId']
    print(f"VPC created with ID: {vpc_id}")
    
    # Add a name tag to the VPC
    ec2_client.create_tags(
        Resources=[vpc_id],
        Tags=[
            {
                'Key': 'Name',
                'Value': 'APP VPC'
            }
        ]
    )
    
    # Enable DNS hostnames in the VPC
    ec2_client.modify_vpc_attribute(
        VpcId=vpc_id,
        EnableDnsHostnames={'Value': True}
    )
    
    print("VPC creation completed successfully!")

if __name__ == '__main__':
    create_vpc()
