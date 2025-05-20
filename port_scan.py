import socket
import ssl
from utils import clear_screen

# List of common ports (https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
COMMON_PORTS_long = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    161: "SNMP",
    194: "IRC",
    443: "HTTPS",
    445: "Microsoft-DS / SMB",
    465: "SMTPS",
    502: "Modbus",
    587: "SMTP (submission)",
    631: "IPP (Impressoras)",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS Proxy",
    1433: "Microsoft SQL Server",
    1521: "Oracle DB",
    1723: "PPTP (VPN)",
    1883: "MQTT (IoT)",
    2049: "NFS",
    2082: "cPanel",
    2083: "cPanel (SSL)",
    2483: "Oracle DB (não-SSL)",
    2484: "Oracle DB (SSL)",
    3306: "MySQL",
    3389: "RDP (Remote Desktop)",
    3690: "Subversion",
    4333: "MySQL Admin",
    5000: "Flask / HTTP Dev",
    5432: "PostgreSQL",
    5900: "VNC",
    5984: "CouchDB",
    6379: "Redis",
    6667: "IRC",
    7001: "WebLogic Admin",
    8000: "Django / Dev Servers",
    8008: "HTTP Alt / Reverse Proxy",
    8080: "HTTP Alt / Proxies",
    8081: "JBoss",
    8443: "HTTPS Alt / Tomcat",
    8888: "Jupyter Notebook / Alt Dev",
    9200: "Elasticsearch",
    9300: "Elasticsearch cluster",
    10000: "Webmin",
    11211: "Memcached",
    27017: "MongoDB"
}

COMMON_PORTS_short = { #Quick scan using essential ports only
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP-alt",
    8443: "HTTPS-alt",
    3000: "Dev Server (Node.js)",
    5000: "Dev Server (Flask)",
    8000: "Dev Server (Django)",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    27017: "MongoDB"
}



# Ports that typically use SSL
SSL_PORTS = [443, 8443, 2083, 2484]

def banner_grab(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((target, port))

        use_ssl = port in SSL_PORTS
        if use_ssl:
            context = ssl.create_default_context()
            sock = context.wrap_socket(sock, server_hostname=target)

        request = f"GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: Mozilla/5.0\r\nConnection: close\r\n\r\n".encode()
        sock.send(request)
        response = sock.recv(1024).decode("utf-8", errors="ignore")
        first_line = response.split("\r\n")[0] if response else "No response"
        sock.close()
        return first_line
    except Exception as e:
        return "No response"

def scan_ports(target, level):
    ports_to_scan = COMMON_PORTS_short if level == "1" else COMMON_PORTS_long
    clear_screen()
    info = f"║ Scanning {len(ports_to_scan)} ports on: {target} ║"
    print("╔" + "═" * (len(info) - 2) + "╗")
    print(info)
    print("╚" + "═" * (len(info) - 2) + "╝")

    open_ports = []
    for port in ports_to_scan:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            service = ports_to_scan[port]
            if result == 0:
                banner = banner_grab(target, port)
                print(f" ✓ Port {port} open ({service}) - Banner: {banner}")
                open_ports.append((port, service, banner))
            else:
                print(f" ✗ Port {port} closed ({service})")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
    return open_ports