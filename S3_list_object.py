import boto3
s3_resource=boto3.client("s3")
s3_resource.list_objects(Bucket="bigstorageforme") ["Contents"]
len(objects)

if len (objects)>0:
    print("objects exit")