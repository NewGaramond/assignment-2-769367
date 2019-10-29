#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import sys
import inspect
import json, pika

import sys, os, inspect

import pika, time
import sys, os, inspect
from pymongo import MongoClient
from bson import ObjectId
import sys, os, inspect
key_queue_send = 'Queue.for.send.data'
key_queue_action = 'Queue.for.action.data'
# reload(sys)

# Config Rabbitmq
RABBIT_HOST = '	dove.rmq.cloudamqp.com'
RABBIT_PORT = 1883
RABBIT_USER = 'gngjbinx'
RABBIT_PASS = 'aFDPKuORkGS0SRvnTO8u6wo8WPdrRH4a'
RABBIT_VHOST = '/'

# Conffig mongodb
MONGO_HOST = '127.0.0.1'
MONGO_PORT = '27017'
MONGO_DB   = 'water_quality_uk'

pathapp = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

pathapp = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))



pathapp = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))



class words(object):

    def __init__(self):
        self.credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASS)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(RABBIT_HOST, RABBIT_PORT, RABBIT_VHOST, self.credentials))
        self.channel = self.connection.channel()

    # Send task to queue rabbitmq
    def sendqueue(self):
        self.msg = {
            'eid': 1,
            'action': 'action something',
            'data': 'Data something'
        }
        self.message = json.dumps(self.msg)
        print(self.message)
        RabbitMQ().send_data(key_queue_send, self.message)

    def progressqueue(self):
        self.channel.queue_declare(key_queue_send)
        print("[*] Waiting for messages. To exit press CTRL+C")

        self.channel.basic_qos(prefetch_count=1)
        # Callback method action queue
        self.channel.basic_consume(actionqueue, queue=key_queue_send)
        self.channel.start_consuming()


# Action queue from rabbitmq
def actionqueue(ch, method, properties, body):
    print('\nCrawl send content to rabbitmq beforafter save')
    print(" Received %r" % (body))
    print('[*] Start action Taks')
    data = json.loads(body)
    MongoDb().insert('collection_name', data)
    print('[*] End action Taks')
    ch.basic_ack(delivery_tag=method.delivery_tag)
class RabbitMQ(object):

    def __init__(self):
        self.credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASS)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(RABBIT_HOST, RABBIT_PORT, RABBIT_VHOST, self.credentials))
        self.channel = self.connection.channel()

    def send_data(self, key_queue_name, message):
        print('\nSend msg to queue rabbitmq')
        print(time.strftime("%H:%M:%S %Y/%m/%d"))
        self.channel.queue_declare(key_queue_name)
        self.channel.basic_publish(exchange='', routing_key=key_queue_name, body=message)
        self.connection.close()
        print("[x] Sent " + message)

    def receive_data(self, key_queue_name):
        self.channel.queue_declare(key_queue_name)
        print("[*] Waiting for messages. To exit press CTRL+C")

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(callback, queue=key_queue_name)
        self.channel.start_consuming()


def callback(ch, method, properties, body):
    print(" Received %r" % (body))
    ch.basic_ack(delivery_tag=method.delivery_tag)

class MongoDb(object):

    def __init__(self):
        self.moConn = MongoClient("mongodb+srv://test:1234@cluster0-wytxl.gcp.mongodb.net/test?retryWrites=true&w=majority")
        self.dbname = self.moConn["water_quality_uk"]

    def insert(self, collection, data):
        newRowId = self.dbname[collection].insert(data)
        print("New Row id: " + repr(newRowId))
        self.moConn.close()

if __name__ == '__main__':
    argNames = ['command', 'task']
    args = dict(list(zip(argNames, sys.argv)))

    tasks = ['sendqueue', 'progressqueue']

    if 'task' not in args:
        print('===> Not found task in tasks')
        for vtask in tasks:
            print(('- ' + vtask))
        exit()

    task = args['task']
    if task in tasks:

        # words.Worker().sendqueue()

        method_to_call = getattr(words.Worker(), task)
        method_to_call()
    else:
        print('===> Not found task in tasks')
        for vtask in tasks:
            print(('- ' + vtask))
        exit()