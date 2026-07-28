# Web, API and integration hardening

## Boundaries

Validate all server input. Bound length, count, range, file size, date span and workload.

Use safe output encoding. Avoid unsanitised HTML and active file content.

## Browser

Use HTTPS, HSTS, CSP, anti-framing, no-sniff, restrictive referrer and permissions policies. Keep CORS and Server Action origins minimal.

## Abuse

Use targeted rate limits by IP, actor, tenant, principal and operation. Protect auth, invitations, exports, AI, token exchange and expensive work.

## Outbound requests

Centralise HTTP clients. Allowlist destinations. Block loopback, private, link-local and metadata networks where input can influence destinations. Restrict redirects and protocols.

## CSRF and replay

Use same-origin and CSRF protections. Apply nonces, expiry and idempotency to replay-sensitive operations.
