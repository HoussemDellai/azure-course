# import logging
# import sys

# handler = logging.StreamHandler(stream=sys.stdout)
# logger = logging.getLogger("azure.servicebus")
# logger.setLevel(logging.DEBUG)
# logger.addHandler(handler)

import os
import datetime
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from dotenv import load_dotenv, dotenv_values

# load environment variables
if os.path.exists(".env"):
    load_dotenv(override=True)
    config = dotenv_values(".env")

SERVICE_BUS_CONNECTION_STRING = os.getenv("SERVICE_BUS_CONNECTION_STRING")
QUEUE_NAME = os.getenv("QUEUE_NAME")

# Create a Service Bus client
servicebus_client = ServiceBusClient.from_connection_string(
    conn_str=SERVICE_BUS_CONNECTION_STRING, 
    logging_enable=True
)

# Create a sender for the queue
with servicebus_client:
    sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
    with sender:
        # Create a message
        now = datetime.datetime.now()
        message = ServiceBusMessage(f"{now} Hello, Azure Service Bus!")

        # Send the message
        sender.send_messages(message)
        print(f"Message sent to the queue {message.message_id}")

        # send message duplicated
        result = sender.send_messages(message)
        print(f"Message sent to the queue {message.message_id}")

        # send message duplicated
        result = sender.send_messages(message)
        print(f"Message sent to the queue {message.message_id}")

# Close the client
servicebus_client.close()
