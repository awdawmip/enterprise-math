# Stage449-B — Two-sided one-POP future quotient and exact positive support

Parent: Stage448-B, current draft PR #1736, 2026-11-05. Frozen scientific inputs: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.

## Target
Keep native X6 ordered sources, A endpoints and isolated B, current full observer (endpoints, directed J, K); allow P and Q at most one POP each and at most rP/rQ APPENDs in all legal interleavings with 12 possible labelled append directions.

Propose a finite exact repair invariant for the union of shifted-overlap windows. Prove both necessity (minimal distinguishing trace) and sufficiency (all labelled future prefixes). Check whether separate short suffixes and equality bits suffice, or whether joint-position directions are required.

## Small verification and complexity
Enumerate m=5,n=7 with one or two nonadjacent B defects, pP=pQ=1 and rP=rQ=1, all signed APPEND choices and operation interleavings. Compare full observer trace partitions versus proposed key; return concrete counterexamples on mismatch. Seek polynomial BigInt class-support and population DP with original-history rank/unrank, tracking input conversion and output cost. Do not treat finite tests as universal proof.

## Artifacts
Return a complete theorem or scoped counterexample, executable checker and actual output, exact Source/PR readback, Researcher activity provenance, and status of native owner/claim/Driver admission.