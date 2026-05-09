from kafka import KafkaProducer
import json
from datetime import datetime
import time

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simulated deployment events
sample_events = [
    {
        "deployment_id": "DEP101",
        "pipeline_name": "vm-provisioning",
        "status": "SUCCESS",
        "resource": "Azure VM"
    },
    {
        "deployment_id": "DEP102",
        "pipeline_name": "storage-provisioning",
        "status": "FAILED",
        "resource": "Azure Storage Account"
    },
    {
        "deployment_id": "DEP103",
        "pipeline_name": "network-deployment",
        "status": "SUCCESS",
        "resource": "Virtual Network"
    }
]

for event in sample_events:

    event["timestamp"] = str(datetime.now())

    producer.send('terraform-deployments', event)

    print(f"Sent Event: {event}")

    producer.flush()

    time.sleep(3)
