# BRC-X6 D8: exact eight-absent native action support masks and 12 singleton fibers

**Date:** 2026-11-10. **Classification:** TASK_RESEARCH author-portable; EXACT_FINITE_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED; not an original Source execution, CLAIM, checkpoint, or Result.

**Frozen scientific pin:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Native four signed source ports `(6,7,28,29)` with signs `(+,-,-,+)`; six labeled actions per source (24 labeled coordinates); 96-port, nine-frozen-root full signed joint next-port/reward conservation. This analysis only uses lawful deterministic policies, independently reconstructed from this frozen model. The source order is:

```
0000 0011 0022 0044 0055 0123 0420 0521
1032 1133 1430 1531 2200 2211 2222 2244 2255
3300 3311 3322 3344 3355 4002 4103 4400
4411 4422 4444 4455 4501 5012 5113 5410
5500 5511 5522 5544 5555
```

Rows encode source order, digits encode labeled action 0..5. This exactly matches the sorted set of 38 original legal deterministic policies checked against all nine frozen roots using the inherited `frozen_native_kernel_prefix577.py` source. Each column of the native matrix `C ∈ {0,1}^{24×38}` has one 1 per source.

## Theorem: exact D8 support feasibility

Among all `binom(24,8)=735471` possible forbidden-eight-label masks, **exactly 5217** have 16-label complements that occur as the positive-coordinate support of `b=Cn`, with `n∈ℤ_{≥0}^{38}`, `Σn_j=8`. The remaining **730254** masks cannot arise from an eight-policy nonnegative integer representation under the 38 lawful original policies.

Let `k(M)` be the minimum number of **distinct** policies whose label union is the allowed support set `M`. Its exact histogram across the feasible 5217 masks is:

| k | 4 | 5 | 6 | 7 | 8 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| masks | 287 | 2344 | 2070 | 504 | **12** |

For precisely 12 masks `k(M)=8`; **each has exactly eight compatible lawful policies**. The sole degree-eight representation with all 16 allowed labels positive is then to use each of the eight policies once. Each of these 12 corresponding targets has a **singleton integral fiber among all 38 lawful columns**; no exchange path is needed.

The hexadecimal allowed-bit mask `M` (bit `6s+a` for source `s`, action `a`) and its unique eight policy indices:

```
ff7ce0: 30,31,32,33,34,35,36,37
ff7cd0: 22,23,24,25,26,27,28,29
ff7cc1: 0,1,2,3,4,5,6,7
dff833: 7,11,29,33,34,35,36,37
dff433: 6,10,24,25,26,27,28,32
dff073: 0,1,2,3,4,8,22,30
3c4ffd: 2,5,6,7,14,19,26,35
3c2ffd: 1,13,18,25,30,31,32,34
3c1ffd: 0,12,17,22,23,24,29,33
10ff7f: 2,8,14,19,22,26,30,35
08ff7f: 1,7,11,13,18,25,29,34
04ff7f: 0,6,10,12,17,24,32,33
```

All 12 rigid masks have missing-count profile `(5,2,1,0)` up to source permutation.

## Exact proof and complete finite coverage

A label set `M` is achievable as a degree-eight positive support iff there are at most eight distinct lawful policies `p_j⊆M` with union `M`. Necessity follows from the distinct positive coefficient support of any eight-policy integer representation; sufficiency follows by assigning weight 1 to the chosen policies and adding the remaining `8-k` units to any one chosen policy. Every such nonnegative integral combination preserves the original full nine-root signed joint flow since each column does.

**Method A (strategy-subset census):** Enumerate all subsets of the 38 distinct lawful policies of cardinality `1..8`. The subset counts by size are `38,703,8436,73815,501942,2760681,12620256,48903492`, totaling **64869363**. Encode a policy as four bits, one per source action at bit position `6s+a`. Union each subset's policy bits and, for popcount exactly 16, retain the smallest subset size by resulting 24-bit mask. Then enumerate all `735471` masks with 16 ones to collect the histogram and source profiles.

**Independent Method B (forbidden-label census):** Enumerate directly all `735471` forbidden 8-label masks. For each allowed `M`, select only lawful policies entirely contained in `M`; reject if their union is not `M`. On surviving masks, solve minimum set-cover by exact branching on a not-yet-covered label having the fewest compatible strategies, trying budgets `k=4..8` and pruning when uncovered labels exceed `4k`. There are exactly **5217** masks whose compatible-policy union equals `M`, and **all 5217** have cover size `≤8`. The independent minimum-cover histogram matches Method A exactly. Full run: **111110** recursive branches.

For the 12 `k=8` masks, enumerate their compatible-policy indices and check count exactly eight. Any degree-eight representation covering all allowed labels must then have eight distinct positive coefficients, so every compatible policy has coefficient exactly one. This proves uniqueness of each of the twelve integral fibers.

## Profile census (missing labels per source, decreasing order)

| profile | all masks | feasible |
| --- | ---: | ---: |
| 2222 | 50625 | 647 |
| 3221 | 324000 | 2636 |
| 3311 | 86400 | 824 |
| 3320 | 72000 | 204 |
| 4211 | 97200 | 420 |
| 4220 | 40500 | 192 |
| 4310 | 43200 | 272 |
| 4400 | 1350 | 10 |
| 5111 | 5184 | 0 |
| 5210 | 12960 | 12 |
| 5300 | 1440 | 0 |
| 6110 | 432 | 0 |
| 6200 | 180 | 0 |

## Verification, evidence and recovery

Locally compiled two independent C++20 exact integer programs and independently imported the frozen original 96-port, nine-root kernel to regenerate the full lawful 38-policy list in the same index order. All three checks returned **PASS**. The complete reproducibility bundle includes `d8_eight_missing.cpp`, `d8_eight_missing_independent.cpp`, `verify_native_policies.py`, frozen original kernel copy (with inherited source provenance), both execution logs, twelve exact 24-coordinate witnesses, and JSON evidence. Bundle SHA-256: `da0a0bb3879e83d0fbf91626eee97ddbc885151bdc3fa78ea4e6b88b29e18ad5`. The bundle is attached to the originating ChatGPT research turn; this Git record contains exact source-policy inputs, coverage and method needed to reproduce its claimed finite result.

**Scope:** 5217 counts feasible *support masks*, not distinct target count; 730254 counts support-infeasible masks in the lawful nonnegative degree-eight policy semigroup, not lattice holes. The other 5205 feasible support masks remain open for per-target quadratic-fiber connectivity and rational-column-span/integral-semigroup comparison.

**Predecessor used, not re-credited:** `enterprise-math@daa64dcd7119f5a2e9d0bda90c2aab96b2aab02e` D8 six-absent graph theorem and the already verified D2-D7 legal quadratic move set. The preceding D8 seven-absent local checkpoint was consumed as scope/status, not treated as present source files or re-proved. Next exact unit: classify degree-eight integer target fibers and quadratic connectivity **within these 5217 masks**, then contrast with rational-column-span integer targets. Native Source D25 claim/run were not obtained, so this remains author-portable evidence, not a formal Task Result. Separately, preserve UR V2 original four-file bundle provenance target: 94687 bytes, SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; not recovered in this turn.
