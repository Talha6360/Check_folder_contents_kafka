import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'validation_results',
    bootstrap_servers='localhost:9092',
    api_version=(3, 5, 0),
    auto_offset_reset='earliest',
    group_id='result_reader',
    value_deserializer=lambda m: json.loads(m.decode())
)

print("Waiting for validation results...")

for msg in consumer:
    print("Received validation result:", msg.value)
