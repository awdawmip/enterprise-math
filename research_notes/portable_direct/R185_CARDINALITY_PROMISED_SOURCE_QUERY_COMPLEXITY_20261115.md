# R185 — Exact adaptive last-source query complexity under cardinality and support promises

Date: 2026-11-15. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

Scientific input is the frozen upstream pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Direct predecessor: R184 at immutable GitHub source `9a917a54ee02c0b71401a58fac7e7a5fbe466360`; R182–R183 at `5557fb3748bbe9e831e2f35716607dacffc0c6d4`. This is independent portable research, not a new Task publication or formal CLAIM.

## Scope and exact model

Fix a set `T` of `k>=1` distinct named source IDs. Each original history is a chronological concatenation of **whole** native-X6 atoms `(branch ID, source ID, ordered signed X6 path)`; branch identity, signed path, provenance, rational BRC weight and multiplicity remain in the underlying full carrier when the permitted operations need them.

For this **specific source-only observer**, the history maps to an ordered list `s` of distinct elements of T, ordered by increasing last-occurrence time. The empty list is permitted. A complete-history concatenation is represented by
`s ⋆ t = (s with all members of t deleted) followed by t`.
For each nonempty subset `U ⊆ T`, the source oracle `q_U(s)` returns the rightmost element in `s∩U` or `NONE`. One query returns one named source or NONE, not an encoded batch of arbitrary independent queries. An adaptive algorithm may choose its next U based on previous oracle answers. Queries have unit cost, and algorithms must recover the complete ordered last-occurrence list on **every** history in the specified promise class.

This is the precise source-observation quotient of R182/R184. It is observer-safe for these q_U and whole-atom concatenations, not a projection authorizing deletion of raw X6 paths or branch/provenance joint relations for other future operations.

## Theorem A: exact cardinality-promise minimax query complexity

Suppose the number r of distinct observed members of T is **known**, but *which* members occur and their relative last-occurrence order are unknown. The promise class consists of all r-permutations from T, of cardinality `P(k,r)=k!/(k-r)!`.

The deterministic adaptive minimax number of subset-source queries is exactly

```text
Q(k,r) = 0       if r = 0;
         r       if 1 <= r < k;
         k - 1   if r = k.
```

The lower bounds hold even if the algorithm may select *any* nonempty subset U, not just singleton/pair subsets, and adapt to every prior answer.

**Constructive upper bound.** When `0<r<k`, start with all of T, ask its latest source, remove that returned source from the next query, and repeat until exactly r sources have been recovered; reverse the answers. The known cardinality makes a final NONE query unnecessary. When `r=k`, stop after k-1 such queries: the sole remaining source is the oldest. When `r=0`, the list is empty by the promise.

**Uniform adversary and lower bound.** Consider any deterministic adaptive query algorithm, at any nonterminal history of t queries. Respond while maintaining a list A of *returned sources*, in their order of first introduction (earliest introduced = most recent in the eventual history). When a new query U meets A, answer with the **earliest introduced** member of U∩A. When it does not meet A, choose a new member of U, answer it, and append it to the **oldest** end of A. Every answer is non-NONE, and at most one new member enters A at each query.

After t queries, select a final history by putting any desired number of still-unreturned distinct sources *before* A (older than every returned source), and writing A newest-to-oldest in reverse chronological order. Every earlier query produces its recorded answer: an earlier returned source is more recent than all later introduced or still-unreturned members, and queries previously without returned members were answered by the first later-introduced member. This constructs valid full, completed histories consistent with the *entire adaptive transcript*.

If `1<=r<k` and `t<r`, then `|A|<=t<r`. There are `k-|A| > r-|A| >=1` unreturned candidates; at least two distinct choices of the `r-|A|` old members yield **different support sets** of size r, with identical answers to all t queries. Therefore t queries cannot always recover the history.

If `r=k` and `t<k-1`, there are at least two unreturned members. Keep full support T but swap two old unreturned sources. The two distinct full permutations again have identical answers. Therefore at least k-1 queries are necessary. Together with the constructive algorithms, both bounds are exact. QED.

## Theorem B: exact complexity if the support set itself is known

Suppose the exact occurring subset S⊆T is given to the algorithm; let `r=|S|`. The query minimax is

`Q_known_support(S)=max(0,r-1)`.

For the upper bound, query S, remove each returned source, and infer the sole oldest member. For the lower bound, run the same adversary with queries intersected with S; if fewer than r-1 sources have been returned, at least two still-unreturned S-elements can be transposed without affecting any answer. When r=0 or 1, the full order is given by the promise. QED.

**Resource distinction.** Knowledge of cardinality but not membership needs one additional query compared with explicit support knowledge whenever `1<=r<k`. When r=k, the cardinality already fixes membership and the two values coincide.

## Theorem C: minimum fixed selector catalog with known support

If the exact support S is known, r=|S|, and a fixed catalog of source-subset query *types* must distinguish **all r! permutations** (and stay discriminating under common whole-history contexts), then among queries with `U⊆S` the unique inclusion-minimal catalog is all `C(r,2)` pair selectors `q_{\{i,j\}}`, i≠j; no singleton selectors are needed.

All pairwise answers determine every relative order, hence the full permutation. For necessity of the pair i,j, let R list every other member of S, and compare `ijR` against `jiR`. Every nonempty V⊆S other than {i,j} returns the same answer on both histories: a V meeting R is masked by the identical later suffix R; singleton V cannot see order. The pair {i,j} alone separates them. Moreover, each q_V is a homomorphism to the right-zero-with-identity answer monoid `q_V(xy)=q_V(x)⊙q_V(y)`, so the equality of the other selectors survives arbitrary common left/right whole-history contexts. QED.

If queries may include IDs outside the known support S, selectors are classified by their intersection with S; the canonical indispensable *intersection types* remain precisely the pairs. This theorem concerns the fixed query-interface catalog, not a global lower bound on unrestricted affine representation dimension.

## Verified finite evidence and limits

Run `python R185_source_oracle_promise_check.py` using the Python standard library. Its JSON result is `R185_verification.json`:

- Every r-permutation for k=1..7 is recovered by both upper-bound algorithms: 16,071 input states for each.
- Exact decision-tree minimax over **all** 2^k-1 possible subset queries confirms every (k,r) for k=1..4, including empty/full support promises.
- 63,112 complete adversarial transcript-prefix checks for k<=5 construct two distinct promise-consistent histories with identical answers at every depth below the asserted bound.
- All 35 pair-catalog indispensability witnesses for known support k=2..6 are checked against **every** competing nonempty subset selector (and pair-catalog fingerprints separate all full permutations).

All checks are finite exact-integer computations; the all-k theorem is supported by the constructive and adversarial proofs above. No native `enterprise_math.brc_transport` module execution is claimed. Independent mathematical review remains `NOT_REVIEWED`.

## Consequence for the R182–R184 observer stack

The state space size for arbitrary partial source order remains `N_k=sum_{r=0}^k k!/(k-r)!`, which fixes minimum state storage but is independent of the allowed **interactive query budget**. R184's k-query unrestricted recovery is sharp without a cardinality promise. The present promise-sensitive theorem improves it to r if membership is unknown and to r-1 if the support is known; even though the full original X6/BRC carrier may contain far richer data, the declared selector need only work through this exact quotient.

**Next scientific questions:** optimal worst-case subset-query count when query subsets have a bounded maximum cardinality (especially pairs); exact tradeoffs between this adaptive oracle, the R183 affine reset representation and fully labeled native BRC ports; implement direct package-native integration with preserved source selectors, branch provenance, positive weights and multiplicity.

**Control provenance:** historical own research identity `EM-DIRECT-BF4AD7`, Session `MCP-46f202db13e64ad6b4c8860e06908245`, Activity `RA-7A118452894D2600AE7DE5A2`. No formal Task CLAIM or Result/Review acceptance is asserted. Current continuation lookup, when queued, remains pending until its own receipt is read; the scientific file is saved independently through the permitted portable path.
