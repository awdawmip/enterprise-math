# PCF7 parent revision and post-reopen reconciliation handoff — 2026-09-09

## Start here

This note is the durable entry point for the next researcher working on PCF7 closure state. It records the inspected repository frontier as of enterprise-math `main` commit `5f9fca51880b6b555a143f3cf4c3fc9da3ea8399` on 2026-09-09.

Do **not** restart either the fixed-probe mathematical correction or the reopen lease-preservation implementation. Both have durable completed evidence. The remaining bounded question is whether the fresh parent-scope Result has received an authorized Driver disposition and, if not, what exact control-state evidence is needed for closure.

## 1. Parent task and the original Driver revision request

Parent task:

- task id: `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION`
- publication id: `TP2-8F7443BCAF2BC5243574`
- taskbook: `research_tasks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_20260827.md`
- parent objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`

The prior reviewed Result was `RR-A9A5ADD3931B3F3EDFAB`. Driver review `DR-8183213860B7A72A2BD3` returned `REQUEST_REVISION`, nonterminal, and authorized one narrow correction only. Its followup packet is `research_driver_followups/DR-8183213860B7A72A2BD3/DFU-0204BC0AB65CDE176BBC.json`.

The defect was exact and local: the old fixed-probe prose incorrectly treated the zero probe like every nonzero probe.

## 2. Mathematical revision is complete

The current main branch contains the fresh parent-scope Result:

`research_result_records/RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION/RR-E9908FEE020773DEF39C.json`

Key bindings:

- Result: `RR-E9908FEE020773DEF39C`
- execution record: `ER-586DD6A098AF43C3EFB1`
- researcher: `EM-PCF7-283667`
- claim: `chatgpt-pcf7-20260906-1520-revision-v2`
- terminal verdict: `SUCCESS`
- unresolved residue: `NONE_WITHIN_AUTHORIZED_REVISION_SCOPE; DRIVER_REVIEW_AND_CONTROL_INTEGRATION_ONLY`
- `driver_review_required: true`

Primary mathematical closure artifact:

`research_artifacts/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION/PCF7_PARENT_REVISION_CLOSURE_RETURN_20260906_V2.md`

The exact corrected statement is:

- for every **nonzero** fixed probe `c` in the finite probe family, choose the semiprime factors outside the prime divisors of `c`, giving `gcd(N,c)=1`;
- for the zero probe, `gcd(N,0)=N`;
- therefore every fixed probe yields only a trivial output in `{1,N}` and never a proper factor.

This preserves the intended exact zero-success failure family. The fresh Result explicitly does not authorize changes to the parent polynomial-prefix complexity conclusions, `L=N`, `T1-T5`, sealed benchmark, factor-blind boundary, or any broader theorem.

Treat `RR-E9908FEE020773DEF39C` as the **primary durable mathematical frontier on main**. Do not prefer an unmerged or historical result merely because it has a similar closure statement.

## 3. Reopen ownership defect is also already repaired

Merged PR #1319, title `control: preserve live claims across Driver reopens`, has merge commit:

`fe9079dddc12f2201d9c74e40394a822b148c90d`

Its relevant durable implementation/test surface is:

- `tools/research_dispatch.py`
- `tools/research_dispatch_core.py`
- `tests/test_research_dispatch_reopen_claim_overlay.py`

The repair preserves a reducer-accepted `LEASED` claim across a nonterminal `RETURN_TO_EXECUTION` overlay, while retaining the existing frozen-result/claim lifecycle gate. It also preserves claimless reopen behavior: when no valid owner is present, the task remains available for dispatch rather than inventing ownership.

PR #1319 states that it changes no task priority, lease duration, terminal review, selection order, or mathematical authority. Do not reopen this implementation unless the new audit produces a concrete regression against the current code.

## 4. Current unresolved boundary

At inspection base `5f9fca51880b6b555a143f3cf4c3fc9da3ea8399`, an exact repository lookup for:

`research_result_reviews/RR-E9908FEE020773DEF39C/`

returned no review record. This is evidence that the fresh Result had **not yet** received a bound Driver review in the current authoritative result-review store at that inspection point.

That absence does not authorize a researcher to act as Driver. It only establishes the bounded residue to audit:

1. confirm the latest authoritative review binding for `RR-E9908FEE020773DEF39C` at execution time;
2. if still absent, classify whether the only lawful next action is Driver review;
3. if a new concrete control inconsistency exists, isolate it without editing the completed mathematics or completed reopen repair;
4. stop if no independent research residue remains.

## 5. Published continuation task

Task id:

`RS-PRIME-COORD-FACTOR-PCF7-POST-REOPEN-CLOSURE-AUDIT`

Taskbook:

`research_tasks/PRIME_COORD_FACTOR_PCF7_POST_REOPEN_CLOSURE_AUDIT_20260909.md`

The task is deliberately P2/MEDIUM and `CONTINUATION`. It is a finite closure/authority audit, not a new factorization route.

The required terminal certificate must choose exactly one of:

- `DRIVER_REVIEW_ONLY`
- `BOUNDED_CONTROL_RECONCILIATION_REQUIRED`
- `NEW_RESEARCH_RESIDUE_PROVED`

The preferred outcome is `DRIVER_REVIEW_ONLY` if the current evidence shows no independent residue.

Publication id is bound by the immutable task publication record under:

`research_task_records/RS-PRIME-COORD-FACTOR-PCF7-POST-REOPEN-CLOSURE-AUDIT/`

## 6. Do-not-repeat list

Do not:

- re-prove the fixed-probe failure family;
- change `gcd(N,0)=N` into `1` or apply the nonzero-prime-avoidance argument to zero;
- redo PR #1319 without a current regression;
- alter the sealed PCF2 benchmark or broaden the parent PCF7 scope;
- relabel factor-aware, answer-dependent, result-sensitive, or oracle information as factor-blind;
- infer a Driver disposition, Working Truth, Foundation status, benchmark promotion, or new factorization theorem from this closure audit.

The job is to make the already-completed research easy to consume and to leave exactly one lawful next control action.