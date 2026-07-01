# Database Connector

Category: Connector

System:
Relational Database

Use When:
- The integration needs to read from or write to a relational database.
- Source or target system is Oracle, SQL Server, PostgreSQL, MySQL, or another supported database.
- Data is processed in scheduled or batch mode.

Common Operations:
- Select
- Insert
- Update
- Delete
- Stored Procedure

Boomi Recommendation:
- Use Database Connector for structured database access.
- Use parameterized queries where possible.
- Use pagination or batching for large result sets.
- Avoid loading very large datasets into memory at once.
- Validate data before mapping to the target system.

Typical Use Cases:
- Local Database to Salesforce nightly upsert.
- Database to SAP batch load.
- Database to Snowflake data synchronization.
- SFTP file to database import.

Risks:
- Long-running queries.
- Database connection timeout.
- Locking or blocking issues.
- Large result sets.
- Data quality issues.

Best Practices:
- Use indexed columns for extraction filters.
- Avoid full table scans when possible.
- Use incremental extraction based on timestamps or change flags.
- Split large datasets into manageable batches.
- Log source record identifiers for failed records.