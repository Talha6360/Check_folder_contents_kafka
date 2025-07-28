# 🗂️ Check Folder Contents with Kafka (Deployment Monitor)

This project is a Kafka-based microservice system that helps validate files before deployment. It simulates a real-world scenario where files (e.g., videos, configs, datasets) must be verified before going live in production.

✅ **Automatically checks if all required files exist before deployment and returns a PASS/FAIL result via Kafka!**

---

## 📦 What This Project Does

- Accepts a JSON deployment payload describing files to be deployed.
- Checks if the specified files exist in the correct folder structure.
- Responds back with deployment status using Kafka:
  - ✅ **PASS** if all files are found.
  - ❌ **FAIL** if any files are missing (with the missing files listed).
- Uses Apache Kafka (via Docker) for communication between services.
- Divides functionality into 3 Python microservices:
  - **Producer**: Sends deployment request.
  - **Validator**: Validates files and sends result.
  - **Monitor**: Monitors validation responses.

---

### Clone the Repository

```bash
git clone https://github.com/Talha6360/Check_folder_contents_kafka.git
cd Check_folder_contents_kafka
