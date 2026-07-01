# Salesforce Connector

Category: Connector

System:
Salesforce

Use When:
- The integration needs to create, update, upsert, query, or delete Salesforce records.
- Salesforce is either the source system or target system.
- CRM data such as Account, Contact, Lead, Opportunity, or Case is involved.

Common Operations:
- Query
- Create
- Update
- Upsert
- Delete

Boomi Recommendation:
- Use Salesforce Connector for standard Salesforce object operations.
- Use Upsert when source records should create or update Salesforce records.
- Use External ID fields for reliable matching during Upsert.
- Use batching when processing moderate or high data volumes.
- Validate required Salesforce fields before connector execution.

Typical Use Cases:
- Local Database to Salesforce customer upsert.
- Workday to Salesforce employee or account updates.
- Salesforce to SAP customer synchronization.
- Salesforce to data warehouse extraction.

Risks:
- API limits.
- Authentication failure.
- Missing required fields.
- Duplicate records if External ID is not used correctly.
- Validation rule failures inside Salesforce.

Best Practices:
- Use OAuth2 authentication where possible.
- Use External ID for Upsert operations.
- Validate mandatory fields before sending data to Salesforce.
- Do not retry Salesforce validation errors without correction.
- Log failed records with Salesforce error messages.