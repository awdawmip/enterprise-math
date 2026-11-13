# R5: one-pass lexicographic radius–minimum-center–mean-cost frontier

Date: 2026-11-13. Author-side mathematical proof and exact computation, awaiting independent review and formal Task/CLAIM binding. No P000 or worldview changes.

## Scientific scope and provenance

Scientific input is unchanged: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. The 15 labeled integer weights and integer k0 coefficients are reproduced in the companion verifier from the pinned R5 construction. The precise activation thresholds are `(1-36*q/n)/23`, for eligible distinct `n` of q=3,12,15, computed with rational arithmetic. Their histogram has 953 distinct thresholds with multiplicities 869×1, 56×2, 28×3; hence the complete ordered event boundaries `x[0]=0 < ... < x[953]=1065`.

Related author-side frontiers: #2220 (minimum mean cost for three fixed budgets), #2253 (radius-cover path criterion), #2279 (fixed-budget DP), #2290 (greedy cardinality primal-dual certificate). Here the new question is: **for every radius R, jointly minimize first the number of centers K and then the total nearest-center event corrections J, and count exactly how many center sets attain both minima, with no K-layer dynamic program.** This is the lexicographic minimum-center frontier; it does not purport to enumerate all `(K,J)` trade-offs for every larger K.

## Theorem (lexicographic shortest path in a radius-cover DAG)

Let `x[0]<...<x[N-1]` be strictly increasing integer event coordinates. Admissible centers are indices in this same array. Fix an integer radius `R>=0`. For a center `p`, let `L(p)=min{b:x[b]>=x[p]-R}` and `U(p)=max{b:x[b]<=x[p]+R}`. A chosen subset `S` is feasible if `min_{p in S}|x[b]-x[p]|<=R` for every boundary `b`. Define `K=|S|`, `J(S)=sum_b min_{p in S}|x[b]-x[p]|`.

Construct a DAG with vertices `0..N-1`, and an edge `p->q` for `p<q` exactly when `L(q)<=U(p)+1`. A source can start at `p` when `x[p]-x[0]<=R`; an endpoint can terminate at `p` when `x[N-1]-x[p]<=R`. Every feasible center subset corresponds to **exactly one** source-to-terminal path in increasing center order, and vice versa. Each edge `p->q` has additive cost

`w(p,q)=sum_{b=p+1}^q min(x[b]-x[p],x[q]-x[b])`.

The source entry costs `head(p)=sum_{b<p}(x[p]-x[b])`; terminal costs `tail(p)=sum_{b>p}(x[b]-x[p])`. For a path `p_0<...<p_{K-1}`, the sum `head(p_0)+sum_j w(p_j,p_{j+1})+tail(p_{K-1})` is precisely `J(S)`.

Define a reverse-DAG dynamic program. At p, a terminal candidate is pair `(1,tail(p))` when it covers the right end. For each feasible edge p->q whose suffix pair is `(K_q,J_q)`, its candidate is `(1+K_q,w(p,q)+J_q)`. Take the **lexicographically least** candidate pair `(K_p,J_p)`; sum the suffix counts over all tied candidates, and remember the earliest tied successor. At the source, take the least `(K_p,head(p)+J_p)` and sum matching counts.

**Conclusion.** One reverse pass returns exactly (a) the global minimum number of radius-R centers, (b) the smallest total correction cost among all such minimum-cardinality selections, (c) the number of center subsets attaining both optima, and (d) the lexicographically first such center subset. No DP center-count axis is necessary.

**Proof.** The closed integer intervals `[L(p),U(p)]` are ordered monotonically in p. Two consecutive selected centers leave no gap precisely when `L(q)<=U(p)+1`. Together with initial/final coverage, these conditions are equivalent to complete coverage. A nearest center for a boundary between consecutive selected centers must be one of those two centers: more distant selected centers lie on either side in the ordered coordinate line. Consequently the displayed cost decomposition holds, with disjoint allocation of boundaries to head, intervening arcs, and tail. Every admissible increasing path represents one distinct center subset. The DAG is acyclic; induction backwards from its terminal vertices shows that selecting the lexicographically best suffix pair and summing its tied counts gives the exact optimal pair and multiplicity at every vertex. The source minimization yields the claimed global result. For integer strictly increasing coordinates, an edge requires `q-p<=2R+1`; otherwise the centers cannot jointly bridge their gap. Thus at most `N(2R+1)` candidate edges exist. Prefix sums and one binary search evaluate each edge cost in `O(log N)`; memory is `O(N)`, time `O(N(2R+1)log N)` plus event construction. At R=0 the only feasible center set is all N boundaries.

The greedy covering algorithm independently certifies each minimal K by matching a covering center set to a set of first-uncovered witness boundaries that **no sampled center** can cover two at once. It is not necessary, and generally false, that successive witnesses have coordinate separation strictly exceeding 2R: center restrictions can make the common-cover test fail even at smaller coordinate separation. The verifier uses the exact `L/U` common-cover criterion.

## Frozen R5 exact findings

The companion `EXACT_FRONTIER.csv` records **every integer radius 0..36**, each exact K, best J, tie count, greedy comparator, edge count and strict improvement. Independent checkpoints:
- R=0: K=954, J=0, one optimal center set.
- R=1: K=351, J=603, greedy J=603.
- R=2: K=213, J=1070, optimal-set count=1,338,767,625,695,954,932,334,592,000; greedy J=1104.
- R=9: K=57, J=4384, greedy J=4486.
- R=36: K=15, J=16813, greedy J=17190.
- A useful fixed-budget plateau: R=25 and 26 both require 21 centers, but the lexicographically best mean correction cost falls from 12146 to 12050 with the extra radius.
- The greedy minimum-K construction is strictly inferior in mean correction cost for 35 of the 37 tested radii (R=0 and 1 tie). This is a statement about this pinned finite instance.

## Verification

The locally executed verifier reconstructs the 15-atom rational threshold corpus and verifies the original 56-byte center encoding SHA256 `bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326`, R=2 original cost 1070, the 953-wall histogram, and exact K at R=2/9/36. Its independent finite exhaustive check covers **6,558** pairs (short integer event sequences of length 1..7 with increments in {1,2,3}, radius 0..5), examining **361,414** candidate subsets; all lexicographic optima, exact multiplicities and lexicographically earliest solutions agree. 3,624 instances have tied optimal sets. It also compares each of 37 full-size results to the independent greedy cardinality/dual bound. All arithmetic affecting scientific conclusions is integer or Fraction, with no floating-point decisions.

The output CSV contains the full exact finite table; `VERIFY_R5_LEXICOGRAPHIC_FRONTIER.py` is the portable standard-library reproduction. Local execution status: PASS on 2026-11-13. The repository program should additionally be rerun from its own immutable GitHub bytes by an independent environment.

## Observer and admission scope

The event-center representation is an algorithmic index of **this frozen, already defined R5 threshold query**, preserving the ordered threshold multiplicities and exact source construction in the verifier. It is not an assertion that a BRC index alone captures all signed X6/joint-relation observers or future operations; no P000 foundation data or six-axis primitive is quotient-identified by this construction. Formal Task owner, CLAIM, Result admission, and independent review are separate from these author-side proofs.

## Next useful unit

Extend the lexicographic DP to **all cardinalities K above K_min(R)** only where the memory/latency trade-off warrants it, or integrate the actual 12/17/33/35/56-byte center codecs with end-to-end frozen prefix queries, using the same immutable science pin. On this boundary, prioritize cold-start RSS and full-query time over another byte-only compression result.
