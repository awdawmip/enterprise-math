# Enterprise Math Cloudflare Supervisor

Status: **V1 live / deterministic control infrastructure / no mathematical authority**

This service externalizes the narrow live-control duties that a one-shot ChatGPT
conversation cannot reliably perform for itself:

- exact `(task_id, claim_id[, cohort_id, lane_id])` owner-scope state;
- `TURN_EXECUTION_LEASE` acquisition and material-progress refresh;
- Durable Object alarms that detect silent/stale turns out-of-band;
- recovery state that preserves the existing CLAIM instead of issuing a second CLAIM;
- one-shot Researcher durable-handoff verification;
- read-only GitHub main-protection/ruleset inspection;
- stateless Streamable HTTP MCP at `/em/mcp`.

It deliberately has **no LLM, Driver, theorem, Working Truth, Foundation, or
promotion authority**.

## Production route

The Worker is mounted only on:

```text
https://181131.xyz/em/*
```

Public endpoints:

```text
https://181131.xyz/em/health
https://181131.xyz/em/mcp
https://181131.xyz/em/api/v1/github/enforcement
https://181131.xyz/em/webhook/github
```

`workers.dev` and Cloudflare preview URLs are explicitly disabled. The Wrangler
contract forbids the broad route `181131.xyz/*`, so this deployment does not own
or modify unrelated paths or other Workers outside `/em/*`.

## Cloudflare shape

- Worker: HTTP/MCP/security boundary.
- `OwnerScope`: SQLite-backed Durable Object, one logical object per exact owner scope.
- Alarm: independent watchdog clock.
- `RecoveryWorkflow`: retryable durable recovery verification.
- GitHub/Google Drive: durable external evidence, never conversational memory.
- Cloudflare Access: user-facing OAuth boundary for the exact `/em/mcp` path.

## Authentication boundary

Production MCP authentication is Cloudflare Access Managed OAuth on the exact
self-hosted Access application `181131.xyz/em/mcp`.

- end-user policy: the pre-existing exact single-email allow policy;
- identity provider: the existing one-time-pin IdP;
- dynamic client registration: enabled;
- redirect allowlist: only ChatGPT connector OAuth callback paths;
- OAuth access token lifetime: 15 minutes;
- OAuth grant / refresh session: 336 hours (14 days);
- localhost and loopback wildcard clients: disabled.

The Worker independently validates Cloudflare's `Cf-Access-Jwt-Assertion` using
RS256, the account Access JWKS, exact issuer, and exact application audience.
Human tokens require a non-empty subject. Cloudflare service-token application
JWTs use the documented empty subject plus non-empty `common_name` machine
principal and are accepted only in that exact shape.

`SUPERVISOR_API_TOKEN` remains an operator/bootstrap credential for `/em/api/*`.
Once Access is configured, it is **not** an MCP bypass: `/em/mcp` accepts the
Access assertion only.

CI does not retain an Access service token. Each normal Supervisor deployment:

1. creates a one-hour Access service token;
2. binds the dedicated reusable CI service-auth policy to that exact token;
3. performs live MCP/lifecycle/handoff smoke tests;
4. deletes the temporary service token.

The ordinary MCP surface deliberately excludes repository-admin mutation.

## Durable handoff allowlists

GitHub handoffs are restricted to the configured repository allowlist, currently:

```text
awdawmip/enterprise-math
```

Google Drive handoffs are restricted to descendants of the dedicated root:

```text
EnterpriseMath-Handoffs
folder id: 1IJ8iAXY5laK1lj-Y4NGWKEOdLofieHLa
```

The Drive root itself is not a handoff artifact, and Drive shortcuts are rejected
to prevent an in-folder shortcut from escaping the allowlist.

Preferred long-lived external read identities are:

- repository-scoped GitHub App: Contents read + Administration read;
- Google service account: `drive.metadata.readonly`, shared only onto the handoff root.

Compatibility PAT/bearer adapters exist only as migration fallbacks.

## Required deployment secrets

```text
CLOUDFLARE_API_TOKEN
CLOUDFLARE_ACCOUNT_ID
SUPERVISOR_API_TOKEN
```

Phase-2 external-read identities, when provisioned:

```text
GITHUB_APP_ID
GITHUB_APP_INSTALLATION_ID
GITHUB_APP_PRIVATE_KEY

GOOGLE_SERVICE_ACCOUNT_EMAIL
GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY
```

Secret values are never committed or returned through MCP tools.

## Local validation

```bash
npm install
npm run check
```

`npm run check` runs a static control contract and a Wrangler dry-run build.

## Deploy

Production deployment is performed by `.github/workflows/cloudflare-supervisor.yml`
using the `cloudflare-supervisor` GitHub Environment. Deployments are serialized,
pin their exact Git SHA into `/em/health`, and live smoke waits until that exact
SHA is visible before validating the production Worker.

## Core invariants

```text
OWNER_LEASE != TURN_EXECUTION_LEASE != SESSION_LIVENESS
TURN_STALE != CLAIM_RELEASE
TURN_STALE -> PRESERVE CLAIM -> RECOVERY_READY
MATERIAL_PROGRESS_ONLY -> REFRESH TURN LEASE
RESEARCHER_ID = PROVENANCE_IDENTITY != ADDRESSABLE_MAILBOX
FUTURE_CONTINUITY + ONE_SHOT_RESEARCHER -> DURABLE_HANDOFF_REQUIRED
HANDOFF_REQUIRED + NOT_VERIFIED -> HANDOFF_INCOMPLETE
MCP_CAPABILITY != INFRASTRUCTURE_CREDENTIAL
SUPERVISOR_ROUTE = 181131.xyz/em/*
SUPERVISOR_ROUTE != 181131.xyz/*
MCP_ACCESS_CONFIGURED -> NO_BOOTSTRAP_BEARER_BYPASS
```

## MCP tools in V1

Read:
- `supervisor_snapshot`
- `recovery_status`
- `handoff_verify`
- `github_enforcement_status`

State transitions:
- `turn_acquire`
- `turn_progress`
- `turn_complete`
- `turn_abandon`

No tool creates a GitHub CLAIM. No tool promotes mathematics. No admin repository
mutation is exposed in V1.

## Known host boundary

Cloudflare can independently detect a stale turn and revoke its Supervisor-side
live execution state. It cannot physically terminate an already-running ChatGPT
UI/model turn unless the host later exposes an external cancellation API.
