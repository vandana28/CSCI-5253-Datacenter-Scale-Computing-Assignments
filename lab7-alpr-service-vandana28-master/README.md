# lab7-solution-alpr-service
Automatic license plate recognition service implemented using virtual machines.

## Overview
In this lab, you're going to create a set of virtual machines and/or images that provide a REST API for scanning images that contain geotagged license plates and records them in a database.

You will deploy virtual machines providing the following services.
+ rest - the REST frontend will accept images for analysis and handle queries concerning specific license plates and geo-coordinates. The REST worker will queue tasks to workers using rabbitmq messages. Full details are provided in rest/README-rest.md
+ worker - Worker nodes will receive work requests to analyze images. If those images contain both a geo-tagged image and a vehicle with a license plate that can be scanned, the information is entered into the REDIS database. Full details are provided in worker/README-worker.md
+ rabbitmq - One node, which should be named `rabbitmq` should act as the rabbit-mq broker. Full details are provided in rabbitmq/README-rabbitmq.md
+ redis - One node, which should be named 'redis' should provide the redis database server. Full details are provided in redis/README-redis.md

The worker will use the [open source automatic license plate reader](https://github.com/openalpr/openalpr) software. This is an open-source component of [a more comprehensive commercial offering](https://openalpr.com). One of the commercial components includes a web service similar to what we're building.

All of your services other than the REST frontend should not have an external IP address. When you create instances, you can use the `--network-interface=no-address` flag to suppress the external IP address. However, your instance will then not be able to access the external Internet, but that's something we can solve by setting up a NAT (network translation) in the router. This is done by issuing the following `gcloud` command:
```
gcloud compute routers create nat-router --network=default --region=us-west1
gcloud compute routers nats create nat-config \
    --router=nat-router \
    --auto-allocate-nat-external-ips \
    --nat-all-subnet-ip-ranges \
    --enable-logging
```

Also, when creating instances, you should specify
```
    --tags=default-allow-internal
```
to insure that internal nodes can access services for the redis and rabbitmq services.

## Suggested Steps

You should first construct the `rabbitmq` and `redis` servers because they're easy. Following that, you should construct the `rest` server because you can use that to test your `redis` database connection as well as connections to `rabbitmq` and your debugging interface. Lastly, start on the `worker`.

Although not explicitly required, you should create a simple python program that connects to the debugging topic exchange as described in `rabbitmq`. You can use that to subscribe to any informational or debug messages to understand what's going on.

Each subdirectory contains directions in the appropriate README file. The `images` directory contains test images.
+ beetle.jpg is not geotagged and has one visible license plate (309-OJN)
+ car.jpg is not geotagged but has one visible license (CZTHEDA)
+ geotagged.jpg is geotagged but has no cars
+ the-meat-car.jpg is geotagged and has one visible license (789-SJL)

The `plate1.png` image is a PNG image -- you can use this to test what happens when non-jpg files are submitted.