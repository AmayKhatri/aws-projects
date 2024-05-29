We will look at a small example of how step functions works with aws lambda functions.

First we create a step function. Step functions are written in a language called as Amazon State Language (ASL). The state diagram is the visal representation
of the code we write in ASL for our step function: 

You can refer the code provided in the gist

State Diagram: 

![stepfunctions_graph](https://github.com/AmayKhatri/aws-projects/assets/162054469/a6fa0408-d5f4-48b3-85d9-a9e278faee79)

Here, we have created to lambda functions, transactionPurchase and transactionRefund. 

The code is provided inside the gist 

WHen the step function execution starts, it goes into a **choice state processTransaction**, then based on the input json provided, it checks the TransactionType. 

TransactionType has 2 values, PURCHASE and REFUND. 

1) If the transactionType is PURCHASE, it flow will be directed to the TransactionPurchase lambda.

2) If the transactionType is REFUND, it flow will be directed to the TransactionRefund lambda.
