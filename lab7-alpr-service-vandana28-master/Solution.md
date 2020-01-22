For this assignment I programmatically constructed all of my instances and installed the respective scripts in them.

**RabbitMQ and Redis:**

I wrote a create instance program for each of the instances that used the respective install scripts to launch the instances and install the dependencies. To mention just the internal IP address for these instances, I configured the network interfaces for these instances in my code and set the flag to 'no-address'. 

**Rest:**

I created this instance programatically as well. So the rest-client uses the host and image filename as the arguments and sends a POST request to the rest-server which takes in the image and computes the MD5 hash of the image through the hashlib library in python. Using the pickle library I bound the filename, its hash and the image contents in bytes and sent this as a message via RabbitMQ to the worker. I used a rabbitMQ queue as my main channel of communication and the request was placed on the queue.
The rest-server also contains two other API endpoints namely: hash and lincense. Here after the worker puts the image hash along with its attribute into Redis, these two apis queries the Redis database and obtains the results back. 

I tested these endpoints through curlI used : 

```curl -H "Accept:application/json -X GET http://localhost:5000/api/hash/<insert hash number>```

```curl -H "Accept:application/json -X GET http://localhost:5000/api/license/<insert license plate number>```

**Worker:**

To install ALPR on the worker node, I created the VM instance using the ubuntu-14.04 image and followed the steps in this link : https://github.com/openalpr/openalpr/wiki/Compilation-instructions-(Ubuntu-Linux)#a-readme-to-real-time-license-plate-detection-with-openalpr-opencv-and-python
The worker takes in the pickled data from the RabbitMQ queue via the internal IP of the RabbitMQ instance. It takes the image data and calculates the latitute-longitude position of the image and the license plate if its available for that image. I created a list that contains the LAT-LON position and the top three predicted plate numbers and their respective confidence levels. 
I stored the hashvalue and the list as a key-value pair in Redis. Similarly I created two other databases that used <imagename : hashvalue> and <license plate : hash value>

I tested the code by creating multiple workers through the snapshot of the initial worker and I found that as the client sent requests, each worker took up a different request from the queue and implemented the ALPR service.


