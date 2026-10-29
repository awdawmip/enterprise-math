# BRC N=4 BU: exact global minimax for the common-continuation policy family

2026-10-30, author-side analytic theorem. Scope: strictly positive external 16-leaf P/Q source model; retained terminal observer (T,Decision,Z_BU); fixed a=961/1000, b=151/1000. Status: EXACT_SYMBOLIC_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Exact claim and scope
Let F contain ALL real stochastic policies with stage-one probabilities A,B in [0,1], common second-stage AU=BU=u in [0,1], AV surviving mass U in [0,A], BV surviving mass V in [0,B]. Conditional AV and BV probabilities are U/A and V/B (zero-mass histories arbitrary). Set e=max(TV_P,TV_Q) for the FULL terminal observer.

**Theorem (without inherited L0/L3 or S2->S23 assumptions).**
min over F of e is exactly

  e* = sqrt(26521161)/15000 - 413/1250
     = 0.012924666557278792...

This is the exact minimax of F, not yet the unrestricted d2/d23 minimax. To transfer it to all admissible original causal policies requires a separately established lossless representation/reduction to F.

## Original complete source probabilities
For c=AU,AV,BU,BV, respectively, the Q source masses are 1/6,1/3,1/4,1/4. Each has four strictly positive leaves (j,k) in {0,1}², with Q(c,j,k)=q_c/4 and P(c,j,k)=q_c * likelihood(c,j)/4. Likelihood pairs: AU=(9/10,11/10); AV=(1/4,1/4); BU=(1/5,9/5); BV=(2,2). Both P,Q normalize to 1. The target stage-one probabilities are (a,b), second-stage rates (AU,AV,BU,BV)=(1,0,0,0).

The four observable atoms, with BU source-bit preserved, are 1=(1,Q,0), 2=(2,Q,0), 3=(3,P,0), 4=(3,Q,1). Let P_i and Q_i denote candidate-minus-target signed mass. Exact leaf aggregation yields

 P1=(a-A+3(b-B))/4;  Q1=(a-A+b-B)/2;
 P3=(Au-a)/6+U/12+V/2;
 Q3=(Au-a)/6+U/3+V/4;
 P4=Q4=Bu/4;
 P2=-P1-P3-P4;  Q2=-Q1-Q3-Q4.

For any observer event S subset of {1,2,3,4}, its signed difference P_S or Q_S is <= the corresponding TV. Consequently every convex combination of such events, minus mu*(B-V) for mu>=0, is <= e.

## Three *direct full-observer* Farkas certificates
Use bitmask event notation: P8={4}, P9={1,4}, P10={2,4}, P11={1,2,4}; Q9={1,4}, Q12={3,4}, Q13={1,3,4}, Q14={2,3,4}. All sums below expand identically to functions independent of A,B,U,V.

EARLY J: events (P10,P11,Q9,Q13) have weights
 [2(u²-2u+7), 2(1+4u-u²), 3-7u, u+4]/(23-2u),
 mu=7(u+4)/[4(23-2u)].
 The weights sum to 1, are nonnegative for 0<=u<=171/500, and
 e >= J(u)=(1730-2883u-1414u²)/[2000(23-2u)].

MIDDLE h: events (P8,P10,P11,Q12) have weights
 [7(1-u), 2u², 2u(2-u), u]/(7-2u),
 mu=7u/[4(7-2u)].
 All weights nonnegative for 0<=u<=1, sum to 1, and
 e >= h(u)=u(961-1414u)/[2000(7-2u)].

LATE K: events (P8,P9,Q14) have weights
 [2(2-u),2u,u]/(4+u), mu=0.
 All weights nonnegative for 0<=u<=1, sum to 1, and
 e >= K(u)=151u/[1000(4+u)].

Every event is legitimate in the stated full observer. The expressions and multipliers are **new verified algebraic dual certificates**, not an appeal to inherited author-side L0/L3.

## Global proof for every real u in [0,1]
Let u0=171/500, p(u)=1414u²+4091u-1730, and r=(sqrt(26521161)-4091)/2828. Since p'(u)=2828u+4091>0, p(u0)<0, p(239/638)>0, the sole positive root r lies in (u0,239/638). Let t=517/40000=0.012925. Integer inequality 26521161 < (5149875/1000)² proves e*<t. Exact checks give
 J(u0)=72328363/5579000000 > t;
 h(u0)=20409363/1579000000 > t.

- For 0<=u<=u0, J'(u)=(2828u²-65044u-62849)/[2000(2u-23)²]<0. Therefore e>=J(u)>=J(u0)>e*.
- For u0<=u<=r, h''(u)=6979/[125(2u-7)³]<0. Its concavity gives h(u)>=min(h(u0),h(r))=e*, using the exact polynomial identity
  h(u)-K(u)=u*p(u)/[2000(u+4)(2u-7)].
- For r<=u<=1, K'(u)=604/[1000(4+u)²]>0, so e>=K(u)>=K(r)=e*.

The intervals exhaust every real 0<=u<=1. This is not a finite grid, a floating-point LP optimum or a conditional missing-event inference.

## Matching legitimate strategy and exact TV under both laws
Set u=r and
 A=(1414u+1033)/[250(7-2u)],
 B=(961-1414u)/[500(7-2u)],
 U=(1+u)B, V=B.
From 0<r<239/638 we get A,B>0,
 1-A=3(239-638u)/[250(7-2u)]>=0,
 A-U=(1105+3281u+1414u²)/[500(7-2u)]>0,
 and 0<=V=B<=1; hence AU=BU=u, AV=U/A, BV=1 are lawful conditional probabilities. The exact signed vectors reduce to
 P=(0,0,-e*,e*),
 Q=(-e*,0,0,e*),
because p(r)=0. Thus TV_P=TV_Q=e*, attaining the lower bound.

## Evidence and limits
The accompanying VERIFY.py checks all three universal affine-event identities with symbolic algebra, the derivative/endpoint/root certificate, and two independent rational full-16-leaf P/Q observer reconstructions. Its checked output is in VERIFY_EVIDENCE.txt. Previous author-side commit 309b4d061a164c1b2c3d9fed519cbae2822d75b9 gave the same sharp *upper bound* but not this exhaustive global lower proof within F.

Unrestricted d2/d23 equality needs an independently checked identification of the original causal information sets with F, including unreachable histories, or a lawful counterexample outside F. The original L0/L3 legality and S2->S23 transfer remain unreviewed. P000 native X6 Cell, three-dimensional slice, and independent time dynamics are separate observer-fidelity obligations. Research publication is not native Result, independent review, or mathematical admission.

Frozen input: GLOBAL_KNOWLEDGE_V1 main@a67604dbe76d4dd9bab15e6574d478c461966ad2; Enterprise Math main@aa3ced8bc134e5b3ea2219b2cc26c9f8381d5d89; preceding author-side Draft PR #1729 at 309b4d061a164c1b2c3d9fed519cbae2822d75b9. Authenticated GitHub actor awdawmip; native research authority false, owner unverified.
