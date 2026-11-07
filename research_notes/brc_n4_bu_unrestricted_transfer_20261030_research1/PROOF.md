# BRC N=4 BU: complete S2/S23 causal minimax — model-preserving composition theorem

2026-10-30. AUTHOR_ANALYTIC_PROOF / EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED.
Scope: strictly positive external 16-leaf P/Q dual-probability BRC model; complete terminal O=(T,Decision,Z_BU); original instantaneous behavioral S2 and S23 policy classes. Not an assertion of physical P000 X6 geometry or time dynamics.

## New mathematical increment

The two previously established author-side proofs below have *exactly matching* mathematical models and compatible domains. Earlier source II confined its minimax equality to a five-real-variable common conditional-rate class F, and explicitly left transfer to all original S2/S23 causal policies open. Earlier source I had already proved that transfer. This note closes that logical gap at a=961/1000, b=151/1000 by verifying the two statements compose without changing observable, hypothesis, quantifiers, information sets or probability law.

**Theorem:** For every legitimate real instantaneous behavioral competitor in the original S2 and S23 classes (under their explicit information-set semantics in Appendix I), the exact globally attained two-law minimax of the FULL terminal observer is

 d2(961/1000,151/1000) = d23(961/1000,151/1000)
     = sqrt(26521161)/15000 - 413/1250
     ≈ 0.012924666557278792.

This is NOT merely the value restricted to common-rate strategies chosen in advance; that class is shown below to be sufficient to minimize over ALL original S2/S23 strategies. Target F itself need not be S2-admissible.

## Bridge proof and checks

1. Define K on observed triples: if T=1 or 2, keep T, force decision Q and BU-bit 0; if T=3 or 4, output (3,Q,1) when the BU-bit is 1, else output (3,P,0). The stipulated target F is K-fixed for P and Q. Given any legal original S2 competitor G, preserve the first- and second-time conditional continuation kernels, force the early decisions to Q, and stop at time 3 with decision Q on BU histories and P elsewhere. At time 3 BU likelihood ratios {1/5,9/5} are disjoint from all nonBU ratios {9/10,11/10,1/4,2}, so the resulting decision is a lawful current-likelihood-ratio-measurable S23 action. The equal AU/BU stage-two kernel is preserved; time four is not reached. This produces for both L=P,Q an EXACT measure identity Law_L(O_(G^K)) = K_push Law_L(O_G), therefore the two-law TV cannot increase. Together with S23 subset S2 it yields d2=d23. The source proof, including all 16 leaves and boundary cases, is reproduced verbatim in Appendix I.

2. For the compressed G^K, A,B are the first-stage continuation probabilities, c is the common AU/BU SECOND-STAGE CONDITIONAL continuation probability, U=A times the AV conditional continuation rate, V=B times the BV conditional continuation rate. All and only tuples satisfying 0<=A,B,c<=1, 0<=U<=A, 0<=V<=B are realized by legal S23 policies. Zero A/B histories give U/V=0 respectively; set arbitrary legal unreachable conditional rates. This is exactly Appendix II's common-u class, with II's u = I's c. In particular, the expression AU=BU=u in II denotes common CONDITIONAL NODE continuation rates; it is not the algebraic multiplication of the variables A and U.

3. The four observable atoms are (1,Q,0),(2,Q,0),(3,P,0),(3,Q,1). For candidate minus target, define
 P1=(a-A+3(b-B))/4, Q1=(a-A+b-B)/2;
 P3=(A*c-a)/6+U/12+V/2, Q3=(A*c-a)/6+U/3+V/4;
 P4=Q4=B*c/4, P2=-P1-P3-P4, Q2=-Q1-Q3-Q4.
These are derived from all 16 strictly positive leaves. Appendix I instead uses TARGET minus candidate signed vectors, so its DeltaP and DeltaQ are exactly the negatives of the above. VERIFY_BRIDGE.py checks this entire symbolic opposite-sign identification independently from appendix derivations. Thus the four-atom TV objective and the feasible domain in I and II coincide exactly, including P/Q, z and boundary semantics.

4. Appendix II gives three direct legal measurable-event Farkas certificates J,h,K_dual. They are nonnegative convex mixtures of full-observer signed-event masses with an optional nonnegative feasible slack mu(B-V). Writing c for the shared continuation rate, J(c)=(1730-2883c-1414c^2)/[2000(23-2c)] on [0,171/500], h(c)=c(961-1414c)/[2000(7-2c)] on [0,1], K_dual(c)=151c/[1000(4+c)] on [0,1]. Let r=(sqrt(26521161)-4091)/2828; 171/500<r<239/638. J is decreasing until 171/500, h is concave between 171/500 and r, K_dual is increasing from r; both J and h at 171/500 exceed 517/40000, which exceeds the proposed optimum; h(r)=K_dual(r)=e*. Therefore all real c in [0,1] have e>=e*.

5. At c=r choose A=(1414r+1033)/[250(7-2r)], B=(961-1414r)/[500(7-2r)], U=(1+r)B, V=B. The exact root interval implies 0<A,B<1 and 0<U<A, 0<=V=B. Together with the source-I time-three lawful decisions this is a genuine original S23 strategy. Its full signed P vector is (0,0,-e*,e*) and Q vector (-e*,0,0,e*), so both full-observer TV equal e*. The global lower bound matches an attained legal original strategy. QED.

No circular reliance is introduced: I establishes the reduction for arbitrary original policies at all real a,b without assuming the optimization; II proves the optimizer within the fully specified reduced domain using the raw 16-leaf observer events, independently of I; the present bridge merely identifies the domains and signs. The full proof bodies are below for self-contained audit.

## New independent execution and limits

The new VERIFY_BRIDGE.py (executed locally with exact SymPy) checked the source-I signed mass vector against the NEGATIVE of source-II's vector for all real symbolic A,B,c,U,V, verified root p(r)=0 and both laws' eight exact radical attaining atom equalities. Its output is in VERIFY_BRIDGE_EVIDENCE.txt. An additional 2026-10-30 author-side raw-leaf script also executed exact tests on 24 lawful S2 policies x both probability laws, K pushforward / two-TV contraction and three symbolic Farkas certificates; full code and evidence are retained in the local user artifact archive. These finite checks do not establish the theorem independently of the universal proof.

This compositional completion remains AUTHOR-side, not independent research review. Persistent hidden random states that violate the specified conditional time-two information-set equality, enlarged observers with future operation, alternative BU labeling, P000 six-dimensional Cell, its three-dimensional slice and independent time dynamics are NOT covered; they demand separate observer-fidelity and model-embedding results. Original Site status: research_authority_granted=false; no native task owner confirmed, CLAIM, Result or independent Driver approval inferred from GitHub publication.

Exact frozen inputs: GLOBAL_KNOWLEDGE_V1 main@f2889be41a071bfaea238c10d71e9a63915d4ebb, Enterprise Math main@e69c62b9fbad1edb4cfc5cfeaad33b7a0e4de2a3; P000 original/projection Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches.

---
## Appendix I — Original full causal S2/S23 reduction, unchanged source

Source commit 1a4898a57e952245eeacb38be7adf109faa49f49; research_notes/brc_n4_bu_full_causal_reduction_audit_20261029_r1t11/PROOF.md

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


---
## Appendix II — Exact minimax inside common conditional-rate family, unchanged source

Source commit d626df0a971cd19518303dd5bf4728daf478fcc6; research_notes/brc_n4_bu_common_u_exact_minimax_20261030_r11/PROOF.md

# BRC N=4 BU: exact global minimax for the common-continuation policy family

2026-10-30, author-side analytic theorem. Scope: strictly positive external 16-leaf P/Q source model; retained terminal observer (T,Decision,Z_BU); fixed a=961/1000, b=151/1000. Status: EXACT_SYMBOLIC_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Exact claim and scope
Let F contain ALL real stochastic policies with stage-one probabilities A,B in [0,1], common second-stage AU=BU=u in [0,1], AV surviving mass U in [0,A], BV surviving mass V in [0,B]. Conditional AV and BV probabilities are U/A and V/B (zero-mass histories arbitrary). Set e=max(TV_P,TV_Q) for the FULL terminal observer.

**Theorem (without inherited L0/L3 or S2->S23 assumptions).**
min over F of e is exactly

  e* = sqrt(26521161)/15000 - 413/1250
     = 0.012924666557278792...

This is the exact minimax of F, not yet the unrestricted d2/d23 minimax. To transfer it to all admissible original causal policies requires a separately established lossless representation/reduction to F.

## Original complete source probabilities
For c=AU,AV,BU,BV, respectively, the Q source masses are 1/6,1/3,1/4,1/4. Each has four strictly positive leaves (j,k) in {0,1}², with Q(c,j,k)=q_c/4 and P(c,j,k)=q_c * likelihood(c,j)/4. Likelihood pairs: AU=(9/10,11/10); AV=(1/4,1/4); BU=(1/5,9/5); BV=(2,2). Both P,Q normalize to 1. The target stage-one probabilities are (a,b), second-stage rates (AU,AV,BU,BV)=(1,0,0,0).

The four observable atoms, with BU source-bit preserved, are 1=(1,Q,0), 2=(2,Q,0), 3=(3,P,0), 4=(3,Q,1). Let P_i and Q_i denote candidate-minus-target signed mass. Exact leaf aggregation yields

 P1=(a-A+3(b-B))/4;  Q1=(a-A+b-B)/2;
 P3=(Au-a)/6+U/12+V/2;
 Q3=(Au-a)/6+U/3+V/4;
 P4=Q4=Bu/4;
 P2=-P1-P3-P4;  Q2=-Q1-Q3-Q4.

For any observer event S subset of {1,2,3,4}, its signed difference P_S or Q_S is <= the corresponding TV. Consequently every convex combination of such events, minus mu*(B-V) for mu>=0, is <= e.

## Three *direct full-observer* Farkas certificates
Use bitmask event notation: P8={4}, P9={1,4}, P10={2,4}, P11={1,2,4}; Q9={1,4}, Q12={3,4}, Q13={1,3,4}, Q14={2,3,4}. All sums below expand identically to functions independent of A,B,U,V.

EARLY J: events (P10,P11,Q9,Q13) have weights
 [2(u²-2u+7), 2(1+4u-u²), 3-7u, u+4]/(23-2u),
 mu=7(u+4)/[4(23-2u)].
 The weights sum to 1, are nonnegative for 0<=u<=171/500, and
 e >= J(u)=(1730-2883u-1414u²)/[2000(23-2u)].

MIDDLE h: events (P8,P10,P11,Q12) have weights
 [7(1-u), 2u², 2u(2-u), u]/(7-2u),
 mu=7u/[4(7-2u)].
 All weights nonnegative for 0<=u<=1, sum to 1, and
 e >= h(u)=u(961-1414u)/[2000(7-2u)].

LATE K: events (P8,P9,Q14) have weights
 [2(2-u),2u,u]/(4+u), mu=0.
 All weights nonnegative for 0<=u<=1, sum to 1, and
 e >= K(u)=151u/[1000(4+u)].

Every event is legitimate in the stated full observer. The expressions and multipliers are **new verified algebraic dual certificates**, not an appeal to inherited author-side L0/L3.

## Global proof for every real u in [0,1]
Let u0=171/500, p(u)=1414u²+4091u-1730, and r=(sqrt(26521161)-4091)/2828. Since p'(u)=2828u+4091>0, p(u0)<0, p(239/638)>0, the sole positive root r lies in (u0,239/638). Let t=517/40000=0.012925. Integer inequality 26521161 < (5149875/1000)² proves e*<t. Exact checks give
 J(u0)=72328363/5579000000 > t;
 h(u0)=20409363/1579000000 > t.

- For 0<=u<=u0, J'(u)=(2828u²-65044u-62849)/[2000(2u-23)²]<0. Therefore e>=J(u)>=J(u0)>e*.
- For u0<=u<=r, h''(u)=6979/[125(2u-7)³]<0. Its concavity gives h(u)>=min(h(u0),h(r))=e*, using the exact polynomial identity
  h(u)-K(u)=u*p(u)/[2000(u+4)(2u-7)].
- For r<=u<=1, K'(u)=604/[1000(4+u)²]>0, so e>=K(u)>=K(r)=e*.

The intervals exhaust every real 0<=u<=1. This is not a finite grid, a floating-point LP optimum or a conditional missing-event inference.

## Matching legitimate strategy and exact TV under both laws
Set u=r and
 A=(1414u+1033)/[250(7-2u)],
 B=(961-1414u)/[500(7-2u)],
 U=(1+u)B, V=B.
From 0<r<239/638 we get A,B>0,
 1-A=3(239-638u)/[250(7-2u)]>=0,
 A-U=(1105+3281u+1414u²)/[500(7-2u)]>0,
 and 0<=V=B<=1; hence AU=BU=u, AV=U/A, BV=1 are lawful conditional probabilities. The exact signed vectors reduce to
 P=(0,0,-e*,e*),
 Q=(-e*,0,0,e*),
because p(r)=0. Thus TV_P=TV_Q=e*, attaining the lower bound.

## Evidence and limits
The accompanying VERIFY.py checks all three universal affine-event identities with symbolic algebra, the derivative/endpoint/root certificate, and two independent rational full-16-leaf P/Q observer reconstructions. Its checked output is in VERIFY_EVIDENCE.txt. Previous author-side commit 309b4d061a164c1b2c3d9fed519cbae2822d75b9 gave the same sharp *upper bound* but not this exhaustive global lower proof within F.

Unrestricted d2/d23 equality needs an independently checked identification of the original causal information sets with F, including unreachable histories, or a lawful counterexample outside F. The original L0/L3 legality and S2->S23 transfer remain unreviewed. P000 native X6 Cell, three-dimensional slice, and independent time dynamics are separate observer-fidelity obligations. Research publication is not native Result, independent review, or mathematical admission.

Frozen input: GLOBAL_KNOWLEDGE_V1 main@a67604dbe76d4dd9bab15e6574d478c461966ad2; Enterprise Math main@aa3ced8bc134e5b3ea2219b2cc26c9f8381d5d89; preceding author-side Draft PR #1729 at 309b4d061a164c1b2c3d9fed519cbae2822d75b9. Authenticated GitHub actor awdawmip; native research authority false, owner unverified.

