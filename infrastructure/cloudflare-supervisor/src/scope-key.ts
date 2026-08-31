export interface OwnerScopeIdentity {
  task_id: string;
  claim_id: string;
  execution_cohort_id?: string;
  execution_lane_id?: string;
}

export function canonicalScopeKey(input: OwnerScopeIdentity): string {
  return JSON.stringify([
    input.task_id,
    input.claim_id,
    input.execution_cohort_id ?? null,
    input.execution_lane_id ?? null,
  ]);
}

export function legacyScopeKey(input: OwnerScopeIdentity): string {
  return `${input.task_id}::${input.claim_id}` +
    `${input.execution_cohort_id ? `::${input.execution_cohort_id}` : ""}` +
    `${input.execution_lane_id ? `::${input.execution_lane_id}` : ""}`;
}
