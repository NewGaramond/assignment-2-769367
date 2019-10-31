#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.connection.URLParameters(url='amqp://gngjbinx:aFDPKuORkGS0SRvnTO8u6wo8WPdrRH4a@dove.rmq.cloudamqp.com/gngjbinx'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()