# X6 R129 — exact Port-10 six-pair BRC D-ray at (136,8,176,D)

Date: 2026-11-23 (Asia/Shanghai). Status: **AUTHOR EXACT PARAMETRIC FINITE PROOF / PYTHON FRACTION REPLAY PASS / NOT INDEPENDENTLY REVIEWED**.
Scope: the *conditional* four-positive-weight, six-pair BRC observer only; no claim of native X6 time/rotation dynamics, physical evidence or accepted Foundation theorem.

## Frozen definitions

Let \(a=(x,y,z)\in\mathbb Z^3\setminus\{0\}\), identify \(a\sim-a\), but do **not** identify positive integer multiples. Let
\[
q(a)=\max\{\sum_i\max(a_i,0),\sum_i\max(-a_i,0)\},
\quad h(a)=(0,x+3y+6z,3x+12y+30z,7x+39y+126z).
\]
Use all six gaps \(g_{ij}=|h_i-h_j|\) for \(01,02,03,12,13,23\). At Port \(p=10\) and **every real \(D>0\)** fix \(w=(A,B,C,D)=(136,8,176,D)\), so that
\[
F_D(a)=\max\left\{\frac{g_{01}}{144},\frac{g_{02}}{312},
\frac{g_{03}}{D+136},\frac{g_{12}}{184},
\frac{g_{13}}{D+8},\frac{g_{23}}{D+176}\right\},
\quad \eta_{10}(D)=\min_{0<q(a)\le10}F_D(a),
\quad N_{10}(D)=\{\{\pm a\}:0<q(a)\le10,\ 2F_D(a)<3\eta_{10}(D)\}.
\]
The triple is a declared *observer input* in a selected three-axis slice, not a final native six-axis Cell address; P000 is unchanged.

## Theorem 1: complete all-real optimizer

\[
\boxed{\eta_{10}(D)=
\begin{cases}
3/(D+136),&0<D\le8,\\
1/48,&8\le D\le280,\\
6/(D+8),&280\le D\le544,\\
1/92,&544\le D\le1096,\\
12/(D+8),&D\ge1096.
\end{cases}}
\]
The neighboring formulas agree at the four shared endpoints. An optimizer witness can change without changing the near-direction set.

## Theorem 2: exact strict 3/2 near-direction fan

| Real \(D\) | \(|N_{10}(D)|\) |
|:---|---:|
| \(0<D\le184\) | 2 |
| \(184<D<304\) | **8** |
| \(304\le D<406\) | 6 |
| \(406\le D<424\) | 5 |
| \(424\le D<544\) | 4 |
| \(544\le D\le728\) | 3 |
| \(728<D<1288\) | 5 |
| \(1288\le D<1648\) | 4 |
| \(1648\le D<2584\) | 2 |
| \(D\ge2584\) | 1 |

For the exact sets start at \(0<D\le184\) with
\(N_0=\{(4,-4,1),(6,-1,0)\}/\pm\), and process these **precise** membership events:

| Exact threshold | Enter strictly to the right | Exit at equality |
|:---|:---|:---|
| 184 | (1,0,0), (1,3,-1), (5,-4,1), (5,-1,0), (7,-1,0), (9,-5,1) | — |
| 304 | — | (1,3,-1), (7,-1,0) |
| 406 | — | (4,-4,1) |
| 424 | — | (6,-1,0) |
| 544 | — | (9,-5,1) |
| 728 | (4,-1,0), (6,-4,1) | — |
| 1288 | — | (5,-1,0) |
| 1648 | — | (1,0,0), (5,-4,1) |
| 2584 | — | (4,-1,0) |

At **D=185**, exactly eight near directions are
\((1,0,0),(1,3,-1),(4,-4,1),(5,-4,1),(5,-1,0),(6,-1,0),(7,-1,0),(9,-5,1)\);
the optimum is exactly \(1/48\).
For every \(D\ge2584\), the unique unoriented near direction is \((6,-4,1)\). The late \(728\) crossing is genuine re-entry (3→5), not an optimizer change.

## Exhaustiveness proof

1. Exactly **1,935** nonzero unoriented integer triples satisfy \(q(a)\le10\): enumerate each coordinate in \([-10,10]\), keep \(a>-a\) lexicographically and enforce the exact Port bound. This is the full finite population, with no primitive-vector quotient.
2. The 18 physical vectors of frozen R121 were independently rechecked to dominate **every** such triple componentwise in the six gap coordinates. Because all six weight denominators are positive, this proves \(\eta_{10}(D)=\min_{b\in B_{18}}F_D(b)\) for **all** \(D>0\), not just tested values.
3. Recheck R122's 20-row envelope against all 1,935 triples. Each triple outside \(E_{20}\) has some \(b\in B_{18}\) with \(2g_j(a)\ge3g_j(b)\) for every six-pair index \(j\). Thus \(2F_D(a)\ge3F_D(b)\ge3\eta_{10}(D)\) for every \(D>0\); no discarded row can be strictly near. No pair observation is dropped.
4. For each retained row and pair, its elementary score is either a rational constant or \(g/(D+c)\). In an open interval containing **no** equality root between: (i) two atoms of the same row; (ii) atoms of any two bank rows; and (iii) \(2f_a=3f_b\), near-envelope atom \(a\) vs bank atom \(b\), neither the active maximum, the minimizing bank atom, nor strict nearness can change. All possible positive rational roots of these equalities were solved exactly using cross multiplication; there are **753 distinct positive roots**, hence **754** complementary open intervals, including \((\text{last root},+\infty)\). Identical functions do not create an isolated event.
5. Exact Python \`Fraction\` evaluates all **754 intervals** and each **753 root points**. The only membership changes are the nine listed thresholds; the only optimizer-formula changes are \(8,280,544,1096\). The near set at every critical point is the intersection of its adjacent open-interval sets, checked rather than assumed. **17** representative values (all 12 distinct membership/optimizer threshold points plus five other values) were independently crosschecked against the **full 1,935-row population**, not merely the reduced bank/envelope. Exact script and JSON summary accompany this note.

The finite computation and the root-completeness argument establish the continuum-\(D\) classification *within the declared model*. No independent author/reviewer or native Result admission is claimed.

## Provenance and continuation

Frozen scientific inputs: [R121 18-row optimizer](https://github.com/awdawmip/enterprise-math/blob/8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd/research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md) and [R122 20-row near envelope](https://github.com/awdawmip/enterprise-math/blob/0687aa24f5402da3b35f914dd6907967a9805b94/research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json). Method comparison: [R128D all-positive D-ray](https://github.com/awdawmip/enterprise-math/blob/c29ac99aa69ba2b6850f34af490672811bbbf1ee/research_notes/portable_direct/2026-11-23_r2_x6_r128_third_maximizer_full_D_ray.md) fixes **different** first three weights (240,577,48), so this is an independent **new parameter-ray classification**, using the same exact root-sweep technique, not a novel new algorithm.
Native X6 Task \`RS-X6-NATIVE-TIME-DYNAMICS\` retains its own Source/CLAIM/Result. This note is portable *informed auxiliary research*, not a CLAIM, PROGRESS, REVIEW or promotion.

Next useful independent unit: complete the remaining \((722,465,240,D)\) positive ray around \(D=48\); examine transverse stability of the \(184<D<304\) eight-direction chamber; and check independent mathematical review of this exact proof.