# RSA-270：bracket 公共零点的 gcd 恒等式与零点集分类（第 2 轮捷径猎取）

Progress-Event-ID: `rsa270-zero-set-gcd-classification-3c9b7d`
At: `2026-09-06T16:15+08:00`
Scope: `enterprise-math / RSA-270 / shortcut hunt (non-exhaustive, exact-identity route)`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 5d8a2c; P000 assumed`
Kind: `PROGRESS / EXACT IDENTITY / CLASSIFICATION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Round 2 of the shortcut hunt. No factor obtained.

### 1. gcd identity for the bracket's common zeros (exact, verified)

From `B(u) = u^((S-N-1)/2)(1-u^(N+1)) + (1-u^S)`, the "both-terms-vanish" part of the zero set is `{m : m | gcd(N+1, S)}`. New exact identity:

`gcd(N+1, S) = gcd(p^2 - 1, p+q) = gcd(q^2 - 1, p+q)`

(proof: `N+1 = pq+1`, reduce `pq+1` mod `p+q` via `q = -p`). Verified on 8 random semiprimes (PASS). For RSA-270 this gives `8 | gcd(N+1, S)` (from `S = 0 mod 8`, `N+1 = 56 mod 72`); the odd part of the gcd remains S-hidden, consistent with the closed-route ledger.

### 2. Zero-set Z(N,S) classification (methodology note + result)

For `m | 144` the value `B(w_m)` is determined by the `S mod 144` class; for `m !| 144` a single class representative is **not** valid (S mod 2m needs the full admissible class set), and the earlier representative-based Z-vectors contained exactly such artifacts at `m in {27,32,54,59,72?,108,118,152,160,177}` — the artifacts at `m !| 144` are discarded here.

Class-determined result (admissible classes `S mod 144 in {16,88}`, prior-consistent):

- both classes: zeros at `{3,4,6,8,9,12,18,36}` (the forced family of 5d8a2c);
- distinguishing moduli among `m | 144`, `m <= 200`: **`m = 24` and `m = 72`** — `B(w_m) = 0` iff `S = 88 mod 144`;
- so the zero-set over divisors of 144 resolves the two admissible `S mod 144` classes — exactly the same resolution as the torsion ladder at `m=24` (S mod 48 up to sign). No new channel.

### 3. Zero-density sweep

For each `m <= 144` (selected set), the fraction of admissible `S mod 2m` classes with `B(w_m) = 0` is 0 or `O(1/#classes)` — no structural spike beyond the divisors of 72. Table recorded in script; e.g. `m=24: 1/2`, `m=48: 1/4`, `m=96: 1/8`, `m=144: 1/4`, `m=15: 1/2` (residue coincidence), rest 0 or 1/n.

### Status

The zero-set observable family is equivalent to the phi(N)-mod ladder (9f3b12): its class-determined content is exactly `S mod 144` at 2-class granularity plus the forced family. RSA-270 factorization remains **not achieved**; the standing wall (sub-`O(sqrt(N))` recovery of the single scalar `S = sigma(N) - N - 1` from N alone) persists unchanged across 5d8a2c and all prior rounds. No exhaustive or traditional algorithm was used.

## Artifacts

- Script: `rsa270_zero_set.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-06/20260906T153000+0800-rsa270-closed-form-zero-criterion-5d8a2c.md`.

## Next

1. Remaining exact-identity candidate: the derivative ladder at torsion points (`W'_s(w_m)` closed form) — expected to again land in the `S mod 2m` class; if confirmed, the shortcut surface is fully enumerated and the only forward step is an N-only sub-`O(sqrt(N))` oracle for `S mod` larger moduli, which is exactly the QR/`phi(N)`-mod hardness boundary.
2. Prepare the blocking assessment: the same condition (no known shortcut to cheaply compute `S`; RSA-270 unfactored; wall identical across journals 68d4a1..5d8a2c) has now persisted for the current goal's consecutive rounds.
