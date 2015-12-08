#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('rabbit', 'x')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost', port=5672, virtual_host='/et-staging', credentials=credentials))
channel = connection.channel()


#channel.queue_declare(queue='filippos')

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='filippos',
                      no_ack=True)

channel.start_consuming()
