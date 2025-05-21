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


```bash
╔═══════════════════════════════════════════════════════╗
║              What would you like to do?               ║
║                                                       ║
║                     1. Quick Scan                     ║
║                     2. Full Scan                      ║
╚═══════════════════════════════════════════════════════╝
 → 1

╔═══════════════════════════════════════════════════════╗
║        Enter the domain or IP address to scan:        ║
╚═══════════════════════════════════════════════════════╝
 → example.com

╔═══════════════════════════════════╗
║ Scanning 14 ports on: example.com ║
╚═══════════════════════════════════╝
 ✗ Port 21 closed (FTP)
 ✗ Port 22 closed (SSH)
 ✗ Port 25 closed (SMTP)
 ✓ Port 80 open (HTTP) - Banner: HTTP/1.1 200 OK
 ✓ Port 443 open (HTTPS) - Banner: HTTP/1.1 200 OK
 ✗ Port 8080 closed (HTTP-alt)
 ✗ Port 8443 closed (HTTPS-alt)
 ✗ Port 3000 closed (Dev Server (Node.js))
 ✗ Port 5000 closed (Dev Server (Flask))
 ✗ Port 8000 closed (Dev Server (Django))
 ✗ Port 3306 closed (MySQL)
 ✗ Port 5432 closed (PostgreSQL)
 ✗ Port 6379 closed (Redis)
 ✗ Port 27017 closed (MongoDB)


╔═════════════════════════════════════════════════════════════════════════════════════╗
║ HTTP Headers of: example.com                                                        ║
║ X Missing - Content-Security-Policy: Protects against XSS                           ║
║ X Missing - X-Content-Type-Options: Prevents incorrect MIME type interpretation     ║
║ X Missing - X-Frame-Options: Protects against clickjacking (iframe)                 ║
║ X Missing - Strict-Transport-Security: Enforces secure HTTPS connections            ║
║ X Missing - Referrer-Policy: Controls information sent in the Referer header        ║
║ X Missing - Permissions-Policy: Restricts access to browser features (e.g., camera) ║
╚═════════════════════════════════════════════════════════════════════════════════════╝
╔════════════════════════════════════════╗
║ Open ports summary for: example.com    ║
║ O 80: HTTP - Banner: HTTP/1.1 200 OK   ║
║ O 443: HTTPS - Banner: HTTP/1.1 200 OK ║
╚════════════════════════════════════════╝

```
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

   git clone https://github.com/steinluiz/Cybersec.git
   cd cybersec-scanner

3. Install dependencies

   pip install -r requirements.txt

4. Run the scanner

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
