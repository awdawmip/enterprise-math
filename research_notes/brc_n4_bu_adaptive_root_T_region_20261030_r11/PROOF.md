# BRC N=4 BU: exact root-aligned TV dual and new real 2D optimum domain

2026-10-30 (Asia/Shanghai). **AUTHOR_ANALYTIC_PROOF / EXACT_CHECKED / NONBLIND / UNREVIEWED / NOT_ADMITTED**.

## Precise mathematical input and provenance

This is a theorem **only in the declared external strictly positive 16-leaf dual-law P/Q finite model**, full terminal observer O=(T,Decision,Z_BU), target F=(a,b,1,0), all real instantaneous behavioral causal S2/S23 policies. The BU source bit is preserved. The full S2-to-S23 minimax reduction, and the two lawful observable-event total-variation dual inequalities L0,L3, are AUTHOR-SIDE INHERITED assumptions pending independent audit. Their source paths respectively are research_notes/brc_n4_bu_full_causal_reduction_audit_20261029_r1t11/PROOF.md at immutable commit 1a4898a57e952245eeacb38be7adf109faa49f49 and research_notes/brc_n4_bu_linear_splice_b3_20_20261030_r11/PROOF.md in Enterprise Math main.

GLOBAL_KNOWLEDGE_V1 main@1e92ceddb8546e8edf45c0d61641fc6d53373c76, original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc (checked against P000_STARTUP projection); initial Enterprise Math scientific main@063316aba2aa706f9e890e791585a8cfab68d6bf. Verified GitHub identity awdawmip. Site v0.6.11 research_authority_granted=false; active native jobs 5/5; actual current Owner not verified. This source PR is not a native session, CLAIM, Result, review or scientific admission, and provides no native P000 six-axis X6, three-dimensional slice, rotation or independent time theorem.

## Theorem 1 — a reusable semialgebraic sufficient E phase

For real 0<a<=1 and 0<b<=1, define

\[
X=a+3b,\quad \delta=(1-a)/3,\quad D=b-\delta=(X-1)/3,\quad
C=\frac{7-a-21b}{4X+2},\quad
E=\frac{DC}{4},\quad
R=\frac{7(X-1)}{6X},
\]

\[
G=5a^2+8ab-21b^2-2b-5,\qquad
T=a^2+38ab-7a+105b^2-14b.
\]

Assume the **explicit sufficient conditions**

\[
\boxed{X>1,\ G\ge0,\ T\le0,\ 0\le R\le\min(3/7,C),\
C\le1,\ D(1+C)\le1.}
\]

Then, conditional on the precisely inherited causal reduction and event-dual legality,

\[
\boxed{d_2(a,b)=d_{23}(a,b)=E=
\frac{(a+3b-1)(7-a-21b)}{12(4a+12b+2)}}.
\]

The conditions are exact rational semialgebraic tests: R<=3/7 iff 31X<=49, and R<=C iff 7+28X-17X^2-54Xb>=0. Their sufficiency is proved, not sharp necessity.

### New aligned TV dual and exact proof

For arbitrary legal competitor continuation u in [0,1], put e=max(TV_Q,TV_P). The inherited full-BU-observer measurable-event duals state

\[
e\ge L_0(u)=\frac{4a-14b-3au-Xu^2}{2(23-2u)}
\quad(0\le u\le3/7),
\]
\[
e\ge L_3(u)=\frac{u(a-Xu)}{2(7-2u)}
\quad(0\le u\le1).
\]

The capacity-and-source-event bound e>=Du/4 is also directly derivable. Let legal first-stage A,B∈[0,1], h=Bu/4, t=(A-a+3(B-b))/4. The isolated BU-terminal observable atom gives e>=h. When B>=D this gives e>=Du/4. When B<D, capacity A<=1 gives t<=3(B-D)/4<0. The measurable union (time-one Q stop OR BU source-marked arrival) has signed difference t-h<0, hence e>=h-t>=Bu/4+3(D-B)/4>=Du/4 (because u<=1<3). This is a genuine joint-observation event bound, not a BU-erasing projection.

**Key new root-aligned identity** (exact rational-function factorization):

\[
\boxed{L_3(u)-E=
\frac{(6Xu-7X+7)((4X+2)u+a+21b-7)}
{24(2u-7)(2X+1)}.}
\]

The first factor vanishes at u=R, the second at u=C. When R<=u<=C<=1, the two numerator factors have opposite signs and the denominator is negative. Therefore **L3(u)>=E pointwise** on [R,C], without a fixed fitted splice.

The second new exact identity is

\[
\boxed{L_0(R)-E=-\frac{3T}{(2X+1)(62X+7)}.}
\]

Since T<=0, L0(R)>=E. Moreover, for 0<=u<=3/7,

\[
L_0'(u)=
\frac{a(2u^2-46u-61)+b(6u^2-138u-28)}
{2(2u-23)^2}<0.
\]

Thus every u∈[0,R] has e>=L0(u)>=L0(R)>=E. Every u∈[R,C] has e>=L3(u)>=E by exact factor signs. Every u∈[C,1] has e>=Du/4>=DC/4=E. These three intervals exhaust **all real** u∈[0,1]; no finite sampling is used to infer globality.

A lawful matching S23 and S2 behavioral strategy is

\[
(A,B,u,U,V)=(1,D,C,D(1+C),D).
\]

Feasibility follows from the displayed hypotheses: 0<=D<=b<=1, 0<=C<=1, U=D(1+C)<=1=A, V=D<=B. The full four-atom target-minus-competitor observable signed laws from the independently published 16-leaf source are

\[
\Delta_Q=(\delta,E-\delta,0,-E),\qquad
\Delta_P=(0,0,E,-E).
\]

Exact identity E−δ=G/[8(2X+1)]>=0 shows the TV for **both** full observed P and Q laws is E. This achieves the lower bound and completes the conditional all-real theorem.

## Theorem 2 — a NEW positive-area rectangle above b=0.150

For **all real pairs** in

\[
\boxed{481/500\le a\le241/250,\qquad
151/1000\le b\le1511/10000,}
\]

the hypotheses of Theorem 1 hold, hence **d2=d23=E**. This entire rectangle has b>=0.151>0.150 (beyond previously main-published E region), a<=0.964<0.965 (outside draft PR #1723's two-phase rectangle), and b>=0.151>0.15095 (outside draft PR #1726's new E rectangle). It is not a repeat of those regions.

Here is an **exact corner/derivative certificate for the continuum**, independently checked in VERIFY.py:

\[
G_a\ge2707/250>0,\quad G_b\le-63/100<0,\quad
G\ge G(481/500,1511/10000)=843019/100000000>0;
\]
\[
T_a\ge331/500>0,\quad T_b\ge27133/500>0,\quad
T\le T(241/250,1511/10000)=-6927/4000000<0.
\]

R increases with both parameters because X>1, while C decreases since
C_a=−(30−72b)/(4X+2)^2<0 and C_b=−(72a+126)/(4X+2)^2<0. The exact edge bounds are

\[
0<R\le9737/28346<3/7,\quad
R\le9737/28346<9543/25564\le C
\le2867/7660<1,
\]

and D>=83/600>0; U=D(1+C)<=2b<=3022/10000<1. This verifies all conditions uniformly over every real point in the rectangle.

At the anchor a=963/1000,b=1511/10000:

\[
R=29141/84978,\quad C=28639/76652,\quad
G=1926399/100000000>0,\quad
T=-48011/20000000<0,
\]
\[
\boxed{\mathrm{TV}_Q=\mathrm{TV}_P=d_2=d_{23}
=119224157/9198240000,}
\qquad L_0(R)-E=720165/36337110556>0.
\]

The exact phase comparison E−H=(1−a)T/[24(a+2b)(2X+1)] shows E<H throughout the new box, where H=b(2a−7b)/[8(a+2b)] is the known alternative candidate.

## Exact outgoing boundary obstruction

At the previously proposed nearby input a=961/1000,b=151/1000:

\[
G=-291/125000<0,\quad
T=-2289/250000<0,\quad
E=16491/1276000<\delta=13/1000.
\]

The *specific* capacity-saturated E-attaining policy has Q TV at least δ>E because its time-one atom has signed mass δ. Its attainment argument fails even though T remains negative and the moving L0 splice remains algebraically meaningful. This is **NOT** an unrestricted minimax lower bound or proof of an H strategy switch. Determining the true phase for G<0 is the next specific task.

## Executed verification, scope and review debts

The companion published VERIFY.py checks 15 exact symbolic identities and exact continuum box-sign certificates, reconstructs all 16 strictly positive P/Q source leaves with Python Fraction, and checks both full-joint TV laws and signed atoms for five exact legal rational policies (anchor and all four corners). Literal stdout is VERIFY_EVIDENCE.txt. Finitely many cases corroborate the formulas but do not replace the analytical all-real proof.

Independent review must derive the L0/L3 dual weights from source-observable events and independently check the S2→S23 causal map, including BU lineage at time four. Native P000 six-dimensional Cell, three-dimensional slice with a typed third component, branch interactions, and time-labelled future-operation fidelity remain distinct proof obligations. This source material is an author-side research handoff: see NEXT_TASK.md and PROVENANCE.json; no native Result, independent Driver verdict or admission.
