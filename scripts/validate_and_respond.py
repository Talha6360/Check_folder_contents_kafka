import os
import json
from kafka import KafkaConsumer, KafkaProducer

# Consumer listens to deployment payloads
consumer = KafkaConsumer(
    'deployments',
    bootstrap_servers='localhost:9092',
    api_version=(3, 5, 0),
    auto_offset_reset='earliest',
    group_id='validator',
    value_deserializer=lambda m: json.loads(m.decode())
)

# Producer sends validation results
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    api_version=(3, 5, 0),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🟢 Validator is running and waiting for messages…")

for msg in consumer:
    data = msg.value

    missing_files = [
        f['file_path'] for f in data.get('files', [])
        if not os.path.exists(f['file_path'])
    ]

    result = {
        "deployment_id": data.get("deployment_id"),
        "verified": len(missing_files) == 0,
        "status": "SUCCESS" if len(missing_files) == 0 else "FAILED"
    }

    if missing_files:
        result["reason"] = f"{len(missing_files)} missing"
        result["non_existent_files"] = missing_files

    producer.send('validation_results', result)
    producer.flush()

    print("✅ Validation result sent:", result)
