# 🗂️ Check Folder Contents with Kafka (Deployment Monitor)

This project is a **Kafka-based file validation and deployment system** that watches for file deployment requests and ensures all expected files exist **before deployment proceeds**. It's useful in cases where files must be validated before pushing them into production systems (e.g., videos, configs, datasets, etc.).

> ✅ This project also monitors if **any files are missing**, and sends a validation response with the deployment status!

---

## 📁 What We Did

- Created a **Kafka-based microservice project** to:
  - Accept a **JSON file payload** describing the files to deploy
  - Automatically validate whether the files exist
  - Respond back with a **PASS** or **FAIL** and the reason
- Organized services into **producers**, **validators**, and **monitors**
- Used **Docker** and **Docker Compose** to run Kafka and Zookeeper locally
- Pushed this entire working project to GitHub 🚀

---

## 🚀 How to Use This Project
1️⃣ Clone the Repository

```bash
git clone https://github.com/Talha6360/Check_folder_contents_kafka.git
cd Check_folder_contents_kafka

Start Kafka and Zookeeper (via Docker)
bash
Copy code
docker-compose up -d
This will start:

Kafka broker (localhost:9092)

Zookeeper (localhost:2181)

3️⃣ Open 3 Terminals and Run the Services
Make sure you're inside the kafka-docker-demo folder

✅ Terminal 1 – Run the Producer
bash
Copy code
python scripts/produce.py
This sends a deployment request based on the JSON file inside data/payload.json.

🛡️ Terminal 2 – Run the Validator
bash
Copy code
python scripts/validate_and_respond.py
This validates if the files listed in the deployment payload actually exist.

👀 Terminal 3 – Run the Monitor
bash
Copy code
python scripts/monitor.py
This listens for validation results and logs whether deployment is allowed or rejected.

📝 Example Payload (data/payload.json)
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
You can edit this file to simulate different deployment requests.

📌 Notes
If any file is missing, the validator will send a FAILED response with the missing file(s) listed.

You can add test video files inside the correct path:
data/serve/org2/ws5/collB/

💻 Tech Stack
Apache Kafka (via Docker)

Python 3 (producer, validator, monitor)

JSON for file payload

YAML (docker-compose.yml) for service orchestration

🔧 Future Enhancements (Optional Ideas)
Add email or Slack notifications on validation result

Store validation logs in a database

Web UI to upload payload JSON

📬 Author
Mohammed Abdul Talha Shahri
🔗 GitHub Profile

🧠 Tip for Beginners
Don't worry if Kafka or Docker is new to you — this project is a simple way to understand:

Kafka message queues

Validating file presence before deployment

Structuring microservices with Python
