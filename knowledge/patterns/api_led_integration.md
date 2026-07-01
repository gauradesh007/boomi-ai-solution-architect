# API-Led Integration Pattern

Category: Integration Pattern

Use When:
- Real-time request-response behavior is required.
- External systems or applications need reusable APIs.
- Low-latency integration is important.
- Multiple consumers may call the same integration service.

Avoid When:
- Large volume batch processing is required.
- Processing can be scheduled.
- Long-running asynchronous processing is expected.

Boomi Recommendation:
- Use Boomi API components where applicable.
- Use REST or HTTP Client connector.
- Use Try/Catch around downstream calls.
- Validate request payload before processing.
- Return clear error responses to API consumers.
- Enable monitoring and request logging.

Typical Use Cases:
- Customer portal to CRM.
- Salesforce to SAP real-time lookup.
- Mobile application to enterprise API.

Risks:
- API timeout.
- Downstream system outage.
- Authentication failure.
- Rate limits.

Best Practices:
- Keep APIs lightweight.
- Use authentication and authorization controls.
- Avoid long-running logic inside synchronous APIs.
- Add clear error handling and response codes.