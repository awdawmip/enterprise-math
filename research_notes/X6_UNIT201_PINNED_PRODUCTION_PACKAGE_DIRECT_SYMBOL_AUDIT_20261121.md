# X6 Unit201 — Frozen production-package direct-symbol provenance audit

Date: 2026-11-21. Parent task: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Historical original Research lane: `chatgpt-research-onhour-enterprise-math-20260923`; original Researcher `EM-X6-FB6990`. **AUTHOR SOURCE-AUDITED / EXACT IMMUTABLE BODY OBSERVATIONS / UNREVIEWED / NOT_ADMITTED / NO NATIVE PROGRESS CLAIM.**

## Frozen source and question

Scientific baseline remains `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03` (P000 V5, six signed native spatial axes). Historical comparison is exactly `awdawmip/enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3`. The pre-existing X6 Unit198–200 exact BRC formulas and test-only caller findings are consumed, not recomputed.

The unresolved question is whether the historical production Python package directly calls or imports the six-axis prototype endpoint calculators, or contains the two alleged LP011/LP019 wrong-caller markers. Unit199 had inspected a small named P022 subset, not the entire production package.

## Actually executed immutable source-body census

Using the connected GitHub repository service, the frozen commit's recursive Git tree was read with `truncated=false`: 5,014 entries total, including 929 `*.py` files. The declared production-package population was **all 225 Python paths under `src/enterprise_math/` at that exact immutable commit**, not the entire repository.

Every one of those 225 files was then fetched individually by exact `repository/path/ref` via `mcp__GitHub__fetch_file`. 38 were checked as named modules, followed by the other 187 in 16 disjoint batches (15 batches of 12 and one batch of 7). **225 of 225 body reads succeeded; zero failed or truncated body reads in this scoped census.** The content of every fetched body was split into lines and examined under the same case-insensitive word-boundary expression:

```regex
\b(endpoint_weight|endpoint_multiplicity|positive_path_multiplicity|relative_endpoint_multiplicity|LP011|LP019|argmax|signed_brc|Spatial6|Coord6)\b
```

Result: **0 matching lines, 0 matching files** among those exact 225 immutable production-package Python bodies. The negative result is reproducible by enumerating the named tree population, reading each `git show fd2bcff...:<path>`, and applying that exact expression to each full body. This is source inspection with explicit coverage, not merely a GitHub code-search hit count. Indeed, GitHub's separately attempted indexed code search reported `incomplete_results=true` and zero hits even for a known-existing symbol, so it was *not* used as evidence of absence.

## Established positive caller and strict inference boundary

The historical `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py:56-76` defines the exact positive-rational `endpoint_weight`. The separate historical `experiments/x6_signed_native_spatial_v16_20260905/check_signed_brc.py:6-9,56-63` imports and invokes that function in a regression **test**. The earlier Unit200 confirmed its test call population of 15: three each with `K=0,1,2`, six parity-invalid zero cases; Unit200 directly executed 45 exact comparisons and a bounded 15-call timing experiment. Those existing experiments are preserved without rerun.

The new audit proves precisely: **the named pinned `src/enterprise_math` Python package does not contain a direct textual reference matching the specified prototype function/LP labels at the frozen commit**. It does **not** prove there was no production usage elsewhere in the 5,014-entry repository, no dynamic/aliased import, or no later consumer. It does **not** establish the existence or absence of alleged LP011 wrong-native argmax or LP019 positive-N-BRC subtraction callers outside this exact lexical/scope contract.

The current 28-LP claim ledger `X6-CL-008` still describes the two alleged historical wrong callers as `UNRESOLVED_PROVENANCE` with unknown `commit:path:line`; existing verified observer/native retypings and active-scoped KEEP decisions remain undisturbed.

## Exact ledger decision and unfinished work

**NEW:** A complete frozen 225/225 production-package direct-symbol census, 0 matches and 0 read errors. Do not migrate Unit198–200's test-only performance advantage into a deployed production optimization absent a true active consumer and its workload evidence.

**UNCHANGED:** R063 native six-file benchmark previously completed, not rerun; Unit200 author work immutable; Units175–200 Native semantic linkage and older Units149–152 pending fresh legitimate same-lane claim; Driver review `UNREVIEWED / NOT_ADMITTED`.

**NEXT:** Follow actual source imports outside this defined package (tests, experiments, command entrypoints, workflows, and any late consumer), and locate the true alleged LP011/LP019 call if it exists. For the newly canonical-dispatched `RS-X6-NATIVE-TIME-DYNAMICS` task, separately use its original typed continuation and author/admitted-resource conditions; never treat that selector decision as claiming this older legacy-plane task or borrow its predecessor's identity.

This is an author-side source-evidence unit, not a new mathematical axiom, a completed native benchmark, a published formal Result, or a production rewrite.
