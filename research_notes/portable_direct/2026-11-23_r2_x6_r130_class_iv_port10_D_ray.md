# X6 R130 — Port-10 exact all-positive D-ray at (722,465,240,D)

Date: 2026-11-23 (Asia/Shanghai). Status: **AUTHOR EXACT PARAMETRIC PROOF / FRACTION REPLAY PASS / NOT INDEPENDENTLY REVIEWED**.

## Observer / immutable mathematical inputs

This is the same **conditional six-pair** four-positive-weight BRC observer used in R121/R122 and R129, not a native X6/P000 physical time law. Take any nonzero integer triple \(a=(x,y,z)\) modulo sign, *not* modulo positive multiples; Port \(q(a)=\max(\sum_i\max(a_i,0),\sum_i\max(-a_i,0))\le10\). Heights are
\(h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z)\).
Retain all six \(g_{ij}(a)=|h_i-h_j|\), indexed \(01,02,03,12,13,23\).

Fix the first three **positive** physical weights \(A=722,B=465,C=240\), take real \(D>0\), and define
\[
F_D(a)=\max\left(\frac{g_{01}}{1187},\frac{g_{02}}{962},
\frac{g_{03}}{D+722},\frac{g_{12}}{705},
\frac{g_{13}}{D+465},\frac{g_{23}}{D+240}\right).
\]
Write \(\eta_{10}(D)=\min_{0<q(a)\le10}F_D(a)\) and
\(N_{10}(D)=\{\{\pm a\}:0<q(a)\le10,\;2F_D(a)<3\eta_{10}(D)\}\).

## Theorem 1: exact optimum, every real D>0

\[
\boxed{\eta_{10}(D)=
\begin{cases}
3/(D+240),&0<D\le241,\\
3/481,&241\le D\le497,\\
6/(D+465),&497\le D\le1077,\\
7/(D+722),&1077\le D\le4568/3,\\
3/962,&4568/3\le D\le3383,\\
12/(D+465),&3383\le D\le7995,\\
1/705,&7995\le D\le8220,\\
12/(D+240),&D\ge8220.
\end{cases}}
\]
The formulas agree at all seven shared endpoints. Seven optimizer-formula changes occur at \(241,497,1077,4568/3,3383,7995,8220\).

## Theorem 2: exact strict 3/2 near count and complete set

| Real D | \(|N_{10}(D)|\) |
|:---|---:|
| \(0<D<243/5\) | **8** |
| \(243/5\le D<1698/11\) | 6 |
| \(1698/11\le D<241\) | 5 |
| \(241\le D\le1095/2\) | 4 |
| \(1095/2<D<978\) | 5 |
| \(978\le D\le6512/5\) | 3 |
| \(6512/5<D\le19004/9\) | 4 |
| \(19004/9<D\le6976/3\) | 5 |
| \(6976/3<D<3765\) | 6 |
| \(3765\le D<5307\) | 5 |
| \(5307\le D<12450\) | 2 |
| \(D\ge12450\) | 1 |

Start with \(0<D<243/5\) and
\[
N_0=\{(1,0,0),(3,-4,1),(3,3,-1),(4,-4,1),(6,-1,0),(7,-8,2),(7,-1,0),(9,-5,1)\}/\pm.
\]
The following table gives the **complete membership**, not just cardinality. At an exit threshold the departing row is already absent; at an entry threshold the entering row appears only strictly to the right.

| Threshold | Enter just to the right | Exit at equality |
|:---|:---|:---|
| \(243/5\) | — | (3,3,-1), (7,-8,2) |
| \(1698/11\) | — | (7,-1,0) |
| \(241\) | — | (3,-4,1) |
| \(1095/2\) | (5,-1,0) | — |
| \(978\) | — | (4,-4,1), (6,-1,0) |
| \(6512/5\) | (5,-4,1) | — |
| \(19004/9\) | (4,-1,0) | — |
| \(6976/3\) | (6,-4,1) | — |
| \(3765\) | — | (9,-5,1) |
| \(5307\) | — | (1,0,0), (5,-4,1), (5,-1,0) |
| \(12450\) | — | (4,-1,0) |

At the original maximizing example \(D=48\),
\(\eta_{10}(48)=1/96\) and there are exactly eight directions in \(N_0\). Multiple later *re-entries* are real: at \(D>1095/2\), \(D>6512/5\), \(D>19004/9\) and \(D>6976/3\). At \(D\ge12450\), only \((6,-4,1)\) remains.

## Complete, machine-reproducible finite-to-continuum proof

The standalone exact rational code [six-pair D-ray sweep](x6_port10_six_pair_D_ray_exact_sweep.py) runs as
\`python x6_port10_six_pair_D_ray_exact_sweep.py 722 465 240\`.
It starts with the *entire* Port-10 unoriented integer population of **1,935** vectors. Using all six gap components, it verifies that the frozen R121 18-row optimizer bank dominates all 1,935 vectors and that the R122 20-row 3/2-exclusion envelope is precisely the set not uniformly excluded by those bank rows. For every excluded vector \(a\), some bank row \(b\) satisfies \(2g_j(a)\ge3g_j(b)\) for all six \(j\), hence \(2F_D(a)\ge3F_D(b)\ge3\eta_{10}(D)\) for **all real D>0**.

All candidate scores are maxima of rational constants and \(g/(D+c)\). A change of the bank minimizer, any row maximum or \(2F_a-3\eta\) requires an equality between elementary functions: within-row, bank-vs-bank, or scaled \(2f_a=3f_b\). The code solves **all** such positive equations exactly; in this ray there are **914 distinct positive critical rational roots**. It checks each of the **915 open intervals** (including the unbounded final interval) and each of the **914 critical points** with exact \`Fraction\` arithmetic. It verifies that at each root the strict near set equals the intersection of both neighboring open interval sets, so there are no missed equality-only events. All full optimizer and near-set calculations were additionally crosschecked directly on the unreduced **1,935 vectors** at **22 distinct exact parameter values**, consisting of all 17 distinct optimizer/near threshold points plus five additional points. This is a complete interval/root partition proof for the stated conditional model, not interpolation from sampled D values.

## Provenance / status / next independent question

Scientific pins: [R121](https://github.com/awdawmip/enterprise-math/blob/8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd/research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md) and [R122](https://github.com/awdawmip/enterprise-math/blob/0687aa24f5402da3b35f914dd6907967a9805b94/research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json). This is a **different** fourth-parameter ray from R127, R128D and R129. The mechanism (exact equality-root sweep) is reused, while the weights, 914 roots, optimizer divisions and membership fan are newly computed. It changes neither frozen native X6 Task inputs nor P000 and grants no Task owner, CLAIM, PROGRESS, Result, independent Review or Foundation status.

All claims are **author-derived/author-replayed**, awaiting independent mathematics review. Next useful question: compare the geometry of the four rays' strict-eight chambers under transverse changes of A,B,C, or extract a general combinatorial upper bound on ray fan complexity from the R121/R122 finite atom arrangement.