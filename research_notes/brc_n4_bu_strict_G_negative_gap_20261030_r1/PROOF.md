# BRC N=4 BU: strict quantitative minimax gap at G<0

Date 2026-10-30 Asia/Shanghai. **AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.** Continuation of PR #1729, author-side. External strict-positive sixteen-leaf double-law P/Q model, full observer O=(T,Decision,Z_BU), a=961/1000, b=151/1000; common AU/BU continuation u in [0,1]. S2->S23 causal reduction and L0/L3 event legality are **inherited author-side hypotheses requiring independent audit**.

## Theorem and exact inputs

Set X=a+3b=707/500, δ=(1-a)/3=13/1000, D=b-δ=69/500, R=7(X−1)/(6X)=69/202, C=(7−a−21b)/(4X+2)=239/638, E=DC/4=16491/1276000, H=b(2a−7b)/(8(a+2b))=26123/2020800. For either lawful real behavioral policy class S2/S23, under the stated inherited conditions:

\[
\boxed{E+1/1500000 \le d_2(a,b),\ d_{23}(a,b) \le H.}
\]

Thus E is **globally unattainable**, strengthening the previous observation that only the particular E-capacity candidate fails. The exact value H versus a third value is not yet decided. H−E=9919/3223176000.

## Lawful full-joint K(u) lower bound, from event atoms

Let A,B be the competitor's first-stage rates, 0≤A,B≤1, and U,V unnormalized surviving AV/BV masses (0≤U≤A and 0≤V≤B). For e=max(TV_P,TV_Q), the target-minus-competitor observed atom differences are

\[
s=\Delta_Q(1,Q,0)=(A+B-a-b)/2,\quad
t=\Delta_P(1,Q,0)=(A-a+3(B-b))/4,\quad
\Delta_P(3,Q,Z_{BU}=1)=-h,\quad h=Bu/4.
\]

Consequently e≥s, e≥h, and e≥h−t (the P-law disjoint union event of time-one Q stop with BU source-marked time-three arrival). For any 0≤u≤1, the positive coefficients λ_s=u/(4+u), λ_h=2(2−u)/(4+u), λ_{h-t}=2u/(4+u) sum to one. Since s−2t=b−B,

\[
e\ge\lambda_s s+\lambda_hh+\lambda_{h-t}(h-t)
=\frac{u(s-2t)+4h}{4+u}=\boxed{K(u)=bu/(4+u)}.
\]

This rederives a previously known K form from full BU-preserving observable atoms, and uses it in a new G<0 regime.

## Complete real-continuation certificate

Use inherited lawful observable-event bounds

\[
L_0(u)=\frac{4a-14b-3au-Xu^2}{2(23-2u)}
\quad (0\le u\le3/7),\qquad
L_3(u)=\frac{u(a-Xu)}{2(7-2u)}\quad(0\le u\le1).
\]

Choose exact rational split points q1=214/625=0.3424 and q2=14977/40000=0.374425. Then 0<R<q1<q2<C<1 and q1<3/7. Direct rational evaluation gives:

| Margin | Exact positive rational value |
|---|---|
| L0(q1)−E | 70817303/11122732500000 |
| L3(q1)−E | 9259803/3147732500000 |
| L3(q2)−E | 2170463043/3190586960000000 |
| K(q2)−E | 269/369042400 |

**Every margin exceeds ε=1/1500000**, exactly. L0' has numerator a(2u²−46u−61)+b(6u²−138u−28)<0 for u≤3/7, so e≥L0(u)≥L0(q1)>E+ε when u≤q1. The L3' numerator is 2Xu²−14Xu+7a, whose derivative 4Xu−14X<0 throughout [0,1]. Thus L3 has at most one internal maximum and no interior minimum; on [q1,q2], e≥L3(u)≥min(L3(q1),L3(q2))>E+ε. Since K'(u)=4b/(4+u)²>0, for u≥q2, e≥K(u)≥K(q2)>E+ε. The three intervals cover **all real** u∈[0,1]; finite sampling does not prove the bound.

## Lawful upper strategy and exact 16-leaf check

Take u_H=(2a−7b)/(2a+4b)=865/2526, A=a, B=b, U=b(1+u_H), V=b. Here **U,V are unnormalized survivors**, so the actual AV rate is U/A, BV rate is V/B=1. The inequalities 0<u_H<1, 0<U<A≤1, 0<V=B≤1 hold.

Q category masses are (AU,AV,BU,BV)=(1/6,1/3,1/4,1/4); P category masses are (1/6,1/12,1/4,1/2). The sixteen positive leaves split every category into j,l∈{0,1}; the P/Q likelihood by j is AU:(9/10,11/10), AV:(1/4,1/4), BU:(1/5,9/5), BV:(2,2). Preserve time, decision, and BU lineage in the four terminal observation atoms. Exact independent Fraction reconstruction of all sixteen leaves confirms

\[
TV_P=TV_Q=26123/2020800=H.
\]

The companion verifier checks both normalized source laws, four rational endpoint margins, the exact upper strategy and its P/Q TV; literal stdout is preserved separately.

## Authority, provenance, and continuation

GLOBAL_KNOWLEDGE_V1 immutable main c73c6ad86b0d7ff507fd3d39d574765e034fecf9; Enterprise Math main bb580b9159a1b170964b7c030c909c37a6f78106; inherited moving-root proof commit 7ca502f03fcd70e065444889c967112c6548ed4c (PR #1729); earlier causal-reduction author commit 1a4898a57e952245eeacb38be7adf109faa49f49. P000, ACTIVE worldview, full joint preservation, portable research protocol read at frozen sources. Authenticated GitHub account awdawmip. Native Site research_authority_granted=false; active-owner query CONTROL_QUOTA. Author-side evidence only: no native CLAIM/Result, genuine Driver review, P000 X6 three-dimensional slice or independent time theorem.

**Next:** establish e≥H for all real u using a lawful stronger full-joint event dual, or produce legal rational (A,B,u,U,V) with exact full-sixteen-leaf P/Q max TV strictly <H. Reaudit the inherited L0/L3 observable weights and causal contraction before admission.