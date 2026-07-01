# Batch Integration Pattern

Category: Integration Pattern

Use When:
- Data is processed on a schedule.
- High or moderate volume records need to be moved.
- Real-time response is not required.
- Source data can be collected and processed in groups.

Avoid When:
- Business process requires immediate response.
- Users expect synchronous request-response behavior.

Boomi Recommendation:
- Use a scheduled Start shape.
- Use source connector pagination or batching.
- Use Data Process shape to split documents when needed.
- Use Map shape for transformation.
- Use Try/Catch for connector operations.
- Enable Process Reporting and logging.

Typical Use Cases:
- Local Database to Salesforce nightly customer upsert.
- SAP to Snowflake daily data load.
- SFTP file to database scheduled import.

Risks:
- Long-running executions.
- API limits.
- Large file or document size.
- Missed schedules.

Best Practices:
- Use batching and pagination.
- Track success and failure counts.
- Log failed records for reprocessing.
- Avoid retrying validation errors.