# PREFIX-789 / R6 — Exact provenance-aware path transfer and modular certificates

Date: 2026-11-15 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / UNREVIEWED / NOT_ADMITTED.
Provenance: R6 independent external scalar-observer continuation after PREFIX-788; recorded historical researcher EM-DIRECT-E77192, Source Activity RA-66BBE259AEE1AD543D9454A3; not a shared native X6 CLAIM, Result, or review.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged).
Predecessor: research_notes/portable_direct/2026-11-15_r6_prefix788_temporal_source_graph_duality_and_discrete_gap.md.

## Question and exact observer

PREFIX-788 established NP-completeness of exact integer-path zero-margin detection, and a shortest-path Bellman oracle at a *fixed* common dual witness. Which exact state retains branch histories while answering the restricted integer-target cancellation query? Which modular certificates are mathematically sound in the presence of mutually exclusive paths?

Let G=(V,E) be a finite directed acyclic multigraph with source s and sink t and at least one s-to-t path. Each edge e has its own unique formal symbol a_e and an integer weight w(e), possibly negative. A complete path p=(e_1,...,e_k) has ordered provenance word a_p=a_(e_1)...a_(e_k) and integer total S(p)=sum_i w(e_i). Parallel edges count as distinct paths. Fix an integer target T. As a special case of PREFIX-788 define the **external scalar observer** V(q,p)=(1-q,S(p)-T), q>0, reflected as (V,-V), with uniform margin rho=inf_(q>0,p)||V(q,p)||_infinity.

## Theorem 789.1 — Ordered-source and N[Z] path-transfer identities

The noncommutative ordered-path series W_t=1 and W_v=sum_(e=(v,u)) a_e W_u enumerate all permitted complete paths from each v, preserving branch and order. Under the semiring homomorphism phi(a_e)=X^{w(e)} into the Laurent polynomial semiring N[X,X^{-1}], the sum-observer polynomial P_v=phi(W_v) satisfies

    P_t=1,  P_v=sum_(e=(v,u)) X^{w(e)} P_u.

For each integer j, [X^j]P_s is precisely the number of permitted complete paths with sum j, including multiplicity. Consequently

    rho=min_{j:[X^j]P_s>0}|j-T|,
    rho=0 iff [X^T]P_s>0.

**Proof.** Every v-to-t path has a unique first edge and a unique continuation from its head. Reverse induction on a topological ordering establishes the ordered-word recurrence, including parallel edges. Applying phi adds edge weights, and the nonnegative coefficients add counts without signed cancellation. For each p, q=1>0 minimizes ||(1-q,S(p)-T)||_infinity at |S(p)-T|. The displayed margin identities follow. QED.

The projection phi is sufficient for *this declared final scalar query*, not for untyped future operations depending on path order, signed sources, Cell/Link/Port identity or event time. E.g. paths (+1,-1) and (-1,+1) both have total zero while their first-edge readouts differ.

## Theorem 789.2 — Exact modular obstruction and safe width

Let pi_m(P_s), m>=1, reduce every exponent modulo m in the nonnegative group semiring N[Z/mZ]. Its coefficient at residue r counts exactly the paths with S(p)=r (mod m). Let R_m be the supported residues, and define

    d_m(T)=min_{r in R_m} min_{k in Z}|T-r-km|.

Then rho>=d_m(T). If the target coefficient [r=T mod m]pi_m(P_s) is zero, exact cancellation is impossible and rho>=1. If m divides n, then d_n(T)>=d_m(T).

If all allowed path sums lie in an integer interval [L,U] and m>U-L, the modular image is injective on the possible sum values. The exact sum histogram and rho for any T can be reconstructed using the interval and pi_m(P_s). This uniform width threshold is sharp: for m<=U-L, the two values L and L+m lie in the interval and are aliased modulo m; there is no guaranteed injective reduction for arbitrary supported histograms in the band.

**Proof.** Since coefficients are nonnegative, reduction modulo m computes exact residue path counts. For any actual path p, S(p) is a representative of its residue and |T-S(p)|>=d_m(T); minimizing over p gives the bound. When m|n the class nZ is a subset of mZ, and distances to those lattices obey the same order pointwise and after minimization. Distinct integers in [L,U] have difference of magnitude <m when m>U-L; hence distinct residues. The endpoint pair proves sharpness. QED.

## Theorem 789.3 — CRT requires one common path

For coprime m,n, the CRT image of R_(mn) is a subset of R_m × R_n, but it need not be all of the product. Equality holds iff every marginally reachable residue pair is jointly realized by one and the same complete path. Therefore two independently positive target-residue tests need not imply a positive target-residue test modulo mn.

**Proof.** A single complete path induces both congruences simultaneously; separately existential witnesses can be different paths. The claimed inclusion and equality criterion are respectively this projection and its surjectivity. QED.

**Explicit counterexample.** A DAG with exactly two complete paths has totals {0,5}, target T=2, so rho=2. Modulo 2, its residue 0 is witnessed by the total-0 path; modulo 3, its residue 2 is witnessed by the total-5 path. Both marginal tests pass, but no complete path has total 2 mod 6. In exact integers,

    d_2(2)=0, d_3(2)=0, d_6(2)=2.

Forming the Cartesian product of independent residues would manufacture a path that never existed. The joint modulo-6 transfer preserves the temporal/source coupling. PREFIX-788's prior no-instance weights (3,5), T=4, yields sums {0,3,5,8}, rho=1 and d_3(4)=1.

## Algorithm, complexity, and validation

Dynamic programming over integer sum -> nonnegative path count implements the transfer on a DAG. Put W=sum_(e in E)|w(e)|. All path sums lie within [-W,W]; dense tables use O(|E|(2W+1)) integer additions and O(|V|(2W+1)) entries. Modular transfer uses O(|E|m) additions and O(|V|m) entries. Each coefficient's possibly large bit length contributes to the bit complexity. Binary-encoded weights can make W exponentially large, so these are pseudopolynomial algorithms, consistent with the restricted family of PREFIX-788 having weak NP-completeness. The count polynomial and residue class observer are distinct from the ordered path-word carrier.

Companion exact checker: research_notes/portable_direct/PREFIX789_R6_PATH_MODULAR_BRC_CHECK.py.
Results: research_notes/portable_direct/PREFIX789_R6_PATH_MODULAR_BRC_RESULTS.json.

The standard-library Python checker independently enumerates and performs nonnegative-semiring DP on 2,048 deterministic-seed two-choice layered DAGs; compares 18,432 residue transfers over moduli (2,3,4,5,6,7,9,11,13); and performs 77,834 counted assertions including the two exact counterexamples. Sample weights are integers in [-9,9], with 1–7 layers and targets in [-30,30]. All checks passed. Regression validates the implementation on the stated finite family; the universal statements follow from the proofs above.

## Next scientific question

Acquire actual typed BRC/X6 Cell/Link/Port/signed-source/event-time transitions and the guards controlling reachable histories. Determine whether integer edge weights and pathwise independent transitions hold for an admitted original observer. If source memory or force closure couples successive updates beyond the transition graph, expand the state to retain that dependency or use a joint path carrier. Any removal of path data requires a scoped future-observer factorization certificate. This work has not changed the original native comparator exclusion tally or the canonical proof/admission state.
