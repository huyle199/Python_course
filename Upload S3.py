import boto3
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="Huy Le Resume (8).pdf",
    #bucket name
    Bucket="bigstorageforme",
    #filename in the bucket
<<<<<<< HEAD:tutorial7.py
    Key="myimage.png")
=======
    Key="Huy Le Resume (10).pdf")
>>>>>>> a8d532f69046c816bd3822bd18b6b0844e807a2a:Upload S3.py
