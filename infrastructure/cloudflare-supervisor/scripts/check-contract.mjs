import fs from "node:fs";

const wrangler = fs.readFileSync(new URL("../wrangler.jsonc", import.meta.url), "utf8");
const index = fs.readFileSync(new URL("../src/index.ts", import.meta.url), "utf8");
const owner = fs.readFileSync(new URL("../src/owner-scope.ts", import.meta.url), "utf8");
const external = fs.readFileSync(new URL("../src/external.ts", import.meta.url), "utf8");
const externalAuth = fs.readFileSync(new URL("../src/external-auth.ts", import.meta.url), "utf8");
const security = fs.readFileSync(new URL("../src/security.ts", import.meta.url), "utf8");
const smokeLive = fs.readFileSync(new URL("./smoke-live.mjs", import.meta.url), "utf8");
const deployWorkflow = fs.readFileSync(
  new URL("../../../.github/workflows/cloudflare-supervisor.yml", import.meta.url),
  "utf8",
);
const quarantineWorkflow = fs.readFileSync(
  new URL("../../../.github/workflows/cloudflare-supervisor-ci-token-quarantine.yml", import.meta.url),
  "utf8",
);
const provisionWorkflow = fs.readFileSync(
  new URL("../../../.github/workflows/cloudflare-supervisor-access-provision.yml", import.meta.url),
  "utf8",
);

const required = [
  [wrangler, '"storage": "sqlite"', "SQLite-backed Durable Object"],
  [wrangler, '"class_name": "OwnerScope"', "OwnerScope binding"],
  [wrangler, '"class_name": "RecoveryWorkflow"', "Recovery Workflow binding"],
  [wrangler, '"workers_dev": false', "workers.dev disabled"],
  [wrangler, '"preview_urls": false', "preview URLs disabled"],
  [wrangler, '"pattern": "181131.xyz/em/*"', "exclusive /em route"],
  [wrangler, '"zone_name": "181131.xyz"', "181131.xyz zone binding"],
  [wrangler, '"GITHUB_HANDOFF_REPOSITORIES": "awdawmip/enterprise-math"', "GitHub handoff repository allowlist"],
  [wrangler, '"GOOGLE_DRIVE_HANDOFF_ROOT_ID": "1IJ8iAXY5laK1lj-Y4NGWKEOdLofieHLa"', "Drive handoff root allowlist"],
  [index, 'const BASE_PATH = "/em"', "/em base path"],
  [index, "requireMcpAuth(request, env)", "MCP-specific auth gate"],
  [index, "requireBearer(request, env)", "operator API bearer gate"],
  [index, '"turn_acquire"', "turn_acquire MCP tool"],
  [index, '"turn_progress"', "turn_progress MCP tool"],
  [index, '"turn_complete"', "turn_complete MCP tool"],
  [index, '"handoff_verify"', "handoff_verify MCP tool"],
  [index, '"github_enforcement_status"', "read-only GitHub enforcement tool"],
  [owner, "TURN_EXECUTION_LEASE_EXPIRED_WITHOUT_VERIFIED_PROGRESS", "stale-turn invariant"],
  [owner, "REQUIRED_DURABLE_HANDOFF_NOT_VERIFIED", "one-shot handoff gate"],
  [owner, "RECOVERY_WORKFLOW.create", "out-of-band recovery workflow"],
  [external, "github_repository_not_allowlisted", "GitHub repo fail-closed gate"],
  [external, "drive_file_not_under_handoff_root", "Drive ancestry fail-closed gate"],
  [external, "drive_shortcut_not_accepted_for_handoff", "Drive shortcut escape prevention"],
  [externalAuth, "drive.metadata.readonly", "Drive metadata-only service account scope"],
  [externalAuth, "/app/installations/", "repository-scoped GitHub App installation identity"],
  [security, 'request.headers.get("cf-access-jwt-assertion")', "Cloudflare Access assertion validation"],
  [security, 'header.alg !== "RS256"', "Access JWT algorithm pin"],
  [security, "Access JWT audience mismatch", "Access application audience binding"],
  [security, 'payload.sub === ""', "documented Access service-token empty subject"],
  [security, "payload.common_name", "Access service-token machine principal"],
  [security, 'return team ? "CLOUDFLARE_ACCESS" : "BOOTSTRAP_BEARER"', "explicit MCP auth mode transition"],
  [smokeLive, "Durable Object reset because its code was updated.", "bounded DO hot-update retry marker"],
  [smokeLive, "attempt <= 8", "bounded DO hot-update retry count"],
  [deployWorkflow, "ACCESS_EPHEMERAL_CI_IDENTITY=READY", "ephemeral CI identity creation"],
  [deployWorkflow, "enabled:false", "CI identity fail-closed revocation"],
  [deployWorkflow, ".result.enabled == false", "CI identity boolean-safe revocation verification"],
  [deployWorkflow, "ACCESS_EPHEMERAL_CI_IDENTITY=DISABLED", "revocation success marker"],
  [deployWorkflow, "ACCESS_STALE_CI_TOKEN=DELETED", "prior CI token pruning"],
  [quarantineWorkflow, ".result.enabled == false", "quarantine boolean-safe revocation verification"],
  [quarantineWorkflow, "SUPERVISOR_CI_TOKEN_QUARANTINE=PASS", "quarantine success marker"],
  [provisionWorkflow, "on:\n  workflow_dispatch:", "manual-only Access provisioning"],
  [provisionWorkflow, 'type:"self_hosted"', "path-scoped self-hosted Access application"],
  [provisionWorkflow, 'access_token_lifetime:"15m"', "short Access token lifetime"],
  [provisionWorkflow, 'session_duration:"336h"', "bounded OAuth grant session"],
  [provisionWorkflow, '"https://chatgpt.com/connector/oauth/*"', "ChatGPT OAuth callback allowlist"],
];

for (const [text, marker, label] of required) {
  if (!text.includes(marker)) throw new Error(`missing ${label}: ${marker}`);
}

for (const forbidden of [
  "GITHUB_ADMIN_TOKEN",
  "force-push",
  "delete_repository",
  '"pattern": "181131.xyz/*"',
  '"workers_dev": true',
  "https://www.googleapis.com/auth/drive ",
  "resourceMatchOriginOnly",
  "allow_any_on_localhost:true",
  "allow_any_on_loopback:true",
]) {
  if (
    index.includes(forbidden) ||
    owner.includes(forbidden) ||
    wrangler.includes(forbidden) ||
    external.includes(forbidden) ||
    externalAuth.includes(forbidden) ||
    security.includes(forbidden) ||
    smokeLive.includes(forbidden) ||
    deployWorkflow.includes(forbidden) ||
    quarantineWorkflow.includes(forbidden) ||
    provisionWorkflow.includes(forbidden)
  ) {
    throw new Error(`forbidden privileged/broad surface in Supervisor: ${forbidden}`);
  }
}

console.log(`SUPERVISOR_CONTRACT_CHECK_PASS checks=${required.length}`);
