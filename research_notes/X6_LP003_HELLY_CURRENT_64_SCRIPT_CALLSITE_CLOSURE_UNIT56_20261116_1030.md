# X6 unit 56 — current `scripts/*.py` direct Helly/S12 consumer audit

Date: 2026-11-16. Parent: RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2. Author Research lane: `chatgpt-research-onhour-enterprise-math-20260923`, EM-X6-FB6990, SID MCP-082892eb480e45dea6d4b9fcc0491034. **BOUNDED AUTHOR SOURCE AUDIT; UNREVIEWED / NOT_ADMITTED.**

## Exact immutable scope and observed result

Pinned complete remote directory listing `scripts/` at `awdawmip/enterprise-math@0903c93b0b032993953ee5d7da68d81b6e27896d`: **64 Python files ending `.py`**. Every one of those 64 file bodies was fetched at that same immutable commit through the authorized GitHub connector; 64/64 succeeded, 0 read failures. Inspected each text body line by line with the following case-insensitive literal-alternative predicate:

```regex
helly|radon|tool_discovery_helly|sample_native_address|sample_fixed_positive_chart_address|native_cell_address_status|FIXED_POSITIVE_S12_LOCAL_CHART
```

The **only** matching file among the 64 was the actual producer `scripts/tool_discovery_helly_radon_certificate_calculus.py`, immutable Git blob `6118b3bd04010e05355586d353c9cf0ec38b1070`. Its inspected match lines are 59, 166, 167, 168, 182. No *other* current `scripts/*.py` body makes a literal reference to the named Helly/S12 symbols or sample address in this predicate. The source itself returns `coordinate_type=FIXED_POSITIVE_S12_LOCAL_CHART` and `native_cell_address_status=UNSPECIFIED_REQUIRES_CELL_ANCHOR_AND_ORDERED_SIGNED_AXIS_EMBEDDING`; it does not export `sample_native_address`.

Separately, the explicitly known consumer outside `scripts/`, `research_checks/X6_LP003_HELLY_FIXED_POSITIVE_CHART_TYPED_OUTPUT_REGRESSION_20261114.py`, imports this original producer by `spec_from_file_location` and checks the local-vs-native address boundary. Unit55 repaired that actual test's `assert` elision with always-evaluated predicates and added seven adversarial invalid fixtures. Other `research_checks/`, `tests/`, experiments, historical material and dynamic indirection are **outside this 64-file scope** and are not presumed closed.

## Interpretation and action

For the *current scripts-root* slice, the Helly producer is not shown to feed a second named in-tree script consumer. This is a direct literal source-reference nonmatch within a complete pinned finite directory, **not** a global proof of no downstream consumer: dynamic imports or renamed literal references could escape the predicate; other directories were not scanned here. No current `scripts/` source patch is justified by this bounded observation. Keep the producer unchanged and retain the typed `research_checks/` regression repaired in unit55.

The parent 28-LP consumer/dependency matrix remains open beyond the inspected 11 production modules, six direct tests, one Helly typed regression and current 64-script literal-reference slice. Historical specific LP011 signed singleton-dominant-axis wrong caller and LP019 positive `N_BRC` signed-subtraction caller remain `UNRESOLVED_PROVENANCE`; independent Driver `REQUEST_REVISION` remains open. Maintain distinct provenance and do not promote author evidence to formal review/admission.

## Replay recipe (no new scheduler)

Resolve `GET /repos/awdawmip/enterprise-math/contents/scripts?ref=0903c93b0b032993953ee5d7da68d81b6e27896d`, select `type=file` and `name.endswith('.py')`, and fetch all 64 `scripts/{name}` bodies at that exact commit. Search their lines with the above case-insensitive predicate. Expect exactly one matching path with five matching lines. This unit is a source inspection, not a runtime or benchmark execution. Original Helly and R063 native programs already executed previously (#54/#50) and were not rerun.

## Native continuation boundary

Original Source request `onhour-20261116-0911-x6-unit52-54-native-semantic-progress-v1` returned `SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED`, verified main Source `d05e82e1bf358fbaa927698997f8c42834f8d565`; no replay. Own resume `onhour-20261116-1004-x6-own-run3356-resume-after-unit54-v1` has been submitted once for original run `RUN-3356cbe3c2b4916d79399941`, initially `RUNNING / WAIT_ORIGINAL`; later original receipt must be consumed before new Native PROGRESS. GitHub source/Activity can be independently preserved without impersonation of the CONTROL_PLANE_MAINTENANCE lane.
