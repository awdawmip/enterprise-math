import fs from "node:fs";

const command = process.argv[2];
const statePath = process.argv[3] || "access-ci-identity.json";
const accountId = process.env.CLOUDFLARE_ACCOUNT_ID;
const apiToken = process.env.CLOUDFLARE_API_TOKEN;
const policyName =
  process.env.ACCESS_CI_POLICY_NAME || "EnterpriseMath Supervisor CI Service Auth";
const tokenPrefix =
  process.env.ACCESS_CI_TOKEN_PREFIX || "enterprise-math-supervisor-canary-";
const mcpDomain = process.env.ACCESS_MCP_DOMAIN || "181131.xyz/em/mcp";

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function writeState(value) {
  fs.writeFileSync(statePath, `${JSON.stringify(value, null, 2)}\n`, "utf8");
}

async function api(path, init = {}) {
  assert(accountId && apiToken, "Cloudflare account authorization is required");
  const response = await fetch(
    `https://api.cloudflare.com/client/v4/accounts/${accountId}/access${path}`,
    {
      ...init,
      headers: {
        Authorization: `Bearer ${apiToken}`,
        "Content-Type": "application/json",
        Accept: "application/json",
        ...(init.headers || {}),
      },
    },
  );
  const text = await response.text();
  let body = {};
  try {
    body = text ? JSON.parse(text) : {};
  } catch {
    body = { raw: text };
  }
  if (!response.ok || body.success === false) {
    throw new Error(
      `Cloudflare Access ${init.method || "GET"} ${path} failed status=${response.status}: ${JSON.stringify(body)}`,
    );
  }
  return body;
}

function policyTokenIds(policy) {
  return new Set(
    (policy.include || [])
      .map((entry) => entry?.service_token?.token_id)
      .filter((value) => typeof value === "string" && value),
  );
}

function policyPayload(policy, tokenIds) {
  const retainedNonToken = (policy.include || []).filter(
    (entry) => !entry?.service_token?.token_id,
  );
  return {
    name: policy.name || policyName,
    decision: policy.decision || "non_identity",
    include: [
      ...retainedNonToken,
      ...[...tokenIds].sort().map((tokenId) => ({
        service_token: { token_id: tokenId },
      })),
    ],
    exclude: Array.isArray(policy.exclude) ? policy.exclude : [],
    require: Array.isArray(policy.require) ? policy.require : [],
  };
}

async function create() {
  if (!accountId || !apiToken) {
    writeState({
      enabled: false,
      reason: "cloudflare_authorization_missing",
      auth_target: "UNKNOWN",
    });
    return;
  }

  const apps = await api("/apps?per_page=100");
  const matches = (apps.result || []).filter((app) => app.domain === mcpDomain);
  if (matches.length === 0) {
    writeState({
      enabled: false,
      reason: "access_app_not_present",
      auth_target: "BOOTSTRAP_BEARER",
    });
    return;
  }
  assert(matches.length === 1, `ACCESS_MCP_APP_AMBIGUOUS count=${matches.length}`);

  const policies = await api("/policies?per_page=100");
  const policyMatches = (policies.result || []).filter(
    (policy) => policy.name === policyName,
  );
  assert(
    policyMatches.length === 1,
    `ACCESS_CI_REUSABLE_POLICY_COUNT_INVALID count=${policyMatches.length}`,
  );
  const policy = policyMatches[0];

  const tokenName = `${tokenPrefix}${process.env.GITHUB_RUN_ID || Date.now()}-${process.env.GITHUB_RUN_ATTEMPT || 1}`;
  const created = await api("/service_tokens", {
    method: "POST",
    body: JSON.stringify({ name: tokenName, duration: "1h", enabled: true }),
  });
  const token = created.result || {};
  assert(
    token.id && token.client_id && token.client_secret,
    "ACCESS_EPHEMERAL_SERVICE_TOKEN_CREATION_FAILED",
  );

  try {
    const tokenIds = policyTokenIds(policy);
    tokenIds.add(token.id);
    await api(`/policies/${policy.id}`, {
      method: "PUT",
      body: JSON.stringify(policyPayload(policy, tokenIds)),
    });
  } catch (error) {
    await api(`/service_tokens/${token.id}`, {
      method: "PUT",
      body: JSON.stringify({ name: tokenName, enabled: false }),
    }).catch(() => {});
    throw error;
  }

  writeState({
    enabled: true,
    auth_target: "CLOUDFLARE_ACCESS",
    app_id: matches[0].id,
    app_aud: matches[0].aud,
    policy_id: policy.id,
    token_id: token.id,
    token_name: tokenName,
    client_id: token.client_id,
    client_secret: token.client_secret,
  });
}

async function revoke() {
  if (!fs.existsSync(statePath)) return;
  const state = JSON.parse(fs.readFileSync(statePath, "utf8"));
  if (state.enabled !== true || !state.token_id) return;

  const policies = await api("/policies?per_page=100");
  const policy = (policies.result || []).find(
    (candidate) => candidate.id === state.policy_id,
  );
  if (policy) {
    const tokenIds = policyTokenIds(policy);
    tokenIds.delete(state.token_id);
    await api(`/policies/${policy.id}`, {
      method: "PUT",
      body: JSON.stringify(policyPayload(policy, tokenIds)),
    });
  }

  await api(`/service_tokens/${state.token_id}`, {
    method: "PUT",
    body: JSON.stringify({ name: state.token_name, enabled: false }),
  });
  const verified = await api(`/service_tokens/${state.token_id}`);
  assert(
    verified.result?.enabled === false,
    "ACCESS_EPHEMERAL_TOKEN_REVOKE_NOT_VERIFIED",
  );

  let deleted = false;
  try {
    await api(`/service_tokens/${state.token_id}`, { method: "DELETE" });
    deleted = true;
  } catch {
    deleted = false;
  }
  writeState({ ...state, revoked: true, deleted });
}

if (command === "create") {
  await create();
} else if (command === "revoke") {
  await revoke();
} else {
  throw new Error("usage: node access-ci-identity.mjs <create|revoke> [state-path]");
}
