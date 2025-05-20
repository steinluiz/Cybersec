import requests
from utils import print_boxed
def check_http_headers(url, target):
    lines = [f"HTTP Headers of: {target}"]
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        security_headers = {
            "Content-Security-Policy": {"present": False, "desc": "Protects against XSS"},
            "X-Content-Type-Options": {"present": False, "desc": "Prevents incorrect MIME type interpretation"},
            "X-Frame-Options": {"present": False, "desc": "Protects against clickjacking (iframe)"},
            "Strict-Transport-Security": {"present": False, "desc": "Enforces secure HTTPS connections"},
            "Referrer-Policy": {"present": False, "desc": "Controls information sent in the Referer header"},
            "Permissions-Policy": {"present": False, "desc": "Restricts access to browser features (e.g., camera)"}
        }
        for header in security_headers:
            if header in headers:
                security_headers[header]["present"] = True
        for header, info in security_headers.items():
            status = "✓ Present" if info["present"] else "✗ Missing"
            lines.append(f"{status} - {header}: {info['desc']}")
    except Exception as e:
        lines.append(f"Error checking HTTP headers: {e}")
    print("\n")
    print_boxed(lines)
