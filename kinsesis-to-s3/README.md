# kinesis-mini-projects
This repository has various AWS Kinesis based architectures and its project code.

Project: Generate weather data using a producer lambda, write it to kinesis data stream. A lambda function will get record from the lambda and write it to s3.

Architectural diagram: 

![Untitled Diagram (1)](https://github.com/AmayKhatri/kinesis-mini-projects/assets/162054469/5d5bf383-d1ed-4622-9e49-497c6481cd1b)



In this project we will do a practical demonstration of writing data stream through an Amazon Kinesis data stream to an Amazon S3 bucket using an AWS Lambda trigger. We will create a python producer that generates simulated weather data and pushes it to an Amazon Kinesis data stream. Following that we'll develop a Lambda function using python which gets triggered as soon as the data is read into the stream, this Lambda function will then write the records to a file on Amazon S3.
