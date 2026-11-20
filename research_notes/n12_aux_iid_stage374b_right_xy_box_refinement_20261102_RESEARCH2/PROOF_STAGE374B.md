# Stage374-B — exact right-source x/y localization in the original 16-label Bernoulli/BRC auxiliary model

Date 2026-11-02 (Asia/Shanghai). Portable Research2 author-side proof. Scientific input freeze: GLOBAL main bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM main 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current rules independently read at GLOBAL main 55f7fddff4fe06a77ecaf7107f8b2d214fe1571d and EM main b46bb821037ee7f21ca0598be6a53d2fee9a655f.

## Definitions, quantifiers and theorem

For k=0,1,2,3 define B_k(z)=z^k(1-z)^(3-k), weights w=(1,3,3,1), m=(61,21,9,9), r_k(x,y)=[4B_k(x)+B_k(y)]/5-m_k/160,
b(x,y)=(5/32)Σ_k w_k|r_k(x,y)|,
D(a,z)=(1/2)Σ_k w_k|B_k(a)-B_k(z)|,
c(x,y)=[63D(1/4,x)+D(3/4,x)+9D(1/4,y)+7D(3/4,y)]/256.
Four provenance-distinct ports retain all sixteen anchor/word comparisons.

Let q* be the unique simultaneous root r0=r1=0 in the Stage366/370 rational isolator and beta*=b(q*). At E=11/5000, minimize T(P,Q)=33/1024+c(P)+c(Q) over independent real P,Q∈[0,1]^2 subject to b(P)+b(Q)≤2 beta*+E.

Stage373-B proves all global minimizers, up to source exchange, lie in P∈(577/2500,469/2000)×(27/50,59/100), Q∈(469/2000,239/1000]×(57/100,29/50).

**Theorem (Stage374-B).** Every global minimizer, after the same exchange, satisfies

P∈(577/2500,469/2000)×(27/50,59/100),
Q∈(473/2000,239/1000]×(143/250,2897/5000).

Thus x_Q>0.2365 and 0.572<y_Q<0.5794, with all boundary cases in the excluded strips covered.

## Universal exact rational interval certificate

Put L=c+(6/5)b, A=37464/1000000 and B=37431/1000000. The accompanying standalone Fraction checker proves four strict bounds on complete closed rectangles:

- L>A on LEFT=[577/2500,469/2000]×[27/50,59/100]: 5915 leaves.
- L>B on RIGHT_LO=[469/2000,239/1000]×[57/100,143/250]: 3817 leaves.
- L>B on RIGHT_HI=[469/2000,239/1000]×[2897/5000,29/50]: 95 leaves.
- L>B on RIGHT_X_LO=[469/2000,473/2000]×[143/250,2897/5000]: 143 leaves.

For each rational interval, the exact range of cubic B_k is determined by both endpoints and its possible interior stationary point k/3. A distance-from-interval lower bound is applied separately to every |r_k| term and to all sixteen source/anchor/word audit comparisons, then summed with positive rational coefficients. The resulting b_lower,c_lower hold simultaneously for every real point in each box. The checker bisects nonclosed boxes recursively and proves all terminal c_lower+(6/5)b_lower bounds strictly exceed the corresponding threshold. Each binary split covers its entire closed parent; exact rational area equality and 0 unclosed leaves verify complete continuous-domain coverage. All algebra and comparisons use Fraction, never floating point.

The checker revalidates rational isolation x*∈(2310839,2310840)/10^7, y*∈(5555086,5555091)/10^7 via residual signs and monotonicity. Since at q* the residuals r0=r1=0, r2>0,r3<0 and Σ_k w_k r_k=0, beta*=(15/16)r2(q*). It follows exactly that

2 beta*+11/5000 < 61/6250.

The rational pair P0=(231138/10^6,555681/10^6), Q0=(237807/10^6,575694/10^6) is strictly feasible by exact lower bounds on beta*, with

c(P0)+c(Q0)=16174439790495832521/256000000000000000000 < 63182/10^6.

For any budget-feasible ordered pair with P∈LEFT and Q in one of the three excluded right rectangles:

c(P)+c(Q)=L(P)+L(Q)-(6/5)[b(P)+b(Q)]
> A+B-(6/5)(61/6250)
= 63183/10^6
> c(P0)+c(Q0)+1/10^6.

Such a pair is strictly cost-dominated by a feasible comparator, so it cannot be a global minimizer. Combine the original Stage373-B ordered domain with the three exclusions to prove the theorem. Continuity and compactness give existence of an optimizer because the displayed rational reference is feasible.

## Executed evidence and next unit

The attached exact source was executed with --emit to generate all 9970 CSV leaves and again without --emit, with byte-identical stdout. Maximum depths 23/22/17/18, zero open leaves. Deterministic CSV size 1,871,013 bytes, SHA256 636a84ea0eb1e9b4aaf7262d632eb7df8207be039044b832885b4ba00e56d4e4. Rebuild with:

    python REPRO_STAGE374B.py --emit CERTIFICATE_STAGE374B_RIGHT_XY_STRIPS.csv

The complete CSV was also preserved as the local author-run artifact. This is an exact continuous-domain author-side theorem, awaiting any applicable independent Driver review. Native P000 X6/three-dimensional-slice/triadic-closure/time/address transfer requires a separately typed observer-preserving map.

Next Stage375-B: investigate the remaining four-dimensional ordered domain using a coupled budget-cost interval certificate or construct a strictly feasible rational competitor to the algebraic Stage367-B post-cusp candidate. Preserve all source labels and scientific pins.
