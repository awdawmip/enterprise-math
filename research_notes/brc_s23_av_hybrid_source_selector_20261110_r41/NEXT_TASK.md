# R42 — Certified multi-owner source selection: bit cost and large-partial-quotient stress

Status: author-side continuation question, not a shared Task-ID or authorized CLAIM.
Predecessor: R41, scientific freeze `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

**Exact unresolved problem.** Derive and test a selector that chooses among a bounded certified suffix scan, q-lane arithmetic, shared Floor Sum and endpoint-coboundary counting using predicted or measured bit-operation cost. In particular, can an Ostrowski/continued-fraction block compute *multiple* historical owner labels faster on large partial quotients without evaluating each source or each owner independently?

**First actionable unit.** On the same exact source windows as R41, instrument multiplication/division/modulo bit lengths, rational enclosure refinement, phase sorting, certified comparisons, q-lane candidate construction, Floor Sum Euclidean iterations and output encoding. Compare deterministic primitive-operation counts, then measure representative local wall time. Include both m=21 extremely near 1/3 (where suffix search loses) and m=257 with width heterogeneity (where suffix wins), in addition to frozen S23 m=128. Preserve all source labels and exact return values.

**Further differentiating experiment.** Create adversarial parameter families with one arbitrarily large continued-fraction partial quotient. Find a candidate batched Ostrowski method with explicit algebraic source-to-owner mapping; independently check exact last-source vectors against the R40 oracle. If a candidate fails, retain the smallest exact failing witness and revise the operator. Include a bounded rational-enclosure refinement method for queries crossing a floor boundary.

**Accepted evidence.** A new exact lemma/counterexample or implemented and verified algorithm with parameter/test scope, arithmetic/cost evidence, direct comparison to R41 reference and a clear input-conversion/precision/output cost model. Preserve frozen scientific inputs and Source governance; no implied new proof, review or shared-task ownership.
