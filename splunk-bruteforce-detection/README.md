# SSH Brute Force Detection (Splunk)

## Description
This project detects SSH brute force attacks followed by a successful login using Splunk.

## Detection Logic
- Multiple failed login attempts
- Followed by a successful login
- Same user and IP within a short time window

## Splunk Query
```spl
index=linux_logs ("Failed password" OR "Accepted password")
| rex "Failed password for (?:invalid user )?(?<user>\w+) from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| rex "Accepted password for (?<user>\w+) from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| stats count(eval(searchmatch("Failed password"))) as failed_attempts,
        count(eval(searchmatch("Accepted password"))) as successful_logins
        by user, src_ip
| where failed_attempts > 5 AND successful_logins > 0
```
## Outcome
Detected brute force attack followed by successful compromise.
