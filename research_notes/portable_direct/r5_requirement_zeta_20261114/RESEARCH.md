# R5 — exact prerequisite masks, optimizer zeta law, and two-cut collapse at budgets 292–954

Date: 2026-11-14. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.
Scientific input frozen at `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Research layer: **derived one-dimensional, integer-coordinate, radius-2, event-index center observer** inside the existing Enterprise Math source lineage. Native X6/P000 states, path provenance, and the 2,520-byte certificate are not quotiented by this theorem.

## Exact observer and notation

Let `x_0<...<x_(n-1)` be integer events, each adjacent gap in {1,2,3}; let `I` be the set of original length-3 gap indices. For `B⊆I`, let `x^B` be obtained by reducing precisely the gaps of B from 3 to 2 while preserving original event indices. A K-element set `S⊆{0,...,n-1}` of indices is feasible if every event is within distance 2 of a selected event. Its cost is `C_B(S)=sum_t min_(j∈S)|x^B_t-x^B_j|`. Let `J_B(K)` be the minimum feasible cost and `Opt_B(K)` the **family of original-index subsets** attaining it.

Assume **no two original length-3 gaps are adjacent** (their starting indices differ by at least 2). The frozen R5 input has 954 events, 28 cuttable gaps, last coordinate 1065, and minimum separation of cut indices **5**, so it satisfies this condition.

## Theorem 1 — principal-filter / exact enabling-mask theorem

For every fixed center-index set S that is feasible with **all** gaps closed, there is one uniquely determined prerequisite mask `M(S)⊆I` such that for every B:

\[
\boxed{S\text{ feasible on }x^B\quad\Longleftrightarrow\quad M(S)\subseteq B.}
\]

Furthermore `C_B(S)=C_I(S)` for every enabling B, and the mask is explicitly recoverable:

\[
\boxed{M(S)=\{i\in I:S\text{ is infeasible with every cut except }i\text{ closed}\}.}
\]

**Proof.** A radius-2 center-event witness in the all-closed coordinates that crosses an original length-3 gap must join the **two immediate event endpoints** of that gap. Indeed that closed gap alone has length 2, and an additional positive adjacent step would make distance at least 3. Such a crossing witness exists precisely when that one gap is closed. A witness that crosses no original length-3 gap remains available at unchanged distance for all closure configurations.

For an event t, either a no-cut witness covers it unconditionally, or every available witness needs a cut incident to t. Nonadjacent length-3 gaps ensure t is incident to **at most one** such cut. Since S is feasible under all closures, the latter condition is exactly the requirement to close that single cut. Taking the union over all t produces M(S) and proves both necessity and sufficiency. Omitting i from the all-closed configuration fails precisely when i belongs to M(S), which proves the explicit mask formula.

For a feasible configuration, each noncenter event is served either at the unchanged within-block distance 1 or 2, or across a closed gap at distance exactly 2. An already feasible nearest distance cannot strictly decrease under a newly closed length-3 gap; the only new cross-gap candidate has distance 2. Hence all feasible C_B(S) are identical. QED.

**Sharp geometric boundary.** Adjacent cut gaps can produce a disjunction rather than a unique mask: original events (0,3,6), S={0,2}, both cuttable. The middle event is covered after closing **either** gap, but not when neither is closed. Thus the separation hypothesis is material.

## Theorem 2 — exact optimizer-fiber zeta law

At a budget K where `J_B(K)=J_I(K)` for **every** closure mask B, Theorem 1 gives

\[
\boxed{\operatorname{Opt}_B(K)=
 \{S\in\operatorname{Opt}_I(K):M(S)\subseteq B\}.}
\]

Define nonnegative integers `a_M(K)=#{S∈Opt_I(K):M(S)=M}`. Then

\[
\boxed{N_B(K):=|\operatorname{Opt}_B(K)|=\sum_{M\subseteq B}a_M(K).}
\]

This is an exact Boolean-zeta relation. The Möbius inversion
`a_M(K)=sum_(B⊆M)(-1)^(|M|-|B|)N_B(K)`
recovers the entire *requirement-mask multiplicity distribution* when the count data are known. The mask retains a provenance-like enabling relation; cardinality alone does not identify individual optimizer sets.

For a target cut i, let `rho_B(S;K)=min_(T∈Opt_B(K))|S\T|` (number of replaced centers) and
`R_i(K)=max_(B⊆I\{i}) max_(S∈Opt_(B∪{i})(K)) rho_B(S;K)`.
Then the max–min quantifier order admits the exact reduction

\[
\boxed{R_i(K)=\max_{\substack{S\in\operatorname{Opt}_I(K)\\i\in M(S)}}
 \rho_{M(S)\setminus\{i\}}(S;K),}
\]

with maximum of an empty collection defined as 0. For fixed S requiring i, `M(S)\{i}` is the smallest background making S optimal after adding i, while enlarging that background only enlarges the old optimal family and can only decrease the nearest-old-family distance. This proves the formula without swapping max and min.

## Theorem 3 — the frozen R5 K≥292 optimizer family has only two effective cut bits

Use 0-based cut labels from the frozen original 28-gap sequence. The earlier exact constant-cost theorem provides `J_B(K)=J_I(K)` for every B and `K≥214`. This run independently reconstructed the frozen 954-event coordinates, then used an exact chosen-center shortest-path/count DP at five masks: empty, {15}, {17}, {15,17}, and all 28.

For **every integer K from 292 through 315**, the DP finds identical optimal cost at all five masks and

\[
N_{\{15,17\}}(K)=N_I(K).
\]

By monotone optimizer-family inclusion, `Opt_{ {15,17} }(K)⊆Opt_I(K)`; equality of finite cardinalities proves **equality of the full optimizer families**. Theorem 1 therefore forces every fully closed optimal S to have `M(S)⊆{15,17}`. Consequently for every closure mask B and each **293≤K≤314**,

\[
\boxed{\operatorname{Opt}_B(K)
=\{S\in\operatorname{Opt}_I(K):M(S)\subseteq B\cap\{15,17\}\}.}
\]

The prior endpoint-family invariance theorem also gives `Opt_B(K)=Opt_empty(K)` at K=292 and all 315≤K≤954. Combining it with the newly proved interval yields the **full K=292..954 two-bit sufficiency**.

The exact four-cohort cardinality formula at K=293..314 is

\[
\boxed{N_B=a_\varnothing+
 [15\in B]a_{15}+[17\in B]a_{17}
 +[15,17\in B]a_{\{15,17\}}.}
\]

All 24 rows for K=292..315 are saved in `EXACT_R5_REQUIREMENT_ZETA.json`. Notable exact values:

| K | a_empty | a_15 | a_17 | a_{15,17} |
|---|---:|---:|---:|---:|
| 293 | 12606779601463240519046922240 | 495879658013739785241231360 | 495879658013739785241231360 | 0 |
| 294 | 296770704568869882883347578880 | 22161992076688082359686266880 | 22238281254844042326646456320 | 991759316027479570482462720 |
| 314 | 34372089438980233382036766720000 | 89534937486897009949409280000 | 89534937486897009949409280000 | 0 |

For every K=294..313, `a_{15,17}>0`: these are **jointly enabled optimizers that require both cuts**. At K=293 and K=314 the joint cohort is empty, while both singleton cohorts are nonempty. K=292 and K≥315 have only the empty-prerequisite cohort. This identifies an exact two-cut interaction that a cost-only observer misses.

**Exact counting certificate.** For sorted selected indices j1<...<jK, each path's prefix, intermediate nearest-center costs and suffix partition the event indices. The finite DP state (k,last selected j) stores minimum integer cost and number of tied paths; predecessor transitions have coordinate span at most 7 for steps 1..3. Ties sum counts, so no duplicate subset is counted. Each of the five R5 masks was computed through K=315. The source script is `VERIFY_R5_REQUIREMENT_ZETA.py`; its output agrees with the 24-row JSON. The K293 empty/single-cut counts and the K292,314,315 endpoints also agree with earlier separately preserved R5 evidence.

## Validation and scientific status

Actual standard-library Python execution returned `PASS_EXACT_R5_REQUIREMENT_ZETA`. It checked all 1,929 step words of lengths n=2..8 with nonadjacent cuttable gaps, 460,152 feasible-set/cost instances, 9,885 constant-cost budget instances and 13,868 exact max–min recourse comparisons against the reduction formula. All five frozen R5 count spectra were recomputed for K=292..315 using exact integers; the all-mask count equaled the {15,17} count in each of the 24 budgets. The 2^28 closure-family statement follows from the proved enabling-mask/optimizer-family theorems plus the exact endpoint certificates, **not** from 268 million individual enumerations.

This is an author-side proof and integer computation. Mathematical review: **NOT_REVIEWED**. No formal Task/CLAIM/Result/Review operation is asserted by this independent file publication.

## Next scientific unit

For cut 15 and cut 17 at K=293..314, use `M(S)∈{∅,{15},{17},{15,17}}` to compute exact
`max_S min_T |S\T|` over the *two* relevant minimal enabling backgrounds rather than all 2^27 masks. A practical exact next algorithm can exploit center-path DP with a prerequisite-mask-labelled automaton, preserving the max–min order. Separately investigate K=214..291, where additional cut bits may remain effective. The native 2,520-byte certificate and 8,192-prefix-query benchmark remains an independent frozen objective.

## Provenance

- Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
- Earlier R5 exact count / optimizer-family endpoint theorem: [Draft PR #2379](https://github.com/awdawmip/enterprise-math/pull/2379), immutable commit `68ac5b5507fbef23378658df5beb6ca1c7ab48ba`.
- All-background strict new optimizers for cuts 15 and 17: [Draft PR #2398](https://github.com/awdawmip/enterprise-math/pull/2398), immutable commit `e469fa1eaa167b566c1e08012ca571041758d4fc`.
- Exact recourse DP: [Draft PR #2402](https://github.com/awdawmip/enterprise-math/pull/2402), immutable commit `dcc59506f4282d8ae521dc5dc428402ec2999010`.
- Unbounded general-family recourse contrast: [Draft PR #2407](https://github.com/awdawmip/enterprise-math/pull/2407), immutable commit `b57d7a820863fd727d842cd8f618b1559c789f04`.
