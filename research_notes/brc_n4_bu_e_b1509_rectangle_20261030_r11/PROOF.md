# BRC N=4 BU: an exact E-optimal post-0.150 sub-rho rectangle

Date: 2026-10-30 (Asia/Shanghai).
Status: AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_AND_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Scientific source, scope, and nonduplication

GLOBAL_KNOWLEDGE_V1 main@a3199e3491817d44a42db1f844c81799be8c4beb; original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; Enterprise Math main@ca0afb93e9b7e2278b68fc1c3441a68b695ae4ab.

This is an exact theorem ONLY within the published external, strictly positive sixteen-leaf two-law BRC N=4 model with full joint terminal observer (T,Decision,Z_BU), target F=(a,b,1,0), and all real behavioral randomized causal S2 and S23 strategies. It is not a theorem about native P000 X6, a native three-dimensional slice, independent time dynamics, or arbitrary later observers.

The original 16-leaf-to-four-atom causal reduction is inherited from research_notes/brc_n4_bu_full_causal_reduction_audit_20261029_r1t11/PROOF.md (author commit 1a4898a57e952245eeacb38be7adf109faa49f49). The two source-preserving legal observable event-TV lower bounds L0,L3 are inherited from the earlier BRC BU author results, including research_notes/brc_n4_bu_linear_splice_b3_20_20261030_r11/PROOF.md. Those dependencies remain author-side and await independent audit.

The former continuous E region has b<=3/20, the subsequent open source PR #1723 T-switch box has a>=193/200, and the H high-ratio theorem requires b/a >= rho=(sqrt(5889)-25)/329. Our box satisfies b>3/20, a<193/200, b/a<rho everywhere, and is therefore disjoint from all three predecessor regions.

## Theorem

For EVERY real pair in the closed rational rectangle

\[
\frac{9619}{10000}\le a\le\frac{9621}{10000},\qquad
\frac{15085}{100000}\le b\le\frac{15095}{100000},
\]

write

\[
\delta=\frac{1-a}{3},\quad D=b-\delta,\quad
C=\frac{7-a-21b}{4a+12b+2},\quad
E=\frac{DC}{4}
=\frac{(a+3b-1)(7-a-21b)}{12(4a+12b+2)}.
\]

Conditional on the previously published lawful full-observer event inequalities and 16-leaf causal reduction, the EXACT all-real minimax values are

\[
\boxed{d_2(a,b)=d_{23}(a,b)=E(a,b).}
\]

The previously lawful competitor branch H=b(2a-7b)/[8(a+2b)] is strictly worse, H>E, everywhere in the same box.

## Direct capacity-event inequality (derived, not assumed)

For any lawful five-variable strategy, 0<=A,B,u<=1, 0<=U<=A, 0<=V<=B, let e=max(TV_Q,TV_P), t=(A-a+3(B-b))/4, and h=Bu/4. The source-preserving signed P-vector has atom differences t at time-one stop and -h at the BU-marked last event.

A new direct bound, valid for every u in [0,1], is

\[
 e\ge\frac{Du}{4}\quad(D=b-(1-a)/3>0).
\]

If B>=D, the single observable BU atom gives e>=h=Bu/4>=Du/4. If B<D, capacity A<=1 gives t<0 with t<=(1-a+3(B-b))/4=3(B-D)/4. The measurable union (time-one stop OR BU-marked terminal arrival) has signed mass t-h<0. Consequently

\[
e\ge h-t\ge Bu/4+3(D-B)/4\ge Du/4
\]

because u<=1<3. This is a legitimate full-joint observable-event TV bound, not a bound obtained by deleting the BU source bit.

## Inherited observable duals and analytic monotonicity

The precisely scoped earlier event lower bounds are

\[
 e\ge L_0(u)=\frac{4a-14b-3au-(a+3b)u^2}{2(23-2u)}
\quad(0\le u\le3/7),
\]
\[
 e\ge L_3(u)=\frac{u[a-(a+3b)u]}{2(7-2u)}
\quad(0\le u\le1).
\]

On [0,1], the numerator of the derivative of L0 is a(2u²-46u-61)+b(6u²-138u-28), strictly negative. The numerator of the derivative of L3 is R(u)=a(2u²-14u+7)+b(6u²-42u), with R'(u)=(a+3b)(4u-14)<0. Hence L0 is decreasing and L3 has no interior minimum on any subinterval of [0,1].

## Fixed exact splice and universal continuum sign certificates

Set k=343/1000. The derivatives C_a=-(30-72b)/(4a+12b+2)^2<0 and C_b=-(72a+126)/(4a+12b+2)^2<0 yield on the full box

\[
0<k<C_{\min}=57359/153196\le C\le19135/51052<1.
\]

For G=5a²+8ab-21b²-2b-5, the identity E-delta=G/[8(2a+6b+1)] holds, and G_a>0, G_b<0 throughout the rectangle. Thus

\[
G\ge G(a_{\min},b_{\max})=595563/80000000>0,
\]

so 0<=delta<=E and D>0. The exact common-denominator symbolic identity

\[
L_0(k)-E=\frac{N_0(a,b)}{44628000(2a+6b+1)}
\]
has
\[
N_0=7566202a^2+33042212ab-12022649a+31030818b^2-92451947b+13016500.
\]

On the whole box N_{0,a}>=37588140439/5000>0 and N_{0,b}<=-256469154403/5000<0, so

\[
N_0\ge N_0(a_{\min},b_{\max})=13503997881/8000000>0.
\]

Hence L0(k)>E for every real pair in the box. Independently,

\[
L_3(k)-E=
\frac{(353a+1059b-500)(1186a+12558b-3157)}
{5412000(2a+6b+1)}.
\]

Both linear factors rise with a,b and remain strictly negative: their respective maxima are -10453/20000 and -1203193/10000. Therefore L3(k)>E. Direct exact substitution proves L3(C)=E.

Now every real u in [0,1] is covered by ONE of three intervals. For u<=k, e>=L0(u)>=L0(k)>E. For k<=u<=C, L3 has no interior minimum, hence e>=L3(u)>=min(L3(k),L3(C))=E. For C<=u<=1, e>=Du/4>=DC/4=E. This establishes a universal all-real lower bound, not a finite-grid extrapolation.

## Explicit lawful attainment under both source laws

Choose the actual S23/S2 randomized causal policy

\[
(A,B,u,U,V)=(1,D,C,D(1+C),D).
\]

All feasibility constraints hold: 0<D<b<1, 0<C<1, V=B, U=D(1+C)<2b<1=A. Full BU-bit-preserving signed observed target-minus-competitor atom differences are exactly

\[
\Delta_Q=(\delta,E-\delta,0,-E),\qquad
\Delta_P=(0,0,E,-E).
\]

Because 0<=delta<=E, BOTH complete observed P and Q total variations equal E. This upper bound matches the universal lower bound and proves the stated conditional theorem for the entire real rectangle.

## Exact strict phase discrimination

The symbolic identity

\[
E-H=\frac{(1-a)(a^2+38ab-7a+105b^2-14b)}
{24(a+2b)(2a+6b+1)}
\]

holds identically. Let T=a²+38ab-7a+105b²-14b. Both T_a=2a+38b-7 and T_b=38a+210b-14 are positive on the box, but T at the upper-right corner is -4456807/400000000<0. Thus T<0, a<1, and E<H everywhere.

New rational anchor (a,b)=(481/500,1509/10000) has

\[
C=28691/76588,\quad
E=118981577/9190560000,\quad
H=13093593/1011040000,\quad
H-E=5289809/1161502972800>0.
\]

The actually executed included VERIFY.py performs eight independent symbolic identities, continuum corner/derivative certificates, reconstructs all sixteen strictly positive P and Q leaves and full BU-labelled joint terminal observations for FIVE exact rational lawful policies (anchor and all four corners). Both law TVs equal the analytic E for every one of the five examples. Its literal stdout is VERIFY_EVIDENCE.txt, ending PASS_BRC_N4_BU_E_OPTIMAL_B1509_NEW_RECTANGLE_20261030. Exact finite tests corroborate the algebra; the proof of the real continuum relies on the inequalities and explicit legal attainment above.

## What this does NOT establish; next work

No independent mathematics reviewer, native Source Result, CLAIM, admission, or theorem/Foundation promotion has been obtained. The inherited causal reduction and two event-TV dual lemmas still require genuinely independent audit. The external model does not automatically represent P000 native six integer Cell axes, native three-dimensional slice/third coordinate, original rotation group, extra AU/source and time-four observers, or independent native physical time. P000/ACTIVE worldview unchanged.

Next: extend from this narrow box towards a=961/1000,b=151/1000 by finding exact semialgebraic sign certificates with an adaptive measurable-event splice k(a,b), or exhibit a lawful rational strategy with BOTH full 16-leaf P and Q TVs strictly below E at an outside point. Do not treat the current fixed certificate's failure as a minimax switch.