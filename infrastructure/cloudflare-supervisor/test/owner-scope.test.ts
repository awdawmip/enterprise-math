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
});
