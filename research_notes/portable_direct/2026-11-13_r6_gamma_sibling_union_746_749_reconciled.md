# R6 Gamma auxiliary sibling certificate union: exact 746–749 reconciliation

Date: 2026-11-13 (Asia/Shanghai). Source read: `awdawmip/enterprise-math@4de5b0a37946f6463b4543270a0676d764c15b3a`. Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Mother objective: PREFIX-675.
Scope: 384×384 closed-grid parameter cells for the frozen 189-layer stopped-survivor, two-independent-Gamma-clock auxiliary model. The source certificates concern all real `q≥2` and fixed comparison point `e=(0,73/500)`. This is a **coordinate-union audit**, not a new evaluation of the Gamma inequalities or a shared Result/Review.

## Exact finite-set result

Read **11** published, version-pinned author-side JSON certificate datasets representing PREFIX-746, 747, 748 and 749 sibling branches. Each has a list of distinct integer upper-diagonal pairs `(i,j)` with `0≤i<j<384`. Map the listed pairs to complete closed cells `R_(i,j)`, and reflect them by `(i,j)↦(j,i)`. For these sources, transposes are distinct and the map is one-to-one within the original upper-triangle.

Let `S_k` be the upper pairs of source `k`. Then direct finite set operations on the complete listed integer arrays give
```
|S_746,747,748,749| = |union_k S_k| = 197,
number of distinct reflected cells = 394.
```
The reproducible script checks every element, the scientific source pin, file blob SHA1, expected cardinality and overlaps. This combinatorial statement uses no floating-point approximation.

| Source | Raw reflected | Repeated within previous sibling union | Newly distinct reflected |
|---|---:|---:|---:|
| PREFIX746/114 | 114 | 0 | **114** |
| PREFIX746/30 | 30 | 14 | **16** |
| PREFIX747/68 | 68 | 12 | **56** |
| PREFIX747/4 | 4 | 4 | **0** |
| PREFIX747/46 | 46 | 28 | **18** |
| PREFIX748/180 | 180 | 0 | **180** |
| PREFIX748/4 | 4 | 4 | **0** |
| PREFIX749/28 | 28 | 24 | **4** |
| PREFIX749/4 | 4 | 4 | **0** |
| PREFIX749/6 | 6 | 6 | **0** |
| PREFIX749/16x16/6 | 6 | 0 | **6** |
| **Total** | **490** | **96** | **394** |

PREFIX-748's sibling-deduplicated predecessor baseline `142326` is recovered exactly after sources through PREFIX-748/4. Of later PREFIX-749 branches, `PREFIX749/28` adds only **4** previously absent reflected cells, namely `(8,50),(9,50)` and their transposes; its other 24 reported cells were certified in the preceding sibling union. PREFIX749/4 and PREFIX749/6 add **zero** to the combined ledger. PREFIX749/16x16/6 contributes **6** new reflected cells at `(12,56),(13,57),(14,59)` and transposes.

**Conditional on the inherited PREFIX-745 author-side ledger** (141942 distinct cells, historically reported with incomplete full-history independent audit), the reconciled count is
```
141942 + 394 = 142336 of 147456 cells,
142336 / 147456 = 142336/147456 = 96.5277777778%,
uncertified under this ledger = 5120 cells.
```
This is an exact reconciliation of the **eleven named source coordinate arrays**. It repairs overlapping sibling claims, including independent documents that label the same cells as newly found. It does not upgrade their author-side Gamma proof certificates to independently admitted mathematics, and it leaves a complete pre-PREFIX-746 union audit open.

## Reproducibility, claim scope, and next problem

- Source list, exact Git blob identities, 197 unique upper pairs, overlap table, inherited premise, and audit status: `PREFIX_R6_GAMMA_SIBLING_UNION_746_749_RESULTS.json`.
- Deterministic Python 3 standard-library source loader and finite-set checker: `PREFIX_R6_GAMMA_SIBLING_UNION_746_749_CHECK.py`. It checks exact local source-file bytes against 11 Git blob hashes before computing the union. The same set union was independently executed here directly from successful GitHub connector reads of all 11 published JSONs; the published Python program has not separately been run end-to-end in a local checkout.
- Scientific arithmetic: retain frozen `f42f2906d77f24085c123f3ccfe9667d41caa96d`, no P000/ACTIVE worldview changes. No active shared CLAIM, formal Result or independent review is asserted.

**Next high-value science:** review the complete historical PREFIX-712–745 certificate union with appropriate 384/768-grid translations, then isolate genuinely uncertified cells and test witnesses/adaptive rational rectangles. This may alter the inherited 141942 premise, without altering the proven 197-pair finite source union.

Evidence grade: **EXACT_GITHUB_SOURCE_SET_RECONCILIATION / AUTHOR_GAMMA_CERTIFICATES / UNREVIEWED / NOT_ADMITTED**.
