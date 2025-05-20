from port_scan import scan_ports
from headers_http import check_http_headers
from utils import clear_screen, print_boxed

clear_screen()
def main():
    while True:
        nivel = input("╔═══════════════════════════════════════════════════════╗\n║              What would you like to do?               ║\n║                                                       ║\n║                     1. Quick Scan                     ║\n║                     2. Full Scan                      ║\n╚═══════════════════════════════════════════════════════╝\n → " )
        if nivel == "1" or nivel == "2":
            break
        clear_screen()
        print("\033[31m╔═══════════════════════════════════════════════════════╗\n║                    Invalid option                     ║\n╚═══════════════════════════════════════════════════════╝\033[0m")
    clear_screen()
    alvo = input("╔═══════════════════════════════════════════════════════╗\n║        Enter the domain or IP address to scan:        ║\n╚═══════════════════════════════════════════════════════╝\n → " )
    portas = scan_ports(alvo, nivel)
    alvo_http = alvo
    if not alvo_http.startswith("http"):
        alvo_http = "http://" + alvo_http
    check_http_headers(alvo_http, alvo)
    resumo = [f"Open ports summary for: {alvo}"]
    for porta, servico, banner in portas:
        banner_info = banner if banner else "Not captured"
        resumo.append(f"✓ {porta}: {servico} - Banner: {banner_info}")
    print_boxed(resumo)
    main()

if __name__ == "__main__":
    main()
