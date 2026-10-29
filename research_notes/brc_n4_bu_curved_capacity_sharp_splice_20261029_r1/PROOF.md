# BRC N=4 BU: a curved exact capacity-optimal minimax region

2026-10-29 · Author-side analytical theorem / exact-checked / UNREVIEWED / NOT_ADMITTED.

## Model and scope

This theorem uses the pre-existing strictly positive sixteen-leaf P/Q stopping model, target F=(a,b,1,0), terminal joint observer O=(T,Decision,Z_BU), and instantaneous lawful behavioral S2/S23 causal competitors. Full 16-leaf-to-four-observation-atom equivalence for precisely this terminal observer is inherited from Enterprise Math immutable commit 1a4898a57e952245eeacb38be7adf109faa49f49. The legal observable-event TV dual certificates L0/L3 are inherited from 55d5a6f9ed278a01b36f89952b76e3fe7641a9c3 and 13270e163c2838f90f79952fc309beb8ae34b050. These remain author-side rather than independent admitted results.

Let

\[
\alpha(b)=\frac{\sqrt{121b^2+10b+25}-4b}{5},
\quad
b_\sharp=\frac{13462-82\sqrt{16081}}{24045}
\approx0.127407261770570.
\]

The algebraic constant is the smaller positive root of q(b)=24045b²-26924b+3040, and 127/1000<b_sharp<128/1000<13/100.

## Theorem: all real parameters in the curved zone

For every real 0<b≤b_sharp and alpha(b)≤a≤1, optimizing over ALL lawful real randomized causal S2 or S23 competitors gives the exact common minimax error

\[
\boxed{d_2(a,b)=d_{23}(a,b)=
\frac{(a+3b-1)(7-a-21b)}{12(4a+12b+2)}.}
\]

This is an additional continuous nonrectangular sufficient region, not an assertion that alpha or b_sharp is the global minimax phase boundary. For a concrete previously unproved rational parameter, a=481/500, b=3/25, the exact minimax is 283199/21864000 (the attaining continuation C=1759/3644). The region reaches alpha(b_sharp)≈0.960867086124016, extending the earlier a≥0.97 parameter band.

## Exact observation atoms and causal event lower bounds

Every lawful policy has real 0≤A,B,u≤1 and 0≤U≤A, 0≤V≤B. Define

\[
s=(A-a+B-b)/2,\quad t=(A-a+3(B-b))/4,\quad H=Bu/4,
\]
\[
r_Q=a/6-Au/6-U/3-V/4,\quad
r_P=a/6-Au/6-U/12-V/2.
\]

The signed four-atom terminal observer differences are

\[
\Delta_Q=(s,H-s-r_Q,r_Q,-H),\quad
\Delta_P=(t,H-t-r_P,r_P,-H).
\]

The minimax objective is e=max(||Δ_Q||₁,||Δ_P||₁)/2. As total variation bounds every event difference, the prior nonnegative event-mixture certificates give, respectively,

\[
e\ge L_0(u)=\frac{4a-14b-3au-(a+3b)u^2}{2(23-2u)}
\quad(0\le u\le3/7);
\]
\[
e\ge L_3(u)=\frac{u[a-(a+3b)u]}{2(7-2u)}
\quad(0\le u\le1).
\]

These event mixtures preserve Z_BU: they are not hidden source selectors. L0 is decreasing on [0,3/7] because its derivative has numerator a(2u²−46u−61)+b(6u²−138u−28)<0. L3 has no interior minimum on any subinterval of [0,1]: its derivative numerator 7a−14(a+3b)u+2(a+3b)u² strictly decreases there, so any critical point is a maximum.

Set delta=(1-a)/3, B_*=b-delta, C=(7-a-21b)/(4a+12b+2), E=B_*C/4. The actual first-three-atom event of P has signed difference H, and its middle-two-atom event has signed difference H−t. Because A≤1, t≤3(B−B_*)/4. If B≥B_*, use e≥H≥B_*u/4. If B<B_*, use e≥H−t≥Bu/4+3(B_*-B)/4≥B_*u/4 since u≤1. Hence the **newly reused capacity-plus-event certificate**

\[
\boxed{e\ge B_*u/4}
\]

holds for every competitor on this domain, without erasing BU provenance.

## Polynomial sign lemma throughout the whole curved zone

Introduce

\[
G(a,b)=5a^2+8ab-21b^2-2b-5,
\]
\[
P(a,b)=131a^2+576ab-232a+549b^2-1746b+245.
\]

The following are exact rational identities:

\[
L_3(C)=E,\qquad E-\delta=\frac{G(a,b)}{8(2a+6b+1)};
\]
\[
C-\frac37=\frac{43-19a-183b}{7(4a+12b+2)};
\]
\[
L_0(3/7)-E=\frac{P(a,b)}{840(2a+6b+1)};
\]
\[
L_3(3/7)-E=
\frac{(19a+183b-43)(31a+93b-49)}
{7224(2a+6b+1)}.
\]

G is strictly increasing in positive a and its unique positive a-root is alpha(b); therefore a≥alpha(b) gives E≥delta. Moreover G(1−3b/5,b)=−24b²<0, so alpha(b)>1−3b/5, implying delta<b/5, B_*>4b/5>0 and C<1. Because b≤b_sharp<13/100 and a≤1, we also have 19a+183b−43≤−21/100<0 and 31a+93b−49≤−591/100<0. Therefore C>3/7 and L3(3/7)>E.

For the remaining sign P(a,b)≥0, observe: for b in [0,13/100], G(24/25,b) increases with b and G(24/25,13/100)=−17/2000<0, so alpha(b)>24/25. Since P_a=262a+576b−232>0 for a≥24/25, it suffices to prove P(alpha(b),b)≥0.

Exact elimination gives

\[
\operatorname{Res}_a(G,P)
=-144(12b-5)(24045b^2-26924b+3040).
\]

On [0,13/100], this resultant has exactly one zero, b_sharp. At b=0, P(alpha(0),0)=144>0. At b=13/100, G(961/1000,b)=429/200000>0, so alpha(b)<961/1000; since P_a>0,

\[
P(\alpha(13/100),13/100)
<P(961/1000,13/100)=-2712969/1000000<0.
\]

Continuity, the resultant and this sign change give P(alpha(b),b)>0 for 0≤b<b_sharp and P(alpha(b_sharp),b_sharp)=0. To rule out confusion with the negative root of G, the exact remainder P mod G is 4(458ab−290a+1374b²−2117b+470)/5. Its a-root R=(1374b²−2117b+470)/[2(145−229b)] is positive on [0,13/100] and satisfies

\[
G(R)=-\frac{45(12b-5)q(b)}{4(229b-145)^2}.
\]

At b_sharp this R is the **positive** G-root alpha(b_sharp), so the equality endpoint is exact. Thus P≥0 on the entire claimed region.

## Full continuous lower-bound coverage and attaining lawful strategy

The three certificates now cover every real u∈[0,1]:

1. 0≤u≤3/7: e≥L0(u)≥L0(3/7)≥E.
2. 3/7≤u≤C: e≥L3(u)≥min(L3(3/7),L3(C))≥E.
3. C≤u≤1: e≥B_*u/4≥B_*C/4=E.

Choose actual causal parameters A=1, B=B_*, u=C, U=B_*(1+C), V=B_*. They are lawful because 0<B_*≤b<13/100, 0<C<1, U<2b<26/100<1=A, V=B, and 0≤U≤A. Direct exact substitution produces

\[
\Delta_Q=(\delta,E-\delta,0,-E),\qquad
\Delta_P=(0,0,E,-E).
\]

Because 0≤delta≤E, both TV_Q and TV_P are E, matching the universal analytic lower bound. This completes the proof for the whole continuous real domain; no numerical grid-to-continuum inference is used.

## Sharp limit of this certificate only

On the lower curved boundary a=alpha(b), the fixed three-piece splice using L0 at u=3/7 has its exact endpoint b_sharp: P(alpha(b_sharp),b_sharp)=0, while P(alpha(b),b)<0 for b_sharp<b≤13/100. There L0(3/7)<E, so this fixed certificate no longer proves the same optimum. This does NOT establish a genuine minimax phase change; an alternative splice point, another observable event or a competing policy must be investigated.

## Verification, provenance and unresolved obligations

Executed source VERIFY.py passed 33 exact SymPy symbolic relations, including resultant and polynomial remainder, plus six exact rational full 16-positive-leaf P/Q reconstructions with both laws normalized and TV_P=TV_Q=E. All six witnesses and PASS records are in VERIFY_EVIDENCE.txt; finite checks verify algebra and implementations, not the universal inequality independently.

Frozen GLOBAL_KNOWLEDGE_V1 canonical main@ebc95a36c61f05438c3294b5dd4c1e2011f51f70; Enterprise Math initial main@e3148a75734182faea1e2822c84bd782b43005bb. The global P000 startup projection matched its canonical original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. P000, ACTIVE worldview, X6 plus separately typed time, joint-observer preservation, current portable protocol and BRC priority were checked. Authenticated GitHub login awdawmip; native service reported research_authority_granted=false and the bounded owner read failed with CONTROL_QUOTA. No native CLAIM, activity, Result or independent Driver review is claimed; publication is author-side non-admitted research.

These are external finite dual-P/Q probability-law statements only. Added AU source-bit observations, time-four/future operations, native P000 six-dimensional Cell/slice embedding and physical time evolution remain unproved. P000 and ACTIVE worldview are unchanged. Next mathematical discriminator: variable splice or full terminal-event LP dual at b=129/1000 near a=alpha(b), or a complete lawful rational strict counterexample; see NEXT_TASK.md.
