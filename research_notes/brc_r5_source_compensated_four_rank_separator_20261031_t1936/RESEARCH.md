# R5 — a full-rank four-observer obstruction on an exactly source-compensated time model

Date: 2026-10-31 (Asia/Shanghai). AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is an auxiliary finite stochastic stopping model, not a native X6 or admitted mother-theorem result.

## Frozen provenance and authority

Account-level GLOBAL_KNOWLEDGE_V1 canonical main: 9c204606f700d04b93ca9cb1e422085a2420b183; verified 00_BOOTSTRAP.md, OPERATING_MANUAL.md, ACTIVE worldview, P000 routing, mathematical/BRC policy. Enterprise Math canonical main: 3244d13af5ec26808eac8494504988f414cddc6e; verified p000_reality_foundation.json, current autonomous-research and portable-research protocol, joint-observer preservation. Scientific predecessor, still author-side and not independently admitted: fe9bc384a1368e5eadd08ada606c8c4297770eb0:research_notes/brc_r5_c_to_l_time_rigidity_20261031_t1840/SOURCE_SPECIFIC_EXTENSION.md. It proves an all-real two-time compensation theorem; the present verifier separately checks the finite rational time-hull at the selected parameter pair.

BRC reuse: REUSE_APPLIED to positive, origin/path-labelled Q-cylinder mass with P=likelihood*Q; source/history is retained before the (e_P,e_Q,T_P,T_Q) observer. The source-by-action contrast is a typed BRC information-loss witness for the future error observable, not an additional X6 spatial axis or a physical law. Source control at intake advertised research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED and native active job quota 5/5. No Source owner, CLAIM, Result or independent Driver review was obtained.

## Exact process and policy sets

At A=(t=1, LR=1), two hidden origins i=0,1 each have Q=P prior mass 1/2. A STOP ends at t1. Otherwise Q at t2 routes with strictly positive conditional masses (alpha_i,1-2alpha_i,alpha_i) to D, C, Y at likelihoods (1/2,1,3/2); the corresponding conditional P masses are (alpha_i/2,1-2alpha_i,3alpha_i/2). D STOP ends (t2, LR1/2); D CONTINUE Q routes 2/3 to terminal (t3,LR1/4) and 1/3 to common L=(t3,LR1). Y STOP ends (t2,LR3/2); Y CONTINUE routes 1/2 to terminal (t3,LR2) and 1/2 to common L. C has no agent action: it naturally STOPs (t2,LR1) with probability 1-kappa_i or enters the same L with kappa_i. At L STOP ends at t3, CONTINUE ends at t4. All P leaf masses are exact LR times Q mass, with per-origin Q=P mass 1/2 for every policy. The natural parameter domain is 0<alpha_i<1/2 and 0<kappa_i<1.

FULL has 12 independent deterministic bits: A/D/Y for each origin, and L for each incoming C/D/Y route and origin. Seedless LR has just four common bits (A,D,Y,L) tied to observed (time, LR), with no persistent random seed. Their real behavioural extensions choose local probabilities. Keys are never revisited, so a linear functional reaches its maximum at deterministic bits. Both classes use one identical, fixed source/path/action-dependent terminal error probability r, not an additional decision. Define O=(e_P,e_Q,T_P,T_Q) with e_Law=E_Law[r], T_Law=E_Law[terminal time].

## Theorem A — all-real A-source error classification

If the terminal error response depends only on origin i and A action (STOP: u_i, CONTINUE: v_i), with 0<=u_i,v_i<=1, put d_i=v_i-u_i. For any legal natural kernels and real behavioural policy probabilities, the FULL e_Q image is exactly the interval with endpoints [min(u_0,v_0)+min(u_1,v_1)]/2 and [max(u_0,v_0)+max(u_1,v_1)]/2. The LR e_Q image is the interval between (u_0+u_1)/2 and (v_0+v_1)/2. Their positive e_Q support gap is exactly

Delta_plus(e_Q) = (|d_0|+|d_1|-|d_0+d_1|)/4.

Both actual e_Q images (and their convex hulls) agree iff d_0*d_1>=0. For strict opposite signs the FULL/LR four-observer convex hulls cannot agree, regardless of the time-hull geometry.

Proof: The fixed per-origin Q mass yields e_Q=[u_0+u_1+d_0*a_0+d_1*a_1]/2. FULL independently chooses a_0,a_1 in [0,1], while LR requires a_0=a_1. Optimize the two linear functions; use max(0,x)=(x+|x|)/2. The same monotonicity establishes the minimum endpoints and the iff. Each conditional downstream Q path integrates to one, so cannot affect this formula. For u_0=1/2-delta, v_0=1/2+delta, u_1=1/2+delta, v_1=1/2-delta with 0<delta<1/2, the gap equals delta. QED.

## Theorem B — strict interior, four-rank and separation at theta=11/2

Choose (alpha_0,kappa_0)=(1/4,3/4), (alpha_1,kappa_1)=(1/5,1/6). Both have theta_i=[1+kappa_i*(1-2alpha_i)]/alpha_i=11/2, although the source transition kernels differ. The previous analytic theorem implies equal ACTUAL two-time FULL/LR real behavioural images at these parameters; our exact checker verifies that all 4096 FULL deterministic time vectors lie in the 16-policy LR rational time polygon.

Let a be the historical A action; let sigma(i,a)=+1 for origin0 with A CONTINUE or origin1 with A STOP, and -1 otherwise. For each final terminal history, assign the same error probability to both strategy classes:

r(i,a,route) = 1/2 + (1/4)*sigma(i,a) + (1/64)*1_{route=A_STOP} + (1/32)*1_{route=D_STOP}.

The final-leaf r lies in [1/4,25/32]; success and error have strictly positive probabilities. No new policy information is given to LR.

For e_Q support, FULL optimally CONTINUEs A in origin0, with D STOP, obtaining origin0 conditional mean 3/4+(1/32)*(1/4); FULL STOPs A in origin1, obtaining origin1 conditional mean 3/4+1/64. Therefore

sup_FULL e_Q = 3/4+(1/2)*[(1/32)*(1/4)+1/64] = 195/256.

For LR the source/opposite-action baseline cancels. Shared A STOP yields 1/2+1/64=33/64. Shared A CONTINUE (with optimal D STOP) yields 1/2+(1/32)*(alpha_0+alpha_1)/2=1/2+9/1280, strictly smaller. Hence

sup_LR e_Q = 33/64,  Delta_eQ = 63/256 > 0.

A legal FULL witness using 12-bit policy (1,0,0,0,0,0,0,0,0,0,0,0) has O=(389/512,195/256,27/16,27/16). Since all y in conv(O_LR) satisfy y_eQ<=33/64, its infinity-norm distance to that ENTIRE convex hull is at least 63/256. This is an exact signed-support/Farkas-style separation, not just a finite-grid nonmembership.

The LR hull nevertheless has full affine rank 4. Index the 4-bit LR policies lexicographically as (A,D,Y,L); the observations for indices 0,8,9,10,12 respectively are:
0: (33/64, 33/64, 1, 1);
8: (1289/2560, 649/1280, 179/80, 179/80);
9: (1289/2560, 649/1280, 99/40, 99/40);
10: (1289/2560, 649/1280, 103/40, 197/80);
12: (1/2, 1/2, 47/20, 197/80).
The determinant of the 4x4 matrix of differences from row 0 is exactly -1539/1048576000, nonzero. Thus this strictly positive, time-compensated, four-rank candidate STILL FAILS four-hull equality. QED.

## Actual reproducible verification and scientific limits

VERIFY.py uses standard-library Fraction arithmetic and enumerates all 4096 FULL and 16 LR deterministic policies; each policy checks both laws' normalization and each source's mass 1/2. It checks every FULL time pair inside the exact six-vertex LR time hull, all coordinate supports, the four-rank determinant and the explicit FULL e_Q witness. It finds 301 distinct FULL and 9 distinct LR four-observer points and prints PASS_EXACT_R5_COMPENSATED_FOUR_ERROR_SOURCE_ACTION_SEPARATOR. EXACT_OUTPUT.txt is the actual execution output; independently recomputing the 4x4 determinant in SymPy gave the same rational number, but SymPy is not needed for VERIFY.py.

Theorem A is all-real analytic for its declared response family; Theorem B is an exact-rational counterexample to four-hull equality in this explicit candidate. The predecessor's all-real actual time-set theorem remains unreviewed and is not independently re-proved here; the finite exact time-hull inclusion is rechecked. The original mother problem seeks equality of FULL/LR FOUR-hulls but inequality of their actual real FOUR-images, which is still OPEN. No native X6 correspondence, mathematical admission, independent review or protected P000/worldview update is asserted.

Next: restrict terminal errors so source-by-A advantages do not oppose, retain full LR four-rank, and check all-signed four-hull equality by exact <=5-vertex LR decompositions or separating hyperplanes. Only if four-hull equality holds investigate real LR nonmembership semialgebraically.
