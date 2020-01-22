#!/usr/bin/env python
import pika
import sys
import json
import pickle
import GetLatLon
from openalpr import Alpr
from PIL import Image
import redis

#credentials = pika.PlainCredentials('guest','guest')
#parameters = pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)
#connection = pika.BlockingConnection(parameters)
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='work')
list1 = []
licensename =''
obj2 = ''
def callback(ch, method, properties, body):
    obj1,obj2,obj3 = pickle.loads(body)
    f = open(obj1,"wb")
    f.write(obj3)
    f.close()
    image = Image.open(obj1)
    exif_data = GetLatLon.get_exif_data(image)
    print (GetLatLon.get_lat_lon(exif_data))
    latlon = GetLatLon.get_lat_lon(exif_data)
    list1.append(latlon)
    alpr = Alpr('us', '/etc/openalpr/openalpr.conf', '/usr/share/openalpr/runtime_data')
    results = alpr.recognize_file(obj1)

    if len(results['results']) == 0:
        print("Can't find a plate")
    else:
        count = 0
#        print(results['results'][0]['candidates'][0])
        licensename = results['results'][0]['candidates'][0]['plate']
        for key in results['results'][0]['candidates']:
            if(count <= 3):
                list1.append((key['plate'], key['confidence']))
                print("Most likely plate is", key['confidence'])
                print("Most likely confidence is", key['plate'])
                count = count+1
 
    redisHash = redis.Redis(host= "redis",db=1)
    redisHash.set(obj2, pickle.dumps(list1))
    list1.clear()
    print("Redis get by Hash Value")
    print(obj2)
    val1 = pickle.loads(redisHash.get(obj2))
    print(val1)

    redisName = redis.Redis(host = "redis",db=2)
    redisName.set(obj1, obj2)
    print("Redis get by Name")
    print(obj1)
    val2 = redisName.get(obj1)
    print(val2)

    if(len(results['results']) != 0):
        redisLicense = redis.Redis(host = "redis",db=3)
        redisLicense.set(licensename, obj2)
        print("Redis get by License")
        print(licensename)
        val3 = redisLicense.get(licensename)
        print(val3)

channel.basic_consume(
    queue='work', on_message_callback=callback, auto_ack=True)
#  print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

