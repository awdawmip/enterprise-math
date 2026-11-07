# R5 — Certified complete four-dimensional hull equality at a strictly positive history-sensitive merger

Date: 2026-11-06 Asia/Shanghai. Researcher-ID `EM-DIRECT-C399A0`; activity `RA-A1EF4B8DCE437AB79704415D`.
Author status: **AUTHOR_COMPUTER_ASSISTED_EXACT_PROOF / FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**.

## Statement

In the four-stage strictly positive finite P/Q BRC specified in `RESEARCH.md`, fix `δ=1/4`. The history-0/time-3-ratio-1 terminal Q row is exactly `(47/180, 43/90, 47/180)`.

The other Q kernels, P transition formula `P(child|history)=Q(child|history)*r_child/r_parent`, likelihood-ratio observations, stop/declaration choices, and four-observer vector `W=(P[declare Q], Q[declare P], E_P[tau], E_Q[tau])` are unchanged. Full-history policies may condition on all past branch identities. Seedless LR policies condition only on (time, likelihood ratio); both allow all real randomized behavioral rules and either terminal P/Q declaration.

**Theorem (exact complete O4 hull equality):** `conv O4(FULL_HIST) = conv O4(seedless LR)`.

The quantifier covers **every real direction in four dimensions and every legal real behavior policy** of the model, including all stop decisions and both P/Q declarations. This completes the *hull-equality half* of the R5 mother objective for an explicitly history-nonlumpable strictly positive P/Q kernel. The *actual real-behavior image inequality* remains the next independent question.

## Exact rational certificate: 80 halfspaces, 82 vertices

The accompanying `H_FACETS.txt` is a fixed immutable integer certificate: each of its **80 rows** `n1 n2 n3 n4 c` encodes the halfspace `n·(720000 W)<=c`. The certificate was proposed by an ordinary convex-hull candidate-generation step, and is accepted only after the exact independent checks below. `VERIFY_HULL.py` is a standalone Python-standard-library verifier reading that certificate; it requires neither NumPy nor SciPy.

1. **Exhaust seedless deterministic policies.** There are `3 * 3^2 * 3^3 * 2^3=5832` complete seedless deterministic strategies: time-1 Q/P/continue; two time-2 Q/P/continue decisions; three time-3 Q/P/continue decisions; three time-4 Q/P declarations. The verifier computes all four observables with exact `Fraction`, yielding **806 distinct** four-vectors, all with common coordinate denominator dividing **720000**. Denote their integer-scaled set by `P`.

2. **Exact containment P in H.** Evaluate every one of the 80 integer inequalities against each of the 806 points, asserting `n·p<=c`. The halfspace set explicitly contains the eight coordinate box bounds `0<=W1,W2<=1` and `1<=W3,W4<=4`, so `H` is compact. Exact rank checks establish `P` affinely spans four dimensions.

3. **Complete exact H-vertex enumeration.** Choose an LR point with four linearly independent active facet normals; it is a vertex of H. At each discovered vertex, enumerate **every triple of active hyperplanes**, compute its exact null direction from 3-by-3 determinant minors, retain both orientations satisfying all active tangent inequalities, and walk by the first **exact rational** intersection with any remaining bounding inequality. Each actual polytope edge lies in at least three linearly independent active hyperplanes; the 1-skeleton of a bounded convex polytope is connected. Consequently this exact graph traversal reaches *every* H vertex. The verifier finds **82** H vertices, with **19,108** active-facet triples attempted and **2,560** admissible edge traversals; each of the 82 vertices belongs to the exact seedless deterministic set `P`. Since all LR points belong to H, and every H vertex is itself a deterministic LR point, the exact set identity is `H = conv(P) = conv O4(seedless LR)`.

4. **All FULL observations lie in H.** For every one of the 80 exact H facet normals n, calculate the maximal FULL_HIST directional observation value by exact backwards Bellman induction on the complete history-distinguished P/Q tree; assert `720000*h_FULL(n)<=c`. All **80** pass. Since H is the intersection of precisely those 80 halfspaces, every full-history observation lies in H. Conversely every seedless LR policy is a legal FULL_HIST policy. Thus both convex hulls equal H, proving the theorem.

5. **Real behavioral policy support scope.** At every time-key, actions form a probability simplex. Because time strictly increases, along a single path an action key cannot recur. The expected four-observer directional payoff is separately affine in each simplex's decision vector, so successive maximization over their compact vertices attains a deterministic strategy. This applies independently to the seedless LR and fully history-observing strategy classes. Consequently no unenumerated real-behavior strategy enlarges their convex hulls.

Exact executed output:

```text
H_vertices= 82 max_active= 38 edge_tests= 2560 triples= 19108
PASS_CERTIFIED_R5_DELTA_1_4_ALL_DIRECTION_HULL_EQUALITY
exact_H_inequalities= 80 LR_deterministic_unique= 806 scale= 720000
all_FULL_Bellman_facets_checked= 80
Proof: every LR point lies in bounded H, every H vertex enumerated via exact active-triple edges and lies in LR; every FULL support facet <= H.
```

**Reproduction:** put `VERIFY_HULL.py` and `H_FACETS.txt` together in this directory and run `python VERIFY_HULL.py`. Exact expected stdout is `EXACT_HULL_OUTPUT.txt`. This check is a computer-assisted finite proof (exact integer and rational arithmetic, complete finite search with a graph-completeness argument), separate from the earlier one-direction continuous-δ analytic phase theorem in `RESEARCH.md`.

## Relevance to the R5 mother question

The kernel depends on hidden past history at the nonterminal observed node `(t=3,r=1)`, and both histories have strictly positive Q mass there. Their conditional terminal distributions are genuinely different; the seedless LR observation projects away their distinguishing history. Yet the full **four-dimensional convex hull** of complete error/time observations is exactly the same for both strategy classes. This establishes a concrete all-directions information-equivalence geometry while retaining underlying history-dependent transitions.

**Still open:** find `W* in O4(FULL_HIST)\setminus O4(seedless LR)` and establish non-membership with an exact all-real certificate, or prove equality of actual images for this δ=1/4 model. A proven image difference in this exact model would close the R5 mother construction. Useful options: constrain a candidate W* to an exposed face of H and characterize the seedless LR behavioral image there; derive exact polynomial elimination of continuation and declaration variables; or search topology/parameter variants while keeping this all-hull certificate as a positive control.

## Governance, pins, provenance

Scientific sources frozen GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`; previous exact R5 frontier EM `794d893322b77898858c657f90f2674c432eb87d`. P000, ACTIVE HEARTBEAT_WORLD, joint relation/observer preservation and project portable research route govern this work. Finite P/Q stopping experiments are auxiliary typed BRC observers; no X6 physical embedding, theorem promotion, formal Task CLAIM, Result or independent review is inferred. The proof and code are original author-side research and exact author-executed verification, pending independent mathematical inspection.
