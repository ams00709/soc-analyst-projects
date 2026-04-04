# 🧪 TCP Connection Analysis (Failed Handshake)

## 🎯 Objective
Analyze TCP traffic using Wireshark to identify how a connection is established and investigate cases where the connection fails.

---

## 🌐 Scenario
A client attempted to establish a TCP connection with an external server over HTTPS (port 443), but the connection did not complete successfully.

---

## 🔍 Analysis Steps

### 1. Applied Filter
tcp.flags.syn == 1
### 2. Identified Traffic
- Source IP (Client): 192.168.1.104  
- Destination IP (Server): 2.19.198.18  
- Source Port: 59186  
- Destination Port: 443 (HTTPS)

### 3. Observations
- Client sent SYN packet  
- No SYN-ACK received  
- Client retransmitted SYN (TCP Retransmission)  
- No ACK observed  

### 4. TCP Handshake Status

| Step     | Status |
|----------|--------|
| SYN      | ✅ Sent |
| SYN-ACK  | ❌ Not received |
| ACK      | ❌ Not sent |

➡️ Result: TCP handshake failed

---

## 📉 Findings
- No response from server  
- Retransmission detected  
- Possible causes:
  - Network issue  
  - Firewall blocking  
  - Server down  

---

## 🧠 Conclusion
The client failed to establish a TCP connection due to missing SYN-ACK response from the server.

---

## 🛠️ Tools Used
- Wireshark

---

## 🚀 Key Takeaways
- TCP uses a 3-way handshake (SYN → SYN-ACK → ACK)  
- Missing responses indicate connection issues  
- Retransmissions are a strong troubleshooting indicator
