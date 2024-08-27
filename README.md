# rabbitmq
This demonstrates the basic capabilities of RabbitMQ as a message broker, allowing asynchronous communication between different parts of a system. Note: RabbitMQ is running in a docker comtainer.

# 
Producer:
Connects to the RabbitMQ server running on localhost at port 5672.
Declares a queue named hello. If the queue does not exist, it will be created.
Sends a message "Hello RabbitMQ!" to the hello queue.
Closes the connection after sending the message.

Consumer:
Connects to the RabbitMQ server on localhost at port 5672.
Declares the same queue hello to ensure the queue exists.
Sets up a subscription to receive messages from the hello queue.
Defines a callback function that is called whenever a message is received. It prints the received message.
Starts consuming messages, waiting for messages to arrive in the queue.