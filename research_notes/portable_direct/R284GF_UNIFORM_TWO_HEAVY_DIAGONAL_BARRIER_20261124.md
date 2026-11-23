# R284GF — Direct two-heavy diagonal obstruction for arbitrary read noise

Date: 2026-11-24 Asia/Shanghai. Author-proved / exact finite crosschecks / NOT independently reviewed. Informed portable TASK_RESEARCH; same frozen R284CO/R284FM/R284FT auxiliary four-phase binary model, P000 and ACTIVE worldview unchanged. No formal CLAIM or Result.

## 1. Result and importance

For all integers u>=1, q>=4u+1, n<=4q+8u+1, a normalized seven-pattern histogram cannot define a correct four-phase protocol if at least two types among {3,5,6} have multiplicity >=2q+2u.

This generalizes the obstructed two-heavy sector from u=1 to arbitrary u. For u=1, combining the R284GD/R284GC two-heavy necessity at n=4q+8,4q+9 with this theorem gives the same sharp capacity 4q+10 for q>=5 without using the 73-family classification or either earlier finite-prefix lifting theorem R284GB/R284FW. It is a simplification of the existing author's result, not independent Review. For u>=2 the global two-heavy necessity is not established.

## 2. A general diagonal prefix witness

Suppose two nonconstant coordinate types g,h separate the four phases into all four possible binary pairs, and both change on a publication edge i->t. Let x_g,x_h be their sizes, and R the total number of all other nonconstant columns. Constants can be ignored. Let q>=R, and set

    T_g = x_g - 2q + R - 2u,
    T_h = x_h - 2q + R - 2u.

If 1<=T_g,T_h<=q+1, every fixed write order is obstructed by a forced third-phase read. Indeed, follow the attempted order until the first of these thresholds is hit, say T_g. The number of attempted h-writes is <T_h<=q+1, hence they can all be omitted within the current q-budget. All other attempted writes succeed. There is a unique third phase j that differs from i on g alone among the two heavy types. It agrees with t on g and with i on h. Thus the successful g-writes already match j, and h can be made to match j by choosing no errors on h in either history.

For the x_g-T_g as-yet-unoverwritten g-coordinates, source history can correct up to q by omitting their last source update; comparison phase j can correct up to q-R additional distinct mismatches by omitting their last comparison update. Independently choose no initial errors on residual columns, and correct their remaining mismatches in the comparison history. There are at most R residual columns total, hence each comparison last-change group receives at most R of these errors; the q-R reserved heavy budget leaves room for them even in a shared group. All chosen masks are attainable by R284FM's exact stable product (also reconstructed in R284GE).

The physical prefix/comparison distance is at most

    max(0,x_g-T_g-2q+R) = 2u.

The two noisy readout sets intersect, so stable correctness forces a forbidden third-phase success. The other first-threshold case is symmetric. No lifting from a finite base q, no assumption that error sources can be collapsed, and no exhaustive write-order scan is used. The argument reserves actual distinct source/target omission slots and is valid for any residual pattern mix satisfying the hypotheses.

## 3. Applying the diagonal witness to all two-heavy histograms

Write n=4q+k with k<=8u+1. Choose two heavy types and offsets a,b>=2u, leaving residual mass R=k-a-b<=4u+1<=q. Use the exact adjacent no-rollback condition from R284GE,

    sum_e (N_e-q)_+ >= q+4u+1,

where N_e counts changing columns grouped by their last source edge. The source groups of changing types on edges 0,1,2,3 are respectively
{1},{3},{5,7}; {2},{6},{1,5}; {3},{4},{2,5}; {7},{6},{4,5}.

Case {3,6}: on edges 0 and 1 only one heavy type changes, and that type is alone in its group. Every other group has size <=R<=q. Therefore x_3,x_6 each >=2q+4u+1. Their sum already exceeds n; contradiction.

Case {3,5} or {5,6}: write a for the nonalternating heavy offset, b for the alternating type-5 offset. Opposite phases 0 and 2 differ in the nonalternating heavy type but not in type 5. Their total differing mass is at most 2q+k-b<=2q+6u+1<=3q+2u. By R284FM the opposite-pair graph is K_(2,2), with four distinct edge types. A separating cut using at least three vertices cannot exceed its q|U|+2u threshold. A two-vertex cut consists of one pattern type, and only the nonalternating heavy type can exceed 2q+2u. Hence a>=2u+1.

On the two edges on which only type 5 is heavy and changes, GE1 requires b+r_1>=4u+1 and b+r_2>=4u+1, with distinct residual types r_1,r_2 (types 1 and 4 if the heavy pair is {3,5}, types 2 and 7 if it is {5,6}). If b>=4u+1 then b>=2u+2. Otherwise R>=2(4u+1-b), so
    k=a+b+R >= a+8u+2-b
    => b>=a+8u+2-k >=2u+2.
Thus R<=4u-2. The diagonal thresholds in section 2 are positive and satisfy

    T_nonalternating = a+R-2u = k-b-2u <=4u-1,
    T_alternating = b+R-2u = k-a-2u <=4u.

The pair {3,5} changes together on edge 0->1, and {5,6} on edge 1->2. Their four phase projections are all distinct binary pairs. Since q>=4u+1, section 2 applies, forcing a third-phase read. This exhausts every possible heavy pair, proving the theorem.

## 4. Consequences and exact verification

For u=1, q>=5, at n=4q+8 or 4q+9 use R284GD's exact rational two-heavy necessity and the present analytic barrier. Together with the original R284FP lower bound and R284FE repeated-Gray upper construction, this proves the existing all-q sharp result in this range, without invoking R284GA, R284GB or R284FW as load-bearing proof steps. Small q=2,3,4 remain covered by their prior finite proofs. The old results remain immutable; this is an alternate simpler proof chain.

For u>=2, the theorem rules out the entire stated sector at every width n<=4q+8u+1. It does not by itself establish a global capacity. The next discriminating question is whether the exact adjacent constraints plus six stable separations force two heavy types at low width for arbitrary u and q>=4u+1; if false, examine the residual non-heavy sector.

The companion script R284GF_uniform_diagonal_barrier_checker.py imports the pinned R284GE checker and uses the original 256-cut exact prefix distance. It enumerates all two-heavy offsets at each listed width, applies old nominal/stable tests and GE1, then checks both explicit first-threshold possibilities for every residual successful-write count. Actual output:

| q,u,k | stable + nominal | GE1 survivors | threshold cut checks |
|---|---:|---:|---:|
| q in {5,6,7,10,100}, u=1,k=8 (each) | 7 | 2 | 4 |
| same q,u=1,k=9 (each) | 66 | 16 | 44 |
| 9,2,16 | 482 | 70 | 252 |
| 9,2,17 | 1512 | 224 | 1020 |
| 13,3,24 | 5273 | 588 | 3300 |
| 13,3,25 | 11406 | 1344 | 9108 |

All 13,920 exact cut checks returned distance <=2u. The general theorem follows from the explicit witness, not extrapolation.

## Sources
- R284GE exact adjacent theorem: a112519ea319ef0e0bdf10ee01d817e10fd3dcd5:research_notes/portable_direct/R284GE_EXACT_ADJACENT_ROLLBACK_CAPACITY_20261124.md
- GE checker (actual imported bytes): d64d202c1230d7b443381f6bb8025dec09ec4a65:research_notes/portable_direct/R284GE_exact_adjacent_rollback_checker.py
- R284FM: 1d1c5dd412719c7aaf016187b6493b77253cd9f9
- R284GD: 84a477be418f97d8d113c79dca27dd2ac930ffc0
- R284FP: de49ae0239abee14619a730fe6ea60614a2cde5b
The latter exact paths and frozen source chain are identified in the R284GE note. This Boolean auxiliary observer calculation preserves actual residual source groups; it is not a native X6 geometric/BRC computation and does not change P000. Formal Review, global general-u completeness and shared task acceptance remain separate.
