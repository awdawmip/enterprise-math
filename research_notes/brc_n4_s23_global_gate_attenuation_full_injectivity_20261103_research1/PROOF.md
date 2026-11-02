# BRC N=4 / S23: one information-preserving gate attenuation observes the full eleven-parameter cube

Date: 2026-11-03 (Asia/Shanghai). Status: **AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED**. The scientific input remains pinned at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; this author-side note continues the observer-fiber classification at `6c2368ce2c205fde60263f1671c694591c7dacb6` and the sharp four-fiber reopening at `df0f97163bcab3c86281146945f97a66b7667b5a`.

## Observer, branch provenance, and declared algebraic operation

Work in the frozen **positive stochastic six-source model** with four observed outcomes and common parameters `z=(z0,...,z10) in [0,1]^11`. Each labeled preparation `j=0,...,5` uses the *ordered* triple of causal coordinates from

```
A = (0,0,0,1,1,1)
B = (2,2,3,2,2,4)
C = (5,6,7,8,9,10)
```

and the four-outcome branch law

```
R(a,b,c) = (a, (1-a)b, (1-a)(1-b)c, (1-a)(1-b)(1-c)).
```

The six **retained source-labeled** observation rows are `P_i(z)=sum_j M_ij R(z_Aj,z_Bj,z_Cj)/20`, with the frozen mixer

```
M = [[10,10,0,0,0,0], [9,11,0,0,0,0], [0,0,20,0,0,0],
     [0,0,0,10,10,0], [0,0,0,2,18,0], [0,0,0,0,0,20]].
```

The six source labels and all four outcome positions remain distinct. For `0<lambda<1`, define the **declared algebraic future probe**

```
A_lambda(z) = (lambda*z0,...,lambda*z4,z5,...,z10),
Q_lambda(z) = P(A_lambda(z)).
```

Unlike the predecessor's constant gate *replacement* `U_beta`, this known multiplicative operation retains the original upstream gate values in its attenuated coordinates. It is a candidate observer-side intervention in the frozen model; it is not an asserted native Heartbeat evolution or physical experimental ability.

## Theorem 1: a single probe reconstructs every original eleven-parameter state

**For every real `0<lambda<1` and every `z in [0,1]^11`, the six labeled four-outcome rows `Q_lambda(z)` uniquely determine all eleven original coordinates.** In particular, the previously classified 32 boundary-degeneracy signatures, including all points of maximal nine-dimensional original-observation fibers, are distinguished by this one probe.

**Exact constructive inverse.** Write `p=Q_lambda(z)`. The mixer is invertible (`det(M/20)=1/50`), and the six raw branch rows are recovered exactly as

```
r0 = 11*p0 - 10*p1;     r1 = 10*p1 - 9*p0;
r2 = p2;                 r3 = (9*p3 - 5*p4)/4;
r4 = (5*p4 - p3)/4;      r5 = p5.
```

For each `j`, put `a=rj[0]`, `b=rj[1]`, `c=rj[2]`. Because every first and second gate of the probed row lies in `[0,lambda]`, `1-a >= 1-lambda>0` and `1-a-b=(1-a)(1-beta_j) >= (1-lambda)^2>0`, with `beta_j` the probed second gate. Hence the ordered triple is inverted by

```
z[A_j] = a/lambda,
z[B_j] = b/(lambda*(1-a)),
z[C_j] = c/(1-a-b).
```

The six raw rows cover every original index `0,...,10`; coordinates that occur in more than one row agree because of the shared parameters. No zero denominator occurs even if an original gate equals 1. This proves a globally defined exact inverse on the observed image. QED.

## Theorem 2: explicit uniform bi-Lipschitz recovery on the full real cube

Put `epsilon=||z-w||_infinity` and define the source-retaining total-variation observer distance

```
d_lambda(z,w) = max_{0<=i<=5} TV(Q_lambda(z)_i,Q_lambda(w)_i),
TV(p,q)=sum_k |p_k-q_k|/2.
```

For every real `0<lambda<1` and all `z,w in [0,1]^11`:

```
 ( (1-lambda) * min(lambda,1-lambda) / 21 ) * epsilon
       <= d_lambda(z,w) <= (1+2*lambda) * epsilon.                 (1)
```

In particular, the single globally fixed probe `lambda=1/2` satisfies

```
                 epsilon/84 <= d_(1/2)(z,w) <= 2*epsilon.       (2)
```

The lower coefficient in (1) is largest, **within this displayed elementary certification**, at `lambda=1/2`, where it equals `1/84`. No claim of the globally sharp observer condition number is made.

**Proof.** Let `rho` be the maximum TV distance between matching raw rows. The displayed source unmixing is linear; convexity and the triangle inequality for TV imply `rho <= 21*d_lambda`, because the maximum absolute row-sum of the inverse mixer is `max(21,19,1,14/4,6/4,1)=21`.

Use the following elementary **binary conditional-TV lemma**. For two probability vectors which split an event of masses `s,s'` into a binary conditional choice with probabilities `t,t'`, and retain the complement as a distinct outcome, their total variation is at least `min(s,s')*|t-t'|`. To see this, aggregate all outcomes outside the event into one category; for `s<=s'` and `t>=t'`, the event's `no` category differs by `s(t-t')+(s'-s)(1-t')` in absolute value. For `t<=t'` use the `yes` category; the case `s>=s'` follows by interchanging vectors. Aggregation can only decrease total variation.

Apply this lemma to the raw branch rows. For their first gates `a=lambda*z_A`, TV bounds `|a-a'|`, hence `|z_A-w_A| <= rho/lambda`. Conditional on not taking the first branch, mass is at least `1-lambda`, so for the second gates `b=lambda*z_B`, `|z_B-w_B| <= rho/[lambda*(1-lambda)]`. Conditional on taking neither first nor second branches, mass is at least `(1-lambda)^2`, hence for the third gates `c=z_C`, `|z_C-w_C| <= rho/(1-lambda)^2`. Since the ordered source triples cover all indices, their largest bound implies

```
epsilon <= 21*d_lambda * max(1/[lambda*(1-lambda)], 1/(1-lambda)^2).
```

This rearranges to the lower bound in (1). For the upper bound, couple the three ordered Bernoulli branch decisions using shared independent uniform variables. A mismatch in the final categorical outcome requires a mismatch at one of the three decisions, with probability at most `|delta a|+|delta b|+|delta c| <= (1+2*lambda)*epsilon`. Total variation is bounded by any coupling's mismatch probability; the source mixer has nonnegative row weights summing to one. This gives the upper bound in (1).

Finally, the lower coefficient is `(lambda*(1-lambda))/21` on `lambda<=1/2` and `(1-lambda)^2/21` on `lambda>=1/2`; its maximum is `1/84` at `1/2`. QED.

## Theorem 3: open attenuation is necessary for this probe family

Both excluded endpoints lose original parameters somewhere on the full cube. At `lambda=0`, any two original states differing only in `z0` have identical probed output, since all first five coordinates are replaced by zero. At `lambda=1`, the probe is the original observation; for `z0=z1=1` it is constant on a nine-dimensional observer fiber. Thus this one-parameter family is globally injective **exactly when** `0<lambda<1`.

## Reusable BRC observer/future-operation consequence

For **this declared one-probe future observer** all original eleven parameters are recoverable. Any state quotient claiming to preserve both the current six-source observation `P(z)` and the allowed future query `Q_lambda(z)` must distinguish all original states: if two states are quotient-equal, their `Q_lambda` results must agree; Theorem 1 then forces `z=w`. Hence the original single-observation representative map from the fiber-classification theorem is sufficient for current-risk evaluation but does not define a state quotient safe for this future probe. This is an exact information-preservation certificate for six labeled positive-probability branches, not a statement about signed/complex BRC phases or native physical evolution.

## Finite verification and precise remaining question

`VERIFY.py` implements `P`, `A_lambda`, exact inverse and TV using Python standard-library `Fraction` with exact rational arithmetic. It executed exact recovery for **2048** binary eleven-coordinate corners, **160** sampled rational interior points at `lambda=1/2`, **320** further sample/lambda combinations, and **480** exact source-TV inequality pairs, plus noninjective endpoint witnesses. The full-real theorems above are proved analytically; these finite checks are reproducibility and consistency tests.

**Next scientific unit:** With the *new* observer horizon restricted to two-stage algebraic queries, compare the single multiplicative `A_(1/2)` probe to **two constant-replacement probes** which open the root (`z0,z1`) and then all root/middle gates (`z0,...,z4`) while leaving downstream parameters fixed. Determine the minimum number of replacements needed to recover every original state, with explicit inverses and (if possible) sharp stability constants; distinguish overwrite operations from information-preserving attenuations. A separate direction is to sharpen the conservative `84` inverse-Lipschitz coefficient for the actual six-source shared-parameter manifold.
