import json


def lambda_handler(event, context):
    # TODO implement
    print(event)
    bucket_name = event["params"]["path"]["bucket"]
    file_name = event["params"]["querystring"]["file"]
    print(bucket_name, file_name)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

##################################################################### (proxy)
import json


def lambda_handler(event, context):
    # TODO implement
    print(event)
    #bucket_name = event["params"]["path"]["bucket"]
    #file_name = event["params"]["querystring"]["file"]
    bucket_name = event["pathParameters"]["bucket"]
    file_name = event["queryStringParameters"]["file"]
    
    print(bucket_name, file_name)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
