import { DurableObject } from "cloudflare:workers";
import { canonicalScopeKey } from "./scope-key";
import type {
  AbandonInput,
  AcquireInput,
  CompleteInput,
  Env,
  HandoffState,
  OwnerScopeState,
  ProgressInput,
  RecoveryVerification,
} from "./types";

const STATE_KEY = "owner-scope-state";

function nowIso() {
  return new Date().toISOString();
}

function parseTime(value?: string): number | null {
  if (!value) return null;
  const n = Date.parse(value);
  return Number.isFinite(n) ? n : null;
}

export class OwnerScope extends DurableObject<Env> {
  constructor(ctx: DurableObjectState, env: Env) {
    super(ctx, env);
    this.ctx.storage.sql.exec(`
      CREATE TABLE IF NOT EXISTS audit_log (
        seq INTEGER PRIMARY KEY AUTOINCREMENT,
        at TEXT NOT NULL,
        event TEXT NOT NULL,
        payload TEXT NOT NULL
      )
    `);
  }

  private async read(): Promise<OwnerScopeState | null> {
    return (await this.ctx.storage.get<OwnerScopeState>(STATE_KEY)) ?? null;
  }

  private async write(state: OwnerScopeState) {
    await this.ctx.storage.put(STATE_KEY, state);
  }

  private audit(event: string, payload: unknown) {
    this.ctx.storage.sql.exec(
      "INSERT INTO audit_log(at,event,payload) VALUES(?,?,?)",
      nowIso(),
      event,
      JSON.stringify(payload),
    );
  }

  private async startRecoveryWorkflow(state: OwnerScopeState) {
    this.audit("RECOVERY_WORKFLOW_REQUESTED", {
      turn_id: state.turn_id,
      generation: state.generation,
    });
    await this.env.RECOVERY_WORKFLOW.create({
      id: `recovery-${crypto.randomUUID()}`,
      params: { scope_key: state.scope_key },
    });
  }

  async snapshot(): Promise<OwnerScopeState | null> {
    return this.read();
  }

  async auditTail(limit = 20): Promise<Array<Record<string, unknown>>> {
    const bounded = Math.max(1, Math.min(100, Math.trunc(limit)));
    return [
      ...this.ctx.storage.sql.exec(
        "SELECT seq,at,event,payload FROM audit_log ORDER BY seq DESC LIMIT ?",
        bounded,
      ),
    ].map((row: any) => ({
      seq: row.seq,
      at: row.at,
      event: row.event,
      payload: JSON.parse(String(row.payload)),
    }));
  }

  async acquire(input: AcquireInput): Promise<OwnerScopeState> {
    const current = await this.read();

    if (current?.status === "RUNNING") {
      if (current.turn_id === input.turn_id) {
        this.audit("TURN_ACQUIRE_IDEMPOTENT", { turn_id: input.turn_id });
        return current;
      }
      throw new Error(`scope already has running turn ${current.turn_id}`);
    }
    if (current?.status === "TURN_STALE") {
      throw new Error("scope recovery verification is still pending");
    }
    if (current?.status === "COMPLETED") {
      throw new Error("completed scope cannot be reopened by turn_acquire");
    }

    const now = Date.now();
    const defaultLease = Number(this.env.DEFAULT_TURN_LEASE_MS || "300000");
    const leaseMs = Math.max(30_000, Math.min(3_600_000, input.lease_ms ?? defaultLease));
    const next: OwnerScopeState = {
      schema: "ENTERPRISE_MATH_SUPERVISOR_OWNER_SCOPE_V1",
      scope_key: current?.scope_key ?? canonicalScopeKey(input),
      task_id: input.task_id,
      claim_id: input.claim_id,
      researcher_id: input.researcher_id ?? current?.researcher_id,
      execution_cohort_id: input.execution_cohort_id,
      execution_lane_id: input.execution_lane_id,
      turn_id: input.turn_id,
      status: "RUNNING",
      started_at: new Date(now).toISOString(),
      last_progress_at: new Date(now).toISOString(),
      lease_until: new Date(now + leaseMs).toISOString(),
      durable_frontier: input.durable_frontier ?? current?.durable_frontier,
      current_action: input.current_action,
      recovery_ready: false,
      recovery_reason: undefined,
      recovery_verification: undefined,
      handoff: {
        ...(current?.handoff ?? { required: false, verified: false }),
        required: current?.handoff.required === true || input.handoff_required === true,
        verified: current?.handoff.verified ?? false,
      },
      generation: (current?.generation ?? 0) + 1,
    };
    await this.write(next);
    await this.ctx.storage.setAlarm(now + leaseMs);
    this.audit("TURN_ACQUIRED", { turn_id: input.turn_id, lease_ms: leaseMs });
    return next;
  }

  async progress(input: ProgressInput): Promise<OwnerScopeState> {
    const current = await this.read();
    if (!current) throw new Error("scope not initialized");
    if (current.status !== "RUNNING") throw new Error(`scope is ${current.status}`);
    if (current.turn_id !== input.turn_id) throw new Error("turn_id does not own scope");

    const now = Date.now();
    const defaultLease = Number(this.env.DEFAULT_TURN_LEASE_MS || "300000");
    const leaseMs = Math.max(30_000, Math.min(3_600_000, input.lease_ms ?? defaultLease));
    const next: OwnerScopeState = {
      ...current,
      last_progress_at: new Date(now).toISOString(),
      lease_until: new Date(now + leaseMs).toISOString(),
      current_action: input.current_action ?? current.current_action,
      durable_frontier: input.durable_frontier ?? current.durable_frontier,
    };
    await this.write(next);
    await this.ctx.storage.setAlarm(now + leaseMs);
    this.audit("TURN_PROGRESS", {
      turn_id: input.turn_id,
      durable_frontier: input.durable_frontier,
      current_action: input.current_action,
    });
    return next;
  }

  async complete(input: CompleteInput): Promise<OwnerScopeState> {
    const current = await this.read();
    if (!current) throw new Error("scope not initialized");
    if (current.status !== "RUNNING") {
      throw new Error(`late turn completion forbidden from state ${current.status}`);
    }
    if (current.turn_id !== input.turn_id) throw new Error("turn_id does not own scope");

    const incoming = input.handoff;
    const required = current.handoff.required === true || incoming?.required === true;
    const incomingRequiredVerification = incoming?.required === true && incoming.verified === true;
    const verified = required
      ? current.handoff.verified === true || incomingRequiredVerification
      : (incoming?.verified ?? current.handoff.verified ?? false);
    const handoff: HandoffState = {
      ...current.handoff,
      ...(incoming ?? {}),
      required,
      verified,
      verified_at: verified
        ? (incomingRequiredVerification ? incoming?.verified_at : current.handoff.verified_at)
        : undefined,
      verification: incomingRequiredVerification
        ? incoming?.verification
        : current.handoff.verification,
    };

    const incomplete = handoff.required && !handoff.verified;
    const next: OwnerScopeState = {
      ...current,
      status: incomplete ? "HANDOFF_INCOMPLETE" : "COMPLETED",
      completed_at: nowIso(),
      durable_frontier: input.durable_frontier ?? current.durable_frontier,
      handoff,
      recovery_ready: incomplete,
      recovery_reason: incomplete ? "REQUIRED_DURABLE_HANDOFF_NOT_VERIFIED" : undefined,
    };
    await this.write(next);
    await this.ctx.storage.deleteAlarm();
    this.audit(incomplete ? "HANDOFF_INCOMPLETE" : "TURN_COMPLETED", {
      turn_id: input.turn_id,
      handoff,
    });
    return next;
  }

  async abandon(input: AbandonInput): Promise<OwnerScopeState> {
    const current = await this.read();
    if (!current) throw new Error("scope not initialized");
    if (current.status !== "RUNNING") {
      throw new Error(`turn_abandon forbidden from state ${current.status}`);
    }
    if (input.turn_id && current.turn_id && input.turn_id !== current.turn_id) {
      throw new Error("turn_id does not own scope");
    }
    const next: OwnerScopeState = {
      ...current,
      status: "ABANDONED",
      recovery_ready: true,
      recovery_reason: input.reason,
      stale_at: nowIso(),
    };
    await this.write(next);
    await this.ctx.storage.deleteAlarm();
    this.audit("TURN_ABANDONED", input);
    return next;
  }

  async markRecoveryVerified(input: RecoveryVerification): Promise<OwnerScopeState> {
    const current = await this.read();
    if (!current) throw new Error("scope not initialized");
    if (current.status === "RECOVERY_READY") return current;
    if (current.status !== "TURN_STALE") {
      throw new Error(`recovery verification cannot overwrite state ${current.status}`);
    }
    const next: OwnerScopeState = {
      ...current,
      status: "RECOVERY_READY",
      recovery_ready: true,
      recovery_verification: input.result,
    };
    await this.write(next);
    this.audit("RECOVERY_VERIFIED", input);
    return next;
  }

  async alarm(): Promise<void> {
    const current = await this.read();
    if (!current) return;

    if (current.status === "TURN_STALE" && !current.recovery_verification) {
      await this.startRecoveryWorkflow(current);
      return;
    }
    if (current.status !== "RUNNING") return;

    const lastProgress = parseTime(current.last_progress_at) ?? 0;
    const leaseUntil = parseTime(current.lease_until) ?? 0;
    const now = Date.now();

    if (leaseUntil > now) {
      await this.ctx.storage.setAlarm(leaseUntil);
      return;
    }

    const threshold = Number(this.env.STALE_RECOVERY_THRESHOLD_MS || "600000");
    const staleBy = Math.max(leaseUntil, lastProgress + threshold);
    if (staleBy > now) {
      await this.ctx.storage.setAlarm(staleBy);
      return;
    }

    const next: OwnerScopeState = {
      ...current,
      status: "TURN_STALE",
      stale_at: new Date(now).toISOString(),
      recovery_ready: false,
      recovery_reason: "TURN_EXECUTION_LEASE_EXPIRED_WITHOUT_VERIFIED_PROGRESS",
    };
    await this.write(next);
    this.audit("TURN_STALE", {
      turn_id: current.turn_id,
      last_progress_at: current.last_progress_at,
      lease_until: current.lease_until,
    });

    await this.startRecoveryWorkflow(next);
  }
}
