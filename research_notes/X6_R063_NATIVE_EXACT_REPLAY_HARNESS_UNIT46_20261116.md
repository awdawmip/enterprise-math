# X6 / R063 original-object native replay acceptance harness — executable support unit (2026-11-16)

Status: **AUTHOR-EXECUTED HARNESS TESTS / NATIVE ORIGINAL NOT YET EXECUTED / NO RESULT ADMISSION**  
Mother task: \`RS-X6-LEGACY-PLANE-RECONCILIATION\`; Researcher: \`EM-X6-FB6990\`; session \`MCP-082892eb480e45dea6d4b9fcc0491034\`.  
Applicable ontology: frozen P000 V5 signed X6 at \`59538f585d037d09ef687b28715c4bc1a3f9fe03\`; R063 experiment remains **only the original selected positive two-generator source object**, not a full signed-six-axis native simulation.

## Actual advance

Implemented a *small, independently validated outer replay harness* for the existing original Stage0 program. Unlike the previous independent mathematical oracles, the wrapper invokes the **unchanged original six-file Python source**, not a reimplementation. It refuses to run if any one of the six pinned Git blobs differs and directs the original program to a new isolated output directory.

Source and test files, byte-verified after GitHub publication:

- [Original-object harness](../research_checks/X6_R063_PINNED_NATIVE_REPLAY_ACCEPTANCE_HARNESS_20261116.py), Git blob \`d93add4c440fc453a16555d86d5e0aefc966d38b\`; actually executed local source SHA256 \`267e17be97c6af66d568008a11a932dac1ca95a4254131038333c14ee67af987\`.
- [Synthetic positive/negative fixture tests](../research_checks/X6_R063_PINNED_NATIVE_REPLAY_HARNESS_TESTS_20261116.py), Git blob \`0a07c09a649aa37373a0e5cb2a81b5b87d316d12\`; actually executed local source SHA256 \`fbbf1aa03caed08362cbb6a291eff5217264810ab25f6a09e1d55fe61284ca30\`.

### Native source pins, all independently read with authorized GitHub connector

Original branch: \`research/r063-stage0-path-valued-sqrt-2500\`; loader:
\`scripts/r063_stage0_validate_path_valued_sqrt_2500.py\`, Git blob \`b4e000a6377f2858ae434eb0eecd0c25c33e8592\`.

The five exact ordered \`scripts/r063_stage0_checker_parts/part00.inc\` through \`part04.inc\` Git blobs are:
\`4a69c4d698887bce56323f393cb979609ce4ab0a\`,
\`913078c642b8995bfc135ef0350912387a17cdb8\`,
\`b543e185ec415b512c0ca0421616404cc12a19a7\`,
\`4f1bbf72abed19dc7dc605371872ee31c501cebe\`,
\`a1834a4b39a9d528760e67220b5fe5f368c9e655\`.

The harness invokes *exactly*:
\`\`\`sh
python3 research_checks/X6_R063_PINNED_NATIVE_REPLAY_ACCEPTANCE_HARNESS_20261116.py \
  --repo-root <authorized-frozen-R063-checkout> \
  --output-parent <isolated-output-parent>
\`\`\`
Inside it the original loader receives:
\`\`\`sh
python3 scripts/r063_stage0_validate_path_valued_sqrt_2500.py \
  --N 2500 --regression-max-r 512 --out <new-isolated-output-dir>
\`\`\`
It does not alter the six original scripts, the discovery/brute phase ordering, the mathematical candidate, source pin, gate semantics or regression input.

### Independent acceptance gates, stricter than vacuous original-only PASS

After an original-process exit of 0 and terminal \`PASS\`, verify all **13** expected artifacts, exact **17 original gate names with Boolean true** (read against the original part04 source), exact regression \`r_range=[1,512]\`, \`tested_r_count=512\`, C3 and C4 mismatch counts zero, source-specific 512-row SHA256 \`51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae\`, N=2500/r=50, six ordered sector roots and positive-chart natural BRC \`110695538274255714208\`.

Compute the pre-verification discovery JSON canonical SHA256 after removing only its appended \`discovery_snapshot_sha256\` field, compare with the stored field, original frozen snapshot digest \`6dd26e75436fb6740134590fc243b59ab9eb287cadbc46d417d5bbbb74022f0d\`, summary reference and terminal reference. Recompute the replay summary core SHA256, check mismatch artifact, preserve original stdout/stderr, original process exit, exact six source Git blob IDs, and SHA256 of each actual output artifact in \`REPLAY_HARNESS_INDEPENDENT_ACCEPTANCE.json\`.

This independent acceptance wrapper directly closes the **vacuous coverage gate** observed in the original source when \`--regression-max-r 0\` is passed, without changing the frozen program or treating the original gate as false on its valid historical 512-case run. It also catches hash-consistent changes to a false acceptance gate.

### Actual local execution performed

\`python -m py_compile\` succeeded. The harness and synthetic test files ran locally with exit code 0:

\`\`\`text
PASS_SYNTHETIC_POSITIVE_SCHEMA_FIXTURE
PASS_REJECT_zero_cases
PASS_REJECT_shorter_range
PASS_REJECT_wrong_hash
PASS_REJECT_false_C3_mismatch
PASS_REJECT_FALSE_GATE_WITH_SELF_CONSISTENT_SHA
PASS_HARNESS_SYNTHETIC_TEST_SUITE; ORIGINAL_NATIVE_R063_NOT_EXECUTED
\`\`\`

**The positive fixture is synthetic and uses a synthetic substituted digest for the harness unit test only. It is neither an original R063 replay nor an accepted research Result.** The real harness restores original immutable digests when run normally. Executed files were hash-matched against the newly published GitHub blobs.

## Owner, remaining evidence, exact handoff

The original Stage0 native six-file replay **has not yet executed in this Chat/container**, because the authorized GitHub connector can verify remote pinned source blobs but there is no local checkout of all six original executable files and no approved connector-to-local source transport. The separate independent 512-radius certificates are not a substitute. Original execution support [#2416](https://github.com/awdawmip/enterprise-math/issues/2416) remains the responsible support path; there is **no verified executing owner**.

Next actor: authorized EM repository runner/Codex with exact original checkout. Run the committed harness, record actual original process exit, output directory, the 13 output artifacts and hashes, 17 gates, fully 512 tested rows, original snapshot SHA, 512-row digest; publish immutable evidence on the original task continuation. Until then \`NATIVE_R063_SAME_OBJECT_EXECUTION=PENDING_UNASSIGNED\`, not PASS or rejected. The mother task additionally needs LP011/LP019 exact historical caller provenance, 28-LP downstream consumer closure and independent Driver review.

Existing unit #1–45 research, original Source claims/Run, historical frozen artifacts and schedule are retained. This harness is an actionable **new experiment-execution/validation unit**, not another C2/C3/C4 auxiliary theorem.
