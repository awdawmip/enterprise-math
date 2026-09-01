import { WorkflowEntrypoint, type WorkflowEvent, type WorkflowStep } from "cloudflare:workers";
import type { Env, HandoffLocator, OwnerScopeState } from "./types";
import { verifyHandoffLocator } from "./external";

export class RecoveryWorkflow extends WorkflowEntrypoint<Env, { scope_key: string }> {
  async run(event: WorkflowEvent<{ scope_key: string }>, step: WorkflowStep) {
    const { scope_key } = event.payload;
    const snapshot = await step.do("load owner scope", async () => {
      const stub = this.env.OWNER_SCOPES.getByName(scope_key);
      return (await stub.snapshot()) as OwnerScopeState | null;
    });

    if (!snapshot) return { status: "NO_SCOPE" };

    const verification = await step.do(
      "verify durable recovery frontier",
      {
        retries: { limit: 3, delay: "10 seconds", backoff: "exponential" },
        timeout: "2 minutes",
      },
      async () => {
        const result: Record<string, unknown> = {
          task_id: snapshot.task_id,
          claim_id: snapshot.claim_id,
          durable_frontier: snapshot.durable_frontier ?? null,
          handoff_required: snapshot.handoff.required,
          handoff_verified: snapshot.handoff.verified,
        };
        if (snapshot.handoff.locator) {
          result.handoff_locator_verification = await verifyHandoffLocator(
            this.env,
            snapshot.handoff.locator as HandoffLocator,
          );
        }
        return result;
      },
    );

    await step.do("mark recovery ready", async () => {
      const stub = this.env.OWNER_SCOPES.getByName(scope_key);
      return stub.markRecoveryReady({
        assessed_at: new Date().toISOString(),
        result: verification,
      });
    });

    return { status: "RECOVERY_READY", scope_key, verification };
  }
}
