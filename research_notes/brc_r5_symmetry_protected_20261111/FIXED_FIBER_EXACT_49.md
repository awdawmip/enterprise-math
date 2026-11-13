# R5 — Exact census: 49 four-circuit adjacent edges in the fixed physical fiber

Date: 2026-11-11 (Asia/Shanghai). Status: new author-side exact finite theorem with runnable Fraction verification and explicit physical witness. This note supersedes the **suggested future incidence procedure** in the earlier `RESEARCH.md` / `FIXED_FIBER_EDGE_INCIDENCE.md`; their general statements remain valid. Source and frozen science unchanged: GK `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Predecessor physical witness from [R5 PR #2017](https://github.com/awdawmip/enterprise-math/pull/2017), independently used for [PR #2021](https://github.com/awdawmip/enterprise-math/pull/2021) and [PR #2038](https://github.com/awdawmip/enterprise-math/pull/2038).

## Exact theorem and frozen mathematical object

Let C be the frozen rank-15 observation matrix on the 30 allowed transfer arcs. Fix the exact strictly positive physical witness E0 contained in the attached immutable-source-derived `WITNESS.txt`, and its right-hand side B=CE0. Let F_B={E in R_{≥0}^{30}:CE=B}. The first result in this PR classified 14832 possible complete 14-arc K4+double-edge signed kernel circuits, each of minimum six-arc-atom word length 4.

**Theorem.** In this **single fixed physically legal fiber F_B**, there exist **exactly 49 different edges whose endpoint differences have six-arc K2,3 residual word length 4**. Their signed direction supports are K4+one-high/high-double-edge 14-arc circuits. The 49 edges split by the choice of low-degree source pair as follows:

| Low source pair | Full abstract 14-arc candidates | Physically realized edges |
|---|---:|---:|
| (1,2) | 2472 | 15 |
| (1,3) | 2472 | 0 |
| (1,5) | 2472 | 15 |
| (2,3) | 2472 | 0 |
| (2,5) | 2472 | 19 |
| (3,5) | 2472 | 0 |
| **Total** | **14832** | **49** |

The exact count is an exhaustive finite computation backed by the following structural reduction, integer data, rational row elimination, strict-interval test, and endpoint checks.

## Proof 1 — every sharp edge has exactly the same two stationary arcs

In the frozen allowed-arc list D, source 0 has the **single** arc (0,0), and source 6 has the **single** arc (6,6). Their masses are forced by the source marginal components of B to equal the strictly positive constants
```
E00 = 219346331/10192753200
E66 = 451274777/3397584400.
```
Every nonzero K4+double-edge direction has all its 14 arcs on variable sources J={1,2,3,5}; these two singletons are stationary and strictly positive on every edge of F_B.

For a 14-arc candidate signed circuit S, rank(C_S)=13. Let U be the positive support of an edge's relative interior. By the general exact face rank lemma (proved in `FIXED_FIBER_EDGE_INCIDENCE.md`), U=S union T, rank(C_U)=13+|T|, |T|<=2. Since the two singleton arcs are always in T, **T is exactly {(0,0),(6,6)}**. These columns increase rank by two because their source-marginal rows are supported on source 0 and source 6 and vanish on all columns in S.

Consequently, each of the 14832 direction supports has exactly **one** possible relative-interior support, consisting of 16 arcs: S plus the two invariant singletons. This eliminates the generic 120-combination stationary-lift search. If a strictly positive 16-arc solution exists, it is the relative interior of exactly one edge, with both endpoints vertices.

## Proof 2 — reduce each 16-arc face to seven rational split variables

For each target i=0,...,6, the K4 labeled multigraph selects a unique pair of the four variable source ports (j_i,k_i). On that target's two edges write the *scaled* masses
```
E(i,j_i)*L = t_i,
E(i,k_i)*L = M_i-t_i,
L=10192753200.
```
The two stationary singleton masses are fixed separately. Scale by L to make all frozen witness input masses and marginal right-hand sides integral. The exact constants derived directly from `WITNESS.txt` are
```
M = [751692825,2277885600,1752301200,1510577788,
      926913000,648519300,751692825]
SM = [2557928025,825388200,4307704588,928561725]
SW = [25579280250,12380823000,86154091760,27856851750].
```
Here SM_j=sum_i L*E0(i,j), SW_j=sum_i R_i*L*E0(i,j) for j in J, and R=(2,10,15,20,25,30,38) are ratio numerators. Source mass and first moment constraints in the frozen 21-observation model are precisely
```
sum_{i: j_i=j} t_i + sum_{i: k_i=j}(M_i-t_i) = SM_j
sum_{i: j_i=j} R_i*t_i + sum_{i: k_i=j}R_i*(M_i-t_i)=SW_j
```
for j in J. These eight linear equations in seven t_i have rank six for every full circuit S (the two universal redundancies are total target mass and target-weighted mass). They have an affine one-parameter solution t_i=alpha_i+beta_i*t, obtained by exact Fraction Gauss-Jordan elimination. The source 0/6 constraints are already satisfied by their fixed singletons; target marginal constraints are built into each split.

The support is strictly positive exactly when
```
0 < alpha_i+beta_i*t < M_i    for all i=0,...,6.
```
Because the signed circuit has full 14-arc support, all beta_i are nonzero. Therefore these inequalities reduce to a single **exact rational open interval** (t_min,t_max). It is nonempty iff t_min<t_max. In that case the endpoints t=t_min,t_max are nonnegative transfers; rank(C_U)=15, |U|=16 proves their connecting segment is a one-dimensional face, hence an edge. Thus the interval test is necessary and sufficient, with one edge per feasible labeled support S.

## Complete finite check and actual observed data

The script `COUNT_FIXED_FIBER_SHARP.py` reads the accompanying immutable predecessor `WITNESS.txt` and enumerates six source low pairs times 7!/2=2520 target labelings. For each assignment it first excludes the 288 degenerate flows using the original polynomial formula, and then applies the **exact integer/rational** affine solver and open-interval test for the remaining 14832 supports. Every one of the 49 successful candidates is independently checked at both endpoints **and at the segment midpoint**, reconstructing all seven target marginal masses, all six source masses, all six source ratio moments, and nonnegativity. This is the entire original 21-row observer: the source moment relative to r_j follows by subtracting r_j times the checked source mass. No floating-point tolerance, random sampling or numerical solver is used.

Run from the directory containing both files:
```bash
python3 COUNT_FIXED_FIBER_SHARP.py
```

Observed output in `FIXED_FIBER_CENSUS_OUTPUT.txt`: `ACTUAL_FIXED_FIBER_SHARP_EDGES 49`, `TOTAL_FULL_SHARP_CIRCUITS 14832`, and `PASS_EXACT_FIXED_FIBER_SHARP_CIRCUIT_EDGE_CENSUS_49_WITH_ENDPOINTS`.

A fully explicit first edge certificate has low source pair (1,2), target label assignment (A,B,C,D,E,F,G)=(0,3,1,2,6,4,5), and open split-parameter interval
```
50201289450/181 < t < 298056850.
```
The midpoint split variables for i=0,...,6 (scaled by L) are
```
(43924081175/181, 383921626410/181, 5188154400/181,
 35139264940/181, 811620680, 82537509860/181, 52074789650/181).
```
These reconstruct a strict positive 16-arc interior point; the exact interval endpoints reconstruct the two different adjacent vertices. Both singleton masses remain fixed. The full verifier checks all 49 analogous endpoint witnesses even though the output prints only this representative.

## BRC and scientific scope

Observer equivalence (the same 21 marginal/first-moment readings) does not determine the signed branch difference, the labeled source/target incidence or which transfer faces are feasible. The repair information is the retained signed branch-incidence support plus the scalar edge coordinate. The **14832** abstract possible circuit types and the **49** actual edges for one frozen physical fiber are different cardinalities with different quantifiers.

This is an exact fixed auxiliary-model result. It does not modify the protected six-dimensional P000 native world nor assert physical realization beyond the frozen Blackwell physical constraints already checked in the predecessor witness. The present result is published as author-side proof and exhaustive exact evidence, not independently reviewed or canonically accepted as a Source Result.

## Next question

Explore the 49-edge subnetwork: enumerate its 98 endpoint vertices and deduplicate them by exact 30-dimensional transfer vectors; determine component sizes, intersecting circuits and K2,3 word-length transitions. Compare the adjacency/rank result to the previously observed 1775-vertex radius-four neighborhood, including possible overlaps. Separately classify 288 symmetry degeneracies' 12-arc directions and their actual incidence in this same fiber, yielding a precise picture of which resonant structures survive physical constraints.