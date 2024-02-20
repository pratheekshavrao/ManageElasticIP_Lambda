# Automate the management of Elastic IPs using Lambda

The objective of this project is to streamline VPC operations through Lambda automation. Elastic IPs, serving as static public IPv4 addresses, can be seamlessly linked with EC2 instances. These Elastic IPs play a crucial role in masking instance failures by swiftly remapping to alternative instances. However, instances may occasionally have unassociated Elastic IPs, leading to unwarranted expenses. This project seeks to automate the identification of unassociated Elastic IPs and initiate their release, thus optimizing cost management.
