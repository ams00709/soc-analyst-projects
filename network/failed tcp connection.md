TCP Connection Analysis (Failed Handshake)
🎯 Objective
Analyze TCP traffic using Wireshark to identify how a connection is established and investigate cases where the connection fails.
🌐 Scenario
A client attempted to establish a TCP connection with an external server over HTTPS (port 443), but the connection did not complete successfully.
🔍 Analysis Steps
1. Applied Filter
Used the following Wireshark filter to capture TCP SYN packets:

tcp.flags.syn == 1
2. Identified Traffic
Source IP (Client): 192.168.1.104
Destination IP (Server): 2.19.198.18
Source Port: 59186
Destination Port: 443 (HTTPS)
3. Observations
The client initiated the connection by sending a SYN packet
No SYN-ACK response was received from the server
The client retransmitted the SYN packet (TCP Retransmission)
No further packets (ACK) were observed
4. TCP Handshake Status
Step
Status
SYN
✅ Sent
SYN-ACK
❌ Not received
ACK
❌ Not sent
➡️ Result: TCP handshake failed
📉 Findings
The connection attempt did not complete due to lack of response from the server
Presence of retransmission indicates possible:
Network connectivity issues
Firewall blocking
Server unavailability
🧠 Conclusion
The analysis shows that the client was unable to establish a TCP connection with the server. The absence of a SYN-ACK response suggests that the server did not respond, leading to a failed handshake.
🛠️ Tools Used
Wireshark
