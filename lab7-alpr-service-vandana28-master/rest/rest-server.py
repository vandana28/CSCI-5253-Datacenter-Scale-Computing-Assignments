from flask import Flask, request, Response
import jsonpickle
from PIL import Image
import io
import hashlib
import sys
import pika
import json
import pickle
import redis
import base64
import logging
# from python_logging_rabbitmq import RabbitMQHandler
# Initialize the Flask application
app = Flask(__name__)

# route http posts to this method
@app.route('/api/image/<X>', methods=['POST'])
def test(X):
    print(X)
    r = request
    # convert the data to a PIL image type so we can extract dimensions
    try:
        m = hashlib.md5()
        m.update(r.data)
        q = m.hexdigest()
        response = {
            "hash" : q
        }
        # encode response using jsonpickle
        response_pickled = jsonpickle.encode(response)
        message = pickle.dumps([X,q,r.data])
        credentials=pika.PlainCredentials('guest','guest')
        parameters = pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue='work')
        mess = X
        channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
        channel.basic_publish(exchange ='topic_logs' , routing_key = 'logs', body = mess)
        channel.basic_publish(exchange ='',routing_key='work', body = message)
        print(" [x] Sent Data ")
        connection.close()
    except:
        response = {
           "hash" : 0
        }

    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/api/hash/<X>', methods=['GET'])
def getvalue(X):
    r = redis.Redis(host = "redis",db=1)
    v = pickle.loads(r.get(X))
    response = {
        "value": v
    }
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/api/license/<X>', methods=['GET'])
def getChecksum(X):
    r = redis.Redis(host = "redis",db=3)
    v = base64.b64decode(r.get(X))
    response = {
        "value": v
    }
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")
app.run(host="0.0.0.0", port=5000)
app.debug = True


