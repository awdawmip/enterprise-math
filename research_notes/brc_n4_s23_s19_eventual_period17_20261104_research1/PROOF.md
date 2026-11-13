# BRC N=4 / S23: period-17 eventual integer-budget optimum at s=1/9

Date: 2026-11-04. Mathematical state: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED.

Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Source-labeled *classical* Chernoff observer only: no native BRC–Shor computation or change to P000, provenance, or the ten-label minimax mother question.

## Exact experiment and main result

Fix `s=1/9, h=1/42, v=1/21`, so `a=s(1+v)/2=11/189` and `b=s(1-v)/2=10/189`. Source-retaining T observes `P_T=(a,1-s,b)`, `Q_T=(b,1-s,a)`; coarse B observes `P_B=(a,1-a)`, `Q_B=(b,1-b)`. Their costs are `c_T=17/9`, `c_B=1`.

For X=T,B define `f_X(t)=-log(sum_y P_X(y)^t Q_X(y)^(1-t))`, `C_X=max_{0<=t<=1} f_X(t)`. The actual mixed information is `C(m,n)=max_{0<=t<=1} (m f_T(t)+n f_B(t))` **with one shared t**, subject to `17m+9n<=9K`, `m,n,K` integers, `m,n>=0`, `K>=1`.

**Theorem (new, infinite exact range).** For **every integer K>=187**, the unique global maximizer is

`(m_K,n_K)=(9 floor(K/17), K mod 17)`.

In particular, the optimum has an exact cost-block period of 17 from K=187 onward. The threshold 187 is sufficient; it is not asserted minimal.

## General lemma: rational costs and eventual endpoint winners

Let costs be `p/q` for T and 1 for B, where `p>q>=1` and `gcd(p,q)=1`. Assume (i) `f_T` attains its Chernoff maximum at t=1/2, (ii) `f_B(t)>0` for 0<t<1, and (iii) `C_B>0`. Put `E=C_T-(p/q)C_B`, `d=C_B-f_B(1/2)>=0`. Suppose

`E>0`, `C_B/q-(q-1)E-(p-1)d>0`,

and some integer `L0>=1` satisfies `q L0 E-(p-1)d>0`. Then for **all integers K>=p L0** the unique optimum is `(q floor(K/p), K mod p)`.

**Proof.** Write `K=pL+r`, `0<=r<p`, and consider the cost-exhausting candidate `A=(qL,r)`. For any feasible competitor `(m,n)`, let `u=K-(p/q)m-n>=0`. Using the same optimizer in the mixture and the fact that `C_T=f_T(1/2)`, we have

`C(m,n)<=m C_T+n C_B=K C_B+m E-u C_B`,

`C(A)>=qL C_T+r f_B(1/2)=K C_B+qL E-r d`.

Consequently

`C(A)-C(m,n)>=(qL-m)E+u C_B-rd`. (1)

When `q` does not divide `m`, coprimality and integer costs give `u>=1/q`. Feasibility bounds `m<=qL+floor(qr/p)<=qL+q-1`. Equation (1) then gives the positive lower bound `C_B/q-(q-1)E-(p-1)d`. Hence every non-multiple-of-q T count is eliminated, uniformly in K.

When `m=qj`, feasibility forces `0<=j<=L`. The optimal B count for that j is `n=K-pj`: positivity of `f_B` on (0,1) makes further B observations strictly informative. The function

`H(j)=max_{0<=t<=1} [j(q f_T(t)-p f_B(t))+K f_B(t)]`

is convex in real j, being the supremum of affine functions. Moreover

`H(L)-H(0)=C(qL,r)-K C_B>=qL E-rd>=qL0 E-(p-1)d>0`.

Convex interpolation gives `H(j)<H(L)` for every `0<=j<L`. This eliminates the remaining competitors and proves uniqueness. QED.

## Exact rational Chernoff certificate at s=1/9

Use `U=sqrt(ab)`, `V=sqrt((1-a)(1-b))`, `Z=U+V`, and `C0=-log Z=f_B(1/2)`. Define `l1=log(a/b)`, `l2=log((1-a)/(1-b))`, `Delta=l1-l2>0`, `w0=U/Z`, `D=-(U*l1+V*l2)/Z=f_B'(1/2)`. With `w(t)=a^t b^(1-t)/(a^t b^(1-t)+(1-a)^t(1-b)^(1-t))`, the exact curvature identity is

`-f_B''(t)=w(t)(1-w(t)) Delta^2`.

Here `w(t)` increases from b to a, both below 1/2; `w'(t)=w(t)(1-w(t))Delta<=Delta/4`. Put `m0=w0(1-w0)Delta^2`, `wplus=w0+Delta/1000`, `M0=wplus(1-wplus)Delta^2`. Exact interval checks establish `D>0`, `D/m0<1/250`, `D/M0<1/250`, `wplus<1/2`.

Strict concavity therefore puts the unique optimizer `t*` in `(1/2,1/2+1/250)` and bounds the curvature on that interval by `m0<=-f_B''<=M0`. The optimality gain `d=C_B-C0` satisfies

`D^2/(2M0) <= d <= D^2/(2m0)`. (2)

The lower bound follows by evaluating at `1/2+D/M0`; the upper bound follows from strong concavity. For T, source-tagged symmetry gives `C_T=-log(1-s+s sqrt(1-v^2))`. Thus (2) yields a purely rational enclosure of both `C_B` and `E=C_T-(17/9)C_B`.

The attached standard-library VERIFY.py uses `fractions.Fraction` and `math.isqrt`, outward square-root bounds on denominator `10^40`, and the exact positive log series `log x=2 sum_{j>=0} y^(2j+1)/(2j+1)` for `y=(x-1)/(x+1)`. It bounds the tail after 18 terms by `2 |y|^37/(37(1-y^2))`, with sign handled by `log x=-log(1/x)`. All theorem assertions use exact integer/rational comparison, not displayed floats.

It confirms strict open intervals

`667/10^7 < C_B < 668/10^7`,

`372/10^11 < d < 374/10^11`,

`64/10^11 < E < 67/10^11`.

And it verifies directly, with tighter original rational enclosures,

`C_B/9-8E-16d>0` and `99E-16d>0`.

Apply the general lemma with `p=17, q=9, L0=11`. Every `K>=17*11=187` is covered. QED.

## Evidence scope and next question

This is a complete analytic author-side argument for the fixed source-tagged two-observation model, including infinitely many K. The checker exercises the finite exact inequalities; the analytic lemma establishes the unbounded K quantifier. Earlier s=1/8 period-15 results remain a separate proven-in-author-notes case, not premises for the s=1/9 certificate. No native Researcher-ID/CLAIM or independent mathematical review is asserted here. The ten-label minimax mother problem retains its historical open range [1/2,2/3]. Next: certify the finite prefix 1<=K<187 and find the **minimal** eventual threshold; vary rational s to locate exact strategy changes.
