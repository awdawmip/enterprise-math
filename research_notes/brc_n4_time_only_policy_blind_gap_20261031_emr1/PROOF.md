# BRC N=4: exact time-only decoder-quantifier gap for two, three, and arbitrary code counts

**Author-side research, 2026-10-31.** Status: AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED. This is a theorem about the stipulated finite positive-probability BRC N=4 experiment, not about P000 native six-axis Heartbeat dynamics. It continues the frozen time-only research at Enterprise Math PR #1757, commit 8e253a633dd479a87ddf31bd42eb34342b237233, including that commit's NEXT_TASK.md.

## 1. Exact input and information model

The original P/Q experiment has strictly positive weights on sixteen leaves (S,J,K) per law, with S in {AU,AV,BU,BV}, binary J, and independent fair binary K. Per-K leaf numerators over 240:

    law       AU        AV        BU        BV
    Q       (10,10)   (20,20)   (15,15)   (15,15)
    P        (9,11)    (5,5)    (3,27)   (30,30)

The six distinct normalized prepared distributions on six disjoint typed future/LR cells C=(AU0,AU1,AV,BU0,BU1,BV) are the rows of

    M=(1/20)*[
      [10,10,0,0,0,0],    # AU,Q
      [ 9,11,0,0,0,0],    # AU,P
      [0,0,20,0,0,0],    # AV,Q/P
      [0,0,0,10,10,0],   # BU,Q
      [0,0,0,2,18,0],    # BU,P
      [0,0,0,0,0,20]     # BV,Q/P
    ].

The original eight preparations distinguish P and Q also at AV and BV even where their probability rows coincide. These six cells retain source, branch and J-history identity; they are not six untyped mass totals.

The lawful causal stopping policy H belongs to either frozen family F=S23 or F=S2. Its public **time-only** outcome is T in {1,2,3,4}, with final decision and BU sensor discarded. For every lawful H, the original causal information grammar and law-independent behavior induce one common Markov kernel K_H from the six typed cells C to {1,2,3,4}. The fair future K and behavioral randomness are integrated into K_H. No hidden P/Q law identifier is supplied to H; C includes the lawful source/history information. The model retains stage-one A/B choices, stage-two AU/BU-tied choices and lawful stage-three LR-history choices. In the full S2 grammar any additional lawful randomization is treated through the same conditional kernel, not through a law-specific update.

Let k>=1. The encoder E is any six-by-k row-stochastic matrix selected before H; its output law is independent of subsequent policy selection. A decoder D_H is a k-by-four row-stochastic kernel. Define

    err(E,D_H,H)=max_(six prepared rows i) TV((M K_H)_i,(E D_H)_i).

Duplicating AV/BV rows gives the original max over eight prepared inputs. TV(p,q)=sum_t |p_t-q_t|/2. Consider the two different games

    R_ad(k)    = inf_E sup_(H lawful) inf_(D_H) err(E,D_H,H),
    R_blind(k) = inf_(E,D) sup_(H lawful) err(E,D,H).

In R_blind the **same** decoder D is used for all policies and is not given a policy label; in R_ad D_H may depend on the chosen H. An externally provided policy as decoder side information would define a different game.

## 2. Sharp theorem

For both F=S23 and F=S2, all real 0<=epsilon<=1/2, all common stochastic encoders and stochastic decoders,

    R_ad(2) = R_ad(3) = 1/2,
    R_blind(k) = 3/4 for every integer k>=1.

Thus the exact decoder-quantifier gap at k=2 and k=3 is 1/4. It persists even at k>=6, where the preceding author-side theorem gives policy-adaptive zero error: the extra 3/4 is an **absence-of-policy-information** obstruction, rather than failure to encode the preparation.

### 2.1 Policy-adaptive upper bound: an explicit two-code kernel

Encode source AU/AV by L, and BU/BV by R, for either prepared law. Decode first to the fixed typed six-cell reference laws

    D_L=(1/4,1/4,1/2,0,0,0),
    D_R=(0,0,0,1/10,2/5,1/2).

The original M shows by exact arithmetic that TV(M_i,D_{E(i)})=1/2 for **all six** normalized rows (hence all eight original inputs). For every lawful policy H, construct its decoder by pushing these two reference laws through its *same* lawful time kernel:

    D_H(L,.)=D_L K_H,    D_H(R,.)=D_R K_H.

By total-variation contraction under common stochastic postprocessing,

    TV(M_i K_H,D_{E(i)}K_H)<=TV(M_i,D_{E(i)})=1/2.

The time kernel can include fair K and lawful randomized choices. The inequality holds for real behavioral probabilities; no grid test or exchange of quantifiers is used. Thus R_ad(2)<=1/2, and ignoring a third code gives R_ad(3)<=1/2.

### 2.2 Policy-adaptive lower bound for every stochastic encoder with k<=3

For each b in {0,1}^6 take a lawful time-bit shattering policy H_b: everyone continues through stages one and two; at stage three STOP on the contemporaneously observed LR class j iff b_j=1, otherwise continue to stage four. Final decisions can be constant. All 64 H_b belong to both S23 and S2: the AU/BU stage-two action is common and identical LR histories share an action. These policies satisfy

    P_i^{H_b}(T=3)=(M b)_i.

Restrict any arbitrary six-by-k stochastic encoder E, k<=3, to the four input rows AU_Q, AV, BU_Q, BV. The resulting four-by-k submatrix has a nonzero left-null vector w. Because E*1_k=1_4, sum_i w_i=0. Extend w by zero on the two unused input rows, and set r=w^T M.

The four selected M rows have pairwise disjoint supports, so their signed combination obeys the exact L1 isometry

    sum_j r_j=0,     ||r||_1=||w||_1.

Let d_b be the k-vector whose code-z coordinate is the decoder probability of T=3 under H_b. For any reconstruction radius delta, every input's event {T=3} discrepancy is <=delta. Multiplication by w gives

    |r*b|=|w^T(M b-E d_b)|<=delta ||w||_1.

Since r has zero sum,

    max_(b in {0,1}^6)|r*b|=||r||_1/2=||w||_1/2.

Nonzero w forces delta>=1/2. The proof allows a different arbitrary stochastic decoder for every b, so the lower bound is valid with policy adaptation. Combining §§2.1-2.2 proves R_ad(2)=R_ad(3)=1/2 for *every real encoder*, including cross-source randomization.

### 2.3 Policy-blind lower and upper bounds for every k

For t=1,2,3,4, there exists a lawful policy H_t which stops **all** preparations deterministically at time t. Each uses the same first-stage A/B, stage-two AU/BU and stage-three LR actions as appropriate, so belongs to both S23 and S2.

Take arbitrary k, stochastic encoder E and a single fixed decoder D. Fix one preparation i and let q_i=(E D)_i be its decoded time law. q_i is the **same** for all four H_t, whereas their true laws are delta_1,delta_2,delta_3,delta_4. Therefore

    sup_H err(E,D,H) >= max_t TV(delta_t,q_i)
       =1-min_t q_i(t) >= 1-1/4=3/4.

This remains true for k>=6 or for any lossless source encoder, as long as it is fixed before the policy and its decoder has no policy input. Conversely assign **every** decoder row the uniform time distribution u=(1/4,1/4,1/4,1/4). Every probability law p on those four times has TV(p,u)<=3/4: the overlap sum_t min(p(t),1/4) is at least 1/4. Thus R_blind(k)=3/4 with explicit attainment for every k>=1.

**General lemma.** If an m-valued observer admits m lawful interventions that each deterministically produce a distinct observable atom for all source preparations, while a decoder must be chosen without the intervention label, then the intervention-blind reconstruction minimax radius is 1-1/m, regardless of source code count. A uniform observation decoder attains it. This is a theorem about intervention visibility and its exact quantifier order, not a claim about an intervention-aware decoder.

## 3. Actual exact arithmetic and coverage

The accompanying actually executed VERIFY.py uses Python standard-library fractions.Fraction. It reconstructs both 16-leaf positive source laws and normalizations, verifies M and the exact two-code reference TV=1/2, checks 64 lawful time-bit policies and the four all-time policies, and checks the four-source dual L1 isometry. It independently enumerates 4 first-stage A/B timing choices x 8 second-stage AU/BU-tied choices x 64 third-stage LR-history choices = **2048 deterministic S23 timing tables** and scores eight preparations each, **16384 exact rational (policy,input) comparisons**. The maximum checked errors are 1/2 for the adaptive two-code construction and 3/4 for the fixed uniform time decoder; 384 time-shattering equalities and 342 nonzero bounded-integer dual-isometry witnesses also pass. The universal stochastic-encoder theorem, real randomized S2/S23 behaviors, every integer k in §2.3, and all real epsilon are proved analytically, not inferred from those finite tests. Actual stdout is in RUN_EVIDENCE.txt.

## 4. Immutable sources, authority, transfer obligations

- Fixed GLOBAL_KNOWLEDGE_V1 canonical read: awdawmip/chatgpt-global-knowledge main@1b3be04291d29e6743f59653927608278a729014, including bootstrap, manual, original P000 and ACTIVE worldview.
- Fixed Enterprise Math canonical control read: awdawmip/enterprise-math main@d26fed9696ab2e230c7c9e8bbe64f684be6bb7ce, with applicable AGENTS, autonomous and portable-research protocols.
- Exact mathematical predecessors: research_notes/brc_n4_time_only_full_causal_r1_20261031_emr1/PROOF.md at 8e253a633dd479a87ddf31bd42eb34342b237233, and research_notes/brc_n4_time_visible_observer_staircase_20261031_emr1/PROOF.md at e30ebcffd8263842b1e6646e2fe16762a65935ce.
- Native owner query for this unit returned CONTROL_QUOTA; current service manifest states authority_granted=false. These GitHub materials are portable author-side science, not native CLAIM, Result, independent review or mathematical admission.
- This finite BRC branch/source carrier retains source, LR class, fair future K, legal stop histories and observer scope. No P000 X6 six-axis Cell rotation, triadic closure or physical-time evolution is inferred. An observer-and-future-operation-preserving native map remains a separate open proof obligation.
- Next unit: quantify how many explicit policy-class messages suffice to recover the adaptive 1/2 radius from a bounded-label strategy announcement and independently audit the full S2 common-kernel assumption (see NEXT_TASK.md).
