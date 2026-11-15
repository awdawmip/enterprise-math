# R5 — separated-star source residual and universal double-closure rigidity

Date: 2026-11-15 (Asia/Shanghai). Scientific input pinned at enterprise-math source commit 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Scope: *auxiliary* mixed-weighted one-dimensional integer-event, indexed-center observer. This is not a native X6 mapping, P000 change, formal Result or independent review.
Prior exact fixed-core source: research_notes/portable_direct/r5_ambient_helper_language_20261115/AMBIENT_OLD_HELPER_GAP_THEOREM.md, source commit e33b92f2c706b39399db7a0dc0e1a3e0c1e12c7c.

## 1. Model and exact distance certificate

Fix the previously proved seven-event old cores, indexed as
O0=0125, O1=0135, O2=0235, O3=0245, O4=0246.
The single-a new core/first-bit pairs are (1235,1), (1245,1), (1246,1), (1345,0), (1346,0).
The ab state additionally has (1236,1).
A suffix is a binary vector of length d. Old resources are all (Oj,s,u) for j=0..4, s in {0,1}, u in X. Targets are all (C,t,v) from the displayed new family and v in Y, with nonempty target language Y.
Both X,Y are arbitrary subsets of {0,1}^d, except where additional hypotheses are stated. No assumption of DFA regularity is necessary.

For any target and resource define the replacement distance exactly by
rho((C,t,v),(Oj,s,u)) = |C \ Oj| + [t != s] + H(v,u),
where H is binary Hamming distance. The repair library number kappa_T(X,Y;2) is the minimum size of a set of *old* configurations reaching every target at distance at most 2. Set it to infinity if impossible.

Exact core distances, columns O0,O1,O2,O3,O4:
- 1235: 1,1,1,2,3
- 1245: 1,2,2,1,2
- 1246: 2,3,3,2,1
- 1345: 2,1,2,2,3
- 1346: 3,2,3,3,2
- 1236: 2,2,2,3,2

Every core distance is at least 1. Thus an old suffix u can contribute to any target suffix v only if H(u,v) <= 1. The actual old core and first bit must still be retained to determine which target is repaired.

## 2. Universal double-closure theorem (new)

For **every finite d >= 0**, every old language X and every *nonempty* new language Y:

- If Y is not a subset of X, both kappa_a and kappa_ab are infinite.
- If Y is a subset of X, **kappa_ab(X,Y;2) = 2|Y|**, independent of all other old helper suffixes in X.

Proof. For each v in Y, the (1346,0,v) target has distance at most 2 only to (O1,0,v) or (O4,0,v). In particular v must belong to X. The ab-only target (1236,1,v) has core distance at least 2 from every old core; its old first bit must be 1 and suffix exactly v. These requirements are pairwise disjoint for each v and across different v, forcing 2|Y| resources. Conversely, for each v store (O1,0,v) and (O0,1,v). Inspection of all six exact core rows shows these two old resources cover every ab target with that suffix, with distance at most 2. Equality follows. The same compulsory (1346,0,v) proves infeasibility for a when v is missing from X. QED.

This strengthens the earlier unit-vector Y result to arbitrary, possibly disconnected or DFA-generated languages.

## 3. Distance-separated target tensorization (new)

Suppose Y is a disjoint union of nonempty groups Y_1,...,Y_k with
min{ H(v,w) : v in Y_i, w in Y_j } >= 3 for each i != j.
For each group define its *actionable old suffix set*
X_i = {u in X : min_{v in Y_i} H(u,v) <= 1}.
Then for T in {a,ab}, provided Y is a subset of X,

kappa_T(X,Y;2) = sum_{i=1}^k kappa_T(X_i,Y_i;2).

Proof. An old resource capable of reaching any target must have its suffix within distance 1 of that target, by the strictly positive core-distance lower bound. If the same resource could cover targets from two different groups, its suffix u would be within distance 1 of v in Y_i and w in Y_j, implying H(v,w)<=2 by the triangle inequality, contradiction. Hence every useful resource belongs to exactly one group, and the full set-cover optimization is the disjoint union of independent group-wise set-cover problems. Upper bounds concatenate group-wise optimal libraries; lower bounds sum their independent minima. QED.

The theorem also preserves exact witness provenance: each chosen old resource remains labeled by its actual (core,first-bit,u), not merely by an aggregated count. The claim concerns one-step radius-two repair, not an unspecified multi-step dynamical horizon.

## 4. Separated translated stars: full arbitrary-X formula (new)

Let h_1,...,h_k be binary words in {0,1}^d with pairwise Hamming distance at least 5. For each i choose a nonempty set I_i of distinct coordinate directions with r_i=|I_i|>=3. Set
Y_i = { h_i XOR e_j : j in I_i },  Y = union_i Y_i,
and let X be *any* old language with Y subseteq X subseteq {0,1}^d.
Define the retained-source bit z_i = 1 if h_i belongs to X, 0 otherwise.

Then for all such choices:

**kappa_a(X,Y;2) = sum_i [ r_i + (2 if z_i=1 else r_i) ].**
**kappa_ab(X,Y;2) = 2 sum_i r_i.**

The distance-five assumption on centers implies H(Y_i,Y_j)>=3, since each target differs by one bit from its center. It also shows that each center h_i is distinct from every target in Y.

Proof of single-star term. XOR translation u -> u XOR h_i preserves all Hamming distances, so the source Y_i becomes r_i distinct unit vectors. We give the exact one-star argument for arbitrary old X.

Each target (1346,0,e_j) forces an old resource (O1,0,e_j) or (O4,0,e_j), using r_i distinct *baselines*. The construction with both (O1,0,e_j) and (O0,1,e_j) for each j gives 2r_i repairs.

If the center 0 is available, retain all r_i baselines (O1,0,e_j) and the two center helpers (O0,1,0),(O4,1,0). The five a-target rows show that these r_i+2 entries repair all targets (1235, 1245, 1246, 1345, 1346).
To prove the lower bound r_i+2, assume at most r_i+1 entries. The r_i forced baselines leave at most one additional helper. No baseline can repair a (1245,1,e_j) target. A single helper covering all r_i>=3 of these targets must have old bit 1, core O0 or O3 and suffix 0: any other suffix is at Hamming distance at most 1 from at most two of the unit vectors, and first-bit-zero resources can reach at most one (1245,1,e_j). That sole helper cannot repair (1345,0,e_j), so every baseline must be O1, not O4. Then neither an O1 baseline nor that O0/O3 center helper can repair (1246,1,e_j), contradiction.

If center 0 is absent, consider four critical targets per unit vector:
(1245,1,e_j), (1246,1,e_j), (1345,0,e_j), (1346,0,e_j).
Any one old configuration with nonzero suffix can cover at most two of these 4r_i critical targets. A unit suffix e_j can reach only targets at its own e_j (other unit vectors are distance 2), and the core table limits one old entry to two critical types. A weight-two suffix can be adjacent to at most two target unit vectors, and a fixed old (core,first-bit) at suffix-distance 1 can repair only one critical type. Other nonzero suffixes are too far to reach any critical target. Therefore at least 2r_i old entries are necessary; the explicit 2r_i construction attains this bound. This proves the one-star dichotomy for **every** X and all d>=r_i>=3, with no assumption about other old auxiliary suffixes. Translate back by XOR h_i and apply the separated-target tensorization. Universal ab rigidity supplies the ab formula. QED.

## 5. Exact residual lower bound for a family of future observers

For fixed star targets Y, the vector z=(z_1,...,z_k) is sufficient to predict the **cardinalities** of all one-step a/ab repair libraries for the subfamily target queries Y_J = union_{i in J}Y_i, J subseteq {1,...,k}. The same formula with the sum restricted to J applies. For the complete query family, the k source bits are also necessary in an information-theoretic sense: choose each of the 2^k old languages X_z = Y union {h_i : z_i=1}. A singleton-cluster query J={i} gives 2r_i if z_i=0 and r_i+2 if z_i=1, distinct as r_i>=3. The full vector of query responses distinguishes all 2^k languages. Thus any deterministic exact quotient answering this declared family of queries has at least 2^k distinct states, i.e. at least k binary bits.

For only the single fixed aggregate total, the sum may identify fewer than 2^k classes; the k-bit minimality claim is explicitly **about the entire subfamily query family**, not that one scalar.

## 6. Finite verification and concrete example

The companion Python program recomputes every core-distance row from integer center sets. It performs exact minimum set-cover search for all 32 old languages containing the unit-star target Y={001,010,100} in Q_3, giving 16 cases at kappa_a=5 and 16 at kappa_a=6, each with kappa_ab=6. It checks all 65 nonempty X,Y pairings with Y subseteq X in Q_2 against the universal ab construction and forced same-suffix certificates. It also builds a two-star, six-bit example with centers 000000 and 011111 and three chosen directions per star. Minimum cross-star target distance is 3; with X=Y plus optionally the two centers the exact (a,ab) answers are:
- neither center: (12,12);
- only one center: (11,12);
- both centers: (10,12).
For each case the program checks direct witness coverage of every a and ab target and the exact no-cross-group incidence condition. All arithmetic is integer set difference / bit-count Hamming, no numerical approximation.

Recorded execution: PASS_R5_SEPARATED_STAR_AND_AB_UNIVERSAL on 2026-11-15. Verification results and executable script are committed alongside this note. Universal claims are proved above, not inferred from finite samples.

## 7. Frontier and boundary

The general pair (X,Y) for a, with overlapping neighborhoods and no star/distance-separation hypothesis, remains an exact weighted set-cover/hypergraph problem. Next investigate interaction certificates for overlapping stars (center distance 3 or 4), and a provenance-preserving transfer for regular X,Y that can compute both optimum cardinality and all optimal-library witnesses. The current one-step language quotient cannot automatically be reused for further repairs with different targets or horizons.

All formal ownership, Source Activity, CLAIМ, Result, Review and independent scientific admission continue to require their separate native authority. The present artifact is an independent non-overwriting research note on the existing R5 Draft branch.
