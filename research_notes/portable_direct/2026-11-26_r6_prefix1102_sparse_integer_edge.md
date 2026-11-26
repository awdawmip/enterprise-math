# PREFIX-1102 — One exact fallback and density-zero unresolved integer edges

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_RATIONAL_COMPUTATION / NOT_REVIEWED. Independent continuation of the existing R6 activity RA-0ABD84561C86E53067DB0322 / EM-DIRECT-780BBE / TASK_RESEARCH. Original own registration request r6-20261123-2358-session-start-own-v1 read SUCCEEDED/error=null. No new shared Task, CLAIM, Result or Review. Fresh LEASED inventory request r6-20261126-1252-owner-read-v1 was RUNNING at last read before proof preparation; no owner authority inferred.

Frozen Stage46 input unchanged: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Retain the full native signed/phase/ordered joint carrier. This note uses only its previously established exact radial observer and its certified root; integer arithmetic below concerns that observer's edge, not a new physical propagation or classical reference.

Immutable parents:
- f0476c7795f31809302dae513504a06d1e9a9e4c:research_notes/portable_direct/2026-11-26_r6_prefix1101_adaptive_precision.md
- 0919218e87c1f6a094123bb19ff315c17846b778:research_notes/portable_direct/2026-11-26_r6_prefix1096_second_order_last_negative_edge.md
- 53d572769fe8745d7c60d93b92b28b182dabfa00:research_notes/portable_direct/2026-11-26_r6_prefix1097_effective_monotone_last_negative.md
- 08f0330096daa21d866aef04ea1db0c6d4f24384:research_notes/portable_direct/2026-11-26_r6_prefix1095_certified_lower_edge.md
- e5f4fc3df56133a943b1fd5d1b9784771066b1ea:research_notes/portable_direct/2026-11-25_r6_prefix1082_exact_ct_integer_sign_triangle.md

## 1. One potentially expensive exact sign, even without a uniform margin

Use D_m(k)=L[x^m(1-x)^k], B=Beta(m+1,k+1)>0, H_m(k)=D_m(k)/(K_normalizer B), K_normalizer>0 fixed as in 1100/1101. Under the parent hypotheses, for all sufficiently large integer m the unique real last crossing k_*(m) satisfies
  k_*(m)=rho*m+c+d/m+O(m^-2),
  K_last(m)=ceil(k_*(m))-1,
and H'_m(k)>=a/m for a>0 on every fixed bounded shift window about rho*m (1096 derivative and normalization). In particular d in [9690788,9690937]/10^6 is strictly positive. The integer suffix is monotone in sign by 1097. The exact coefficient supply and polynomial absolute error oracle of 1101 are inherited, not newly executed here.

For each sufficiently large m, compute a rational interval [rho_l,rho_u] containing rho of width <=1/(8m). This uses O(log m) bits in the coefficient supply of 1101 and the strictly negative derivative bound on F of 1095 in [5/4,13/10]. The uniform rational series approximation of F can be made O(1/m) there with O(log m) terms; bisection uses rational values with certified errors. If a midpoint sign is undecidable at that precision, |F| is bounded by twice the radius and the derivative bound directly encloses the true root within O(1/m). Select the precision constants sufficiently small to ensure the stated rho width after the smooth map rho=36/t^2-1; the derivative of this map is bounded on the interval. No irrationality assumption is needed, and this is a polynomial-bit-cost construction in log m under the parent coefficient supply.

Let [c_l,c_u]=[99141009,99141012]/10^6. Since d/m+O(m^-2) tends to zero, for all sufficiently large m the interval
  I_m=[m*rho_l+c_l-1/8, m*rho_u+c_u+1/8]
contains k_*(m), with width <=3/8+3*10^-6<1. The threshold is asymptotic, not explicitly certified for finite m. Then the exact integer endpoints L_m=ceil(inf I_m)-1, U_m=ceil(sup I_m)-1 satisfy U_m-L_m<=1. If equal, the last integer is determined by the interval alone. Otherwise one integer j=U_m separates the two possibilities. D_m(j)<0 selects U_m; D_m(j)>=0 selects L_m, including exact zero. The query lies within a fixed bounded shift window and the monotonic cone. Apply the 1101 oracle with radius <= S^-3, S=m+j+2. If the interval does not certify negative or nonnegative, use the inherited exact CT sign calculation at just this one integer. The complete procedure therefore needs polynomial(log m) bit work plus at most one possibly expensive exact sign. No assertion of a polylog worst-case exact sign cost is made. All statements are eventual and conditioned on the parent proof chain.

## 2. Density-zero exceptional scales, without proving irrationality of rho

Call a scale exceptional if the preceding fast procedure needs the exact fallback. If the sign interval does not decide, |H_m(j)|<=2 S^-3. The derivative lower bound a/m between j and k_* implies
  dist(k_*(m),Z)<= (2/a)m S^-3 = O(m^-2).
Write E for the set of exceptional scales. Claim: for every fixed H>=1, sufficiently far out, any block of H+1 consecutive integer scales contains at most one E; hence E has upper natural density zero.

Proof splits on rho, with neither case assumed for the actual edge. If rho is irrational, delta_H=min_{1<=h<=H} dist(h*rho,Z)>0. For m,m+h both exceptional, choose integers j_m,j_(m+h) at distances O(m^-2) from their real crossings. Subtract the asymptotic expansions:
  k_*(m+h)-k_*(m)=h*rho - d*h/[m(m+h)] + O(m^-2).
For fixed H the remainder is uniform because the parent O constant is common and m+h>=m. Consequently dist(h*rho,Z)=O_H(m^-2), contradicting delta_H for all sufficiently large m. If rho=p/q is rational in lowest terms, the values rho*m+c mod 1 lie in a finite set. Any nonzero distance of those classes to Z is bounded below by a fixed positive constant, whereas on the classes with rho*m+c integer, dist(k_*(m),Z)=d/m+O(m^-2) >= d/(2m) for sufficiently large m. Both exceed the O(m^-2) exceptional radius eventually. Thus in the rational case E is finite. For the irrational case, at most one exceptional scale in H+1 consecutive scales yields limsup_{N->infty} |E intersect [1,N]|/N<=1/(H+1). Let H tend to infinity. This proves the density-zero result regardless of rationality. The nonzero d is essential for the rational resonant case at this precision. No equidistribution rate or Diophantine lower bound assumed. The result concerns the number of expensive exact fallback scales, not their aggregate bit cost. No proof of uniform separation at every irrational scale, and no effective overall activation threshold, yet.

## 3. A finite exact separation certificate for 15,250 step differences

From 1095 the exact t-root interval gives
  bl=(6800006737/5368709120)^2/36,
  bu=(3400003369/2684354560)^2/36.
Therefore rho is in [lo,hi]=[1/bu-1,1/bl-1], where
  lo=247847315627329219439/11560022909211350161,
  hi=991389262522916891231/46240091623245387169.
Using exact rational arithmetic, for 1<=h<=15250, no [h*lo,h*hi] contains an integer. The minimum possible distance to an integer over all such intervals is
  Delta=1752007270743434/46240091623245387169
        > 37/10^6,
attained at h=5445 (approx 3.78893555e-5). The first interval to contain an integer is h=15251, p=326982, i.e. p/h=326982/15251; this does not establish that rho equals this rational. The enumeration proves no rational with positive denominator <=15250 belongs to the certified slope interval.

Thus even without the rational/irrational case distinction, the fixed H=15250 spacing bound is quantitatively available. More explicitly if the edge expansion has error <=C/m^2 and exceptional distances <=T/m^2 for m>=m0, then two exceptions m,m+h, 1<=h<=H, would imply
  Delta <= (2T+2C+H*|d|)/m^2.
For m>=m0 and m^2>(2T+2C+H*|d|)/Delta such pairs are excluded. C,T,m0 are not computed here, so this is an explicit formula in inherited but not yet explicit constants. It is not a finite-start assertion. In particular the finite certificate alone yields eventual fallback density <=1/15251, while section 2 proves density zero non-effectively.

Executed finite exact calculation (Python 3 Fraction; no floating decision):
```python
from fractions import Fraction as F
bl=F(6800006737,5368709120)**2/36
bu=F(3400003369,2684354560)**2/36
lo=1/bu-1; hi=1/bl-1
for q in range(1,1000000):
    a=lo*q; b=hi*q; p=-(-a.numerator//a.denominator)
    if p<=b:
        break
assert (q,p)==(15251,326982)
H=q-1
best=min((min(lo*i-(lo*i).__floor__(),
              (hi*i).__ceil__()-hi*i),i) for i in range(1,H+1))
assert best==(F(1752007270743434,46240091623245387169),5445)
assert best[0]>F(37,10**6)
print(q,p,H,best)
```
Actual Python execution of equivalent loop and minimum: first q=15251, p=326982; H=15250, minimum exactly 1752007270743434/46240091623245387169 at 5445. The interval test checks both endpoints using integer ceilings. Since none of the first H intervals contains any integer, distance to the nearest integer over each interval is the smaller endpoint distance. This proves exhaustive finite coverage, no floating reference computation. No new full BRC sign oracle run or new row endpoint in this note. The previously certified 18 rows remain unchanged.

Next: implement adaptive coefficient/edge enclosure and single-fallback path; quantify finite constants C,T,m0 using 1095 derivative certificates and the exact centered-moment recurrence. Explore the exact CT zero case and c2=0 separately. Mother B_fix,odd(32), full spectral classification and global p,d remain open. Independent review pending.
