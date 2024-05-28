The goal of this project is to stream dynamodb data into s3 using kinesis data stream and kinesis data firehose.
we will divide this project into 2 parts:

 1) storing device information data into dynamodb.
 2) streaming dynamodb data to kinesis data stream to kinesis fireshose and finally storing it into s3.

**THe architectural diagram is as follow:**

![sns-tos3](https://github.com/AmayKhatri/kinesis-mini-projects/assets/162054469/2e719a3c-1040-4a14-b281-c08ab46a2deb)

**Part 1. Storing device information data into dynamodb.**

1) Firstly create an sns topic.
2) Create an IAM role and give the lambda, access to sns, dynamodb, cloudwatch etx.
3) Create a lambda function by using the code provided in sns_triggered_lambda.py
4) attach the sns trigger to the lambda.
5) Create a dynamodb table. Add the partition key carefully looking at what the field used in the code is. YOu can modify it as per your use case.
6) Take the json provided in sample_event.json file and publish it.

Now the data should store in the dynamodb table.

**Part 2: Streaming dynamodb data to kinesis data stream to kinesis fireshose and finally storing it into s3.**

1) Create a Kinesis data stream.
2) Create a S3 bucket
3) Create a kinesis data firehose stream. Select sorce as kinesis data stream you just created and choose the destination as S3. You can use data transformation
such as buffering, batching, compression, or a lambda function to customize your transformation.
4) Go back to your dynamodb table, navigate to exports and streams, and turn on Amazon Kinesis data stream details by selecting your data stream.

And that's it !! You have created the architecture. Now ingest data from your sns topic that should store in your amazon S3 bucket !!
