We will look at a small example of how step functions works with aws lambda functions.

State Diagram: 

![stepfunctions_graph](https://github.com/AmayKhatri/aws-projects/assets/162054469/a6fa0408-d5f4-48b3-85d9-a9e278faee79)

Here, we have created to lambda functions, transactionPurchase and transactionRefund. 

WHen the step function execution starts, it goes into a **choice state processTransaction**, then based on the input json provided, it checks the TransactionType. 

TransactionType has 2 values, PURCHASE and REFUND. 

1) If the transactionType is PURCHASE, it flow will be directed to the TransactionPurchase lambda.

   
2) If the transactionType is REFUND, it flow will be directed to the TransactionRefund lambda.
