# SSH Brute Force Detection (Splunk)

## Description
This project detects SSH brute force attacks followed by a successful login using Splunk.

## Detection Logic
- Multiple failed login attempts
- Followed by a successful login
- Same user and IP within a short time window

## Splunk Query
index=linux_logs ("Failed password" OR "Accepted password")
| rex "Failed password for (?:invalid user )?(?<user>\w+) from (?<src_ip>[\d\.]+)"
| rex "Accepted password for (?<user>\w+) from (?<src_ip>[\d\.]+)"
| eval action=if(searchmatch("Failed password"), "failed", "success")
| sort 0 _time
| transaction user src_ip maxspan=2m
| search eventcount>3 AND action="success"
## Result
The detection identifies suspicious IPs performing brute force attacks followed by successful login.
## Fields Extracted
- user
- src_ip

## Detection Method
Used Splunk transaction to correlate failed and successful login events within a 2-minute window.

## Attack Scenario
Simulated SSH brute force attack where multiple failed attempts were followed by a successful login.
