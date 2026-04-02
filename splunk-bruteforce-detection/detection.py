import re

count = {}
users = {}

logs = [
    "Failed password for admin from 192.168.1.10 port 22 ssh2",
    "Failed password for root from 10.0.0.5 port 22 ssh2",
    "Failed password for admin from 192.168.1.10 port 22 ssh2",
    "Accepted password for user from 8.8.8.8 port 22 ssh2",
    "Failed password for test from 172.16.0.3 port 22 ssh2",
    "Failed password for root from 10.0.0.5 port 22 ssh2",
    "Failed password for root from 10.0.0.5 port 22 ssh2"
]

for line in logs:
    if "Failed" in line:
        pattern = re.search(r"for (\w+) from (\d+\.\d+\.\d+\.\d+)", line)
        ip = pattern.group(2)
        user = pattern.group(1)

        if ip not in count:
            count[ip] = 1
        else:
            count[ip] += 1

        if user not in users:
            users[user] = 1
        else:
            users[user] += 1

for ip in count:
    print(ip, " --> ", count[ip])

for user in users:
    print(user, " --> ", users[user])

max_count = 0
max_ip = ""

for ip in count:
    if count[ip] > max_count:
        max_count = count[ip]
        max_ip = ip

print("most attacking ip:", max_ip)
