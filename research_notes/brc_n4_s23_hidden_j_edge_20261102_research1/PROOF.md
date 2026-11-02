# BRC N=4/S23: exact hidden J(t) adversary in the S18 fixed bank (2026-11-02)

**Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_AND_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED.** Scientific input frozen at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessor PR #1765, commit `41b1b8defffdf1e7909a5ff26ea8087bc8d53604`, research_notes/brc_n4_s23_s18_plus_v_sharp_four_sevenths_20261102_research1/.

## Exact object

Retain the original 6 prepared S23 source labels (AU0,AU1,AV,BU0,BU1,BV), their positive M20 mixture and shared causal parameter b_U. For original policy z with 11 real coordinates, F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)), and Q_i(D) the same-source mixed rows of one common stochastic decoder, put L_D(z)=max_{i=1..6} TV(P_i(z),Q_i(D)). Hold the original seven decoders D1,D2,D3,D4,D6,D7,D8 fixed, plus the explicit K1,K2,K3 given by the S18 predecessor. Define R_bank(z)=min of these ten L_D(z).

### Exact finite-grid result (complete declared finite sets)

The executed VERIFY_GRID.js recomputes the exact prepared probabilities and decoder rows at integer scale 50400 and total-variation denominator 100800. Over all 2^11=2048 binary policies, max R_bank=4/7 with 64 maximizers; over all 3^11=177147 ternary policies with coordinates {0,1/2,1}, max R_bank=4/7 with 972 maximizers. Neither finite set has any point exceeding 4/7. Over the 78,848 policies with one coordinate in {1/8,...,7/8} and the other ten binary, 256 exceed 4/7 and the maximum is 5/8. These are finite complete enumerations, not eleven-dimensional continuum proofs.

### Theorem: an exact all-real hidden-edge peak

In the 11-coordinate order (a_A,a_B,b_U,b_AV,b_BV; c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV), define the lawful edge J(t)=(1,t,0,0,0;0,0,0,0,1,0) for every REAL 0<=t<=1. Then

**max_{0<=t<=1} R_bank(J(t)) = 40/63, uniquely at t*=17/63.**

Proof. For this J(t), the unmixed A-source rows are e1, the BU0,BV rows are te1+(1-t)e4, and BU1 is te1+(1-t)e3. The original M20 mixing is linear, so every prepared P_i(J(t)) is affine in t. Therefore, for any fixed decoder D, each TV(P_i(J(t)),Q_i(D)) is convex; its maximum over the six original source labels, L_D(J(t)), is convex.

Exact endpoint certificates (verified against all 16 stopping-event subsets in all six rows with fractions.Fraction):
L_D6(J(0))=1/2; L_D6(J(17/63))=40/63;
L_K1(J(17/63))=40/63; L_K1(J(1))=4/7.

On [0,17/63], convexity of L_D6 and its endpoint chord bounds R_bank<=40/63. On [17/63,1], convexity of L_K1 and its endpoint chord does the same. Both opposite endpoints have STRICTLY smaller risk; thus the chords give strict inequalities for every t other than the junction t*.

At t*, all ten risks in bank order (D1,D2,D3,D4,D6,D7,D8,K1,K2,K3) are exactly
**(1,1,1,1,40/63,1,1,40/63,277/315,46/63)**.
The full original six-preparation stopping-event witnesses are in RUN_EDGE_EVIDENCE.json; every decoder has L_D(J(t*)) >=40/63. Hence equality holds only at t*, finishing the all-real theorem. The excess over the S18 bank's finite-witness bound 4/7 is exactly 4/63.

A smaller rational witness J(1/4) has R_bank=5/8, exceeding 4/7 by 3/56. Neither 1/4 nor 17/63 belongs to the binary or ternary coordinate grids. Consequently a full pass on those finite grids does not extend this particular S18 bank's 4/7 upper guarantee to all real eleven-parameter policies.

## Scope and next scientific dependency

The predecessor's exact minimax 4/7 on its **18 fixed witnesses** remains valid. The present 40/63 is a counterexample to one concrete bank's continuum 4/7 guarantee, not a bank-independent lower bound on full ten-decoder optimization; the previously established mother interval [1/2,2/3] for k=4,6 is unchanged. Next: add J(17/63) to S18, allow the three free kernels to vary over all real stochastic rows and obtain a new sharp S19 primal/dual certificate; in parallel seek a bank covering J([0,1]) while preserving S18.

P000, the ACTIVE six-axis discrete Cell worldview, the native three-dimensional slice and separately typed time are retained as project premises; this S23 auxiliary result is not automatically a native geometric or physical theorem.
