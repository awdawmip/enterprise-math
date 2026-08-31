import type { Env } from "./types";

const encoder = new TextEncoder();
const ACCESS_JWKS_CACHE_MS = 5 * 60 * 1000;

type AccessJwksCache = {
  team_domain: string;
  expires_at_ms: number;
  keys: JsonWebKey[];
};
let accessJwksCache: AccessJwksCache | undefined;

function toHex(bytes: ArrayBuffer): string {
  return [...new Uint8Array(bytes)]
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

function base64UrlDecode(value: string): Uint8Array {
  const padded = value.replace(/-/g, "+").replace(/_/g, "/") + "===".slice((value.length + 3) % 4);
  const binary = atob(padded);
  const bytes = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i += 1) bytes[i] = binary.charCodeAt(i);
  return bytes;
}

function decodeJwtJson(value: string): Record<string, unknown> {
  const bytes = base64UrlDecode(value);
  return JSON.parse(new TextDecoder().decode(bytes)) as Record<string, unknown>;
}

function normalizeTeamDomain(value: string): string {
  const url = new URL(value);
  if (url.protocol !== "https:" || url.pathname !== "/" || url.search || url.hash) {
    throw new Error("ACCESS_TEAM_DOMAIN must be an HTTPS origin");
  }
  return url.origin;
}

async function fetchAccessKeys(teamDomain: string, force = false): Promise<JsonWebKey[]> {
  const now = Date.now();
  if (
    !force &&
    accessJwksCache?.team_domain === teamDomain &&
    accessJwksCache.expires_at_ms > now
  ) {
    return accessJwksCache.keys;
  }

  const response = await fetch(`${teamDomain}/cdn-cgi/access/certs`, {
    headers: { accept: "application/json" },
  });
  if (!response.ok) throw new Error(`Access JWKS fetch failed status=${response.status}`);
  const data = (await response.json()) as { keys?: JsonWebKey[] };
  if (!Array.isArray(data.keys) || data.keys.length === 0) {
    throw new Error("Access JWKS response contains no keys");
  }
  accessJwksCache = {
    team_domain: teamDomain,
    expires_at_ms: now + ACCESS_JWKS_CACHE_MS,
    keys: data.keys,
  };
  return data.keys;
}

function audienceMatches(value: unknown, expected: string): boolean {
  if (typeof value === "string") return value === expected;
  return Array.isArray(value) && value.some((item) => item === expected);
}

function accessPrincipalIsValid(payload: Record<string, unknown>): boolean {
  // Human/IdP application tokens carry a stable non-empty subject.
  if (typeof payload.sub === "string" && payload.sub.length > 0) return true;

  // Cloudflare documents service-token application JWTs with sub="" and the
  // service-token Client ID in common_name. Accept that exact machine shape,
  // but do not accept anonymous empty-subject JWTs without common_name.
  return (
    payload.sub === "" &&
    typeof payload.common_name === "string" &&
    payload.common_name.length > 0
  );
}

async function verifyAccessJwt(token: string, env: Env): Promise<Record<string, unknown>> {
  const teamDomain = normalizeTeamDomain(env.ACCESS_TEAM_DOMAIN ?? "");
  const audience = env.ACCESS_AUD?.trim();
  if (!audience) throw new Error("ACCESS_AUD is missing");

  const parts = token.split(".");
  if (parts.length !== 3) throw new Error("malformed Access JWT");
  const header = decodeJwtJson(parts[0]);
  const payload = decodeJwtJson(parts[1]);
  if (header.alg !== "RS256" || typeof header.kid !== "string") {
    throw new Error("unsupported Access JWT header");
  }

  let keys = await fetchAccessKeys(teamDomain);
  let jwk = keys.find((key) => key.kid === header.kid);
  if (!jwk) {
    keys = await fetchAccessKeys(teamDomain, true);
    jwk = keys.find((key) => key.kid === header.kid);
  }
  if (!jwk) throw new Error("Access signing key not found");

  const key = await crypto.subtle.importKey(
    "jwk",
    jwk,
    { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" },
    false,
    ["verify"],
  );
  const signatureOk = await crypto.subtle.verify(
    "RSASSA-PKCS1-v1_5",
    key,
    base64UrlDecode(parts[2]),
    encoder.encode(`${parts[0]}.${parts[1]}`),
  );
  if (!signatureOk) throw new Error("invalid Access JWT signature");

  const now = Math.floor(Date.now() / 1000);
  const skew = 60;
  if (payload.iss !== teamDomain) throw new Error("Access JWT issuer mismatch");
  if (!audienceMatches(payload.aud, audience)) throw new Error("Access JWT audience mismatch");
  if (typeof payload.exp !== "number" || payload.exp < now - skew) {
    throw new Error("Access JWT expired");
  }
  if (typeof payload.nbf === "number" && payload.nbf > now + skew) {
    throw new Error("Access JWT not yet valid");
  }
  if (typeof payload.iat === "number" && payload.iat > now + skew) {
    throw new Error("Access JWT issued in the future");
  }
  if (!accessPrincipalIsValid(payload)) {
    throw new Error("Access JWT has no valid user or service-token principal");
  }
  return payload;
}

export function mcpAuthMode(env: Env): "CLOUDFLARE_ACCESS" | "BOOTSTRAP_BEARER" | "MISCONFIGURED" {
  const team = Boolean(env.ACCESS_TEAM_DOMAIN?.trim());
  const aud = Boolean(env.ACCESS_AUD?.trim());
  if (team !== aud) return "MISCONFIGURED";
  return team ? "CLOUDFLARE_ACCESS" : "BOOTSTRAP_BEARER";
}

export async function timingSafeEqual(a: string, b: string): Promise<boolean> {
  const [da, db] = await Promise.all([
    crypto.subtle.digest("SHA-256", encoder.encode(a)),
    crypto.subtle.digest("SHA-256", encoder.encode(b)),
  ]);
  const aa = new Uint8Array(da);
  const bb = new Uint8Array(db);
  let diff = 0;
  for (let i = 0; i < aa.length; i++) diff |= aa[i] ^ bb[i];
  return diff === 0;
}

export async function requireBearer(request: Request, env: Env): Promise<Response | null> {
  if (!env.SUPERVISOR_API_TOKEN) {
    return new Response("Supervisor auth is not configured", { status: 503 });
  }
  const header = request.headers.get("authorization") ?? "";
  const prefix = "Bearer ";
  if (!header.startsWith(prefix)) {
    return new Response("Unauthorized", {
      status: 401,
      headers: { "WWW-Authenticate": 'Bearer realm="enterprise-math-supervisor"' },
    });
  }
  const supplied = header.slice(prefix.length);
  if (!(await timingSafeEqual(supplied, env.SUPERVISOR_API_TOKEN))) {
    return new Response("Unauthorized", { status: 401 });
  }
  return null;
}

export async function requireMcpAuth(request: Request, env: Env): Promise<Response | null> {
  const mode = mcpAuthMode(env);
  if (mode === "MISCONFIGURED") {
    return new Response("Cloudflare Access authentication is partially configured", { status: 503 });
  }
  if (mode === "BOOTSTRAP_BEARER") return requireBearer(request, env);

  const assertion = request.headers.get("cf-access-jwt-assertion") ?? "";
  if (!assertion) return new Response("Missing Cloudflare Access assertion", { status: 401 });
  try {
    await verifyAccessJwt(assertion, env);
    return null;
  } catch (error) {
    console.error("Cloudflare Access assertion rejected", error);
    return new Response("Invalid Cloudflare Access assertion", { status: 401 });
  }
}

export async function verifyGithubWebhook(
  request: Request,
  secret: string | undefined,
): Promise<{ ok: boolean; body: ArrayBuffer }> {
  const body = await request.arrayBuffer();
  if (!secret) return { ok: false, body };
  const sig = request.headers.get("x-hub-signature-256") ?? "";
  if (!sig.startsWith("sha256=")) return { ok: false, body };

  const key = await crypto.subtle.importKey(
    "raw",
    encoder.encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const digest = await crypto.subtle.sign("HMAC", key, body);
  const expected = `sha256=${toHex(digest)}`;
  return { ok: await timingSafeEqual(sig, expected), body };
}
