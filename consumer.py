import pika
import threading
import time

# Global variable to track the last received message time
last_message_time = time.time()

# Callback function to process received messages
def callback(ch, method, properties, body):
    global last_message_time
    print(f"Received {body}")
    last_message_time = time.time()  # Update the last message time
    time.sleep(0.5)
# Function to print "Waiting for messages..." every 7 seconds
def print_waiting_message():
    while True:
        time.sleep(7)
        if time.time() - last_message_time >= 7:
            print(" [*] Waiting for messages...")

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()

# Declare a queue named 'hello'
channel.queue_declare(queue='hello')

# Set up subscription on the 'hello' queue
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

# Start a separate thread to print the waiting message
waiting_thread = threading.Thread(target=print_waiting_message, daemon=True)
waiting_thread.start()

print(' [*] Waiting for messages. To exit press CTRL+C')
# Start consuming messages
channel.start_consuming()