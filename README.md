# Twitter Stream AWS

## Setup

1. Create and setup an AWS account.

2. Install the [serverless framework](https://www.serverless.com).

3. Add your twitter credentials in your environment:
```python
  # stream.py
  access_token = os.getenv('TWITTER_ACCESS_TOKEN')
  access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
  consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
  consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
```

4. deploy using `sls deploy` (you may need to deploy a first time commenting `ElasticSearch AccessPolicies`, since AWS may refuse it, then re-deploy with these lines).

5. Launch `stream.py` with tweet filter as params:
```sh
python3 stream.py "#HandsomeLucas" "#SmartLucas"
```
*This command will stream into Kinesis Firehose tweets containing `#HandsomeLucas` or `#SmartLucas`*

### Test

- To test the stream, enter the following command:
```sh
aws firehose put-record --delivery-stream-name=tweet-stream --record="{\"Data\":\"SGVsbG8sIHRoaXMgaXMgYSB0ZXN0IDEyMy4=\"}"
```
