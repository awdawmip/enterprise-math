# R059D Stage U Driver Freeze

Researcher-ID: `EM-R059D-9C6B2A`
Stage-U frozen owner head: `a9929a5bd666e621cb1bd77adb464df0d35db399`
Taskbook source: `320e0525f0aa4d5ccc9faec2a408187b2e6f9222`
Driver disposition: `VALID_UNIFIED_STABILIZER_FILTERED_SELECTOR_CALCULUS`

Accepted freezes:

- `STABILIZER_FILTERED_EQUIVARIANT_SELECTOR_THEOREM_ESTABLISHED`
- `BRC_SELECTABLE_SET_EQUALS_EXACT_FEASIBLE_INTERSECT_STABILIZER_FIXED_SET`
- `FILTERED_SINGLETON_NOT_FEASIBILITY_SINGLETON_IS_THE_EXACT_UNIQUENESS_CRITERION`
- `SYMMETRY_BREAKING_CONTEXT_IS_NECESSARY_IN_MANY_NO_GO_CASES_BUT_NOT_SUFFICIENT_IN_GENERAL`
- `PREEXISTING_AXIS_CONTEXT_RETAINS_COMPLEMENT_AXIS_AMBIGUITY`
- `STRAIGHTNESS_FORCES_AXIS_BUT_NOT_ORIENTATION`
- `STABILIZER_FILTERING_UNIFIES_SYMMETRY_NO_GO_BUT_DOES_NOT_REPLACE_ORDER_POST_CREDIT_AXIOMS`

Canonical finite-group selector formula:

`E(x)=A(x) ∩ Fix_Y(Stab_G(x))`.

Interpretation:

- `A(x)` is the exact feasible output set after all independently declared algebraic/post-credit constraints;
- `Fix_Y(Stab_G(x))` is the symmetry-compatible output set under the exact state+context stabilizer;
- `E=∅` means deterministic equivariant feasible selection is impossible on the orbit;
- `|E|=1` means exact unique forced output for the frozen relation;
- `|E|>1` means noncanonical / insufficient context or constraints.

Boundaries:

- stabilizer reduction alone is not a selector;
- post-credit is not a scalar reward; it changes `A` by exact constraint pullback;
- straightness makes the full-D12 axis feasible set singleton but leaves the orientation fiber unresolved;
- scalar `5 -> 4` remains conditional on Stage-R order/reflection/single-valuedness axioms and is not derived by the stabilizer filter alone;
- no universal physical BRC law, physical probability, or physical direction preference is established.

Checker: `324/324 PASS`, digest `1538acd6933798066b5717932b4027f41e77fc017144b45eed2249aba2d4781a`.

Stage U artifacts are immutable after this freeze.
