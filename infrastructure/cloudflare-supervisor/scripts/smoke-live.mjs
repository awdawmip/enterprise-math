import fs from "node:fs";
import { Client, StreamableHTTPClientTransport } from "@modelcontextprotocol/client";

const baseUrl = process.env.SUPERVISOR_BASE_URL || "https://181131.xyz/em";
const token = process.env.SUPERVISOR_API_TOKEN;
const requestedRef = process.env.SUPERVISOR_SMOKE_REF?.trim() || null;
const reportPath = process.env.SUPERVISOR_CANARY_REPORT?.trim() || null;
const githubToken = process.env.GITHUB_TOKEN?.trim() || null;
const driveSmokeFileId = process.env.SUPERVISOR_DRIVE_SMOKE_FILE_ID;
const driveRootId = "1IJ8iAXY5laK1lj-Y4NGWKEOdLofieHLa";
const accessServiceClientId = process.env.ACCESS_SERVICE_CLIENT_ID;
const accessServiceClientSecret = process.env.ACCESS_SERVICE_CLIENT_SECRET;
const durableObjectResetMarker = "Durable Object reset because its code was updated.";
const requiredEnforcementChecks = (
  process.env.REQUIRED_ENFORCEMENT_CHECKS ||
  "quality-gate,reference-integrity-gate,bilingual-sync-gate,lean-gate"
)
  .split(",")
  .map((value) => value.trim())
  .filter(Boolean)
  .sort();

if (!token) throw new Error("SUPERVISOR_API_TOKEN is required");
if (requestedRef && !/^[0-9a-f]{40}$/i.test(requestedRef)) {
  throw new Error("SUPERVISOR_SMOKE_REF must be an immutable 40-character commit SHA");
}

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

async function githubCheckSnapshot(repository, ref) {
  const response = await fetch(
    `https://api.github.com/repos/${repository}/commits/${ref}/check-runs?per_page=100`,
    {
      headers: {
        Accept: "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "enterprise-math-supervisor-canary",
        ...(githubToken ? { Authorization: `Bearer ${githubToken}` } : {}),
      },
    },
  );
  assert(response.ok, `GitHub check snapshot failed status=${response.status}`);
  const body = await response.json();
  const runs = Array.isArray(body.check_runs) ? body.check_runs : [];
  const counts = {};
  for (const run of runs) {
    const key = run.status === "completed"
      ? `completed:${run.conclusion || "unknown"}`
      : run.status || "unknown";
    counts[key] = (counts[key] || 0) + 1;
  }
  return {
    observed_after_turn_release: true,
    blocks_turn: false,
    total_count: Number(body.total_count || runs.length),
    counts,
    checks: runs.map((run) => ({
      name: run.name,
      status: run.status,
      conclusion: run.conclusion,
    })),
  };
}

function enforcementContexts(enforcement) {
  const raw = enforcement?.required_status_checks;
  const contexts = new Set();
  if (Array.isArray(raw)) {
    for (const item of raw) {
      if (typeof item === "string") contexts.add(item);
      if (item && typeof item.context === "string") contexts.add(item.context);
    }
  } else if (raw && typeof raw === "object") {
    for (const item of raw.contexts || []) {
      if (typeof item === "string") contexts.add(item);
    }
    for (const item of raw.checks || []) {
      if (item && typeof item.context === "string") contexts.add(item.context);
    }
  }
  return [...contexts].sort();
}

function enforcementMatches(enforcement) {
  return (
    enforcement?.verified === true &&
    enforcement?.main_protected === true &&
    JSON.stringify(enforcementContexts(enforcement)) ===
      JSON.stringify(requiredEnforcementChecks)
  );
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

  const observed = healthBody?.deployment_sha;
  if (requestedRef ? observed === requestedRef : /^[0-9a-f]{40}$/i.test(observed ?? "")) {
    break;
  }
  console.log(
    `WAITING_FOR_DEPLOYED_SHA attempt=${attempt} observed=${observed ?? "null"} expected=${requestedRef ?? "immutable deployed SHA"}`,
  );
  await sleep(2000);
}

const ref = requestedRef || healthBody?.deployment_sha;
assert(
  /^[0-9a-f]{40}$/i.test(ref ?? ""),
  `live Worker deployment SHA is not immutable: ${ref ?? "null"}`,
);
if (requestedRef) {
  assert(
    healthBody?.deployment_sha === requestedRef,
    `live Worker SHA mismatch observed=${healthBody?.deployment_sha ?? "null"} expected=${requestedRef}`,
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
  { name: "enterprise-math-supervisor-live-canary", version: "0.2.0" },
  { versionNegotiation: { mode: "auto" } },
);
const transport = new StreamableHTTPClientTransport(new URL(`${baseUrl}/mcp`), {
  requestInit: { headers: authenticatedHeaders },
});

await client.connect(transport);
const serverVersion = client.getServerVersion();
assert(
  serverVersion?.name === "enterprise-math-supervisor",
  `unexpected MCP server ${JSON.stringify(serverVersion)}`,
);

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
const taskId = `RS-SUPERVISOR-LIVE-CANARY-${suffix}`;
const claimId = `CLM-SUPERVISOR-LIVE-CANARY-${suffix}`;
const turnId = `TURN-SUPERVISOR-LIVE-CANARY-${suffix}`;
const scope = { task_id: taskId, claim_id: claimId };

const acquired = await callToolJson(client, {
  name: "turn_acquire",
  arguments: {
    ...scope,
    turn_id: turnId,
    researcher_id: `EM-CANARY-${suffix}`,
    lease_ms: 30000,
    current_action: "PRE_TOOL_CHECKPOINT",
    durable_frontier: "CANARY_PRE_TOOL",
    handoff_required: true,
  },
});
assert(acquired.status === "RUNNING", `turn_acquire failed: ${JSON.stringify(acquired)}`);
assert(acquired.current_action === "PRE_TOOL_CHECKPOINT", "PRE_TOOL checkpoint not persisted");
const generation = acquired.generation;
assert(Number.isInteger(generation) && generation > 0, "turn generation missing");

const preToolSnapshot = await callToolJson(client, {
  name: "supervisor_snapshot",
  arguments: scope,
});
assert(preToolSnapshot?.generation === generation, "generation drift before tool call");
assert(preToolSnapshot?.turn_id === turnId, "PRE_TOOL snapshot lost exact turn ownership");

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
assert(
  verified.verified === true,
  `GitHub handoff verification failed: ${JSON.stringify(verified)}`,
);

const postToolSnapshot = await callToolJson(client, {
  name: "supervisor_snapshot",
  arguments: scope,
});
assert(postToolSnapshot?.generation === generation, "generation changed across tool call");
assert(postToolSnapshot?.status === "RUNNING", "tool call changed turn state unexpectedly");

const progressed = await callToolJson(client, {
  name: "turn_progress",
  arguments: {
    ...scope,
    turn_id: turnId,
    lease_ms: 30000,
    current_action: "POST_TOOL_PROGRESS",
    durable_frontier: "CANARY_TOOL_VERIFIED",
  },
});
assert(progressed.status === "RUNNING", `turn_progress failed: ${JSON.stringify(progressed)}`);
assert(progressed.generation === generation, "progress changed owner generation");
assert(progressed.durable_frontier === "CANARY_TOOL_VERIFIED", "progress frontier not persisted");

let noOpProgressRejected = false;
try {
  await callToolJson(client, {
    name: "turn_progress",
    arguments: {
      ...scope,
      turn_id: turnId,
      lease_ms: 30000,
      current_action: "POST_TOOL_PROGRESS",
      durable_frontier: "CANARY_TOOL_VERIFIED",
    },
  });
} catch {
  noOpProgressRejected = true;
}
assert(noOpProgressRejected, "no-op turn_progress refreshed the lease");

let mutableRefRejected = false;
try {
  await callToolJson(client, {
    name: "handoff_verify",
    arguments: { locator: { ...locator, ref: "main" } },
  });
} catch {
  mutableRefRejected = true;
}
assert(mutableRefRejected, "mutable GitHub handoff ref was accepted");

const forbiddenRepo = await callToolJson(client, {
  name: "handoff_verify",
  arguments: {
    locator: {
      surface: "GITHUB",
      repository: "openai/openai",
      path: "README.md",
      ref,
    },
  },
});
assert(
  forbiddenRepo.verified === false &&
    forbiddenRepo.reason === "github_repository_not_allowlisted",
  `GitHub handoff repo allowlist failed open: ${JSON.stringify(forbiddenRepo)}`,
);

const driveRootAsArtifact = await callToolJson(client, {
  name: "handoff_verify",
  arguments: { locator: { surface: "GOOGLE_DRIVE", file_id: driveRootId } },
});
assert(
  driveRootAsArtifact.verified === false &&
    driveRootAsArtifact.reason === "drive_handoff_root_itself_is_not_an_artifact",
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
    durable_frontier: "CANARY_HANDOFF_VERIFIED",
    handoff: {
      required: true,
      locator,
      inventory: ["infrastructure/cloudflare-supervisor/README.md"],
      durable_frontier: "CANARY_HANDOFF_VERIFIED",
      next_action: "ASYNC_CI_RECONCILIATION",
    },
  },
});
assert(completed.status === "COMPLETED", `turn_complete failed: ${JSON.stringify(completed)}`);
assert(completed.generation === generation, "completion changed owner generation");
assert(completed.handoff?.verified === true, "required handoff was not verified");

const releasedAt = new Date().toISOString();
const releasedBeforeCi = await callToolJson(client, {
  name: "supervisor_snapshot",
  arguments: scope,
});
assert(releasedBeforeCi?.status === "COMPLETED", "turn was not released before CI observation");

const ciSnapshot = await githubCheckSnapshot(locator.repository, ref);
assert(ciSnapshot.blocks_turn === false, "CI observation became a turn lease");

const reconciledAfterCi = await callToolJson(client, {
  name: "supervisor_snapshot",
  arguments: scope,
});
assert(
  reconciledAfterCi?.status === "COMPLETED" &&
    reconciledAfterCi?.generation === generation,
  "asynchronous CI reconciliation reopened or replaced the completed turn",
);

const enforcement = await callToolJson(client, {
  name: "github_enforcement_status",
  arguments: {},
});
const enforcementMatch = enforcementMatches(enforcement);

await client.close();

const report = {
  schema: "ENTERPRISE_MATH_CONTROL_PLANE_E2E_CANARY_V1",
  status: "PASS",
  base_url: baseUrl,
  deployment_sha: healthBody?.deployment_sha,
  requested_deployment_sha: requestedRef,
  mcp_auth_mode: authMode,
  protocol_era: client.getProtocolEra?.(),
  tool_count: names.size,
  turn_status: completed.status,
  turn_generation: generation,
  released_at: releasedAt,
  pre_tool_checkpoint_verified: true,
  tool_call_verified: verified.verified === true,
  generation_recheck_verified: true,
  handoff_verified: completed.handoff?.verified === true,
  turn_released_before_ci_observation: true,
  async_ci_observation: ciSnapshot,
  reconciliation_preserved_completed_turn: true,
  no_op_progress_rejected: noOpProgressRejected,
  mutable_github_ref_rejected: mutableRefRejected,
  handoff_transport: verified.verification_transport,
  github_repo_allowlist_fail_closed:
    forbiddenRepo.reason === "github_repository_not_allowlisted",
  drive_root_fail_closed:
    driveRootAsArtifact.reason === "drive_handoff_root_itself_is_not_an_artifact",
  drive_handoff_verified: driveSmoke.verified === true,
  drive_handoff_reason: driveSmoke.reason,
  github_enforcement_verified: enforcement.verified === true,
  github_enforcement_match: enforcementMatch,
  github_main_protected: enforcement.main_protected === true,
  github_required_checks: enforcementContexts(enforcement),
  expected_required_checks: requiredEnforcementChecks,
  github_ruleset_count: enforcement.ruleset_count,
};

if (reportPath) {
  fs.writeFileSync(reportPath, `${JSON.stringify(report, null, 2)}\n`, "utf8");
}
console.log(JSON.stringify(report, null, 2));
