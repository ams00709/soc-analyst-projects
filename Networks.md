Network Traffic Analysis using Wireshark
##🎯 Objective
Analyze network traffic using Wireshark to understand how a client resolves a domain (DNS) and communicates with a web server using HTTP.
##🔍 Scenario
A user accessed the following website:

http://example.com
The goal is to analyze the full communication flow:
DNS resolution (domain → IP)
HTTP request (client → server)
##🧠 Analysis Steps
1. DNS Analysis
Captured a DNS query for:

example.com
Identified record type:
A (IPv4)
Extracted IP address from the response:

104.18.x.x
2. HTTP Analysis
Identified HTTP request:

GET / HTTP/1.1
Extracted:
Host: example.com
User-Agent: Mozilla/5.0 ...
3. Traffic Correlation
The client first performed a DNS query to resolve the domain
After receiving the IP, it sent an HTTP GET request to the server
##👉 This demonstrates the full communication flow:

DNS → HTTP
##🛠️ Tools Used
Wireshark
##📌 Key Takeaways
DNS translates domain names into IP addresses
HTTP enables communication between client and server
Traffic correlation is essential for network analysis and SOC investigations

🚀 Additional Note
This project demonstrates practical network analysis skills relevant to SOC and networking roles.
