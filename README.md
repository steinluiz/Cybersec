\# 🔍 Cybersec Scanner

A simple and educational Python tool for scanning common vulnerabilities
on a given domain or IP address. It performs:

\- ✅ \*\*Port scanning\*\* (quick or full) - ✅ \*\*Banner
grabbing\*\* - ✅ \*\*HTTP security header analysis\*\*

Useful for learning cybersecurity basics and testing services on your
own infrastructure.

\-\--

\## 📸 Preview

\`\`\`bash ╔═══════════════════════════════════════════════════════╗ ║
What would you like to do? ║ ║ ║ ║ 1. Quick Scan ║ ║ 2. Full Scan ║
╚═══════════════════════════════════════════════════════╝ → 1

Scanning 10 ports on: example.com ☑ Port 80 open (HTTP) - Banner:
HTTP/1.1 200 OK ☒ Port 22 closed (SSH)

HTTP Headers of: example.com ☒ missing - Content-Security-Policy:
Protects against XSS ☑ present - X-Frame-Options: Protects against
clickjacking

╔══════════════════════════════════════════════════════╗ ║ Open ports
summary of: example.com ║ ║ ✓ 80: HTTP - Banner: HTTP/1.1 200 OK ║
╚══════════════════════════════════════════════════════╝
