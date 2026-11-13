# R132 — Effective rational phase lifting for a primitive-coefficient S23 family

Date: 2026-11-14, Asia/Shanghai. Author-side auxiliary signed S23 mathematics. Frozen scientific source pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This continues R131's high-primitive-coefficient open frontier, with prior R128 rotation word insight.

## Setup and exact theorem

For an integer B>=1 and m>=1, put `A=B,d=1,E=1,x=0`; then `gcd(A,d,E)=1` even when B has hundreds of digits. The one-parameter observer is

`S_i^{(B)}(theta)=1[{(B+i)*theta}<{theta}], i=0,...,m-1,`

on `0<theta<1`.

Fix rational `0<alpha<1` and rational `0<=y<1`. Define the two-parameter target word

`W_i(alpha,y)=1[{y+i*alpha}<alpha]`.

Assume a positive **generic margin**

`eta=min_{0<=i<m}(dist(y+i*alpha,Z),dist(y+(i-1)*alpha,Z)) > 0`,

where `dist(v,Z)=min_{k in Z}|v-k|`. Set `M=max(1,m-1)` and choose **any positive integer** B such that

`B>max(M/(2*eta), 1/(2*min(alpha,1-alpha)))`.

Choose `k` as an integer nearest to `B*alpha-y` and let

`theta_B=(k+y)/B`.

Then `theta_B` is a rational number in (0,1), `|theta_B-alpha|<=1/(2B)`, `{B*theta_B}=y`, and

**`S_i^{(B)}(theta_B)=W_i(alpha,y)` for every i=0,...,m-1.**

This gives a constructive rational witness for *every* finite generic target word at **every sufficiently large integer B**, not merely at some subsequence. The source coefficients `B,1,1` have gcd 1, so the R131 nontrivial common-divisor quotient does not apply here.

### Proof

Nearest-integer rounding gives `|k-(B*alpha-y)|<=1/2`, hence `|theta_B-alpha|<=1/(2B)`. The strict second B inequality keeps theta_B inside (0,1). Also `B*theta_B=k+y`, so its fractional part is y.

For each i, the two potential discontinuity/decision thresholds of the strict observer, when alpha is varied with y held fixed, are exactly the integer crossings of `y+i*alpha` and `y+(i-1)*alpha`: the first changes the floor used for the left fractional part; the second is where the left fractional part equals alpha within an unchanged floor cell. Their distances to integers at the target are at least eta. Their respective changes under `alpha -> theta_B` are bounded by `i/(2B)` and `|i-1|/(2B)`, each no greater than `M/(2B)<eta`. Thus neither a fractional-part jump nor an equality crossing occurs on the connecting segment, and every strict indicator bit is unchanged.

Finally `{(B+i)*theta_B}={y+i*theta_B}` and `{theta_B}=theta_B`. Consequently the S23 word at theta_B coincides with the target W(alpha,y). QED.

### Uniform finite-word corollary

For fixed m, let `G_m` be the set of binary length-m words possessing *some* generic rational witness (alpha,y) satisfying the margin assumption. As `G_m\subseteq {0,1}^m` is finite, choosing one witness and the explicit finite threshold above for each word, then taking their maximum, proves there is a finite B_m such that for **every integer B>=B_m** the primitive family `A=B,d=E=1,x=0` realizes **every word in G_m** on `0<theta<1`. This is a lower-inclusion theorem; boundary-only words not possessing positive margins require separate exact analysis. It does not assert a minimal B_m or equality of the entire word vocabularies.

### Exact example

Take `m=6, alpha=15/52, y=28/69`. The margin is `eta=31/1794`. The constructive bound allows `B=145`; choosing the nearest k gives `theta_B=2857/10005` and the word `(0,0,0,1,0,0)`. All quantities are exact rational values.

## Executed verification

Companion `check_r132.py` uses only `fractions.Fraction`: 400 fixed-seed rational (alpha,y,m) examples with 1<=m<=8, verified at B equal to the computed threshold and at B+1, B+11, B+200 (1,600 exact checks); two further cases verified for `B=10^100`. Program output: `R132_GENERIC_PHASE_LIFT_PASS`. Largest minimal safe B seen in this finite sample was 8693. These checks validate the construction implementation; the universal statement is justified by the proof.

## Provenance and next

R132 addresses a primitive-gcd-one high-frequency special family left open by R131. The construction is direct integer/rational arithmetic and makes no native X6 Cell/Link/Port permission claim or change to P000. The next useful problem is an effective uniform bound B_m in terms of m by constructing bounded-denominator generic rational representatives of every open rotation-word cell, and characterizing whether/how cut-only words enter the single-parameter family.
