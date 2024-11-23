import os
from dotenv import load_dotenv
load_dotenv()
import boto3
import requests

OBJECT_NAME_TO_UPLOAD = 'file_to_upload.jpg'

print(os.getenv("ACC"),os.getenv("KEY") )
s3_client = boto3.client(
    's3',
    region_name='ap-southeast-2',
    aws_access_key_id=os.getenv("ACC"),
    aws_secret_access_key=os.getenv("KEY")
)

#Generate the presigned URL
response = s3_client.generate_presigned_post(
    Bucket = 'image-motize',
    Key = OBJECT_NAME_TO_UPLOAD,
    ExpiresIn = 1000
)



#Upload file to S3 using presigned URL
files = { 'file': open("blur.jpg", 'rb')}
r = requests.post(response['url'], data=response['fields'], files=files)
print(r.status_code)
