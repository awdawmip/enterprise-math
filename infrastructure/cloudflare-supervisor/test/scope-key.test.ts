import { describe, expect, it } from "vitest";
import { canonicalScopeKey, legacyScopeKey } from "../src/scope-key";

describe("owner-scope key compatibility", () => {
  it("keeps the canonical key unambiguous", () => {
    const left = canonicalScopeKey({ task_id: "RS::A", claim_id: "CLM" });
    const right = canonicalScopeKey({ task_id: "RS", claim_id: "A::CLM" });
    expect(left).not.toBe(right);
  });

  it("uses legacy fallback only for separator-safe historical identifiers", () => {
    expect(legacyScopeKey({
      task_id: "RS-SAFE",
      claim_id: "CLM-SAFE",
      execution_cohort_id: "COH-SAFE",
      execution_lane_id: "LANE-SAFE",
    })).toBe("RS-SAFE::CLM-SAFE::COH-SAFE::LANE-SAFE");

    expect(legacyScopeKey({ task_id: "RS::AMBIGUOUS", claim_id: "CLM" })).toBeNull();
    expect(legacyScopeKey({ task_id: "RS", claim_id: "CLM::AMBIGUOUS" })).toBeNull();
    expect(legacyScopeKey({
      task_id: "RS",
      claim_id: "CLM",
      execution_cohort_id: "COH::AMBIGUOUS",
    })).toBeNull();
  });
});
