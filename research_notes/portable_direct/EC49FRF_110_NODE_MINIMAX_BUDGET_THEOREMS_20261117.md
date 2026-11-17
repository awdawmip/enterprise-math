# EC49FRF — 12 exact native BRC price seams, 110-node interval certificate, optimal multi-gap sampling allocation

Date: 2026-11-17. Evidence level: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.
Parent: [EC49FRE PR #2607](https://github.com/awdawmip/enterprise-math/pull/2607), commit `e2f8e0c5f1ac33773ac4a5f714ba22ccb4da9ce9`.
Frozen scientific source: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (unchanged).
Complete author proof, original data, original and independent code, all 12 complete native JSON certificates, full rerun logs, inherited full evidence and 49-file SHA256 manifest: **EC49FRF_12_SEAMS_110NODE_BUDGET_ALLOCATION_FULL_EVIDENCE_20261117.tar.xz**, SHA256 `0a72208882510bb7c4cd107203abe8a9fa8045eb1ff5ab4251b9ad05f3087631`, attached to the originating research conversation. This GitHub file is a complete mathematical statement/proof; the raw ~16MB uncompressed data are in the referenced immutable bundle, not claimed to be stored in the PR.

## Typed native BRC model

Original class 16943: 310 configurations, 141 distinct **complete physically named profiles**, 228 legal physically labeled sensing actions (144 terminal, 84 root), yielding 209 distinct response partitions. Distinct physical first labels are retained when partitions coincide. For profile i with multiplicity m_i, use the positive prior `p_i(λ)=(1−λ)/141+λ*m_i/310`, `0≤λ≤1`, `Σm_i=310`. Root observation costs `r=xt`, terminal `t>0`, `x≥1`.

Let `V(x,λ)` be the global minimum expected price of a finite adaptive separating tree over *all* 228 legal physical queries. The three feasible candidate trees have normalized costs
```
A(x,λ)=(1−λ)(6x+290)/141 + λ(6x+751)/310
B(x,λ)=(1−λ)(5x+293)/141 + λ(5x+704)/310
C(x,λ)=(1−λ)(5x+295)/141 + λ(5x+685)/310
K(x)=7557−169x, G(x)=310(3−x)/K(x), β=620/3299.
```

### Theorem 1. Twelve additional fully classified continuous-prior slices

For all `λ∈[0,1]` at each of the following prices `x`, the full finite adaptive Bellman optimum is `V(x,λ)=t*min(A,B,C)`, **using the inherited exact endpoint and named-first-action exclusion lemmas at their stated scopes**.

| x | first critical prior λ=G(x) | exact integer Bellman optimum at G(x) |
|---|---|---:|
| 107/64 | 5270/93113 | 559087966080 |
| 109/64 | 25730/465227 | 2794539054720 |
| 111/64 | 8370/154963 | 931212759680 |
| 113/64 | 24490/464551 | 2792737503360 |
| 115/64 | 23870/464213 | 2791836727680 |
| 117/64 | 62/1237 | 7442495872 |
| 119/64 | 22630/463537 | 2790035176320 |
| 121/64 | 22010/463199 | 2789134400640 |
| 123/64 | 230/4977 | 29981006720 |
| 125/64 | 20770/462523 | 2787332849280 |
| 127/64 | 4030/92437 | 557286414720 |
| 129/64 | 6510/153949 | 928510432640 |

The integer minimum multiplies the normalized expected price by `64*310*141*denominator(G(x))`. Every critical seam has first-action tie set exactly `{32,34,140,142}`, and every tied tree was fully replayed. The optimal named first-query sets for real λ are: `{32,34}` on `[0,G(x))`, `{140,142}` on `(G(x),β)`, `{16,23}` on `(β,1]`; at each critical point take the union of adjacent sets.

**Proof and finite-completeness argument.** The frozen original data reconstruct exactly the 141 complete profiles and 228 physically named queries. For each 12 critical rational pairs, integer-cost Bellman recursion considers all separating queries at every recursively reachable non-singleton response fiber. Strictly positive per-query costs eliminate non-splitting loops, and every useful query decreases the fiber cardinality, so this recursion includes every finite separating adaptive tree. Its optimum, first-action costs and four tied trees were recomputed by a second, independently implemented weighted-subset DP; all 12 independent checks passed for all 228 physical first labels. For each *fixed* price x, every fixed decision tree has cost affine in λ, so V is a concave lower envelope. Equality of an affine feasible candidate with V at both ends of a λ-interval entails equality throughout it. Combining the newly computed G(x) critical endpoints with the previously certified λ=0, λ=β and λ=1 endpoints and named-label exclusion lemma establishes the phase classification above. The inherited endpoint and label lemmas remain an explicit proof dependency and are author-side, not independently project-admitted. QED under these inherited certified dependencies.

### Theorem 2. Globally optimal finite-budget allocation across multiple old price gaps

Take any existing finite certified price grid `1≤p_0<...<p_M≤3` and fix a finite budget `m≥0` additional **real** price knots. For gap `I_j=[a_j,b_j]`, define `L_j=log(K(a_j)/K(b_j))>0`. Allocate `n_j≥1` subintervals, `Σ_j(n_j−1)=m`. The gap's unique grid simultaneously minimizing its internal strip-area upper bound and maximal normalized-regret upper bound is the equal-log-K grid:
```
K(x_{j,k})=K(a_j)^(1−k/n_j) K(b_j)^(k/n_j),  k=0,...,n_j.
D=2185500; c=169.
F_j(n)=(2D/c²)*n*(cosh(L_j/n)−1)
Q_j(n)=(50/c)*tanh(L_j/(4n)).
```
Here F_j is the minimal total *uncertified-strip area enclosure* inside gap j with n subintervals; Q_j is its minimal maximum normalized-regret upper bound. These are parameter-domain analytic functions, not physical Heartbeat rotations or BRC sensing operators.

**For total enclosed area**, the globally optimal integer allocation for *every* m is obtained by repeatedly incrementing n_j on a gap maximizing the currently available marginal `Δ_j(n)=F_j(n)−F_j(n+1)`, and then respacing that gap to equal log K. The marginal sequence is positive and strictly decreasing.

**For global maximum regret**, the globally optimal allocation for every m is obtained by repeatedly incrementing n_j at a current maximum of `L_j/n_j`, respacing to equal log K. Equivalently let
```
h_m=min {h>0 : Σ_j(max(1,ceil(L_j/h))−1) ≤ m}.
```
Then the smallest achievable global maximum normalized-regret bound is exactly `(50/c)*tanh(h_m/4)`.

**Proof.** For any n subintervals of one gap, define positive log-increments `y_k=log(K(x_{k−1})/K(x_k))` with sum L. The exact area identity is `(2D/c²)Σ_k(cosh(y_k)−1)`, so strict Jensen convexity uniquely minimizes the sum at all `y_k=L/n`. The exact regret upper bound for one increment is `(50/c)tanh(y_k/4)`; its strict increase in y uniquely minimizes the maximum at equal increments. With y=L/n,
```
F'_j(n)=(2D/c²)[cosh(y)−1−y*sinh(y)]<0,
F''_j(n)=(2D/c²)(L_j²/n³)*cosh(y)>0.
```
Therefore each gap's discrete marginal improvements decrease in n. Selecting the m largest accessible marginal improvements is globally optimal by the standard exchange argument: replacing a smaller selected marginal by a larger unselected available marginal decreases total area, contradiction. For minimax, a target maximum log-increment h is feasible exactly if each gap receives `n_j≥max(1,ceil(L_j/h))`. The threshold inequality follows, and incrementing the currently largest L_j/n_j never expends a node on a gap already below the target while some gap is still above it. Thus the described greedy allocation attains the optimal threshold with m nodes. QED. The two allocation objectives need not yield the same integer allocation for arbitrary grids.

### Theorem 3. Exact 12-node budget allocation and rational 110-node result

For the inherited 98-node grid, exact rational comparisons of `K(a)/K(b)` show the 12 largest log-K gaps are the consecutive original intervals `[53/32,27/16],...,[2,65/32]`, all length 1/32. Exact squared-ratio comparisons show that half of every selected gap's log-length is shorter than the 13th-largest gap. Hence the global minimax budget allocator of Theorem 2 assigns **one extra knot in each of precisely those twelve gaps**. The chosen *rational* new knots (arithmetic midpoints of the selected intervals) are
```
107/64,109/64,111/64,113/64,115/64,117/64,
119/64,121/64,123/64,125/64,127/64,129/64.
```
The **integer allocation** is globally minimax-optimal among all allocations of twelve ideal real nodes; the displayed rational knot positions are close feasible approximations, not falsely identified with the unique exact real equal-log-K knots.

After native Bellman certification of all twelve new knots, the full exact geometric enclosure is:
```
node count=110; adjacent intervals=109
S98 =296902200973874060795/160864097511408031554912
S110=259924479610030238135/162277343928838082317536
S98−S110=13113000/53754785413 >0
certified rectangle fraction ≥ 324294763378066134396937/324554687857676164635072
certified percentage ≥ 99.91991350322938%
new unique worst upper-regret interval=[13/8,53/32]
```
The 109 radical regret bounds are ordered by rational outward integer-square-root brackets at precision `10^−40`. For all `x≥1,0≤λ≤1,t>0` (reusing the inherited x≥3 certificate),
```
0 ≤ t*min(A,B,C)−V(x,λ)
  ≤ 50t*(53/32−13/8)/(sqrt(K(13/8))+sqrt(K(53/32)))²
  ≈ 0.0000536592398468369543*t.
```
The preceding bound was ~`0.00005413048225249587545*t`, so this *certified upper bound* fell by about 0.87%. The 110-node exact source program and full numeric outputs are in the complete archive. The 109 remaining narrow strips still require a parameterized Bellman lower bound or an exact counterexample; improving an enclosure is not itself proof that a candidate tree is universally optimal.

## Reproduction / provenance / next precise question

Pinned inputs: `frozen_original_master.txt` SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; `EC49FPG_PROFILE.csv` SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. The full package includes native solver `EC49FQL_ALL_FIRST_BELLMAN.py`, separate `EC49FRC_INDEPENDENT_VERIFY.py`, 12 complete certificates, three independent batch outputs, exact `EC49FRF_GEOMETRY.py`, and all inherited science. Execute:
```
python EC49FRF_GEOMETRY.py
PYTHONPATH=code python code/EC49FRC_INDEPENDENT_VERIFY.py 0 4
PYTHONPATH=code python code/EC49FRC_INDEPENDENT_VERIFY.py 4 8
PYTHONPATH=code python code/EC49FRC_INDEPENDENT_VERIFY.py 8 12
```
All tests above actually ran and passed on the included exact bytes; package manifest verified 49 file SHA256 digests and sizes. Preserved P000: six native spatial dimensions, independent time and three-dimensional native slice, no invented two-dimensional native plane; sensor-grid analytic functions only compare prices and do not collapse named source observations.

Current exact task-publication directory `research_task_records/RS-EC49AS` was absent (GitHub main 404 read on 2026-11-17), matching earlier native `unknown current immutable task publication`. This publication is **independent portable research**, not a formal shared-task CLAIM/Result/Review or proof admission; no shared owner was displaced. No currently authenticated Researcher-ID/Activity scientific checkpoint is asserted from an historical ID.

**Next:** derive a uniform *parametric* Bellman lower bound across the remaining 109 strips, or find one exact physically labeled adaptive tree with cost below `t*min(A,B,C)`. The new worst enclosure interval `[13/8,53/32]` provides a concrete discriminating test.