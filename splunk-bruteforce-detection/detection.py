import re

count = {}
users = {}

with open("auth.log", "r") as f:
    logs = f.readlines()

for line in logs:
    if "Failed password" in line:
        pattern = re.search(r"for (\w+) from (\d+\.\d+\.\d+\.\d+)", line)
        
        if pattern:
            ip = pattern.group(2)
            user = pattern.group(1)

            count[ip] = count.get(ip, 0) + 1
            users[user] = users.get(user, 0) + 1

print("=== Failed Attempts by IP ===")
for ip in count:
    print(ip, " --> ", count[ip])

print("\n=== Failed Attempts by User ===")
for user in users:
    print(user, " --> ", users[user])

max_ip = max(count, key=count.get)
print("\nMost attacking ip:", max_ip)
