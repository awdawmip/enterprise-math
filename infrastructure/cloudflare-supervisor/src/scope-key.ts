export interface OwnerScopeIdentity {
  task_id: string;
  claim_id: string;
  execution_cohort_id?: string;
  execution_lane_id?: string;
}

const LEGACY_SEPARATOR = "::";

export function canonicalScopeKey(input: OwnerScopeIdentity): string {
  return JSON.stringify([
    input.task_id,
    input.claim_id,
    input.execution_cohort_id ?? null,
    input.execution_lane_id ?? null,
  ]);
}

export function legacyScopeKey(input: OwnerScopeIdentity): string | null {
  const parts = [
    input.task_id,
    input.claim_id,
    input.execution_cohort_id,
    input.execution_lane_id,
  ].filter((part): part is string => part !== undefined);

  if (parts.some((part) => part.includes(LEGACY_SEPARATOR))) return null;
  return parts.join(LEGACY_SEPARATOR);
}
