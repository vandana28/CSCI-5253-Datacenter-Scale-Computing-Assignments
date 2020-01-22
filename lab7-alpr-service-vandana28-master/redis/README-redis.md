# Redis database

You should create a server that provides a Redis database. The instance name should be `redis` so that worker nodes can use DNS names to locate the instance. You should provide a startup script that installs Redis and starts the server. There are [directions at the Redis website](https://redis.io/topics/quickstart) of how to do this.

You don't need to create any database tables in advance -- that happens automatically when you start using the database; see instructions in `worker/README-worker.md`.

You must create a script `redis-launch.sh` that creates the instance and uses the `redis-install.sh` script to install the redis database and start the service.

Make sure that your instance does not have an external IP address using the `--network-interface=no-address` flag if using the `gcloud` command interface or similar method if using Python.

After you've installed Redis, you'll need to change the configuration to allow connections from any network address. This is very insecure, but is suitable for this assignment. You can do this using:
```
sudo echo "bind 0.0.0.0 ::1" >> /etc/redis/redis.conf
sudo systemctl restart redis-server
```

# *N.B.*

If you delete your redis instance, the database will also be deleted. If you want avoid that problem, you can create a 2GB persistent disk and [use the `disk` property](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create#--disk) of the `gcloud` command interface to hold the database, following the [directions for persistent data in the Redis website](https://redis.io/topics/quickstart)

We're not using Redis because it's great, we're using it because it's easy.