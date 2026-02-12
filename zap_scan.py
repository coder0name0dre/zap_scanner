import time
import json
import csv
from zapv2 import ZAPv2

# Configuration #

# target website
target_url = "https://demo.owasp-juice.shop"

# ZAP API configuration
zap_api_key = ""  # leave empty unless you configured one
zap_proxy = "http://127.0.0.1:8080"

# output files
json_output = "results.json"
csv_output = "results.csv"


# Connect To ZAP #

print("Connecting to OWASP ZAP...")
print("Waiting for ZAP to be ready...")
time.sleep(3)

zap = ZAPv2(
    apikey=zap_api_key,
    proxies={
        "http": zap_proxy,
        "https": zap_proxy
    }
)

print("Connected to ZAP!")


# Spider Scan #

print(f"Starting spider scan on {target_url}")

scan_id = zap.spider.scan(target_url)

# wait until spider finishes
while int(zap.spider.status(scan_id)) < 100:
    print(f"Spider progress: {zap.spider.status(scan_id)}%")
    time.sleep(2)

print("Spider scan completed!")


# Active Scan #

print("Starting active vulnerability scan...")

scan_id = zap.ascan.scan(target_url)

# wait until active scan finishes
while int(zap.ascan.status(scan_id)) < 100:
    print(f"Active scan progress: {zap.ascan.status(scan_id)}%")
    time.sleep(5)

print("Active scan completed!")


# Collect Results #

print("Fetching alerts from ZAP...")

alerts = zap.core.alerts(baseurl=target_url)

print(f"Total alerts found: {len(alerts)}")


# Save Results To JSON #

print("Saving results to JSON file...")

with open(json_output, "w") as json_file:
    json.dump(alerts, json_file, indent=4)

print(f"Results saved to {json_output}")


# Save Results to CSV #

print("Saving results to CSV file...")

# Define CSV columns
csv_headers = [
    "alert",
    "risk",
    "confidence",
    "url",
    "param",
    "description",
    "solution"
]

with open(csv_output, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()

    for alert in alerts:
        writer.writerow({
            "alert": alert.get("alert"),
            "risk": alert.get("risk"),
            "confidence": alert.get("confidence"),
            "url": alert.get("url"),
            "param": alert.get("param"),
            "description": alert.get("description"),
            "solution": alert.get("solution")
        })

print(f"Results saved to {csv_output}")


# Finished #

print("\nScan completed successfully!")
print("Check results.json and results.csv for details.")