import { createMcpHandler } from "agents/mcp/server";
import { McpServer } from "@modelcontextprotocol/server";
import { z } from "zod";
import { OwnerScope } from "./owner-scope";
import { RecoveryWorkflow } from "./recovery-workflow";
import { githubEnforcementStatus, verifyHandoffLocator } from "./external";
import { canonicalScopeKey, legacyScopeKey } from "./scope-key";
import { mcpAuthMode, requireBearer, requireMcpAuth, verifyGithubWebhook } from "./security";
import type { Env, HandoffLocator, HandoffState } from "./types";

export { OwnerScope, RecoveryWorkflow };

const BASE_PATH = "/em";
const MCP_PATH = `${BASE_PATH}/mcp`;
const API_PREFIX = `${BASE_PATH}/api/`;

type ScopeIdentity = {
  task_id: string;
  claim_id: string;
  execution_cohort_id?: string;
  execution_lane_id?: string;
};

async function resolveScopeStub(env: Env, input: ScopeIdentity) {
  const canonicalKey = canonicalScopeKey(input);
  const canonical = env.OWNER_SCOPES.getByName(canonicalKey);
  if (await canonical.snapshot()) return canonical;

  const legacyKey = legacyScopeKey(input);
  if (legacyKey !== canonicalKey) {
    const legacy = env.OWNER_SCOPES.getByName(legacyKey);
    if (await legacy.snapshot()) return legacy;
  }
  return canonical;
}

function jsonText(value: unknown) {
  return {
    content: [{ type: "text" as const, text: JSON.stringify(value, null, 2) }],
  };
}

function serverFactory(env: Env) {
  const server = new McpServer({
    name: "enterprise-math-supervisor",
    version: "0.1.0",
  });

  const scopeFields = {
    task_id: z.string().min(1),
    claim_id: z.string().min(1),
    execution_cohort_id: z.string().min(1).optional(),
    execution_lane_id: z.string().min(1).optional(),
  };

  server.registerTool(
    "supervisor_snapshot",
    {
      description: "Read the exact durable Supervisor state for one task/claim owner scope.",
      inputSchema: scopeFields,
    },
    async (input) => {
      const stub = await resolveScopeStub(env, input);
      return jsonText(await stub.snapshot());
    },
  );

  server.registerTool(
    "turn_acquire",
    {
      description:
        "Acquire or resume a turn-execution lease for an already-authorized Enterprise Math owner scope. This does not create a CLAIM.",
      inputSchema: {
        ...scopeFields,
        turn_id: z.string().min(1),
        researcher_id: z.string().min(1).optional(),
        lease_ms: z.number().int().min(30_000).max(3_600_000).optional(),
        current_action: z.string().min(1).optional(),
        durable_frontier: z.string().min(1).optional(),
        handoff_required: z.boolean().optional(),
      },
    },
    async (input) => {
      const stub = await resolveScopeStub(env, input);
      return jsonText(await stub.acquire(input));
    },
  );

  server.registerTool(
    "turn_progress",
    {
      description:
        "Refresh a turn lease only when material progress occurred; repeated status polls are not progress.",
      inputSchema: {
        ...scopeFields,
        turn_id: z.string().min(1),
        lease_ms: z.number().int().min(30_000).max(3_600_000).optional(),
        current_action: z.string().min(1).optional(),
        durable_frontier: z.string().min(1).optional(),
      },
    },
    async (input) => {
      const stub = await resolveScopeStub(env, input);
      return jsonText(await stub.progress(input));
    },
  );

  const githubLocatorSchema = z.object({
    surface: z.literal("GITHUB"),
    repository: z.string().min(3),
    path: z.string().min(1),
    ref: z.string().regex(/^[0-9a-f]{40}$/i),
    expected_blob_sha: z.string().regex(/^[0-9a-f]{40}$/i).optional(),
  });
  const driveLocatorSchema = z.object({
    surface: z.literal("GOOGLE_DRIVE"),
    file_id: z.string().min(10),
    expected_name: z.string().optional(),
    expected_md5: z.string().regex(/^[0-9a-f]{32}$/i).optional(),
  });
  const locatorSchema = z.discriminatedUnion("surface", [
    githubLocatorSchema,
    driveLocatorSchema,
  ]);

  server.registerTool(
    "handoff_verify",
    {
      description:
        "Verify that a one-shot Researcher handoff is externally durable on GitHub or Google Drive.",
      inputSchema: { locator: locatorSchema },
    },
    async ({ locator }) => jsonText(await verifyHandoffLocator(env, locator as HandoffLocator)),
  );

  server.registerTool(
    "turn_complete",
    {
      description:
        "Complete a live turn. A previously required durable handoff cannot be downgraded, and stale/recovery-ready turns cannot regain authority by completing late.",
      inputSchema: {
        ...scopeFields,
        turn_id: z.string().min(1),
        durable_frontier: z.string().min(1).optional(),
        handoff: z.object({
          required: z.boolean(),
          locator: locatorSchema.optional(),
          inventory: z.array(z.string().min(1)).optional(),
          durable_frontier: z.string().min(1).optional(),
          next_action: z.string().min(1).optional(),
        }).optional(),
      },
    },
    async (input) => {
      let handoff: HandoffState | undefined;
      if (input.handoff) {
        let verification: Record<string, unknown> | undefined;
        let verified = false;
        if (input.handoff.locator) {
          verification = await verifyHandoffLocator(
            env,
            input.handoff.locator as HandoffLocator,
          ) as Record<string, unknown>;
          verified = verification.verified === true;
        }
        handoff = {
          ...input.handoff,
          verified,
          verified_at: verified ? new Date().toISOString() : undefined,
          verification,
        };
      }
      const stub = await resolveScopeStub(env, input);
      return jsonText(await stub.complete({
        turn_id: input.turn_id,
        durable_frontier: input.durable_frontier,
        handoff,
      }));
    },
  );

  server.registerTool(
    "turn_abandon",
    {
      description:
        "Mark one exact currently-running turn abandoned while preserving its owner CLAIM and durable frontier for recovery.",
      inputSchema: {
        ...scopeFields,
        turn_id: z.string().min(1),
        reason: z.string().min(1),
      },
    },
    async (input) => {
      const stub = await resolveScopeStub(env, input);
      return jsonText(await stub.abandon({ turn_id: input.turn_id, reason: input.reason }));
    },
  );

  server.registerTool(
    "recovery_status",
    {
      description: "Read recovery state and recent Supervisor audit events for one owner scope.",
      inputSchema: { ...scopeFields, audit_limit: z.number().int().min(1).max(50).optional() },
    },
    async (input) => {
      const stub = await resolveScopeStub(env, input);
      const [snapshot, audit] = await Promise.all([
        stub.snapshot(),
        stub.auditTail(input.audit_limit ?? 10),
      ]);
      return jsonText({ snapshot, audit });
    },
  );

  server.registerTool(
    "github_enforcement_status",
    {
      description:
        "Read current GitHub main protection and ruleset state. This v1 tool is deliberately read-only.",
      inputSchema: {},
    },
    async () => jsonText(await githubEnforcementStatus(env)),
  );

  return server;
}

async function handleApi(request: Request, env: Env): Promise<Response> {
  const url = new URL(request.url);
  if (url.pathname === `${BASE_PATH}/api/v1/github/enforcement` && request.method === "GET") {
    return Response.json(await githubEnforcementStatus(env));
  }
  return new Response("Not found", { status: 404 });
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);

    if (url.pathname === `${BASE_PATH}/health`) {
      return Response.json({
        ok: true,
        service: "enterprise-math-supervisor",
        version: "0.1.0",
        deployment_sha: env.DEPLOYMENT_SHA ?? null,
        base_path: BASE_PATH,
        mcp_auth_mode: mcpAuthMode(env),
        time: new Date().toISOString(),
      });
    }

    if (url.pathname === `${BASE_PATH}/webhook/github` && request.method === "POST") {
      const verification = await verifyGithubWebhook(request, env.GITHUB_WEBHOOK_SECRET);
      if (!verification.ok) return new Response("Invalid webhook signature", { status: 401 });
      return new Response(null, { status: 202 });
    }

    if (url.pathname === MCP_PATH) {
      const denied = await requireMcpAuth(request, env);
      if (denied) return denied;
      const handler = createMcpHandler(() => serverFactory(env), {
        route: MCP_PATH,
        responseMode: "json",
        legacy: "stateless",
        corsOptions: false,
        onerror: (error) => console.error("MCP error", error),
      });
      return handler(request, env, ctx);
    }

    if (url.pathname.startsWith(API_PREFIX)) {
      const denied = await requireBearer(request, env);
      if (denied) return denied;
      return handleApi(request, env);
    }

    return new Response("Not found", { status: 404 });
  },
};
