# API Security Assessment (Access Control)

## Overview
This project presents a security assessment of a web application focusing on API access control.

## Scope
- Frontend application
- Public API endpoints
- Authenticated user testing

## Findings

### 1. Broken Access Control (High)

Description
A normal authenticated user was able to access an admin-only API endpoint.

Affected Endpoint
GET /api/settings

Impact
- Exposure of sensitive admin data
- Email addresses
- Internal configuration
- Potential for further attacks

Root Cause
- Missing role-based authorization checks
- Server only validated authentication, not permissions

Recommendation
- Implement Role-Based Access Control (RBAC)
- Enforce authorization checks on all endpoints
- Return 403 Forbidden for unauthorized users

---

### 2. Inconsistent Authorization (Medium)

Description
The user was able to read admin data but not modify it.

Impact
- Indicates incomplete authorization logic
- Potential for future vulnerabilities

Recommendation
- Apply consistent authorization checks
- Separate read/write/admin permissions clearly

---

## Security Notes
- No XSS vulnerabilities found
- Input validation was properly implemented

## Analyst Perspective (SOC Relevance)
From a SOC perspective, this type of vulnerability may lead to:
- Unusual API access patterns
- Access to restricted endpoints by non-admin users
- Suspicious behavior in logs

Monitoring recommendations:
- Track access to sensitive endpoints
- Detect abnormal API usage per user role
