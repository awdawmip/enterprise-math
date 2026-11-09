# PREFIX-649-R6 — BRC采样槽位下标准化偏度与超额峰度的反向单调流

Date: 2026-11-10 (Asia/Shanghai). Research: independent TASK_RESEARCH.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Status: AUTHOR_PROVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Frozen observer and question

This work continues the **signed two-informative-direction BRC first-stop statistical observer** of PREFIX-645–648, not a new 96-port native-dynamics simulation. For two independently marked unit-rate informative clocks let Y(p,z) be the maximum first-stop time and T_q(p,z) the discrete marked-action stopping count at a model-admissible real q>=12. The carrier retains the frozen 189 survivor layers, signed branch identity and source provenance. This analysis observes the first four cumulants under the downstream sampling-slot operation q; it neither collapses the native X6 relations nor equates statistical cumulants with physical residuals.

Writing a=E[Y], b=Var[Y], c=kappa3(Y), d=kappa4(Y), PREFIX-645 established:

kappa2(T_q)=q^2*b-q*a;
kappa3(T_q)=q^3*c-3q^2*b+q*a;
kappa4(T_q)=q^4*d-6q^3*c+7q^2*b-q*a.

## Theorem 649.1 — Uniform strict monotonicity and quantitative gaps

For EVERY (p,z) in the closed rectangle
R={ |p-1/6|<=2^-29, |z-19/128|<=2^-29 }
and every model-admissible real q>=12, define
gamma1(q)=kappa3(T_q)/Var(T_q)^(3/2) (standardized signed skewness),
gamma2(q)=kappa4(T_q)/Var(T_q)^2 (excess kurtosis).

Then gamma1(q)<0 and is strictly increasing in q; gamma2(q)>0 and is strictly decreasing in q. The q->infinity limits are c/b^(3/2)<0 and d/b^2>0, respectively. For the two actual slots:
 gamma1(24)-gamma1(12) > 1/100;
 gamma2(12)-gamma2(24) > 1/200.
Both strict gaps are uniform over R.

## Proof A — Certified cumulant envelopes

At (p0,z0)=(1/6,19/128), PREFIX-645's exact 6dp Fraction containers give:
108.655674<a0<108.655675;
336.821864<b0<336.821865;
-1209.500201<c0<-1209.500200;
50374.253006<d0<50374.253007.

The inherited common-mark moment coupling from PREFIX-646, local refinement from PREFIX-647 and fourth-cumulant bound from PREFIX-648 give on segments from the center within R:
|a-a0|<=71442*delta,
|b-b0|<=29291220*delta,
|c-c0|<=14877582174*delta,
|d-d0|<=9592604213472*delta,
where delta=|p-p0|+|z-z0|<=2^-28.

Their exact rational implications (verified by the accompanying checker) are
 108<a<110; 335<b<338; -1266<c<-1153; 14638<d<86111.
For all q>=12, b-a/q>335-110/12>0.

## Proof B — Derivative identities and signs

Set t=1/q, 0<t<=1/12. The Stirling-transfer identities simplify to

gamma1(t)=(c-3*b*t+a*t^2)/(b-a*t)^(3/2),
gamma2(t)=(d-6*c*t+7*b*t^2-a*t^3)/(b-a*t)^2.

Direct differentiation gives the exact identities

-2*(b-a*t)^(5/2)*gamma1'(t)
 = 6*b^2-3*a*c-a*b*t+a^2*t^2,

(b-a*t)^3*gamma2'(t)
 = 2*a*d-6*b*c+(14*b^2-6*a*c)*t-3*a*b*t^2+a^2*t^3.

Let x=a*t/b, so 0<x<1. The first right-hand side is positive because 6*b^2-a*b*t+a^2*t^2=b^2(6-x+x^2)>0 and -3*a*c>0. The second is positive because 14*b^2*t-3*a*b*t^2+a^2*t^3=b^2*t(14-3*x+x^2)>0, with every remaining term positive (a,b,d>0,c<0).
Thus gamma1'(t)<0<gamma2'(t), which becomes the claimed opposite monotonicities in q. The gamma1 numerator is negative since c<0 and t(-3b+a*t)<0; gamma2's numerator is positive because d>14638 and a*t^3<110/12^3. Limits follow by t->0.

## Proof C — Quantitative slot gaps

For 1/24<=t<=1/12, the certified envelopes imply
-gamma1'(t)> D1/(2*338^2*19),
where D1=6*335^2+3*108*1153-110*338/12.
The denominator uses (b-a*t)^(5/2)<338^2*sqrt(338)<338^2*19. Integration yields the exact rational comparison
 D1/(2*338^2*19*24)=3131471/312571584>1/100.

Likewise discard the positive terms -6*a*c*t and a^2*t^3 in gamma2's derivative numerator, and note 14*335^2-3*110*338/12>0. Then
gamma2'(t)>D2/338^3,
D2=2*108*14638+6*335*1153+(1/24)*(14*335^2-3*110*338/12).
Integration yields
 D2/(338^3*24)=133065967/22241935872>1/200.
These verify the slot inequalities. QED.

## Reproducibility and provenance

Run the companion PREFIX649_R6_SHAPE_FLOW_CERTIFICATE.py with standard-library Python. It regenerates PREFIX649_R6_RESULTS.json and reports ALL_CHECKS_PASS; all arithmetic comparisons are exact Fraction computations. The symbolic differentiation proof is displayed here, not formal-checker certified. No 189-layer survivor recomputation or original 96-port native simulation occurred in this unit. The author result awaits independent math review and Source Result/Review admission.

Immutable source checkpoints: PREFIX-645@f11c0345bf89321aba48d90671c244bdec25d416; PREFIX-646@d64c99d8e6ea82f6c1d803df9f93b91e70eaf7b0; PREFIX-647@0dcaaf8c51a6cd38c8bc0d9183f916246e1e377c; PREFIX-648@6b53f51abe70ac29a591fa9fcd29c1308f6c98e2.

## Scientific next action

Use centered-cumulant Bernstein/score local bounds to extend the strict signs and normalized shape-flow monotonicities to wider regions; an exact sign-change witness would settle its own universal-sign candidate. Independently review the PREFIX-646 coupling and PREFIX-645 central witness before promotion. The mother objective—global maximum of the two-parameter sampled stopping-time variance—remains open.
