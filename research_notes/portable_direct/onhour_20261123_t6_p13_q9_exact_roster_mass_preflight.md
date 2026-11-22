# T6 p13 valuation-one vertical order9: exact input preflight, not exclusion

Date 2026-11-23, Asia/Hong_Kong. Frozen parent `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`, source `d84bd940cfb093cdc60e569f15cad58772a51dca`. This note begins the next exact p13 unit **after** the author-level q8 five-split closure. It is **PRELIMINARY_INPUT_CENSUS / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED**, not a modular or native benchmark result.

Named 13-valuation-one atom `(q,r)`: denominator `13(13q+r)`, residue `1<=r<=12`, vertical order q, exponent cost `169q+13r-1`. A single side is an unordered multiset of these named atoms. Its vertical order is the sum of q, and original mass cap is 2331.

With `x` recording vertical order and `t` recording exponent cost, the exact multiset generating function is

```
F(x,t) = product(q=1..9,r=1..12) 1/(1 - x^q * t^(169*q+13*r-1)).
```

The total number of canonical named order9 rosters is `[x^9]F(x,1) = 1,669,720`. Retaining only original side mass at most 2331 leaves

```
sum(m=0..2331) [x^9 t^m]F(x,t) = 1,513,291.
```

Therefore **156,429** order9 named rosters exceed the actual original side budget and can be discarded *before* q0 affine work. This is a complete combinatorial roster/cost preflight, not proof of a mixed congruence obstruction.

Two different integer methods agreed:
1. In-place unbounded-knapsack bivariate DP, initialized `D[0,0]=1`, for each of the 108 named atoms update `D[k,m]+=D[k-q,m-cost]` with increasing k and m. Extract q9 sum up to 2331.
2. Independently generate all **30 partitions** of 9 into vertical orders; for each equal-q block enumerate residue multisets of size `m` from 1..12 via combinations-with-replacement, sum the exact named costs and count both all states and those at or below 2331. The two results are identical.

As a consistency check, the same DP returns full unbudgeted q8 roster size `521,235` and budget-admissible q8 roster size `519,139`, matching the earlier q8 full roster before cost pruning.

**Next executable experiment**: for `q9 (0,9)`, enumerate all 1,513,291 budget-admissible negative-side rosters (plus side has empty vertical support), using the same exact saturated 12D q0 lattice and six mixed 13-adic constraints. Optimize by streaming canonical source order; record actual completed nonoverlapping ranges, exact q0 witnesses, both side costs and independent replay status. Do **not** infer that this 1,513,291-roster population is empty under the mixed congruences. Also remaining q9 splits are (1,8),(2,7),(3,6),(4,5).

No Native CLAIM, semantic PROGRESS, independent mathematical review, post-publication checker execution or Source Result is claimed. Existing Activity author/source mismatch remains unresolved. The mother `T6=2332` is OPEN.
