# BRC three-sector backbone and compensated-star domination

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / AUXILIARY_ONLY / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`.

Stable logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`.

This unit consumes the finite 19-neutral LCM-atom reduction and the exact semigroup-domination criterion already established for the class-13 repair observer. It does not change D24 ownership, UR/JT0 theorem status, Result/review status, or LIFT/JT2.

## 1. Exact observer and sector split

Fix a target prime `p == 13 (mod24)`. For every earlier class-13 prime `q<p`, write

`ord_q(4)=2 s_q`, `c_q=v_q(1+4^{s_q})`.

For an exact 19-neutral LCM atom `L`, its compensated earlier-row signature is

`a_q(L)=-c_q` if `s_q|L`,

and

`a_q(L)=v_q(L)` otherwise.

The already-proved semigroup criterion says that a finite set of atom signatures `S` preserves repair feasibility for every residual vector iff every original atom signature is coordinatewise dominated by a nonnegative integer combination of elements of `S`.

The present unit splits the finite atom library into two provenance sectors:

`V_3={L: 3|L}`,

`V_0={L: 3 does not divide L}`.

This is not an arbitrary parity label. Since `s_13=3`, membership in `V_3` is exactly the presence of the base class-13 cancellation carrier.

## 2. Sector-backbone theorem

### Theorem 2.1 — exact two-generator sector certificate

Let `C in V_3` and `A in V_0`. Suppose

1. `a(C)<=a(L)` coordinatewise for every `L in V_3`;
2. `a(A)+a(C)<=a(L)` coordinatewise for every `L in V_0`.

Then `{A,C}` is a universal semigroup domination basis for the complete finite LCM library.

Proof. Every original atom lies in exactly one of the two sectors. Replace a `V_3` atom by one copy of `C`; hypothesis 1 weakly decreases every observed coordinate. Replace a `V_0` atom by one copy each of `A` and `C`; hypothesis 2 again weakly decreases every coordinate. Thus every original generator is dominated by a nonnegative integer combination of `{A,C}`. The exact semigroup-domination criterion gives universal feasibility preservation. QED.

If, in addition, no single original atom dominates the full library, then the minimum domination-basis cardinality is exactly two.

This statement is stronger than pairwise Pareto pruning: the witness for a `V_0` atom is the two-atom combination `A+C`, not necessarily one Pareto representative.

## 3. Arithmetic sufficient certificate

The direct inequalities in Theorem 2.1 admit a provenance-readable sufficient condition.

Call an atom `C` **pure** when every earlier coordinate is nonpositive. Equivalently, every earlier class-13 prime dividing `C` is also cancelled by `C`; there is no uncancelled denominator spill.

Let

`S_C={q<p: s_q|C}`

be the cancellation support of `C`.

A sufficient certificate for Theorem 2.1 is:

1. `C` is pure and its cancellation support contains the cancellation support of every atom in `V_3`;
2. `A` cancels every row outside `S_C` that is cancelled by some atom in `V_0`;
3. on every row in `S_C` where `a_q(A)>0`, no atom in `V_0` cancels q and `a_q(A)<=c_q`;
4. `A` has zero positive spill on dirty rows.

Proof. For `L in V_3`, if L cancels q then C also cancels q and both have value `-c_q`; if L does not cancel q, purity gives `a_q(C)<=0<=a_q(L)` unless C itself cancels q, in which case `-c_q<=a_q(L)`. Hence C dominates the entire 3-sector.

Now take `L in V_0`. If q is outside `S_C` and some `V_0` atom can cancel q, condition 2 makes A cancel q, so `(A+C)_q=-c_q<=a_q(L)`. If q lies in `S_C` and `a_q(A)<=0`, C contributes `-c_q`, so the sum is at most `-c_q`, again no larger than any atom coordinate. If `a_q(A)>0`, condition 3 says no `V_0` atom can cancel q, hence every `V_0` value is nonnegative; meanwhile `a_q(A)+a_q(C)<=c_q-c_q=0`. Dirty rows are safe by condition 4 and the absence of negative 19-neutral cancellation on those rows. Thus `A+C` dominates every 3-free atom. QED.

The key point is that a small positive denominator debt in A need not be forbidden. It may be exactly compensated by the backbone C when the affected row is structurally unavailable to the entire 3-free sector.

## 4. Pure-cover regime at p=397, 733, 1021

Exact reconstruction gives the already-observed horizons:

- `p=397`: 23 raw atoms, 20 signatures, 3 Pareto classes. One valid pair is `A=23`, `C=175305`.
- `p=733`: 79 raw atoms, 63 signatures, 3 Pareto classes. One valid pair is `A=253`, `C=10342995`.
- `p=1021`: 447 raw atoms, 288 signatures, 5 Pareto classes. One valid pair is `A=20999`, `C=3270072328185`.

At all three horizons, C is pure and dominates the whole 3-sector, while A is itself pure and `A+C` dominates the whole 3-free sector. No single atom dominates the full library, so the exact minimum cardinality is two.

For `p=1021` the factorization makes the split transparent:

`A=20999=11*23*83`

carries the q=`277,397,997` cancellation block, while

`C=3270072328185=3*5*13*29*31*59*61*71*73`

carries the complementary base-3 cancellation backbone.

This recovers the existing `A0+A4` certificate without treating its five Pareto classes as fundamental objects.

## 5. The first new boundary mechanism at p=1117

At `p=1117`, exact reconstruction gives 959 atoms, 959 distinct signatures and 5 Pareto classes. The important new phenomenon is that the previous **pure cover** mechanism fails.

For `q=1093`,

`s_1093=91=7*13`, `c_1093=2`.

The step 91 is itself 19-neutral, so q=1093 is a legitimate clean cancellation row. But any atom cancelling q=1093 contains factor 13. Since `s_13=3`, such an atom has positive q=13 denominator spill unless it also contains 3.

That attempted purification is impossible under exact class-19 neutrality:

`lcm(3,91)=273=(547-1)/2`,

and `547 == 19 (mod24)` is an earlier class-19 prime. Thus 273 is a forbidden class-19 endpoint divisor. Consequently:

**No 19-neutral pure atom can cancel q=1093 at p=1117.**

So the pure-cover theorem is genuinely insufficient from this horizon onward; the failure is structural, not a search artifact.

## 6. Compensated-star repair at p=1117

Despite that obstruction, the exact two-generator basis persists by a different mechanism.

Take

`A=1910909=7*11*13*23*83`

and

`C=4947619432543905=3*5*13*17*29*31*59*61*71*73*89`.

Their nonzero relevant signatures include

`a_13(A)=+1`, `a_1093(A)=-2`,

while

`a_13(C)=-1`, `a_1093(C)=0`.

Hence the unavoidable q=13 denominator debt carried by the q=1093 suppressor is paid exactly once by the base-3 backbone:

`a_13(A)+a_13(C)=0`.

Exact reconstruction verifies:

- C is pure;
- C dominates every atom with `3|L`;
- A+C dominates every atom with `3 not divide L`;
- no single atom dominates the whole library.

Therefore Theorem 2.1 gives a universal domination basis `{A,C}`, and the exact minimum cardinality at `p=1117` is still two.

This is a different reason from the earlier pure-cover examples. The observed size-two pattern survives even after pure covering fails because the observer permits a **compensated debt**: a positive denominator coordinate of one sector generator is cancelled by the invariant negative backbone of the other sector.

## 7. BRC interpretation

The relevant carrier is not a Boolean cancellation set. The q=1093 boundary shows why the integer denominator coordinate must survive compression:

- Boolean support would say A cancels q=1093 and miss its q=13 cost;
- a pure-cover quotient would reject q=1093 as impossible;
- the exact signed integer signature retains both `q1093=-2` and `q13=+1`;
- the shared backbone C supplies `q13=-1`, making the pair feasible.

Thus the two-generator phenomenon is an observer-level semigroup statement with provenance-preserving integer debt, not a claim that every useful atom is individually clean.

## 8. Independent falsification/regression

Paired checker:

`research_checks/check_brc_three_sector_backbone_domination_20260924.py`.

It reconstructs the finite LCM libraries from multiplicative orders and exact valuations at `p=397,733,1021,1117`, verifies the expected atom/signature/Pareto counts, verifies C-sector and A+C-sector domination against every atom, checks absence of a one-generator universal basis, and separately verifies the q=1093 / h_547 obstruction.

Current exact run:

- four horizons checked;
- 1508 total atom-sector comparisons;
- p=1117 pure atoms cancelling q=1093: 0;
- q=13 compensated debt: `+1-1=0`;
- q=1093 cancellation credit in A: `-2`;
- total failures: 0.

Finite computation is falsification/regression only. The proof is Theorem 2.1 plus the arithmetic rowwise certificate and the exact q=1093 obstruction.

## 9. Do not repeat / next

Do not infer a universal two-generator theorem merely from four exact horizons.

Do not revert to a pure-cover conjecture: p=1117 is an exact counterexample to that stronger mechanism.

If formal D24 succession remains blocked, the next nonredundant auxiliary question is structural: characterize when the base-3 sector admits a pure universal backbone C and when the complementary 3-free sector has a single compensated star A satisfying the rowwise debt condition. A useful theorem should be stated in terms of cancellation-support divisibility and forbidden class-19 endpoint hyperedges, not additional horizon census.

If the canonical lossless staging/session-rollover operation becomes live, stop this auxiliary line and return immediately to the Source-native D24 continuation path.
