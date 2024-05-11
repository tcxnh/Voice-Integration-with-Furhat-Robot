import boto3
import os
import uuid

def upload_audio(file_path):

    # Set AWS credentials as environment variables
    os.environ['AWS_ACCESS_KEY_ID'] = 'AKIA6ODUZKBYB2B436NA'
    os.environ['AWS_SECRET_ACCESS_KEY'] = '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'

    # Create an S3 client
    s3 = boto3.client('s3')

    # Specify the bucket name and file path
    bucket_name = 'furhataudios'

    # Generate a unique object key
    object_key = f"{uuid.uuid4().hex}_{os.path.basename(file_path)}"

    # Upload the file to S3
    s3.upload_file(file_path, bucket_name, object_key)

    # Generate the URL for the uploaded file
    url = f'https://{bucket_name}.s3.amazonaws.com/{object_key}'
    
    return url
