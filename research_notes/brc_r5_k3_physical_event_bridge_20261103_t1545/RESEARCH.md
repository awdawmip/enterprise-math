# R5 K3 — Physical terminal-event bridge for joint P/Q answer kernels

Date 2026-11-03 Asia/Shanghai. Scientific status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Frozen scientific provenance and problem

The mother goal is one genuine finite two-law stopped experiment with equal convex hulls for FULL-history and seedless-LR four-observer images, and different actual real-behavior images. The prior author-side note (Enterprise Math commit 83bfce42a15d932ff767b7ba2fc360d3be2c1678, research_notes/brc_r5_k3_joint_answer_rigidity_20261103_t1440/RESEARCH.md) classified an auxiliary K3 answer kernel but left its path-level interpretation as a physical error event open. This paper resolves that local semantic problem by constructing a *single policy-independent exogenous sample space* and physical terminal decision map.

Frozen scientific input pins: Global Knowledge a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. The baseline genuine P/Q stopped tree is reported by the predecessors 9bcdb1337dbe9d7b05e99010e0a2a55edce59524 and 0592311ad484d47c449563167d2ae6521ccf4234. Current behavior rules, P000 and ACTIVE worldview were read separately; neither scientific pins nor protected worldview were changed. Author mathematical review remains pending.

## Positive source and observer model

The four source labels are C,I,BJ,IJ. Before the new K3 decision at (time 5, likelihood P/Q=4), incoming source masses are S_s under P and S_s/4 under Q. FULL controls x,y,i with 0<=x,y<=1, 0<=i<=1-x and z_s,t_s,u_s independently in [0,1]. Define

    w=(1/4,(1-x)/4,y/8,i/8),
    alpha=(1/2,2/3,1/2,3/4),
    M_s=w_s alpha_s z_s, S_s=(2/3) M_s t_s,
    U_s=S_s u_s, d=y/16+3i/32.

Seedless LR instead requires i=(1-x)y and common z_s=z, t_s=t, u_s=u. The underlying genuine baseline terminal kernel had error probability 1/2 under each law for both K3 gate actions, baseline terminal clock increment Bernoulli(1/2), and extra increment Bernoulli(3/4) only when continuing.

## One policy-independent physical experiment

For every source s, fix p_s,q_s in the open interval (0,1). BEFORE any behavior policy is selected, augment the source history by four independent potential terminal variables B,D,L0,L1 with these law-conditional marginal kernels:

    B in {0,1}: P(B=1)=Q(B=1)=1/2.
    D in {0,1}: P(D=1)=Q(D=1)=3/4.
    L0 in {P,Q}: P(L0=Q)=Q(L0=Q)=1/2.
    L1 in {P,Q}: P(L1=Q)=1/2+p_s/8;
                    Q(L1=Q)=1/2-q_s/8.

The full conditional product distribution on all 16 (B,D,L0,L1) atoms is strictly positive under BOTH laws: 1/2<1/2+p_s/8<5/8 and 3/8<1/2-q_s/8<1/2, while each Bernoulli clock probability lies strictly between 0 and 1. It is a common measurable finite terminal sample space with two fixed probability measures, not a stochastic kernel redefined by the controller. The whole experiment is the inherited finite physical tree times this conditional product at K3; all preceding paths and probabilities are retained.

At K3 the policy chooses gate action a=0 (stop) or a=1 (continue) based only on its permitted current information. When a=0, the terminal time is 5+B and the terminal decision delta=L0. When a=1, the terminal time is 5+B+D and the decision delta=L1. Both label outcomes appear only at the terminal readout; no later control action sees them. The same deterministic output function delta=L_a is applied under P and Q. The errors are eP=P(delta=Q) and eQ=Q(delta=P). The source and aggregate K3 likelihood ratio before action are P/Q=4. The ratios for terminal labels may differ because the experiment terminates there.

## Theorem — exact all-real event bridge

For every p,q in (0,1)^4 and every real admissible FULL or LR behavioral policy, this single finite physical two-law experiment has the observation vector

    eP=107/128 -21x/128 +d/4 -(sum S)/2 +sum_s p_s U_s/8
    eQ=13/64 +3x/64 -d/2 +(sum S)/8 +sum_s q_s U_s/32
    TP=3+sum M +(3/2)sum S +(3/4)sum U
    TQ=3+(1/2)sum M +(3/8)sum S +(3/16)sum U.

Proof. In each positive source's K3 arrival, old baseline type-I/II error masses were S_s/2 and S_s/8. Since action a=1 is selected with probability u_s conditional on K3 information, in the new fixed sample space the K3 error masses are exactly

    P error_s =S_s*((1-u_s)/2 +u_s*(1/2+p_s/8))
              =S_s/2 +p_s U_s/8.
    Q error_s =(S_s/4)*((1-u_s)/2 +u_s*(1/2+q_s/8))
              =S_s/8 +q_s U_s/32.

These relations hold for all real u_s, including 0 and 1. Baseline time distributions do not change: extra continuation delay has mean (3/4)U_s in P and (3/16)U_s in Q. The P/Q terminal masses of each disjoint source sum to exactly S_s and S_s/4 because both label channels and the independent clocks are normalized. Every unmodified upstream branch contributes exactly its original error and clock expectation. Summing disjoint source arrival contributions proves all four displayed coordinates. The full primitive law is fixed before the stopping policy acts, preserving the information key at K3. QED.

This establishes an ACTUAL binary-testing error event and stopping-time realization of the prior "auxiliary" formulas for the explicitly augmented model. Consequently the preceding joint eight-parameter theorem, whose all-real Bellman proof is a separate author-side dependency, applies here as a physical candidate-family classification: convex hulls agree iff p_s and q_s are each constant in s; in that case the actual real-behavior observation images agree as well. This classification and the terminal-event construction are scoped to this modified genuine stopped experiment with the action-selectable terminal label readout. Independent review and original native X6 attribution have not been completed. The mother counterexample remains open.

## Exact rational verification

The accompanying actually executed Python standard-library Fraction program VERIFY.py enumerates all local terminal rows (gate action, baseline delay, optional extra delay, label), checks their P/Q normalization and physical errors, and checks unchanged clock expectations across 48 nonbinary policy/parameter trials with four sources each. It also independently enumerates 1536 FULL and 16 LR deterministic gate/upstream configurations and calculates both signed support directions from the earlier theorem for p=(1/4,1/2,3/4,1/2), q=(3/4,1/2,1/4,1/2). Recorded stdout:

    EXACT_K3_SEMANTIC_EVENT_BRIDGE
    source_kernel_checks 1734
    full_supports 1135/32 2093/96
    lr_supports 851/24 523/24
    gaps 1/96 1/96
    PASS_EXACT_R5_K3_PHYSICAL_TERMINAL_EVENT_BRIDGE

The aggregate check count is the number tallied by the verifier loops (individual nested assert executions exceed that count). The all-real terminal embedding is an analytic conditional-probability identity. The signed hull theorem is inherited from the noted predecessor, not inferred from this finite cross-check.

## Next mother-goal unit

Extend the same exogenous construction to independent source-conditional continuation-delay kernels r_s and v_s, alongside p_s and q_s, and derive its exact four-signed support envelope. Search for complete convex-hull equality using exact rational FULL-vertex to LR mixtures (at most five LR vertices in R4) or rational Farkas separators. Only on a hull-equal candidate ask whether a real FULL observation lies outside the real LR image. The inherited native Source owner/CLAIM/Result/Driver review and any X6 bridge remain separately unresolved; current Site control owner inventory returned CONTROL_QUOTA.