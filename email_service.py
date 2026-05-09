from azure.storage.queue import QueueClient
import json
import time

connection_string = "YOUR_AZURE_STORAGE_CONNECTION_STRING"
queue_name = "terraform-alerts"

queue_client = QueueClient.from_connection_string(
    conn_str=connection_string,
    queue_name=queue_name
)

print("Checking Azure Queue for alerts...")

while True:

    messages = queue_client.receive_messages()

    for message in messages:

        alert = json.loads(message.content)

        print("EMAIL ALERT")
        print("====================")
        print(f"Deployment ID: {alert['deployment_id']}")
        print(f"Pipeline: {alert['pipeline']}")
        print(f"Severity: {alert['severity']}")
        print(f"Message: {alert['message']}")

        # Delete message after processing
        queue_client.delete_message(message)

    time.sleep(5)
