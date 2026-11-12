# PREFIX-734-R6 — Exact union of two distinct PREFIX-733 Gamma certificates

Date: 2026-11-12 (Asia/Shanghai). Mother objective: PREFIX-675. Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: **AUTHOR_EXACT_SET_ARITHMETIC / INHERITED_AUTHOR_GAMMA_CERTIFICATES / UNREVIEWED / NOT_ADMITTED**.

## New result

Two separately authored PREFIX-733-R6 certificates target different 384×384 fine-grid blocks of the *same* frozen independent-Gamma maximum objective `V_q`, for all real `q>=2`, with the same strict comparator `e=(0,73/500)`:

- Certificate A: `[30,58)^2`, i.e. 784 complete fine-grid cells (28×28), in `2026-11-12_r6_prefix733_adaptive_gamma_28x28_union.md`, source program `PREFIX733_R6_ADAPTIVE_GAMMA_28X28.py`, and `PREFIX733_R6_SUMMARY.json`. It reports 504 new cells over the PREFIX-732 baseline.
- Certificate B: `[50,70)^2`, i.e. 400 complete fine-grid cells (20×20), with `V_q(e)-V_q(p,z)>76q²`. The program is `PREFIX733_R6_HALF_TILE_400_CHECKER.py`; its output is `PREFIX733_R6_RESULTS.json`. It reports 400 new cells over the *same* PREFIX-732 baseline.

These are different scientific artifacts sharing the label PREFIX-733; their separate filenames and immutable blob identifiers are essential.

## Exact grid-set theorem and proof

Let `C` be the 139,140 previously certified grid cells in PREFIX-732. Let `A=[30,58)^2` and `B=[50,70)^2` in integer cell-index coordinates. The source certificates give:

```
|A|=784; |B|=400; |A∩C|=144+136=280; |B∩C|=0.
A∩B=[50,58)^2, so |A∩B|=8²=64.
```

Because `B∩C=∅`, none of the 64 intersecting cells is in `C`. Exact inclusion-exclusion yields:

```
|(A∪B)\C|=(784-280)+400-64=840.
|C∪A∪B|=139140+840=139980.
139980/147456 = 11665/12288 = 94.9300130208333...%.
147456-139980=7476 cells not yet certified excluded.
```

For each cell of `A∪B`, the corresponding inherited all-real-`q>=2` strict comparator inequality excludes a global maximizer from the entire continuous cell. The 840-cell addition is a **deduplicated union** rather than a newly computed Gamma inequality. Compared with the 28×28-only count of 139,644, it adds exactly **336** additional uniquely certified cells. This is a new exact finite-set deduction from the two separate predecessor certificates.

## Source pin and verification scope

The source records were read at immutable `enterprise-math@e1fa6b92dc599f059f4c7e67673330c3dcd69d95`:
- `PREFIX732_R6_RESULTS.json` blob `c53979fd92cc7e00d37d7ab5aa99b2584fab96ce`
- `PREFIX733_R6_SUMMARY.json` blob `edda0b59f6f6c78e9b0c10f5c7b10becfbc49809`
- `PREFIX733_R6_RESULTS.json` blob `bddc9059502b7f20d4154aeff2fc1a89daa19643`

The accompanying checker compares source fields and enumerates all indexed cells using exact integer set arithmetic. The source-record comparison and geometry were executed in a current GitHub connector read plus an independent local Python standard-library calculation on extracted fields, both passing.

The Gamma inequalities and 136/0 historical overlaps remain inherited **author-grade** exact evidence; this round did not rerun the 189-layer Gamma kernel and does not claim independent review. Additionally, the 28×28 checker would write the same `PREFIX733_R6_RESULTS.json` name as the existing 20×20 checker. Retain both original artifacts; future end-to-end reproduction must emit distinct 28×28 and 20×20 output filenames before recomputing the merged union.

## Next discriminating unit

Run both Gamma verification kernels independently under distinct output names, compare the original integer-moment hashes and the exact 136/0 old-union overlap sets, then certify adjacent cells outside `[30,58)^2 ∪ [50,70)^2`. Record new set coordinates before modifying the cumulative excluded total. Maintain current active-owner and canonical Result/Review boundaries.
