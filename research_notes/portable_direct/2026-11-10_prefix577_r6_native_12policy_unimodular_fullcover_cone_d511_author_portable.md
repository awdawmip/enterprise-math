# BRC-X6 original-native: exact full-positive 12-policy cone and D=511 counts

2026-11-10 Asia/Hong_Kong. **AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED**. This is author-side portable mathematics, not native Source CLAIM, Result, review, promotion or P000 change.

## Frozen native model / source exposure

Scientific pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Original four source ports `(6,7,28,29)` with signs `(+,-,-,+)`, six distinct labeled actions per port, full nine signed seven-variable joint-root observers, and 96 native ports. Reconstruct all `6^4=1296` deterministic 4-tuples and test every joint root: precisely 38 native lawful policies, lexicographically indexed 0..37. Let `C` be their full 24-by-38 integer labeled-action incidence matrix (four ones per column), with rank 13.

Preserved prior original-native author results, not newly credited: fixed 11-policy cone `S4=(0,1,3,6,8,12,17,28,29,30,31)` from commit `cb7c65bf9b51f2658984952d96562ef5e3950d93`; different cone `S5=(1,3,6,8,12,17,28,29,30,31,7)` and its exact union with S4 from commit `92ecb0ae95558047b93d624c367207385ed35d63`. **New current support** is their twelve-element union:

`U=(0,1,3,6,7,8,12,17,28,29,30,31)`.

For integer D>=1 let `T_U(D)` be the set of distinct original-native 24-component integer numerator vectors `b=C_U v`, with `v∈Z_{≥0}^{12}`, `sum(v)=D`, and every original 24 coordinate `b_i>0`. No relabeling, quotient, averaging or replacement of the signed native joint observer is used.

## Theorem 1: unimodular integer recovery and exact coverage condition

Direct integer row reduction gives `rank(C_U)=12`; at native row indices

`R=(0,1,2,3,4,5,6,7,10,12,13,16)`

the 12-by-12 determinant is **-1**. Consequently the source-indexed integer numerator map has an integer left inverse; it is injective on all integer coefficients and `gcd(b_0,...,b_23)=gcd(v_0,...,v_11)`. Thus `b/D` has true reduced denominator D iff `gcd(D,v_0,...,v_11)=1`.

Every native 24-cell probability is positive **if and only if** the positive-weight support includes either

`A={3,7,8,12,17,28,31}` (seven policies) **or**

`B={3,6,8,12,17,28,29,31}` (eight policies).

Proof: the six mandatory indices `M={3,8,12,17,28,31}` are forced by unique original labeled cells: source0 actions1,2,3 force 8,12,17; source1 action1 forces31; source2 actions4,5 force3,28. With M selected, the only remaining uncovered native cells are source2 action2, supported by original indices `{6,7}`, and source1 action5, supported by `{7,29}`. These impose `(6 OR 7) AND (7 OR 29)`, exactly `7 OR (6 AND 29)`. All other original 24 labeled cells are then covered. Neither model-native ports nor signed joint observation has been discarded.

Exact full-cover support polynomial, by inclusion-exclusion of A and B:

`z^7(1+z)^5 + z^8(1+z)^4 - z^9(1+z)^3 = z^7(1+z)^3(1+3z+z^2)`.

Therefore the complete histogram of 4096 supports has 40 full-cover supports, sizes 7..12 occurring `(1,6,13,13,6,1)`. This was also independently enumerated on the original 24 coordinates.

## Theorem 2: full-positive exact counting and primitive denominator

By stars-and-bars on all 12 integer weights, including each mandatory support, and inclusion-exclusion, for every integer D>=1 (binomial coefficients vanish when their upper index is below 11):

`N_U(D)=|T_U(D)|=binom(D+4,11)+binom(D+3,11)-binom(D+2,11)`.

The rank/minor proof makes this a count of **distinct original-native 24-coordinate probability vectors**, not a count of potentially overlapping presentations.

For `D=511=7×73`, exact integer evaluations yield:

```
N_U(7)   = 1
N_U(73)  = 7,510,618,206,065
N_U(511) = 15,524,805,354,188,138,314,176
P_U(511) = N_U(511)-N_U(73)-N_U(7)+N_U(1)
         = 15,524,805,346,677,520,108,110
```

Here `P_U(511)` counts precisely those vectors whose probabilities have **true reduced denominator 511**, by the integer left inverse and Möbius inversion over divisors of 511. Relative ONLY to the previously counted union of the two fixed eleven-policy cones S4 and S5, the twelve-policy cone adds exactly

```
14,881,533,578,909,331,070,464   distinct all-positive D511 vectors;
14,881,533,573,182,170,699,284   with truly irreducible D511.
```

All vectors within this U cone have explicit presentations using at most 12 lawful original-native deterministic policies. **This theorem does not establish that any one needs exactly 12 policies among all 38, nor that 9-bit 13-minimal native vectors are globally absent.**

## Exact instance and independent certificates

For U in the displayed order, `v=(1,1,1,1,1,1,1,1,1,1,1,500)` yields D511 and the original four source-by-six action numerators:

```
[ 5,  1, 1,   1, 2, 501]
[ 5,500, 1,   1, 2,   2]
[ 4,502, 2,   1, 1,   1]
[ 4,  3, 2, 500, 1,   1]
```

Every entry is positive; each row sums to 511; `gcd(511, b_0,...,b_23)=1`. Since the 12 constituent original deterministic policies individually satisfy all nine frozen signed joint-root checks, the weighted combination does too.

Two separate exact scripts were clean extracted and executed: `verify_12cone.py` rebuilds all 38 native policies, rank and determinant -1, Smith invariant factors all 1, all 4096 support masks, coverage counts, integer binomial expressions and primitive divisor correction; `verify_12cone_independent.py`, without SymPy or dependency on the first checker, reconstructs the original policy set, verifies the two minimal covers, and directly enumerates distinct original 24-coordinate vectors for D=7,8,9, respectively **1,13,89**, in agreement with the theorem. No floating point or substitute native experiment. Standalone 7-file conversation research package `BRC_X6_ORIGINAL_12_POLICY_CONE_D511_AUTHOR_PORTABLE_20261110.zip`, SHA-256 `8ae73c02bdf7ae84ded9ca8ec7fe6cd7b754accdeba20a55e3fa47e57b160ded`, is author portable and **not claimed as Source-published**.

## Remaining parent task and exact next action

Canonical D25/LIFT/JT2 remains OPEN and requires an authenticated original-class divided-power H0/B0, [X]U mod p², native Frobenius eta/kappa, lawful writer/claim and independent review. The original four-file UR V2 bundle (94687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) remains unverified, so no fake provenance/write credit is claimed.

For further independent portable BRC-X6 science: extend this original-native rank-12 U cone by one independent legal native column to a rank-13 candidate family, then discriminate D<=511: either produce a complete rational nonnegative <=12 decomposition, or an exact separating certificate proving a genuinely 13-minimal candidate. Retain exact original source/action labels and all nine signed observers; avoid duplicating Research1 J1/J2 without canonical CLAIM. This author note is NOT_ADMITTED and does not issue a session, claim or Source checkpoint.
