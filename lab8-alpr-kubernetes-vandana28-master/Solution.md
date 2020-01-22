Created a Kubernetes cluster and set the zone using the commands :

```gcloud config set compute/zone us-west1-b```

```gcloud container clusters create lab8 --num-nodes=3```

**Redis and RabbitMQ:**

Used the images specified in docker hub and ran the commands specified in the commands.md file

**Rest:**

Created a dockerfile for rest that installs packages from Python 3.7. Provided the command to run rest-server.py file in the dockerfile. Created an image using the dockerfile and ran the commands specified in commands.md file to deploy the service.

**Worker:**

Similar to rest, I installed the openALPR using ubuntu 19.10 in the dockerfile and installed the relevant python commands as well. Provided the command to run worker-receiver.py in the dockerfile.Created an image using the dockerfile and ran the commands specified in commands.md file to deploy the service.

Tested the test-rest.sh script by providing the external IP of the rest service and got the required output.

Output image attached to the repository along with commands run during the execution of kubernetes services.
Docker files attached as well.
