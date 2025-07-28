# 🗂️ Check Folder Contents with Kafka (Deployment Monitor)

This project is a **Kafka-based microservice system** that helps **validate files before deployment**. It simulates a real-world scenario where files (e.g., videos, configs, datasets) must be verified before going live in production.

✅ Automatically checks if all required files exist before deployment and returns a PASS/FAIL result via Kafka!

---

## 📦 What This Project Does

- Accepts a **JSON deployment payload** describing files to be deployed.
- Checks if the specified files **exist in the correct folder structure**.
- Responds back with deployment **status** using Kafka:
  - ✅ `PASS` if all files are found.
  - ❌ `FAIL` if any files are missing (with the missing files listed).
- Uses **Apache Kafka (via Docker)** for communication between services.
- Divides functionality into 3 Python microservices:
  - **Producer**: Sends deployment request.
  - **Validator**: Validates files and sends result.
  - **Monitor**: Monitors validation responses.

---

## 🚀 How to Run This Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Talha6360/Check_folder_contents_kafka.git
cd Check_folder_contents_kafka
2️⃣ Start Kafka and Zookeeper via Docker
bash
Copy code
docker-compose up -d
This starts:

Kafka Broker → localhost:9092

Zookeeper → localhost:2181

3️⃣ Open 3 Terminals and Run Services
🟢 Terminal 1 – Producer
bash
Copy code
python scripts/produce.py
🔵 Terminal 2 – Validator
bash
Copy code
python scripts/validate_and_respond.py
🟡 Terminal 3 – Monitor
bash
Copy code
python scripts/monitor.py
📁 Project Structure
text
Copy code
Check_folder_contents_kafka/
├── data/
│   ├── payload.json              # Deployment payload
│   └── serve/org2/ws5/collB/     # Target folder for files
│       ├── video1.mp4
│       └── video2.mp4
├── scripts/
│   ├── produce.py                # Kafka producer
│   ├── validate_and_respond.py   # Validator consumer
│   └── monitor.py                # Monitor consumer
├── docker-compose.yml            # Kafka & Zookeeper services
└── README.md                     # Project documentation
📄 Example Payload (data/payload.json)
json
Copy code
{
  "deployment_id": "deploy_42ef",
  "target": "serve",
  "org": "org2",
  "workspace": "ws5",
  "collection": "collB",
  "files": [
    "video1.mp4",
    "video2.mp4"
  ]
}
💡 Tips
Place required files inside:
data/serve/org2/ws5/collB/

If a file from payload.json is missing, the validator sends a FAIL response listing missing files.

🔧 Tech Stack
🐍 Python 3 (Producer, Validator, Monitor)

🐘 Apache Kafka (via Docker)

📝 JSON (payload format)

⚙️ YAML (docker-compose.yml)

🔮 Future Improvements
Add notifications (Slack/Email) on validation.

Persist logs to a database.

Build a web UI for uploads and results.

👨‍💻 Author
Mohammed Abdul Talha Shahri
🔗 GitHub

🧠 For Beginners
Learn:

Kafka fundamentals (topics, producers, consumers)

Microservice patterns in Python

Docker Compose orchestration
