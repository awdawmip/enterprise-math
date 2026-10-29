# BU N=4: exact positive-area capacity tail with rational stitch 9/25

Date: 2026-10-29. Status: AUTHOR_SIDE / SHARED_EXPOSED_CONTEXT / CONDITIONAL_ANALYTIC_PROOF / UNREVIEWED / NOT_ADMITTED / RESEARCH_ACTIVITY_REGISTER_PENDING. This is not a native Driver Review, official Task, CLAΙM, Result or acceptance. Any later reviewer must retain the author-side contribution disclosure.

## Scope and inherited hypotheses

The exact positive 16-leaf P/Q stopping tree, four signed observation atoms, lawful real randomized causal constraints and three event-TV duals are inherited as **hypotheses**, not independently re-proved here, from the prior BU N=4 reduction at Enterprise Math commit 88492f07eacb063891464c536ec906e8298fcd71. The immediate preceding conditional capacity result is research_notes/brc_n4_bu_capacity_extension_k7_20_20261029_r1t11/PROOF.md at main@cc55cd808640ebaa973d8605e8bda137192073e5 (Git blob a16fa1d7826c62a7dcf27561294d706f070b1299). The model is an external finite-probability abstraction. No X6 three-dimensional-slice or temporal native transfer is claimed.

**Conditional exact all-causal theorem.** For every real

\[
(a,b)\in [989/1000,99/100]\times[307/2100,3/20],
\]

the inherited S2 and S23 observer minimax values agree and equal

\[
E(a,b)=\frac{(a+3b-1)(7-a-21b)}{12(4a+12b+2)}.
\]

The new tail has strictly positive area 1/262500 above the preceding full rectangle's upper edge b=307/2100. It does NOT imply the same formula on the full a∈[97/100,99/100], b≤3/20 rectangle.

## Universal dual lower bound

Let D=4a+12b+2, C=(7-a-21b)/D, E=C(a+3b-1)/12 and fixed k=9/25. Every lawful competitor with common causal c∈[0,1] and e=max(TV_P,TV_Q) obeys the **inherited** event-TV inequalities

\[
L_0(c)=\frac{4a-14b-3ac-(a+3b)c^2}{2(23-2c)}\le e \quad (c\in[0,3/7]),
\]
\[
L_3(c)=\frac{c[a-(a+3b)c]}{2(7-2c)}\le e,\quad
R(c)=\frac{c(a+3b-1)}{12}\le e \quad (c\in[0,1]).
\]

The dual weight positivity / event-list validity is inherited, and remains a separate independent 16-leaf audit obligation.

On the target rectangle a+3b−1≥2993/7000>0, so R increases. Also ∂a C=(72b−30)/D²<0 and ∂b C=−(72a+126)/D²<0. Thus

\[
 k=9/25 < 143/388=C(99/100,3/20)\le C\le C(989/1000,307/2100)=20587/53972 <1.
\]

Symbolic exact subtraction yields

\[
L_0(k)-E=\frac{N(a,b)}{334200(2a+6b+1)},
\]
\[
N=55781a^2+243936ab-90472a+229779b^2-692766b+97475.
\]

Here N_a=111562a+243936b−90472≥27761969/500>0, and N_b=243936a+459558b−692766≤−19116783/50<0. So N≥N(989/1000,3/20)=1792601/1000000>0.

For the other dual,

\[
L_3(k)-E=\frac{(61a+633b-157)(121a+363b-175)}{94200(2a+6b+1)}>0.
\]

Each numerator factor increases in a,b, but even at the upper corner (99/100,3/20) they equal −83/50 and −19/25, respectively. Finally L_3(C)=R(C)=E identically. The derivative

\[
L_0'(c)=\frac{a(2c^2-46c-61)+b(6c^2-138c-28)}{2(2c-23)^2}<0
\]

for c∈[0,k]; while

\[
L_3''(c)=\frac{7(5a+21b)}{(2c-7)^3}<0
\]

for c∈[k,C], so L_3 is concave and minimized at an interval endpoint. Combining all ranges gives

\[
e\ge L_0(c)\ge L_0(k)>E \quad (0\le c\le k),
\]
\[
e\ge L_3(c)\ge\min\{L_3(k),L_3(C)\}=E\quad(k\le c\le C),
\]
\[
e\ge R(c)\ge R(C)=E\quad(C\le c\le1).
\]

These conclusions cover ALL real lawful causal policies if the inherited event-TV duals are valid, not only rational tests or sampled strategies.

## Attainment

The inherited legal causal randomized policy A=1, B=(a+3b−1)/3, c=C, U=B(1+C), V=B is feasible: 0<B≤b≤3/20, U<2b<1=A, V=B. Its inherited signed four-observation-atom differences are

\[
\Delta_Q=((1-a)/3,\ E-(1-a)/3,\ 0,\ -E),\qquad
\Delta_P=(0,0,E,-E).
\]

The sign needed for both TV norms to equal E follows from

\[
E-(1-a)/3=\frac{G}{8(2a+6b+1)},\qquad
G=5a^2+8ab-21b^2-2b-5.
\]

Because G_a=10a+8b>0 and G_bb=−42<0, its minimum over the rectangle is attained at the minimum a and a b endpoint: G(989/1000,307/2100)=183647/600000 and G(989/1000,3/20)=60981/200000. Both are positive. Thus TV_Q=TV_P=E, matching the universal bound.

## Evidence and limitations

Accompanying VERIFY.py passed locally under SymPy with exact rational arithmetic. It checks the symbolic dual-gap identities, monotonicity/concavity identities, rational endpoint signs, causal feasibility and TV of the inherited signed atoms at all four corners. These symbolic checks establish the displayed exact algebra and signs; they DO NOT rederive the inherited 16-leaf reduction, event weights, native X6 bridge, clean independence or admission.

At (a,b)=(99/100,3/20), the former k=7/20 certificate had a negative L_3(k)−E gap (−1/72750); k=9/25 has a positive gap 1577/456870000. Failure of a previous certificate was not evidence that a lawful better competitor existed.

Next: verify 16-leaf to four-atom causal reduction and dual event weights independently; test a variable k(a,b) for the whole high-b strip, or exhibit a legal rational improvement where capacity truly fails. Do not add a redundant official research task without current Driver authority and taskbook deduplication.
