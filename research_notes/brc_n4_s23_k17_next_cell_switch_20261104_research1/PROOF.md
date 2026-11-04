# BRC N=4 / S23: K=17 on the next cost cell [1/8,1/7)

Date: 2026-11-04. Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Author-side analytic proof and exact rational computation; independently UNREVIEWED / NOT_ADMITTED. Continues the 0<s<1/8 phase classification from 9c03c592177d106b8e89f448536cd120229d7acc (same PR #1765).

## Scoped model and provenance-preserving observer

Let alpha=11/21, beta=10/21. Source-labelled ternary experiment T has P=(alpha*s,1-s,beta*s), Q=(beta*s,1-s,alpha*s), cost 2-s. B records whether the first T label occurred: P_B=(alpha*s,1-alpha*s), Q_B=(beta*s,1-beta*s), cost 1. The ternary source labels remain in T. For nonnegative integers (m,n) with m*(2-s)+n<=17, C_mix(m,n;s) is the Chernoff information of the product experiment evaluated at ONE COMMON exponent t in [0,1]. Put CT=C_mix(1,0;s), CB=C_mix(0,1;s), and fB(t;s)=-log[(alpha*s)^t*(beta*s)^(1-t)+(1-alpha*s)^t*(1-beta*s)^(1-t)].

## Theorem 1 (global candidate reduction, all real s in [1/8,1/7))

For every real 1/8<=s<1/7, every global integer-budget maximizer for K=17 is in {(0,17),(8,2)}. The allocation (9,0) is strictly dominated by (8,2); all configurations with 1<=m<=7 are strictly dominated by pure B with 17 trials.

Proof. Since 10*(2-s)>17, m<=9. For 0<=m<=7, m*s<1, hence n_max(m)=floor(17-m*(2-s))=17-2m. For m=8, 1<=8*s<8/7<2 and n_max=2; for m=9, 1<=9*s<9/7<2 and n_max=0. For fixed m positive information makes its maximal n optimal.

Define U=s*sqrt(alpha*beta), V=sqrt((1-alpha*s)*(1-beta*s)), qB=U+V, qT=1-s+2*U. Because alpha+beta=1, the exact identity qB^2=1-s+2*U*qB holds. Thus qT-qB^2=2*U*(1-qB)>0, since 0<qB<1 by strict Cauchy-Schwarz. T is symmetric and attains its Chernoff optimum at t=1/2. Consequently CT=-log(qT)<-2log(qB)=2*fB(1/2;s)<=2*CB.

For m=1,...,7 the shared-exponent upper bound gives C_mix(m,17-2m;s)<=m*CT+(17-2m)*CB<17*CB=C_mix(0,17;s). For m=9, C_mix(9,0;s)=9*CT, whereas the admissible t=1/2 trial gives C_mix(8,2;s)>=8*CT+2*fB(1/2;s)>9*CT. Hence only the two named candidates remain. QED.

## Theorem 2 (new continuous switch: existence and rational bracket)

There exists at least one real s** satisfying

    12501/100000 < s** < 12503/100000

at which C_mix(8,2;s**)=17*CB(s**), so the two candidates tie as global K=17 maximizers. At s=12501/100000 the unique optimizer is (8,2); at s=12503/100000 it is (0,17). The mixed allocation is also uniquely best at s=1/8. This is the genuine joint-exponent Chernoff experiment, not a separated-optimization surrogate. The number of interior roots is still OPEN.

Proof. Both Chernoff maxima depend continuously on s, since their objective functions are continuous on each compact positive-s region and the exponent interval [0,1] is compact.

The exact rational interval program VERIFY.py computes CT=-log(qT) and the fixed-exponent fB(1/2)=-log(qB). To evaluate CB exactly, use H=log(alpha/beta), L=log((1-beta*s)/(1-alpha*s)), r=L/(H+L), and CB = r*log(r/(alpha*s))+(1-r)*log((1-r)/(1-alpha*s)) (optimal tilted Bernoulli KL divergence).

Using integer sqrt brackets and bounded rational atanh logarithms, the program certifies:

  at s=1/8: 8*CT+2*fB(1/2)-17*CB > 6927275/10^15 > 0;
  at s=12501/100000: 8*CT+2*fB(1/2)-17*CB > 883434/10^15 > 0;
  at s=12503/100000: 15*CB-8*CT > 2893186/10^15 > 0.

Because 8*CT+2*fB(1/2)<=C_mix(8,2;s)<=8*CT+2*CB, the first two signs establish the mixed winner, and the third establishes the pure-B winner. Theorem 1 excludes other competitors. By continuity the difference has at least one zero in the open rational interval. QED.

## Independent radical-only far-end certificate

At s=13/100, strict exact rational sqrt enclosures establish qT^8-qB^15 > 3067176223/10^15 >0. Taking logarithms implies 8*CT<15*fB(1/2)<=15*CB. Hence 17 pure B observations are uniquely optimal there. This independent certificate needs no Bernoulli Chernoff optimizer.

## Verification scope, mother question, and remaining work

VERIFY.py was run locally with Python standard-library Fraction and isqrt. Positive rational square roots are enclosed by consecutive 10^-48 grid values; each logarithm uses 34 terms of 2*atanh((x-1)/(x+1)) and a proven absolute geometric tail bound. All decisive decisions use strict rational comparisons. The proof of reduction is analytic for every real s in [1/8,1/7); computation checks exact rational endpoint inequalities only. A derivative certificate or counterexample is needed to decide whether this new crossing is unique and to finish the interval phase diagram.

The original ten-label S23 minimax mother target remains in its previously recorded open interval [1/2,2/3]. This result is a scoped Chernoff observer theorem and does not modify P000, the frozen input, native TASK claim, independent review, or project admission.
