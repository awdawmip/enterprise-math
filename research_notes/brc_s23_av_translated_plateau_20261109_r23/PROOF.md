# R23: a source-labelled 389-step zero-risk epoch for the S23/AV circle observer

Date: 2026-11-09. Scientific input (unchanged): enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. This is the auxiliary scalar circle observer, with m=128 historical cuts. Antecedent: r22 proof, PR #1887, commit ce48aafd77dadce7ed56ac345cd4a8e76498ff2a. Author-side exact result; independent mathematical review pending.

## Precise statement

Let phi_j={j theta}, P_n={phi_j:0<=j<n}, and let I range over adjacent circular intervals of P_128. Let M_n(I) be the longest subinterval of I after refinement by P_n. Define R(128,n-128)=1-sum_I M_n(I). Assume irrational theta belongs to the strict certified interval

262204504569236716045286/10^24 < theta < 262204504569236716045287/10^24.

Put a=164 theta-43, b=59-225 theta, c=102-389 theta=b-a, e=145-553 theta=c-a, and f=717 theta-188=a-e. Exact endpoint comparisons give 0<f<e<a<c<b. Then the following holds for *every integer* in each displayed range:

- 492<=n<=553: R=-10432+39788 theta+(n-492)a.
- 553<=n<=620: R=-13055+49792 theta+(n-553)e.
- 620<=n<=656: R=-3340+12741 theta.
- 656<=n<=717: R=-3340+12741 theta+(n-656)e.
- 717<=n<=1106: R=5505-20992 theta.
- n=1107: R=5317-20275 theta.

Thus 389 consecutive cut additions n=718,...,1106 have exactly zero risk increment; the n=1107 addition restores strictly positive increment f. This extends r22's n=493 frontier by exact proof and independently computed finite checks.

## Translation lemma and proof

Let a new cut labelled t0 enter an historical clockwise adjacent arc phi_u -> phi_v. For s>=0 suppose the translated indices u+s and v+s are still historical (<128) and form another historical adjacent arc. Then, immediately before insertion of label t0+s, every interior cut of the translated historical arc is exactly label j+s for an interior cut j of the first arc immediately before t0. Rotation by s theta preserves ordered gaps and each source label. The only extra predecessor labels 0,...,s-1 are historical, so none lies inside the shifted historical adjacent arc. Consequently the *complete ordered source-labelled fibre* and its impending split are equal after index translation. The risk increment is therefore equal. QED.

For any split of a gap g=x+y and maximal length M of unaffected gaps in the same historical arc, the risk increment is max(g,M)-max(x,y,M). In particular, splitting one of two equal longest gaps gives zero increment. The labelled fibre retains where the next cut lands; a total-length-only observer need not.

## Three historical adjacency certificates, reused from r22 and rechecked

For shifts 0<=s<=24: historical arcs (s,103+s), clockwise gap G=103 theta-27. All possible intervening historical displacements lie in [-24,127]. Exact endpoint tests show {k theta}>G for all except k=0,103.

For shifts 0<=s<=35: historical arcs (25+s,67+s), clockwise gap H=42 theta-11. All displacements lie in [-60,102]; {k theta}>H for all except k=0,42.

For shifts 0<=s<=66: historical arcs (61+s,s), clockwise gap d=16-61 theta, the unique minimum of ||k theta|| for 1<=k<128.

Each strict inequality, phase floor and phase-order comparison for indices 0..1106 has a constant sign at both rational enclosure endpoints. Hence all comparisons and conclusions hold throughout the open theta interval.

## Sixteen source-labelled base families

The exact finite certificate is reproducible by VERIFY_R23.py. Each tuple has form (pre-insertion t0, number of consecutive shifts, historical owner, exact increment). Owner index means the left endpoint of the historical arc; all source labels and gap lengths are computed as integer-affine pairs by the verifier.

(492,25,0,a); (517,36,25,a); (553,67,61,e); (620,36,25,0);
(656,25,0,e); (681,36,25,e); (717,25,0,0); (742,36,25,0);
(778,67,61,0); (845,36,25,0); (881,25,0,0); (906,36,25,0);
(942,67,61,0); (1009,36,25,0); (1045,25,0,0); (1070,36,25,0).

At each base t0 the verifier independently reconstructs the full ordered source-labelled subpartition within the historical owner arc and the exact insertion split. The translation lemma and one-time adjacency certificates then transport the entire fibre across its claimed 25, 36 or 67 shifts. The 16 disjoint, consecutive ranges exhaust 493..1106 (614 updates). The first six families have aggregate nonzero increments 61*a+128*e, with a 36-step tie plateau at n=621..656. The last ten families account for exactly 389 consecutive zero increments. Their endpoints yield the displayed affine risk formula.

The base immediately before insertion t=1106 is the historical arc 61->0 with successive labelled gap lengths f,e,f,e,a,e. The new cut splits the **unique** a into f and e, so the increment is a-e=f; therefore R(128,979)=5317-20275 theta.

## Certificate and scope

VERIFY_R23.py uses Python Fraction and integer-affine gap pairs. It checks all cut floors/order at both strict bounds, the three displacement adjacency certificates, 16 complete base fibres and their translated copies, every exact insertion delta for n=493..1107, and fresh independent full circle partitions at all base and epoch endpoints. It also recovers the r22 value R(128,364)=-10432+39788 theta by construction from n=128, not by trusting a printed predecessor value.

The calculation is a finite exact proof certificate on the given parameter interval and horizon, with a general translation lemma. No new asymptotic running-time claim is made; exact integer bit costs and the 24-decimal-place source interval remain relevant. BRC reuse: REUSE_APPLIED, in typed preservation of source-labelled fibres, split destinations and maximum-tie multiplicity. No native X6 or P000 result is asserted by the circle calculation.

Next unit: starting at n=1107, derive the entire next nonzero-growth family and its first tie/plateau breakpoint from the historical arc 61->0, then connect adjacent source-labelled families with Farey/continued-fraction jump identities without losing future-insertion destinations.
