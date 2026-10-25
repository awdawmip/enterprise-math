# N14 auxiliary ternary iid Stage133: full real-affine primal/dual theorem and right sharpness

STATUS: AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_PROOF. This is an external auxiliary iid problem; neither native P000/Heartbeat X6 transfer nor independent Research Driver review is established.

## Theorem

For N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), and arbitrary randomized stopping/decisions on full *literal ordered* prefixes, let eP=P(declare Q), eQ=Q(declare P), tP=E_P[tau], tQ=E_Q[tau], and V14(alpha)=inf max(tP,tQ) with both errors <=alpha.

Consume Stage132's author-side proved endpoint, alpha132=12234055251084235565/35205614928358539264 and V132=72989119067006060803/5867602488059756544. Then for **every real** 0<=delta<=eta133=25790646875/3223170312044544,

V14(alpha132+delta)=V132-(1392174556/1179001)*delta.

The right endpoint is **alpha133=36703010861169506695/105616844785075617792** and **V133=656403116242184147227/52808422392537808896**. The supporting affine line is right-sharp (not a claim that primal feasibility ends there).

## Universal Bellman lower bound

For s=(n,a,b) counts of symbols 0 and 1, the likelihood ratio on every ordered prefix with those counts is r=Q/P=2^(a+b)/3^a. Set K=717127668/1179001, L=675046888/1179001. Exactly compute H(s)=min{K*r,L,1+sum(Pj H(child_j))}; omit continuation at n=14. Every one of the 680 count states is checked by Fraction. There are exactly 1238 strictly positive unchosen-action gaps, no negative gap, minimum positive gap 129758627/4074627456, and only two ties: B=(11,0,1), declare Q/continue; F=(8,1,2), declare Q/continue. H(root)=36407190671104521664854919/86115052294916278321152.

This dynamic program bounds **all** literal ordered-history strategies, not only count policies: iid suffix distributions and r coincide on any prefixes with the same count; backward induction applies to each prefix. In P units H(root)<=tP+L*eP+K*eQ<=max(tP,tQ)+(K+L)*alpha.

## Exact ordered positive-weight carrier and independent computation

Preserve every literal ordered prefix and its P/Q positive rational probability and action until the four-observer map (eP,eQ,tP,tQ), using the positive weighted-branch/provenance aspect of BRC only for this external iid model. A separately coded top-down integer-weight DFS (P numerators 3,1,20 over 24, Q numerators 1,1,10 over 12) finds **actual first-hit** masses under the strict Bellman policy:

B: 11 distinct literal first-hit words; P=107421875/1451188224, Q=107421875/725594112.
F: 112 distinct literal first-hit words; P=21875/2239488, Q=21875/839808.

The tied cones are disjoint: F has one symbol 0 at depth8 and cannot reach B which has none at depth11; B is deeper so cannot reach F. Therefore randomizing at B and F produces no mixed term. Let w=Pr(stop Q at B), z=Pr(stop Q at F); otherwise continue, and use unique Bellman choices elsewhere. Define M=(eP,eQ,tP,tQ). Exact calculation yields

M(w,z)=M00+w*dB+z*dF, where:

M00=(2430614155800880769/7011906707722862592,447126332273041/1283918464548864,10936533185003261711/876488338465357824,142234281771437/11888133931008).

dB=(4619140625/2229025112064,-751953125/417942208512,-25673828125/278628139008,-17939453125/104485552128).

dF=(1016684375/7925422620672,-120903125/1253826625536,-180971875/12230590464,-3572471875/104485552128).

M11-M10-M01+M00=(0,0,0,0), verified by both implementations. The integer-weight DFS traverses (00,01,10,11) respectively 747778,736690,747646,736558 ordered prefix nodes and ends on 498519,491127,498431,491039 literal terminal words. These are exhaustive counts, not a sample.

## Legal continuum, time dominance and primal/dual equality

Solving eP=eQ gives exactly

w(z)=3079578232623767/7403520000000000 - (46161227/795300000)*z, 0<=z<=1.

Its endpoints obey 0<w(1)=29148450914061437/81438720000000000<w(0)<1. Along the curve,

eP=eQ=alpha132+(25790646875/3223170312044544)*z,
tP=V132-(1392174556/1179001)*(25790646875/3223170312044544)*z.

At z=0 and z=1, respectively, tP-tQ equals 86558755630978696807/158425267177613426688 and 88899829683689096807/158425267177613426688, both strictly positive. The gap is affine, hence tP>tQ throughout the entire closed real interval. All actions are Bellman minimizers and the exact identity tP+L*eP+K*eQ=H(root) holds at both endpoints and hence throughout. The unrestricted dual bound is attained for **every real** z in [0,1], proving the theorem.

## Right sharpness against per-prefix coins

Suppose alpha>alpha133 also attained the same dual support line. The finite-horizon behavioral policy domain is compact and all four observables are continuous, so a minimizer exists. K,L>0 then force saturation eP=eQ=alpha, tP=max(tP,tQ), and only Bellman-minimizing actions along every positive-P-mass reached literal prefix. There are only the two ties B and F. Every first-hit prefix within a tie count has identical likelihood ratio and conditional iid suffix; even history-specific coins collapse *for these four observables only* to a P-first-hit-mass-weighted effective coin in [0,1]. Disjoint cones exclude interactions. The resulting balance law is the displayed w(z); therefore alpha=alpha132+eta133*z<=alpha133, contradiction. Thus the supporting line cannot extend to the right even among arbitrary literal-prefix policies.

## Validation, frozen sources, non-promotions, next task

Locally executed (1) exact Fraction Bellman/observer checker, 680 states, complete action gaps, all corners, endpoint and dual identities: PASS; and (2) independently coded ordered integer-word DFS with actual history counts and complete corners: PASS. Source readback in GitHub is *storage verification*, not remote execution or mathematical peer review. A further exact Stage134 ray scan is **DUAL_CANDIDATE_ONLY**, not a primal theorem.

Pinned at start: GLOBAL_KNOWLEDGE_V1 main@c88538f7cca687bea21eb55c5c546fff84c35d86, Enterprise Math main@59fe656c8f3544c87efc4f7b622bd21f03666f73, original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched its startup projection. Native control_tasks => CONTROL_QUOTA; native Researcher session_start => STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Current live owner, CLAIM, native Result and independent Driver authority were **not** verified; publication is ordinary author-source material only. No proved embedding/readout/suffix-observer-preserving bridge to P000's six-dimensional discrete Cell world, and no physical Heartbeat conclusion.
