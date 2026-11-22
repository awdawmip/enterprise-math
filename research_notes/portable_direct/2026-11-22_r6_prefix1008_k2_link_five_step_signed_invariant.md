# PREFIX-1008 — Sharp two-negative X6 Link horizon, exact five-step BRC packets, and a signed invariant

Date: 2026-11-22 (+08). Status: **AUTHOR_ANALYTIC_AND_FINITE_ENUMERATION_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED**. This is independent portable mathematics, not an authorized shared CLAIM, native PROGRESS, Result, Review, or physical time-law promotion.

## Fixed scientific model and provenance

Scientific input remains frozen at `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json`, with its X6 native-Cell torsor and six signed axes. Continue the **candidate** Stage46 BRC local law from PREFIX-1003: incoming-neighbour port `h`, outgoing primitive signed direction `d`, coefficient `C(h,d)=(1-6[h=d])/6`, next incoming-neighbour port `-d`. Start at chart-relative Cell 0, incoming-neighbour port `-e1`. Absorb both traversals of the single native Link `{0,e1}` without renormalizing any remaining branch. Let `k` count negative moves. Preserve each joint terminal `(Cell,incoming-port,k)` fibre as a signed amplitude **before** taking the squared norm. No physical heartbeat-time calibration, native-plane assumption, or new spatial axis is involved.

Inherited: [PREFIX-1003](https://github.com/awdawmip/enterprise-math/blob/d9c53f6af236cf7d128409c9eb07dd3e735f523c/research_notes/portable_direct/2026-11-22_r6_prefix1003_single_link_first_interior_finite_prefix.md) proves the general `2k+1` finite-horizon statement; [PREFIX-1007](https://github.com/awdawmip/enterprise-math/blob/d8ce38c05475290f7b54e13a5d316f3621e9f3b5/research_notes/portable_direct/2026-11-22_r6_prefix1007_four_shift_collision_closure.md) compresses only the **k=1 final scalar**. Here we examine **k=2**, where that compression cannot simply be re-used as an evolving state.

## Theorem 1008.1 — Exact, sharp, orientation-resolved last crossing at k=2

For a path with exactly two negative native steps, any prohibited `0→e1` crossing is at an odd step `t∈{1,3,5}`; any prohibited `e1→0` crossing is at an even step `t∈{2,4}`. Both upper bounds are sharp even among paths with **no earlier blocked crossing**.

**Proof.** Before a positive crossing the Cell grade `sum_i x_i` is 0. For a prefix of length `t-1` containing `r` negative steps, `t-1-2r=0`, hence `t=2r+1≤5`. Before a negative crossing the grade is 1, so `t-1-2r=1`; the crossing itself consumes a negative step, giving `r≤1` and `t=2r+2≤4`. Parity and upper bounds are forced. Sharpness witnesses (all paths begin at 0, using chart-relative displacements): `(+e2,+e3,-e2,-e3,+e1)` first crosses at step 5; `(+e2,+e1,-e2,-e1)` first crosses at step 4. Neither crosses the closed Link earlier. QED.

## Theorem 1008.2 — A complete five-step packet (and why all three grades survive)

Let `W(u)=W_+ + u W_-` be the **integer-numerator** unrestricted BRC transfer on full `(Cell,port)` fibres, with `u` marking negative moves, and `W_L(u)` the two-sided-Link-absorbed transfer. Write `v0` for the initial full state. Each length-`n` actual amplitude divides the integer numerator by `6^n`. For **all n≥5**,

[
\boxed{\Psi^L_{n,2}=6^{-n}[u^2]W(u)^{n-5}W_L(u)^5v_0},
\qquad
\boxed{\Psi_{n,2}-\Psi^L_{n,2}=6^{-n}[u^2]W(u)^{n-5}(W(u)^5-W_L(u)^5)v_0}.
]

**Proof.** Theorem 1008.1 excludes every prohibited edge traversal after step 5 in the `u^2` sector. Thus the suffix can use the unrestricted transfer without changing any path contributing to that sector. The identity holds at the complete named port state before applying any scalar observer. QED.

Write `D_5=W^5v0-W_L^5v0`, truncated to nonnegative negative-step grades `0,1,2`. Its **nonzero joint fibres** are exactly

| Grade in the five-step defect | Nonzero joint Cell/port fibres |
|---:|---:|
| 0 | 336 |
| 1 | 912 |
| 2 | 1152 |
| **Total** | **2400** |

These are reproducible exact finite counts, not a claim of minimal state dimension. Keeping only the grade-2 component of `D_5` fails even at the very next update: one missing grade-1-to-grade-2 contribution at step 6 has terminal Cell `(-1,0,0,0,0,3)`, incoming port `+e1`, numerator **−2** over `6^6`. Thus **retaining only the currently observed grade-2 defect is not a future-safe quotient**. The joint port and lower-grade resource remain necessary for the declared following evolution. This is a concrete scope-typed residual witness, not an objection to PREFIX-1007's separately proved final `k=1` scalar reduction.

## Theorem 1008.3 — A nonzero exact signed total invariant for all n≥5

Let `S^L_{n,2}=Σ_(x,h) Ψ^L_{n,2}(x,h)` denote the **signed sum of amplitudes**, *not* their probability or squared mass. Then for every integer `n≥5`,

[
\boxed{S^L_{n,2}=-\frac{390}{6^5}=-\frac{65}{1296}.}
]

**Proof (complete finite part plus symbolic continuation).** For any incoming negative port, summing the integer BRC weights over the six positive outgoing directions gives 6 and over the six negative directions gives 0. For an incoming positive port these two sums are 0 and 6, respectively. Thus every unrestricted suffix starting from a negative incoming port has signed total **zero** in every strictly positive negative-step grade. This is an exact cancellation within named full fibres followed by a declared scalar observation.

At step 5 and exact grade 2, partition unrestricted paths that attempt the closed Link by their **first** forbidden step. Exhaustive finite decomposition, including every ordered signed native path with exactly two negative steps, gives:

| First forbidden step | Path count | Signed integer numerator sum |
|---:|---:|---:|
| 1 | 7776 | 0 |
| 2 | 0 | 0 |
| 3 | 792 | 0 |
| 4 | 60 | 0 |
| 5 | 342 | **390** |

At first hit 1 or 3, the unrestricted suffix begins with incoming port `-e1` and still requires a negative move, hence its signed total vanishes. At first hit 4, the suffix has one positive move from incoming port `+e1`, again with signed total zero. At first hit 5, the first four steps must form a closed native Cell loop with exactly two negative moves **avoiding the Link**. The last crossing is `+e1` and has integer multiplier +1; a preceding incoming `+e1` would have meant an already forbidden step-4 `-e1`. Enumeration of all such four-step loops reduces to the following complete support-axis classes (the pairs of distinct other axes are included):

| Used-axis class | Safe loops | Signed numerator sum |
|---|---:|---:|
| One axis, e1 | 2 | 650 |
| One axis, one of the other five | 30 | −1050 |
| Two axes, including e1 | 70 | −890 |
| Two axes, both outside e1 | 240 | 1680 |
| **Total** | **342** | **390** |

For each one-axis class enumerate the six orderings of two positive and two negative occurrences; for each distinct-axis pair enumerate the 24 orderings of `(+ei,-ei,+ej,-ej)`. Keep only paths avoiding `{0,e1}`, multiply the exact local integer weights `1` or `−5`, and group as shown; this finite evaluation is completely reproduced by the companion code and independently by the length-five free-path first-hit enumeration.

The unrestricted grade-2 signed total at step 5 is zero, so the masked total is `−390/6^5`. Also, the masked **positive-incoming-port** total at grade 1 is zero for every step: a negative blocked transition at grade 1 would require the already blocked initial `0→e1` crossing, and the unrestricted orientation-row cancellation otherwise gives zero. At step 5 the masked positive-incoming-port grade-2 total is zero (its last negative transition comes from the zero grade-1 positive-port total; the possible step-5 blocked transition is positive). After step 5 there can be no additional deleted transition in grade 2. The unnormalized negative-port grade-2 sum therefore multiplies by 6 per step, while the positive-port grade-2 sum remains 0. Dividing by `6^n`, `S^L_{n,2}` is constant. QED.

The result is a **nonzero signed interference residual**. It must not be identified with a probability, which is `Σ_(x,h)|Ψ^L_{n,2}(x,h)|²`.

## Exact probabilities for independent comparison

| n | Masked grade-2 joint-fibre probability | Unrestricted grade-2 joint-fibre probability |
|---:|---:|---:|
| 5 | 446995/5038848 | 2875/23328 |
| 6 | 6110005/181398528 | 53645/1119744 |
| 7 | 65505005/3265173504 | 3535775/120932352 |
| 8 | 345588635/26121388032 | 63463045/3265173504 |
| 9 | 2144824195/235092492288 | 527836865/39182082048 |

All fractions are computed from integer numerator amplitudes and the common `36^n` probability denominator; fractions are reduced only for display. This table is **not** an asymptotic estimate.

## Verification, validity, and next question

The checker `PREFIX1008_R6_K2_LINK_PREFIX_CHECK.py` uses two independent finite constructions: exhaustive ordered five-step unrestricted paths with first-hit classification, and separate four-step mask-safe loop enumeration. It compares the former against the integer dynamic-programming amplitude state for every grade-2 terminal Cell/port. It independently computes unrestricted and masked twelve-direction BRC transition states, and verifies the five-step packet and defect identities in **every joint Cell/port/grade fibre at n=5…9**, along with the signed invariant and the grade-1 leakage witness. Output: `PREFIX1008_R6_EXACT_RESULTS.json`. All computations are exact integers/Fractions; independent mathematical Review and native historical Stage46 execution were **not** performed.

The finite prefix theorem and signed-total invariant are exact under the declared **candidate** constitutive law and stated observer. The new five-step packet is a finite source for future exact `k=2` scalarization; the next valuable question is whether the complete squared-mass observer `||Ψ^L_{n,2}||²` admits a short collision formula via the PREFIX-1007 seven-state `A_6` module or requires marked/mixed-grade overlap modules. It must not be replaced by the signed-total invariant. A second independent direction is to compare a norm-preserving reflection on this same Link with absorption, retaining all terminal ports.

Historical authorship/provenance: R6 `EM-DIRECT-FBEA5D`, Activity `RA-3FB2D033BE6048D8712FF056`; historical IDs alone do **not** authorize protected writes. Mother question `B_fix,odd(32)∈{19,20}` remains open.
