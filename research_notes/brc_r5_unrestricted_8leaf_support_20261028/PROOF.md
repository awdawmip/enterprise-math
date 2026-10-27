# R5 — Unrestricted eight-leaf BRC likelihood-ratio support separation

Date: 2026-10-28 (Asia/Shanghai). Author-level provenance: EM-R5-LOCAL-20261028-T11; this is not a Source-issued session/CLAIM or independent Driver review. Mathematical status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Source freeze and scope

At startup, GLOBAL_KNOWLEDGE_V1 canonical main was verified at a935c2321a618259b517ed476e73b3b0d81fca60. Both global entry files, the active P000 worldview, mathematical/code rules, BRC preference and research activity policy were loaded at that immutable version. Enterprise Math was separately pinned to 9b67d426c1eaed49ed517342e0b4a226ca572b6d, including AGENTS.md, P000 V5, native X6/time, joint relation observer preservation and PORTABLE_RESEARCH_PROTOCOL.md. This result advances the exact predecessor research_notes/brc_r5_fanin_bilinear_rank_20261027_t11/PROOF.md at that project source pin.

The model is an EXTERNAL double-measure finite sequential observation tree. BRC is used for positive rational P/Q branch transport and retained ordered path identities. The signed supporting functional is readout algebra, not positive BRC mass. X6 is used only as an explicit ordered-path encoding, not as a claimed native dynamical law. No P000 or physical truth is modified.

## Unrestricted positive rational model

Let R=P/Q. At t=1, Q(A)=Q(B)=1/2 and R_A=1/2,R_B=3/2. At t=2, under A, conditional Q masses of U,V are (1/3,2/3) with P/Q multipliers (2,1/2); under B, Q masses are (1/2,1/2) with multipliers (2/3,4/3). Thus R_AU=R_BU=1, R_AV=1/4 and R_BV=2. At t=3 every t=2 history has two Q-equiprobable leaves; conditional P/Q multipliers for AU are (1/4,7/4) and for AV,BU,BV are (1/2,3/2). Each pair has Q-mean one. The eight distinct terminal LR values are {1/4,7/4,1/8,3/8,1/2,3/2,1,3}. All eight P and Q leaf masses are positive, and the P and Q totals are each one.

At t=1 and t=2 all histories may freely choose stop-and-declare-P, stop-and-declare-Q or continue. At t=3 each terminal may freely declare P or Q. Full-history policies distinguish every history. Seedless LR policies share a local distribution at equal (time,R); the ONLY nontrivial shared signature is AU and BU at t=2, and persistent common random seeds are not allowed.

Set O=(e_P,e_Q,T_P,T_Q)=(P[declare Q],Q[declare P],E_P tau,E_Q tau).

## Reusable one-collision Bellman lemma, valid for all real local randomizations

For any signed four-direction lambda=(a,b,u,v), define stop costs at node h and time t:

S_t^P(h)=b Q(h)+t(uP(h)+vQ(h));
S_t^Q(h)=a P(h)+t(uP(h)+vQ(h)).

For h=A,B let K_h^P,K_h^Q,K_h^C denote the three possible action costs at hU, where C includes optimal t=3 declarations; let W_h denote the optimum at hV. Let L_h=min(S_1^P(h),S_1^Q(h)). Then

(1) V_full(lambda) = sum_h min{ L_h, W_h+min_d K_h^d },

(2) V_LR(lambda) = min_{d in {P,Q,C}} sum_h min{ L_h, W_h+K_h^d }.

Proof. The t=3 signatures are all distinct, so their declarations optimize independently. Each hV has its own t=2 signature, and optimizing it gives W_h. In the full class each hU action may optimize separately, yielding (1). In the seedless LR class the action at AU and BU must be common, yielding (2) after the two t=1 roots optimize separately. Every trajectory visits any (time,R) signature at most once. Consequently the signed expected cost is multi-affine in independent local action probabilities and attains its minimum at a deterministic vertex of the product of action simplices. Hence (1)-(2) characterize the GLOBAL optima for all real seedless behavioral policies and all real full-history behavioral policies, not just deterministic policies. The gap is strictly positive exactly when no shared gate action attains both independent root optima after optional t=1 stops. QED.

## Exact signed separating direction

Take lambda=(-20,-10,-2,3). The exact t=2 node action costs are:

| t=2 history | stop P | stop Q | continue with optimal terminal decisions |
| --- | ---: | ---: | ---: |
| AU | -4/3 | -3 | -13/4 |
| AV | -5/3 | 0 | -5/6 |
| BU | -2 | -9/2 | -17/4 |
| BV | -3 | -21/2 | -43/4 |

At t=1, A has stop costs -4,-4; B has -5,-15. Under full history, A's optimal continuation is -13/4-5/3=-59/12, B's is -9/2-43/4=-61/4; both beat stopping. Therefore V_full=-121/6.

Fixing shared AU/BU action to P, Q, C in the seedless LR class gives GLOBAL root costs -19, -239/12, -239/12 respectively, with all earlier stops and all later declarations optimized. Thus V_LR=-239/12 and

**V_LR - V_full = 1/4 > 0.**

A full optimal policy continues at t=1 A/B, continues at AU, stops P at AV, stops Q at BU, continues at BV; declares (P,Q) at AU's two terminals and (Q,Q) at BV's. Its exact four-vector is

O_full=(43/48,5/12,8/3,29/12); lambda dot O_full=-121/6.

An LR optimal policy continues at t=1 A/B, stops Q at AU/BU, stops P at AV, continues at BV and declares Q at both BV terminals. Its vector is

O_LR=(11/12,1/3,5/2,9/4); lambda dot O_LR=-239/12.

Therefore every real seedless LR policy satisfies the unrestricted supporting inequality

**20 e_P + 10 e_Q + 2 T_P - 3 T_Q <= 239/12,**

while the full-history witness gives 121/6 = 242/12. Hence O_full is outside conv(O_LR), and this exact eight-leaf tree is excluded from the target equal-hull/unequal-image mother-question candidate set. This is an unrestricted result; it does not assert that the previously studied fixed-slice barycenter remains globally unattainable.

## Exact enumeration, alias control and computational evidence

Raw deterministic history tables: 3^2 times 3^4 times 2^8 = 186624. Raw seedless LR tables: 3^2 times 3^3 times 2^8 = 62208. Decisions on unreachable descendants produce duplicates. Each t=2 node has 2 stopped alternatives plus 4 pairs of continued terminal declarations, yielding 6 effective t=2 options. Each full t=1 root has 2 stops or 6^2 continued choices, giving 38^2=1444 reduced full tables. The shared AU/BU gate has 2 common stops or 16 joint continued terminal patterns (18 options); each root then has 2 stops or 6 unique-V continued options (8), giving 18*8*8=1152 reduced LR tables.

Exact Fraction enumeration gives 1402 distinct full four-vectors and 754 distinct LR four-vectors; all LR vectors occur in the full set. The program VERIFY.py independently checks positivity, normalization, collision and distinct terminal signatures, all counts, exhaustive signed support minima, witnesses and the analytical Bellman table. Literal output is in EXACT_OUTPUT.txt and ends ALL EXACT CHECKS PASSED. Enumeration covers every deterministic policy by reachability reduction. The all-real inequality additionally uses the multi-affinity proof.

## Native interpretation and research status

Fix one chart-relative Cell in the six-axis X6 affine torsor. Encode first A/B by E1/E2, second U/V by E3/E4, and final lower/higher outcomes by E5/E6; preserve ordered history and P/Q mass. Each primitive step follows exactly one native axis; time t=1,2,3 is separately typed. LR aggregation identifies AU and BU although their future kernels differ: that is a structural observer residual. This does not prove a heartbeat physical propagation law.

During this run the native Enterprise Math task inventory request returned CONTROL_QUOTA. The Source owner, formal CLAIM, native Result and independent Driver admission are therefore not established. This author-level portable research deliverable is UNREVIEWED / NOT_ADMITTED. Next: develop an exact signed cone-cover test for all lambda in R^4 from (1)-(2), apply it to a DISTINCT positive rational t=2 fan-in tree, then attempt all-real image nonmembership only after proving complete hull equality.
