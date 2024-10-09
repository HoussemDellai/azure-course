import os
from azure.mgmt.servicebus import ServiceBusManagementClient
from azure.identity import DefaultAzureCredential

QUEUE_NAME=os.getenv('QUEUE_NAME')
NAMESPACE_NAME=os.getenv('NAMESPACE_NAME')
RESOURCE_GROUP_NAME=os.getenv('RESOURCE_GROUP_NAME')
SUBSCRIPTION_ID=os.getenv('SUBSCRIPTION_ID')

# Create a Service Bus client
servicebus_client = ServiceBusManagementClient(
    credential=DefaultAzureCredential(), 
    subscription_id=SUBSCRIPTION_ID
    )

# Create a sender for the queue
with servicebus_client:
    queue = servicebus_client.queues.get(
        resource_group_name=RESOURCE_GROUP_NAME, 
        namespace_name=NAMESPACE_NAME, 
        queue_name=QUEUE_NAME
        )
    print(f'Queue Duplicate detection enabled: {queue.requires_duplicate_detection}')
servicebus_client.close()