# R71 — wrap-aware subtree exclusion and matched full-cost comparison

Continuation of independent author-side R70. Frozen scientific pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

**Exact first problem.** A subtree may contain sources whose integer phases wrap inside [L,U], yet all remain outside a given original-labelled arc. Find a subtree-aggregate certificate proving this without enumerating every event, or a sharp counterexample showing a proposed four-extrema certificate is insufficient.

Start with `a=1,b=2,t=4,I=[249/1000,251/1000]` (the R70 wrap witness), then add same-time branches `(4,b0),(4,b1)` and a newer `(6,b2)`. Check independent branch deletion under immutable-version semantics. Repeat across moving observation (j,x) and changing original labels with full typed signatures.

**Cost target.** Benchmark original R66 and R68 persistent-tree implementations against R70 on exactly the same auxiliary source sets, queries and output scopes, charging tree build/update, input conversion, big-integer operands, parameter width, cache memory/eviction and output materialization. Distinguish wall-time measurement from formal bit-complexity proof. Investigate query compilation as an implementation optimization, not an assumed speedup.

**Return.** Exact theorem/counterexample, runnable program, independence-aware oracle, finite verification scope, evidence links and smallest unresolved question. Keep P000/X6 and frozen scientific input unchanged. Native transfer requires a typed BRC interface and appropriate future-operations preservation. No formal task publication is created by this note.
