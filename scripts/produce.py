import json
import os
import sys
import argparse
from kafka import KafkaProducer
from kafka.errors import KafkaError

def load_payload(path):
    if not os.path.exists(path):
        print(f"❌ Payload file not found: {path}")
        sys.exit(1)
    with open(path, 'r') as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="Kafka producer for deployment payload")
    parser.add_argument(
        "--bootstrap-server",
        default="localhost:9092",
        help="Kafka bootstrap server (default: localhost:9092)"
    )
    parser.add_argument(
        "--topic",
        default="deployments",
        help="Kafka topic to send to (default: deployments)"
    )
    parser.add_argument(
        "--payload",
        default="deployment_payload.json",
        help="Path to your JSON payload file (default: deployment_payload.json)"
    )
    args = parser.parse_args()

    payload = load_payload(args.payload)

    producer = KafkaProducer(
        bootstrap_servers=args.bootstrap_server,
        api_version=(3, 5, 0),
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        retries=3,
        linger_ms=10
    )

    try:
        future = producer.send(args.topic, payload)
        record_metadata = future.get(timeout=10)
        print(f"✅ Payload sent to {record_metadata.topic} partition {record_metadata.partition} @ offset {record_metadata.offset}")
    except KafkaError as e:
        print(f"❌ Failed to send payload: {e}")
        sys.exit(1)
    finally:
        producer.flush()
        producer.close()

if __name__ == "__main__":
    main()
