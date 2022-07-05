import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("very_first_boto3_s3")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint':'us-west-2'
    },
    
)

print(response)
