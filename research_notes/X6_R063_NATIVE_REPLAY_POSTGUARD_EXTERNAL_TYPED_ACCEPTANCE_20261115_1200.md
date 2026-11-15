# X6 / R063 — Original Stage0 replay external acceptance guard

Date: 2026-11-15 (Asia/Hong_Kong).
Mother: RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2.
Research lane: chatgpt-research-onhour-enterprise-math-20260923.
Author: EM-X6-FB6990 / SID MCP-082892eb480e45dea6d4b9fcc0491034.
Classification: ORIGINAL_BENCHMARK_ACCEPTANCE_CONSUMER / BOUNDED_EXECUTED_MUTATION_TESTS / UNREVIEWED / NOT_ADMITTED. Original native R063 benchmark NOT rerun in this Chat.

## Frozen inputs and actual original executable

Current P000 V5 science pin: awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03. Historical comparison pin @fd2bcff10ca6e147348b6c1236027fc0d2877df3.
Original owner branch: research/r063-stage0-path-valued-sqrt-2500.
Original loader: scripts/r063_stage0_validate_path_valued_sqrt_2500.py, Git blob b4e000a6377f2858ae434eb0eecd0c25c33e8592.
The loader concatenates five original sorted include files part00–part04.inc with respective Git blobs: 4a69c4d698887bce56323f393cb979609ce4ab0a; 913078c642b8995bfc135ef0350912387a17cdb8; b543e185ec415b512c0ca0421616404cc12a19a7; 4f1bbf72abed19dc7dc605371872ee31c501cebe; a1834a4b39a9d528760e67220b5fe5f368c9e655.
Previously accepted historical output remains intact. Native support issue: https://github.com/awdawmip/enterprise-math/issues/2416 (OPEN, unassigned on this read).

## New executable research result

External pure-stdlib acceptance guard:
https://github.com/awdawmip/enterprise-math/blob/ed450ba355c17d77cadaa8075e4eaf5c1567618e/research_checks/X6_R063_STAGE0_NATIVE_REPLAY_ACCEPTANCE_GUARD_20261115_1200.py
Git blob 74d63403c8921ee2ffddadafab3581d8ed978e9f, SHA256 947083595cb9a7a305aafaaef5c86be021294e7bb29fee7a111390dec4ad8ea6.

The guard reads SIX generated original JSON artifacts, enforces all 17 exact named Boolean output gates, complete r_range=[1,512], tested_r_count=512 and zero C3/C4/combined mismatches. It verifies regression rows SHA256 51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae and the frozen discovery canonical JSON SHA256 6dd26e75436fb6740134590fc243b59ab9eb287cadbc46d417d5bbbb74022f0d by recomputation after stripping only its embedded marker. It checks typed C2 incomplete, C3/C4 complete, zero original mismatch objects and all SIX ordered two-generator positive sector roots (0,50),(14,48),(30,40),(40,30),(48,14),(50,0).

Exact Python integer BRC checks recompute each binomial path cardinality and the total 110695538274255714208. Duplicate JSON keys, nonfinite numbers, rounded large branch cardinalities, wrong root order, missing gates/files, and vacuous 0-case regression fail closed. The guard does not alter original discovery, checker or benchmark.

Mutation test:
https://github.com/awdawmip/enterprise-math/blob/a8f91bdffc167990f2de3d28bb3c891b39ed4d7e/research_checks/X6_R063_STAGE0_GUARD_MUTATION_TEST_20261115_1200.py
Git blob 899549b5db999e9859d5c5595bccef8a40635629, SHA256 7067affee0a6453877e6815bc3cb96bd0a9ffd81dc3d957b712d801107cb7394.

Local byte-matched execution gave a positive synthetic 512/17/6 fixture PASS and three expected failures: vacuous tested_r_count=0, float-rounded (30,40) BRC cardinality 55347740058143510000 in place of 55347740058143507128, omitted SCALAR_SQRT_2500_EXACT gate. Terminal: PASS_X6_R063_STAGE0_GUARD_MUTATION_FIXTURES. The fixture substitutes its own local discovery digest intentionally; it is NOT the frozen historical discovery or native benchmark execution.

## Exact next authorized runner action and limits

In authorized original-branch checkout, verify all six original source blobs, isolate a new output directory, then execute:
  python3 scripts/r063_stage0_validate_path_valued_sqrt_2500.py --N 2500 --regression-max-r 512 --out ISOLATED_OUTPUT
  python3 research_checks/X6_R063_STAGE0_NATIVE_REPLAY_ACCEPTANCE_GUARD_20261115_1200.py --out ISOLATED_OUTPUT

Runner must record ORIGINAL process exit, the discovery materialize-and-hash-before-brute sequence, all original 17 gates, complete 512 regression, unchanged frozen source inputs, generated output SHA256 and commit/path readback. Only the actual original program can establish a fresh same-object benchmark execution. The external guard checks emitted artifacts but does not establish original invocation, source blobs, provenance of file generation, or independently prove internal gates. Keep two-axis positive-sector original output distinct from full signed X6 and selected native three-axis shell.

This is a concrete reusable acceptance consumer for the same OPEN issue #2416, not a new task/CLAIM, not a substitute experiment and not a repeat of previously closed auxiliary theory. Next Source action: source semantic checkpoint for prior #30 and this #31 under original current Researcher/SID/CLAIM/RUN with original request reconciliation and CAS. Remaining parent: actual LP011 historical native argmax and LP019 natural-positive signed-cancellation wrong caller provenance UNRESOLVED_PROVENANCE; 28-LP complete consumer closure and independent Driver REQUEST_REVISION outstanding. Do not replay the previously safety-denied 17:00 prose mutation.
