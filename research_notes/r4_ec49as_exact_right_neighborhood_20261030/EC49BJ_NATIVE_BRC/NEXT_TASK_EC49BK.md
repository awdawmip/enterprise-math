# EC49BK — Composition-safe observer state for X6 path BRC

Origin: EC49BJ proof and exact BRC verification in this directory. It establishes that endpoint/N-BRC count loses path reversal-prefix information even for native signed six-coordinate shortest paths.

## Concrete target
For genuine path-formal signed-X6 BRC words, specify a finite operation language with (i) ordered path concatenation at matching native Cells, (ii) signed axis-permutation from established S6 rotation skeleton, (iii) inverse-word reversal and (iv) permitted positive-rational edge-weight composition. State future observer(s) precisely (e.g., first k primitive actions after any word of declared operations, or full path realization).

Classify the coarsest exact state quotient sufficient to predict all such future observations on a declared horizon. Does retaining a bounded terminal k-suffix plus the endpoint suffice when reversal and concatenation repeat without a horizon bound? If not, give an exact parametric family with a growing-memory lower bound, including both reverse and concatenate witnesses. Then check invariance of the quotient under serial BRC multiplication and alternative sum; preserve multiplicity and provenance until a context-safe factorization theorem applies.

## Proof and evidence
Use full X6 signed primitive labels; keep Cell anchors chart relative and separate physical time. Reuse exact native `signed_brc.py` and its path-formal enrichment. For non-shortest walks allow opposite-sign inverse pairs and carry the actual path length; do not use shortest-word counts after loops are introduced. Produce a proof or explicit minimal counterexample with exact source pin and an executed bounded checker as support. Do not conflate positive mass, signed/complex phase or an auxiliary three-label R.

Deliver portable proof, source evidence and executable checker to existing research PR; native CLAIM, formal Result and independent Driver acceptance remain separate permissions.
