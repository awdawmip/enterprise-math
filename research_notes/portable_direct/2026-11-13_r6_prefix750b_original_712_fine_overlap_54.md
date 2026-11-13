# PREFIX-750B-R6 — Explicit 54-cell collision with the ORIGINAL PREFIX712 fine-grid certificate

Date: 2026-11-13 Asia/Shanghai. Researcher `EM-DIRECT-5D86C4`, Activity `RA-048376E73CBA013C20DEEAFC`.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Model: the 189-layer BRC stopped-survivor, **auxiliary** Gamma(max) two-clock optimizer, not native X6 plane/slice.

## Exact proposition

The preceding R6 lattice audit proved that the 11 published PREFIX746–749 sibling JSON files contain exactly 197 unique upper `R_ij` rectangles with side 1/384 and their transposes: **1,576 distinct original PREFIX712 /768 fine cells**. The original PREFIX711/712 verifier instead uses `D=[0,1/2]^2`, coarse rectangles `R_ij` of width 1/384 and four refined fine rectangles `F_(2i+a,2j+b)` of width 1/768.

Using the original `e0=(0,3/20)` Gamma comparator and the exact originally published monotone-mean/moment envelope, exhaustively evaluate **all 197 source-listed upper macro cells** and their 4 fine children. For all 197 the original one-block `G1` endpoint minimum is **strictly negative**, with maximum millionth floor `-102756816`. Thus none of these coarse rectangles passes PREFIX711's strict coarse acceptance.

Among their **788 upper fine children**, exactly **27** pass the old PREFIX712 two-endpoint strict `G2>0` test. Symmetry gives 27 further transposed fine children. Therefore **54 of the 1,576** /768 fine cells in the sibling rectangles were **already certified excluded by PREFIX712**. Exactly **1,522 sibling fine cells** remain outside the original PREFIX712 certificate, prior to overlap checks against PREFIX713/714/716/718 or any later sources.

This result addresses the original `/768` fine-cell membership, not numeric equality of differently scaled cell indices. It demonstrates an actual overlap that was missed by using failure of the coarse `/384` G1 bound to infer exclusion from the earlier **refined** certification mask.

## Concrete contradiction witness

One sibling rectangle is `R_(20,47)`, of physical side 1/384. Its original old-witness coarse bound is:

```
floor(1,000,000 G1_old(R_20,47)) = -113719823 < 0.
```

Yet its four original PREFIX712 fine children have the following exact rational bounds (displayed via exact millionth integer floors):

| /768 fine-child index | floor(1,000,000 G2_old) | PREFIX712 accepted? |
|---|---:|---|
| (40,94) | 2,253,597 | Yes |
| (40,95) | -2,616,132 | No |
| (41,94) | 5,318,721 | Yes |
| (41,95) | 452,325 | Yes |

The three positive children and their transposes make **six explicit prior-certified fine cells**. Because the original endpoint inequalities imply a strict comparison for every real `q>=2` on each complete closed fine rectangle, these are mathematical certificate overlaps, not sampled optimizers.

## Exhaustive original-fine overlap certificate

The complete 27 upper pairs (each with its exact microfloor) are recorded in `PREFIX750B_R6_712_FINE_CHILD_OVERLAP_RESULTS.json`. Their transposes are distinct. The exact sequence was computed using the frozen 189-row integer survivor recurrence (9,529 nonzero count positions), its Gamma(max) moment formula, and Python `fractions.Fraction`. The independently reconstructed witness numerators match the published exact SHA256 regressions:

- `797121e567e6422d342b2647cd17ff01187d5000b08bde8a954730d071bed46e`
- `814be93bb068b6a6e688e8ea5a466939a06e617b67ab585c177176f57afd57ae`

Execution completed across eight bounded local Python batches for all 197 upper rectangles; all 788 G2 exact signs and all 197 coarse G1 signs were evaluated. The companion `PREFIX750B_R6_712_FINE_CHILD_OVERLAP_CHECK.py` is a source-native, exact-dependency replay using the existing `PREFIX741_R6_INNER_STRIP_194.py` file and the already published sibling JSON; it accepts bounded index intervals, reconstructs the expected 27 accepted upper children and tests strict inequalities. The compact newly published checker itself has **not** been independently run end-to-end as a single source import after publication, while its arithmetic logic was executed through the equivalent local full-kernel reconstruction.

## Reconciliation and scope

This is a **new exact finite source-overlap result** and a falsifying instance for the historical claim that coarse G1 failure by itself makes a later /384 certificate disjoint from PREFIX712's entire accepted set. It does not invalidate the later strict Gamma inequalities: a duplicated certified exclusion still proves the inequality on its rectangle, but does not increase coverage twice.

The prior mixed-unit ledger numerator `142336/147456` and remainder `5120` remain unverified as a physical area tally. The number `1,522` is the exact sibling-only new fine-index count **relative to PREFIX712 alone**, not yet a completed union over PREFIX713–745. All work remains `AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED`.

Next task: translate the 713/714/716/718 published original /768 fine-cell lists (including 713's coarse representative expansions) into one exact set, subtract overlaps with these 1,522, and then extend the same membership audit to each PREFIX729–745 certificate and newer parallel branches before stating a corrected complete percentage.
