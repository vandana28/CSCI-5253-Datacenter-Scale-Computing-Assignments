Commands I used to create my dockers images and deploy my services into Kubernetes

**RabbitMQ:**

```
export PROJECT_ID=vasr6141-254820
docker run -d --hostname rabbitmq --name rabbitmq rabbitmq:3
docker build -t gcr.io/${PROJECT_ID}/rabbitmq:3 .
docker tag 0a13855dcf8f gcr.io/${PROJECT_ID}/rabbitmq:3
docker push gcr.io/${PROJECT_ID}/rabbitmq:3
kubectl create deployment rabbitmq --image=gcr.io/${PROJECT_ID}/rabbitmq:3
kubectl expose deployment rabbitmq --port 5672 --target-port 5672 
```

**Redis:**

```
docker run --name some-redis -d redis
docker tag de25a81a5a0b  gcr.io/${PROJECT_ID}/redis:1
docker push gcr.io/${PROJECT_ID}/redis:1
kubectl create deployment redis --image=gcr.io/${PROJECT_ID}/redis:1
kubectl expose deployment redis --port 6379 --target-port 6379
```

**Rest:**

```
docker build -t rest:v1 .
docker build -t gcr.io/${PROJECT_ID}/rest:v1 .
docker push gcr.io/${PROJECT_ID}/rest:v1
kubectl create deployment rest --image=gcr.io/${PROJECT_ID}/rest:v1
kubectl expose deployment rest --type=LoadBalancer --port 5000 --target-port 5000
```

**Worker:**

```
docker build -t worker:v1 .
docker build -t gcr.io/${PROJECT_ID}/worker:v1 .
docker push gcr.io/${PROJECT_ID}/worker:v1 
kubectl create deployment worker --image=gcr.io/${PROJECT_ID}/worker:v1
```
```
kubectl get pods
kubectl get service
sh test-rest.sh 35.227.166.22
```

