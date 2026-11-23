# T6 maximal-p13 q-order9 signed split (1,8): full negative length-six exact exclusion

Date: 2026-11-23, Asia/Hong_Kong. Frozen task scientific input: `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca:research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md`. This is author-executed portable mathematics, **UNREVIEWED / NOT_ADMITTED**.

## Proposition

Under the established cancellation of all higher p13 valuations, consider maximal prime 13, p13 valuation exactly one, signed q-order9 split positive q=1 and negative q-order8. Let the negative signed side contain **exactly six named vertical atoms** `(q,r)`, each representing original denominator `a=13(13q+r)` and mass `a-1`. Let the positive side contain exactly one `(1,r)`. For each original side allow exponent mass at most 2331. Retain integer name, sign, full composite denominator and multiplicity; allow lower-prime denominators in the complete shapes.

The only negative q-partitions of 8 into six positive integers are `(1,1,1,1,1,3)` and `(1,1,1,1,2,2)`. All canonical residue multisets are exhaustively enumerated. Common positive/negative named vertical atoms cancel to previously considered strictly lower q-order cases. For support-disjoint pairs, use the previously proved saturated 12-dimensional p13 q0 compensation lattice (index `13^21`) and the six *global-necessary* mixed congruences

```
for j=1,...,6:
  sum_{r=1}^{12} u_r*r^(-j)
  + sum_{(q,r) in V_positive}(13q+r)^(-j)
  - sum_{(q,r) in V_negative}(13q+r)^(-j) == 0 mod 13^j.
```

The exact rational smallest Gram–Schmidt diagonal squared is greater than `2*2331^2=10867122`. Thus every admissible q0 vector lies inside the necessary weighted Euclidean sphere of radius squared `(2331-c_positive)^2+(2331-c_negative)^2`, and a two-nearest-integers recursion per coordinate searches every possible q0 lattice element inside the sphere. All leaves are recalculated with exact integer congruences and both **original** signed exponent masses.

## Complete exact author experiment

| Negative six-atom q-partition | Negative named rosters | Raw signed pairs | Shared named-atom canceled pairs | GS nodes | In-sphere candidates | Original-budget-legal |
|---|---:|---:|---:|---:|---:|---:|
| (1,1,1,1,1,3) | 52,416 | 628,992 | 196,560 | 1,056,399 | 4 | **0** |
| (1,1,1,1,2,2) | 106,470 | 1,277,640 | 340,704 | 2,286,516 | 4 | **0** |
| **Entire negative length 6** | **158,886** | **1,906,632** | **537,264** | **3,342,915** | **8** | **0** |

These involve **1,369,368** support-disjoint pairs. All eight in-sphere witnesses were inspected with a separate same-author exact integer script. The exact original side-mass pairs are

```
(2624,5184), (5876,2453), (2775,5320), (4243,3497),
(3456,4449), (4964,2738), (1634,5408), (2326,3777).
```

None meets the two-sided cap 2331. Their complete positive and negative original vertical rosters, q0 signed 12-vectors, exact search radii, original masses, and source-order interval digests appear in the new JSON certificate.

The finite enumeration used three no-gap/no-overlap half-open intervals for pattern `111113` and six for `111122`:
```
111113: [0,10000), [10000,30000), [30000,52416)
111122: [0,20000),[20000,40000),[40000,60000),
        [60000,80000),[80000,100000),[100000,106470)
```
All intervals were executed with exact fractions/integers; no inferred result is assigned to a timed-out partial calculation. The new published compact checker is reproducible but has not separately undergone post-publication full rerun or external independent review.

## Consequences and provenance

The entire p13 q-order9 signed split (1,8) negative lengths **1 through 6** now has no legal two-sided mass candidate. The previously completed negative lengths1..4 have 492,804 raw signed pairs, length5 contributes 1,166,256 raw, and the present length6 contributes 1,906,632 raw, for **3,565,692 signed raw pairs** in these combined ranges. Neither this result nor the completed signed split (0,9) proves the full mother target.

Evidence:
- `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN6_ALL_PATTERNS_AUTHOR_EXACT_CERT_20261123_1000.json`
- `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN6_ALL_PATTERNS_EXACT_REPLAY_20261123_1000.py`
- Previous length5 report: `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split1_8_negative_length5_exact_author.md`
- Frozen original T6 taskbook `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md`.

Next smallest portable scientific unit: **negative length7** for signed p13 q-order9 split(1,8), first q-pattern (1,1,1,1,1,1,2), followed by negative length8 all q=1, with original mass budgets and six mixed congruences. Then signed order9 splits(2,7),(3,6),(4,5), smaller-prime completion, and global target.

The canonical native T6 Source separately names a maximal-p17 q14 split(7,7) full roster/cost preflight and live owner requirements. No native winning CLAIM, RUN, protected semantic PROGRESS or independent review was inferred. Existing historical Research Activity328 remains unchanged pending exact author/session attribution; this portable evidence is **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**; global T6=2332 remains **OPEN**.
