# Next exact research unit: minimum destructive probes and sharp stability

Mother objective: preserve BRC N=4/S23 joint causal source information under declared observer/future-operation families, and use the resulting certified observer interfaces in larger decoder optimization and residual-fidelity studies.

Frozen input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; retained six labeled four-outcome rows; unchanged A/B/C arrays and M mixer. Current completed result: global injectivity of a **single non-destructive multiplicative gate attenuation** `A_lambda` for every `0<lambda<1`, with exact inverse and valid full-cube bound `(1-lambda)*min(lambda,1-lambda)/21`. Verified finite execution is in `RUN_EVIDENCE.json`.

Next question: Define constant-replacement probes `U_I(z)` overwriting a subset `I` of gates among `{0,1,2,3,4}` by a known `beta in (0,1)` and retaining every non-overwritten original coordinate. When the baseline `P(z)` and a fixed family of such probes are available, what is the minimum family size needed for injectivity on all of `[0,1]^11`? Begin with candidate probes replacing `{0,1}` and `{0,1,2,3,4}`; prove their joint injectivity or provide an exact counterexample. If a smaller family works, provide the corresponding source-by-source inverse. Compare lower bounds by constructing indistinguishable pairs for undersized families.

Second useful unit: compute the sharp lower TV stability constant for `A_(1/2)` over the shared-parameter image, or certify a tighter constructive constant than `1/84`; retain all source labels while doing so.

Evidence required: exact definitions/quantifiers, analytic inverse or exact indistinguishable witnesses, any finite proof certificates/checkers with complete coverage, verification status, immutable source ref and next unresolved step. This is author-side research pending independent review and native owner/CLAIM, not an accepted theorem in the project state machine.
