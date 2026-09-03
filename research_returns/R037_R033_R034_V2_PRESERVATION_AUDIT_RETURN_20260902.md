# R037 — Immutable-V2 Preservation / Redispatch Audit — Return

- Task: `RS-R037-R033-R034-INDEPENDENT-ALGORITHM-DATA-REPLICATION-AUDIT`
- Publication: `TP2-FEE5990D460CCB106345`
- Researcher-ID: `EM-R037-DA5B4D`
- Claim: `chatgpt-r037-v2pres-20260902-1034-a71c2e`
- Claim comment: `Issue #240 / 5503474685`
- Execution branch: `research/r037-v2-preservation-audit-em-r037-da5b4d`
- Execution base: `ac709e6d472c39b1b623905d85eb753d965a6567`
- Scope: `V2_PRESERVATION_AND_DISPATCH_SEMANTICS_AUDIT_ONLY`
- Mathematical replay: `FORBIDDEN / NOT PERFORMED`

## 1. Direct verdict

**Preservation verdict:** `PRESERVATION_PASS_WITH_RUNTIME_DISPATCH_GAP`.

The immutable-V2 migration preserves the R037 task identity, theorem-owner boundary, frozen R033/R034 owner-head pins, historical return boundary, provenance caveat, and the distinction between mathematical evidence and Driver authority. The current publication does **not** grant Working Truth or canonical promotion.

However, the migration does **not** preserve the historical task's runtime lifecycle state strongly enough to prevent duplicate researcher execution. The migrated generation is simultaneously:

- `claimable=true`;
- `base_state=HANDOFF_READY`;
- `P0/HIGH`; and
- explicit that its next action is **Driver review of PR #812**, while the preservation body says completed work must not be replayed.

At the exact execution base `ac709e6d472c39b1b623905d85eb753d965a6567`, no task-scoped V2 execution-record directory and no task-scoped V2 result-record directory exist for this task. Therefore the historical frozen return cannot produce the ordinary result overlay that would place the task in `AWAITING_DRIVER_REVIEW`.

The canonical selector consequently redispatched the task. This audit's server-authenticated CLAIM comment `5503474685` is a concrete reproduction of that control-plane gap.

## 2. Frozen inputs checked

Current immutable-V2 generation:

- task record: `research_task_records/RS-R037-R033-R034-INDEPENDENT-ALGORITHM-DATA-REPLICATION-AUDIT/TP2-FEE5990D460CCB106345.json`;
- taskbook: `research_tasks/LEGACY_CONTROL_MIGRATION_RS_R037_R033_R034_INDEPENDENT_ALGORITHM_DATA_REPLICATION_AUDIT_20260902.md`;
- taskbook blob: `sha1:16f7343d8087e0eb43b4af697de9785139539cc8`.

Exact migration provenance:

- legacy source commit: `ce629e24e5af59128e25af87075c6622413684e0`;
- original taskbook: `research_tasks/R037_R033_R034_INDEPENDENT_ALGORITHM_DATA_REPLICATION_AUDIT_20260812.md`;
- original taskbook blob: `sha1:23c4f0c3dc034ee0f1d48d72d47009376685a56d`;
- frozen R033 owner head: `c2aa1758c6cf8f194d8b4493b90c903a2dfcd048`;
- frozen R034 owner head: `674fb8717d753cd36fd83b061c869d79e8875b31`.

Historical handoff:

- PR: `#812`;
- historical return head: `87d617a90d81b6197d521699512e1894db4346d8`;
- return: `research_returns/R037_R033_R034_INDEPENDENT_ALGORITHM_DATA_REPLICATION_AUDIT_RETURN_20260828.md`;
- return blob: `sha1:66c837d42227d7de02dfd2de82219a17b875a66f`.

The historical return says `DONE / RETURNED_WITH_PROVENANCE_CAVEAT / AWAITING_DRIVER_REVIEW`. It reports no theorem-critical mathematical mismatch in its audited scope, retains all-radius boundary `S^2` and pointwise nonperiodic heat-kernel/local-CLT strength as theorem candidates, and upgrades the Barlow return/root-local spectral statement only in its stated ideal bi-infinite uniform-NN scope. This audit does **not** independently re-adjudicate those mathematical claims; they are read only to verify migration fidelity and provenance boundaries.

## 3. Preservation checks

### 3.1 Mathematical identity and boundary — PASS

The migrated task keeps the same R037 identity, `program/p022-geometry-v2` owner, exact R033/R034 frozen owner pins, and Driver-review next action.

The provenance caveat is also retained: the prior R034 run had an accidental partial frozen-script patch exposure, so it must not be labeled provenance-clean blind replication. If that strict label is required, the migrated next action correctly calls for a fresh **R034-only** executor rather than rerunning the completed parent R037 task.

### 3.2 Truth-authority backflow — PASS

The current task publication explicitly has:

- `working_truth_granted=false`;
- `canonical_promotion_granted=false`.

Therefore migration does not silently turn the historical replication return or its Barlow scope into repository-level mathematical authority.

### 3.3 Runtime metadata normalizations — NON-MATHEMATICAL

Two fields are normalized rather than copied literally:

- legacy leverage `FOUNDATIONAL_VERIFICATION` -> V2 selector leverage `HIGH`;
- legacy claim lease `1440` minutes -> V2 claim lease `120` minutes.

These change scheduling/liveness metadata, not the mathematical task statement. They should be documented as control-plane normalization rather than described as exact field preservation.

## 4. Runtime redispatch gap — REPRODUCED

The gap is the composition of four individually valid pieces:

1. The migrated publication is active, claimable and `HANDOFF_READY`.
2. V2 runtime policy orders `HANDOFF_READY` before `READY`.
3. The runtime reducer maps an unleased `HANDOFF_READY` task to `NEEDS_DISPATCH`.
4. The current generation has no V2 result lifecycle record capable of overlaying the historical frozen return as `AWAITING_DRIVER_REVIEW`.

This conflicts with the result-contract invariant that a frozen return without Driver review should be `AWAITING_DRIVER_REVIEW` and should not be researcher-dispatchable on the ordinary result path.

The effect is observable, not hypothetical: after exact selector reduction and race refresh, this task accepted server-authenticated CLAIM `5503474685` under Researcher-ID `EM-R037-DA5B4D`.

## 5. Required control action

The safe resolution is **not** to replay R033/R034 research.

Driver/control-plane action should instead:

1. materialize or otherwise authoritatively represent the historical R037 frozen return in the V2 result lifecycle so its current state reduces to review-pending rather than dispatchable;
2. review historical PR #812 and its mathematical evidence/provenance caveat separately;
3. keep this migrated task non-dispatchable until that lifecycle authority is present;
4. if strict provenance-clean R034 replication is desired, publish a new R034-only task with a fresh clean executor;
5. retain the `FOUNDATIONAL_VERIFICATION -> HIGH` and `1440 -> 120` changes as explicit runtime-normalization notes.

Until step 1 is durable, this return recommends a scheduler `HARD_BLOCK` owned by the Research Driver, with unblock only after authoritative V2 review-pending lifecycle materialization or an explicit nonterminal Driver disposition returning R037 to execution.

## 6. Machine-auditable outputs

- `research_artifacts/R037_R033_R034_V2_PRESERVATION_AUDIT/AUDIT_MATRIX.json`
- `research_checks/R037_R033_R034_V2_PRESERVATION_AUDIT_CHECK_20260902.py`
- this return

The focused checker verifies the current V2 publication/taskbook invariants, selector ordering, reducer dispatch mapping, and the audit matrix's preservation-vs-runtime verdict. The task-scoped result/execution-directory absence is recorded as provenance evidence from the exact execution-base GitHub read rather than inferred by the checker.

## 7. Return classification

- Terminal verdict: `AUDIT_COMPLETE`
- Hard target disposition: `V2_MATHEMATICAL_PRESERVATION_PASS__LEGACY_REVIEW_PENDING_RESULT_RUNTIME_OVERLAY_MISSING__RESEARCHER_REDISPATCH_REPRODUCED`
- Method harvest: `RESULT_ONLY`
- Independence status: `NOT_APPLICABLE`
- Source exposure status: `NONBLIND_DISCLOSED`
- Unresolved residue: Driver must reconcile the historical frozen R037 return into the V2 result/review lifecycle and review PR #812. No R033/R034 mathematical replay is authorized by this audit.
- Next control-plane recommendation: block researcher redispatch; materialize/reconcile the review-pending result lifecycle; review PR #812; if required, publish a fresh R034-only clean-replication task.
