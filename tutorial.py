import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("bigstorageforme12")
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint':'us-west-2'
    },
    
)

print(response)
