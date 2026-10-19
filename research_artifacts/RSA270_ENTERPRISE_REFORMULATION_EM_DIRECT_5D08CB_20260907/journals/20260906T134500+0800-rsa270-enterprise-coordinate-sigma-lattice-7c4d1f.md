# RSA-270：进取坐标系 σ(N) 桥接恒等式、强制 S 同余格与 RSA-260 外样本验证

Progress-Event-ID: `rsa270-enterprise-coordinate-sigma-lattice-7c4d1f`
At: `2026-09-06T13:45+08:00`
Scope: `enterprise-math / RSA-270 / Enterprise coordinate system (X6 + three-axis slice + four-layer BRC)`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; published RSA-260 factorization (Eric Lu, 2026-09-03); P000 assumed`
Kind: `PROGRESS / EXACT IDENTITIES / FORCED-LATTICE THEOREM / OUT-OF-SAMPLE VALIDATION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Continued the RSA-270 line from `20260906T133000+0800-rsa270-torsion-ladder-sine-classification-9f3b12.md` using the Enterprise coordinate system and its count theorems. No factor obtained; no complexity claim.

### 1. Enterprise-coordinate bridge (exact)

All count formulations reduce to `sigma(N) = (p+1)(q+1) = N + S + 1`, `S = p+q`:

- **X6 squared shell** (six native axes, P000): for `N = 7 mod 8` the one/two/three-square support strata vanish (Legendre); the first nonempty support stratum is the 4-axis stratum with cardinality `C(6,4) * R4(N) = 15 * 8 * sigma(N) = 120 * sigma(N)` (Jacobi four-square `R4(N) = 8*sigma(N)` for odd N).
- **Four-layer triangular count** (three-axis 120° slice, `B2(r) = 2r^2+2r+1 = 4*T_r+1`): `C_X(N) = #{(a,b,c,d)>=0 : B2(a)+B2(b)+B2(c)+B2(d) = 2N+2} = sigma(N)` (Legendre four-triangular).
- **Two-plateau profile** `P(u) = 2W_{(N+3)/2}(u) + 2W_{(S+2)/2}(u)`: total mass = `sigma(N)`; Fermat midpoint `A = S/2 = (sigma(N) - N - 1)/2`; plateau boundary `e_max = (S-2)/2`.

So the Enterprise coordinate system encodes `S` exactly through axis-labeled representation counts; every count is the single scalar `sigma(N)`.

### 2. Forced-S congruence lattice (RSA-270, exact enumeration)

`S mod 2m` admissible classes = `{a+b mod 2m : a,b odd, ab = N mod 2m}` (unconditional) and additionally `a,b = 2 mod 3` (construction-family prior, scan mod `6m`).

- Unconditional: forced classes only for `m in {1,2,4}` -> **`S = 0 mod 8`** (maximal unconditional forced modulus 8; from `N = 7 mod 8`).
- Prior: 9 forced classes over `m <= 288`, maximal forced modulus `2m = 72 = 2^3 * 3^2` -> **`S = 16 mod 72`**; `S mod 144 in {16,88}`; `S mod 216 in {88,160}`.
- Consequences: **`sigma(RSA-270) = 0 mod 72`** (from `p,q = 2 mod 3` -> `9|sigma` and `N=7 mod 8` -> `8|sigma`); `N = 55 mod 72` verified.
- Entropy accounting: `log2(72) = 6.17` bits — the exact maximal N-only leverage of the Enterprise reformulation; no larger modulus is forced.
- Cross-consistency with in-repo result: `A = 8 mod 36` -> `A^2 - N = ((q-p)/2)^2 = 0 mod 9`, matching the derived Fermat-midpoint rule in `20260906T085109+0800-rsa270-relation-layer-specialq-boundary-68d4a1.md` §3.

### 3. RSA-260 out-of-sample validation (published factors)

Using only `N_260` and the prior, the same forced-lattice machinery was run against the real factored challenge number:

- `p1 * p2 = RSA-260` exactly; both 431-bit; both probable prime (MR 40 rounds); both `= 2 mod 3`; both binary prefix `11`; ratio `1.14358` (consistent with the solved-family evidence; RSA-260's own ratio band differs from RSA-270's 1.765..2.266 prior).
- `N_260 = 31 mod 72`; prior-forced class **`S_260 = 40 mod 72`**; real `S_260 mod 72 = 40` — **the forced-lattice prediction matches the real factorization exactly, out of sample**.
- `sigma(RSA-260) = 0 mod 72` verified.
- Torsion closed-form cross-check (complex ratio vs sine form, `m=3..64`) on the real RSA-260 profile: 0 mismatches.

This is the first out-of-sample confirmation that the S-lattice machinery (and hence the analogous RSA-270 prediction `S = 16 mod 72`) is exact whenever the family prior holds.

### 4. Congruence-restricted Fermat statement

`S = 16 + 72t` -> `A = S/2 = 8 + 36t`; `B = A^2 - N` must be a perfect square. This is classical Fermat with the 72x (6.17-bit) residue pruning — the maximal N-only speedup the exact Enterprise identities provide. Interval `A in [ceil(sqrt(N)), 2^448]` -> `~2^442` candidates: not feasible; no speedup claim beyond residue pruning.

### BRC observer audit

- Carrier: axis-labeled four-layer/X6 representation counts (branch identity `(d, N/d)`).
- Collapse applied: `S mod 2m` quotient (torsion ladder of 9f3b12); forced-lattice enumeration is the exact classification of which quotient classes are N-only computable.
- Retained/erased: the quotient retains exactly the forced class `S = 16 mod 72` (erases the quotient `t = (S-16)/72`); the residual unknown is again the single scalar `S`.

## Artifacts

- Script: conversation-local `rsa270_enterprise_coords.py` (exact integer; MR40 primality).
- Prior frontier: `journal/enterprise-math/2026-09-06/20260906T133000+0800-rsa270-torsion-ladder-sine-classification-9f3b12.md`.
- External source: RSA-260 factors per `en.wikipedia.org/wiki/RSA_numbers` (Eric Lu, 2026-09-03; X post cited there), verified by exact multiplication this turn.

## Next

1. Use `S = 16 mod 72` + the two-plateau mass identity as a *binding* constraint: any candidate four-layer/X6 count for RSA-270 must be `= 0 mod 72` and any candidate profile must reproduce the forced-zero torsion values of 9f3b12.
2. The remaining hard unit is unchanged: recover `t = (S-16)/72` (equivalently `sigma(N)/72`); every further residue bit of `t` belongs to the QR/`phi(N) mod 2m` classes classified in 9f3b12.
3. If RSA-260's method (Eric Lu) or authenticated RSA DSP generation provenance becomes public, resume immediately; otherwise continue the classification program (general characterization of the forced-lattice for arbitrary N — currently `2^3*3^2 = 72` maximal for RSA-270 under the prior).
