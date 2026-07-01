# Development and Testing Estimation Guidelines

Category: Estimation

Purpose:

These guidelines provide a consistent approach for estimating development
and testing effort for Boomi integration projects.

---

## Complexity Levels

### Low Complexity

Characteristics:

- One source system
- One target system
- Simple mapping
- Standard connectors
- Few business rules
- Low data volume

Typical Development Effort:

2–4 business days

Typical Testing Effort:

1–2 business days

Examples:

- Database → Salesforce
- REST API → Database

---

### Medium Complexity

Characteristics:

- Multiple objects
- Moderate mapping
- Validation logic
- Retry logic
- Scheduled processing
- Medium data volume

Typical Development Effort:

5–8 business days

Typical Testing Effort:

3–5 business days

Examples:

- Database → Salesforce Upsert
- Salesforce → SAP Customer Sync

---

### High Complexity

Characteristics:

- Multiple systems
- Complex mappings
- Multiple integrations
- Advanced transformations
- High volume
- Security requirements

Typical Development Effort:

9–15 business days

Typical Testing Effort:

5–8 business days

Examples:

- SAP ↔ Salesforce
- Multi-system synchronization

---

### Very High Complexity

Characteristics:

- Enterprise-wide integration
- Multiple interfaces
- Custom connectors
- Advanced orchestration
- Large data volume
- Complex business rules

Typical Development Effort:

Requires detailed project estimation.

Typical Testing Effort:

Requires detailed project estimation.

---

## Factors That Increase Complexity

- Multiple source systems
- Multiple target systems
- High data volume
- Complex transformations
- Advanced error handling
- Custom APIs
- Multiple authentication methods
- Real-time processing
- Complex security requirements

---

## Factors That Reduce Complexity

- Standard connectors
- Simple mappings
- Batch processing
- Low data volume
- Single source
- Single target
- Standard authentication

---

## Estimation Best Practices

- Estimates are planning guidance only.
- Always document assumptions.
- Validate requirements before estimating.
- Review estimates after architecture design.
- Update estimates when project scope changes.