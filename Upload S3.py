import boto3
s3_resource=boto3.client("s3")
s3_resource=upload_file(
    Filename="Huy Le Resume (8).pdf",
    #bucket name
    Bucket="bigstorageforme"),
    #filename in the bucket
    Key="Huy Le Resume (10).pdf")
