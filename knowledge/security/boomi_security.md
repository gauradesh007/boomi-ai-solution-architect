# Boomi Security Standard

Category: Security

Use When:
- Integration processes access enterprise systems.
- Credentials, tokens, certificates, or sensitive data are involved.
- Data moves between internal and external systems.

Boomi Recommendation:
- Use secure connection settings.
- Store credentials securely.
- Use least-privilege access.
- Use HTTPS or secure transport.
- Avoid hardcoding secrets in process logic.
- Restrict access to production processes and environments.

Authentication Guidance:
- Use OAuth2 where supported.
- Use certificates or mutual TLS for stronger transport security.
- Use API keys only when appropriate and approved.
- Avoid basic authentication unless required and secured.

Sensitive Data Guidance:
- Do not log passwords, tokens, secrets, or sensitive payloads.
- Mask or exclude sensitive fields in logs.
- Use secure properties for credentials.
- Limit access to logs containing business-sensitive data.

Access Control:
- Use role-based access.
- Separate development, test, and production access.
- Restrict deployment permissions.
- Review access periodically.

Best Practices:
- Rotate credentials based on company policy.
- Use environment-specific credentials.
- Use approved authentication methods.
- Validate inbound requests before processing.
- Encrypt data in transit.
- Follow internal security and compliance standards.