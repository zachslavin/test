import json
import hmac
import base64
import hashlib

def _hmac_is_valid(body, secret, hmac_to_verify):
    hash = hmac.new(secret, body, hashlib.sha1)
    hmac_calculated = base64.b64encode(hash.digest())
    print(hmac_calculated)
    print(hmac_to_verify)
    return hmac_calculated == hmac_to_verify

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    print(event)
    print(json.dumps(event))
    payload = json.loads(event['body'])
    headers = json.dumps(event['headers'])
    print(payload)
    sig = json.loads(headers)
    print(sig['X-Hub-Signature'])

    if _hmac_is_valid(str(payload), 'supersecret', str(sig['X-Hub-Signature']).split('=')[1]):
        print("True")

    # Use this code if you don't use the http event with the LAMBDA-PROXY integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
