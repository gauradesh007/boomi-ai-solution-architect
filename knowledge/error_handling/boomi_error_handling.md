# Boomi Error Handling Standard

Category: Error Handling

Use When:
- Any integration calls an external system.
- Connector operations can fail.
- Records can fail validation.
- Failed records need reprocessing or operational review.

Boomi Recommendation:
- Use Try/Catch around connector operations.
- Use exception handling paths for failed records.
- Capture connector response messages.
- Capture source record identifiers.
- Capture process execution ID.
- Separate recoverable and non-recoverable errors.

Recoverable Errors:
- Temporary network failure.
- Timeout.
- HTTP 429 rate limit.
- HTTP 503 service unavailable.
- Temporary downstream outage.

Non-Recoverable Errors:
- Authentication failure.
- Missing required fields.
- Invalid data format.
- Business validation failure.
- Duplicate record failure.

Retry Guidance:
- Retry only transient technical failures.
- Do not retry validation errors without correction.
- Limit retry attempts to avoid duplicate processing.
- Log retry count and final failure reason.

Recommended Boomi Shapes:
- Try/Catch
- Exception
- Decision
- Message
- Set Properties
- Notify or alerting process

Best Practices:
- Always log failed records.
- Store enough context for reprocessing.
- Avoid swallowing exceptions silently.
- Route failed records to an error path.
- Include business identifiers in logs.
- Alert support teams for repeated failures.