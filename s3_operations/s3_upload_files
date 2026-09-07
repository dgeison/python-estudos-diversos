import boto3
import os
from constants import *

client = boto3.client('s3',
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,)

root_path = os.getcwd()
print(f"Root path: {root_path}")

folder_path = os.path.join(root_path, 'data')
print(f"Folder path: {folder_path}")


AWS_BUCKET_NAME = 'meubucketcielo'

for file_name in os.listdir(folder_path):
    file_name_path = os.path.join(folder_path, file_name)
    print(f"File name path: {file_name_path}")
    print(f"File name: {file_name}")
    if os.path.isfile(file_name_path):
        print(f"Uploading {file_name} to AWS S3 bucket {AWS_BUCKET_NAME}")
        client.upload_file(file_name_path, AWS_BUCKET_NAME, file_name)
