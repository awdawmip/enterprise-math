# PREFIX-751-R6 — Full /384 macro-support normalization through PREFIX-749, with exact fine-family intersections

Date: 2026-11-13 (Asia/Shanghai). Researcher-ID: `EM-DIRECT-A94071`; Activity-ID: `RA-74B4CD4EAA062E1E07F179AD`.
Frozen science: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Parent: PREFIX-675. Continuation: PREFIX-750A/B/C.
Evidence: **EXACT FINITE INTEGER-SET GEOMETRY**, author Gamma inequalities inherited and **NOT INDEPENDENTLY REVIEWED / NOT ADMITTED**. No native CLAIM, Result or Review is asserted.

## Precise question and domain

Earlier PREFIX-712 certified original fine cells
`F_uv=[u/768,(u+1)/768] x [v/768,(v+1)/768]` on `D=[0,1/2]^2`, `0<=u,v<384`. Later PREFIX-729–749 author certificates are stated on coarse physical rectangles
`R_ij=[i/384,(i+1)/384] x [j/384,(j+1)/384]`. Each `R_ij` contains precisely four `F`-cells, with distinct interiors.

The current goal is to **enumerate the physical support** of every later claimed full-macro-cell Gamma exclusion through PREFIX-749, without assuming that the previous mismatched-unit coverage totals are additive. The full PREFIX-712 fine membership mask is not in the source set read for this computation; therefore the *true all-history author union count remains unknown*.

## Lemma 1: normalized later support

Use the actual original family supports, **including portions that older reports already labeled overlaps**, not just their advertised 'new' indices:

* PREFIX-729–734: the two entire squares `A=[30,58)^2` and `B=[50,70)^2` of /384 cell indices. PREFIX-729, 730, 731, 732 and the 784-cell adaptive certificate are contained in A; PREFIX-733's 400-cell certificate is B. `|A|=784`, `|B|=400`, `|A∩B|=64`, `|A∪B|=1120`.
* PREFIX-735, 736, 737, 738: their full original rectangles and transposes, respectively `[58,70)×[70,76)`, `[58,70)×[76,96)`, `[40,58)×[76,79)`, `[40,58)×[79,96)`. They contribute, before collisions with other groups, 144, 480, 108 and 612 /384 cells.
* PREFIX-739: source-listed ten row ranges for `j=96..105`, with `i` lower bound 40 and upper bounds `58,58,58,58,58,58,58,55,52,46`; 159 upper and 159 transposed cells.
* PREFIX-740: `[58,70)×[96,104)` and its transpose, 192 cells.
* PREFIX-741–745: source-result coordinate arrays, with 97,18,15,8,70 upper pairs, each mirrored; 416 cells in all.
* PREFIX-746–749: 197 distinct source-listed upper pairs plus transposes, 394 cells **before collision**.

Exact integer-set comparison finds **only one further cross-family collision** among these groups beyond A versus B: the /384 upper cell `(30,52)` and its transpose occur in both A and the 746–749 sibling support. They account for **2 /384 cells = 8 original /768 fine cells**. No other cross-group collision occurs.

Therefore the exact union contains

```text
|M| = (784+400-64) + 144+480+108+612+318+192
      +194+36+30+16+140 + (394-2)
    = 3782 distinct /384 cells.
|fine(M)| = 4 * 3782 = 15128 distinct original /768 cells.
```

This is a **support count**, not a newly certified /768 count relative to the pre-729 historical union, and does not by itself establish the Gamma inequalities' validity.

## Lemma 2: exact intersections with explicitly enumerated historical fine families

Read the original PREFIX-713 coupled certificate, PREFIX-713 multicompetitor, PREFIX-716 and PREFIX-718 JSONs. Their disjoint source-certified /768 fine sets have respectively `90,20,1590,150` members (1,850 total).

Against all **15,128** fine children of the later support M, the verified exact intersections are:

| Earlier explicit family | Intersection |
|---|---:|
| PREFIX-713 coupled | 0 |
| PREFIX-713 multicompetitor | 14 |
| PREFIX-716 | 244 |
| PREFIX-718 | 84 |
| **All explicit non-712 historical fine sets** | **342** |

The 342 pairwise-disjoint collisions occur in the later families as follows: PREFIX-742 2, PREFIX-743 2, PREFIX-744 48 (=4+44), PREFIX-745 110 (=4+106), PREFIX-746–749 180 (=2+94+84). All preceding 729–741 groups have zero intersection with these enumerated extra historical sets. The arithmetic checks source arrays, not unverified historical claims about index non-overlap.

Additionally, PREFIX-750B's exact old-PREFIX712 witness computation enumerates **54 fine cells** of original PREFIX-712 coverage inside the sibling support. All 54 also lie in M. **Eight** of those 54 lie in the overlapping A / sibling macro pair `(30,52)` and transpose. This is a *known subset* of the original PREFIX-712 intersection, not the full PREFIX-712 intersection for M.

## Lemma 3: a necessary lower bound on prior PREFIX-712 overlap

The inherited historical PREFIX-718 author count is `139018=137168+1850`, where `137168` is original PREFIX-712 and `1850` comprises the disjoint explicit PREFIX-713/716/718 additions. Under those original source-family membership/count assumptions, the remaining original fine cells number `147456-139018=8438`.

Let `O712` be the original PREFIX-712 certified mask, `E` the 1850-cell disjoint later explicit mask. From Lemmas 1 and 2,

```text
|M_fine \ E| = 15128 - 342 = 14786.
|(D_fine \ (O712 ∪ E))| = 8438.
|M_fine ∩ O712| >= 14786 - 8438 = 6348.
```

Thus **at least 6,348 of the 15,128 later fine-support cells were already certified in the original PREFIX-712 baseline**. This is a precise counting consequence, not a speculative approximation. It proves that a direct sum of the older reported increments cannot give a valid overall coverage rate. The actual PREFIX-712 collision number may be larger; it must be determined from the genuine source mask / exact witness tests. The full true union numerator remains unresolved.

## Proof and computation

The map `(i,j) -> {(2i+a,2j+b):a,b∈{0,1}}` is injective on distinct /384 macro-cell interiors; each macro contributes four distinct /768 indices. Mirroring is ordinary coordinate transpose, with diagonal cells counted once. Every family is a finite rectangle or explicit integer-coordinate array. The companion `PREFIX751_R6_FULL_MACRO_FINE_SUPPORT_CHECK.py` reconstructs these families from pinned JSON inputs, computes source intersections and asserts the displayed exact counts.

In this research turn the full set arithmetic was **actually executed in JavaScript using GitHub-connector-returned original source arrays**, with all displayed integer assertions satisfied. The packaged Python script is a reproducibility artifact but **has not been separately run as an end-to-end local Python process**. The Gamma analytic inequalities remain inherited, author-side and unreviewed. The frozen pin was not rebased.

## Remaining scientific work

1. Recover or compute the original PREFIX-712 **complete /768 membership mask** on the 3,782 macro support cells, using exact old witness tests; then compute `|M_fine ∩ O712|` and a valid full author union `139018 + 15128 - 342 - |M_fine∩O712|`.
2. Check every later certificate's original analytic premises, particularly the coarsening-to-fine transfer and its all-real-`q>=2` quantifier. Re-run the published checker in an independent Python execution environment.
3. Only after this unified audit, target genuinely unexcluded fine cells for new auxiliary Gamma bounds. Neither this report nor its coverage arithmetic modifies P000, native X6 or the canonical shared CLAIM/Result/Review state.
