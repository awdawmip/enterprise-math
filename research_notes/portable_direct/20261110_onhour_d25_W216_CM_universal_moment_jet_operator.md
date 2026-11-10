# D25/W216 — universal local CM moment-jet operator (author-side exact theorem)

Date: 2026-11-10, Asia/Hong_Kong. Parent Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; **frozen scientific Source pin** `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923` (separate from maintenance). Classification: **AUTHOR_SIDE / EXACT ALGEBRAIC DERIVATION CONSUMING ACCEPTED CM0+SIMPLE / FINITE INTEGER VALIDATION / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN**.

## The precise unfinished unit

The preceding author-side finite Clausen-square note produced the ordinary signed first-jet identity `(W_p-p)/p² = tau+j²-R_p (mod p)` and mistakenly listed the proof of `J_p=0 (mod p)` in the two inert target classes as an open independent task. **That input already follows from the accepted original CM0 theorem** in `research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md`: `H_m(1/2)=0` for every `p ≡ 13,19 (mod 24)`, and `H'_m(1/2) != 0`. The earlier source-aligned note `20261026_onhour_d25_native_lift_source_port_identity.md` also consumed this fact. This unit retires that duplicate open action and develops the **previously missing entire higher-degree signed Newton-moment interface**, instead of re-proving CM0, SIMPLE, UR, the old cubic moment identity or the original Clausen cutoff.

## Theorem (all mod-p moment jets collapse to a single nonzero original carrier)

Fix a prime `p=6m+1 >=13` with `p mod 24 in {13,19}`, and work in `F_p`. Keep the **original** W216 coefficient and its original index `k`:

`A_k = binom(2k,k)^2 binom(3k,k)/216^k,  0 <= k < p`.

Let `M_j = sum_(k=0)^(p-1) binom(k,j) A_k` for `0<=j<p`; this is the signed-compatible indexed Newton moment (the coefficients may be summed with further signed weights; no positive-mass quotient is used). Define the **prime-independent rational** local coefficients by

```text
h_0=0, h_1=1,
(n+2)(n+1) h_(n+2) = -(n+1)h_(n+1)
                          +(4n²+2n+2/9)h_n,       n>=0;
c_j=sum_(a=1)^(j-1) h_a h_(j-a),  j>=2;
alpha_0=alpha_1=0; alpha_j=2^(2-j)c_j, j>=2.
```

For all `j=0,...,p-1` the `h` and `alpha` denominators generated up to index `j` are `p`-units. Then

```text
M_0=M_1=0 (mod p),   M_2 = (H'_m(1/2))²/4 != 0 (mod p),
M_j = alpha_j M_2 (mod p)       for EVERY 2<=j<p.           (T1)
```

Equivalently, for **every** function `P:{0,...,p-1}->F_p`, writing its unique Newton interpolation as `P(k)=sum_(j=0)^(p-1) Delta^j P(0) binom(k,j)`,

```text
sum_(k=0)^(p-1) A_k P(k)
  = M_2 * sum_(j=2)^(p-1) alpha_j Delta^j P(0)   (mod p). (T2)
```

This is a full `p`-index finite-field functional, not merely the earlier `M_2+2M_3=0` identity. Its universal coefficients are independent of the target prime; the only prime-specific nonzero amplitude is the accepted CM-simple derivative `M_2`.

### Proof

Set `H_m(z)=sum_(k=0)^m binom(m,k)binom(2m,k)z^k` over `F_p[z]`, and let `C_p(z)=sum_(k=0)^(p-1) ((1/2)_k(1/3)_k(2/3)_k)/(k!)³ z^k`. The exact formal Clausen identity plus the valuation cutoffs `(1/6)_(m+1)=0` and `(1/3)_(2m+1)=0` mod `p` give the **finite polynomial identity** `C_p(z)=H_m(z)^2` in `F_p[z]`, as already proved in `20261110_onhour_d25_W216_CM_finite_Clausen_exact_double_root.md`. Its specialization `C_p((1+x)/2)=sum_(k<p) A_k(1+x)^k=sum_j M_j x^j` is exact over `F_p[x]`.

The *terminating* `H_m={}_2F_1(-m,-2m;1;z)` satisfies the Gauss differential equation
`z(1-z)H''+[1+(3m-1)z]H'-2m² H=0`. Since `6m=-1 (mod p)`, reduction yields
`z(1-z)H''+(1-3z/2)H'-H/18=0`.
By accepted `CM0`, `H_m(1/2)=0`; by accepted `SIMPLE`, `d=H'_m(1/2)` is a unit. Put `t=z-1/2` and `H_m(1/2+t)=d sum_(n>=1) h_n t^n` through degree `p-1`. The local differential equation becomes
`(1/4-t²)H''+(1/4-3t/2)H'-H/18=0`.
Extracting `t^n` gives precisely the displayed recurrence. For `n<=p-3`, the factors `(n+1)(n+2)` are invertible, so the local Taylor jet up to `p-1` is uniquely fixed by `h_0=0,h_1=1`. Squaring at `z=(1+x)/2`, we get `M_j=d² 2^(-j)c_j` for `j>=2`; `M_2=d²/4`, proving (T1). Finite Newton interpolation in characteristic `p` then proves (T2), since `j!` is invertible for `j<p`. All manipulations preserve the original `k` and the exact `p`-unit domain. QED.

## Explicit new jets and a discriminating exceptional null moment

The uniform rational coefficient sequence through index eight is

| j | `alpha_j = M_j/M_2` in Fp |
|---:|---|
| 2 | `1` |
| 3 | `-1/2` (existing cubic moment relation, reused) |
| 4 | `287/432` |
| 5 | `-377/864` |
| 6 | `237133/466560` |
| 7 | `-348517/933120` |
| 8 | `78323947/188116992` |

The **new sixth moment** has a particularly useful exact special case: `237133 = 13*17*29*37`. For `p=37` (a genuine `13 mod 24` target), `M_6=0 mod37` while `M_2=21 != 0` and the original CM polynomial has degree `2m=12 >=6`; thus the sixth-moment cancellation is **not** a tautology of degree truncation. At `p=19` (the other target class), `M_6=11 !=0`. Neither class may be silently averaged.

**Existing p-block transfer interface, consumed within its exact scope.** Any `q_6 in p^6 Z_(p)` multiplying this original moment satisfies the precise **7th-digit** projection `q_6 M_6 = p^6 (q_6/p^6) * (237133/466560) M_2 (mod p^7)`; at `p=37`, that isolated port is `0 (mod p^7)` for every such `q_6`. Applied to the previously *author-proved, not yet admitted* degree-filtered W216 p-block Newton coefficient, this is a new immediate high-precision diagnostic. No assertion about the total `W_(p²)` or native Frobenius is inferred from the isolated port.

For every target prime, the finite degree `deg C_p <=2m` also forces the **scoped congruences** `alpha_j=0 mod p` for `2m<j<p`, with rational denominators interpreted in the appropriate `Z_(p)`. This yields an infinite family of explicit numerator-divisibility conditions indexed by `(p,j)`, entirely from the proved polynomial root and the local ODE.

## Exact integer verification and source provenance

Reproducible Python 3 standard-library code: `d25_w216_cm_universal_moment_jet_20261110.py` (companion). It generates original `A_k` by its exact ratio `A_(k+1)/A_k=(2k+1)(3k+1)(3k+2)/[36(k+1)^3]`; independently builds `H_m` from terminating binomials and its derivative; and generates the prime-independent `h_n` by exact rational arithmetic before reduction. **All 77 target primes `p<=2000`** passed the two class-root conditions and the `M_j/M_2` identities for `j=2,...,8`, yielding 539 moment equalities. A separate full Pascal/Newton array implementation checked **every `j=0,...,p-1`** at `p=13,19,37,43,61,109,373` (7 primes) using modular Gauss Taylor recurrence (not the finite rational generator).

Selected original carrier readouts:

| p | M2 | M3 | M4 | M5 | M6 |
|---:|---:|---:|---:|---:|---:|
| 13 | 10 | 8 | 12 | 0 | 0 |
| 19 | 1 | 9 | 11 | 13 | 11 |
| 37 | 21 | 8 | 25 | 20 | 0 |
| 373 | 273 | 50 | 13 | 35 | 163 |

Exact computation is validation of the finite arithmetic; the universal theorem follows from the preceding finite Clausen identity, accepted CM0/SIMPLE, and the Gauss coefficient recurrence. Previous CM0/SIMPLE accepted authorship is preserved, not recredited.

## Project/observer status and next actual frontiers

BRC resolution: `COMPOSE_APPLIED` (existing finite Clausen-square/CM polynomial + original indexed signed-compatible Newton-jet carrier). The population is all original `k<p`; preserved dimensions are `p`, original index, binomial moment degree, coefficient sign, full original `A_k` provenance, and the separate native H0/B0 boundary. The `M_2` projection is **certified only for mod-p polynomial-index observables**, not for mod `p^2` carries, the signed Clausen `R_p`, or an arbitrary native `[X]U` coefficient.

The frozen mother goal stays `Delta_p-R_p=0 (mod p)` for every target prime, or an exact same-object counterexample. **Next exact portable mathematical operation:** insert (T2)'s new `alpha_4,alpha_5,alpha_6` into the already author-proved seven-moment `W_(p²)` transfer, isolate each remaining `p^4,p^5,p^6` carry without borrowing lower-precision kernels, and test the resulting **signed** defect expression at `p=13,19,37,373`. Compare its first nonzero `M_2` term with the frozen original `(W_p-p)/p²` before proposing a LIFT theorem.

The **independent higher-priority native benchmark** remains the exact original H0/B0 divided-power `[X]U mod139129` at p373 with module rank, semilinear Frobenius direction/eta, odd Green/Hesse port, signed kappa, original Delta-R and independent replication; support Issue #1559 remains OPEN/PENDING_OWNER/NOT_RUN as observed on 2026-11-10. This author-side proof is no substitute.

Current read-only Source continuation `onhour11-20261110-1658-exact-cont-after-unit` returned `SUCCEEDED` with read snapshot `c1b02040c8c3aa6086fe8e1ef76dd940adb0ac23`, changed by completion; the native self-recovery returned `SESSION_CAPABILITY_REQUIRED` for historical session `MCP-5378d3819d8947bda9049c9428493e2d`. No native winning CLAIM, open run, Source checkpoint, Result, review or claim owner change is reported. Logical Research lane remains distinct from maintenance.

**Scientific result status:** AUTHOR_PROVED_MOD_P_FINITE_OPERATOR / 77_8JET_PRIMES / SEVEN_FULL_INDEX_ARRAYS / UNREVIEWED / NOT_ADMITTED / NATIVE_PENDING.