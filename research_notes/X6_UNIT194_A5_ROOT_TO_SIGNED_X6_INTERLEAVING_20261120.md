# X6 Unit194 — Exact A5 transfer-to-native signed-X6 BRC shuffle fiber

**Author scope:** RS-X6-LEGACY-PLANE-RECONCILIATION, immutable publication TP2-B4A441B23DA3159232C2, mother PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905; Research lane `chatgpt-research-onhour-enterprise-math-20260923` only.
**Scientific input pin:** `59538f585d037d09ef687b28715c4bc1a3f9fe03`; **frozen source comparison pin:** `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.
**Status:** AUTHOR_PROVED / SOURCE_FORMULA_MATCHED / EXACT_FINITE_BIGINT_EXECUTED / GITHUB_EVIDENCE / UNREVIEWED / NOT_ADMITTED. No Native PROGRESS, Result, independent review, P000 change, or original R063 rerun.

## Actual typed sources and research question

At the immutable historical comparator, `src/enterprise_math/p022_geodesic_multiplicity.py:49–91` defines `a_graph_radius`, `sc_graph_radius`, `a_geodesic_path_count`, and `sc_geodesic_path_count`. The original code counts *A_p root-transfer graph moves* `e_i-e_j` and *simple-cubic signed unit-axis graph moves* separately. The actual signed X6 BRC kernel `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py:19–32` defines shortest native event count and path multiplicity for six signed integer components. The frozen Git blobs are, respectively, `46373050168d2430b6cb3952aa763f3081284632` and `300a96e3dc24bf6fff73743037a0347a8bc83176`.

P000 fixes six pairwise Enterprise-orthogonal native spatial axes and 12 signed primitive directions, whereas the A5 transfer step `e_i-e_j` has **two** nonzero signed native coordinates. It is a **composite two-event X6 realization**, not another X6 primitive axis. The comparison below is a typed combinatorial bridge between *different graph event alphabets*. It is not an equivalence between P000 geometry and an external Euclidean plane, nor a native code consumer wiring claim.

## Theorem — universal shuffle-fiber factor

Fix any integer displacement `z=(z_1,...,z_6)` with `sum_i z_i=0`, and set
`r=sum_{z_i>0} z_i=sum_{z_i<0}(-z_i)` (nonnegative integer). Let
`D(z)=prod_i |z_i|!`. Let `A(z)` be the number of shortest A5 transfer paths of length `r` from zero to `z`, and `S(z)` the number of shortest native signed-X6 paths of length `2r` from zero to `z`. Then

```text
A(z) = (r!)^2 / D(z)
S(z) = (2r)! / D(z)
S(z) = binomial(2r,r) * A(z).
```

There is a **canonical bijection**
```text
{shortest signed X6 paths to z}
  <-> {shortest A5 root-transfer paths to z}
      x {binary sign-interleavings with r positive and r negative slots}.
```
To obtain the right pair from an X6 word, retain its ordered list of positive primitive-axis labels and its ordered list of negative primitive-axis labels, pair their k-th entries into the k-th A5 transfer, and record which of the 2r event slots were positive. In the reverse direction, extract both lists from the A5 transfer word and place them into the chosen sign slots. The processes are mutually inverse, including repeated labels. The fiber is exactly `binomial(2r,r)` over **every** A5 root path, independent of `z` other than its transfer radius.

## Order-sensitive residual: adjacent-only lifts omit paths

If each A5 root step is expanded **adjacently** as either `(+e_i,-e_j)` or `(-e_j,+e_i)`, the expansion produces exactly `2^r A(z)` distinct signed-X6 words. The remaining `[binomial(2r,r)-2^r] A(z)` signed words have positive and negative primitives not balanced in every adjacent two-event block. This gap is zero at `r=0,1`, positive for every `r>=2`, and its fraction of all native signed words tends to 1 because
`2^r/binomial(2r,r) ~ sqrt(pi*r)/2^r -> 0`.
This asymptotic is a standard binomial-coefficient estimate; the exact discrete gap requires no approximation.

**Witness:** `z=(2,-2,0,0,0,0)`: A5 transfer paths `A=1`; signed X6 shortest words `S=6`; adjacent two-event transfer expansions `4`; the other `2` are `++--` and `--++` in the positive/negative slot alphabet. For `z=(3,-3,0,0,0,0)`, the corresponding values are `1,20,8`.

This formally separates positive root-transfer multiplicity from native signed path multiplicity. **A raw subtraction of one count from the other is not a universal cancellation law**: it is simply the difference of two counting populations unless the observer, path fiber, and future operation are typed. The exact scalar fiber suffices for endpoint path *totals*, but an order-sensitive future operator needs the sign-shuffle residual (and possibly more event metadata) rather than merely multiplying by the factor. It does not establish the still-unlocated LP019 alleged faulty original source line.

## Independent finite certificate

A single JavaScript BigInt checker evaluates **all 11,253 balanced integer six-vectors** with `r<=5`, no coordinate truncation (each necessarily lies in [-5,5]). It independently computes the two graph path counts using distinct zero-boundary recurrences:

```text
A(z) = sum_{i:z_i>0} sum_{j:z_j<0} A(z-e_i+e_j),  A(0)=1
S(|z|) = sum_{i:|z_i|>0} S(|z|-e_i),  S(0)=1
```

It compares both recurrences against the respective immutable-source factorial formulas, the universal shuffle factor, and the adjacent-only lower bound. **Violations: 0.** These computations are finite checks, not the proof of the all-r statement; the bijection proves all r.

| r | balanced endpoints | total A5 transfer paths | total signed X6 paths | adjacent-only lifts | omitted native paths |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 1 | 0 |
| 1 | 30 | 30 | 60 | 60 | 0 |
| 2 | 240 | 630 | 3,780 | 2,520 | 1,260 |
| 3 | 1,010 | 9,750 | 195,000 | 78,000 | 117,000 |
| 4 | 2,970 | 121,590 | 8,511,300 | 1,945,440 | 6,565,860 |
| 5 | 7,002 | 1,324,470 | 333,766,440 | 42,383,040 | 291,383,400 |

**Execution detail:** The recurrence-based BigInt computation was executed in the current JavaScript runtime; the standalone self-contained Node.js checker and its exact result JSON are preserved separately for reproduction. This unit did **not** directly import/run the original Python module; its formulas and object types were read from their exact frozen source. Unit193 already directly executed P022's simple-cubic Python producer; do not misreport that as an A5 original-native benchmark in this unit.

## Task-specific resolution and next action

The source distinction is a substantive **LP019 typed population boundary** and a reusable exact correction factor for a legitimate A5-to-X6 observer bridge. It neither invents a frozen production caller nor retroactively attaches an offending `commit:path:line`. The alleged historic LP011 wrong native signed-axis argmax and LP019 positive N-BRC subtraction locations remain **UNRESOLVED_PROVENANCE**. Continue tracing exact claimed offending historical source beyond prior 647-file Python named-reference census and 60 August documents, with actual code and typed caller, not merely keywords.

Original R063 same-object six-file benchmark (17/17,512/512) is consumed, not rerun. Native authenticated progress previously through Unit174; author Units175–194 remain distinct saved evidence pending legitimate same-lane PROGRESS. Historical Units149–152 and independent Driver review remain open. Preserve former original rejected/unknown native requests, private session identity and Research/maintenance separation.
