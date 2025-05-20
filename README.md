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

╔═══════════════════════════════════════════════════════╗
║              What would you like to do?               ║
║                                                       ║
║                     1. Quick Scan                     ║
║                     2. Full Scan                      ║
╚═══════════════════════════════════════════════════════╝
 → 1

 Scanning 10 ports on: example.com
 ☑ Port 80 open (HTTP) - Banner: HTTP/1.1 200 OK
 ☒ Port 22 closed (SSH)

 HTTP Headers of: example.com
 ☒ missing - Content-Security-Policy: Protects against XSS
 ☑ present - X-Frame-Options: Protects against clickjacking

╔══════════════════════════════════════════════════════╗
║   Open ports summary of: example.com                ║
║     ✓ 80: HTTP - Banner: HTTP/1.1 200 OK            ║
╚══════════════════════════════════════════════════════╝

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

## Project Structure

cybersec-scanner/
├── main.py               # Main script with menu and control flow
├── port_scan.py          # Port scanning and banner grabbing logic
├── headers_http.py       # HTTP header analysis
├── utils.py              # Utility functions (e.g., screen clear, printing)
├── requirements.txt      # Python dependencies
└── README.md             # Project info

---

## Disclaimer

This tool is for educational and authorized testing purposes only.  
Do not use it to scan domains or IPs you do not own or have permission to test.

---

## Learning Resource

This project was made as part of a cybersecurity learning journey.  
Feel free to use it as a base to learn Python, sockets, HTTP, and ethical hacking.

---

## TODO (Suggestions)

- Export scan report to .txt
- Add multithreading for faster scans
- Check for known CVEs by banner

---

## License

MIT License. Feel free to use, modify, and share.
