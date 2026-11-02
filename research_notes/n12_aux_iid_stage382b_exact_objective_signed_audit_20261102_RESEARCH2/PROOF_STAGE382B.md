# Stage382-B — Exact objective interval and signed-audit independent check

**Research class:** portable author certificate, not independently Driver-admitted. **Date:** 2026-11-02. Parent: Stage381-B commit d4c0ce1f2ffd941a8f6556f87937cee5257b9953, PR #1736.

**Frozen scientific sources:** GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current rule sources were separately read from GLOBAL main 2e6b960d7bf1d81841356975a2561e7a8f4be18d and EM main 3394518cc290181570ef446e076669aec51e703e. Original P000 and ACTIVE X6 worldview remain unchanged.

## Exact original model

B_k(z)=z^k(1-z)^(3-k), k=0..3; w=(1,3,3,1); m=(61,21,9,9).
r_k(x,y)=[4B_k(x)+B_k(y)]/5 - m_k/160.
D(a,z)=1/2 sum_{k=0..3} w_k |B_k(a)-B_k(z)|.
b(x,y)=(5/32) sum_k w_k |r_k(x,y)|.
c(x,y)=[63D(1/4,x)+D(3/4,x)+9D(1/4,y)+7D(3/4,y)]/256.
T=33/1024+c(P)+c(Q); B_*=2 beta_* + 11/5000; beta_* is budget at r0=r1=0. Optimize on the whole [0,1]^4 subject to b(P)+b(Q)<=B_*. The original 16 audit comparisons per source and four independent residuals are retained.

## New A: exact signed audit

On the inherited closed P rectangle [0.2308,0.2345]×[0.55,0.56] and Q rectangle [0.2365,0.239]×[0.57566,0.57574], exact cubic Bernstein controls for each of 32 coordinate/anchor/channel comparisons certify 31 strict nonzero signs. The single varying original cost audit is (Q,y,a=3/4,k=2):
delta(y)=9/64-y²(1-y)=(y-3/4)(16y²-4y-3)/16.
Its sole zero in the Q rectangle is alpha=(1+sqrt(13))/8. The original cost in both rectangles is therefore exactly
c=C0+21/512 |delta(y)|,
C0=5157/32768-189x/256+93x²/128-61x³/256+33y²/512-29y³/512.
The executable additionally checks original cost vs the piecewise polynomial at 96 exact rational pairs containing at least four distinct abscissae and ordinates in each smooth sign chamber. Once signs are known, both sides have degree ≤3 in each variable, so polynomial interpolation proves the identity throughout each chamber.

On the inherited residual wedge r0≤0≤r1, with r2>0>r3 throughout these boxes (and r0(Q)<0), exact conservation sum_k w_k r_k=0 gives:
b=(5/32)(-r0+3r1+3r2-r3)=(15/16)(r1+r2)
 =(3/16)[4x(1-x)+y(1-y)]-45/256.
This identity is valid **in that wedge**, not asserted on arbitrary parameters. No individual original residual was discarded before the signed identity was established.

## New B: rational algebraic candidate/objective isolation

On r1=0, 4f(x)+f(y)=21/32, f(z)=z(1-z)². On the relevant boxes f'(x)>0>f'(y), giving a unique increasing y(x). The r0=0 face intersection is isolated by 68 x-bisections and 115 nested y-bisections with strict rational endpoint signs:
0.231083940855521784 < x_beta < 0.231083940855521785,
0.555508857277334359 < y_beta < 0.555508857277334360,
0.003779133618858469 < beta_* < 0.003779133618858470.

The quadratic 16 alpha²-4 alpha-3=0, solved by 90 exact bisections, and the Q r1 face, solved by 85 exact bisections, yield:
0.575693909432998661 < alpha < 0.575693909432998662,
0.237806902790747172 < x_Q < 0.237806902790747173,
0.005960540845879909 < b(Q) < 0.005960540845879910.

Under Stage381-B's author-side candidate system (r1(P)=r1(Q)=0, yQ=alpha and active joint budget), the P face budget is strictly increasing, with exact directional derivative
Bdot=[3/(4(1-y)(3y-1))](y-x)(6xy-3x-3y+2)>0
because the final factor on the P box is at least 25193/62500. Its unique budget root is isolated:
0.231139116642444278 < x_P < 0.231139116642444861,
0.555684475792773398 < y_P < 0.555684475792775251.

Evaluating the exact absolute-value C0 expression by rational interval arithmetic, including the cusp interval, gives:
**0.095407556068 < T_candidate < 0.095407556069**.
The unrounded mathematical interval is less than 9×10^-16 wide, so it comfortably satisfies the requested <10^-8 precision. Exact rational bounds reside in the regenerated JSON certificate.

**Global-optimality scope:** This is an *unconditional interval for the algebraic candidate* and a **conditional global optimum value** only if the inherited Stage379/380 localization and Stage381 global uniqueness proofs hold. No new independent global-optimality claim is made.

## New C: full-original-model rational feasible witness

P0=(0.2311391166,0.5556844758),
Q0=(0.2378069027,0.5756939095).
With the original four absolute-valued residuals the joint budget is strictly below 2 beta_lower+11/5000, with certified slack >2.82×10^-11. With the original sixteen labeled comparisons per source, the cost satisfies:
**0.095407556128 < T(P0,Q0) < 0.095407556129**.
This pair gives an unconditional full-domain upper bound on the global optimum, independent of Stage381's optimality theorem.

## Executed exact evidence and limits

The local expanded Fraction checker was executed twice with identical stdout; it emitted a 11993-byte JSON certificate, SHA256 b418782298fa36eb34f9c4e494fde5c116990c900b283a0f3d870f3e9f481b75. The adjacent portable standalone REPRO_STAGE382B.py implements the same exact formulas, sign controls, rational brackets and witness; reproduce and compare the certificate digest. Actual remote code publication is not native Source admission.

This is an auxiliary observer optimization. Native P000 X6 requires explicit embedding, third coordinate semantics and preservation under declared future operations. BRC label/provenance distinctions have not been silently promoted into a native geometric theorem.

**Next Stage383-B:** independently prove or falsify one inherited Stage380 wedge/active-budget boundary perturbation, or Stage379 global localization, against the original unsimplified model. Publish an exact counterexample if found and identify the first invalid lemma.