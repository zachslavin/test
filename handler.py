import json

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
    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
