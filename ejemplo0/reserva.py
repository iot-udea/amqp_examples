#!/usr/bin/env python
import pika
import sys

# Creando la conexion y el canal
print('1. Creando la conexion...')
parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

# Declarar la exchange
print('2. Declarando el exchange...')
channel.exchange_declare(exchange='my_exchange', exchange_type='topic')


# Declarando la cola
print('3. Declarando las colas...')
channel = connection.channel()
channel.queue_declare(queue='my_queue')
channel.queue_declare(queue='my_queue_2')

# Haciendo los binds
print('4. Haciendo los binds...')
channel.queue_bind(exchange='my_exchange', queue='my_queue', routing_key='a.*.c')
channel.queue_bind(exchange='my_exchange', queue='my_queue_2', routing_key='#.e')

# Cerrar conexion
print('5. Cerrando la conexion...')
connection.close()


