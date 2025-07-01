import subprocess
import platform

def detect_os(ip):
    print(f"Detecting OS for {ip}...")
    try:
        if platform.system().lower() == "windows":
            output = subprocess.check_output(f"ping -n 1 {ip}", shell=True).decode()
        else:
            output = subprocess.check_output(f"ping -c 1 {ip}", shell=True).decode()
        
        for line in output.split("\n"):
            if "ttl" in line.lower():
                ttl = int(line.lower().split("ttl=")[-1].split()[0])
                if ttl <= 64:
                    print("[+] Likely OS: Linux/Unix-based")
                elif ttl <= 128:
                    print("[+] Likely OS: Windows")
                else:
                    print("[+] Likely OS: Unknown (High TTL)")
                return
        print("[-] TTL not found in ping output. OS detection failed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ip = input("Enter IP to detect OS: ")
    detect_os(ip)
