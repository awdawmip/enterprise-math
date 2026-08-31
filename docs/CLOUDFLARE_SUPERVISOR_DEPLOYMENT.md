# Enterprise Math Cloudflare Supervisor Deployment

Status: `CONTROL_PLANE_INFRASTRUCTURE_CANDIDATE / NO_NEW_MATHEMATICS`

Source: `infrastructure/cloudflare-supervisor/`
Production route: `https://181131.xyz/em/*`

## Purpose

Move the narrow live control runtime outside one-shot Researcher/Driver chats
without introducing a resident LLM agent.

The Supervisor is deterministic infrastructure only. It owns timing, liveness,
handoff verification, recovery bookkeeping, and narrow service enforcement
checks. Enterprise Math repository state remains the source of task/result/review
authority.

## Route isolation

This deployment owns only:

```text
181131.xyz/em/*
```

It must not bind `181131.xyz/*`, change unrelated routes, replace unrelated
Workers, or expose a second `workers.dev` / preview URL entrypoint. The production
endpoints are:

```text
https://181131.xyz/em/health
https://181131.xyz/em/mcp
https://181131.xyz/em/api/v1/github/enforcement
https://181131.xyz/em/webhook/github
```

## Deployment phases

### Phase 1 — bootstrap

1. Deploy Worker + SQLite Durable Object + Recovery Workflow to `181131.xyz/em/*`.
2. Configure `SUPERVISOR_API_TOKEN`.
3. Confirm `/em/health`.
4. Confirm unauthenticated `/em/mcp` fails closed.
5. Test `/em/mcp` with an MCP Inspector or another supported MCP client.
6. Exercise `turn_acquire -> turn_progress -> turn_complete`.
7. Exercise an intentionally expired lease and verify `RECOVERY_READY`.
8. Verify one GitHub handoff locator.

### Phase 2 — service credentials

1. Add GitHub read/webhook credentials with least privilege.
2. Add a long-lived Google Drive credential flow scoped to the dedicated
   Enterprise Math handoff folder.
3. Route repository webhooks into durable-progress observations.
4. Never return external-service credentials through an MCP tool.

### Phase 3 — production authentication

Replace bootstrap bearer auth with OAuth for `/em/mcp`.
Keep admin capabilities on a separate, more privileged surface; ordinary
ChatGPT MCP access must not receive repository-admin authority.

### Phase 4 — GitHub physical enforcement

Once an audited admin transport is available, configure main protection/rulesets
server-side. This is separate from the normal Supervisor MCP tool set.

## iOS boundary

The Supervisor does not depend on iOS custom-MCP support to keep running.
Durable Object alarms and Workflows are out-of-band. Until the iOS ChatGPT
surface can invoke the custom MCP directly, durable Supervisor outcomes can be
bridged through existing GitHub/Drive surfaces or invoked from a supported MCP
client.

## One-shot Researcher rule

If later Driver review, redispatch, or voice/oral continuation will need material
from a Researcher, the dispatch must require persistence before Researcher final:

- GitHub for repository-native artifacts;
- Google Drive for large/binary/audio/external-format material.

The Supervisor rejects a required but unverified handoff as
`HANDOFF_INCOMPLETE`.
