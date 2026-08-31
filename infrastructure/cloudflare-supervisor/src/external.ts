import { githubReadAccessToken, googleDriveAccessToken } from "./external-auth";
import type { Env, GithubLocator, GoogleDriveLocator, HandoffLocator } from "./types";

const encoder = new TextEncoder();
const GOOGLE_SHORTCUT_MIME = "application/vnd.google-apps.shortcut";

type GithubBranchResponse = {
  protected?: boolean;
  protection?: {
    enabled?: boolean;
    required_status_checks?: unknown;
  };
};

async function githubHeaders(env: Env): Promise<HeadersInit> {
  const headers: Record<string, string> = {
    Accept: "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "enterprise-math-supervisor",
  };
  const token = await githubReadAccessToken(env);
  if (token) headers.Authorization = `Bearer ${token}`;
  return headers;
}

function githubIdentityMode(env: Env): string {
  if (env.GITHUB_READ_TOKEN) return "COMPAT_READ_TOKEN";
  if (env.GITHUB_APP_ID && env.GITHUB_APP_INSTALLATION_ID && env.GITHUB_APP_PRIVATE_KEY) {
    return "REPOSITORY_SCOPED_GITHUB_APP";
  }
  return "ANONYMOUS";
}

function githubHandoffRepositories(env: Env): Set<string> {
  return new Set(
    (env.GITHUB_HANDOFF_REPOSITORIES || env.ENTERPRISE_MATH_REPOSITORY || "awdawmip/enterprise-math")
      .split(",")
      .map((value) => value.trim())
      .filter(Boolean),
  );
}

function hex(bytes: ArrayBuffer): string {
  return [...new Uint8Array(bytes)]
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

async function gitBlobSha1(content: ArrayBuffer): Promise<string> {
  const body = new Uint8Array(content);
  const header = encoder.encode(`blob ${body.byteLength}\0`);
  const framed = new Uint8Array(header.byteLength + body.byteLength);
  framed.set(header, 0);
  framed.set(body, header.byteLength);
  return hex(await crypto.subtle.digest("SHA-1", framed));
}

function rawGithubUrl(locator: GithubLocator): string {
  const [owner, repo] = locator.repository.split("/");
  const path = locator.path.split("/").map(encodeURIComponent).join("/");
  return `https://raw.githubusercontent.com/${encodeURIComponent(owner)}/${encodeURIComponent(repo)}/${locator.ref}/${path}`;
}

async function verifyGithubImmutableRaw(locator: GithubLocator, apiStatus: number) {
  if (!/^[0-9a-f]{40}$/i.test(locator.ref)) {
    return {
      verified: false,
      status: apiStatus,
      reason: "github_api_unavailable_and_ref_not_immutable_commit",
    };
  }

  const response = await fetch(rawGithubUrl(locator), {
    headers: { "User-Agent": "enterprise-math-supervisor" },
  });
  if (!response.ok) {
    return {
      verified: false,
      status: response.status,
      reason: "github_raw_locator_not_found",
      api_status: apiStatus,
    };
  }

  const body = await response.arrayBuffer();
  const blobSha = await gitBlobSha1(body);
  if (locator.expected_blob_sha && blobSha !== locator.expected_blob_sha.toLowerCase()) {
    return {
      verified: false,
      status: 200,
      reason: "github_blob_mismatch",
      observed_blob_sha: blobSha,
      verification_transport: "RAW_IMMUTABLE_COMMIT_FALLBACK",
    };
  }

  return {
    verified: true,
    surface: "GITHUB",
    repository: locator.repository,
    path: locator.path,
    ref: locator.ref,
    blob_sha: blobSha,
    size: body.byteLength,
    verification_transport: "RAW_IMMUTABLE_COMMIT_FALLBACK",
    api_status: apiStatus,
  };
}

export async function verifyGithubLocator(env: Env, locator: GithubLocator) {
  if (!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(locator.repository)) {
    throw new Error("invalid GitHub repository");
  }
  if (!githubHandoffRepositories(env).has(locator.repository)) {
    return {
      verified: false,
      reason: "github_repository_not_allowlisted",
      repository: locator.repository,
    };
  }
  if (!locator.path || locator.path.startsWith("/") || locator.path.includes("..")) {
    throw new Error("invalid GitHub path");
  }
  if (!/^[0-9a-f]{40}$/i.test(locator.ref)) {
    return { verified: false, reason: "github_ref_not_immutable_commit" };
  }

  const url =
    `https://api.github.com/repos/${locator.repository}/contents/` +
    `${locator.path.split("/").map(encodeURIComponent).join("/")}?ref=${encodeURIComponent(locator.ref)}`;
  const response = await fetch(url, { headers: await githubHeaders(env) });
  if (!response.ok) {
    if (response.status === 403 || response.status === 429) {
      return verifyGithubImmutableRaw(locator, response.status);
    }
    return { verified: false, status: response.status, reason: "github_locator_not_found" };
  }
  const data = (await response.json()) as {
    sha?: string;
    path?: string;
    type?: string;
    size?: number;
    html_url?: string;
  };
  if (data.type !== "file") {
    return {
      verified: false,
      status: 200,
      reason: "github_locator_not_file",
      observed_type: data.type,
    };
  }
  if (locator.expected_blob_sha && data.sha !== locator.expected_blob_sha) {
    return {
      verified: false,
      status: 200,
      reason: "github_blob_mismatch",
      observed_blob_sha: data.sha,
    };
  }
  return {
    verified: true,
    surface: "GITHUB",
    repository: locator.repository,
    path: data.path ?? locator.path,
    ref: locator.ref,
    blob_sha: data.sha,
    object_type: data.type,
    size: data.size,
    html_url: data.html_url,
    verification_transport: "GITHUB_CONTENTS_API",
  };
}

async function driveMetadata(
  token: string,
  fileId: string,
  fields: string,
): Promise<{ ok: true; data: Record<string, unknown> } | { ok: false; status: number }> {
  const url =
    `https://www.googleapis.com/drive/v3/files/${encodeURIComponent(fileId)}` +
    `?supportsAllDrives=true&fields=${encodeURIComponent(fields)}`;
  const response = await fetch(url, { headers: { Authorization: `Bearer ${token}` } });
  if (!response.ok) return { ok: false, status: response.status };
  return { ok: true, data: (await response.json()) as Record<string, unknown> };
}

async function verifyDriveAncestry(
  env: Env,
  token: string,
  initialParents: string[],
): Promise<Record<string, unknown>> {
  const root = env.GOOGLE_DRIVE_HANDOFF_ROOT_ID?.trim();
  if (!root) return { allowed: false, reason: "drive_handoff_root_not_configured" };

  let frontier = [...initialParents];
  const seen = new Set<string>();
  for (let depth = 1; depth <= 64 && frontier.length > 0; depth += 1) {
    const next: string[] = [];
    for (const parentId of frontier) {
      if (parentId === root) return { allowed: true, root_id: root, depth };
      if (seen.has(parentId)) continue;
      seen.add(parentId);

      const parent = await driveMetadata(token, parentId, "id,parents,trashed");
      if (!parent.ok) {
        return {
          allowed: false,
          reason: "drive_parent_lookup_failed",
          status: parent.status,
          parent_id: parentId,
        };
      }
      if (parent.data.trashed === true) continue;
      const parents = Array.isArray(parent.data.parents)
        ? parent.data.parents.filter((value): value is string => typeof value === "string")
        : [];
      next.push(...parents);
    }
    frontier = next;
  }
  return { allowed: false, reason: "drive_file_not_under_handoff_root", root_id: root };
}

export async function verifyGoogleDriveLocator(env: Env, locator: GoogleDriveLocator) {
  if (!/^[A-Za-z0-9_-]{10,}$/.test(locator.file_id)) {
    throw new Error("invalid Google Drive file id");
  }
  const root = env.GOOGLE_DRIVE_HANDOFF_ROOT_ID?.trim();
  if (!root) return { verified: false, reason: "drive_handoff_root_not_configured" };
  if (locator.file_id === root) {
    return { verified: false, reason: "drive_handoff_root_itself_is_not_an_artifact" };
  }

  const token = await googleDriveAccessToken(env);
  if (!token) {
    return { verified: false, reason: "google_drive_read_identity_not_configured" };
  }

  const file = await driveMetadata(
    token,
    locator.file_id,
    "id,name,mimeType,modifiedTime,md5Checksum,size,trashed,parents,driveId",
  );
  if (!file.ok) {
    return { verified: false, status: file.status, reason: "drive_locator_not_found" };
  }
  const data = file.data;
  if (data.trashed === true) return { verified: false, reason: "drive_file_trashed" };
  if (data.mimeType === GOOGLE_SHORTCUT_MIME) {
    return { verified: false, reason: "drive_shortcut_not_accepted_for_handoff" };
  }

  const parents = Array.isArray(data.parents)
    ? data.parents.filter((value): value is string => typeof value === "string")
    : [];
  const ancestry = await verifyDriveAncestry(env, token, parents);
  if (ancestry.allowed !== true) {
    return { verified: false, ...ancestry };
  }

  if (locator.expected_name && data.name !== locator.expected_name) {
    return { verified: false, reason: "drive_name_mismatch", observed_name: data.name };
  }
  if (locator.expected_md5 && data.md5Checksum !== locator.expected_md5) {
    return { verified: false, reason: "drive_md5_mismatch", observed_md5: data.md5Checksum };
  }
  return {
    verified: true,
    surface: "GOOGLE_DRIVE",
    handoff_root_id: root,
    ancestry,
    ...data,
  };
}

export async function verifyHandoffLocator(env: Env, locator: HandoffLocator) {
  if (locator.surface === "GITHUB") return verifyGithubLocator(env, locator);
  return verifyGoogleDriveLocator(env, locator);
}

export async function githubEnforcementStatus(env: Env) {
  const repository = env.ENTERPRISE_MATH_REPOSITORY || "awdawmip/enterprise-math";
  const headers = await githubHeaders(env);
  const [branchResponse, rulesetResponse] = await Promise.all([
    fetch(`https://api.github.com/repos/${repository}/branches/main`, { headers }),
    fetch(`https://api.github.com/repos/${repository}/rulesets`, { headers }),
  ]);
  if (!branchResponse.ok || !rulesetResponse.ok) {
    return {
      verified: false,
      repository,
      identity_mode: githubIdentityMode(env),
      branch_status: branchResponse.status,
      rulesets_status: rulesetResponse.status,
    };
  }
  const branch = (await branchResponse.json()) as GithubBranchResponse;
  const rulesets = (await rulesetResponse.json()) as Array<Record<string, unknown>>;
  return {
    verified: true,
    repository,
    identity_mode: githubIdentityMode(env),
    main_protected: branch.protected === true,
    protection_enabled: branch.protection?.enabled === true,
    required_status_checks: branch.protection?.required_status_checks ?? null,
    ruleset_count: Array.isArray(rulesets) ? rulesets.length : null,
    rulesets,
  };
}
