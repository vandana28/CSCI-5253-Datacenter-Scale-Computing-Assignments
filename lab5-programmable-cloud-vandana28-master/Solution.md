
# LAB 5 - Vandana Sridhar

> **PART 1**

> Part1 requires me to create a VM instance on the google cloud platform and install the flask application in the IP address of the running VM instance.

> I have used the create_instance.py program from the python samples in my part1.py and I've included the startup_script that helps install the flask application

> I've specified the image family as Ubuntu for the instance  creation. The metadata and configuration details are additionally added as well
> I've added the firewall rule "allow 5000" to my instance through the firewall-body. To add this to the instance, i've created a list of firewall rules and the "allow 5000" rule is checked against the list to see its available. If its not available the the firewall rule is added to the instance after obtaining the project credentials.

> I additionally checked the VM instance through the API and the firewall rule appears to be 5000

> To set the tags, I've used the setTags method and I provided a fingerprint to the tag's body which was obtained from the get() request to the instance.

> Finally to obtain the public/external IP from the VM instance,I have obtained the natIP under the networkInterfaces key in the get() response from the VM instance. That provides the IP address to access the flask application

>I've formatted it to a url format for the user to click on the link.

> To run this part : 
>>```python part1.py "projectID" "bucketname"```



>**PART 2**

> Part 2 requires me to create a snapshot of the disk from the instance I created in the first part.

> To do this I used the createSnapshot() method and I provided the project ID, the zone, the disk and the body of the snapshot as the parameters. The snapshot body contains the name os the snapshot and the disk for the snapshot resides under the same name as the VM instance

> After the creating the snapshot I created three instances and while doing so, I provided the name of the parameter as an additional argument to the create_instance() method. The create instance method using the snapshot to create the instance after getting the project details and the snapshot name. The source snapshot is obtained from the response obtained from the get() request to the VM instance and this source snapshot is added to the configuration details.

> To calculate the time of creating the instance, I've started the time calculator before the instance creation and I've stopped the timer after the creation. Python facilitates this using the time package and I used the time() method to calculate time.

> I've calculated the difference between the times and I've appended it to a list and i've printed it out to a file.

>To run this part: 

>> ```python part2.py```

> **PART 3**

> In part 3, a VM needs to create another VM.

>To faciliate this, I have two python scripts and 2 startup scripts.

> In the first python script ie part3.py, I have created an instance similar to part1.py . I've added my project details  and created a VM instance. 

> In the first startup script, I've curled the metadata server to obtain the configuration details of the first VM instance. 

>I've created the service-credentials.json file and I've curled it into a environment variable called service_credentials which will help validate and create the second VM instance. The metadata in part3.py's config{} also contains the service-credentials key-value pair argument.

> Additionally, I've installed the python api client in the first startup script and I've committed the scripts for the second VM instance( part3a.py) along with its startup script into github. This code can be easily cloned and run through the second startup script.

>I've cloned my part3a repository and I've run my part3a by passing the project ID and the bucket name.

> **PART 3a**

> When the first VM instance runs, the first startup script invokes the second instance.

>Under the second instance's program ie part 3a, the VM instance is validated and made to run. I've mentioned the project details which is passed as the parameter to the create instance method

> The startup-script for this running instance contains the installation of flask and the IP address of this running instance opens up the flask startup page after flask is unpacked.

> Hence VM 1 invoked VM 2

> To run this part:

>> ```python part3.py "projectID" "bucketname"```


```python

```
