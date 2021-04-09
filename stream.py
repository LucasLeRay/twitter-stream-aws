import sys
import os
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from dotenv import load_dotenv, find_dotenv
import boto3

print(sys.argv[1:])
if len(sys.argv) < 2:
    raise Exception('No tweet filter provided')

load_dotenv(find_dotenv())
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')

DeliveryStreamName = 'tweet-stream'

client = boto3.client('firehose', region_name='us-east-1')

class ListenerOut(StreamListener):
    def on_data(self, data):
        print(data)
        client.put_record(
            DeliveryStreamName=DeliveryStreamName,
            Record={'Data': json.loads(data)["text"]},
        )
        return True

    def on_error(self, status):
        print(status)

l = ListenerOut()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=sys.argv[1:])
