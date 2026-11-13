# R6 PREFIX-750A — Gamma certificate lattice-unit reconciliation (/384 versus original /768)

Date: 2026-11-13, Asia/Shanghai. Author session Researcher-ID `EM-DIRECT-5D86C4`; Activity `RA-048376E73CBA013C20DEEAFC` (registration is separate from shared CLAIM).
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Parent question: PREFIX-675; follows the 11-file sibling set union through PREFIX749 and the independently published PREFIX750. P000 and native X6 remain unchanged. The two-parameter Gamma model is an external auxiliary observer.

## Exact problem and discovered unit mismatch

The original PREFIX712 theorem explicitly works on `D=[0,1/2]^2`; it partitions D into 192×192 coarse cells and refines to 384×384 **fine** cells, each with physical side `1/768`. It reports `137168/147456` accepted fine cells for all real `q>=2`.

Later PREFIX741 and PREFIX745 code uses the literal `Fraction(i,384)` cell endpoints, and PREFIX746/114, PREFIX748/180, PREFIX749/28 and PREFIX750 explicitly define the later cells as

`R_ij=[i/384,(i+1)/384] × [j/384,(j+1)/384]`.

Consequently these are **original PREFIX712 coarse cells** of side `1/384`, not its fine cells of side `1/768`. They are fully within D for all the indices audited below (maximum index 66). The common statement “384×384 complete grid” describes different physical units in the two generations.

Let `F_uv=[u/768,(u+1)/768] × [v/768,(v+1)/768]`. For every integer index pair inside D,

```
R_ij = F_(2i,2j) ∪ F_(2i+1,2j) ∪ F_(2i,2j+1) ∪ F_(2i+1,2j+1).
```

This is an exact equality of **closed sets**, including shared boundaries. For `i<j` the transpose is distinct in interior, and one published original+transpose pair covers **eight distinct original fine cells**.

## New finite exact audit

Read the current connector-visible exact Git blobs of the sibling 11-result reconciliation, PREFIX741–745 and PREFIX750 (full SHA identities are in the companion JSON). Expand each distinct upper-coordinate pair by the formula above. The calculation uses integer pairs only: no floating approximation, no re-pinning and no assertion of Gamma theorem admission.

| Source group | Unique original upper pairs indexed by /384 | /384 cells including transposes | Original /768 fine cells |
|---|---:|---:|---:|
| 11 PREFIX746–749 sibling JSONs, already de-duplicated | **197** | **394** | **1,576** |
| PREFIX745 only | **70** | **140** | **560** |
| Combined PREFIX745 + sibling | **267** | **534** | **2,136** |
| PREFIX750 separately | **1** | **2** | **8**, all already in the 1,576 |

The sibling original 197 upper pairs are also disjoint (under the /384 coordinates and hence their expanded fine children) from all source-listed PREFIX741–745 upper pairs: those five predecessor sets comprise **208 distinct upper pairs**. The PREFIX750 original upper pair `(11,52)` and its transpose occur in the earlier sibling union, so its distinct incremental coverage is exactly **zero** on both coordinate lattices.

The sibling group by itself has absolute area `394/384²`; relative to `D` of area `1/4`, its exactly represented area is

```
(394/384²) / (1/4) = 1576/147456 = 197/18432 ≈ 1.0687934028% of D.
```

This is the exact area of the *published sibling rectangles*. Whether each claimed Gamma inequality withstands independent verification is a separate scientific question.

## Consequence for cumulative author ledger

The earlier `141942 + 394 = 142336` tally adds a count of original **/768 fine cells** (whose `141942` baseline itself inherits later /384 counts) to **/384 coarse cells**, then divides by `147456`. That operation is not a common-lattice cardinality or area calculation. In particular, `142336/147456 = 96.52777778%` and the derived remainder `5120` should be treated as *historical mixed-unit ledger arithmetic*, not a verified fraction/remainder of the original PREFIX712 domain.

The original PREFIX712 1×1 sufficient-test failure evaluated on a later /384 coarse cell does **not** show that each of its four /768 fine children failed the original sparse adaptive test; refinements can strengthen lower bounds. Thus the later documents' earlier-source disjointness needs correct fine-cell membership, not coarse failure or numerical equality of differently scaled indices.

A genuine corrected all-history coverage fraction requires the **complete original /768 cell membership mask** (including PREFIX712 retained 192-grid parent descendants and its additional accepted refinements), the fine-grid sets of PREFIX713/714/716/718, and four-child expansions for every later /384 certificate, followed by one set union and mathematical evidence scope check. This report does **not** propose a replacement all-history numerator without that calculation. It proves exact unit conversion, the finite contemporary intersections, and the PREFIX750 duplication.

## Reproducibility and provenance

- `R6_GAMMA_LATTICE_384_768_AUDIT.py`: standalone Python standard-library checker containing exactly the source-read coordinate pairs in compact form, with the eight-child reflection expansion.
- `R6_GAMMA_LATTICE_384_768_RESULTS.json`: exact source blob IDs, counts, intersection results and unresolved historical target.
- Actual in-turn verification: all source arrays fetched through the authorized GitHub connector, converted into integer sets, and tested against the assertions; **every stated finite-set assertion passed**. The separately published Python replay is provided for third-party execution and has not yet been run in its own Python process.
- Authors' Gamma proofs and reported strict margins remain `AUTHOR / UNREVIEWED / NOT_ADMITTED`; the present lattice identity is an exact finite combinatorial result.
- Native shared CLAIM/Result/Review: not requested or changed; this is portable independent Source research.

Next smallest useful unit: derive a common `/768` historical fine-mask from the actual published proofs and check overlap; then use its exact uncovered cells to guide further rational enclosures without credit duplication.
