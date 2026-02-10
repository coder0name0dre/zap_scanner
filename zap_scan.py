import time
from zapv2 import ZAPv2

# Configuration #

# target website
target_url = "https://demo.owasp-juice.shop"

# ZAP API configuration
zap_api_key = ""  # leave empty unless you configured one
zap_proxy = "http://127.0.0.1:8080"


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


# Print Results To Terminal #

for index, alert in enumerate(alerts, start=1):
    print("=" * 20)
    print(f"Vulnerability #{index}")
    print("=" * 20)

    print(f"Alert Name   : {alert.get('alert')}")
    print(f"Risk Level   : {alert.get('risk')}")
    print(f"Confidence   : {alert.get('confidence')}")
    print(f"URL          : {alert.get('url')}")
    print(f"Parameter   : {alert.get('param')}\n")

    print("Description:")
    print(alert.get("description", "No description provided."))

    print("\nSolution:")
    print(alert.get("solution", "No solution provided."))


# Finished #

print("\nScan completed successfully!")
print("Results displayed above in the terminal")