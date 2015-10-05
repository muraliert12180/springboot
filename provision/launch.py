import json
import os
import time

#grab ami id of last built image
images = os.popen("aws ec2 describe-images --filters Name=tag-key,Values=type Name=tag-value,Values=springapp --query 'Images[*].{ID:ImageId}'").read()
images = json.loads(images)
ami = images[0]['ID']


#launch instance
#instance = os.popen("aws ec2 run-instances --image-id " + ami + " --count 1 --instance-type t2.micro --key-name cmoon --security-groups 'wide open'").read()
#print instance

#instanceid = json.loads(instance)
#instanceid1 = instanceid['Instances'][0]['InstanceId']

#add tags
#print os.popen("aws ec2 create-tags --resources " + instanceid1 + " --tags Key=Name,Value=mavenapp").read()

#wait until instance has launched to create asg
#time.sleep(120)

#ec2-run-instances --key KEYPAIR --user-data-file install-lamp ami-bf5eb9d6

#create launch configuration
launchconfig = "launch" + ami
print os.popen("aws autoscaling create-launch-configuration --launch-configuration-name " + launchconfig + " --user-data file://user-data.sh --key-name cmoon --image-id " + ami + " --instance-type t2.micro --security-groups sg-1dbaff78").read()


#create asg
print os.popen("aws autoscaling create-auto-scaling-group --auto-scaling-group-name springapp-web-dev --launch-configuration-name " + launchconfig + " --min-size 2 --max-size 2 --desired-capacity 2 --vpc-zone-identifier subnet-88fb53ed  --load-balancer-names 'Tomcat' --health-check-type ELB --health-check-grace-period 30").read()

#terminate parent instance