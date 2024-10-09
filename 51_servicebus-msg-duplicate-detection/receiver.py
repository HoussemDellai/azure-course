import os
from azure.servicebus import ServiceBusClient, ServiceBusMessage

SERVICE_BUS_CONNECTION_STRING=os.getenv('SERVICE_BUS_CONNECTION_STRING')
QUEUE_NAME=os.getenv('QUEUE_NAME')

# Create a ServiceBusClient
with ServiceBusClient.from_connection_string(SERVICE_BUS_CONNECTION_STRING) as client:
    # Create a receiver for the queue
    with client.get_queue_receiver(queue_name=QUEUE_NAME) as receiver:
        print("Receiving messages...")
        for msg in receiver:
            print(f"Received: {msg}, {msg.message_id}")
            # Complete the message so that it is removed from the queue
            receiver.complete_message(msg)
            
# Close the client
servicebus_client.close()