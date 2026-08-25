# CBRC F5R — Source and Target Leak Audit

Status: `CHECKPOINT_B / RAW_FREEZE_AUDIT / CHECKER_RECORDED`
Researcher-ID: `EM-CBRC-F5R-8120F1`
Taskbook source: `3015cee704b6864c955bf577637383dd8c3dfd19`

## 1. Allowed mathematical source surface actually used

Only the following mathematical sources were read before this raw freeze:

1. `research_inputs/CBRC_F5_BLIND_FORGETFUL_BRANCH_SEMANTICS_PACKET_20260823.md@a107c133e11597623bbe79ef37397fc8ba5c13f7`;
2. `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md@6ec0d73a19e28ec586c59a97d24f5798c9119771`;
3. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@b631242db84c5bd3640e6dc554b19a1d04d464f3`.

The taskbook itself and repository/branch metadata were used only as execution-control material, not as mathematical premises.

## 2. Forbidden mathematical surfaces not read/used

Before raw freeze, this execution did not read or use:

- any reconstruction or remembered statement of the lost original F5 verdict;
- full F0–F4 reports beyond facts frozen into the F5 blind packet;
- R063, R064, R065 or FQ mathematics;
- downstream coherent-BRC/wave research;
- external quantum mechanics, quantum walks, Hilbert spaces, Born rules, path integrals, gauge theory or wave equations;
- a preselected rank-two, complex or quadratic carrier;
- a phase group, norm, inner product, square law, Hadamard/Fourier/splitter target.

## 3. Target-leak test

The candidate `FORGETFUL_BRANCH_NONDEGENERACY` was treated only as the proposition to classify, never as a premise.

The proof route was source-first:

1. identify the type boundary between concrete Path-formal witnesses and later marked coefficient slots;
2. isolate exactly what the allowed sources require of `pi`, `x`, `y` and marker retention;
3. construct both candidate-true and candidate-false exact semantic models under the common allowed conditions;
4. test each proposed load-bearing implication separately;
5. state any rank consequence only after the semantic classification and only through the F4 boundary already present in the blind packet.

No desired rank lift was used to choose the semantic model.

## 4. Countermodel-target independence

The countermodel carrier `Z × (Z/2)` is used only as the smallest exact bookkeeping witness of a nontrivial kernel for `pi`. Its second coordinate has no phase, metric, norm, inner-product, wave, quadratic, complex or geometric interpretation.

The candidate-false map

`M_B((n,t),(m,s))=((n,t),(m,s+n mod 2))`

was selected because it simultaneously makes the relevant logical tests exact:

- retraction remains exact;
- the map is reversible;
- total old coefficient is conserved;
- old Boolean support is conserved;
- the second enriched output is nonzero;
- the second old projection is zero.

Thus the countermodel tests logical independence and does not encode a downstream target structure.

## 5. Rank-target audit

No rank-two carrier was constructed, named, classified or selected. The only rank statement is the strictly conditional implication permitted by the blind packet:

`FORGETFUL_BRANCH_NONDEGENERACY + accepted F4 boundary => torsion_free_rank(C) >= 2`.

Because the antecedent is not derived, the execution labels the lower bound `CONDITIONAL_ON_NEW_AXIOM` and does not promote it to an unconditional theorem.

## 6. Pushed-checker execution record

Pushed checker:

`scripts/cbrc_f5r_validate_forgetful_branch_semantics.py`

Owner-branch commit containing checker:

`1f67d0b475efc8d6afd900f2632b280534c26e20`.

Remote checker Git blob SHA:

`b83995d4d1bf00db3d078fcb349ef5ed5223f8a4`.

The executed file had the identical Git blob SHA `b83995d4d1bf00db3d078fcb349ef5ed5223f8a4`, establishing byte identity with the pushed owner-branch checker.

Exact execution result:

- `CBRC_F5R_CHECK_RESULT=PASS`;
- `CBRC_F5R_MISMATCH_COUNT=0`;
- `CBRC_F5R_DETERMINISTIC_DIGEST=14201c39734a17782aa7dabb48a22c0e97fc72a002f6f78578cf3645869d9a97`;
- finite carrier elements checked: `10`;
- two-slot states checked: `100`;
- complete additivity sample states: `36`;
- semantic/model checks: `39`.

## 7. Raw-freeze verdict

`TARGET_LEAK_AUDIT_PASS`.

`F5R_SOURCE_FIREWALL_PASS`.

`F5R_RAW_MATHEMATICAL_FREEZE_INDEPENDENT = true`.

`F5R_PUSHED_CHECKER_PASS = true`.
