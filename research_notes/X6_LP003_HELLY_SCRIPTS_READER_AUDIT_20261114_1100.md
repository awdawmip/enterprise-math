# X6 LP003 — bounded pinned-source audit of Helly JSON field readers in scripts/

Date: 2026-11-14. Mother task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication: `TP2-B4A441B23DA3159232C2`.
Researcher `EM-X6-FB6990`; own Research SID `MCP-082892eb480e45dea6d4b9fcc0491034`.
Status: **AUTHOR-VERIFIED BOUNDED SOURCE CONSUMER AUDIT / UNREVIEWED / NOT_ADMITTED**. No Result, reviewer decision, or frozen input is modified.

## Exact immutable inspection domain

- Repository: `awdawmip/enterprise-math`.
- Pinned source HEAD: `638f05b83e3126b216f15a5e44eb5270781d6ba0`.
- Exact directory tree: `scripts/` Git tree `ec94d0e0765866e38a3f5475b640fc13471d3c0a`, **64 files, all `.py`**. Root Git tree readback had `truncated=false`; `scripts/` tree readback had `truncated=false`.
- Inspection operation: for all 64 names in that immutable tree, fetch the **full file body** through authorized GitHub connector with `ref=638f05b83e3126b216f15a5e44eb5270781d6ba0`, verify returned Git blob SHA equals the corresponding immutable tree entry; all **64/64** match, 0 fetch failures, 0 hash mismatches. The four deterministic partitions were 0–15, 16–31, 32–47, 48–63, with 16 successful reads each. This is an actual source-body audit; it is **not** an execution of the 64 programs.
- Searched exact literal tokens in every file body: `sample_native_address`, `sample_fixed_positive_chart_address`, `native_cell_address_status`, `check_enterprise_demos`, `tool_discovery_helly_radon_certificate_calculus`.

## Consumer result at that pin

The old unsafe output key `sample_native_address` appears in **0/64 `scripts/*.py` file bodies**. Exactly **1/64** files contains any of the above exact tokens: `scripts/tool_discovery_helly_radon_certificate_calculus.py`, blob `6118b3bd04010e05355586d353c9cf0ec38b1070`; its occurrences are the new typed field `sample_fixed_positive_chart_address`, explicit `native_cell_address_status`, and its own `check_enterprise_demos` producer definition. **No other source file in this directory is a direct literal-key reader of either field.**

The producer currently emits the fixed `S12`-chart value `[5,3,0]` with type `FIXED_POSITIVE_S12_LOCAL_CHART`, and does **not** infer a six-axis native Cell address without a Cell anchor and ordered signed-axis embedding. That exact code correction was previously saved at commit `c7b479b029c2b476fe33f7c2f47c4f148126d25d`; this audit does not re-execute it or add a new Helly theorem.

Additional previously read **specific** in-tree regression surfaces:
- `research_checks/X6_LP003_HELLY_FIXED_POSITIVE_CHART_TYPED_OUTPUT_REGRESSION_20261114.py`, blob `3ed2051763303e614b30ec17050d03d450da7dd6`, deliberately asserts absence of the old field and checks the typed value;
- `tests/test_tool_discovery_20260823_integration.py`, blob `1c4fe896cd470692ddd9ae3cd8d0d98a358d793f`, checks six *other* tool discovery modules, not this Helly JSON key.

The pinned tree permits a precise disposition: **`scripts/`: NO_DIRECT_LITERAL_KEY_READER_CONFLICT (64/64 actual file bodies)**. This closes the named *scripts-subtree direct literal reader* question, not whole-repository compatibility. A dynamic dictionary accessor, a CLI output parser outside `scripts/`, a workflow, another repository, or a consumer under `tests/`, `research_checks/`, `src/`, `tools/` is not settled by the inspected domain. The repository code-search index returned no hits for either literal but is not used as negative evidence.

## Mother task and typed scientific boundary

- Frozen scientific input remains `p000_reality_foundation.json` at `59538f585d037d09ef687b28715c4bc1a3f9fe03`, blob `c93d8150f1d223424b3506a6d2cdd5280b50825f`; six signed native axes and selected three-axis chart are not interchangeable.
- Historical fixed-positive Helly interval certificate and its original 66,675-family regression were already validated. This bounded reader audit consumes those results without rerunning them.
- Existing Source semantic PROGRESS `onhour-20261114-1013-x6-own-semantic-progress-zero-upload-v1` is already `SUCCEEDED/SOURCE_CHECKPOINT_PUBLISHED`, with four preceding units. **This audit is a fifth, new author-side bounded consumer-evidence unit, not an amendment to that historical Source receipt.**
- Pending exact work: inspect actual external/current JSON consumers beyond `scripts/` only where source evidence identifies them; establish LP011 frozen signed-native dominant-axis historical wrong caller and LP019 positive N-BRC signed-cancellation historical wrong caller; complete the 28-LP dependency ledger and independent Driver `REQUEST_REVISION`. Do not promote an unexamined module to KEEP/BUG.

## Preserved continuation and no-repeat scope

Own last winning claim from the known prior receipt: `MCP-30a8f5fd123215e08bd4a7cf`, native RUN `RUN-3356cbe3c2b4916d79399941`, generation initially 1, original SID as above. The receipt only establishes historical authorization; Source must check the current lease/generation before any new semantic PROGRESS write. Do not re-register, replay the failed 0710/0905 requests, repeat the earlier Helly theorem, or substitute this audit for native benchmark evidence.


## 2026-11-14 11:00 — research_checks subtree addendum (separate exact audit unit)

A second **completed source-body audit**, using the same immutable commit `638f05b83e3126b216f15a5e44eb5270781d6ba0`, inspected the current `research_checks/` tree `a11b4571c988f39133a33ad72b0e172ecd552f11`: 200 top-level entries (199 file blobs and one nested tree). Every one of the 199 direct file bodies was fetched from the exact commit and its Git blob SHA matched that immutable tree entry. The nested tree `RS-P000-THREE-AXIS-COMMON-MODE-FORGETFUL-SEMANTICS/` (tree `00003e1fb602866657c867f7e1c7e6b9f040e915`) contains exactly one Python file `check_common_mode_forgetful_semantics.py` (blob `f9723c04e5544d891c444501af5f2d08a1311e3c`), also read with matching blob SHA. **Total 200/200 actual `research_checks/` source files**, 0 blob mismatches and 0 unexamined descendants.

The same five literal tokens were checked throughout. Exactly one file contains any term: `research_checks/X6_LP003_HELLY_FIXED_POSITIVE_CHART_TYPED_OUTPUT_REGRESSION_20261114.py`, blob `3ed2051763303e614b30ec17050d03d450da7dd6`. Its reference to the legacy `sample_native_address` occurs solely as a **negative schema assertion** (`assert "sample_native_address" not in chart`), while its `sample_fixed_positive_chart_address` and `native_cell_address_status` checks verify the corrected producer. It is a valid typed regression consumer, not an incompatible legacy-value reader. No other current `research_checks/` file contains these exact names or direct Helly producer imports.

The merged bounded result is: **264/264 direct source files under `scripts/` (64) and recursively under `research_checks/` (200) inspected at one pinned commit**, all matched immutable Git blobs; the producer and a correctly typed regression are the only two lexical Helly-interface sites. **Zero confirmed unsafe direct literal-key readers in those two subtrees.** This closes these two named subtrees' direct-key compatibility checks, while external readers, dynamic key construction and untouched `tests/`, `src/`, `tools/`, workflows and other repositories remain separate unknowns. Code-search index incompleteness is not evidence of absence.

No new Helly theorem is claimed; no original benchmark is repeated and no source artifact is overwritten. This is a reproducible, exact, bounded scientific consumer-attribution result with independent Driver review still pending.
