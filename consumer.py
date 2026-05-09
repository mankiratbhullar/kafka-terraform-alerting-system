from kafka import KafkaConsumer
from azure.storage.queue import QueueClient
import json

# Azure Queue Connection
connection_string = "YOUR_AZURE_STORAGE_CONNECTION_STRING"
queue_name = "terraform-alerts"

queue_client = QueueClient.from_connection_string(
    conn_str=connection_string,
    queue_name=queue_name
)

# Kafka Consumer
consumer = KafkaConsumer(
    'terraform-deployments',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='deployment-monitor-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening for deployment events...")

for message in consumer:

    event = message.value

    print(f"Received Event: {event}")

    # Detect failed deployments
    if event['status'] == 'FAILED':

        alert_message = {
            "severity": "HIGH",
            "deployment_id": event['deployment_id'],
            "pipeline": event['pipeline_name'],
            "message": f"Deployment failed for {event['resource']}"
        }

        # Push to Azure Queue
        queue_client.send_message(json.dumps(alert_message))

        print("Alert pushed to Azure Queue")
