export type ScopeStatus =
  | "IDLE"
  | "RUNNING"
  | "TURN_STALE"
  | "RECOVERY_READY"
  | "COMPLETED"
  | "ABANDONED"
  | "HANDOFF_INCOMPLETE";

export type DurableSurface = "GITHUB" | "GOOGLE_DRIVE";

export interface GithubLocator {
  surface: "GITHUB";
  repository: string;
  path: string;
  ref: string;
  expected_blob_sha?: string;
}

export interface GoogleDriveLocator {
  surface: "GOOGLE_DRIVE";
  file_id: string;
  expected_name?: string;
  expected_md5?: string;
}

export type HandoffLocator = GithubLocator | GoogleDriveLocator;

export interface HandoffState {
  required: boolean;
  verified: boolean;
  locator?: HandoffLocator;
  inventory?: string[];
  durable_frontier?: string;
  next_action?: string;
  verified_at?: string;
  verification?: Record<string, unknown>;
}

export interface OwnerScopeState {
  schema: "ENTERPRISE_MATH_SUPERVISOR_OWNER_SCOPE_V1";
  scope_key: string;
  task_id: string;
  claim_id: string;
  researcher_id?: string;
  execution_cohort_id?: string;
  execution_lane_id?: string;
  turn_id?: string;
  status: ScopeStatus;
  started_at?: string;
  last_progress_at?: string;
  lease_until?: string;
  stale_at?: string;
  completed_at?: string;
  durable_frontier?: string;
  current_action?: string;
  recovery_ready: boolean;
  recovery_reason?: string;
  recovery_verification?: Record<string, unknown>;
  handoff: HandoffState;
  generation: number;
}

export interface AcquireInput {
  task_id: string;
  claim_id: string;
  turn_id: string;
  researcher_id?: string;
  execution_cohort_id?: string;
  execution_lane_id?: string;
  lease_ms?: number;
  current_action?: string;
  durable_frontier?: string;
  handoff_required?: boolean;
}

export interface ProgressInput {
  turn_id: string;
  current_action?: string;
  durable_frontier?: string;
  lease_ms?: number;
}

export interface CompleteInput {
  turn_id: string;
  durable_frontier?: string;
  handoff?: HandoffState;
}

export interface AbandonInput {
  turn_id?: string;
  reason: string;
}

export interface RecoveryVerification {
  verified_at: string;
  result: Record<string, unknown>;
}

export interface Env {
  OWNER_SCOPES: {
    getByName(name: string): any;
  };
  RECOVERY_WORKFLOW: {
    create(options: { id?: string; params: Record<string, unknown> }): Promise<unknown>;
  };

  // Bootstrap/operator auth. /em/api/* remains on this surface in V1.
  SUPERVISOR_API_TOKEN: string;
  GITHUB_WEBHOOK_SECRET?: string;

  // When both are configured, /em/mcp switches fail-closed to Cloudflare Access JWT auth.
  ACCESS_TEAM_DOMAIN?: string;
  ACCESS_AUD?: string;

  // GitHub read identity: prefer a repository-scoped GitHub App; PAT is compatibility only.
  GITHUB_APP_ID?: string;
  GITHUB_APP_INSTALLATION_ID?: string;
  GITHUB_APP_PRIVATE_KEY?: string;
  GITHUB_READ_TOKEN?: string;
  GITHUB_HANDOFF_REPOSITORIES: string;

  // Google Drive read identity: prefer a service account shared only onto the handoff root.
  GOOGLE_SERVICE_ACCOUNT_EMAIL?: string;
  GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY?: string;
  GOOGLE_DRIVE_BEARER_TOKEN?: string;
  GOOGLE_DRIVE_HANDOFF_ROOT_ID: string;

  DEPLOYMENT_SHA?: string;
  DEFAULT_TURN_LEASE_MS: string;
  STALE_RECOVERY_THRESHOLD_MS: string;
  ENTERPRISE_MATH_REPOSITORY: string;
}
