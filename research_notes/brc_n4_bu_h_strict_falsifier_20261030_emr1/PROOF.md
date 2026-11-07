# BRC N=4 BU full observer: exact counterexample to candidate H

Date: 2026-10-30 (Asia/Shanghai). Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED. This is an author-side portable research continuation of Draft PR #1729. It works in the inherited external strictly positive sixteen-leaf P/Q probability model with full terminal observation (T, Decision, Z_BU). The independent legality audit of inherited L0/L3 event duals and S2-to-S23 causal reduction remains outstanding; the new explicit upper-bound witness does not use those two lemmas.

## The result

At a=961/1000, b=151/1000, the old upper candidate is H=26123/2020800, whereas the new continuous lawful strategy attains, in *each* P and Q law,

\[
\boxed{e_*=\frac{\sqrt{26521161}}{15000}-\frac{413}{1250}
=0.012924666557278792\ldots < H.}
\]

Consequently, H is **strictly suboptimal** in any minimax policy class containing this explicit behavioral strategy. Conditional on the preceding author's global lower-certificate assumptions, the exact sharpened bracket is

\[
\frac{1546111}{119625000}\ \le d_2,d_{23}\ \le
\frac{\sqrt{26521161}}{15000}-\frac{413}{1250},
\]

whose width is approximately 1.86993895549e-8. The upper inequality is independently established within the complete declared finite observer model; the lower inequality imports the earlier conditional L0/L3 analysis.

## Explicit lawful policy and continuous proof

For a real continuation u, define stage-one probabilities A,B and **unnormalized surviving AV/BV masses** U,V:

\[
A=\frac{1414u+1033}{250(7-2u)},\quad
B=\frac{961-1414u}{500(7-2u)},\quad
U=(1+u)B,\quad V=B.
\]

The actual second-stage conditional probabilities are AU=u, BU=u, AV=U/A and BV=V/B=1. Set

\[
u_H=\frac{865}{2526},\qquad
u_*=\frac{\sqrt{26521161}-4091}{2828}.
\]

For **every real** u in [u_H,u_*], the strategy is legal: 0<u_H<u_*<239/638<1, hence A<=1; B>0 because u_*<961/1414; and

\[
A-U=\frac{1105+3281u+1414u^2}{500(7-2u)}>0.
\]

Thus 0<U<A<=1 and 0<V=B<=1, and all conditional stage-two rates are in [0,1]. At u=u_H the strategy becomes the old H witness A=a, B=b.

## Exact full-BU-observer signed differences

The four observation atoms are (1,Q,0), (2,Q,0), (3,P,0), (3,Q,1), where the last retains the BU source bit. The source category Q masses (AU,AV,BU,BV) are (1/6,1/3,1/4,1/4); their P masses are (1/6,1/12,1/4,1/2). Each category has four positive leaves indexed by j,l in {0,1}, with Q_leaf=Q_category/4 and P_leaf=Q_category*likelihood[category,j]/4; likelihood pairs AU:(9/10,11/10), AV:(1/4,1/4), BU:(1/5,9/5), BV:(2,2). The target stage-one rates are (a,b) and stage-two rates (AU,AV,BU,BV)=(1,0,0,0).

For candidate minus target in that atom order, exact full-leaf aggregation gives

\[
\begin{aligned}
\Delta_P&=(0,0,-h,h),\\
\Delta_Q&=\left(
\frac{2526u-865}{1000(2u-7)},
-\frac{1414u^2+4091u-1730}{2000(2u-7)},
0,h\right),\\
h&=\frac{uB}{4}=\frac{u(961-1414u)}{2000(7-2u)}.
\end{aligned}
\]

The quadratic p(u)=1414u^2+4091u-1730 increases strictly for u>=0, and its unique positive root equals u_*. For u_H<=u<=u_*, the first two Q differences are nonpositive, the third is zero and the fourth positive; the P differences have exactly one positive entry. Thus **TV_P=TV_Q=h(u)** throughout this continuous real interval, not just on a numeric grid.

At u=u_*, exact algebraic simplification gives

\[
B(u_*)=(7221-\sqrt{26521161})/15000,\qquad
h(u_*)=\sqrt{26521161}/15000-413/1250=e_*.
\]

A fully **rational** strict counterexample is u=234/625, A=976501/976750, B=269749/1953500, U=231714391/1220937500, V=B, for which exact sixteen-leaf computations under each law give

\[
TV_P=TV_Q=\frac{31560633}{2441875000}<H,\qquad
H-TV_P=\frac{56867293}{24672705000000}>0.
\]

A stronger rational near-root witness is u=18721181/50000000, for which both laws have TV=201985162574423973/15627881900000000000. The signs p(18721181/50000000)<0 and p(37442363/100000000)>0 bound the unique root. An integer-square certificate 5149.869998^2<26521161<5149.87^2 establishes the radical comparisons exactly. The companion verifier reconstructs all sixteen P/Q leaves, confirms probabilities, lawful rates, two-law TVs, and the exact radical identities using Fraction/SymPy; local execution ended PASS_BRC_N4_BU_H_STRICT_COUNTEREXAMPLE_RADICAL_UPPER_20261030.

## Scope, sources and next question

Full BU lineage and the two separate probability laws are retained: no total-only projection or likelihood collapse is used. This is an external finite BRC theorem, not a native P000 X6/three-dimensional slice/time-dynamics identification. Independent audit is still due for L0/L3 source-event legality and the complete S2-to-S23 causal reduction. No native Result, Driver review or mathematical admission is claimed.

Frozen read pins: GLOBAL_KNOWLEDGE_V1 main@d7fa790482c7dbec4c3018b234436452769e2879; Enterprise Math main@f4ca1284608113e2ec2faaa66ce6360834cb1578; inherited exact input and former H upper witness in Enterprise Math author-side commit 0f4251bb57b06d98c10142f1acf667742fe2fbd1. GitHub authenticated writer awdawmip. Native Site v0.6.11 status returned research_authority_granted=false and active native quota 5/5, so current formal owner and current native claim remain unverified.

**Next mathematical unit:** determine whether e_* is the true global minimax. At fixed u, form the exact full four-atom TV linear program in A,B,U,V,e and construct a sign-enumerated rational/algebraic Farkas dual valid for all u in [0,1], or find an exact lawful rational strategy with both TVs below e_*. A floating-point candidate was rejected after exact sixteen-leaf reconstruction exposed a violated event constraint (~1e-7), so subsequent witnesses must be tested with exact rational arithmetic.
