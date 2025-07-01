from port_scanner import scan_ports
from brute_forcer import brute_force
from os_detector import detect_os
from banner_grabber import grab_banner

def main():
    print("\n🛠️ Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    print("3. OS Detection (Basic TTL Analysis)")
    print("4. Banner Grabbing")
    choice = input("Choose a module (1-4): ")
    
    if choice == "1":
        target = input("Enter target IP or hostname: ")
        scan_ports(target, range(20, 1025))
    elif choice == "2":
        url = input("Enter login URL: ")
        usernames = ["admin", "user"]
        passwords = ["1234", "admin", "password"]
        brute_force(url, usernames, passwords)
    elif choice == "3":
        ip = input("Enter IP to detect OS: ")
        detect_os(ip)
    elif choice == "4":
        ip = input("Enter target IP: ")
        port = int(input("Enter port number: "))
        grab_banner(ip, port)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
