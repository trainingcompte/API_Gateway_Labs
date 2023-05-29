import json
import base64
import boto3


def lambda_handler(event, context):
    # TODO implement
    print(event)
    s3 = boto3.client("s3")
    bucket_name = event["params"]["path"]["bucket"]
    file_name = event["params"]["querystring"]["file"]
    
    fileObj = s3.get_object(Bucket=bucket_name, Key = file_name)
    file_content = fileObj["Body"].read()
    #file_content = b"hello"
    #print(type(file_content))
    print(bucket_name, file_name)
    #for proxy: 
    #bucket_name = event["pathParameters"]["bucket"]
    #file_name = event["queryStringParameters"]["file"]
    return base64.b64encode(file_content)