import boto3

# ❗ Replace these after creating AWS S3 bucket
AWS_ACCESS_KEY = "YOUR_ACCESS_KEY"
AWS_SECRET_KEY = "YOUR_SECRET_KEY"
AWS_BUCKET_NAME = "YOUR_BUCKET_NAME"
AWS_REGION = "ap-south-1"

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)
