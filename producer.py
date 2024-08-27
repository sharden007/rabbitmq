import pika
import time

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()

# Declare a queue named 'hello'
channel.queue_declare(queue='hello')

# Send 20 messages to the 'hello' queue with the format 'Hello RabbitMQ#n'
for i in range(20):
    message = f'Hello RabbitMQ#{i+1}'
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f" [x] Sent '{message}'")
    time.sleep(5)  # Wait for 5 seconds before sending the next message

# Close the connection
connection.close()