# R277 — Prime-uniform crossed-Port pole depth and complete unit-residue controllability

Date: 2026-11-18. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECK / NOT_REVIEWED.
Lineage: R275–R276 in branch `portable/r1-r275-shared-port-cycle-20261118-1600`, frozen scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; native WBRC-T30/T31/T32 labeled visible-Port positive rational interface.

## Theorem: every p-adic unit leading residue at arbitrarily deep pole order

For **every prime p**, integers `t,h>=1`, and positive integer `c` with `p∤c`, put

```
P=p^t,  M=1+c*p^h,  u=P/[M(1+P)].
W=[[0,1/4,1/4],
   [2/(1+P),0,u],
   [2/(1+P),u,0]].
```

All entries are nonnegative rational numbers and every row sum is strictly below 1, so `W` is a legal strictly stable three-visible-Port BRC context. Its hub star `S_00=(I-W)^(-1)[0,0]` satisfies the exact identities

```
D=det(I-W)=P(M-1)[M+P(M+1)]/[M^2(1+P)^2],
S_00=(1-u^2)/D,
v_p(D)=t+h,                v_p(S_00)=-(t+h),
p^(t+h)*S_00 == c^(-1) (mod p).
```

Consequently, **for any desired pole depth N>=2 and any nonzero residue R in F_p**, set `t=1, h=N-1` and choose a positive integer `c` representing `R^(-1) mod p`. Then the same three-Port positive rational construction has pole depth N and normalized hub residue exactly R. Every one of the `p-1` unit residues is attained, keeping port labels and all rational edge weights explicit.

Moreover, for fixed p,t,c, as h grows the two cross-edge weights `u` approach zero in the ordinary real metric while the p-adic pole depth `t+h` tends to infinity. Thus the large p-adic cancellation is a property of arithmetic precision, not a real-magnitude instability.

## Complete proof

Schur/cycle-cover expansion of the actual labeled graph gives
`D=P/(1+P)-u/(1+P)-u²`.
Substitute `u=P/[M(1+P)]` and collect the numerator:

```
M²(1+P)² D
 = P[M²(1+P)-M-P]
 = P(M-1)[M+P(M+1)].
```

Because `M=1+c p^h`, `p∤c` and `h>=1`, the numbers M, `1+P`, and `M+P(M+1)` are all p-adic units. Furthermore `v_p(P)=t` and `v_p(M-1)=h`; hence `v_p(D)=t+h`. The (0,0) inverse cofactor equals `1-u²`, which is also a p-adic unit because `v_p(u)=t`. This proves the pole order.

For its normalized residue, divide by `P(M-1)=c p^(t+h)`:

```
p^(t+h) S_00
 = (1-u²) M² (1+P)² / [c (M+P(M+1))]
 == c^(-1) (mod p).
```

For row-sum stability: the hub row sum is 1/2; the other two row sums are `[2+P/M]/(1+P)`. They are strictly below 1 exactly when `P(M-1)>M`. Since `P>=2`, `M>=3`, we have `P(M-1)>=2(M-1)>M`. Thus strict stability holds even for p=2. Finally `u<P/M`, and M grows unboundedly with h, proving the real-smallness claim.

This is a uniform prime-level extension of R276 with a new surjectivity statement for the **leading normalized p-adic residue**. It provides an explicit missing residual coordinate: pole depth alone does not determine the normalized star observer; every unit residue can occur at the same depth on the same three-label port graph.

## Finite exact checks / source status

`R277_prime_unit_residue_checker.py` uses only Python stdlib `fractions.Fraction`. It tests every `p ∈ {2,3,5,7,11,13,17}`, `1<=t,h<=4`, and `c=1,...,p-1`: **816 exact cases**. For every (p,t,h) it checks that all nonzero F_p residues occur, the determinant factorization holds, each row is subunit, the pole order is t+h, and the normalized residue is c^{-1}. The complete bounded summary is `R277_verification.json`, reproducible by invoking the code. The unbounded theorem follows from the proof, not extrapolation.

Role status: independently authored and computed, not independently reviewed; no formal CLAIM, Result, or Foundation promotion is inferred from the GitHub research branch.

## Next

Classify how many additional labeled-Port entries or mixed-cycle coordinates must be retained to predict these freely varying normalized residues after each operation in a *specified* finite sequence of permitted Port additions; seek a sharp minimal future-observer signature. The R269 auxiliary-source-to-native BRC-Port mapping remains a separate open bridge.
