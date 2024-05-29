We will look at a small example of how step functions works with aws lambda functions.

What is a step function ? 

AWS Step Functions is a serverless orchestration service that lets developers create and manage multi-step application workflows in the cloud. By using the service’s drag-and-drop visual editor, teams can easily assemble individual microservices into unified workflows. At each step of a given workflow, Step Functions manages input, output, error handling, and retries.

How AWS Step Functions Works
AWS Step Functions consists of the following main components:

State Machine
In computer science, a state machine is defined as a type of computational device that is able to store various status values and update them based on inputs. AWS Step Functions builds upon this very concept and uses the term state machine to refer to an application workflow. Developers can build a state machine in Step Functions with JSON files by using the Amazon States Language.

State
A state represents a step in your workflow. States can perform a variety of functions:

Perform work in the state machine (Task state—see more information below)

Choose between different paths in a workflow (Choice state)

Stop the workflow with failure or success (a Fail or Succeed state)

Pass output or some fixed data to another state (Pass state)

Pause the workflow for a specified amount of time (Wait state)

Begin parallel branches of execution (Parallel state)

Repeat execution for each item of input (Map state)

The states that you decide to include in your state machine and the relationships between your states form the core of your Step Functions workflow.

Task State
A task state (typically just referred to as a task) within your state machine is used to complete a single unit of work. Tasks can be used to call the API actions of over two hundred Amazon and AWS services. Two types of tasks can be included in your workflows:

Activity tasks
Activity tasks let you connect a step in your workflow to a batch of code that is running elsewhere. This external batch of code, called an activity worker, polls Step Functions for work, asynchronously completes the work using your code, and returns results. Activity tasks are common with asynchronous workflows in which some human intervention is required (to verify a user account, for example).

Service tasks
Service tasks let you connect steps in your workflow to specific AWS services. Step Functions sends requests to other services, waits for the task to complete, and then continues to the next step in the workflow. They can be used easily for automated steps, such as executing a Lambda function.

Within your AWS console, you’ll be able to visualize and validate your state machine as a series of steps. As each step is executed, Step Functions logs its execution time, any input and output, the number of retries, and any errors that occur. This information allows engineering teams to easily understand which step or steps may have caused a workflow to fail and which steps led up to that failure.

State Diagram: 

![stepfunctions_graph](https://github.com/AmayKhatri/aws-projects/assets/162054469/a6fa0408-d5f4-48b3-85d9-a9e278faee79)

Here, we have created to lambda functions, transactionPurchase and transactionRefund. 

WHen the step function execution starts, it goes into a **choice state processTransaction**, then based on the input json provided, it checks the TransactionType. 

TransactionType has 2 values, PURCHASE and REFUND. 

1) If the transactionType is PURCHASE, it flow will be directed to the TransactionPurchase lambda.

   
2) If the transactionType is REFUND, it flow will be directed to the TransactionRefund lambda.
