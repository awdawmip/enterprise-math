/* D25 author-side exact certificate runner, 2026-11-04.
 * Mathematics: universal normalized valuation-2 port of quartic 2304 model.
 * Does not compute the frozen native H0/B0 benchmark or grant Source admission.
 * Run with: node d25_quartic_val2_universal_port_checker_20261104.mjs
 */
"use strict";

function primesUpTo(limit) {
  const flags = new Uint8Array(limit + 1);
  flags.fill(1, 2);
  for (let p = 2; p * p <= limit; p++) {
    if (flags[p]) {
      for (let k = p * p; k <= limit; k += p) flags[k] = 0;
    }
  }
  return Array.from({ length: limit - 1 }, (_, i) => i + 2)
    .filter(p => flags[p]);
}

function modInvTable(p, last) {
  const inv = new Int32Array(last + 1);
  inv[1] = 1;
  for (let i = 2; i <= last; ++i) {
    if (i >= p) throw Error("Attempt to invert a multiple of p");
    inv[i] = (p - Math.floor(p / i) * inv[p % i] % p) % p;
  }
  return inv;
}

function normalizedPort(p) {
  const N = Math.floor((p + 1) / 4);
  const M = Math.max(2 * N + 1, 18 % p, 72 % p);
  const inv = modInvTable(p, M);
  let d = inv[72 % p]; // d_1 = 1/72 (mod p)
  let S = 0;
  for (let n = 1; n <= N; ++n) {
    S = (S + (8 * n - 3) * d) % p;
    if (n < N) {
      // d_(n+1)/d_n = n*(16n²-1)/(18*(2n+1)³).
      let ratio = n * (16 * n * n - 1) % p;
      ratio = ratio * inv[18 % p] % p;
      const q = inv[2 * n + 1];
      ratio = ratio * q % p;
      ratio = ratio * q % p;
      ratio = ratio * q % p;
      d = d * ratio % p;
    }
  }
  return S;
}

function inverseBig(a, mod) {
  let [r, b, t, u] = [mod, ((a % mod) + mod) % mod, 0n, 1n];
  while (b) {
    const q = r / b;
    [r, b] = [b, r - q * b];
    [t, u] = [u, t - q * u];
  }
  if (r !== 1n) throw Error("Non-unit denominator");
  return (t % mod + mod) % mod;
}

function independentOriginalQuarticCheck(p) {
  const P = BigInt(p);
  const mod = P ** 3n;
  const h = (p - 1) / 2;
  const N = Math.floor((p + 1) / 4);
  let b = 1n; // original b_0, modulo p^3
  let d = inverseBig(72n, P); // normalized universal d_1
  let highPort = 0n;
  let pointwiseChecks = 0;
  let first = null, last = null;

  for (let k = 0; k <= h + N; ++k) {
    if (k > h) {
      const n = k - h;
      const actual = (b / (P * P)) % P;
      const expected = (2n * d) % P;
      if (actual !== expected) {
        throw Error(`p=${p}, n=${n}: original coefficient != normalized term`);
      }
      ++pointwiseChecks;
      const term = BigInt(8 * k + 1) * b % mod;
      highPort = (highPort + term) % mod;
      if (n === 1) first = Number(actual);
      if (n === N) last = Number(actual);
      if (n < N) {
        const j = BigInt(n);
        const denom = 18n * (2n * j + 1n) ** 3n;
        d = d * j * (16n * j * j - 1n) % P;
        d = d * inverseBig(denom % P, P) % P;
      }
    }

    if (k < h + N) {
      const t = BigInt(k);
      const numer = (4n * t + 1n) * (4n * t + 2n) *
                    (4n * t + 3n) * (4n * t + 4n);
      const denom = 2304n * (t + 1n) ** 4n;
      b = b * (numer % mod) % mod;
      b = b * inverseBig(denom % mod, mod) % mod;
    }
  }

  if (highPort !== 0n) throw Error(`p=${p}: quartic high band nonzero`);
  return { p, N, pointwise_checks: pointwiseChecks,
           first_normalized: first, last_normalized: last,
           valuation_two_port_mod_p3: String(highPort) };
}

function main() {
  const primes = primesUpTo(10000).filter(p => p >= 5);
  const failed = primes.filter(p => normalizedPort(p) !== 0);
  if (failed.length) throw Error("Truncated sum discrepancy: " + failed.join(","));

  const samples = [5, 7, 11, 13, 19, 37, 373]
    .map(independentOriginalQuarticCheck);

  const result = {
    scope: "finite exact tests only; no all-prime proof of S_N=0",
    primes_5_to_10000: primes.length,
    primes_1_mod_4: primes.filter(p => p % 4 === 1).length,
    primes_3_mod_4: primes.filter(p => p % 4 === 3).length,
    normalized_port_failures: failed.length,
    direct_original_samples: samples,
    mathematical_theorem: "b_(h+n)/p^2 = 2*d_n (mod p), proved algebraically",
    conjecture: "S_floor((p+1)/4) = 0 (mod p), tested only"
  };
  process.stdout.write(JSON.stringify(result, null, 2) + "\n");
}

main();
