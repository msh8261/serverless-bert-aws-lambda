try:
    import unzip_requirements
except ImportError:
    pass
from model.model import ServerlessModel
import json



model = ServerlessModel('./model', 'my-bert-models','qa/squad-distilbert.tar.gz')


def handler(event, context):
    print("------>>>>>here ")    
    body = json.loads(event['body'])
    print("--->>>body: ", body)
    answer = model.predict(body['question'], body['context'])

    return {
        "statusCode": 200,
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            "Access-Control-Allow-Credentials": True

        },
        "body": json.dumps({'answer': answer})
    }



