# R5 continuation — unbounded intersection arity for two-block discrete responses

Date: 2026-11-19. AUTHOR_PROVED (all integer m>=3); FINITE_EXHAUSTIVE_CHECKED (m=3,...,12); NOT_REVIEWED. This is portable mathematical research, with no new formal Task CLAIM/RUN or native X6 assertion.

The preceding R5 theorem reconstructs all named maximal supports from pairwise compatibility edges because each possible scalar response set is a **single interval**. Here is a complete and minimal obstruction when the observation model is extended to allow two disjoint ordered blocks per state. The frozen scalar R5 science remains unchanged.

**Theorem.** For every integer m>=3, two m-state systems with the same ordered discrete observation alphabet Ω_m={1,...,m} can agree on the feasibility of every named state subset of cardinality <m, while having different maximal feasible support families. In one of the systems, every allowed response set is a union of at most two contiguous blocks.

**Construction and proof.** Let A_i=Ω_m\{i} = [1,i−1] ∪ [i+1,m] (allowing empty end blocks). In the comparison system, B_i=Ω_m for each named state i. For every set of named states J,

`intersection(A_i : i in J) = Ω_m \ J`.

Hence every proper subset J is jointly feasible in A, but the full m-subset is not. Every J is feasible in B. The maximal feasible supports of A are the m distinct (m−1)-state subsets; the sole maximal feasible support of B is the full m-state set. Every feasible intersection predicate of order ≤m−1 agrees across the two systems; the first distinguishing predicate has arity exactly m.

For m≥3, every pairwise intersection is nonempty in both, so both pairwise compatibility graphs are the same complete graph K_m, even though their true maximal support families differ. Choosing m>r for any fixed proposed intersection rank r shows **there is no uniform finite Helly number for arbitrary two-block response sets on ordered discrete alphabets**. The worst-case required joint-coordinate arity grows with the number of named states.

Minimal explicit witness: Ω_3={1,2,3}; A_1={2,3}, A_2={1,3}, A_3={1,2}. All three pairs intersect but the three-way intersection is empty; the pairwise graph would falsely declare {1,2,3} a feasible maximal support.

`VERIFY_NONCONVEX_HELLY.py` exhaustively checks all subsets for each m=3,...,12, their maximal supports, matching feasibility through rank m−1 and the at-most-two-block property. The written proof establishes the statement for all m≥3.

**Scope and next question.** This is an exact theorem about *arbitrary two-block discrete observation sets*, not a contradiction of R5's true single-interval scalar noise, and not a claim about any unverified native X6 carrier. The required information-preserving higher-order residual is the joint-intersection predicate; in general a ternary bit is not enough for all m. For concrete Enterprise Math multiblock ports, identify an applicable Helly rank or retain the relevant full intersection hypergraph and observer/provenance types before compression.
