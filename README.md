# Twitter Stream AWS

A serverless application to stream tweets into Elasticsearch and Kibana through AWS Kinesis Firehose. This stream uses a custom lambda function as a preprocessor to get the sentiment associated with the tweet (`NEUTRAL`, `POSITIVE`, `NEGATIVE` or `MIXED`) with AWS Comprehend.
![Architecture](https://user-images.githubusercontent.com/29681007/112118616-d646aa80-8bbc-11eb-8961-5dc5559f16dd.png)

You have access to a Kibana domain through this URL: `${elasticsearch-domain-endpoint}/_plugin/kibana/`.
Here is an example with a Pie containing the proportion of each sentiment in the received tweets:
![Kibana visualization](https://user-images.githubusercontent.com/29681007/112006391-f5ddc480-8b23-11eb-9c83-8d840e419071.png)


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

4. deploy using `sls deploy`.  
You may need to deploy a first time without these lines in `serverless.yml`, since AWS refuses public access to ES domains for security reasons:
```yaml
# in serverless.yml
73|  AccessPolicies:
74|    Version: "2012-10-17"
75|    Statement:
76|      - Effect: "Allow"
77|        Principal:
78|          AWS: "*"
79|        Action: "es:*"
80|        Resource:
81|          - arn:aws:es:us-east-1:*:domain/tweet-search/*
```

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
