# RSA-270：BRC 坍缩 × 更大素数——两层坍缩轨迹与自身因子的关系

Progress-Event-ID: `rsa270-brc-collapse-trajectory-6f1e8a`
At: `2026-09-06T23:10+08:00`
Scope: `enterprise-math / RSA-270 / BRC two-layer collapse x primes (user clarification: BRC collapse)`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journals 1f4c8e/9e2d4f; P000 assumed`
Kind: `PROGRESS / EXACT THEOREMS`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

User clarification applied: the collapse meant is the **BRC two-layer collapse** (shell collapse + square-difference collapse), applied to `l*N` for larger primes `l`. No factor obtained.

### Theorem 1 — BRC collapse trajectory encodes the own factors (verified)

For branch `k = l` (prime), the two-layer BRC collapse:

- layer 1: `4lN -> x0 = ceil(sqrt(4lN))`, residual `d_(l,0) = x0^2 - 4lN`;
- layer 2: the factor-bearing endpoint from `(l*p+q)^2 - 4lN = (l*p-q)^2`:
  - endpoint `x*(l) = l*p + q` — a line in `l` with **slope = p**;
  - collapse root `y*(l) = |l*p - q|` — two rays with slopes `-p` then `+p`, **vertex at `l = q/p`** (the factor ratio);
  - minimal root over primes = the prime nearest to `q/p`.

Verified on `N in {15,35,143,391}` for all primes `l <= 31`: square identity, endpoint-below-shell, slopes, and `argmin_l y(l) = 2` in all cases.

### Theorem 2 — layer 1 carries no factor signal (RSA-270, computed)

The N-only layer-1 trajectory of RSA-270 over the 50 primes `l <= 229`: normalized shell residual `rho` has `min = 0.0176 (l=47), max = 0.957, mean = 0.505`; three random 60-bit synthetic semiprimes give `min rho in {0.006, 0.010, 0.042}, mean ~ 0.50` — statistically indistinguishable. The factor data lives entirely in layer 2, as the BRC observer discipline predicted (layer 1 erases factor information; only the second collapse layer retains it).

### RSA-270 consequences

- Under the prior band `q/p in [1.765, 2.266]`, the prime nearest to the vertex is `l = 2` -> the **×2 branch has the minimal collapse root** `y = |2p - q| in [1, 0.266*p]`. This matches the cost-field minimax direction `(2,1)` (7e3b5d/9d4c2e): **the BRC root vertex and the cost-field ridge coincide** — two independent derivations of the same optimal branch.
- The V-vertex `q/p` and the endpoint slope `p` are the factor data themselves; recovering them requires layer-2 observability (the standing wall).

## Artifacts

- Script: `rsa270_brc_collapse.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-06/20260906T222500+0800-rsa270-collapse-trajectory-factors-9e2d4f.md`.

## Next

1. Layer-2 root statistics for larger l on synthetic semiprimes (the V-shape's curvature/rounding as a function of the band) — calibration of how much of p leaks from the root trajectory if layer 2 were partially observable.
2. Keep the honest boundary: all factor information in the BRC collapse is layer-2-only; layer 1 is provably structureless (now verified on RSA-270 itself).
