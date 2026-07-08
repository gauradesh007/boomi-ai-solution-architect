# Software Requirements Specification (SRS)
# Boomi AI Solution Architect

Version: 1.1  
Status: Draft  
Primary Platform: Boomi  
Designed for Future Platform Replacement: Yes  

---

## 1. Purpose

Boomi AI Solution Architect is an AI-powered enterprise integration architecture assistant.

The application helps users generate professional, implementation-ready integration architecture recommendations by combining:

- Structured requirement inputs
- Plain-English business requirements
- A pluggable knowledge layer
- Deterministic architecture tools
- Multi-agent LangGraph workflow
- Development and testing estimation
- Human approval
- Exportable architecture reports

Although the first implementation focuses on Boomi, the architecture must be reusable for future platforms such as MuleSoft, Azure Integration Services, Informatica, SnapLogic, or other enterprise integration platforms.

---

## 2. Product Vision

The product should shift users away from open-ended prompts such as:

> How do I connect Salesforce to SAP?

toward a guided architecture workflow:

```text
Structured Inputs
+
Business Requirement
+
Trusted Knowledge
+
Architecture Rules
+
Effort Estimation
+
Agent Workflow
=
Professional Integration Architecture Report
```

The system should not behave like a generic chatbot. It should behave like an AI-assisted solution architect.

---

## 3. Scope

### 3.1 In Scope for MVP

- Streamlit UI
- Ollama-based local version
- LangGraph workflow
- Persistent ChromaDB knowledge store
- Curated architecture knowledge
- Dynamic source and target system inputs
- Integration pattern recommendation
- Connector recommendation
- Risk and complexity estimation
- Development and testing estimate
- Architecture report generation
- Architecture review
- Human approval
- Markdown export

### 3.2 Future Scope

- OpenAI / ChatGPT API version
- PDF export
- Word export
- Mermaid architecture diagrams
- Official documentation retrieval
- Internal enterprise document connectors
- Knowledge source citation
- Multi-platform support
- User login and saved reports
- Report history
- Team collaboration
- Detailed cost estimation
- Sprint planning estimate
- Boomi process skeleton generation

### 3.3 Out of Scope for MVP

- Production authentication
- Enterprise SSO
- Live Boomi API deployment
- Automatic Boomi process creation
- Real-time connector validation from Boomi runtime
- Financial cost estimation
- Healthcare EDI validation

---

## 4. Target Users

- Boomi Developers
- Integration Architects
- Solution Architects
- Technical Leads
- Enterprise Integration Engineers
- Integration Consultants
- Delivery Leads
- Project Managers needing rough implementation estimates

---

## 5. Core User Workflow

```text
User opens Streamlit app
↓
User enters structured integration metadata
↓
User enters plain-English business requirement
↓
Requirements Agent validates inputs
↓
Clarification Agent checks missing details
↓
Planner Agent creates implementation plan
↓
Knowledge Layer retrieves relevant guidance
↓
Pattern Tool recommends integration pattern
↓
Connector Tool recommends platform connectors
↓
Risk Tool identifies delivery risks
↓
Complexity Tool estimates solution complexity
↓
Estimation Agent estimates development and testing effort
↓
Architecture Agent drafts report
↓
Review Agent validates report
↓
Human reviews / edits / approves
↓
Final Report Agent formats output
↓
User exports report
```

---

## 6. UI Requirements

### 6.1 Main Screen

The main screen must include:

- Application title
- Short description
- Structured input form
- Business requirement text area
- Generate Architecture button
- Workflow progress/status area
- Final report area
- Export buttons

### 6.2 Structured Inputs

| Field | Type | Required | Example |
|---|---|---:|---|
| Source System | Dropdown + Custom | Yes | Local Database |
| Target System | Dropdown + Custom | Yes | Salesforce |
| Integration Style | Dropdown | Yes | Batch |
| Operation Type | Dropdown | Yes | Upsert |
| Frequency | Dropdown | Yes | Daily |
| Expected Volume | Text / Number | Yes | 50,000 records/day |
| Number of Objects / Entities | Number | Optional | 3 |
| Mapping Complexity | Dropdown | Optional | Low / Medium / High |
| Transformation Complexity | Dropdown | Optional | Low / Medium / High |
| Authentication Type | Dropdown | Optional | OAuth2 |
| Runtime Environment | Dropdown | Optional | Atom / Molecule / Cloud |
| Testing Scope | Dropdown | Optional | Unit + SIT + UAT |
| Additional Constraints | Text Area | Optional | Must complete before 6 AM |

### 6.3 Source and Target System Values

Initial values:

- Salesforce
- SAP
- Local Database
- REST API
- SFTP
- Workday
- Snowflake
- Oracle
- SQL Server
- PostgreSQL
- Custom

The design must allow new platforms to be added without changing core workflow logic.

### 6.4 Human Approval UI

After report generation, user must be able to choose:

- APPROVE
- REJECT
- REQUEST_CHANGES

If REQUEST_CHANGES is selected, user must be able to enter feedback.

---

## 7. Functional Requirements

- FR-001: Capture structured metadata about the integration request.
- FR-002: Capture a plain-English business requirement.
- FR-003: Validate required inputs before executing the agent workflow.
- FR-004: Detect missing or ambiguous details and ask clarification questions.
- FR-005: Retrieve relevant architecture knowledge from the Knowledge Layer.
- FR-006: Recommend an integration pattern based on structured inputs and business requirement.
- FR-007: Recommend platform-specific connectors based on source and target systems.
- FR-008: Generate a structured architecture report.
- FR-009: Review the report against validation rules.
- FR-010: Revise the report if review fails or user requests changes.
- FR-011: Require human approval before finalizing the report.
- FR-012: Export the final report as Markdown in MVP.
- FR-013: Generate development and testing estimate.
- FR-014: Explain estimation assumptions and complexity drivers.
- FR-015: Include estimation section in the final report.

---

## 8. Non-Functional Requirements

- NFR-001: Separate UI, workflow, knowledge layer, tool layer, prompts, and report templates.
- NFR-002: Isolate Boomi-specific logic so future platforms can replace it.
- NFR-003: Explain why patterns and connectors were recommended.
- NFR-004: Use deterministic tools and validation rules instead of relying only on LLM judgment.
- NFR-005: Allow new platforms, connectors, patterns, and knowledge sources to be added.
- NFR-006: MVP must run locally using Ollama.
- NFR-007: Estimation must be transparent and explain assumptions.
- NFR-008: Estimation must be treated as planning guidance, not a contractual commitment.

---

## 9. Knowledge Layer Architecture

The Knowledge Layer must be pluggable.

### 9.1 Purpose

The Knowledge Layer provides trusted context to the agent workflow.

It should not be limited to ChromaDB forever.

### 9.2 MVP Knowledge Sources

- Curated markdown files
- Persistent ChromaDB

### 9.3 Future Knowledge Sources

- Official Boomi documentation
- Internal standards
- SharePoint
- Confluence
- PDFs
- GitHub repositories
- Web retrieval

### 9.4 Knowledge Categories

```text
knowledge/
├── patterns/
├── connectors/
├── architecture/
├── monitoring/
├── security/
├── error_handling/
├── mapping/
├── estimation/
└── platform/
```

### 9.5 Knowledge Packet Schema

```python
class KnowledgePacket(TypedDict):
    query: str
    source_type: str
    source_name: str
    title: str
    content: str
    relevance_score: float
    trust_level: str
    freshness: str
```

### 9.6 Retrieval Ranking

Ranking should consider:

- Relevance
- Source trust
- Freshness
- Platform match
- Source system match
- Target system match
- Pattern match

---

## 10. Tool Layer

The Tool Layer provides deterministic decision support.

### 10.1 Pattern Selection Tool

Inputs:

- Integration style
- Frequency
- Volume
- Operation type

Output:

- Recommended pattern
- Reason

### 10.2 Connector Recommendation Tool

Inputs:

- Source system
- Target system
- Platform

Output:

- Recommended source connector
- Recommended target connector
- Notes

### 10.3 Risk Assessment Tool

Inputs:

- Volume
- Frequency
- System types
- Authentication
- Operation type
- Mapping complexity

Output:

- Risk level
- Risk reasons

### 10.4 Complexity Estimator

Inputs:

- Number of systems
- Number of objects/entities
- Volume
- Frequency
- Mapping complexity
- Security complexity
- Error handling needs
- Testing scope

Output:

- Complexity level
- Complexity score
- Complexity drivers

### 10.5 Development and Testing Estimation Tool

Inputs:

- Complexity score
- Number of objects/entities
- Mapping complexity
- Operation type
- Integration style
- Testing scope
- Risk level

Output:

- Development estimate range
- Testing estimate range
- Total estimate range
- Estimate assumptions

---

## 11. Estimation Model

The MVP estimation is a planning estimate, not a contract.

### 11.1 Estimate Categories

The system should estimate:

| Area | Description |
|---|---|
| Requirements Clarification | Time to finalize details |
| Boomi Process Development | Process build and connector setup |
| Mapping and Validation | Profiles, maps, validations |
| Error Handling and Logging | Try/Catch, exception routing, logging |
| Unit Testing | Developer testing |
| SIT Support | Integration testing support |
| UAT Support | User validation support |

### 11.2 Example Output

```markdown
## Development and Testing Estimate

| Area | Estimate |
|---|---:|
| Requirements clarification | 0.5–1 day |
| Boomi process development | 2–4 days |
| Mapping and validation | 1–2 days |
| Error handling and logging | 1–2 days |
| Unit testing | 1–2 days |
| SIT support | 2–3 days |
| UAT support | 1–2 days |

**Total Estimate:** 8.5–16 business days  
**Complexity:** Medium

**Assumptions:**
- One source and one target system
- Moderate mapping complexity
- Standard connector availability
- No custom SAP enhancement required
- Standard SIT and UAT support included
```

### 11.3 Estimation Rules

Example rules:

- Low complexity: 3–7 business days
- Medium complexity: 8–16 business days
- High complexity: 17–30 business days
- Very high complexity: requires manual estimation

The system must explain why it selected an estimate.

---

## 12. Agent Workflow

```text
START
↓
Requirements Agent
↓
Clarification Agent
↓
Planner Agent
↓
Retriever Agent
↓
Pattern Selection Agent
↓
Connector Recommendation Agent
↓
Risk Assessment Agent
↓
Complexity Estimation Agent
↓
Development Estimation Agent
↓
Architecture Agent
↓
Architecture Review Agent
↓
Final Report Agent
↓
Human Approval
↓
END
```

### Agent Responsibilities

- Requirements Agent: Normalize inputs and create requirement summary.
- Clarification Agent: Detect missing critical inputs and ask questions.
- Planner Agent: Create implementation plan.
- Retriever Agent: Retrieve relevant knowledge packets.
- Pattern Selection Agent: Recommend pattern using deterministic tool.
- Connector Recommendation Agent: Recommend connectors using deterministic tool.
- Risk Assessment Agent: Identify delivery and architecture risks.
- Complexity Estimation Agent: Determine solution complexity.
- Development Estimation Agent: Estimate development and testing effort.
- Architecture Agent: Generate architecture report draft.
- Architecture Review Agent: Validate report against rules.
- Final Report Agent: Format final export-ready report.
- Human Approval: Approve, reject, or request changes.

---

## 13. Report Schema

The final report must include:

1. Executive Summary
2. Requirement Summary
3. Recommended Integration Pattern
4. Source System
5. Target System
6. Boomi Process Flow
7. Connector Strategy
8. Mapping Strategy
9. Error Handling Strategy
10. Retry Strategy
11. Monitoring and Logging
12. Security Considerations
13. Risks and Assumptions
14. Scalability Considerations
15. Development and Testing Estimate
16. Implementation Roadmap
17. Final Recommendation

---

## 14. Validation Rules

The review agent must verify:

- Source system is clearly identified.
- Target system is clearly identified.
- Integration direction is not reversed.
- Recommended pattern is present.
- Connector strategy is present.
- Mapping strategy is present.
- Error handling is present.
- Retry strategy is present.
- Monitoring and logging are present.
- Security considerations are present.
- Risks and assumptions are present.
- Development and testing estimate is present.
- Report is implementation-oriented.

---

## 15. Platform Abstraction

Although MVP is Boomi-focused, platform-specific logic must be isolated.

### Platform Config Example

```yaml
platform: boomi
display_name: Boomi
concepts:
  process_flow: Boomi Process Flow
  connector: Boomi Connector
  runtime: Atom / Molecule / Cloud
  monitoring: AtomSphere Process Reporting
```

To support another platform later, replace:

- platform config
- connector catalog
- report terminology
- knowledge files
- validation rules
- estimation rules if needed

Core workflow should remain unchanged.

---

## 16. Suggested Repository Structure

```text
boomi-ai-solution-architect/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── workflow/
│   ├── agents/
│   ├── tools/
│   ├── knowledge/
│   ├── prompts/
│   ├── schemas/
│   ├── export/
│   └── ui/
│
├── knowledge/
│   ├── patterns/
│   ├── connectors/
│   ├── architecture/
│   ├── monitoring/
│   ├── security/
│   ├── error_handling/
│   └── estimation/
│
├── chromadb_data/
├── docs/
├── diagrams/
├── sample_outputs/
└── tests/
```

---

## 17. MVP Delivery Plan

### Phase 1 — Project Setup

- Create repository
- Create folder structure
- Add Streamlit skeleton
- Add requirements.txt

### Phase 2 — Knowledge Layer

- Create curated knowledge files
- Create ingest script
- Create persistent ChromaDB
- Test retrieval

### Phase 3 — Tool Layer

- Build pattern selector
- Build connector recommender
- Build risk estimator
- Build complexity estimator
- Build development/testing estimator

### Phase 4 — LangGraph Workflow

- Build requirements agent
- Build planner
- Build retriever
- Build pattern agent
- Build connector agent
- Build risk agent
- Build estimation agent
- Build architecture agent
- Build review agent
- Build final report agent

### Phase 5 — UI Integration

- Connect Streamlit to workflow
- Add progress/status display
- Add report rendering

### Phase 6 — Export

- Markdown export
- PDF export later

---

## 18. Success Criteria

The MVP is successful when:

- User can enter structured metadata and business requirement.
- System retrieves relevant knowledge.
- System selects pattern and connectors.
- System estimates risk and complexity.
- System estimates development and testing effort.
- System generates a complete architecture report.
- System validates the report.
- User can approve or request changes.
- User can export Markdown report.

---

## 19. Design Principle

The LLM is not the source of truth.

```text
Knowledge Layer = trusted context
Tool Layer = deterministic decision support
LLM = reasoning and writing engine
Review Layer = validation
Human = final governance
```
