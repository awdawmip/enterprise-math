# Stage375-B — exact left-source y-localization by a joint budget/cost dual certificate

Date: 2026-11-02 (Asia/Shanghai). Status: PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Scientific source freeze (unchanged): GLOBAL main bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM main 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavioral norms independently read 2026-11-02: GLOBAL canonical main b73614fc02ad989a719f894be6a90379982379dc and EM main 01686797499ab8cbd9e3d9416990958987f8a9d7. Previous result: Stage374-B exact proof, commit b8868973e61714da38d05b78d01c6280768762a1, PR #1736.

## Mathematical objects and theorem

Let k=0,1,2,3; B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9). Define

r_k(x,y)=[4B_k(x)+B_k(y)]/5 - m_k/160,
b(x,y)=(5/32)Σ_k w_k |r_k(x,y)|,
D(a,z)=(1/2)Σ_k w_k|B_k(a)-B_k(z)|,
c(x,y)=[63D(1/4,x)+D(3/4,x)+9D(1/4,y)+7D(3/4,y)]/256.

These retain the 16 distinct anchor/word audit comparisons through four independent provenance-labelled audit channels. Let q* denote the Stage374-B unique simultaneous r0=r1=0 root, beta*=b(q*). At E=11/5000 minimize T(P,Q)=33/1024+c(P)+c(Q) over real P,Q in [0,1]^2, b(P)+b(Q)<=2 beta*+E.

Stage374-B proves every global optimizer, after source exchange, lies in
P in (577/2500,469/2000) x (27/50,59/100),
Q in (473/2000,239/1000] x (143/250,2897/5000).

**Theorem.** Every global optimizer (with the same order) also satisfies

P in (577/2500,469/2000) x (11/20,14/25),
Q in (473/2000,239/1000] x (143/250,2897/5000).

Thus 0.55<y_P<0.56. For any budget-feasible pair in the stated Stage374-B domain, y_P<=0.55 entails cost gap >8/100000 over the rational feasible comparator, and y_P>=0.56 entails cost gap >1/100000. The closed boundaries are included in the excluded regions.

## Exact dual proof

Fix λ=13/10 and L=c+λ b. The accompanying executable Fraction checker proves these strict all-real bounds over complete closed rational rectangles:

P_LO: x in [577/2500,469/2000], y in [27/50,11/20] => L>37970/10^6 (503 leaves).
P_HI: x in [577/2500,469/2000], y in [14/25,59/100] => L>37900/10^6 (1070 leaves).
Q_CORE: x in [473/2000,239/1000], y in [143/250,2897/5000] => L>37980/10^6 (2046 leaves).

For any rational interval the exact range of the cubic B_k is obtained from its endpoints and the possible interior stationary point k/3. Distance from a fixed target to the containing interval is a rigorous lower bound on the absolute-value term. Apply separately to each residual channel and every one of the 16 source/anchor/word audit comparisons, with original positive port weights; hence the exact interval values b_lower,c_lower satisfy L>=c_lower+λ b_lower throughout the box. The checker recursively bisects each rectangle, closes a leaf only when its rational L_lower strictly exceeds the target, and checks exact dyadic covering area and leaves=splits+1. Every real point is covered.

Its exact reference checks isolate q* by the Stage374-B residual signs, verify 2 beta*+11/5000 <61/6250, and certify that P0=(231138/10^6,555681/10^6), Q0=(237807/10^6,575694/10^6) is budget-feasible, with c(P0)+c(Q0)=16174439790495832521/256000000000000000000 <63182/10^6.

For a feasible pair with P in P_LO and Q in Q_CORE:
c(P)+c(Q)=L(P)+L(Q)-(13/10)(b(P)+b(Q))
> (37970+37980)/10^6-(13/10)(61/6250)
=63262/10^6 > c(P0)+c(Q0)+8/100000.

For P in P_HI, the same calculation yields
c(P)+c(Q)>(37900+37980)/10^6-(13/10)(61/6250)
=63192/10^6 > c(P0)+c(Q0)+1/100000.

These exclude both P strips, including endpoints. Compact feasible set and the feasible reference ensure existence of a minimizer. Combining with Stage374-B gives the displayed necessary central P-band.

This is a dual sum of source-local interval bounds with joint two-source budget accounting; a fully adaptive 4D partition remains the next research unit.

## Executed evidence and open question

REPRO_STAGE375B.py was actually executed with --emit to generate complete CSV and a second time without --emit; stdout matched byte-for-byte. Result STAGE375B_LEFT_Y_BAND_EXACT_PASS; 3619 rational dyadic leaves, no unresolved leaf; depths 15/18/16. Deterministic certificate: 653418 bytes, SHA256 75d0233f4425b0ad8f6fb46bea8a68be1568e328b237ef8cf9250c5d3cc8e6e7. Executed stdout and reproduction source are stored alongside this proof; full local CSV is preserved, and the remote source generates it deterministically.

Next Stage376-B: within P x-range (0.2308,0.2345), y-range (0.55,0.56); Q x-range (0.2365,0.239], y-range (0.572,0.5794), build a genuinely coupled four-dimensional partition using simultaneous b(P)+b(Q), c(P)+c(Q) and interval candidate bounds, or an exact feasible rational counterexample to the Stage367-B algebraic cusp candidate. Native P000 X6 / 3D-slice / triadic-closure / typed-time / Cell-address transfer is a separate observer-preserving question. No native CLAIM, Result or independent Driver acceptance is claimed.
