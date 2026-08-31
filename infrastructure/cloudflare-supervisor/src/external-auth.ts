import type { Env } from "./types";

const encoder = new TextEncoder();

type CachedToken = { token: string; expires_at_ms: number };
let googleTokenCache: CachedToken | undefined;
let githubTokenCache: CachedToken | undefined;

function base64Url(bytes: Uint8Array): string {
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}

function base64UrlJson(value: unknown): string {
  return base64Url(encoder.encode(JSON.stringify(value)));
}

function pemToDer(pem: string): ArrayBuffer {
  const normalized = pem.replace(/\\n/g, "\n").trim();
  const body = normalized
    .replace(/-----BEGIN PRIVATE KEY-----/g, "")
    .replace(/-----END PRIVATE KEY-----/g, "")
    .replace(/\s+/g, "");
  if (!body) throw new Error("empty PKCS8 private key");
  const binary = atob(body);
  const bytes = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i += 1) bytes[i] = binary.charCodeAt(i);
  return bytes.buffer;
}

async function signRs256(privateKeyPem: string, header: object, payload: object): Promise<string> {
  const unsigned = `${base64UrlJson(header)}.${base64UrlJson(payload)}`;
  const key = await crypto.subtle.importKey(
    "pkcs8",
    pemToDer(privateKeyPem),
    { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const signature = await crypto.subtle.sign(
    "RSASSA-PKCS1-v1_5",
    key,
    encoder.encode(unsigned),
  );
  return `${unsigned}.${base64Url(new Uint8Array(signature))}`;
}

export async function googleDriveAccessToken(env: Env): Promise<string | null> {
  if (env.GOOGLE_DRIVE_BEARER_TOKEN) return env.GOOGLE_DRIVE_BEARER_TOKEN;
  if (!env.GOOGLE_SERVICE_ACCOUNT_EMAIL || !env.GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY) return null;

  const now = Date.now();
  if (googleTokenCache && googleTokenCache.expires_at_ms - now > 120_000) {
    return googleTokenCache.token;
  }

  const nowSec = Math.floor(now / 1000);
  const assertion = await signRs256(
    env.GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY,
    { alg: "RS256", typ: "JWT" },
    {
      iss: env.GOOGLE_SERVICE_ACCOUNT_EMAIL,
      scope: "https://www.googleapis.com/auth/drive.metadata.readonly",
      aud: "https://oauth2.googleapis.com/token",
      iat: nowSec - 30,
      exp: nowSec + 3300,
    },
  );

  const response = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "urn:ietf:params:oauth:grant-type:jwt-bearer",
      assertion,
    }),
  });
  if (!response.ok) {
    throw new Error(`google service-account token exchange failed status=${response.status}`);
  }
  const data = (await response.json()) as { access_token?: string; expires_in?: number };
  if (!data.access_token) throw new Error("google token exchange returned no access_token");
  googleTokenCache = {
    token: data.access_token,
    expires_at_ms: now + Math.max(300, data.expires_in ?? 3600) * 1000,
  };
  return googleTokenCache.token;
}

export async function githubReadAccessToken(env: Env): Promise<string | null> {
  if (env.GITHUB_READ_TOKEN) return env.GITHUB_READ_TOKEN;
  if (!env.GITHUB_APP_ID || !env.GITHUB_APP_INSTALLATION_ID || !env.GITHUB_APP_PRIVATE_KEY) {
    return null;
  }

  const now = Date.now();
  if (githubTokenCache && githubTokenCache.expires_at_ms - now > 120_000) {
    return githubTokenCache.token;
  }

  const nowSec = Math.floor(now / 1000);
  const appJwt = await signRs256(
    env.GITHUB_APP_PRIVATE_KEY,
    { alg: "RS256", typ: "JWT" },
    {
      iat: nowSec - 60,
      exp: nowSec + 540,
      iss: env.GITHUB_APP_ID,
    },
  );

  const response = await fetch(
    `https://api.github.com/app/installations/${encodeURIComponent(env.GITHUB_APP_INSTALLATION_ID)}/access_tokens`,
    {
      method: "POST",
      headers: {
        Accept: "application/vnd.github+json",
        Authorization: `Bearer ${appJwt}`,
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "enterprise-math-supervisor",
      },
    },
  );
  if (!response.ok) {
    throw new Error(`github app installation token exchange failed status=${response.status}`);
  }
  const data = (await response.json()) as { token?: string; expires_at?: string };
  if (!data.token) throw new Error("github app token exchange returned no token");
  const expires = Date.parse(data.expires_at ?? "");
  githubTokenCache = {
    token: data.token,
    expires_at_ms: Number.isFinite(expires) ? expires : now + 50 * 60 * 1000,
  };
  return githubTokenCache.token;
}
