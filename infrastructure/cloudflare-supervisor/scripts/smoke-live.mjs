import { Client, StreamableHTTPClientTransport } from "@modelcontextprotocol/client";

const baseUrl = process.env.SUPERVISOR_BASE_URL || "https://181131.xyz/em";
const token = process.env.SUPERVISOR_API_TOKEN;
const ref = process.env.SUPERVISOR_SMOKE_REF || "infrastructure/cloudflare-supervisor-v1-20260830";
const driveSmokeFileId = process.env.SUPERVISOR_DRIVE_SMOKE_FILE_ID;
const driveRootId = "1IJ8iAXY5laK1lj-Y4NGWKEOdLofieHLa";
const accessServiceClientId = process.env.ACCESS_SERVICE_CLIENT_ID;
const accessServiceClientSecret = process.env.ACCESS_SERVICE_CLIENT_SECRET;
const durableObjectResetMarker = "Durable Object reset because its code was updated.";

if (!token) throw new Error("SUPERVISOR_API_TOKEN is required");

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function toolText(result) {
  return result?.content?.find?.((item) => item?.type === "text")?.text;
}

async function callToolJson(client, request) {
  for (let attempt = 1; attempt <= 8; attempt += 1) {
    try {
      const result = await client.callTool(request);
      const text = toolText(result);
      if (text?.includes(durableObjectResetMarker)) {
        if (attempt === 8) {
          throw new Error(`Durable Object reset did not settle after ${attempt} attempts`);
        }
        console.log(`RETRY_DURABLE_OBJECT_RESET tool=${request.name} attempt=${attempt}`);
        await sleep(1000);
        continue;
      }
      if (!text) throw new Error(`tool result missing text: ${JSON.stringify(result)}`);
      return JSON.parse(text);
    } catch (error) {
      const message = String(error?.message ?? error);
      if (message.includes(durableObjectResetMarker) && attempt < 8) {
        console.log(`RETRY_DURABLE_OBJECT_RESET tool=${request.name} attempt=${attempt}`);
        await sleep(1000);
        continue;
      }
      throw error;
    }
  }
  throw new Error(`unreachable bounded tool retry exhausted for ${request.name}`);
}

let healthBody = null;
for (let attempt = 1; attempt <= 30; attempt += 1) {
  const health = await fetch(`${baseUrl}/health`, {
    headers: { "cache-control": "no-store" },
  });
  assert(health.ok, `health failed status=${health.status}`);
  healthBody = await health.json();
  assert(healthBody?.ok === true, "health payload not ok");
  assert(healthBody?.base_path === "/em", "health base_path drift");
  if (!/^[0-9a-f]{40}$/i.test(ref) || healthBody?.deployment_sha === ref) break;
  console.log(
    `WAITING_FOR_DEPLOYED_SHA attempt=${attempt} observed=${healthBody?.deployment_sha ?? "null"} expected=${ref}`,
  );
  await sleep(2000);
}
if (/^[0-9a-f]{40}$/i.test(ref)) {
  assert(
    healthBody?.deployment_sha === ref,
    `live Worker SHA mismatch observed=${healthBody?.deployment_sha ?? "null"} expected=${ref}`,
  );
}

const authMode = healthBody?.mcp_auth_mode;
assert(
  ["BOOTSTRAP_BEARER", "CLOUDFLARE_ACCESS"].includes(authMode),
  `unexpected MCP auth mode ${authMode}`,
);

const unauth = await fetch(`${baseUrl}/mcp`, {
  method: "POST",
  headers: { "content-type": "application/json" },
  body: JSON.stringify({ jsonrpc: "2.0", id: 1, method: "ping" }),
  redirect: "manual",
});
assert(unauth.status === 401, `unauthenticated MCP must be 401, got ${unauth.status}`);

const authenticatedHeaders = {};
if (authMode === "CLOUDFLARE_ACCESS") {
  assert(
    accessServiceClientId && accessServiceClientSecret,
    "Access-mode live smoke requires ACCESS_SERVICE_CLIENT_ID and ACCESS_SERVICE_CLIENT_SECRET",
  );
  authenticatedHeaders["CF-Access-Client-Id"] = accessServiceClientId;
  authenticatedHeaders["CF-Access-Client-Secret"] = accessServiceClientSecret;
} else {
  authenticatedHeaders.Authorization = `Bearer ${token}`;
}

const client = new Client(
  { name: "enterprise-math-supervisor-live-smoke", version: "0.1.0" },
  { versionNegotiation: { mode: "auto" } },
);
const transport = new StreamableHTTPClientTransport(new URL(`${baseUrl}/mcp`), {
  requestInit: { headers: authenticatedHeaders },
});

await client.connect(transport);
const serverVersion = client.getServerVersion();
assert(serverVersion?.name === "enterprise-math-supervisor", `unexpected MCP server ${JSON.stringify(serverVersion)}`);

const tools = await client.listTools();
const names = new Set((tools.tools || []).map((tool) => tool.name));
for (const required of [
  "supervisor_snapshot",
  "turn_acquire",
  "turn_progress",
  "turn_complete",
  "turn_abandon",
  "recovery_status",
  "handoff_verify",
  "github_enforcement_status",
]) {
  assert(names.has(required), `missing MCP tool ${required}`);
}

const suffix = `${process.env.GITHUB_RUN_ID || Date.now()}-${Math.random().toString(16).slice(2, 10)}`;
const taskId = `RS-SUPERVISOR-LIVE-SMOKE-${suffix}`;
const claimId = `CLM-SUPERVISOR-LIVE-SMOKE-${suffix}`;
const turnId = `TURN-SUPERVISOR-LIVE-SMOKE-${suffix}`;
const scope = { task_id: taskId, claim_id: claimId };

const acquired = await callToolJson(client, {
  name: "turn_acquire",
  arguments: {
    ...scope,
    turn_id: turnId,
    researcher_id: `EM-SMOKE-${suffix}`,
    lease_ms: 30000,
    current_action: "LIVE_DEPLOYMENT_SMOKE",
    durable_frontier: "SMOKE_ACQUIRED",
    handoff_required: true,
  },
});
assert(acquired.status === "RUNNING", `turn_acquire failed: ${JSON.stringify(acquired)}`);

const progressed = await callToolJson(client, {
  name: "turn_progress",
  arguments: {
    ...scope,
    turn_id: turnId,
    lease_ms: 30000,
    current_action: "LIVE_DEPLOYMENT_SMOKE_PROGRESS",
    durable_frontier: "SMOKE_PROGRESS_VERIFIED",
  },
});
assert(progressed.status === "RUNNING", `turn_progress failed: ${JSON.stringify(progressed)}`);
assert(progressed.durable_frontier === "SMOKE_PROGRESS_VERIFIED", "progress frontier not persisted");

const locator = {
  surface: "GITHUB",
  repository: "awdawmip/enterprise-math",
  path: "infrastructure/cloudflare-supervisor/README.md",
  ref,
};
const verified = await callToolJson(client, {
  name: "handoff_verify",
  arguments: { locator },
});
assert(verified.verified === true, `GitHub handoff verification failed: ${JSON.stringify(verified)}`);

const forbiddenRepo = await callToolJson(client, {
  name: "handoff_verify",
  arguments: {
    locator: {
      surface: "GITHUB",
      repository: "openai/openai",
      path: "README.md",
      ref: "main",
    },
  },
});
assert(
  forbiddenRepo.verified === false && forbiddenRepo.reason === "github_repository_not_allowlisted",
  `GitHub handoff repo allowlist failed open: ${JSON.stringify(forbiddenRepo)}`,
);

const driveRootAsArtifact = await callToolJson(client, {
  name: "handoff_verify",
  arguments: { locator: { surface: "GOOGLE_DRIVE", file_id: driveRootId } },
});
assert(
  driveRootAsArtifact.verified === false && driveRootAsArtifact.reason === "drive_handoff_root_itself_is_not_an_artifact",
  `Drive root must not be accepted as an artifact: ${JSON.stringify(driveRootAsArtifact)}`,
);

let driveSmoke = { verified: false, reason: "drive_smoke_file_not_configured" };
if (driveSmokeFileId) {
  driveSmoke = await callToolJson(client, {
    name: "handoff_verify",
    arguments: {
      locator: {
        surface: "GOOGLE_DRIVE",
        file_id: driveSmokeFileId,
        expected_name: "SUPERVISOR-HANDOFF-SMOKE-DO-NOT-EDIT",
      },
    },
  });
  if (driveSmoke.reason !== "google_drive_read_identity_not_configured") {
    assert(driveSmoke.verified === true, `Drive handoff fixture failed: ${JSON.stringify(driveSmoke)}`);
    assert(driveSmoke.handoff_root_id === driveRootId, "Drive handoff root identity drift");
  }
}

const completed = await callToolJson(client, {
  name: "turn_complete",
  arguments: {
    ...scope,
    turn_id: turnId,
    durable_frontier: "SMOKE_COMPLETE",
    handoff: {
      required: true,
      locator,
      inventory: ["README.md"],
      durable_frontier: "SMOKE_COMPLETE",
      next_action: "NONE",
    },
  },
});
assert(completed.status === "COMPLETED", `turn_complete failed: ${JSON.stringify(completed)}`);
assert(completed.handoff?.verified === true, "required handoff was not verified");

const enforcement = await callToolJson(client, {
  name: "github_enforcement_status",
  arguments: {},
});
assert(typeof enforcement.verified === "boolean", `GitHub enforcement tool returned malformed state: ${JSON.stringify(enforcement)}`);

await client.close();

console.log(JSON.stringify({
  status: "SUPERVISOR_LIVE_SMOKE_PASS",
  base_url: baseUrl,
  deployment_sha: healthBody?.deployment_sha,
  mcp_auth_mode: authMode,
  protocol_era: client.getProtocolEra?.(),
  tool_count: names.size,
  turn_status: completed.status,
  handoff_verified: completed.handoff?.verified === true,
  handoff_transport: verified.verification_transport,
  github_repo_allowlist_fail_closed: forbiddenRepo.reason === "github_repository_not_allowlisted",
  drive_root_fail_closed: driveRootAsArtifact.reason === "drive_handoff_root_itself_is_not_an_artifact",
  drive_handoff_verified: driveSmoke.verified === true,
  drive_handoff_reason: driveSmoke.reason,
  github_enforcement_verified: enforcement.verified === true,
  github_enforcement_identity_mode: enforcement.identity_mode,
  github_enforcement_branch_status: enforcement.branch_status,
  github_enforcement_rulesets_status: enforcement.rulesets_status,
}, null, 2));
