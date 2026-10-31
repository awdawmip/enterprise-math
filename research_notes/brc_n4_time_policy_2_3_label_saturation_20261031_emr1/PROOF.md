# BRC N=4 time-only minimax: two or three policy labels cannot improve the blind decoder

Date: 2026-10-31. Status: AUTHOR_EXACT_FINITE_PROOF / EXECUTED_INTEGER_CERTIFICATE / UNREVIEWED / NOT_ADMITTED. This is a theorem in the stated finite positive BRC N=4 experiment, not P000 native physical dynamics.

## Exact input and game

The six typed prepared LR-cell distributions are the rows of

    M = 1/20 * [
      [10,10,0,0,0,0], [9,11,0,0,0,0], [0,0,20,0,0,0],
      [0,0,0,10,10,0], [0,0,0,2,18,0], [0,0,0,0,0,20]
    ].

The cells are (AU0,AU1,AV,BU0,BU1,BV), with fair future K and strictly positive original P/Q sixteen-leaf input weights, explicitly reconstructed in VERIFY.py. AV and BV duplicated P/Q normalized rows give eight original preparations but only six distinct rows.

There are exactly 2048 deterministic lawful S23 time policies H, specified by 2 stage-one A/B continue bits, 3 stage-two bits (AU and BU tied, AV, BV), and 6 third-stage LR-history stop bits. The public output T is one of {1,2,3,4}. Let K_H be the corresponding 6x4 Markov kernel.

Choose an arbitrary 6xk row-stochastic common encoder E BEFORE selecting H; choose a label map L(H) taking at most m values, and a kx4 row-stochastic decoder D_l for each label. L may know the complete ex-ante policy table but not the realized preparation, outcome or encoder coin. Define

    R_(k,m) = inf_(E,L,D_1,...,D_m) max_(H deterministic S23) max_(i=1,...,6)
              TV( (M K_H)[i,.], (E D_(L(H)))[i,.] ).

All stochastic cross-source encoders and decoders are permitted. This differs from a decoder given the complete H.

## Theorem

For every integer k>=1:

    R_(k,1) = R_(k,2) = R_(k,3) = 3/4,
    2/3 <= R_(k,4) <= 3/4.

The lower bounds also hold for any larger lawful policy family containing the 64 constructed deterministic S23 witness policies; the uniform decoder upper bound holds for any stochastic time-output law. S2 membership of ALL these 64 S23 witnesses is a separately open grammar audit, not asserted.

## 64 exact lawful witnesses

Enumerate all 2^2 * 2^3 * 2^6=2048 declared S23 bit tables. The time of typed cell c is 1 if its A/B first-stage bit is STOP; else 2 if its AU/BU-tied or AV/BV second-stage bit is STOP; else 3 if its corresponding LR-history bit says STOP; else 4.

Keep the policies with equal stop times on AU0/AU1 and on BU0/BU1. Each such policy makes the four prepared classes (AU,AV,BU,BV) emit exact point-mass time distributions for BOTH P and Q, including AU_Q, AV_Q, BU_Q and BV_Q. Taking distinct ordered source-time signatures s=(t_AU,t_AV,t_BU,t_BV) gives a set S of exactly 64 signatures, including (1,1,1,1). The checker computes and retains a legal policy bit-table witness for each signature.

## General radius-to-Cartesian-box reduction

For each label l and each of those four fixed prepared inputs j, the decoded time law q_j^l=(E D_l)[i(j),.] is a fixed 4-atom probability vector, independent of H. If signature s is assigned label l, then

    TV(delta_(s_j), q_j^l) = 1-q_j^l(s_j).

Suppose the common maximum error were strictly less than 3/4. Then for every j, q_j^l(s_j)>1/4. At most three coordinates of a probability vector can be strictly greater than 1/4. So all signatures assigned label l lie in a Cartesian product of four subsets, each having at most 3 of the 4 time atoms. Every such box lies in an omission box

    B_e = {s in S : s_j != e_j for all j}, e in {1,2,3,4}^4.

The checker exhausts all 4^4=256 omission boxes, all their 27,949 distinct pair-union masks and every third possible box. It proves the exact finite identity

    max_(e,f,g) |B_e union B_f union B_g| = 63 < |S|=64.

Thus THREE OR FEWER policy labels cannot give error strictly below 3/4, irrespective of k or how E mixes source states. The universal stochastic-encoder quantifier is analytic here, not verified by a finite encoder grid.

If instead the error were strictly less than 2/3, each fixed decoded q_j^l could have more than 1/3 probability on at most two time atoms. Each label then covers a subset of one 2x2x2x2 time box. The checker exhausts all binom(4,2)^4=1296 such boxes and proves: each meets S in at most 16 signatures; exactly nine boxes meet S in 16 signatures, and all nine have AU allowed times {3,4}. Covering all 64 signatures with four labels would require four disjoint boxes of size exactly 16, but none of the nine covers (1,1,1,1). Hence four labels cannot achieve error strictly below 2/3. This proves R_(k,4)>=2/3.

The mask enumeration is complete, finite, deterministic integer arithmetic. Its actual output is saved in RUN_EVIDENCE.txt. The finite checker proves the stated finite combinatorial sublemmas conditional only on its explicit policy grammar; it does not claim a Lean kernel check or independent scientific review.

## Matching universal upper bound

Decode every code and label to u=(1/4,1/4,1/4,1/4). For any time law p,

    TV(p,u)=1-sum_t min(p_t,1/4)<=3/4.

Therefore R_(k,m)<=3/4 for every k,m, for every deterministic or randomized lawful time-output policy. The lower bound closes equality for m=1,2,3. No P000 X6 or external physical observation is inferred.

## Information scope and continuation

The result quantifies loss of future-operation side information, separate from stored-source-state compression. In particular, the prior author-side full-policy decoder result R_ad(2)=R_ad(3)=1/2 contrasts sharply with R_(k,2)=R_(k,3)=3/4. Realized-outcome or preparation-dependent labels are outside this theorem.

Next: solve R_(2,4), R_(3,4) within [2/3,3/4] and verify the exact native S2 causal grammar membership of the 64 witnesses. A typed P000 six-axis Cell and independent-time observer/future-operation bridge remains separately open.

## Provenance / permission

Frozen GLOBAL_KNOWLEDGE_V1 current main read: awdawmip/chatgpt-global-knowledge@a5ce32dac233e1f9b61031f26acc58e391849a57; ACTIVE worldview and canonical router loaded. Frozen Enterprise Math canonical project input: awdawmip/enterprise-math@6efa6699766c16e524ae429ca3f78b043b928750; P000 V5 original blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488, typed time/joint observer policies and portable research protocol read. Earlier global startup P000 V4 projection points to a different historical blob; the current project original was used for material native semantics.

Finite model predecessor: commit d0cf6aea82934f052e931c411f384fa8b921027a, research_notes/brc_n4_time_only_policy_blind_gap_20261031_emr1/PROOF.md and VERIFY.py, pending independent review on PR #1757.

As of 2026-10-31, native Enterprise Math 0.6.11 reports research_authority_granted=false and active job quota 5/5; the owner inventory request returned CONTROL_QUOTA. Thus current formal active owner is not confirmed. This work is an author-side portable research artifact, NOT a native CLAIM, Result, independent review, Working Truth or Foundation admission.
