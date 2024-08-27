import pika

# Callback function to process received messages
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()

# Declare a queue named 'hello'
channel.queue_declare(queue='hello')

# Set up subscription on the 'hello' queue
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
# Start consuming messages
channel.start_consuming()