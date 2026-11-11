# R709 — Port-filtered X6 triads: minimal fractional/integral obstruction and exact source repair

Date 2026-11-11 Asia/Shanghai. Task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`. Frozen scientific pin `a72226e2430ffa4786321ac86e7f0c599d5f0389`. Source predecessors: R707 PR #2033 and R708 PR #2042. This work is an independent author-side candidate-model derivation, not a formal Result or native `TRIADIC_CLOSURE_E` claim.

## Definitions

At a Cell `c` in the X6 affine torsor, take `3m` individually labeled nonzero primitive tokens of common positive magnitude `q`, distributed among six signed native axes with unsigned axis counts `n=(n_0,...,n_5)` and `sum n_i=3m`. Retain each token's sign/path/branch identity in the source carrier. A candidate *allowed triad state* `H⊆C({0,...,5},3)` declares which three-distinct-axis combinations may form an equal-q primitive closure block. This H is a typed hypothetical port filter; native Link/Port/V29/V39 reachability remains to be established.

Let `D_H(n)` count partitions of all individually labeled tokens into unordered admissible three-token blocks. For `m=0`, `D_H(0)=1`.

## Theorem 1 — exact labeled source-count formula

Write `F_H(x)=∑_{T∈H}∏_{i∈T}x_i`. For each nonnegative `n` with `∑n_i=3m`,

`D_H(n) = (∏_{i=0}^5 n_i! / m!) [x_0^{n_0}...x_5^{n_5}] F_H(x)^m.`

**Proof.** Expand the mth power as an ordered list of m admissible axis triples. For each axis i, allocate its n_i distinct token labels bijectively to the n_i appearances of i in that list, obtaining n_i! assignments. Every unordered partition has exactly m! orderings of its blocks, so division by m! gives each source once. The empty case follows by convention. When H consists of all twenty triples, this is precisely the R707 formula. QED.

For `n=(1,1,1,1,1,1)`, `m=2`, a cover exists iff H contains a complementary pair `T,V\T` (V={0,...,5}). More precisely,
`D_H(1^6)= 1/2 ∑_{T∈C(V,3)} 1_H(T)1_H(V\T)`.

## Theorem 2 — sharp port-filter counterexample

Take `P={012,034,135,245}`, where e.g. 012 abbreviates the unordered set {0,1,2}. Every pair of these four triples meets in exactly one axis; every axis occurs in exactly two of them. Consequently, P contains no complementary pair and `D_P(1^6)=0`. Nonetheless `max_i n_i=1≤m=2`, so the R708 unfiltered saturation criterion alone does not decide this port-filtered existence problem.

For the fractional incidence system `w_T≥0`, `∑_{T∋i}w_T=1` for each of the six axes, the explicit witness `w_T=1/2` for each `T∈P` satisfies all six equations. Therefore the fractional system is feasible while the exact integer partition has no solution. The four-triple/six-point incidence is the classical **Pasch configuration** (quadrilateral), a known object in Steiner-triple-system literature.

## Theorem 3 — minimal support and uniqueness

For every family H of distinct three-axis triples on six axes possessing a nonnegative fractional perfect cover but **no two disjoint permitted triples**, the positive-weight support S of every fractional witness satisfies `|S|≥4`. At equality, S is isomorphic under axis permutation to P and its positive fractional weights are uniquely all 1/2.

**Proof.** If any axis i belongs to only one positive-weight triple E, the equality at i forces `w_E=1`. At every axis of E the incidence equation is already saturated; hence any other positive-weight triple must be disjoint from E, contradicting the no-disjoint-triples condition. Each axis must therefore appear in at least two positive support edges. Counting incidences gives `3|S|≥6·2=12`, so `|S|≥4`.

At `|S|=4`, the total incidence number is exactly 12, forcing every one of the six axes to have support degree exactly two. Counting pairwise edge intersections gives `∑_i C(deg(i),2)=6`. There are six pairs of support triples and each pair intersects, so each pair intersects in exactly one axis. Thus the six axes are in bijection with six unordered pairs of four edge labels, uniquely determining P up to relabeling. The axis shared by two arbitrary support edges E,F has degree two, so `w_E+w_F=1`. The pairwise equations on any triangle of edge labels imply `w_E=1/2` for all edges. Conversely P with these weights is a valid fractional certificate and has no disjoint pair. QED.

There are exactly `6!/4!=30` labeled copies of P, because its automorphism group permuting its four hyperedges is S4 of order 24. Enumeration of all `C(20,4)=4845` four-edge families and all 720 six-axis permutations verifies the 30 configurations form exactly one orbit. This theorem classifies the **minimum positive support**; larger-support fractional counterexamples need not be Pasch.

## Theorem 4 — exact source residual and smallest one-triple repair

In the explicitly stated finite-source candidate sampler, the ordered choices `(E,F)∈P×P` each carry formal rational positive weight 1/16 and independent source IDs. Define the **incidence observer residual** `R(E,F)=∑_{i=0}^5 |1_{i∈E}+1_{i∈F}-1|`. This is a count mismatch observer, *not* signed-force cancellation.

For distinct E,F in P, exactly one axis repeats and one axis is missing, so R=2. For E=F, R=6. The 16 ordered source pairs split as 12 with R=2 and 4 with R=6; none has R=0.

Choose E∈P, enable its missing complement `E^c=V\E` and set `P'=P∪{E^c}`. The unique complementary pair in P' is {E,E^c}; hence `D_{P'}(1^6)=1` and adding **one** permitted triad is the minimum repair. Under independent uniform choices of the five *named* permitted sources, exactly two of 25 ordered branches (E,E^c) and (E^c,E) have R=0, giving observer weight `2/25`. If the first step is fixed to E, one of five second-step branches completes it, giving `1/5`. These are exact rational source-branch weights of this stated finite-source model, not a native BRC engine execution or physical probability inference.

## Theorem 5 — permutation covariance of the tagged filter

For `σ∈S6`, transform allowed triples `σH`, token axis counts `(σn)_{σi}=n_i` and source labels together. Relabeling induces a bijection of all admissible labeled partitions. Therefore `D_{σH}(σn)=D_H(n)`; fractional certificates, the R observer and minimum repair count transport accordingly. P's orbit has thirty distinct labeled members. Actual native rotation/port transport still requires exact X6 generator mapping.

## Verification and research bridge

An executed standard-library checker `experiments/R709_PASCH_PORT_TRIADS_VERIFY_20261111.py` exhausts 4845 four-edge families and the complete S6 orbit, and checks all 16 and 25 ordered-source pairs using integer and Fraction operations. It returns `R709_PASCH_PORT_TRIADS_EXACT_PASS 4845 30 30 2/25`. Companion JSON records tested scope and outcomes. General statements rely on the explicit proofs above; finite enumeration checks the six-axis instance.

Established external terminology: Encyclopedia of Mathematics, *Pasch configuration*, https://encyclopediaofmath.org/wiki/Pasch_configuration (retrieved 2026-11-11). General constrained triple context: Hubai, Mezei, Béres, Benczúr and Miklós (2024), *Constructing and sampling partite, 3-uniform hypergraphs with given degree sequence*, PLOS ONE 19(5), https://doi.org/10.1371/journal.pone.0303155. Neither citation is a claim that the project's P000 native event bridge has been independently solved.

**Next differentiating question.** From the **frozen** X6 Link/Port, V29 PASS/TRANSFER and V39 loop-flow j inputs, compute which typed H(c,state,t) may actually occur, then test whether P's obstruction is native-reachable and whether enabling a complementary triad can be a source-preserving permitted event. Preserve Cell, sign, path, time and BRC provenance; verify TRIADIC_CLOSURE_E and rotation covariance against actual native generators.
