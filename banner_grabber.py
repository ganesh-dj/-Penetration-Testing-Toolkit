import socket

def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, port))
        sock.send(b"\r\n")
        banner = sock.recv(1024).decode().strip()
        if banner:
            print(f"[+] Banner for {ip}:{port} => {banner}")
        else:
            print(f"[-] No banner received from {ip}:{port}")
        sock.close()
    except Exception as e:
        print(f"[!] Error grabbing banner: {e}")

if __name__ == "__main__":
    ip = input("Enter target IP: ")
    port = int(input("Enter port number: "))
    grab_banner(ip, port)
