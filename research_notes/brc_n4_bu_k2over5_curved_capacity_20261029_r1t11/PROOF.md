# BRC N=4 BU: exact rational-splice capacity theorem past b-sharp
Author-side analytical result (2026-10-29). UNREVIEWED / NOT_ADMITTED. Exact scope: pre-existing strictly positive 16-leaf dual P/Q model, target F=(a,b,1,0), full terminal joint observer (T,Decision,Z_BU), all real lawful instantaneous causal S2/S23 competitors. This is not a claim concerning native P000 X6, future readouts or physical time.

## Prior facts, preserved provenance
Use the four-atom causal reduction and observable-event TV inequalities established as *author-side* in:
- https://github.com/awdawmip/enterprise-math/blob/1a4898a57e952245eeacb38be7adf109faa49f49/ (four-atom reduction)
- https://github.com/awdawmip/enterprise-math/blob/d78e2b5729c824918126aec8ffb26ff3e5dc4cb5/research_notes/brc_n4_bu_curved_capacity_sharp_splice_20261029_r1/PROOF.md (exact L0/L3/capacity dual and construction).
Write
\[
\delta=(1-a)/3,\quad B_*=b-\delta,\quad
C=(7-a-21b)/(4a+12b+2),\quad E=B_*C/4,
\]
\[
G(a,b)=5a^2+8ab-21b^2-2b-5,\quad
\alpha(b)=(\sqrt{121b^2+10b+25}-4b)/5.
\]
The prior event-total-variation lower bounds hold for all lawful strategies:
\[
e\ge L_0(u)=[4a-14b-3au-(a+3b)u^2]/[2(23-2u)]\quad (0\le u\le3/7),
\]
\[
e\ge L_3(u)=u[a-(a+3b)u]/[2(7-2u)]\quad (0\le u\le1),
\qquad e\ge B_*u/4\quad (B_*>0).
\]
In particular L0 is decreasing on [0,3/7], L3 has no interior minimum on [0,1], and \(L_3(C)=E,\ E-\delta=G/[8(2a+6b+1)]\).
The BU provenance is retained in these observed event bounds.

## New theorem
For every real
\[
\boxed{0<b\le27/200,\qquad\alpha(b)\le a\le1,}
\]
the global exact minimax values coincide:
\[
\boxed{d_2(a,b)=d_{23}(a,b)=
\frac{(a+3b-1)(7-a-21b)}{12(4a+12b+2)}=E.}
\]
The earlier fixed-splice sufficient limit \(b_\sharp=(13462-82\sqrt{16081})/24045\approx0.12740726177\) is strictly below \(27/200=0.135\). Therefore it is not the true minimax change point: a full two-parameter open region beyond it retains this capacity-optimal value. We do not assert \(27/200\) is sharp.

## Complete analytic proof given the prior event bounds
Set \(a_0=9607/10000,\ b_1=27/200,\ k=2/5<3/7\). The positive root of \(G(a,b)=0\) in \(a\) is \(\alpha(b)\). Since \(G(a_0,b_1)=-8931/20000000<0\) and
\(\partial_b G(a_0,b_1)=39/2500>0\), with this derivative decreasing in b, \(G(a_0,b)<0\) for all \(0\le b\le b_1\), so \(\alpha(b)>a_0\). Also \(G(1-3b/5,b)=-24b^2<0\), hence \(\alpha(b)>1-3b/5\). It follows that \(B_*>4b/5>0,\ 0\le\delta\le E,\ 0<C<1\).

The continuation \(C\) decreases in both a and b over the region:
\[
\partial_a C=-(30-72b)/(4a+12b+2)^2<0,\quad
\partial_b C=-(72a+126)/(4a+12b+2)^2<0.
\]
Thus \(C\ge C(1,b_1)=211/508>k\).

At this new rational splice, direct exact algebra gives
\[
L_0(k)-E=N_0/[4440(2a+6b+1)],
\quad N_0=713a^2+3128ab-1216a+2967b^2-9218b+1295,
\]
\[
L_3(k)-E=
(13a+129b-31)(23a+69b-35)/[3720(2a+6b+1)].
\]
Both differences are strictly positive on the whole rectangle \(a_0\le a\le1,\ 0\le b\le b_1\). Indeed
\[
\partial_b N_0\le -528891/100<0,\quad
\partial_a N_0(a,b_1)\ge2881191/5000>0,
\]
so \(N_0(a,b)\ge N_0(a_0,b_1)=17619237/100000000>0\). The two factors of \(L_3(k)-E\) are each negative, bounded above by \(-117/200\) and \(-537/200\) respectively.

For *every* real continuation \(u\in[0,1]\), use the exhaustive partition:
- \(0\le u\le k\): \(e\ge L_0(u)\ge L_0(k)>E\);
- \(k\le u\le C\): \(e\ge L_3(u)\ge\min(L_3(k),L_3(C))=E\);
- \(C\le u\le1\): \(e\ge B_*u/4\ge B_*C/4=E\).

Finally choose lawful causal \((A,B,u,U,V)=(1,B_*,C,B_*(1+C),B_*)\). Legality follows from \(0<B_*\le b\le27/200,\ C<1,\ 0<U<2b\le27/100<1=A\) and \(V=B\).
The complete four-observer signed differences become
\[
\Delta_Q=(\delta,E-\delta,0,-E),\qquad
\Delta_P=(0,0,E,-E).
\]
Since \(0\le\delta\le E\), both law-specific total variations equal \(E\). Matching lower and upper bounds proves the all-real-parameter theorem (conditional on the cited four-atom/event-certificate dependencies). QED.

## New exact rational discriminator
At \(a=961/1000,\ b=129/1000>b_\sharp\), \(G=237/125000>0\), so this is inside the new region. Exact values:
\[
C=555/1232,\quad B_*=29/250,\quad U=51823/308000,\quad
d_2=d_{23}=3219/246400.
\]
The companion verifier constructs all 16 strictly positive P/Q leaves, checks normalization and these law-specific TV values. Six rational parameter witnesses and 29 exact symbolic identities were executed; finite checks support but do not replace the analytic proof. See VERIFY.py and VERIFY_EVIDENCE.txt.

## Boundaries, source and authority
Frozen global rules: GLOBAL_KNOWLEDGE_V1 main@810119772912460cd8f1838f6017db2dd4e5ad77; Enterprise Math source input main@13c96bdc2c883b5f9e5aa6c75ecfd0b7b26d4048. Read P000, ACTIVE worldview, joint observer preservation and portable research protocol. The native gateway observed research_authority_granted=false and active-job quota 5/5, with no current formal owner verified. There is no native CLAIM/Result/Driver review and no admitted theorem. Native X6, 3D slice, AU source bit, future events and time dynamics require separate fidelity proofs.

Next: test b>27/200 around a=alpha(b) with legal variable-splice or new observable dual, or full rational strict counterexample. Details in NEXT_TASK.md.
