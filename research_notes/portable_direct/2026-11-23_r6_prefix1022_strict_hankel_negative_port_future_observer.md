# PREFIX-1022 — Strict Hankel positivity and infinite linear-observer rank for fixed-seed k=1 negative-port BRC

2026-11-23 Asia/Shanghai. Status: **AUTHOR_EXACT_LAURENT_PROOF / NATIVE_INTEGER_BRC_CHECKED / NOT_REVIEWED**.
Scope: frozen Stage46 *candidate* signed X6 BRC, not P000 promotion, actual physical dynamics or an accepted formal Task Result. Continuation of PREFIX-1014/1015/1021.

## Frozen input and complete observer

Scientific P000 V5 pin: `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json`. The native signed six-axis chart is relative to a chosen Cell, with twelve outgoing directions `d`, incoming-neighbour ports `h`, signed weight `W(h,d)=1-6[h=d]`, update fibre `(x+d,-d)`, and absorption of both orientations of the Link `{0,e1}`. Seed: `(Cell 0, incoming port -e1)`. Grade `k=1` counts exactly one **negative outgoing direction**. Coherent signed amplitudes combine *within identical Cell–terminal-port–grade fibres before squaring*; normalized mass is the integer squared numerator divided by `36^n`.

Let `R=Z[z_1^{±1},...,z_6^{±1}]`, `S=sum_i z_i`, `S*=sum_i z_i^-1`, `L=SS*`. The involution `f*` reverses Laurent exponents. The constant-term norm `||f||²=CT(ff*)=sum_alpha coeff_alpha(f)^2` is positive for every nonzero real-coefficient Laurent polynomial `f`. This is exact signed-BRC coefficient bookkeeping, not a classical physical propagator or unsigned branch replacement.

PREFIX-1014 proves for every integer `n>=5`, each fixed terminal negative-direction port `j`:
 
`N_{n,j}=z_j^-1 S^{n-3}(S-6z_j)(S-z_1)=S^{n-4} R_j`,
`R_j=z_j^-1 S(S-6z_j)(S-z_1) != 0`.

Consequently the squared mass numerator is the exact Laurent moment

`Q^-_{n,j}=CT(R_j R_j* L^{n-4})`.                                    (1)

PREFIX-1015 separately proves, for `j=2,...,6`, with `V_i=S-6z_i` and `D_j=V_1 V_1* - V_j V_j* != 0`, the exact signed Gram contrast identity

`Delta^-_{n,j}=Q^-_{n,1}-Q^-_{n,j}=(1/12) CT(D_j D_j* L^{n-3})>0`.  (2)

The latter is an identity in the declared *joint* coherent observer, not a positive-mass approximation.

## Theorem: all future Hankel matrices are strictly positive definite

For every integers `n0>=5`, `h>=1` and `j=1,...,6`, the real `h x h` Hankel matrix

`H^-_{h,n0,j}=[Q^-_{n0+a+b,j}]_{0<=a,b<h}`

is **strictly positive definite**. For every `j=2,...,6`, the contrast matrix

`H^Delta_{h,n0,j}=[Delta^-_{n0+a+b,j}]_{0<=a,b<h}`

is also strictly positive definite. Thus every leading principal minor is positive, and the infinite Hankel rank of each negative-port mass and of each negative-port contrast is unbounded.

**Proof.** For a nonzero real coefficient vector `c=(c_0,...,c_{h-1})`, put `p(t)=sum_a c_a t^a`. Equation (1) gives

`c^T H^- c = CT[R_j R_j* L^{n0-4} p(L)^2] = ||S^{n0-4} R_j p(L)||²`.

The Laurent polynomial ring is an integral domain, `S` and `R_j` are nonzero, and `p(L)` cannot vanish for a nonzero polynomial `p`. For the last assertion, specialize `z_1=u`, `z_2=...=z_6=1`, so `L=26+5(u+u^-1)`. If `p` has degree `d`, the coefficient of `u^d` in `p(26+5(u+u^-1))` is exactly `5^d` times the leading coefficient of `p`, hence nonzero. The norm above is therefore strictly positive.

For the contrast use (2) and replace `R_j` by `D_j`, `n0-4` by `n0-3`, and multiply the squared norm by `1/12`. Its Laurent factor is nonzero: specialize `z_1=1`, `z_j=u`, all other variables `1`, yielding `D_j=-24(u-1)(u^-1-1) != 0`. The same integral-domain proof applies. QED.

This is an algebraic proof for *all* `n0` and `h`, not an extrapolation of finite computations.

## Three sharp consequences, with the declared observer scope

1. **Strict log-convexity**: for `a_n=Q^-_{n,j}` or `Delta^-_{n,j}`, every `n>=5` satisfies
   `a_n a_{n+2}>a_{n+1}²>0`. Hence `a_{n+1}/a_n` increases strictly with `n`.

2. **Strict normalized decay**: finite Laurent shifts preserve the coefficient-`l²` norm, and `Sf=sum_{i=1}^6 z_i f`. Therefore `||Sf||<6||f||` whenever `f!=0`, since equality in the triangle inequality would force `(z_i-z_j)f=0` for distinct indices in an integral domain. Applied to (1)/(2), `0<a_{n+1}/a_n<36`. Thus `a_n/36^n` decreases strictly while its successive ratio increases and remains below `1`. The unnormalized ratio has a limit at most `36`; its exact limit is *not claimed*.

3. **No finite constant-coefficient linear scalar closure**: no such sequence satisfies any nontrivial *eventual* constant-coefficient linear recurrence. Otherwise late columns of a sufficiently large Hankel matrix would be linearly dependent, contradicting strict positive definiteness. By Cayley–Hamilton, this rules out an autonomous fixed-finite-dimensional **time-invariant linear** state update with a linear output reproducing the entire negative-port mass trajectory (or contrast) for this seed. It does not rule out nonlinear or time-dependent coordinates, finite-horizon observers, the Laurent carrier itself, or the full signed native BRC state.

## Native exact-integer check and reproducibility

An independently implemented named-port native BRC update, preserving Cell, sign, port and actual negative-step grade, was executed through `n=8`. Separate integer multinomial Laurent expansion of (1) computed `n=5,...,11`. The full native negative-terminal masses matched the Laurent values at `n=5,...,8`. Fraction-free Bareiss elimination evaluated `1x1`, `2x2`, `3x3` Hankel determinants exactly at `n0=5`.

| n | Q minus axis 1 | Q minus each other axis | strict difference |
|---:|---:|---:|---:|
| 5 | 16560 | 12384 | 4176 |
| 6 | 246870 | 191574 | 55296 |
| 7 | 4299380 | 3455060 | 844320 |
| 8 | 83992020 | 69575892 | 14416128 |
| 9 | 1790819940 | 1521116436 | 269703504 |
| 10 | 40858323910 | 35414546374 | 5443777536 |
| 11 | 983156336340 | 866106436596 | 117049899744 |

| order | det for axis 1 | det for other axis | det for difference |
|---:|---:|---:|---:|
| 1 | 16560 | 12384 | 4176 |
| 2 | 10252935900 | 6086865564 | 468232704 |
| 3 | 359622707860774000 | 170254317911251888 | 2618665390743552 |

Evidence: `PREFIX1022_R6_STRICT_HANKEL_CHECK.py` and `PREFIX1022_R6_INTEGER_CERT.json` in this directory. Checks are finite; the theorem has the separate exact proof above. No π, trigonometric propagation, matrix exponential, Taylor/Padé/Cayley or external classical comparison was run.

## Context, limits and next discriminating question

PREFIX-1021 established rank `2H` for *oriented future flux* and a `C¹` lower bound `H+1` for arbitrary-all-grade one-shot squared norm trajectories. The new result concerns a fixed seed, exactly one negative direction, **negative terminal mass and its contrast**, and the class of *autonomous constant-coefficient linear scalar observers*. These are different propositions and should not be promoted to an unrestricted minimum dynamic state dimension. The safe fixed-seed amplitude formulas still retain complete Cell–port coefficients; this theorem is an output-specific no-go for compressing their entire future mass sequence into one finite constant linear recurrence.

Next: investigate positive-terminal-port squared masses, whose frozen Laurent amplitudes have `n`-dependent templates, for a similar infinite-Hankel obstruction; then seek genuinely future-closed **nonlinear/time-indexed** Gram repair coordinates and verify the allowed operation/observer family. Mother objective `B_fix,odd(32) in {19,20}` remains open.

Provenance: actual scientific input from PREFIX-1014/1015/1021. Earlier contributor `EM-DIRECT-FBEA5D`, Activity `RA-3FB2D033BE6048D8712FF056`, and SID `MCP-45ad6d29cd534c1aad25595a72e3c532` are historical locators, not inferred new research authority. This publication has **not** received independent mathematical review or formal CLAIM/PROGRESS acceptance.
