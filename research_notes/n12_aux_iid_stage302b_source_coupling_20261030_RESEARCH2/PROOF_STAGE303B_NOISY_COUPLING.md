# Stage303-B — Exact all-horizon error of an imperfect persistent source coupling

**2026-10-30 / PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.** Research2 author continuation of Stage302-B; external finite positive-rational BRC-style probability model. No P000-X6 native transfer, canonical Task, CLAIM, formal Source Result, or independent Driver admission is asserted.

## Immutable assumptions and observer

Use the frozen Stage302-B parent commit 96745f54d8323c1f18fcb37545e0cdd7bdf11a9e, based on GLOBAL_KNOWLEDGE_V1 main@b86a7783db271ebadd217ac6acbd0249653336d3 and Enterprise Math main@bcd9709cc57f0313c734d0b53110f9f0d6f0cd1a. P000, native six-axis X6/time, ACTIVE residual-fidelity and joint-relation observers, current portable research protocol and existing weighted BRC substrate remain unchanged.

A pre-existing S~Bern(1/2) selects p_0=1/4 or p_1=3/4. Initial visible X and each H operation emit independent fair Bernoulli bits. Each F emits an independent Bernoulli(p_S) bit conditional on S. During n>=1 rounds an examiner adaptively selects H/F from visible history only, possibly with private source-independent randomness; record all action labels and outcomes. For each examiner policy pi, P_s^pi denotes the original complete action-labelled path law given S=s. As shown in Stage302-B, D_n:=TV(P_0^{all-F},P_1^{all-F})=TV(Bern(1/4)^n,Bern(3/4)^n), and TV(P_0^pi,P_1^pi)<=D_n for any pi by a common source-blind kernel.

The repair simulator draws one persistent J with conditional probabilities q_s=Pr(J=1|S=s) in [0,1]; it then emits X/H fair and all F conditionally independently at p_J. Neither examiner nor simulator adjusts J based on revealed S before the nth output. The evaluation may reveal the *actual pre-existing S* afterward. J is not observed during the policy. This is a joint coupling model, not an unconditioned seed independent of S. Define epsilon=Pr(J!=S)=(q_0+1-q_1)/2. The joint BRC carrier retains S,J, ordered actions, outcomes and positive rational branch multiplicity; projected source-labelled paths omit J under a declared observer lease.

## Theorem 303.1 — exact noisy-coupling minimax for all n

Let Q_s^pi be the simulator law of complete action-labelled visible paths conditional on S=s. For all n>=1 and q_0,q_1 in [0,1],

    sup_pi [TV(P_0^pi,Q_0^pi)+TV(P_1^pi,Q_1^pi)]/2 = epsilon * D_n,

and the all-F policy attains the supremum. In particular n=1,2 give risk epsilon/2; n=3,4 give 11epsilon/16; n=5,6 give 203epsilon/256; as n tends to infinity the risk tends to epsilon.

**Proof.** For each fixed visible-history-adaptive pi, conditioning the repair on J=j yields exactly the original path distribution P_j^pi. This is valid because the policy cannot read S or J, so the same causal action kernel acts in the j-labelled component. Therefore

    Q_0^pi=(1-q_0)P_0^pi+q_0 P_1^pi,
    Q_1^pi=(1-q_1)P_0^pi+q_1 P_1^pi.

The difference P_0^pi-Q_0^pi equals q_0(P_0^pi-P_1^pi) as a signed measure; similarly P_1^pi-Q_1^pi=(1-q_1)(P_1^pi-P_0^pi). By homogeneity of TV,

    [TV(P_0^pi,Q_0^pi)+TV(P_1^pi,Q_1^pi)]/2
    =[(q_0+1-q_1)/2] TV(P_0^pi,P_1^pi)
    =epsilon TV(P_0^pi,P_1^pi).

Stage302-B's common-kernel data processing yields TV(P_0^pi,P_1^pi)<=D_n, while all-F realizes D_n. This proves equality uniformly over randomized or deterministic adaptive policies and over all real couplings q_s. The exact D_n binomial formula and the Hellinger-affinity bound 1-D_n <= (sqrt(3)/2)^n establish convergence. QED.

No optimization is hidden: fixing the **actual mismatch rate epsilon exactly** makes every feasible coupling attain the same source-labelled minimax objective epsilon D_n. If the only requirement is an *upper* cap Pr(J!=S)<=epsilon, coupling J=S is allowed and gives risk 0. These are different constraints and should not be conflated.

## Corollary 303.2 — terminal double-label read reveals the entire coupling defect

Let the ideal joint label be (S,J_ref=S), and let the repaired terminal observer read the pair (S,J) as well as the preceding complete visible path. For every fixed policy pi and horizon n,

    TV(Law(S,J_ref,path),Law(S,J,path)) = epsilon.

**Proof.** The ideal measure is concentrated on pairs J_ref=S. The repaired measure puts total probability epsilon on J!=S, disjoint from ideal support. On the matching event J=S the repaired conditional law of paths is the correct original P_s^pi, weighted by Pr(J=S,S=s), so its measure is a submeasure of the ideal measure. The overlap has mass 1-epsilon, hence TV is epsilon. QED.

Thus source-labelled path observation alone has exact risk epsilon D_n, while a joint (S,J) read has exact risk epsilon, even at horizon zero. This is a specific **observer noncommutation witness**: deleting J can conceal a future-readable relational defect. The single J label without S is a different observer interface; its safe scope was proved in Stage302-B.

## Theorem 303.3 — one-bit mutual-information-budget optimum (external derived observer)

Assume the simulator remains in the same persistent binary-J port class and impose I(S;J)<=C bits, 0<=C<=1, with S fair. Define h_2(t)=-t log_2 t-(1-t)log_2(1-t) with endpoints by continuity; let e_C be the unique number in [0,1/2] satisfying h_2(e_C)=1-C. Then

    inf_{Pr(J|S): I(S;J)<=C} sup_pi mean_s TV(P_s^pi,Q_s^pi)
    = D_n * e_C.

**Proof.** Put E=1_{J!=S}, so S is determined by (J,E). Therefore H(S|J)=H(E|J)<=H(E)=h_2(epsilon), while I(S;J)=1-H(S|J). If I<=C, then h_2(epsilon)>=1-C. For epsilon<=1/2, monotonicity of h_2 gives epsilon>=e_C; for epsilon>1/2 the inequality epsilon>=e_C is automatic. Theorem 303.1 gives risk epsilon D_n>=e_C D_n. Equality holds for the binary symmetric coupling J=S XOR E with independent E~Bern(e_C): its mismatch epsilon=e_C and I(S;J)=1-h_2(e_C)=C. QED.

This is the classical binary rate-distortion/Fano-inequality calculation specialized to the present observer and port interface, **not a novelty claim** for information theory or a primitive logarithmic BRC coordinate. The exact rational core Theorems 303.1/303.2 does not use entropy or floating computation.

## Exact verification and limits

Standard-library Python Fraction verifier \`REPRO_STAGE303B.py\` imports the actual \`REPRO_STAGE302B.py\` from this directory and exhaustively checks six rational (q_0,q_1) pairs, all 64 deterministic 2-round adaptive examiners per pair, full strictly positive conditional path laws, all-F rational n=1..7, and exact joint-label TV; actual stdout file \`REPRO_STAGE303B_EXECUTED_STDOUT.txt\` ends \`STAGE303B_NOISY_COUPLING_EXACT_PASS\`. The all-real/n-horizon theorem is the analytic argument above, not a finite-grid extrapolation; Theorem 303.3 is an analytic entropy inequality, not tested by Fraction.

**BRC reuse:** REUSE_APPLIED to provenance-labelled positive rational branches, source/port conditional kernels and observer-scoped quotient. The jointly labelled S,J mass is distinct from pooled path weights; no signed/complex cancellation. Auxiliary Fraction script does not establish execution of a native Heartbeat/BRC computational kernel.

**Native bridge:** no commuting morphism to native six signed X6 axes, ordered one-axis steps, native three-dimensional slice with explicit third coordinate, triadic closure E, ordered real time, or registered six-nonnegative-field lossless Cell codec has been established. P000 remains a premise without a proof obligation.

**Next Stage304-B:** model an actual S-reveal between F/H operations and source-adaptive future controls, determine whether an all-F worst observer remains valid when the policy/kernel may inspect S midstream, and analyze whether correction of J after S revelation preserves the retained joint provenance. Keep native transfer separately scoped and canonical research authority, formal Source/Driver admission pending.
