 🛠️ Penetration Testing Toolkit

A modular penetration testing toolkit built using Python as part of the **CodTech Internship (Task 3)**.

> 🔐 This project demonstrates foundational tools for penetration testing and ethical hacking.

---

## 👨‍💻 Developed By

- **Name:** D.J. Ganesh  
- **Intern ID:** CITSOD227  
- **Company:** CodTech IT Solutions  
- **Domain:** Cyber Security & Ethical Hacking  
- **Mentor:** Neela Santosh  
- **Internship Duration:** 6 Weeks  

---


## 📌 About the Project


This toolkit provides essential modules to perform basic penetration testing tasks such as:

- ✅ Scanning open ports on a host  
- ✅ Brute-forcing login credentials  
- ✅ OS Detection using TTL analysis  
- ✅ Banner Grabbing for fingerprinting  

The project is designed with simplicity and modularity in mind so that even beginners in cybersecurity can understand and extend it.


---


## 🔍 Toolkit Modules


### 1. 🔎 Port Scanner
Scans a range of ports on a given IP or hostname to find open ports.

```bash

python port_scanner.py

2. 🔐 Brute Forcer

Attempts to brute-force login credentials (for testing purposes) using POST requests.

bash

python brute_forcer.py
⚠️ Only use this on test environments like DVWA or bWAPP.



3. 🧠 OS Detector


Guesses the target operating system based on the TTL value from ping responses.

bash

python os_detector.py


4. 🛰️ Banner Grabber


Connects to a port on the target IP and grabs the service banner (e.g., from FTP, SSH, etc.).

bash

python banner_grabber.py


▶️ Main Launcher


To access all tools through one interface:

bash
Copy code
python main.py
Select a tool from the interactive menu.



📦 Requirements


Python 3.x

requests

Install dependencies with:

bash
Copy code
pip install -r requirements.txt


📁 Folder Structure


css
penetration-testing-toolkit/
├── banner_grabber.py
├── brute_forcer.py
├── main.py
├── os_detector.py
├── port_scanner.py
├── README.md
└── requirements.txt


🧠 Learning Outcome


This project helped me:

Learn how basic security tools are designed

Understand network protocols and socket programming

Apply real-world cybersecurity skills responsibly



💡 Future Improvements


Add custom wordlist support for brute force

Log output to a report file (JSON or TXT)

Integrate advanced scanning (nmap wrapper, shodan API)

Add a GUI version using Tkinter or PyQt



⚠️ Disclaimer


This project is intended only for educational and ethical hacking purposes.
⚠️ Do not use these tools on live websites or servers without proper authorization.


📜 License

MIT License – Free to use, modify, and share.
