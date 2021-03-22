# Twitter Stream AWS

A serverless application to stream tweets into Elasticsearch and Kibana through AWS Kinesis Firehose. This stream uses a custom lambda function as a preprocessor to get the sentiment associated with the tweet (`NEUTRAL`, `POSITIVE`, `NEGATIVE` or `MIXED`) with AWS Comprehend.
![Product ORG-3](https://user-images.githubusercontent.com/29681007/112006597-245b9f80-8b24-11eb-9952-e517e763ad59.png)


You have access to a Kibana domain through this URL: `${elasticsearch-domain-endpoint}/_plugin/kibana/`.
Here is an example with a Pie containing the proportion of each sentiment in the received tweets:
![Screen Shot 2021-03-22 at 15 33 27](https://user-images.githubusercontent.com/29681007/112006391-f5ddc480-8b23-11eb-9c83-8d840e419071.png)


## Setup

1. Create and setup an AWS account and a Twitter Developer account.

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
