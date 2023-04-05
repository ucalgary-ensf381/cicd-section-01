import requests
import json

def handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({ "ip": get_public_ip(), "version": "10"})
    }

def get_public_ip():
    res = requests.get("https://checkip.amazonaws.com")
    return res.text