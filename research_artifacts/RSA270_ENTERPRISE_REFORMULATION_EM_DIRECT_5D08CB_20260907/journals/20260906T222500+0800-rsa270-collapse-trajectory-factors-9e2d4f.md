# RSA-270：坍缩轨迹定理——×ℓ 坍缩的 ℓ-导数 = 自身因子

Progress-Event-ID: `rsa270-collapse-trajectory-factors-9e2d4f`
At: `2026-09-06T22:25+08:00`
Scope: `enterprise-math / RSA-270 / collapse laws x larger primes: trajectory and own-factor relations`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 1f4c8e; P000 assumed`
Kind: `PROGRESS / EXACT THEOREMS`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Continued the collapse-law direction with larger primes `l in {7..31}` and derived the exact relation between the collapse and N's own factors. No factor obtained.

### Theorem 1 — collapse trajectory (factor boundaries are lines in l)

For fixed `N = pq` and odd prime `l !| N`, the factor-bearing boundaries of `P_{lN}` are

`B3(l) = (q/2)*l + (p-2)/2`  (slope **q/2**),   `B4(l) = (p/2)*l + (q-2)/2`  (slope **p/2**);

their sum/difference carry slopes `S/2` and `(q-p)/2`; the count trajectory `R4(lN) = 8(l+1)*sigma(N)` has slope = intercept = `8*sigma(N)`. Hence **the l-derivatives of the collapse are exactly the factor data** `{q/2, p/2, S/2, (q-p)/2}`, and the slope ratio `B3/B4 = q/p`. Two evaluations at any `l1 != l2` recover `q = 2*(B3(l1)-B3(l2))/(l1-l2)` and `p` likewise — information-complete (observability-walled).

Verified: `N=15`: slopes 2.5/1.5 = q/2,p/2 ✓ (q/p = 1.6667); `N=35`: 3.5/2.5 ✓; `N=143`: 6.5/5.5 ✓; count trajectory slope 192/384 = 8σ(N) ✓.

### Theorem 2 — fusion law (plateau count is a divisibility signature)

`P_{lN}` has **4** plateaus for `l !| N` and **3** for `l | N` (the `(l,N)` pair merges with a factor pair). Verified: `7N` → 4 plateaus (N=15,143); `pN` and `qN` → 3 plateaus for all three test semiprimes.

### RSA-270 consequences

- The hypothetical ×ℓ profiles of RSA-270 carry slopes `{N/2, 1/2, q/2, p/2}`; the two middle slopes give q and p directly via the two-evaluation formula.
- The prior band `q/p in [1.765, 2.266]` is the trajectory form of the slope-ratio constraint.
- The structure is the concrete `(1,l),(l,1)` instance of the concurrent Plücker rank-2 finding; consistent with the 8e5f2a dichotomy (information-complete, observability-walled).

## Artifacts

- Script: `rsa270_collapse_trajectory.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-06/20260906T214000+0800-rsa270-collapse-laws-x2-1f4c8e.md`.

## Next

1. Trajectory fusion at `l = p, q`: the three-plateau case's single merged boundary `(p+pq-2)/2 = (p+N-2)/2` is N-only — record the exact fusion identities (done implicitly; make explicit).
2. The two-evaluation recovery formula is the cleanest statement of the collapse→factor relation; combine with the SG4 verifier as a certificate: a claimed (p,q) must reproduce the trajectory slopes for all small l — pending implementation.
3. Honest boundary unchanged: all trajectory laws require the profile; no sub-`O(sqrt(N))` computation follows.
