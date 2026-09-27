# Dyadic carry contraction for native signed correlations

Status: AUTHOR_SYMBOLIC_CANDIDATE / SHARED_CONTEXT / NOT_ADMITTED. This package contains a new symbolic lemma and its shared-context cross-review. It reports zero new scientific executions.

For each fixed dyadic displacement, two carry-indexed matrices contract the complete native signed correlation in polynomial work in the supplied word descriptions and prefix length. The construction preserves chronological, potentially noncommuting feedback and every residual coordinate. Reconstructing the queried Gram matrix still requires complete modular alias information or a proved aggregate; the documented bounded baby-step/giant-step alternative remains exponential in input bit length at the default Shor width.

Read DYADIC_CARRY_CORRELATION.md for the definitions, proof, counterexamples and accounting, then REVIEW.md for the source-specific checks. CONTINUE.md gives the next concrete implementation task. MANIFEST.json pins these files and the existing source/dependency chain.

The immediate goal is to implement the two-carry coefficient recurrence through the existing actual native Gram interface and compare all matrix entries on bounded same-word fixtures. No ideal propagator, supplied order/factors, precision upgrade or favorable asymptotic claim is part of this deliverable. The symbolic proof is readable on its own; exact native execution reuses the explicitly pinned historical dependencies.

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1
