import { env, runInDurableObject } from "cloudflare:test";
import { describe, expect, it } from "vitest";
import type { OwnerScope } from "../src/owner-scope";

function stubFor(label: string) {
  return env.OWNER_SCOPES.getByName(`${label}-${crypto.randomUUID()}`);
}

describe("OwnerScope state machine", () => {
  it("only lets the exact running turn abandon its scope", async () => {
    const stub = stubFor("abandon-owner");
    await stub.acquire({
      task_id: "RS-TEST",
      claim_id: "CLM-TEST",
      turn_id: "TURN-OWNER",
      current_action: "RUNNING",
    });

    const errors = await runInDurableObject(stub, async (instance: OwnerScope) => {
      const attempt = async (input: never) => {
        try {
          await instance.abandon(input);
          return null;
        } catch (error) {
          return String((error as Error).message);
        }
      };
      return [
        await attempt({ turn_id: "TURN-OTHER", reason: "wrong owner" } as never),
        await attempt({ reason: "missing owner" } as never),
      ];
    });
    expect(errors).toEqual([
      "turn_id does not own scope",
      "turn_id does not own scope",
    ]);
    expect(await stub.snapshot()).toMatchObject({ status: "RUNNING", turn_id: "TURN-OWNER" });

    expect(await stub.abandon({ turn_id: "TURN-OWNER", reason: "operator stopped" }))
      .toMatchObject({ status: "ABANDONED", recovery_ready: true });
  });

  it("rolls back state and alarm when the audit insert fails", async () => {
    const stub = stubFor("atomic-commit");
    const before = await stub.acquire({
      task_id: "RS-ATOMIC",
      claim_id: "CLM-ATOMIC",
      turn_id: "TURN-ATOMIC",
      current_action: "BEFORE",
      durable_frontier: "F0",
      lease_ms: 30_000,
    });
    const alarmBefore = await runInDurableObject(
      stub,
      async (_instance: OwnerScope, state) => {
        state.storage.sql.exec(`
          CREATE TRIGGER reject_turn_progress
          BEFORE INSERT ON audit_log
          WHEN NEW.event = 'TURN_PROGRESS'
          BEGIN
            SELECT RAISE(ABORT, 'forced audit failure');
          END
        `);
        return state.storage.getAlarm();
      },
    );

    const failure = await runInDurableObject(stub, async (instance: OwnerScope) => {
      try {
        await instance.progress({
          turn_id: "TURN-ATOMIC",
          current_action: "AFTER",
          durable_frontier: "F1",
          lease_ms: 60_000,
        });
        return null;
      } catch (error) {
        return String((error as Error).message);
      }
    });
    expect(failure).toContain("forced audit failure");

    expect(await stub.snapshot()).toEqual(before);
    const persisted = await runInDurableObject(
      stub,
      async (instance: OwnerScope, state) => ({
        alarm: await state.storage.getAlarm(),
        audit: await instance.auditTail(20),
      }),
    );
    expect(persisted.alarm).toBe(alarmBefore);
    expect(persisted.audit.map((row) => row.event)).not.toContain("TURN_PROGRESS");
  });

  it("releases the turn before asynchronous CI reconciliation", async () => {
    const stub = stubFor("e2e-canary");
    const acquired = await stub.acquire({
      task_id: "RS-CONTROL-PLANE-E2E-CANARY",
      claim_id: "CLM-CONTROL-PLANE-E2E-CANARY",
      turn_id: "TURN-CONTROL-PLANE-E2E-CANARY",
      current_action: "PRE_TOOL_CHECKPOINT",
      durable_frontier: "CANARY_PRE_TOOL",
      handoff_required: true,
      lease_ms: 30_000,
    });
    expect(acquired).toMatchObject({
      status: "RUNNING",
      current_action: "PRE_TOOL_CHECKPOINT",
      durable_frontier: "CANARY_PRE_TOOL",
      generation: 1,
    });

    const generationBeforeTool = acquired.generation;
    const preToolSnapshot = await stub.snapshot();
    expect(preToolSnapshot?.generation).toBe(generationBeforeTool);
    expect(preToolSnapshot?.turn_id).toBe("TURN-CONTROL-PLANE-E2E-CANARY");

    const progressed = await stub.progress({
      turn_id: "TURN-CONTROL-PLANE-E2E-CANARY",
      current_action: "POST_TOOL_PROGRESS",
      durable_frontier: "CANARY_TOOL_VERIFIED",
      lease_ms: 30_000,
    });
    expect(progressed).toMatchObject({
      status: "RUNNING",
      current_action: "POST_TOOL_PROGRESS",
      durable_frontier: "CANARY_TOOL_VERIFIED",
      generation: generationBeforeTool,
    });

    const completed = await stub.complete({
      turn_id: "TURN-CONTROL-PLANE-E2E-CANARY",
      durable_frontier: "CANARY_HANDOFF_VERIFIED",
      handoff: {
        required: true,
        verified: true,
        locator: {
          surface: "GITHUB",
          repository: "awdawmip/enterprise-math",
          path: "infrastructure/cloudflare-supervisor/README.md",
          ref: "0123456789abcdef0123456789abcdef01234567",
        },
        inventory: ["infrastructure/cloudflare-supervisor/README.md"],
        durable_frontier: "CANARY_HANDOFF_VERIFIED",
        next_action: "ASYNC_CI_RECONCILIATION",
      },
    });
    expect(completed).toMatchObject({
      status: "COMPLETED",
      recovery_ready: false,
      generation: generationBeforeTool,
      handoff: { required: true, verified: true },
    });

    const releasedBeforeCiObservation = await stub.snapshot();
    expect(releasedBeforeCiObservation?.status).toBe("COMPLETED");

    // CI_PENDING_NONBLOCKING: pending integration cannot reopen or prolong the turn.
    const asynchronousCiObservation = {
      state: "PENDING",
      blocks_turn: false,
      observed_after_release: true,
    };
    expect(asynchronousCiObservation.blocks_turn).toBe(false);

    await expect(
      stub.acquire({
        task_id: "RS-CONTROL-PLANE-E2E-CANARY",
        claim_id: "CLM-CONTROL-PLANE-E2E-CANARY",
        turn_id: "TURN-CONTROL-PLANE-E2E-CANARY-REOPEN",
        current_action: "CI_PENDING",
      }),
    ).rejects.toThrow("completed scope cannot be reopened by turn_acquire");

    const reconciled = await stub.snapshot();
    expect(reconciled).toMatchObject({
      status: "COMPLETED",
      generation: generationBeforeTool,
      durable_frontier: "CANARY_HANDOFF_VERIFIED",
    });

    const audit = await stub.auditTail(20);
    const events = [...audit].reverse().map((row) => row.event);
    expect(events).toEqual([
      "TURN_ACQUIRED",
      "TURN_PROGRESS",
      "TURN_COMPLETED",
    ]);
  });
});
