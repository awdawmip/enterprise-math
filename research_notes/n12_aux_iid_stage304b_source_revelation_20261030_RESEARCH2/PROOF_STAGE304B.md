# Stage304-B: intermediate source revelation and typed provenance repair

2026-10-30. Classification: PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. This is an external positive-weight finite BRC-style probability model, NOT a P000-X6 native proof, native Task/CLAIM/Result, or independent Driver admission.

## Frozen sources and actual authorization
GLOBAL_KNOWLEDGE_V1 canonical main@359b47f8acac12e42ba23dda10421add75de5198 (00_BOOTSTRAP, OPERATING_MANUAL, TASK_RESEARCH router, ACTIVE worldview, P000 V4 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc). Enterprise Math canonical main@1e3e5dc23f21b7333efefe0e4746d29e074ee38a (AGENTS, ACTIVE Heartbeat X6, joint-relation observer rule, autonomous and portable research protocols). Scientific parent: Stage302/303 at immutable c87de0a741cfe90488c98c8a025c7139455719d0; Stage303 proof blob 7c13eca05dedc00bb8d5dc670f6d1fb37cb8943e. Pins represent separate actual snapshots. Current Sites identity has research_authority_granted=false and no write relay. Owner query CONTROL_QUOTA; no claim of authorized native ownership.

## Exact model and observers
S~Bern(1/2) is a pre-existing external source; p_0=1/4, p_1=3/4. The independent initial visible X and all H visits emit fair bits. F visits emit mutually independent Bern(p_S) bits conditional on S. An examiner chooses H/F in n rounds: before time tau in {0,...,n}, actions depend on observed X, previous action labels and bits; AFTER round tau the examiner receives the real S and future actions may additionally depend on it. It never reads private J. It can randomize its policies using private coins independent of S and J; all action labels and the S-reveal event are retained in the observable path.

A repair possesses persistent J with q_s=Pr(J=1 | S=s) (real values in [0,1]); c_0=q_0, c_1=1-q_1, epsilon=(q_0+1-q_1)/2=Pr(J!=S). Given source, seed and actions, independent output coins are used. Three strictly specified interfaces:
A: the external examiner sees S, but repair does not; F remains p_J all along. The examiner supplies its actions to the repair.
B: repair receives true S at tau, but its port MUST keep J and p_J; extra source-dependent output kernels are not allowed. Thus A and B have the same trace law.
C: repair receives true S at tau and atomically retunes *future* F outputs to p_S, preserving original immutable J_old and earlier outputs. Future H remains fair.

O_trace reads actual S, the revelation time, X and all ordered action/output pairs, not J. O_joint additionally reads the ORIGINAL J_old terminally (reference J_ref=S). Replacing this requested historical field by J_new:=S is a different observer.
TV(P,Q)=1/2 sum_omega |P(omega)-Q(omega)|. Let P_s^pi and Q_{s,I}^pi be O_trace laws conditional on true S=s, and R_I(pi)=1/2 sum_s TV(P_s^pi,Q_{s,I}^pi). Let D_k=TV(Bern(1/4)^{tensor k},Bern(3/4)^{tensor k}), D_0=0.

## THEOREM 304.1: Exact minimax for all real couplings, all adaptive policies and all horizons
For every n>=1, every 0<=tau<=n and real q_0,q_1 in [0,1],
    sup_pi R_A(pi) = sup_pi R_B(pi) = epsilon * D_n,
    sup_pi R_C(pi) = epsilon * D_tau.
The SAME all-F policy attains all maxima.

Proof: Fix s and condition on private J. With J=s the repaired trace equals P_s^pi. With J=1-s, write W_{s,k}^pi for the wrong-rate trace, where k=n for locked A/B and k=tau for C. In C all visits after the reveal have the correct p_s regardless of J. Thus in every interface
    Q_{s,I}^pi=(1-c_s)P_s^pi+c_s W_{s,k}^pi,
and TV(P_s,Q_{s,I})=c_s TV(P_s,W_{s,k}) by signed-measure homogeneity.

For each *fixed actual source s*, pre-sample k source-dependent F innovation bits; a common conditional Markov kernel converts those bits into the whole adaptive path, including independent fair X/H bits, all later correct F bits when I=C, the externally revealed s, all policy coins and action labels. It consumes a pre-sampled bit only when a relevant F action is selected. The kernel may depend on fixed s but NOT on which of the two competing F rates was used. Hence TV(P_s,W_{s,k})<=D_k by data processing. This is a source-CONDITIONAL common-kernel proof: source revelation does not justify assuming one common kernel across distinct s. Weighting by fair s yields R_I<=epsilon D_k.

Choose all actions F, before and after revelation. In A/B the full trace has n wrong-rate versus n correct-rate Bernoulli draws; in C exactly tau early wrong-rate draws versus correct-rate draws, followed by an independent common suffix of n-tau correct draws. The common suffix preserves TV and all-F attains D_k for either s. Both upper bounds are sharp, simultaneously. Randomized policies are included by incorporating the independent policy coins into the common kernel. QED.

The binomial likelihood ratio for a word with j ones in k visits is 3^(2j-k); D_1=D_2=1/2, D_3=D_4=11/16. At tau=0 the rate-reset trace risk is zero despite possible historical provenance error; at tau=n C is locked. Mere source knowledge in B cannot repair a locked port.

## THEOREM 304.2: immutable joint-provenance audit
For every n, tau, policy and q_s, the complete terminal observer O_joint satisfies
    TV(Law_ideal(S,J_ref=S,trace), Law_repair(S,J_old,trace)) = epsilon.
Proof: the ideal is supported on J_ref=S; repaired mass epsilon lies disjointly on J_old!=S. On J_old=S the full repaired path law agrees with the ideal and its mass is a submeasure thereof, so the common overlap equals 1-epsilon exactly. This persists after C's output-rate reset, which does not rewrite historical J_old. If J_old is overwritten as J_new=S, a later observer of J_new alone sees another typed quantity, not the requested pre-reset relationship. QED.

## Positive-rational witness and executed validation
Take q_0=1/8, q_1=7/8, so all S,J and H/F output branches are positive rationals, epsilon=1/8. Reveal S after tau=1.
n=2: locked and reset O_trace minimax = 1/16, terminal O_joint TV = 1/8.
n=3: locked O_trace minimax = 11/128, reset O_trace minimax = 1/16, terminal O_joint TV = 1/8.
Thus n=3 separates a real rate reset from merely giving S to a locked port. n=2 alone cannot discriminate because D_1=D_2.

REPRO_STAGE304B.py runs Python Fraction in the EXTERNAL model (not an executed native BRC/Heartbeat operator). For n=2 it exhausts 2^10=1024 deterministic H/F policy trees: 2 pre-reveal X-conditioned decision nodes, then 8 post-reveal (S,X,Y1)-conditioned nodes. It computes normalized positive full action-labelled paths for both interfaces, all joint-label TV checks, the exact maxima and an n=3 all-F witness. Actual stdout: STAGE304B_SOURCE_REVEAL_RESET_EXACT_PASS. Its finite verification does not establish the all-real theorem; the proof above does.

## BRC scope and native bridge
Reuses positive provenance-labelled (S,J_old,ordered H/F visit) branches and explicit observer quotients, without treating positive mass as signed amplitude. Auxiliary Fraction is not the native typed BRC kernel; no physical residual, phase cancellation, or P000 dynamical law is inferred. Native transfer remains NATIVE_TRANSFER_PENDING: six signed X6 displacement components, ordered one-axis steps/source/multiplicity, native E triads, native 3-dimensional slice plus third coordinate, true time, registered six-nonnegative-field lossless final Cell codec (no global full-X6 codec presently registered), and one commuting observer/operation map are not yet proved. Independent Driver review and Source formal execution/admission are pending.

Next specific problem: Stage305-B noisy/delayed revelation W of original S; test whether post-signal predictive mean alone preserves multi-F joint covariance and derive a sharp risk under a specified interface. See NEXT_TASK_PACKET_305B.md.
