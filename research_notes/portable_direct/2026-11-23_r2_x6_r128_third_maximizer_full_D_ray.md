# X6 R128D — third Port-10 maximizing chamber: exact full positive D-ray

Date: 2026-11-23 (Asia/Shanghai). Scientific status: **AUTHOR EXACT FINITE PARAMETRIC CERTIFICATE / PYTHON FRACTION REPLAY PASS / NOT INDEPENDENTLY REVIEWED**.

This continues R127's recommendation to study a *third* maximizing weight chamber. The existing R127 Port-10 ray fixes (48,577,240,D); the present result fixes the **different** weights (240,577,48,D). All four physical weights stay positive. It retains all six pairwise observations and the frozen R121/R122 observer; it neither repins the native X6 Task nor claims a P000 heartbeat-time theorem.

## Model, domain and theorem

Let \(a=(x,y,z)\in\mathbb Z^3\setminus\{0\}\), identify \(a\sim-a\) but *not* positive integer multiples, and define
\[
q(a)=\max\{\sum_i\max(a_i,0),\sum_i\max(-a_i,0)\},
\quad h(a)=(0,x+3y+6z,3x+12y+30z,7x+39y+126z).
\]
Write \(g(a)=(|h_0-h_1|,|h_0-h_2|,|h_0-h_3|,|h_1-h_2|,|h_1-h_3|,|h_2-h_3|)\).
For **every real D>0** fix \(p=10\), \(w_D=(240,577,48,D)\), and
\[
F_D(a)=\max\left\{\frac{g_{01}}{817},\frac{g_{02}}{288},
\frac{g_{03}}{D+240},\frac{g_{12}}{625},
\frac{g_{13}}{D+577},\frac{g_{23}}{D+48}\right\},
\quad
\eta(D)=\min_{0<q(a)\le10}F_D(a),
\quad N(D)=\{\{\pm a\}:0<q(a)\le10,\ 2F_D(a)<3\eta(D)\}.
\]

**Theorem A (all-real exact optimizer).**
\[
\boxed{\eta(D)=
\begin{cases}
9/(D+240),&0<D\le48,\\
3/(D+48),&48\le D\le144,\\
6/(D+240),&144\le D\le336,\\
1/96,&336\le D\le1008,\\
11/(D+48),&1008\le D\le5771,\\
12/(D+577),&5771\le D\le6923,\\
1/625,&6923\le D\le7452,\\
12/(D+48),&D\ge7452.
\end{cases}}
\]
Adjacent formulas coincide at shared endpoints.

**Theorem B (complete strict \(3/2\) near-direction fan).** The count \(|N(D)|\) has the following *exact* 15 regimes. All endpoints are as written, including strict inequalities:

| Real D | Count |
|---|---:|
| \(0<D\le48/7\) | 2 |
| \(48/7<D<96/5\) | 5 |
| \(96/5\le D\le624/19\) | 4 |
| \(624/19<D<96\) | 6 |
| \(96\le D<192\) | 4 |
| \(192\le D\le400\) | 2 |
| \(400<D\le464\) | 3 |
| \(464<D\le656\) | 4 |
| \(656<D\le720\) | 5 |
| \(720<D\le912\) | 6 |
| \(912<D\le976\) | 7 |
| \(976<D<6096/5\) | **8** |
| \(6096/5\le D<1536\) | 7 |
| \(1536\le D<11202\) | 2 |
| \(D\ge11202\) | 1 |

For an exact **set**, not just the count, start at \(D\in(0,48/7]\) with
\[
N_0=\{(3,-4,1),(7,-1,0)\}/\pm.
\]
Crossing each threshold **to its right**, apply the following additions/removals. On the threshold itself, departing rows are *already absent* (strict inequality), while entering rows are *not yet present*:

| Threshold | Add just to right | Remove at threshold |
|---|---|---|
| \(48/7\) | (3,3,-1), (6,-1,0), (9,-5,1) | — |
| \(96/5\) | — | (3,3,-1) |
| \(624/19\) | (1,0,0), (4,-4,1) | — |
| \(96\) | — | (3,-4,1), (7,-1,0) |
| \(192\) | — | (4,-4,1), (6,-1,0) |
| \(400\) | (5,-1,0) | — |
| \(464\) | (5,-4,1) | — |
| \(656\) | (4,-1,0) | — |
| \(720\) | (6,-4,1) | — |
| \(912\) | (3,-1,0) | — |
| \(976\) | (7,-4,1) | — |
| \(6096/5\) | — | (7,-4,1) |
| \(1536\) | — | (1,0,0), (3,-1,0), (5,-4,1), (5,-1,0), (9,-5,1) |
| \(11202\) | — | (4,-1,0) |

At the maximizing sample \(D=978\), the eight directions are
\[
(1,0,0),(3,-1,0),(4,-1,0),(5,-4,1),(5,-1,0),(6,-4,1),(7,-4,1),(9,-5,1).
\]
At \(D\ge11202\), just \((6,-4,1)\) remains. Thus the early positive ray has a new **2→5→4→6→4→2** cascade, before the already-known high-D 8→7→2→1 tail. Changes of \(\eta\)'s rational branch at 48, 144, 336, 1008, 5771, 6923, 7452 need not change \(|N|\).

## Complete finite-to-continuum proof certificate

The attached standalone program \`x6_r128_third_chamber_full_D_ray_verify.py\` performs all computations with integer arithmetic and Python \`Fraction\`, with no sampling assumption.

1. Since \(q(a)\le10\), all \(|x|,|y|,|z|\le10\); selecting the lexicographically larger member of each pair \(a,-a\) exhausts exactly **1,935** nonzero unoriented integer triples.
2. The exact 18-row R121 bank is *revalidated on this full population*: every physical triple \(a\) has a feasible bank row \(b\) with all six \(g_j(b)\le g_j(a)\). Consequently \(\eta(D)\) is the minimum of those 18 scores for **every** positive \(D\).
3. Independently, on all 1,935 triples the code verifies that the R122 20-row envelope consists exactly of rows for which **no** bank row \(b\) has \(2g_j(a)\ge3g_j(b)\) simultaneously for all six pairs. Every other row satisfies \(F_D(a)\ge\frac32F_D(b)\ge\frac32\eta(D)\) for all \(D>0\). Thus **the same 20 rows suffice for every near-set calculation**, with all six pair observations retained.
4. For each bank/envelope direction every score is the maximum of six elementary functions, each a nonnegative constant or \(g/(D+c)\) with integer \(g,c>0\). On an interval where no two relevant elementary functions cross, the active branch of each maximum, the winning minimum and every sign of \(2F_D(a)-3\eta(D)\) are fixed. All possible changes therefore lie among (i) within-row crossings, (ii) bank-vs-bank branch crossings, or (iii) scaled envelope-vs-bank crossings \(2f_a=3f_b\). Solving those one-variable equations *exactly* yields **953 distinct positive rational critical points**. Identically equal branch functions do not change the ordering. No finite upper bound on \(D\) is imposed.
5. The verifier evaluates all **954 open intervals** at exact rational midpoints (and \(D=\text{last root}+1\) on the final unbounded interval), and all **953 critical points** separately. It checks the seven branch switches of Theorem A and exactly 14 membership thresholds of Theorem B; at every critical point, the strict near set agrees with the intersection of the adjacent open-interval sets. This is justified by continuity and the strict sign test, and is also directly checked. In addition, 23 parameter values receive an independent, full **1,935-row** Fraction cross-check.

The decisive property is that all sign-changing events occur among the computed roots. Therefore the finite computation proves the **continuous, unbounded real half-ray** classification, not merely its 23 spot checks. Saved JSON records every membership transition, exact endpoint count and the source script's reproducible assertion outputs.

## Provenance, interpretation and next question

Frozen observer: R121 @8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd (18-row bank), R122 @0687aa24f5402da3b35f914dd6907967a9805b94 (20 near candidates); independent R123 global Port-10 maximum=8 and other chambers are recorded in the 2026-11-23 account foundation router. This theorem extends R127's *different* D-ray method; it does not replace the R127 statement. P000 six native axes, three-dimensional research slice, distinct time and full joint relation/provenance constraints remain in force; here \((x,y,z)\) is the explicitly declared *conditional observer* input and not a complete native six-axis address.

Proof status: author exact parametric finite computation with reproducible code and full mathematical coverage argument; independent scientific review is pending. There is no formal CLAIM/Result/Review asserted for the native X6 time-dynamics Task.

Next unit: classify the remaining two Port-10 maximizing chambers \((136,8,176,D)\) near \(D=185\) and \((722,465,240,D)\) near \(D=48\), or establish a general bound on the number of strict-near crossings along one positive-weight ray. Reuse these exact six-pair certificates instead of restarting the 1,935-row problem.
