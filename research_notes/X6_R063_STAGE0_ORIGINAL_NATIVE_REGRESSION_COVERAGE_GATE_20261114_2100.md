# X6 / R063 Stage 0 — exact native regression-coverage gate counterexample (2026-11-14)

**Mother:** `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`. **Source-bound author analysis**, `UNREVIEWED / NOT_ADMITTED`. No original benchmark was run, amended, or superseded by this note. Existing 17:00 safety-denied report was not reused.

## Source and frozen scope

The historical accepted R063 Stage 0 owner branch is `research/r063-stage0-path-valued-sqrt-2500`, exactly one commit ahead of taskbook `e7dd7af0b7f01168afd25e55d04900e841cc399e` (connected GitHub compare). Its *actual original loader* is `scripts/r063_stage0_validate_path_valued_sqrt_2500.py` (blob `b4e000a6377f2858ae434eb0eecd0c25c33e8592`) which lexically concatenates the five `part*.inc` objects. The five original source blobs, verified by connected GitHub full-body reads, in sorted loader order are:

| Object | Original Git blob |
|---|---|
| `scripts/r063_stage0_checker_parts/part00.inc` | `4a69c4d698887bce56323f393cb979609ce4ab0a` |
| `scripts/r063_stage0_checker_parts/part01.inc` | `913078c642b8995bfc135ef0350912387a17cdb8` |
| `scripts/r063_stage0_checker_parts/part02.inc` | `b543e185ec415b512c0ca0421616404cc12a19a7` |
| `scripts/r063_stage0_checker_parts/part03.inc` | `4f1bbf72abed19dc7dc605371872ee31c501cebe` |
| `scripts/r063_stage0_checker_parts/part04.inc` | `a1834a4b39a9d528760e67220b5fe5f368c9e655` |

The old review `driver_reviews/R063_STAGE0_PATH_VALUED_SQRT_2500_DRIVER_REVIEW_20260821.md` at `627c2cf273fe65db725b18062ca2783711b27411` accepted the actual full `1<=r<=512` run. The preserved old regression result `research_results/R063_STAGE0/R063_STAGE0_GENERAL_SQUARE_REGRESSION.json` (blob `0a5627760b960ac1a139b20eedea43664a0fb900`) reports `r_range=[1,512]`, `tested_r_count=512`, C3/C4 mismatches `0`, and rows SHA256 `51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae`. Those historical successful facts are **not** contradicted.

## Concrete validator contract gap

**Proposition (source-level, conditional on unchanged successful N=2500 direct tests).** The checker has a command-line configuration in which its named `GENERAL_R_SQUARED_REGRESSION_R_LE_512_PASS_OR_MINIMAL_COUNTEREXAMPLE_PRESERVED` gate evaluates `True` even though *none* of the required `r=1,...,512` regression cases has been tested.

**Exact witness:** supply `--regression-max-r 0` with the default `--N 2500`.

**Source proof:** `part04.inc` `parse_args()` accepts an unrestricted integer `--regression-max-r`; `main()` passes it to `run_general_regression(args.regression_max_r)` (`part04.inc`, near lines 237–258). `part02.inc` `run_general_regression(max_r)` iterates `for r in range(1, max_r+1)`. At `max_r=0`, the loop is empty, the independently accumulated `checker_mismatches` is empty, `combined_checker_mismatch_count=0`, `tested_r_count=0`, and `r_range=[1,0]`. Yet `part04.inc` `render_outputs()` defines the entire named general-regression acceptance gate as `regression["combined_checker_mismatch_count"] == 0` and `COMMITTED_DETERMINISTIC_CHECKER_PASS` uses only the central/test mismatch list. It does not require `r_range=[1,512]` or `tested_r_count=512`. Nothing in the related reporting logic treats an absent C2 first failure as an error (`part03.inc` explicitly handles `None`). Thus the gate itself is vacuously true without the mandated population. This is a **test-coverage/acceptance-predicate defect**, not a counterexample to the factorization theorem and not an assertion that the frozen reviewed 512-case run failed.

A separate local exact Python control-flow check of `range(1, max_r+1)` and the stated gate (not the original R063 executable) showed `max_r=0 -> tested_count=0, gate=True`; `max_r=1 -> tested_count=1, gate=True` if its sole tested case passes; `max_r=512 -> tested_count=512`. **No claim is made of executing the unmodified original command with max_r=0.**

## Exact correction / original-object next action

Do **not** mutate the old owner branch or replace its checker, C3/C4 implementation, five parts, frozen input or verification method. For any *new* same-object native replay, enforce `--N 2500 --regression-max-r 512` (or the original default 512) **and** independently gate the emitted `R063_STAGE0_GENERAL_SQUARE_REGRESSION.json` on all three: `r_range==[1,512]`, `tested_r_count==512`, `combined_checker_mismatch_count==0`; compare its `rows_sha256` to the original pinned digest above when replay identity is claimed. Under the original task's anti-leakage protocol, the discovery snapshot must be materialized/hashed before the brute verification, and the full original C3/C4 source/loader and output provenance must be retained.

The original native replay remains **UNEXECUTED IN THIS TURN**; direct transport of the five private GitHub code blobs into the local Python runner was unavailable through this conversation's authorized connector, which does not provide a local checkout. The historical archived 512-case artifact is valid evidence of the older run, not a new current-P000 six-axis acceptance. Assign same-object execution to an authorized repository runner/Codex environment if required; this note is a precise runnable input/coverage contract and a newly located historical test-gate issue, **not** the missing LP011 spatial argmax caller or LP019 natural positive N-BRC subtraction caller. All current signed-X6 and P000 scientific pins are unchanged.

**Next unresolved mother objective:** actual frozen/current dynamic LP011/LP019 wrong callers (if any), 28-LP dependency closure, independent Driver REQUEST_REVISION, and the original same-object R063 C3/C4 replay with full source/coverage/phase validation.
