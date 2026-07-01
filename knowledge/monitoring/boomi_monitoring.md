# Boomi Monitoring and Logging Standard

Category: Monitoring and Logging

Use When:
- Integration processes run in production.
- Business-critical data is exchanged.
- Failed records need investigation.
- Support teams need operational visibility.

Boomi Recommendation:
- Enable process reporting.
- Track process execution status.
- Capture success and failure counts.
- Capture document counts.
- Capture connector error responses.
- Log business identifiers for traceability.

Recommended Tracking Fields:
- Process execution ID
- Source system
- Target system
- Source record identifier
- Target record identifier
- Operation type
- Success count
- Failure count
- Error message
- Timestamp

Recommended Boomi Features:
- Process Reporting
- Execution Dashboard
- Process Logs
- Custom Logging
- Alerts / Notifications

Alert Conditions:
- Repeated connector failures.
- Authentication failures.
- Missed schedule.
- High failure percentage.
- Unexpected zero-record processing.
- Long-running execution.

Best Practices:
- Do not log sensitive data such as passwords or tokens.
- Log business identifiers instead of full payloads.
- Use consistent logging format across integrations.
- Capture enough detail to support reprocessing.
- Monitor both technical failures and business validation failures.