# -*- coding:utf-8 -*-
import json
import base64
import urllib
import urllib2
from datetime import date


def handler(event, context):
    # Get function input
    input_data = base64.b64decode(event['body'])
    input_header = event['headers']

    # should be really gettting it from the path params
    org_id = 'o123'

    # a transaction id & callback URL received from the function flow
    txn_id = input_header['async-txn-id']
    call_back_url = input_header['call-back-url']

    # Find available external server and process the data
    url = find_available_processor()
    agg_req = urllib2.Request(url)
    agg_req.add_header('Content-Type', 'application/json')
    agg_req.add_header('async-txn-id', txn_id)

    # build a request body to be sent to the external task
    lrt_req_body_json = {
        "account_id": org_id,
        "date": date.today().strftime("%d/%m/%Y"),
        "callback": call_back_url
    }
    urllib2.urlopen(agg_req, json.dumps(lrt_req_body_json))

    # Async response to caller
    response_body = {
        'message': 'Financial account aggregation job submitted. ' +
                   'Transaction Id: ' + txn_id + '. '
                                                 'Processing the external task...'}

    response = {
        'statusCode': 200,
        'isBase64Encoded': True,
        'headers': {
            "Content-type": "application/json"
        },
        'body': base64.b64encode(json.dumps(response_body))
    }
    return json.dumps(response)


def find_available_processor():
    return 'http://129.0.0.229:3000/financialsummary'