# PFSSV Stage 1 — independent bounded review

Conclusion: **PASS within the reviewed Stage 1 scope; no substantive blocker found.**

This memo records the read-only review already completed on 2026-09-08. It adds no new execution or check. The reviewer did not rerun the probe, run new mathematics, read the editing Stage 2 source, or issue a formal Driver verdict.

## Frozen input and provenance

- Input: `D:/em/TEMP/pfssv-stage1-20260908/stage1-publication.json`.
- Manifest SHA256: `47c0e0ca4e0fd26e0eb5c16d08902cc3ba63f561d73587ebf4a7a920012a8bc5`.
- All 11 files under its `frozen-source/` snapshot were independently checked against the manifest's SHA256 and byte lengths; all matched.
- Script SHA256: `37684dece1a454858ca5e89b5cb63ed88a65a2b6f86862aee5e89a30e51bde56`.
- Test SHA256: `ea5cbe7c5a2da743df9b03ba9d49c4b8b54d7a7c9f94f8c66e731f2a6a2fbe0e`.
- Root reported source-only publication `01b6dd932f62fd3b0a6f3b06d29ff809b04ed62e`; this review used the frozen local bytes and did not independently perform remote readback.

## Findings

1. **BRC interval bins.** The script uses canonical DIV/ROOT/LOG entrypoints. For raw/small-trim coordinates, interval numerators and positive denominators give conservative lower/upper bin bounds. The scale-trim and coarse-band transforms are monotone. Density-flat composition bounds `log_3(3u/(1-u))`, retaining the known `u>1/4` domain when its coarse lower endpoint overlaps that boundary. A bin is accepted only when both bounds agree; finite refinement exhaustion raises `PrecisionUnresolved`. Exact right endpoints use the declared final bin. This is a paper/static check of the frozen implementation, not a new numerical run.

2. **Complete ranks and support.** The additive sieve creates a complete bounded prime prefix. The shell uses `max(p, floor(X/p)+1) <= q <= floor(U/p)`; nonempty integer windows remain even when their prime count is zero. Stored `pi_p` and q-rank endpoints refer to the complete prefix, not surviving row order. The 24-by-24 grid intersects those exact rank intervals. Empty integer windows are separately enumerated. Counts with `p*p>X` remain in raw/rank totals and a separate overflow stratum rather than being clipped into the last log bin.

3. **Decisive original Null A capacity violation.** The immutable old source at `2aa103eee829b78fa7784674ec1be4c3c5052a79`, `scripts/check_prime_factor_semiprime_shell_residual_validation.py`, has SHA256 `8772484435d77abf74e87a6f053a0edaf4fa9395bdbade93ede2413083f22140` and Git blob `c2e6319ab0f52a2ac7d0ad4845d345c96177eb8d`. Lines 94–107 group by coarse band and p residue, then independently permute each q-residue channel. Its band formula agrees with the frozen exact formula on this witness's domain.

   In the already-executed probe, the band-2 / p-mod-30-equals-7 group consists exactly of p=97 and p=127. **Both rows have total count 2, so both survive the old `counts>0` mask; this particular counterexample also survives that old mask.** Their q-mod-30-equals-17 channel values are 1 and 0. The target window is [15749,15763]; the first integer congruent to 17 mod 30 at or above its lower endpoint is 15767. Its integer residue capacity is therefore zero. The permitted two-label permutation sends the p=97 channel to p=127 with probability 1/2. No random draw, clipping, rejection sampling, or null repair was used. This refutes an exact factor-window-occupancy interpretation of every allowed draw; it does not forbid studying the original scalar surrogate with its limitations stated.

4. **Actual trace consistency.** The unchanged canonical DIV and ROOT source SHA is `f4f8feead82dc53a35e5fec495b31e46e64820f7b115c9efd6034063e68f8ad6`; LOG source SHA is `cb9ce27bbea7ac9d264c8e013c4f3d0ef830842feae7ec63fe5dc39de79b8343`. Their exact immutable source contracts were read. The frozen profiler captures original canonical function code objects. Parsing the existing trace independently found 6495 definitions plus 19 references: 6514 events, comprising 5861 DIV, 8 ROOT, and 645 LOG. Every definition digest matched, every reference pointed to a preceding definition, and the per-function counts agreed with the author's recorded call and return counts. LN was an observed identity candidate, not an executed entrypoint in this receipt. This is not a claim of transitive migration of every imported dependency.

## Execution evidence and limits

The original logs, whose hashes were checked against the frozen manifest, record 11 tests PASS (unittest 0.032 s; process receipt 0.750 s), the selected two-file static gate PASS, and one new bounded probe PASS (internal 5.422 s; process receipt 5.781 s). That probe stored 223 rows, including 116 zero-count rows, and 393 raw pairs. These are the author's actual executions, not independent reruns.

Trace SHA256: `160c1321da7b706e1201247f61269e08e46ef7b4e656e17de867303378e38572`.

Stage 1 does not establish a 21-cell scientific conclusion, the 512/4096 screen, a repaired Null A, a joint-rank null, a fresh blind holdout, or formal Driver acceptance. Full-scale resource behavior remains outside this review. The adjoining `receipt.json` records exact paths, existing argv/log hashes, and the independent observation tool chunks.
