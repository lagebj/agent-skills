---
name: application-security-engineering
description: Designs, implements, reviews, and verifies secure application changes using threat modelling, least privilege, boundary validation, negative testing, and provider-state verification. Use when work affects authentication, authorisation, tenancy, APIs, data, databases, secrets, browser controls, integrations, dependencies, logging, operations, or security findings.
license: MIT
compatibility: Agent Skills standard; repository filesystem access is required for implementation and verification work.
metadata:
  owner: lagebj
  category: security
---

# Application Security Engineering

Use this skill to design, implement, review and verify secure application changes without relying on security theatre or unnecessary user friction.

This is a generic skill. Adapt it to the repository, framework, hosting platform, data sensitivity and threat model.

## Use this skill when

A task changes or reviews:

- authentication, sessions or identity linking;
- authorisation, roles, scopes or resource ownership;
- multitenancy or data isolation;
- server routes, actions, APIs or background jobs;
- input validation, files, exports or rich text;
- SQL, ORM, database roles, RLS or migrations;
- caches, queues, object storage or generated artifacts;
- outbound HTTP, webhooks, integrations or AI providers;
- secrets, environment variables or CI credentials;
- CSP, headers, CORS, CSRF or browser security;
- rate limiting, WAF or abuse protection;
- logging, audit, monitoring, backup or incident response;
- dependencies, build workflows or software supply chain;
- a security finding, accepted risk or architectural residue.

## Core invariants

```text
Deny by default.
Derive trust server-side.
Use least privilege.
Validate every boundary.
Minimise data and capabilities.
Layer important controls.
Test failure and abuse paths.
Preserve evidence without exposing sensitive data.
```

Security must be proportional. Prefer invisible controls for ordinary workflows. Apply visible friction to high-risk privileged operations, not routine use.

## Workflow

### 1. Load context selectively

Read only what the task requires:

- repository agent instructions;
- architecture and threat model;
- authentication and tenancy documentation;
- relevant ADRs and unresolved ARRs;
- data classification and privacy rules;
- provider and environment documentation;
- existing security tests and findings.

Load references as needed:

- `references/security-change-workflow.md`
- `references/identity-authorisation-and-tenancy.md`
- `references/web-api-and-integration-hardening.md`
- `references/data-database-and-secrets.md`
- `references/supply-chain-operations-and-provider-actions.md`

### 2. Classify the change

Identify:

- assets affected;
- actors;
- trust boundaries;
- hostile input;
- data leaving the process;
- secrets and privileges;
- external dependencies;
- expected failure modes.

### 3. Find existing owners

Search for shared owners of:

- authentication and session context;
- authorisation policy;
- validation;
- database access;
- outbound HTTP;
- audit logging;
- rate limiting;
- secret access;
- error handling.

Do not create route-specific security logic when a shared owner exists.

### 4. Implement defence in depth

Apply the smallest sufficient set of controls across relevant layers:

- edge;
- transport;
- authentication;
- authorisation;
- application command;
- repository;
- database;
- cache or artifact storage;
- audit and monitoring.

Do not duplicate the same fragile check everywhere.

### 5. Test negative paths

Add tests for unauthorised actors, wrong resource ownership, malformed and oversized input, replay, concurrency, leakage, unsafe destinations and stale authority.

### 6. Verify provider state

When a control lives outside code:

- automate only through safe existing authenticated tooling;
- otherwise create an exact provider action;
- include navigation, value, reason, verification and rollback;
- never fabricate completion;
- never record secret values.

### 7. Document durable outcomes

Update code, tests, threat model, security architecture, ADRs, ARRs and operations documentation as appropriate.

Use:

- a security finding for a vulnerability or failed control;
- an ARR for a structural architectural mismatch;
- an ADR for a decision, deferral or accepted risk.

## Prohibited shortcuts

Do not:

- treat authentication as authorisation;
- trust client-supplied ownership or roles;
- rely on hidden UI controls;
- use unsafe SQL or string concatenation;
- log secrets or sensitive payloads;
- accept arbitrary outbound URLs;
- open CORS or CSP broadly to fix integration issues;
- disable RLS, validation or checks to make tests pass;
- use permanent broad machine credentials;
- claim provider configuration without evidence;
- introduce routine CAPTCHA, user IP restrictions or VPN requirements without a specific justified threat.

## Verification checklist

Before completion:

- trust boundaries and actors are explicit;
- authorisation is deny-by-default;
- resource and tenant ownership are verified;
- input is bounded server-side;
- output and logs are minimised;
- SQL and external requests are safe;
- secrets and environments are separated;
- negative tests pass;
- dependency and static checks pass;
- provider actions are verified or recorded;
- threat model and architectural records are current;
- user experience is not degraded without justification.

## Stop or escalate

Stop and report when:

- intended authorisation cannot be determined;
- two active security decisions conflict;
- provider state is unavailable and material;
- a secret is exposed or suspected compromised;
- a fix requires accepting material residual risk without authority;
- safe verification cannot be performed.

Do not invent assurance.

## Common rationalizations

| Rationalization | Required response |
|---|---|
| "The user is authenticated." | Authentication does not prove authority for this action or resource. |
| "The UI hides the action." | Enforce the policy server-side and test the denied path. |
| "The ORM makes the query safe." | Verify parameterisation, tenant scope, privileges, constraints, and unsafe escape hatches. |
| "The provider setting is probably enabled." | Verify it or record an exact provider action. Do not invent assurance. |
| "Rate limiting will solve abuse." | Apply operation-specific controls and preserve underlying authorisation and validation. |
| "Security can be reviewed after the feature works." | Security boundaries are part of the feature design and its tests. |

## Red flags

- Client-supplied roles, ownership, tenant IDs, or redirect destinations are trusted.
- A broad CORS, CSP, network, or permission exception is introduced to make integration easier.
- Negative tests are absent for a sensitive operation.
- Secrets, full payloads, access tokens, or personal data appear in logs or documentation.
- Provider configuration is claimed without evidence.
- A runtime identity has migration, administrative, or cross-tenant privileges without a documented need.
