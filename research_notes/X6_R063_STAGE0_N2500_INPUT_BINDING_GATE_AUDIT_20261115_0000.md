# X6 / R063 Stage 0 — exact input-identity gate audit (2026-11-15 00:00 Asia/Hong_Kong)

Mother: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`; Researcher `EM-X6-FB6990`; own SID `MCP-082892eb480e45dea6d4b9fcc0491034`; original CLAIM `MCP-30a8f5fd123215e08bd4a7cf` and RUN `RUN-3356cbe3c2b4916d79399941`. This is an independently new **frozen-source validation-contract audit**, not a replay of the original native benchmark, not mathematical admission, and not the previously host-denied 17:00 Stage 2 prose report. Status: AUTHOR-VERIFIED SOURCE-LEVEL / ORIGINAL SAME-OBJECT BENCHMARK NOT RUN / UNREVIEWED / NOT_ADMITTED.

## Immutable input and file identities

Original owner branch `research/r063-stage0-path-valued-sqrt-2500`, taskbook `e7dd7af0b7f01168afd25e55d04900e841cc399e`.
Loader `scripts/r063_stage0_validate_path_valued_sqrt_2500.py` Git blob `b4e000a6377f2858ae434eb0eecd0c25c33e8592`.
Five ordered `scripts/r063_stage0_checker_parts/part0{0..4}.inc` blobs: `4a69c4d698887bce56323f393cb979609ce4ab0a`, `913078c642b8995bfc135ef0350912387a17cdb8`, `b543e185ec415b512c0ca0421616404cc12a19a7`, `4f1bbf72abed19dc7dc605371872ee31c501cebe`, `a1834a4b39a9d528760e67220b5fe5f368c9e655`.
All six original connected-GitHub source bodies were directly read and exact Git blob identities checked; the original files/branch were not modified. Current signed-X6 P000 V5 remains frozen at `59538f585d037d09ef687b28715c4bc1a3f9fe03`.

## New independent defect: "N=2500" is not bound by its named acceptance gates

In original `part04.inc` lines 237–241, `--N` is an unrestricted integer option with default `DEFAULT_N=2500` (part00 lines 21–27); `main()` passes its selected value to `discover_from_scalar_root(args.N)` (part04 lines 245–259). The source checks that N is a nonnegative square (part01 lines 138–144), **not** that the task-required input equals 2500.

The actual named gates in part04 lines 141–160 are:
- `SCALAR_SQRT_2500_EXACT`: `discovered["scalar_root"]["r"] ** 2 == discovered["input"]["N"]`.
- `DISCOVERED_COMPONENT_ROOTS_MATCH_D2500_EXACTLY`: `verification["comparisons"]["C3"]["exact_set_equality"]`.
- `C2_UNSCALED_SQUARE_LIFT_CLASSIFIED`: `not verification["comparisons"]["C2"]["exact_set_equality"]`.
- `GENERAL_R_SQUARED_REGRESSION_R_LE_512_PASS_OR_MINIMAL_COUNTEREXAMPLE_PRESERVED`: `regression["combined_checker_mismatch_count"] == 0`.
- `COMMITTED_DETERMINISTIC_CHECKER_PASS`: `len(checker_mismatches) == 0`.

None binds the input `N` to 2500. In particular, the N2500-named comparisons are against the brute root set for the **same run-selected N**, not the frozen `N=2500` target. The separately computed generic 1..512 regression uses only `--regression-max-r` and is independent of the selected central N. The final PASS status is determined only by those gates and mismatch list (part04 lines 264–276). The summary also records the true N, so full artifact inspection can detect the discrepancy; the defect concerns *acceptance predicates and reliance on PASS/gate names alone*, not hidden alteration of the recorded input.

## Explicit discriminating witness: N=25 without changing the 512 regression

Consider the original argument shape `--N 25 --regression-max-r 512` (not executed as an original replay here).
Exact central-target mathematics gives `r=5` and the full ordered nonnegative sector root set
`{(0,5),(3,4),(4,3),(5,0)}`.
C3 obtains the two axes through `k=5,h=1,(m,n)=(1,0)` and the two non-axis roots through `k=1,h=5,(m,n)=(2,1)`; C4 Gaussian factor-allocation yields exactly the same four solutions. C2's unscaled square of `2+J` yields only `(3,4),(4,3)`, so its deliberately negative-classification gate is **also true**. The four binomial path counts are `1,35,35,1`, giving total `72`, not the N2500 path total. The component/root/generator and norm formulas are exact at N25.

A literal scan of the full six original source bodies for each original `source_hardcode_scan` pattern `(3, 4)`, `(3,4)`, `[3, 4]`, `[3,4]` and their swapped forms found **zero** matches, so the corresponding hardcode gate does not block this witness. The C3/C4, norm, binomial, trace and source-typed predicates are independent of the fixed constant 2500. Under the unchanged, separately archived successful 1..512 regression (r_range=[1,512], 512 cases, zero C3/C4 mismatches), the 17 source gate predicates are compatible with N25 and do not certify the frozen central input. This is an exact **source-level input-identity nonimplication**, not a claim that the original `--N 25` command was run or that any new output was byte-verified.

The original correctly parameterized N2500 archived run and Driver acceptance remain intact. Preserved regression rows SHA256 `51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae`; historical N2500 discovery snapshot `6dd26e75436fb6740134590fc243b59ab9eb287cadbc46d417d5bbbb74022f0d`.

## Consequence / bounded next action

For any future *authorized original-object* replay under existing support [issue #2416](https://github.com/awdawmip/enterprise-math/issues/2416), require both central **input binding** `summary.N == discovery.input.N == 2500` and `scalar_root.r == 50`, and distinct complete **regression coverage** `r_range == [1,512]`, `tested_r_count == 512`, `combined_checker_mismatch_count == 0`, verifying exact source/phase/digests before declaring original acceptance. This newly found input-binding gap is separate from the previously proved `--regression-max-r 0` vacuous-coverage gap [3542a613](https://github.com/awdawmip/enterprise-math/blob/3542a613a9bb857383b8214b74a44d04045698bc/research_notes/X6_R063_STAGE0_ORIGINAL_NATIVE_REGRESSION_COVERAGE_GATE_20261114_2100.md).

No original R063 C3/C4 program was run or modified; no replacement native benchmark was claimed. No actual historical LP011 wrong signed-native argmax caller or LP019 wrong positive-natural-N-BRC cancellation caller was discovered; both remain UNRESOLVED_PROVENANCE, alongside full 28-LP consumer closure and independent Driver REQUEST_REVISION. Do not replay the host-denied 17:00 Stage2 prose write.