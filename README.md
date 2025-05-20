# 🔍 Cybersec Scanner

A simple and educational Python tool for scanning common vulnerabilities on a given domain or IP address.  
It performs:

- ✅ Quick Scan (checks a smaller set of ports)
- ✅ Full Scan (checks a wider range of ports)
- ✅ Banner grabbing
- ✅ HTTP security header analysis

Useful for learning cybersecurity basics and testing services on your own infrastructure.

---

## Preview

![image](https://github.com/user-attachments/assets/67a6a7d8-2bdc-4193-bbc6-ef5bcceb52f7)

![image](https://github.com/user-attachments/assets/2139886c-8dd3-4c5b-b9c6-6027c00af39d)

![image](https://github.com/user-attachments/assets/e0ed052a-dd1d-4913-b9eb-05453c8534cf)

---

## Features

- Quick Scan: checks only a few common ports (faster)
- Full Scan: checks a wider set of known ports
- Banner Grabbing: grabs first line of server response
- HTTP Security Headers Check: looks for missing headers like Content-Security-Policy, X-Frame-Options, etc.
- CLI Interface: simple menu system with visual formatting

---

## How to Use

1. Clone the repository

   git clone https://github.com/yourusername/cybersec-scanner.git
   cd cybersec-scanner

2. Install dependencies

   pip install -r requirements.txt

3. Run the scanner

   python main.py

---

## Dependencies

- Python 3.8+
- requests (for HTTP header checks)

---

## Disclaimer

This tool is for educational and authorized testing purposes only.  
Do not use it to scan domains or IPs you do not own or have permission to test.

---

## Learning Resource

This project was made as part of a cybersecurity learning journey.  
Feel free to use it as a base to learn Python, sockets, HTTP, and ethical hacking.

---

## TODO

- Export scan report to .txt
- Add multithreading for faster scans
- Check for known CVEs by banner

---

## License

MIT License. Feel free to use, modify, and share.
