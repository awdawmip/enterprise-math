# PREFIX-1005 — Eleven exact marked-collision orbits for the native X6 one-Link BRC observer

Date: 2026-11-22 (+08). Status: AUTHOR_GROUP_RING_PROOF / EXACT_SYMBOLIC_AND_INTEGER_CHECKED / NOT_REVIEWED. Independent portable scientific note; not a formal Result or accepted Foundation.

## Source and exact observation scope

Scientific inputs retain frozen P000 V5 at `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json` and the **Stage46 candidate** typed signed BRC local coefficient `C(h,j)=1/6−[h=j]`; next incoming-neighbour port is the reverse of the actual outgoing step. Native space is an affine six-dimensional Cell torsor with signed axis steps; the step counter is separately typed. Initial incoming-neighbour port is `−e1`.

The undirected Link between the chosen chart-relative anchor and `anchor+e1` is blocked in both directions by absorption (no renormalization). Fix the **first interior grade**: exactly one negative axis step in `n` steps. Observe the final Cell **and** final incoming-neighbour port as a joint fibre. Each fibre's positive-weight `N[Z2]` BRC branches are signed-summed and then squared; fibres are then summed. This is a final-observer scalar reduction, **not** a replacement for complete path/port history under arbitrary future operators.

Exact prior source: [PREFIX-1004](https://github.com/awdawmip/enterprise-math/blob/aec844a083f0517570ce1dd5924717db6880da98/research_notes/portable_direct/2026-11-22_r6_prefix1004_marked_collision_asymptotic.md). The present note derives a new, bounded orbit basis for its all-length collision expression and checks the former exact certificate.

## Theorem 1005.1 — universal eleven-orbit formula

Put `S=Σ_{i=1}^6 z_i`, `U=Σ_i z_i^{-1}` in the formal Laurent group ring of **chart displacements** and let `n≥5`, `m=n−4`. Let

\[
H_m(\delta)=\sum_{\substack{a\in\mathbb N^6\\ |a|=m}}
\binom ma\binom m{a+\delta},
\]
where a multinomial with an invalid lower index is zero (hence `H_m(δ)=0` unless `Σδ_i=0`). Define `A_6(m)=H_m(0)`.

For every integer `n≥5`, the *exact final joint-port probability mass* `M^L_{n,1}` of the specified absorbing Stage46 candidate obeys

\[
\boxed{36^n M^L_{n,1}=\sum_{\alpha=0}^{10}K_\alpha(n)\,H_{n-4}(\delta_\alpha).}
\]

The **eleven orbit representatives and complete coefficients** are:

| `δα` (coordinates sorted) | Laurent shifts in orbit | `Kα(n)` |
|---|---:|---|
| (0,0,0,0,0,0) | 1 | `30(722n²−4610n+8055)` |
| (−1,0,0,0,0,1) | 30 | `60(378n²−2371n+5924)` |
| (−2,0,0,0,0,2) | 30 | `−60(57n²−235n+185)` |
| (−2,0,0,0,1,1) | 120 | `−480(63n²−340n+458)` |
| (−1,−1,0,0,1,1) | 90 | `−720(69n²−451n+749)` |
| (−3,0,0,0,0,3) | 30 | `60(n−4)(2n+1)` |
| (−3,0,0,0,1,2) | 240 | `1440(2n²−9n+2)` |
| (−3,0,0,1,1,1) | 120 | `1440(2n²−10n+5)` |
| (−2,−1,0,0,1,2) | 360 | `6480(2n²−11n+8)` |
| (−2,−1,0,1,1,1) | 240 | `8640(2n²−12n+11)` |
| (−1,−1,−1,1,1,1) | 20 | `1440(2n²−13n+14)` |

The original Laurent-square expression has **1,281 distinct exponent shifts**, including zero; its entire dependence on length in this observer is captured by eleven quadratic polynomials `Kα(n)` and eleven exact collision values. The eleven orbits are a complete symmetry grouping of the **present polynomial support**, not a claim of linear independence or universally minimal recurrence order among marked collisions.

### Proof

Set
\[
B_{k,j}=(k-1)SU-36(k-3)-6S/z_1-6S/z_j.
\]
By the already established exact typed Z2 BRC first-interior Laurent identity in PREFIX-1004, the masked positive-final-port packet is `F^L_{n,j}=z_j S^{n-4}P_{n,j}`, and the masked negative-final-port packet is `N^L_{n,r}=S^{n-4}Q_r`, where
\[
\boxed{
P_{n,j}=SB_{n,j}-z_1B_{n-1,j}+25z_1,\qquad
Q_r=z_r^{-1}S(S-6z_r)(S-z_1).
}
\]
All packets are exact signed integer numerators; dividing by `6^n` recovers amplitudes. Preserve each terminal port's separate square:
\[
D_n(z)=\sum_{j=1}^{6}P_{n,j}(z)P_{n,j}(z^{-1})
+\sum_{r=1}^{6}Q_r(z)Q_r(z^{-1}).
\]
Then
\[
36^n M^L_{n,1}=\operatorname{CT}\{S^{m}U^{m}D_n(z)\}.
\]
Indeed `CT(S^mU^mz^\delta)=H_m(\delta)` exactly, by expanding the two multinomial powers and matching the zero exponent.

Write `D_n(z)=Σ_δ c_n(δ)z^δ`. Under simultaneous permutations of all six coordinates, and under `δ↦−δ`, the collision observer `H_m(δ)` is unchanged. Therefore group **coefficients**, not histories, under
\[
\mathcal O(\delta)=\{\,\sigma(\delta),-\sigma(\delta):\sigma\in S_6\,\},
\qquad K_{\mathcal O}(n)=\sum_{\eta\in\mathcal O}c_n(\eta).
\]
Finite Laurent polynomial multiplication of the displayed `P,Q` expressions yields precisely the eleven rows of the table, with `1+30+30+120+90+30+240+120+360+240+20=1281`. Every coefficient identity is a degree-at-most-two polynomial in `n`, so this finite symbolic expansion proves the formula for **all** integer `n≥5` rather than extrapolating from finite lengths. The accompanying independent algebraic enumerator reconstructs `P,Q,D`, checks all eleven symbolic polynomial identities and exact integer collision sums. QED.

### Auxiliary identity — first marked orbit reduces to the unmarked collision

For `i≠j`, directly expand `A_6(m+1)=CT[(SU)S^mU^m]`. The `6` diagonal terms are `A_6(m)`; the other `30` terms all equal `H_m(e_i-e_j)`. Thus, for every `m≥0`,
\[
\boxed{H_m(e_i-e_j)=\frac{A_6(m+1)-6A_6(m)}{30}.}
\]
This reduces the second orbit exactly to existing `A_6` data. No analogous elimination of the remaining marked orbits is claimed here.

## Exact validation

The attached `PREFIX1005_R6_ORBIT_COLLISION_CHECK.py` uses symbolic Laurent coefficients and integer multinomial arithmetic. It verifies the complete 1,281-shift expansion and all eleven polynomial orbit coefficients, then recomputes the pre-existing PREFIX-1004 certificate at `n=5,6,7,8,9,10,12,14,16,20`. All ten exact masses match, including `M^L_{8,1}=259181485/78364164096` and `M^L_{20,1}=89379684726508120031933065/371319292745659279662190166016`.

The BRC joint-port packet identity is an imported, explicitly scoped previously checked result. This round supplies an independent symbolic/integer crosscheck **of its final-scalar consequence**; it has not performed a new live canonical Stage46 core invocation, an independent mathematical review, nor a physical heartbeat calibration. Asymptotic claims remain exactly at their PREFIX-1004 status.

## Next exact question

Derive and test a shorter **closed exact recurrence** for the marked-collision orbit family under the declared observer; in particular determine which other marked `H_m(δ)` admit elimination into shifts of `A_6` and which genuine interaction coordinates remain. Also investigate the `k=2` first-five-step Link prefix at full joint-port resolution before proposing any further quotient.

Source-state: historical R6 contribution `EM-DIRECT-FBEA5D`, Activity `RA-3FB2D033BE6048D8712FF056` (provenance only). Fresh authenticated Researcher/Activity capability and canonical owner/CLAIM were not established by the present GitHub write. No formal `PROGRESS` or `Review` mutation is asserted.
