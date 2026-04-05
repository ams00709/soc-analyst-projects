# 🌐 Network Traffic Analysis using Wireshark (DNS + HTTP)

## 🎯 Objective
Analyze how a client resolves a domain using DNS and communicates with a web server using HTTP.

---

## 🌍 Scenario
A user accessed the following website:

http://httpforever.com

The goal is to analyze the full communication flow from DNS resolution to HTTP request.

---

## 🔍 Analysis Steps

### 1. DNS Analysis

Captured a DNS query for:

- Domain: httpforever.com  
- Record Type: A (IPv4)  
- Extracted IP address from the DNS response  

### 2. HTTP Analysis

Identified HTTP request:
