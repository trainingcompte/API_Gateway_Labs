import json

def lambda_handler(event, context):
    #GET method
    if event.get("httpMethod") == "GET":
        return {
            "statusCode" : 200,
            "body" : json.dumps(f'GET method invoked! QueryString: {event.get("queryStringParameters")}')
        }

    #POST method
    if event.get("httpMethod") == "POST":
        return {
            "statusCode" : 200,
            "body" : json.dumps(f'POST method invoked! PayLoad: {event.get("body")}')
        }

    #DELETE method
    if event.get("httpMethod") == "DELETE":
        return {
            "statusCode" : 200,
            "body" : json.dumps(f'DELETE method invoked!!')
        }
    #TO DO implement
    return {
        "statusCode": 200,
        "body": json.dumps("Hello from Lambda!")
    }