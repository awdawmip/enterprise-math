# BRC N=4 BU observer: complete 16-leaf causal reduction audit

**2026-10-29 (Asia/Shanghai)** — AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_AND_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Model and exact claim

This is a theorem **inside the stipulated external finite dual-probability BRC model**, not a P000 native-X6 physical or time-dynamics result. The sixteen leaves are four time-two nodes AU, AV, BU, BV, each split into two time-three children and then two time-four daughters. At time two the Q masses are 1/6, 1/3, 1/4, 1/4 and their P/Q likelihood ratios are 1, 1/4, 1, 2. At time three the corresponding children have respective ratios (9/10,11/10), (1/4,1/4), (1/5,9/5), (2,2); each Q mass and the corresponding P mass split equally at time four. The 16 Q and P leaf masses are strictly positive and both laws sum to one.

The behavioral instantaneous randomized class S2 uses the **same conditional time-two stop/continue and decision kernel** on AU and BU (their contemporaneous likelihood ratio is 1), with separate kernels for AV/BV and earlier A/B. S23 additionally requires equality of actions at time-three/four nodes with equal contemporaneous likelihood ratios. These are conditional behavioral policies; persistent hidden random states that violate equality of the specified conditional time-two kernels are outside this claim.

The target F_(a,b), for real 0<=a,b<=1, continues at time one with probability a on A and b on B, otherwise stops and decides Q. At time two F continues AU with probability 1, stops AV,BU,BV with decision Q, and stops AU at time three with decision P. The **complete terminal observer** is O=(T,Decision,Z_BU), with Z_BU=1 if and only if a BU path reaches time three or four, and Z_BU=0 on any earlier stop.

**Reduction theorem.** For all real 0<=a,b<=1, the minimax observable total-variation distance against all S2 strategies equals that against all S23 strategies and equals the minimum of the explicitly realizable five-variable four-atom objective given below. No pre-existing four-atom reduction is assumed.

## Pathwise map and S23 realizability

Define K on the *observed tuple* O: at T=1,2 retain T and set Decision=Q, Z_BU=0; at T=3,4 replace T by 3, retain the BU bit, and set Decision=Q iff the bit is 1, otherwise P. The target satisfies K_# O_F=O_F under each of P and Q.

For **any** lawful original G in S2 (with possibly arbitrary randomized stop decisions and time-three/four continuation and decisions), define G^K by preserving the entire conditional time-one and time-two continuation kernels of G, setting every early stop decision to Q, and stopping every arrival at time three: its decision is Q on BU descendants and P on all others. At time three the BU likelihood-ratio set {1/5,9/5} is disjoint from the non-BU set {9/10,11/10,1/4,2}. Thus the terminal decision is a function of current likelihood ratio only, satisfies S23, and no time-four node is reached. The AU/BU time-two equal-likelihood conditional kernel remains unchanged.

For each law L=P,Q individually, tracing every branch gives

    Law_L(O_(G^K)) = K_# Law_L(O_G).

This is an **equality of full observed distributions**; it does not rely on discarding the BU source label. The target is K-fixed, so deterministic-map total-variation data processing gives simultaneously

    TV_L(O_F,O_(G^K)) <= TV_L(O_F,O_G),   for L in {P,Q}.

Since S23 is a subset of S2, this S2-to-S23 construction proves equality of their minimax infima. It uses a lawful concrete policy and does not introduce independent noncausal masses.

## Exact feasible parametrization and four atoms

Let A,B∈[0,1] be time-one continuation probabilities, c∈[0,1] the common AU/BU time-two continuation probability, U=A*u the AV time-two continuation mass, and V=B*v the BV time-two continuation mass. The entire feasible domain is

    0<=A,B,c<=1, 0<=U<=A, 0<=V<=B.

Every collapsed lawful policy maps into this domain. Conversely, any feasible tuple gives an actual S23 policy using u=U/A for A>0 and u=0 for A=0; likewise v=V/B for B>0 and v=0 for B=0, then stopping at time three as above. This verifies the boundary faces A=0/B=0 as well as the interior.

Under the four terminal atoms [(1,Q,0),(2,Q,0),(3,P,0),(3,Q,1)], direct summation of all 16 positive leaves gives the **target** and **collapsed competitor** probability vectors:

    Q_F = (1-(a+b)/2, a/3+b/2, a/6, 0)
    Q_G = (1-(A+B)/2,
           (A+B)/2-A*c/6-B*c/4-U/3-V/4,
           A*c/6+U/3+V/4, B*c/4)
    P_F = (1-(a+3*b)/4, a/12+3*b/4, a/6, 0)
    P_G = (1-(A+3*B)/4,
           (A+3*B)/4-A*c/6-B*c/4-U/12-V/2,
           A*c/6+U/12+V/2, B*c/4).

The four components under either law sum to one. Set

    s=(A-a+B-b)/2, t=(A-a+3*(B-b))/4, H=B*c/4,
    rQ=a/6-A*c/6-U/3-V/4,
    rP=a/6-A*c/6-U/12-V/2.

Their target-minus-competitor signed differences therefore are exactly

    DeltaQ=(s,H-s-rQ,rQ,-H),
    DeltaP=(t,H-t-rP,rP,-H).

Consequently the **fully causal**, BU-bit-preserving finite-model minimax is, for every real a,b in [0,1],

    d2(a,b)=d23(a,b)
      = min_{0<=A,B,c<=1; 0<=U<=A; 0<=V<=B}
          max(||DeltaQ||_1, ||DeltaP||_1)/2.

The minimum is attained because the parameter domain is compact and the objective is continuous. This is a reduction theorem, not a claim that the minimum's closed-form phase diagram has been solved for arbitrary a,b.

## Exact independent reconstruction and discriminating example

VERIFY.py separately constructs the 16 terminal Q/P leaf masses from the given mass/ratio tree, checks their normalization and correct first-stage marginals, constructs the observation distributions of arbitrary legal randomized policies, and symbolically recovers the two four-atom signed vectors from the underlying second-level masses. It checks deterministic K pushforward equality and P/Q data processing for 41 pseudo-random rational S2 policies (82 exact law comparisons), verifies the signed vectors for the same policies, and exercises four degenerate feasible-rate profiles. All these are exact rational or symbolic computations. They check the implementation and algebra; the continuous universal statement follows from the preceding pathwise construction and algebra, not the 41 sampled policies.

An exact lawful witness that K can **strictly** improve both losses is a=A=97/100, b=B=1/10, common AU/BU c=1/2, AV/BV continuation zero, every time-three node stopping P, every time-one stop deciding P and every time-two stop Q. Its Q-loss decreases from 131/240 to 97/1200 (gap 93/200); its P-loss decreases from 229/300 to 97/1200 (gap 273/400). Thus replacing G by G^K is not falsely presented as identity of uncollapsed observation laws.

Actual local execution output in VERIFY_EVIDENCE.txt ends with PASS_EXACT_BRC_N4_BU_CAUSAL_REDUCTION_16LEAF_AUDIT. The same verifier is published as VERIFY.py; proof independence refers to reconstruction from raw leaf masses, not to an independent human reviewer.

## Observer-fidelity and transfer limits

K discards time-four timing, decisions and path detail. It is valid for the specified **terminal** (T,Decision,Z_BU) readout and its two-law TV objective, not for arbitrary downstream operations, joint relation queries, future observation horizons, or the native six-dimensional P000 world. BU lineage is explicitly retained, and the time-three current-likelihood separation makes its decision implementable; this is an observer-scoped exact factorization certificate, not a general license to erase branch provenance. Positive masses are not signed amplitudes.

Formal project admission needs independent review of the policy-class semantics and the BU indicator at time four. P000 X6 Cell, six-axis path algebra, three-dimensional slice selection/third-coordinate semantics, and independent time-update fidelity each remain separate proofs.

## Next question and exact provenance

Next: enlarge O to include Z_AU and/or retain time-four timing, and either prove an observation-preserving sufficient repair state or exhibit the smallest lawful rational S2 strategy for which K is no longer a valid target-preserving implementation. Then use the audited reduction to analyze the still-open two-dimensional strip 97/100<=a<=99/100, 0<b<1/100. See NEXT_TASK.md.

Fixed GLOBAL_KNOWLEDGE_V1 main@99ce00fffc6ecc6426729ce702d8e787f0d336bd; Enterprise Math input main@2528561531a335c545c1312bf9a1ed16f8d0df3c. The model and former inherited dependency are described in research_notes/brc_n4_bu_2d_highb_gamma_phase_20261029_r1t11/PROOF.md at that EM source pin. Author-side portable research by this task; no service-issued claim or independent Driver verdict.
