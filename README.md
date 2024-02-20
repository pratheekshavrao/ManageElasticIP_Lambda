# Automate the management of Elastic IPs using Lambda

The objective of this project is to streamline VPC operations through Lambda automation. Elastic IPs, serving as static public IPv4 addresses, can be seamlessly linked with EC2 instances. These Elastic IPs play a crucial role in masking instance failures by swiftly remapping to alternative instances. However, instances may occasionally have unassociated Elastic IPs, leading to unwarranted expenses. This project seeks to automate the identification of unassociated Elastic IPs and initiate their release, thus optimizing cost management.

## Steps to execute

1. First navigate to the EC2 dashboard in the AWS console and then launch a new EC2.

   ![alt text](https://github.com/pratheekshavrao/ManageElasticIP_Lambda/blob/master/images/Ec2_created.jpg)

3. Create a few Elastic IPs from the EC2 console. Associate any 1 EIP to the instance created.

   ![alt text](https://github.com/pratheekshavrao/ManageElasticIP_Lambda/blob/master/images/Associate_EIP.jpg)

5. Next to create a Lambda function,  navigate to Lambda console. Click on "Create function."Choose a meaningful name for your Lambda function, specify the runtime as Python 3.9, and create a new role.

   ![alt text](https://github.com/pratheekshavrao/ManageElasticIP_Lambda/blob/master/images/Lambda_created.jpg)

7. For local testing of Lambda functions, download the functions to Cloud9 environment, create event.json and template .yaml files. Use below code from terminal to test the functions.

   ![alt text](https://github.com/pratheekshavrao/ManageElasticIP_Lambda/blob/master/images/Local_invoke_command.jpeg)

9. Upon successful local testing, upload the Lambda function code from Cloud9 to AWS Lambda.

10. Grant Permissions to Lambda for EC2 Access. Attach an IAM policy to the Lambda Execution Role to permit access to EC2 resources.

    ![alt text](https://github.com/pratheekshavrao/ManageElasticIP_Lambda/blob/master/images/Lambda_permissions.jpg)

12. To configure Amazon EventBridge Scheduler navigate to the Amazon EventBridge console.  Create a new schedule with a schedule expression, specifying a recurrence pattern for daily execution at a designated time.Set the scheduler’s target to be your Lambda function.

    ![alt text](https://github.com/pratheekshavrao/ManageElasticIP_Lambda/blob/master/images/Event_bridge_rule.jpg)

## Result

The unassociated EIPs are released. Only 1 EIP which was associated with an EC2 instance remains.

![alt text](https://github.com/pratheekshavrao/ManageElasticIP_Lambda/blob/master/images/Released_EIPS.jpg)
