# Stage340-B — a genuine full-domain initial Pareto interval for the source-labelled Bernoulli/BRC observer

Date: 2026-11-01 Asia/Shanghai.
Status: PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_BERNSTEIN_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Scope, frozen sources, upstream dependency

GLOBAL_KNOWLEDGE_V1 canonical main at 13c1954f3fddaedfe5b4beaae57ce1e5ec2d1784; Enterprise Math canonical main at 9412897fb2b8e77bb30ee26391fb65edaba2a8fd; original P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. The global bootstrap/manual, ACTIVE worldview, P000 original, joint observer-preservation and heartbeat X6/time contracts, project TASK_RESEARCH routing and current portable/autonomous research protocol were read. The original P000 bytes were used because the current global projection carries an outdated canonical blob SHA. Stage338-B supplies the exact double-zero root brackets; Stage339-B established only local Pareto efficiency. **Stage329-B strict concavity of the right r1=0 branch is an explicitly inherited, unreviewed author-level theorem, not freshly independently audited here.** The current 139-leaf global localization and new entire-domain Pareto argument below are new.

This scientific model is an **auxiliary**, source-labelled three-visit Bernoulli/BRC observer. Retain all 16 labelled source-comparison terms. It is not a theorem about native P000 X6, triadic forces, a complete 3D slice, physical time or final Cell addresses. This is a continuation of the same exposed author context, not independent verification.

## Model and theorem

Let k=0,1,2,3; B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9). Define
\[
r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},\quad
b(x,y)=\frac5{32}\sum_{k=0}^{3}w_k|r_k(x,y)|,
\]
\[
D_3(a,z)=\tfrac12\sum_kw_k|B_k(a)-B_k(z)|,\quad
c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]
For two completely free source groups q1,q2 in [0,1]^2 set
P=b(q1)+b(q2), T=33/1024+c(q1)+c(q2).
Let q*=(x*,y*) be the unique root r0=r1=0 in
x* in [231083/10^6,231085/10^6], y* in [5554961/10^7,5555202/10^7].
Put beta*=b(q*). On the **right-hand** r1=0 arc from q* let q_s denote its unique point with b(q_s)=beta*+s and let phi(s)=c(q_s).

**THEOREM (full two-group global, not branch-restricted):** for every 0<=E<=E0=3/10000,
\[
\boxed{\min_{\substack{q_1,q_2\in[0,1]^2\\ b(q_1)+b(q_2)\le2\beta_*+E}}
\left[\frac{33}{1024}+c(q_1)+c(q_2)\right]
=\frac{33}{1024}+c(q_*)+\phi(E).}
\]
For E=0 the only optimizer is (q*,q*); for 0<E<=E0 the only optimizers are (q*,q_E) and (q_E,q*) in the two orders. Therefore any first *global* structural deviation from the one-group-active allocation occurs at E>3/10000. No claim is made that it occurs precisely at the larger Stage329 cusp budget epsilon_dagger (~0.002181407227).

## Lemma A: all low-budget points lie in one small rational rectangle

Set R=[29/128,15/64] x [69/128,37/64] and Q=51/12500. For all real (x,y) in [0,1]^2,
\[
b(x,y)\le Q \Longrightarrow (x,y)\in R. \tag{A}
\]

Proof via an exact **139-leaf complete closed-square cover**, generated, exported and read back by REPRO_STAGE340B.py and supplied as CERTIFICATE_STAGE340B.csv. Its 135 HIGH leaf rectangles each carry a strict rational lower bound b>Q on the entire continuous rectangle; the other 4 INNER rectangles are wholly inside R. The quadtree's maximum depth is 12 and its leaf area sum is *exactly 1*, with each child of every internal node present. The csv preserves each leaf's dyadic endpoints, a 15-subset witness mask and the actual rational bound, not sampling-based estimates.

For each nonempty S subset {0,1,2,3}, let F_S(z)=sum_{k in S} w_k B_k(z). On any interval [a,b], its cubic Bernstein coefficients are
F_S(a), F_S(a)+(b-a) F'_S(a)/3, F_S(b)-(b-a) F'_S(b)/3, F_S(b).
Their exact minimum L_S[a,b] is a **continuous** lower bound for F_S(z) on [a,b]. For any (x,y) in rectangle [a,b] x [c,d], one has
\[
b(x,y)\ge \frac5{16}
\left[\frac{4L_S[a,b]+L_S[c,d]}5
-\frac{\sum_{k\in S} w_km_k}{160}\right]. \tag{A1}
\]
Indeed the weighted residuals sum to 0, so b is twice (5/16) times their positive sum, which dominates the sum over any subset S; the factor 5/16 in (A1) is thus conservative. Every HIGH leaf has at least one S for which the right-hand side is strictly greater than Q. No unexamined continuum cells exist.

The root bracket + strict monotonicity of r3 give
\[
\beta_* <\frac{60478550833982446319}{16000000000000000000000}
,\qquad
\frac{60478550833982446319}{16000000000000000000000}+
\frac3{10000}<Q.\tag{A2}
\]
After proving global single-group b>=beta* in Lemma C, every group in a two-group budget P<=2beta*+E0 must satisfy b(q_i)<=beta*+E0<Q and therefore lie **strictly inside R**. All boundary points of R satisfy b>=Q by continuity and (A).

## Lemma B: complete tagged gradients and public-residual chambers in R

Throughout R, exact interval monotonicity yields
r2 >= r2(29/128,69/128)=24111/10485760>0;
r3 <= r3(15/64,37/64)=-1915/262144<0.
The conservation identity r0+3r1+3r2+r3=0 gives exactly
\[
b=\kappa[-r_3+(-r_0)_+ +3(-r_1)_+],\quad \kappa=5/16.\tag{B}
\]
The 16 source-tagged Bernoulli atom comparisons have k=0..3 sign strings:
(x,1/4): -+++; (x,3/4): --++; (y,1/4): ++--; (y,3/4): --sigma+.
The only changing term is sigma for k=2 on the last row, at the exact algebraic cusp
y_dagger=(1+sqrt(13))/8.
Both sides are retained, and direct symbolic expansion of all 16 terms gives
\[
c_x=-p(x),\qquad p(x)=\frac{(1-x)(189-183x)}{256}>\frac25,
\]
\[
c_y=\begin{cases}
3y(1-y)/64,&y<y_\dagger,\\
3y(18-25y)/256,&y>y_\dagger.
\end{cases}
\quad 0<c_y<1/40\tag{C}
\]
with the corresponding two positive one-sided derivatives at the cusp.

Four open (sign r0, sign r1) chambers have strict improvements, covering every real interior point:
(+, +): b=-kappa*r3, b_x<0 and c_x<0; move x upwards.
(+, -): b=-kappa*(r3+3r1), b_x=-3(1-2x)^2/4<0 and c_x<0; move x upwards.
(-, -): b=3*kappa*r2, b_y=3y(2-3y)/16>0 and c_y>0; move y downwards.
(-, +): b=-kappa*(r3+r0), b_x=3(1-2x)/4>0, b_y=-3(2y-1)/16<0. Move x and y upwards along the b=constant implicit curve; there
\[
\frac{dc}{dx}=-p+\frac{c_y b_x}{-b_y}
<-\frac25+\max(21/64,35/96)<0.
\]
The two exact ratio bounds apply on the two sides of the tagged cusp, and their one-sided integration also handles the cusp itself. All four chambers lack a constrained c-minimum at their own b budget; every chamber also has a direction decreasing b (in (-,+), move x down), so no chamber can contain a global b-minimum. Zero-labelled public boundaries are addressed next, not silently removed.

## Lemma C: both zero curves, their intersection and all budget-efficient candidates

On r0=0, implicit y=Y0(x) has
Y0'=-4(1-x)^2/(1-y)^2<0; r1(x,Y0(x)) is strictly increasing. Its unique zero is q* by the exact Stage338 root brackets. Left of q*, r1<0, b=3*kappa*r2, and
\[
\frac{dr_2}{dx}=\frac45(1-x)^2[f(x)-f(y)]<0,\quad
f(z)=\frac{z(2-3z)}{(1-z)^2}.
\]
Indeed f(x)<=f(6/25)=192/361<3/4<=f(y) on R (f decreases above 1/2). Meanwhile dc/dx=c_x+c_yY0'<0. So every point on this left zero arm is strictly dominated on approaching q*.

On the right r0=0 arm, r1>0, the adjacent (-,+) open chamber gives an arbitrarily close *same-b, lower-c* point. Enter this chamber by increasing x,y along its b=constant curve, so r0 decreases below zero. The special r0=0 arm cannot be a separate global b-minimum: b=-kappa*r3 and
\[
\frac{dr_3(x,Y_0(x))}{dx}=
\frac{12}{5}\left[x^2-\frac{y^2(1-x)^2}{(1-y)^2}\right]<0
\]
since x<y, so b **increases** for x>x* starting at q*.

On r1=0, implicit y=Y1(x) has
\[
0<Y1'=\frac{4(1-x)(1-3x)}{(1-y)(3y-1)}<5.
\]
By (C), dc/dx=c_x+c_yY1'<-2/5+(1/40)5<0, including both sides of the tagged cusp. On the left arm x<x* (r0>0), b=-kappa*r3 **decreases** toward q* (both x and y increase); the entire arm is dominated by q*. On the right arm x>x* (r0<0), b=-kappa*(r3+r0) **increases**:
\[
\frac{d[-r_3-r_0]}{dx}=
\frac{12}{5}(1-2x)-\frac35(2y-1)Y1'
>\frac{31}{125}>0. \tag{D}
\]
Thus this right r1=0 arc is the **only** possible constrained c-optimizer for budgets beta*<=B<Q close enough to beta*. Its tagged cost decreases, its public error increases, and it contains q*.

The right r1 arc exists through the required s=E0 while remaining in R: at x=15/64 its r1-zero has 565/1000<y<566/1000, and direct exact evaluation gives
kappa*[-r3(15/64,566/1000)-r0(15/64,566/1000)] > beta*+E0.
The entire short arc is inside the region of Stage329's previously verified concavity (also r1(15/64,577/1000)<0). Its strict c monotonicity and b monotonicity establish the unique q_s for all 0<=s<=E0.

The complete chamber and zero-stratum examination, compactness of the whole parameter square, and the boundary exclusion (A) imply: q* is the unique **global** minimizer of b, and for each beta*<=B<=beta*+E0 the unique **global** minimum of c subject to b<=B is q_{B-beta*}. This uses a global exhaustion of continuous regions; numerical samples are not used to infer absence of competitors. The q* global-minimum fact was also an earlier Stage307 author result; its repetition here is a needed lemma, not claimed as a fresh discovery.

## Proof of global two-group theorem

For any pair satisfying P<=2beta*+E, put s_i=b(q_i)-beta* >=0. Then s1+s2<=E<=E0. Lemmas A–C give c(q_i)>=phi(s_i), with equality only at q_{s_i}. Since phi is strictly decreasing on the right r1-zero arc, the best pair spends the entire budget, i.e. s1+s2=E. The Stage329 exact Bernstein certificate gives phi''<0 on 0<=s<=E0 (within its precise author-proved arc), so h_E(t)=phi(t)+phi(E-t) is **strictly concave** on [0,E]. A strictly concave function on a compact interval has its unique minimizers at the two endpoints 0,E when E>0 (the endpoints here have identical value by symmetry). Therefore equality requires (s1,s2)=(0,E) or (E,0); single-group uniqueness gives exactly (q*,q_E) and its swap. At E=0 both equal q*. This proves the displayed global theorem conditional only on inherited Stage329 strict concavity. QED.

## Executable evidence, exact scope and next question

Run REPRO_STAGE340B.py with Python 3 plus SymPy from this directory. Its stdlib Fraction operations generate the complete dyadic 139-leaf certificate and reread its CSV; every rational leaf witness is checked, the exact area totals 1, root brackets and endpoint inequalities pass, all 16 tagged signs and their derivative polynomials are checked symbolically, and the algebraic inequalities used for the continuous chamber/zero-arc argument are checked. Two executions produced byte-identical saved stdout, with marker
STAGE340B_GLOBAL_INITIAL_PARETO_INTERVAL_EXACT_PASS.
The CSV SHA256 is d7282c5dd51a9d47b2b7cd50d973c34040b6dec7491dd6ee18b65c6ea2f09c03.
Exact-code checks certify rational inputs; the analytical chamber/curve argument supplies real-domain quantifiers. The 98 Bernstein coefficients supporting inherited Stage329 strict concavity were not rerun this turn; this dependency remains explicitly authored and unreviewed.

Native Enterprise Math v0.6.11 returned research_authority_granted=false, CONTROL_QUOTA (5 of 5), and upstream CODE_REVIEW_REQUIRED; no active owner identity, CLAIM, Source Result, independent Driver review or Foundation admission was verified. Source publication is evidence retention only. Do not promote this auxiliary model to original P000/X6 6D discrete Cell geometry or physical conclusions.

**Stage341-B next exact unit:** extend the continuous global localization threshold beyond beta*+3/10000 toward the Stage329 algebraic cusp epsilon_dagger~0.002181407227. Either derive a continuous exclusion certificate for each newly appearing residual/tagged region and prove first global allocation through the cusp, or produce a strict *exact rational* competing pair for a smaller E, with all tagged labels and zero boundaries preserved.
