# Privacy Baseline

Version: 0.1
Last Updated: {{DATE}}

> This document is a practical privacy baseline for MVP teams. It is not legal advice.

## Data Inventory

| Data Category | Purpose | Required? | Storage Location | Shared With | Retention | Deletion Method |
|---------------|---------|-----------|------------------|-------------|-----------|-----------------|
| Account email | | | | | | |
| Profile name | | | | | | |
| App content/uploads | | | | | | |
| Payment metadata (non-card) | | | | | | |
| Logs/telemetry metadata | | | | | | |

## Legal/Jurisdiction Snapshot

- Target users: <!-- EU/UK/US/CA/other -->
- Regulated context: <!-- none / health / finance / education / other -->
- Applicable baseline laws (as relevant): GDPR/UK GDPR, CCPA/CPRA, ePrivacy/cookie rules, COPPA.

## Collection Principles

- Collect the minimum data needed for the feature.
- Do not collect sensitive categories unless there is a clear product need and additional controls.
- Do not process raw card data in app code.

## User Rights Process (MVP)

- Access/export request process: <!-- email + manual SLA -->
- Deletion request process: <!-- email + manual/automated flow -->
- Correction process: <!-- how user can correct profile data -->
- SLA target: <!-- e.g., 30 days -->

## Subprocessors

| Vendor | Purpose | Data Shared | DPA/Terms Checked | Region |
|--------|---------|-------------|-------------------|--------|
| | | | | |

## Cookies / Analytics

- Default to privacy-preserving analytics.
- If non-essential cookies are used, add consent flow where legally required.

## Security Controls Supporting Privacy

- Encryption in transit (TLS)
- Managed encryption at rest
- Access controls with least privilege
- Redaction/no-PII logging policy

## Review Cadence

- Review this file at each release with user-facing data changes.
