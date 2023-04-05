import requests

def handler(event, context):
    return {
        "statusCode": 200,
        "body": get_public_ip()
    }

def get_public_ip():
    res = requests.get("https://checkip.amazonaws.com")
    return res.text