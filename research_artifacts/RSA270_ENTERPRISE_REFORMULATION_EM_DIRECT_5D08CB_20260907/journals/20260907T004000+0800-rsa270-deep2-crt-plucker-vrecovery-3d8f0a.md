# RSA-270：深入研究第 2 轮——根轨迹 CRT 视图、双 ℓ Plücker 双曲线、V 函数射线系数恢复

Progress-Event-ID: `rsa270-deep2-crt-plucker-vrecovery-3d8f0a`
At: `2026-09-07T00:40+08:00`
Scope: `enterprise-math / RSA-270 / deep research round 2`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 2c7e9f; P000 assumed`
Kind: `PROGRESS / EXACT THEOREMS`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Deep-research round 2. No factor obtained.

### 1. CRT joint view of the root trajectory (exact, verified)

For all primes `l`, the BRC collapse root satisfies

`y(l) mod p = +-q` (CONSTANT two-point set),  `y(l) mod q = +-l*p` (varies with `l mod q`).

Verified for 4 semiprimes x all primes <= 31. (Correction of the round-1 Next guess: the q-coordinate is not constant; it traces `+-p * (primes mod q)`.)

### 2. Two-l Plucker hyperbola (exact, verified)

The x-prime endpoint family satisfies the concurrent Plucker relation in its two-direction form:

`(x(l1) - x(l2)) * (l1*x(l2) - l2*x(l1)) = (l1-l2)^2 * N`,

for ALL prime pairs `l1 != l2`. Verified exhaustively for 4 semiprimes x all prime pairs <= 31.

### 3. V-function ray-coefficient recovery (constructive, verified)

The root trajectory is exactly `V_{p,q}(l) = |p*l - q|` over primes; its two rays `q - p*l` (left of the vertex `q/p`) and `p*l - q` (right) have **ray coefficients (p, q) = the factors themselves**. Recovery from the y-sequence: p = |Δy|/Δl from consecutive same-side primes; q = p*l ± y. Verified: `N=15 -> (3,5)`, `35 -> (5,7)`, `143 -> (11,13)`, `391 -> (17,23)` — all exact. This is the deepest form of the collapse<->factor relation: the factors ARE the V-function's ray coefficients; the vertex `q/p` is the factor ratio (prior band -> `l=2` attains the minimum root).

## Artifacts

- Script: `rsa270_deep2.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-06/20260906T235500+0800-rsa270-deep1-two-prime-root-modp-null-2c7e9f.md`.

## Next

1. The V-function is the terminal form of the collapse<->factor relation; the remaining deep question is whether ANY of its layer-1 (N-only) shadows — e.g. the x0-sequence gaps, the rho-sequence order statistics — carry a detectable vertex signal (round-1 null says no for first-order; test second-order statistics next).
2. Package the V-function + Plucker + CRT checks into the SG4 verifier as layer-2 certificates.
