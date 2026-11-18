# R749SUV — Complete square-plus-two phase diagram for the named two-Port Q=+1 observer

Date: 2026-11-18 (Asia/Shanghai). Evidence status: AUTHOR_EXACT_NOT_REVIEWED. Independent portable continuation of R749SUU (#2739); no native X6 CLAIM/Result/Review.

## Frozen scientific input and exact question

Source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md`, WBRC-T30–T32. Reuses the exact *auxiliary* positive-integer named two-Port observer and its Q=+1 factorization from R749SUT/R749SUU; neither source nor P000 is modified.

Consider `M=t^2+1`, integer `t>=3`, `B=M+1=t^2+2`. In the Q=+1 sector, legal unordered factors obey
\[
2\le x\le y,\qquad n=xy\le B,\qquad n-x-y\ge1.
\]
The named matrix and score are
\[
(a,u,v,d)=(n-x-1,n-1,n-x-y,n-y-1),\quad
ad-uv=1,\quad Q=u+v-a-d=1,
\]
\[
F(n,s)=(n-1)[(n-1)^2-(n-1)s+n],\quad s=x+y,
\qquad \tau=F(n,s).
\]
Swapping the two diagonal entries or the two off-diagonal entries independently gives the other named configurations. The unordered optimizer is unique, hence there are 2 named maximizers if x=y and 4 otherwise.

## Theorem (all integer t>=3; exact unique unordered optimizer)

Apply the first matching case. Here all k,r are integers, with the stated bounds.

**Odd t:**
1. If `t=2k(k+1)+1` for `k>=1`, then `(x*,y*)=(t-2k,t+2k+2)` and `n*=t^2+2` (zero gap).
2. Else if `t=r(r+1)+1` for `r>=1`, then `(x*,y*)=(t-r,t+r+1)` and `n*=t^2+1` (unit gap).
3. Otherwise `(x*,y*)=(t,t)` and `n*=t^2` (gap two).

**Even t:**
1. If `t=r(r+1)+2` for `r>=1`, then `(x*,y*)=(t-r,t+r+1)`, `n*=t^2+2`.
2. Else if `t=3k^2+5k+2` for `k>=1` or `t=3k^2+7k+4` for `k>=0`, put `h=\sqrt{12t+1}`, an odd integer, and
\[
(x^*,y^*)=((2t+3-h)/2,(2t+3+h)/2),\quad n^*=t^2+2.
\]
3. Else if `t=2k^2` for `k>=2`, then `(x*,y*)=(t-2k+1,t+2k+1)`, `n*=t^2+1`.
4. Otherwise `(x*,y*)=(t,t)`, `n*=t^2`.

In every case the exact optimal threshold is `(n*-1)(n*-x*-1)(n*-y*-1)`. The priority order handles overlaps and is strict; no distinct unordered factors tie.

Consequently, the square-plus-two zero-gap parameters are **exactly** the odd first family and the three even quadratic families above (the second even case has two quadratic parametrizations). Their number among `3<=t<=T` is `\Theta(\sqrt T)`; among `M=t^2+1<=X` it is `\Theta(X^{1/4})`. These counts imply zero relative density within the square-plus-one M slice, while giving infinitely many zero-gap M.

## Proof

### A. All n<=t^2 are beaten or matched uniquely by the square pair

Let `S=F(t^2,2t)=(t^2-1)(t^2-t-1)^2`, attained by legal x=y=t. For any legal n<=t^2 and s>=2t, `F(n,s)` is increasing in n for fixed s in the domain `n>=s+1`, since
\[
\partial F/\partial n=3(n-1)^2-2s(n-1)+2n-1>0.
\]
It decreases strictly in s for fixed n. Thus `F(n,s)<=F(t^2,s)<=S`, with equality only at n=t^2,s=2t. If s<=2t-1, AM–GM and integrality give `n<=t(t-1)`; each positive factor in `(n-1)(n-x-1)(n-y-1)` is at most `t^2-t-1`. Hence `F(n,s)<S`. This establishes unique optimality of the square pair over n<=t^2.

### B. For n=t^2+1, only one near-square sum can beat S

Every factor pair has s>2t. If t is odd, n is 2 mod 4, x,y have opposite parity and s is odd. The smallest candidate is `s=2t+1`; at `s>=2t+3`,
\[
F(t^2+1,2t+3)-S=-4t^3-t^2+2t+1<0.
\]
If t is even, n is odd, both factors are odd and s even; the smallest candidate is `s=2t+2`. At `s>=2t+4`, the score lies strictly below S. For the candidate sums the exact equations are
\[
t\text{ odd}: x=t-r,\ y=t+r+1,\quad r(r+1)=t-1;
\]
\[
t\text{ even}: x=t-r,\ y=t+r+2,\quad (r+1)^2=2t.
\]
These are exactly the stated n=t^2+1 families. Each possible candidate strictly beats S (for even t the family has t>=8).

### C. For n=t^2+2, parity, score cutoff and modular obstructions leave only two even and one odd candidate sums

Again s>2t. Direct substitution gives
\[
F(t^2+2,2t+6)-S=-2(4t^3+4t^2+1)<0.
\]
As F is strictly decreasing in s, every n=t^2+2 candidate beating S has s<2t+6.

If t is odd, n is odd and s even: only `s=2t+2` or `2t+4` remain. For `s=2t+4`, writing x=t-r and y=t+r+4 gives `r(r+4)=4t-2`, impossible: r odd makes the left side odd, while r even makes it divisible by four, but the right side is 2 modulo four. Therefore s=2t+2 alone is possible. It yields `r(r+2)=2t-2`, necessarily even `r=2k`, hence `t=2k(k+1)+1` and the first odd family.

If t is even, n is 2 modulo four and s odd. The eligible sums are `2t+1,2t+3,2t+5`. The last would imply `r(r+5)=5t-2`, hence `r^2=3\pmod5`, impossible because 3 is a quadratic nonresidue modulo 5. The first gives `r(r+1)=t-2`, exactly the first even family. The second gives `r(r+3)=3t-2`, or `(2r+3)^2=12t+1`. The solutions with t even and r>=1 are `r=3k+1` (k>=1) or `r=3k+2` (k>=0), giving precisely the two quadratic formulas of the second even family. The reconstructed pairs are positive and legal.

### D. Strict score hierarchy resolves all simultaneous candidate families

For odd t>=3, writing `F_{c,j}=F(t^2+c,2t+j)`:
\[
F_{2,2}>F_{1,1}>S,\qquad
F_{2,2}-F_{1,1}=2t^4-4t^3+t^2-2t+1>0,
\]
\[
F_{1,1}-S=(t-1)(2t^3-2t^2-3t-1)>0.
\]
For even t>=4:
\[
F_{2,1}>F_{2,3}>S,\quad
F_{2,1}-F_{2,3}=2(t^2+1)^2>0,
\]
\[
F_{2,3}-S=3t^4-8t^3-2t^2+1>0.
\]
Whenever the n=t^2+1 family exists, t=2k^2>=8 and
\[
F_{2,3}>F_{1,2}>S,\quad
F_{2,3}-F_{1,2}=t(2t^3-4t^2-t-2)>0,
\]
\[
F_{1,2}-S=t^4-4t^3-t^2+2t+1>0.
\]
Thus the case priority is exact. Each fixed n,s yields at most one unordered factor pair by the quadratic formula. Unique optimality and the named reconstruction follow.

For the density claim, each quadratic family contributes at most O(sqrt T) t values, while the odd zero-gap family contributes Omega(sqrt T). Replacing T by sqrt X proves the square-slice statement.

## Integer algorithm and exact verification

Each case is decided using a bounded number of integer-square-root tests and O(1) integer arithmetic operations, with O(1) auxiliary integer words. Inputs have O(log t) bits; integer sqrt, multiplication and output costs are **not** claimed to have constant bit complexity. A named output needs 2 or 4 configurations.

Companion `R749SUV_SQUARE_PLUS_TWO_CERT.py` (Python stdlib, exact integers) checks:
- all admissible unordered pairs for t=3..139 (137 complete finite domains);
- independent all-x endpoint oracle for t=3..2500 (2498 domains);
- independent bounded-discriminant oracle against the closed classification for t=3..50000 (49998 domains);
- exact score and polynomial cutoffs for t=3..10000 (9998 instances);
- large-t samples up to 10^12, with values serialized as decimal strings.

All checks returned PASS. Complete infinite-domain validity is supported by the proof above, not inferred from the finite ranges. Tool/concept reuse: the WBRC positive-rational labeled Port observer is inherited, and the new root tests are integer observer calculations; no native X6 three-action dynamics or triadic-balance claim is made.

## Boundary, provenance, and next frontier

This theorem is unconditional **within the defined Q=+1 integer observer**. Transfer to all nonstandard two-Port global maxima for t>=11 uses the upstream author theorem R749SUO (`Q=+1` when M>=116) and therefore inherits its independent-review status. Neither this integer observer nor a two-entry matrix is a native X6 slice.

Next useful science: general fixed-offset `B=t^2+c`, with c>=3; identify a finite candidate-sum cutoff and local modular obstructions uniformly in c, and establish whether the bound on candidate roots is O(c^2) independent of t. Separately evaluate native triadic/temporal event embeddings without conflating an observer optimization with a native result.
