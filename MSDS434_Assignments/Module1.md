# Module 1 Documentation
## For your first screencast video, create and share a brief demo showing the instantation of an instance on both the Google Cloud Platform as well as on Amazon AWS. In addition, describe one application of AI that you would be interested in pursuing in the context of the GCP leveraging the technologies identified in this course.

### Google Cloud Platform

1. Navigate to console.cloud.google.com
2. Create account & link up billing (or activate $300 credit)
3. Create a new project and select new project
4. Search "Compute Engine"
5. Click Create Instance
6. Type a name for the instance/service
7. Select E2-Mirco for the machine type. You can leave most of the stuff default 
8. Notice the billing/cost summary on the right
9. Click Create Instance
10. On Compute Engine Dashboard, you can click SSH to SSH into the machine
11. You've successfully created an instance in GCP with SSH

### AWS
1. Navigate to aws.amazon.com/console/
2. Create Account and activate free credits
3. Navigate to EC2 Instance
4. Click Launch EC2 Instance
5. Select a name for the service
6. Populate necessary fields (Ubuntu & E2 Machine)
7. Click Launch Instance
8. For SSH into the new EC2 instance, download the .pem file
9. In local terminal, use the following commands

chmod 400 Sept_23_2022.pem
ssh -i "Sept_23_2022.pem" ubuntu@ec2-54-84-23-217.compute-1.amazonaws.com

Note: The dates will be different

10. You've successfully created an instance in AWS with SSH
