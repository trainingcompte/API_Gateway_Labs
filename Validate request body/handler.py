import json


def lambda_handler(event, context):
    print(event)
    response = {
        "contractors" : [
            {
                "On site": 70,
                "Total Contractors": 200
            }
        ],
        "permanent": [
            {
                "On site": 350,
                "Total Employees": 1000
            }
        ]
    }
    # TODO implement
    return {
        'statusCode': 200,
        'body': response[event["status"]]
    }
