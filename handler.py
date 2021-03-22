import base64
import json
import boto3

client = boto3.client('comprehend')

def transformTweets(event, context):
    print(event)
    output = []

    for record in event['records']:
        print(record)
        text = base64.b64decode(record['data']).decode('utf-8').strip()
        print('Record text: %s' % text)
        sentiment = client.detect_sentiment(Text=text, LanguageCode='en')
        print('Record sentiment: %s' % sentiment)
        data_record = {
            'text': text,
            'sentiment': sentiment
        }

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(json.dumps(data_record).encode('utf-8')).decode('utf-8')
        }
        output.append(output_record)
        print(output)

    return {'records': output}
