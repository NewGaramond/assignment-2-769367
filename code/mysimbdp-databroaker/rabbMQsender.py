#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.connection.URLParameters(url='amqp://gngjbinx:aFDPKuORkGS0SRvnTO8u6wo8WPdrRH4a@dove.rmq.cloudamqp.com/gngjbinx'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()