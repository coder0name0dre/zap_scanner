# OWASP ZAP Python Web Application Scanner

This script is a Python cybersecurity project that uses OWASP ZAP to scan web applications for security vulnerabilities and export the results to JSON and CSV files.

---

## Features

- Uses OWASP ZAP (industry standard web app scanner)
- Performs:
    - Spider scan (crawling)
    - Active vulnerability scan
- Exports scan results to:
    - `results.json`
    - `results.csv`
- Uses **safe, legal practice targets**

**Only scan websites you own or have explicit permission to test.**

---

## Safe Practice Targets (Legal to Scan)

| Website | Description |
|------|------|
| https://demo.owasp-juice.shop | OWASP Juice Shop (recommended) |
| https://dvwa.co.uk | Damn Vulnerable Web App |
| http://testfire.net | Altoro Mutual training app |
| OWASP WebGoat | Learning-focused vulnerable app |

---

## Requirements

- Python 3.8+
- OWASP ZAP (running locally)
- Internet connection

---

## Installation

### 1. Install OWASP ZAP

Download and install from:

```
https://www.zaproxy.org/download/
```

**Launch ZAP before running the script.**

---

### 2. Install Python Dependencies

```
pip install python-owasp-zap-v2.4
```

---

## How To Run

1. Open OWASP ZAP:
    a. When prompted, choose "No, I do not want to persist this session at this moment in time"
    b. At the bottom bar of ZAP, you should see:

    ```
    localhost:8080
    ```

    c. Go to **Tools**, and then **Options**
    d. Select **API**
    e. Make sure:
        - Enable API is ticked
        - API Key is disabled
    f. Click **OK**

    Open a browser and go to:

    ```
    http://127.0.0.1:8080/JSON/core/view/version/
    ```

    If ZAP is working, you'll see something like:

    ```
    {
        "version":"2.17.0"
    }
    ```

2. Run the Python scanner:

```
python zap_scan.py
```

---

## Output Files

### `results.json`
- Full structured vulnerability data
- Useful for automation and integrations

### `results.csv`
- Human readable format
- Easy to open in Excel / Google Sheets

---

## Risk Levels Explained

| Level | Meaning |
|------|------|
| High | Serious vulnerability |
| Medium | Needs fixing |
| Low | Minor issue |
| Informational | Not exploitable, but useful |

---

## References

- OWASP ZAP: [https://www.xaproxy.org/](https://www.zaproxy.org/)
- OWASP Top 10: [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)
- Python ZAP API: [https://pypi.org/project/python-owasp-zap-v2.4/](https://pypi.org/project/python-owasp-zap-v2.4/)

---

## License

This project is licensed under the [MIT License](https://github.com/coder0name0dre/zap_scanner/blob/main/LICENSE).