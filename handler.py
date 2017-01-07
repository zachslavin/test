import json
import hmac
import base64
import hashlib
import os

def _hmac_is_valid(body, secret, hmac_to_verify):
    digest = hmac.new(secret, msg=body, digestmod=hashlib.sha1).hexdigest()
    print(hmac_to_verify)
    print(digest)
    return digest == hmac_to_verify

def hello(event, context):
    print(os.environ['SECRET_KEY'])
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    print(json.dumps(event))
    headers = json.dumps(event['headers'])
    sig = json.loads(headers)
    print(sig['X-Hub-Signature'])

    if _hmac_is_valid(event['body'], 'supersecret', str(sig['X-Hub-Signature']).split('=')[1]):
        print("True")

    # Use this code if you don't use the http event with the LAMBDA-PROXY integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
