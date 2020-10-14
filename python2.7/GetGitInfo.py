# -*- coding:utf-8 -*-
import json
import base64
import urllib
import urllib2
import ssl


def handler(event, context):
    # Get function input
    input_header = event['headers']

    # should be really gettting it from the path params
    github_id = input_header['githubid']

    # Git github info for a given user
    url = get_github_info(github_id)
    git_req = urllib2.Request(url)
    git_req.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(git_req, context=ssl._create_unverified_context())
    git_info = response.read()

    # Async response to caller
    response_body = git_info

    response = {
        'statusCode': 200,
        'isBase64Encoded': True,
        'headers': {
            "Content-type": "application/json"
        },
        'body': base64.b64encode(json.dumps(response_body))
    }
    return json.dumps(response)


def get_github_info(github_id):
    return "https://api.github.com/users/" + github_id + "/events/public"
