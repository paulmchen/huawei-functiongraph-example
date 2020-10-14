# -*- coding:utf-8 -*-
import json
import base64


def handler(event, context):
    # a transaction id & callback URL received from the function flow
    input_header = event['headers']
    user_id = input_header['userid']

    # build a request body to be sent as a response
    res_body_json = {
        "userid": user_id,
        "lastname": "Smith",
        "firstname": "Bob",
        "sex": "m",
        "hobby": "basketball",
        "cell": "14169836187",
        "email": "abcde1@huawei.com",
        "location": "Singapore",
        "githubid": "abcde"
    }

    # Sync response to caller

    response = {
        'statusCode': 200,
        'isBase64Encoded': True,
        'headers': {
            "Content-type": "application/json"
        },
        'body': base64.b64encode(json.dumps(res_body_json))
    }
    return json.dumps(response)

