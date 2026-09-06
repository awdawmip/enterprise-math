# RH `H_log3` N=8 four-branch sine finite-subspace positivity certificate

Status: `TASK_RESEARCH / VERIFIED 32-DIMENSIONAL FINITE-SUBSPACE ARB CERTIFICATE / NOT FULL H_LOG3 POSITIVITY / NOT AN RH PROOF`
Date: `2026-09-06`
Researcher-ID: `EM-DIRECT-7C1A42`
Scope: `RH / Weil form / H_log3 / four labelled support branches / first eight Dirichlet-sine modes per branch / Arb rigorous ball arithmetic`

## 0. Certified statement

Let `V_8` be the 32-dimensional real subspace of `H_log3` spanned by the first eight Dirichlet-sine modes on each of the four labelled intervals

- `S_-=[-log3,-log2]`,
- `O_-=[-log2,0]`,
- `O_+=[0,log2]`,
- `S_+=[log2,log3]`.

For the Riemann-Weil quadratic form with the current project normalization, the **complete** Gram matrix on `V_8` is rigorously positive definite.

This is a finite-dimensional theorem certificate. It is not positivity on all of `H_log3`, does not control the Galerkin complement, and is not an RH proof.

## 1. Exact positive archimedean matrix series

The cutoff-free physical-space identity gives

`h_inf(t)=h0+2 integral_0^infinity w(r)(1-cos(tr)) dr`,

where

`w(r)=exp(-r/2)/(1-exp(-2r))`

and

`h0=psi(1/4)-log pi=-gamma-pi/2-3log2-log pi`.

Expanding

`w(r)=sum_(n>=0) exp[-(2n+1/2)r]`

defines

`J_c=integral_0^infinity exp(-cr)[2I-R(r)-R(r)^T]dr`,

with `R(r)_(ij)=<phi_i,T_r phi_j>`.

For every `c>0`,

`J_c >= 0`

because `2I-R-R^T` is the Gram matrix of the translated differences `T_r phi_j-phi_j`.

Hence

`boxed: A_arch=h0 I+sum_(n>=0) J_(2n+1/2)}`.

All `J_c` entries are elementary closed forms in the four-branch sine basis. No numerical quadrature and no frequency cutoff are used in the production certificate.

## 2. Why naive positive-tail truncation is inefficient at N=8

A finite partial sum is a Loewner lower bound, but the smallest complete N=8 eigenvalue is extremely small. Independent high-precision floating pressure tests showed the minimum eigenvalue of the lower matrix approaching zero from below approximately as

- `K=10^5`: `-4.86e-10`;
- `K=2*10^5`: `-1.17e-10`;
- `K=5*10^5`: `-1.80e-11`;
- `K=10^6`: `-3.97e-12`;

while the cutoff-free floating target is positive at about `7e-13`.

Thus summing millions of Arb terms would be possible in principle but structurally wasteful. The production certificate instead sums a moderate exact prefix and rigorously accelerates the infinite tail.

## 3. Convergent algebraic tail expansion

Put

`c_n=2n+1/2`.

For `n>=K`, every closed-form rational part of `J_(c_n)` admits a convergent expansion in powers of `1/c_n`; exponentially small endpoint terms remain separately bounded.

The production certificate uses

`K=10000`, `P=10`.

All algebraic matrix coefficients through powers `c^-P` are retained exactly in Arb. Their infinite sums are evaluated using the exact identity

`boxed: sum_(n>=K) c_n^(-p) = 2^(-p) zeta(p,K+1/4)}`,

where the right side is evaluated by Arb's rigorous Hurwitz-zeta implementation.

The remaining denominator-series tails are bounded by explicit geometric remainders using the first omitted power and the ratio `(alpha/c_K)^2`. Product denominators receive the corresponding convolution-geometric bound. Endpoint exponentials are bounded separately by geometric sums in `exp(-2d)`.

The resulting tail is therefore

`EXACT PREFIX + HURWITZ-ZETA ALGEBRAIC TAIL + RIGOROUS REMAINDER BALLS`,

not a floating extrapolation.

## 4. Exact finite prime and pole blocks

At support radius `log3`, only prime powers

`{2,3,4,5,7,8,9}`

contribute to the prime-translation term.

Their translation overlaps are evaluated in Arb. Every support-intersection branch decision is made by exact `Fraction` comparison in multiplicative coordinates using endpoints

`{1/3,1/2,1,2,3}`.

No floating-point control flow enters the certificate.

The unreduced two-sided pole block retains the two endpoint channels

`l_+(f)=integral f(x)e^(x/2)dx`,
`l_-(f)=integral f(x)e^(-x/2)dx`,

and is assembled exactly as

`P=l_+l_-^T+l_-l_+^T`.

No parity/inversion rank-one recoalescence is assumed.

## 5. Production Arb certificate

Certificate implementation:

- script: `scripts/rh_log3_n8_arb_certificate.py`;
- workflow: `.github/workflows/rh-log3-n8-arb-cert.yml`;
- source head: `d0a4eca2a49a9167848ba4d5d5cfd7eb03d355f7`;
- workflow run: `34022226755`;
- job: `101456774145`;
- Python: `3.13.15`;
- `python-flint==0.9.0`;
- Arb precision: `384 bits`;
- exact prefix: `K=10000`;
- algebraic tail order: `P=10`.

The production run returned

`max tail enclosure radius = 1.0525844716513274413e-26`.

It then performed an interval no-pivot `LDL^T` factorization of the complete rigorously enclosed 32x32 Gram matrix.

## 6. Certified Arb LDL^T pivots

All 32 pivot balls lie strictly in the positive half-line:

| i | midpoint | radius |
|---:|---:|---:|
| 0 | `0.123699577166339931843165090506` | `9.802785627e-36` |
| 1 | `0.697155347182387848753296771130` | `1.003806085e-32` |
| 2 | `1.07719943154735465171226321252` | `5.820004958e-31` |
| 3 | `1.45299982462277241496590137019` | `1.032760368e-29` |
| 4 | `1.64454181733175681369095504615` | `9.661794555e-29` |
| 5 | `1.89700913034817825096173116411` | `5.967711036e-28` |
| 6 | `2.02312232347113796364469806202` | `2.800626649e-27` |
| 7 | `2.20783317532285144242986616464` | `1.060715468e-26` |
| 8 | `0.00238239463625952131193744682407` | `7.866140065e-31` |
| 9 | `0.00796767842017522353334447981296` | `3.554563608e-30` |
| 10 | `0.00842144383497319445235546883307` | `9.949839322e-28` |
| 11 | `0.385688086588680059115203114604` | `3.823735996e-26` |
| 12 | `0.347082862215309973698724938733` | `2.897204742e-25` |
| 13 | `1.11681801337912161170608301953` | `3.185366756e-26` |
| 14 | `0.672860917185434500329919149111` | `1.825022441e-24` |
| 15 | `1.48375219529411634179310813538` | `1.733259880e-25` |
| 16 | `0.000193393318066207434201405229800` | `8.205761551e-28` |
| 17 | `9.40163484253829014526800557353e-7` | `2.219379713e-26` |
| 18 | `2.06524281822765274038962959009e-5` | `3.525053650e-24` |
| 19 | `1.34022050111216244963090410241e-5` | `6.317344473e-23` |
| 20 | `0.000253531853942141358682217002017` | `1.159047005e-20` |
| 21 | `0.000599457115238596122423024241170` | `1.321281319e-18` |
| 22 | `0.0458203362853294946402801903210` | `1.417618709e-16` |
| 23 | `0.0320070386600852326067407327886` | `3.620165698e-15` |
| 24 | `0.000735985777199341223236085380860` | `1.015114531e-18` |
| 25 | `2.82725899122356278472054703146e-6` | `2.873109003e-17` |
| 26 | `1.16813416246958873232464879081e-6` | `2.856938022e-15` |
| 27 | `2.54803710928073363062946125034e-6` | `1.086368136e-12` |
| 28 | `0.00591636396229029637608893156714` | `1.158865727e-8` |
| 29 | `0.165399587109739546101857597129` | `1.517572851e-6` |
| 30 | `0.820794222534933604281117657143` | `9.387086601e-7` |
| 31 | `1.26974918404770515690288991722` | `5.437674311e-6` |

Every lower endpoint remains strictly positive. Therefore Sylvester/LDL inertia certifies the entire enclosed Gram matrix as positive definite.

The workflow concluded:

`CERTIFIED: all 32 Arb LDL^T pivots are strictly positive.`

and

`RESULT: the complete Weil Gram matrix is positive definite on the declared 32-dimensional N=8 H_log3 branch-sine subspace.`

## 7. Certified conclusion

Let `M_V8` be the full Weil Gram matrix on the declared 32-dimensional space `V_8`. Then

`boxed: M_V8 > 0}`.

No numerical-integration remainder, frequency cutoff, or unbounded positive-series tail remains outside the certified matrix enclosure.

This upgrades the former N=8 floating `eta=1` diagnostic to a rigorous finite-subspace positivity result.

## 8. Why the small spectral margin is still certifiable

The complete smallest eigenvalue was previously observed at only about `7e-13`, but no-pivot LDL is much better conditioned for this basis ordering. The smallest certified pivot midpoint is approximately

`9.4016e-7`,

while its radius is about `2.2e-26`.

Thus the certificate does not require a direct interval eigenvalue enclosure at the `1e-13` scale. A basis-order-sensitive exact factorization provides a much healthier positivity witness.

This is a finite-certificate phenomenon, not a claim that the true spectral gap is `1e-6`.

## 9. CI context boundary

The dedicated mathematical workflow succeeded.

At the same PR snapshot, generic repository checks had unrelated concurrent failures:

- `reference-integrity`: failures in independently published X6 task records missing mandatory V2 body sections;
- `quality`: unrelated import failure `cannot import name 'research_scheduler' from 'tools'` in control/runtime tests.

Neither failure path involved the N=8 certificate script or its mathematical workflow. They are control/baseline issues and do not alter the Arb certificate result.

## 10. BRC / observer preservation

The certificate keeps:

- four support-branch identities;
- exact prime-shift support provenance;
- both pole channels;
- the complete archimedean tail as a rigorously enclosed operation-relevant object.

The tail acceleration is operation-safe: it replaces an infinite positive matrix series by exact retained moments plus a certified enclosure, not by heuristic truncation.

## 11. Smallest unresolved unit: Galerkin complement

The sine bases over the four intervals are complete in `L2([-log3,log3])` when all mode indices are retained. Therefore the remaining gap from this certificate to full `H_log3` positivity is entirely the complement of the first eight modes on each branch.

The next target is not a larger finite matrix by itself. It is a theorem/certificate of the form

`HIGH-MODE COMPLEMENT >= positive floor`

plus a low/high Schur-response bound.

A promising route is to use the exact full-line Fourier multiplier of the non-pole Weil form. Its archimedean part grows logarithmically while the finite prime comb is bounded and oscillatory, so the negative part of a shifted multiplier can be confined to a finite frequency band. This converts the dangerous correction on a compact support window into a compact time-frequency concentration operator, with the pole term remaining finite rank.

That route must be derived in the exact project normalization before any full-window claim is made.

## 12. Hard boundaries

- `V_8 POSITIVITY != H_LOG3 POSITIVITY`.
- `32-DIMENSIONAL CERTIFICATE != RH`.
- The no-pivot LDL pivot sizes are positivity witnesses, not eigenvalue lower bounds.
- No claim is made that N=8 is a sufficient universal repair dimension.
- No future square-shell step is certified automatically.
- A Galerkin-complement theorem remains mandatory before full-window positivity can be claimed.

## Provenance

- Mathematical substrate:
  - `research_notes/RH_ARCH_PHYSICAL_TRANSLATION_DIRICHLET_FORM_20260906.md`;
  - `research_notes/RH_SINE_BASIS_ARCH_DIAGONAL_TAIL_INERTIA_CERTIFICATE_20260906.md`;
  - `research_notes/RH_LOG2_LOG3_N8_THRESHOLD_INERTIA_DIAGNOSTIC_20260906.md`;
  - `research_notes/RH_LOG3_N2_ARB_POSITIVITY_CERTIFICATE_20260906.md`.
- Production script: `scripts/rh_log3_n8_arb_certificate.py`.
- Production workflow run: `34022226755`, job `101456774145`.
- Production source head: `d0a4eca2a49a9167848ba4d5d5cfd7eb03d355f7`.
- Researcher-ID: `EM-DIRECT-7C1A42`.
