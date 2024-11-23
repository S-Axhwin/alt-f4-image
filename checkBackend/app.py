import os
from dotenv import load_dotenv, dotenv_values

from flask import Flask
import boto3

load_dotenv()


app = Flask(__name__)


@app.route('/')
def check():
    client = boto3.client("rekognition")

    res = client.detect_moderation_labels(Image={
        'S3Object': {
            'Bucket': 'basiccurdopps',
            'Name': 'adult.jpeg'
        }
    }, MinConfidence=40)

    return res

@app.route("/generate")
def gen():
    s3_client = boto3.client(
    's3',
    region_name='ap-southeast-2',
    aws_access_key_id=os.getenv("ACC"),
    aws_secret_access_key=os.getenv("KEY")
    )

    response = s3_client.generate_presigned_post(
        Bucket = 'image-motize',
        Key = "image.jpg",
        ExpiresIn = 1000
    )
    fields = response["fields"]
    base_url = response['url']
    query_params = '&'.join([f"{key}={value}" for key, value in response['fields'].items()])
    full_url = f"{base_url}?{query_params}"
    
    return full_url
