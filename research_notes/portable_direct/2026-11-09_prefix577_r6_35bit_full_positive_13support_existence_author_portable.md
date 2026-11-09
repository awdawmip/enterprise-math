# BRC-X6: a 35-bit denominator existence theorem for full-positive 13-minimal native controllers

2026-11-09 · AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED.

## Exact scope, predecessor and evidence status

This author-portable result reuses the frozen science pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`, unchanged original 96-port/six-action kernel with SHA-256 `d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0`, four source ports (6,7,28,29), signs (+,-,-,+), nine roots and complete signed next-port/seven-reward joint observer. Exact re-enumeration yields 38 lawful preserving deterministic action quadruples. The full 24 original labeled action coordinates are retained. The inherited explicit full-positive 13-minimal 169-bit certificate remains valid; this new result is an **existence bound**, not an explicit 35-bit witness. It is not a native D25 CM/Frobenius calculation, Source Result, Review or admitted task checkpoint.

For `X` in the 38-vertex convex hull, let `s(X)` denote the least number of distinct lawful pure strategies in any exact positive-coefficient convex representation.

## New theorem

There exists a strictly positive rational native controller `X` such that

```
s(X) = 13
X_{p,a} = N_{p,a}/D > 0 for all four source ports and all six action labels,
1 <= D <= 32,489,701,789 < 2^35.
```

The bound is for one common *unreduced* denominator; all numerators and the denominator are integers, the four row sums equal `D`, and every frozen signed observer constraint is respected.

## Exact independent 13-column basis

Take the following original deterministic native action quadruples, all found among the 38 lawful policies:

```
(0,0,2,2) (1,0,3,2) (2,2,4,4) (3,3,5,5) (4,4,0,0)
(4,4,5,5) (4,5,0,1) (5,1,1,3) (5,5,5,5)
(0,0,0,0) (0,0,1,1) (0,0,4,4) (0,1,2,3)
```

Their lexicographic indices within the 38 are `[2,8,15,21,24,28,29,31,37,0,1,3,5]`. In the original 24-row/13-column 0/1 incidence matrix, the 13x13 minor obtained from 0-based row indices `(0,1,2,3,4,5,6,7,10,12,13,14,16)` has exact **integer determinant -1** (verified independently by fraction-free Bareiss). Thus the 13 columns are linearly independent over Q. The 13 policies together cover all 24 source/action labels, hence every strictly positive convex combination has all 24 coordinates >0.

## Proof by finite grid exclusion

Set `H = C(38,12) = 2,707,475,148` and `M = H+1 = 2,707,475,149`. Fix `w_13=1`, and let the remaining twelve coefficients independently range over positive integers `1,...,M`, a grid of `M^12` points.

For any subset `S` of twelve among the 38 lawful columns, its rational linear span has dimension at most twelve. As our selected 13-column span has dimension thirteen, the subset of coefficient vectors `w` for which `sum_i w_i v_i` belongs to `span_Q(S)` is a proper rational linear subspace of Q^13, contained in a nonzero homogeneous rational hyperplane `L_S(w)=0`. The affine slice `w_13=1` cannot lie inside any such nonzero homogeneous hyperplane: otherwise its linear span would force `L_S=0`. Therefore, for each S, either there is no grid point at all on the forbidden hyperplane, or fixing eleven variable weights determines the remaining variable weight uniquely. At most `M^11` points are excluded.

Every representation with at most twelve lawful columns is contained in a twelve-column span by extension. There are at most H possible twelve-column subsets. The union of all forbidden hyperplanes removes at most `H*M^11` grid vectors. Since `M=H+1`, at least `M^12-H*M^11 = M^11>0` positive integer weight vectors avoid the union.

For any surviving vector, put `D=1+sum_{i=1}^{12}w_i <= 1+12M = 32,489,701,789` and `X=(sum_i w_i v_i)/D`. All 24 cells are positive, and the four rows sum to 1. Every selected column is a lawful policy under all nine frozen signed observations, so the mixture is lawful. Its 13-term representation proves `s(X)<=13`; an <=12-term representation would put its integer numerator in a forbidden twelve-column span, contradiction. Hence `s(X)=13`. QED.

## Quantitative corollary and reproducibility

For any `T>H`, sample `w_1,...,w_12` independently uniformly in `{1,...,T}` and fix `w_13=1`. The probability of an exact 13-minimal, full-positive strategy is at least `1-H/T`. At `T=2H+1`, this bound exceeds 1/2; `D <= 64,979,403,565` (36 bits). Exact lower-support checking is still needed to certify a *sampled concrete* strategy. Neither this corollary nor this note claims an efficient finder or an explicit 35-bit witness.

Author-portable reproducibility package contains unchanged frozen kernel, exact rational rank/checking script, independently written native enumerator and integer Bareiss minor check, and an integer counting certificate. They verify 1296 action quadruples -> 38 lawful policies; all 9 roots; rank 13; 24 positive-cell cover; determinant -1; H/M/D bounds. No floating point and no exhaustive enumeration of H hyperplanes is used; the latter is replaced by the rigorous counting argument.

## Preserved frontier and next discriminating action

D25/LIFT/JT2 original-class divided-power H0/B0, native Frobenius direction/normalization, kappa/Delta_p-R_p and native CM experiment remain separately UNFINISHED. The original UR four-file V2 bytes remain to recover under the exact 94,687-byte/SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` provenance target. No task CLAIM/session/open or formal Source checkpoint is asserted.

Next: count distinct 12-column spans intersecting the chosen 13-space and find one compact *explicit* 13-minimal native controller with exact infeasibility certificate, or apply the previously established two-source transportation tree/native-lift obstruction with the 12-edge tree-doubling/unicycle split. Preserve source pin, complete signed observers, separate author vs Source status, and past contributors.
