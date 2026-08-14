# R029 — Research Reasoning Kernel: Logic / Philosophy Tools

Researcher-ID: `EM-R029-LP2A71`  
Task: `RS-R029-RESEARCH-REASONING-KERNEL-LOGIC-PHILOSOPHY-TOOLS`  
Taskbook source commit: `c59c2ad1e56fcae3bf858b874a5a636c242e62c5`  
Execution base: `main@db9958cc006cacc32d5b30cd1a9a35594543a8d1`  
Status: `RESEARCH / NOT_CANONICAL`

## 0. Driver return

Preferred:

`SMALL_TRUSTED_REASONING_KERNEL_FOUND / MOST_PHILOSOPHY_TOOLS_INTERPRETIVE_ONLY / HIGH_VALUE_DIAGNOSTICS_FROZEN / CONTEXT_COMPILER_READY / NOT_CANONICAL`

Full:

`RESEARCH_REASONING_KERNEL_FOUND / LOGIC_PHILOSOPHY_TOOLS_TYPED / HISTORICAL_RESTART_COST_CLASSIFIED / TOOL_COMPOSITION_BOUNDARIES_FROZEN / CONTEXT_COMPILER_READY / NOT_CANONICAL`

## 1. Executive result

R029 does **not** find a new mathematical foundation and does not recommend a universal reasoning checklist. It finds a reusable research-process layer with four evidence classes:

1. `PROOF_PRESERVING`: proof-object transformations that preserve derivability under explicit preconditions.
2. `EXACT_SEMANTIC_TRANSFORMATION`: certified semantic transformations/factorizations; exact only for the declared semantic contract.
3. `ADVERSARIAL_DIAGNOSTIC`: typed questions, splits, counterexample/regime generators and evidence checks. High value, but never theorem evidence by themselves.
4. `INTERPRETIVE_LENS`: ontology/explanation/reduction lenses that can generate questions or reorganize vocabulary; never theorem evidence by themselves.

The machine registry contains **61 tools**: 1 proof-preserving, 3 exact-semantic, 53 adversarial diagnostics/generators, and 4 interpretive lenses. Dispositions are 43 KEEP, 11 NARROW, 3 MERGE, 4 INTERPRETIVE_ONLY. The asymmetry is deliberate: most historically useful “reasoning” is not proof transport; it is early detection of a type/scope/composition/evidence mistake.

## 2. Typed Research Tool contract

Every expanded registry record has the taskbook-required fields:

`id, name, layer, status, input_types, output_types, preconditions, transformation_or_question, preserves, may_destroy_or_not_preserve, trigger_signals, required_evidence, kill_tests, known_counterexamples, prior_art_root, project_specific_residue, composition_notes, executable_oracle, lean_declaration, source_refs, examples, anti_examples`, plus disposition/trust and quality metrics.

`reasoning_tools.json` is normalized: compact rows are expanded by `experiments/r029_reasoning_tool_registry.py` through defaults and layer profiles **before** validation/use. This keeps the registry machine-readable without repeating identical contracts dozens of times.

Trust class is an evidence boundary, not a prestige label. Even a `PROOF_PRESERVING` or `EXACT_SEMANTIC_TRANSFORMATION` tool contributes theorem evidence only when its required proof/certificate is actually supplied; the registry label cannot self-certify a result.

## 3. Reverse mining R015–R028

The lineage matrix replays 15 nodes and separates completed research from taskbook-only specifications. Six restart-cost clusters dominate:

- **Carrier/object typing — very high.** R015 support/count boundary; R017/R018 bracket and fibre distinctions; R020 exact witness relation vs cardinality shadow; R021 carrier taxonomy; R022/R023 Boolean-support scope; R028 credit carrier. Reusable tools: `STATE_OBSERVATION_SPLIT`, `STATE_CARRIER_REPRESENTATION_RESOURCE_SPLIT`, `BOOLEAN_COUNT_PROVENANCE_CARRIER_SPLIT`.
- **One-step vs composition — very high.** R017/R018 one-step quotient lift, R020 middle incidence, R021/R022/R023 composition safety, R024 cache reuse. Reusable tools: `ONE_STEP_EXACT_NOT_COMPOSITION_SAFE`, `MIDDLE_INCIDENCE_CORRELATION_CHECK`, `GENERATORWISE_CLOSURE_CHECK`.
- **Future-language/horizon relativity — very high.** Adequacy/deletion changes when the permitted continuation language changes. Tools: `FUTURE_LANGUAGE_RELATIVITY`, `CURRENT_VS_FUTURE_SAFE_EQUALITY`, `HORIZON_RELATIVITY_CHECK`.
- **Evidence vs validation coverage — medium but severe.** R023I showed a successful Lean build did not validate the new module until root coverage actually reached it. Tool: `ROOT_COVERAGE_EVIDENCE_CHECK`.
- **Semantics vs representation/resource — high.** R021→R022→R024→R028 repeatedly separated semantic exactness from storage, metadata, cache, rewind and acquisition cost. Tools: `SEMANTICS_VS_RUNTIME_REPRESENTATION`, `METADATA_IS_INFORMATION_CHECK`, narrowed `RESOURCE_EQUAL_SEMANTIC_FIBRE_CHECK`.
- **Prior-art root vs project residue — high.** Generic abstraction/search machinery can be rooted without erasing project-specific typed contracts. Tools: `PRIOR_ART_REDUCTION`, `PROJECT_SPECIFIC_RESIDUE_EXTRACTION`, `EQUIVALENCE_TO_KNOWN_ALGORITHM_CHECK`.

R019 and R026 are explicitly marked taskbook-only in the lineage; they are not promoted to completed evidence. R017’s accepted core is reconstructed from the official R018 dependency because a direct owner return was not located in the searched PR surface.

## 4. Seed-tool disposition

All required seed tools are classified in `R029_SEED_TOOL_CLASSIFICATION.json`.

KEEP: `QUANTIFIER_SCOPE_CHECK`, `NECESSARY_SUFFICIENT_SPLIT`, `STATE_OBSERVATION_SPLIT`, `STATIC_CORRECT_NOT_DYNAMIC_STATE`, `ONE_STEP_EXACT_NOT_COMPOSITION_SAFE`, `DECLARED_VS_REALIZED_FUTURE`, `FACTOR_THROUGH_COMPLETE_ENCODING`, `ROOT_COVERAGE_EVIDENCE_CHECK`, `PRIOR_ART_REDUCTION`.

NARROW: `RESOURCE_EQUAL_SEMANTIC_FIBRE_CHECK`, `COUNTEREXAMPLE_MINIMIZATION`, `REGIME_EXHAUSTION`.

MERGE: `CARRIER_TYPE_SPLIT` → `STATE_CARRIER_REPRESENTATION_RESOURCE_SPLIT`; `SUPPORT_COUNT_PROVENANCE_SPLIT` → `BOOLEAN_COUNT_PROVENANCE_CARRIER_SPLIT`; `CAUSAL_PREDICTIVE_RETROSPECTIVE_SPLIT` → `CAUSAL_PREDICTIVE_RETROSPECTIVE_RELEVANCE_SPLIT`.

The seed set needs no standalone KILL entry; the taskbook’s universal claims are killed separately. Four philosophy tools in the full registry are `INTERPRETIVE_ONLY`.

## 5. Small trusted kernel

Only four tools are allowed onto the theorem-carrying lane.

### `CONTRAPOSITIVE_CHECK` — `PROOF_PRESERVING / NARROW`

Input is a source proof/certified theorem `A ⇒ B`; output is `¬B ⇒ ¬A`. It preserves derivability in the declared logic. It does **not** establish the converse or an equivalence, and scope diagnostics cannot manufacture its proof input.

### `FACTOR_THROUGH_COMPLETE_ENCODING` — `EXACT_SEMANTIC_TRANSFORMATION / KEEP`

For encoding `E:X→Q` and future target/signature `F`, exactness is certified only when `F` is constant on `E`-fibres, equivalently when a factor `g` exists with `F=g∘E`. It preserves that declared target, not richer unmentioned carriers/futures. R017’s square-bracket +1 obstruction is a standing kill test against universal carrier claims.

### `FUTURE_LANGUAGE_EXTENSION_REFINEMENT` — `EXACT_SEMANTIC_TRANSFORMATION / NARROW`

When future language `L` is extended to `L'⊇L`, the induced future-indistinguishability relation can only refine. This preserves the declared observation semantics. It does not say extra context always helps, nor that every new operation is relevant.

### `RECOALESCENCE_SUFFIX_SAFETY_CHECK` — `EXACT_SEMANTIC_TRANSFORMATION / NARROW`

Under the frozen Boolean/result-support BRC semantics, forgetful recoalescence is safe exactly when the relevant suffix-support signatures agree. It does not extend to multiplicity/provenance/weights/amplitudes without a new carrier proof.

## 6. Why diagnostics dominate

The historically expensive failures are usually category errors before they are failed derivations: wrong carrier, wrong quantifier/horizon, one-step theorem reused compositionally, runtime identity confused with semantic equality, build PASS confused with target coverage, hindsight credit confused with ex-ante dispensability, or generic prior art confused with novelty. A diagnostic can eliminate these branches cheaply, but because it only asks/partitions/searches it must remain non-evidentiary.

## 7. Philosophy compiled, not elevated

Ontology, explanation and reduction are useful only after compilation into typed questions. For example, “what is the state object?” becomes `STATE_OBSERVATION_SPLIT`; “is this primitive or representation?” can lead to carrier/resource typing; “does this reduce to known machinery?” becomes `PRIOR_ART_REDUCTION` + `PROJECT_SPECIFIC_RESIDUE_EXTRACTION`. Pure `ONTOLOGICAL_COMMITMENT_LENS`, `EXPLANATION_VS_PREDICTION_LENS` and `THEORY_REDUCTION_LENS` remain interpretive. Calling a BRC token “primitive” creates no factorization, reachability or arithmetic proof.

## 8. Causality and R028

R028 forces a three-way separation: causal relevance, predictive relevance and retrospective/hindsight credit. Realized-path zero credit does not imply declared-language dispensability; a permitted alternative suffix may still require the distinction. Shapley-like allocations are comparison devices unless a causal model is independently supplied. Therefore `REALIZED_PATH_VS_DECLARED_LANGUAGE_CREDIT` is a diagnostic and is a **known-invalid** direct input to exact factorization when the theorem concerns the full declared future language.

## 9. Tool composition calculus

`R029_TOOL_COMPOSITION_MATRIX.json` contains **15** explicit rules: 3 `ALWAYS_SAFE`, 5 `SAFE_WITH_PRECONDITIONS`, 3 `DIAGNOSTIC_ONLY`, 4 `KNOWN_INVALID`.

Recommended gated pipeline:

`STATE_OBSERVATION_SPLIT → FUTURE_LANGUAGE_RELATIVITY → FACTOR_THROUGH_COMPLETE_ENCODING → NO_RESURRECTION_CHECK`

This pipeline is not a theorem by concatenation. The factorization step must discharge its own certificate and the same encoding/future contract must be preserved.

Representative invalid compositions:

- one-step exactness → suffix-safe recoalescence without a suffix certificate;
- realized-path hindsight credit → declared-language factorization;
- ontology lens → exact factorization/theorem evidence;
- quantifier-scope diagnostic → contrapositive proof transport without a source proof.

## 10. Trigger compiler

Keyword matching is weak evidence. The selector in `r029_reasoning_tool_registry.py` ranks by structural task tags, typed input matches and semantic aliases before raw keywords, and returns two channels:

- exact/proof-preserving candidates, still certificate-gated;
- sparse advisory diagnostics/generators, default top-k ≤ 6.

Mutation fixtures include both directions: “all tests passed” must **not** by itself trigger universal-theorem quantifier checking; “closed under arbitrary continuations” must trigger future-language reasoning even without the token `future`. Root-coverage, one-step composition, R028 hindsight-credit and prior-art cases are also executable mutations.

## 11. Universal claims attacked

All ten taskbook pressure claims are killed in `R029_UNIVERSAL_REASONING_KILL_FIXTURES.json`, each with counterexample, killing tools and a narrower survival condition:

1. `LOGIC_TOOL_IS_ALWAYS_PROOF_PRESERVING` — KILLED: diagnostics/generators do not transport proofs.
2. `PHILOSOPHY_LENS_CAN_BE_USED_AS_THEOREM` — KILLED: interpretive vocabulary is not a certificate.
3. `MORE_CONTEXT_ALWAYS_HELPS` — KILLED: under bounded context/tool budget, irrelevant injection consumes capacity; task-relative typed coverage is the relevant condition.
4. `EVERY_HISTORICAL_DISTINCTION_SHOULD_BE_INJECTED_EVERYWHERE` — KILLED: many tasks lack the input types for BRC/carrier/future/causal tools.
5. `ONE_UNIVERSAL_REASONING_CHECKLIST_SUITS_ALL_TASKS` — KILLED: e.g. root-coverage checking is critical for Lean integration but type-mismatched for a standalone arithmetic identity.
6. `TRIGGER_KEYWORD_MATCH_IS_SEMANTICALLY_COMPLETE` — KILLED by explicit false-positive and false-negative mutations.
7. `A_TOOL_THAT_HELPED_ONCE_IS_REUSABLE` — KILLED by bracket-carrier +1 instability; reuse requires new-task preconditions.
8. `TOOL_COMPOSITION_IS_AUTOMATICALLY_SAFE` — KILLED by the spurious middle-representative stitching counterexample.
9. `PRIOR_ART_ROOTING_DESTROYS_PROJECT_SPECIFIC_VALUE` — KILLED: generic roots and typed project residue coexist.
10. `THE_RESEARCH_REASONING_KERNEL_SHOULD_BECOME_A_NEW_MATHEMATICAL_FOUNDATION_PRIMITIVE` — KILLED: it reduces to established reasoning families plus project workflow contracts.

No universal numeric law such as “more context monotonically hurts” is asserted. The result is conditional: usefulness is task- and budget-relative.

## 12. Prior-art rooting

`R029_TOOL_PRIOR_ART_MATRIX.md` systematically roots the required areas: classical/FOL, modal/temporal, type/refinement, abstract interpretation, model checking, proof/program logic, epistemic logic, causal/counterfactual reasoning, philosophy of science/reduction, proof planning, automated theorem-proving heuristics, scientific discovery/hypothesis generation, and CEGAR.

The project-specific residue is the evidence-aware compilation contract and its Enterprise Math counterexample library—not ownership of the underlying logic/philosophy.

## 13. Quality metrics

The registry carries bounded ordinal quality metrics rather than pretending they are intrinsic real-valued truth: historical reuse/restart evidence, false-positive/false-negative trigger pressure, counterexample sharpness, composition risk, evidence strength and expected context cost. They are for router comparison, not theorem statements. Historical replay indicates the highest restart-reduction potential in carrier typing, one-step/composition, future-language relativity, root coverage, semantics/resource separation and prior-art reduction.

## 14. R030-consumable interface

R030 should consume the registry as a **context compiler**, not inject it wholesale:

1. infer task structural tags / input types / evidence goal;
2. select exact/proof candidates by type compatibility and require certificates;
3. select a small advisory set of diagnostics/generators;
4. preserve trust labels in downstream prompts/logs;
5. consult the composition matrix before chaining tools;
6. run negative-trigger fixtures so keyword expansion does not silently regress;
7. never promote the registry itself to Foundation/common semantic surface without a separate theorem-level promotion task.

## 15. META_TOOL_DELTA

`R029_META_TOOL_DELTA_SCHEMA.json` defines optional, evidence-gated fields for `new_tool`, `strengthened_tool`, `narrowed_tool`, `killed_tool`, `new_trigger`, `new_counterexample`, and `composition_rule`. Empty arrays are valid. A diagnostic/lens cannot self-promote its own registry status.

## 16. Focused executable evidence

Executed on the frozen owner-local artifacts:

- Python compile: PASS.
- `PYTHONPATH=experiments python3 -m unittest -q tests/test_r029_reasoning_tools.py`: **15/15 PASS**.
- `PYTHONPATH=experiments python3 experiments/r029_reasoning_tool_oracle.py`: PASS.
- Registry schema: PASS; 61 expanded tools.
- Composition consistency: PASS; 15 rules, all four composition classes represented.
- Universal-kill fixture validation: PASS; 10/10 claims present and killed.
- Trigger mutations: **6/6 PASS**.

Repository CI is not required for this research-only task and was not polled: `CI_NOT_REQUIRED_FOR_RESEARCH`.

## 17. Scope / non-claims

- No new foundational primitive is proposed.
- No philosophy lens is theorem evidence.
- No claim that context quantity is globally monotone in research quality.
- No claim that the 61-tool catalogue should be injected into every task.
- No change to canonical BRC/common surface.
- R019/R026 taskbooks are not relabeled as completed research.
- R017 lineage is explicitly provenance-qualified.

## 18. Driver recommendation

Freeze R029 as an **owner-local reasoning-tool registry + selector + mutation suite** and feed it to R030. The useful kernel is intentionally small on theorem-carrying transformations and large on adversarial diagnostics. The next optimization target is not adding more philosophy vocabulary; it is measuring whether sparse typed selection lowers restart cost and false-branch rate without increasing context debt.
