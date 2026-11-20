# Stage295-B partial｜来源显露后的最优残差保持为 1/4 的全有限期定理

Status: PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. This note completes the **source-revelation subproblem only** of Stage295-B; the fully randomized, cross-label shared-port feasibility/gap problem remains OPEN. Parent Stage294-B proof and actual checker are in this same Draft PR; original Stage293-B immutable parent is 2ec0d172153641d3e4e7e85f84153150e336d33a.

## Exact model and observer
Use the Stage294-B 3-hidden-state, 2-action rational transition law on a,b,c, outputs 0,0,1, and equal source prior on initial a/b. The action policy may randomize using **only the observed output/action history and independently generated randomness**, not the hidden initial source. The declared observer now includes the FULL ACTION WORD alongside the complete ordered output word, and retains the initial source as an evaluation tag. Compare source-conditional output/action laws P_a^pi and P_b^pi against one SOURCE-OBLIVIOUS surrogate law Q^pi on the same word space; the surrogate may be an arbitrary full-output probability kernel. Its risk is
R_pi(Q) = (1/2)TV(P_a^pi,Q)+(1/2)TV(P_b^pi,Q).

## Theorem 295.B.1 (exact source-revelation penalty for every horizon and adaptive policy)
At H=0, both sources have the same visible word (0), so the optimum is 0. For every H>=1, for every source-blind observation-adapted action policy pi:
TV(P_a^pi,P_b^pi) = 1/2,
min_Q R_pi(Q) = 1/4.
The minimum is attained by the Stage294-B 2-label weak quotient law Q=(P_a^pi+P_b^pi)/2, so even allowing an arbitrary surrogate full-history kernel cannot improve on its source-aware loss. This is a SHARP uniform-in-H statement in the declared finite system, not a generic theorem about all weak lumpings.

**Proof.** Conditional on the first action A1=L, subtract the two source-conditioned post-step state measures:
P_L(a,·)-P_L(b,·)=(+1/2 at a, 0 at b, -1/2 at c).
Conditional on A1=R the difference is (-1/2 at a,0 at b,+1/2 at c). Thus for either first action, the signed difference has a positive component of total mass 1/2 and a negative component of total mass 1/2, supported in disjoint observed events: (A1=L,Y1=0) vs (A1=L,Y1=1), or reversed for R. After any subsequent source-blind randomized adaptive actions and hidden transitions, the signed surviving mass at a is pushed forward through the same stochastic kernel, hence retains its sign and total mass 1/2; the component already at c also retains its sign and mass. They can never cancel in the FULL future observed word because the *first action and first visible output* remain as distinguishing prefixes. If A1 is randomized, A1 is included in the observer and the signed measures for L and R occupy disjoint action-tagged fibers; averaging them with the policy’s source-independent action weights preserves total positive and negative masses 1/2 each. Hence the L1 norm of P_a^pi-P_b^pi is 1 and TV is 1/2, for every H>=1, regardless of downstream adaptive policies.

The TV triangle inequality implies R_pi(Q) >= (1/2)TV(P_a^pi,P_b^pi)=1/4. For the actual pooled law Q=(P_a^pi+P_b^pi)/2, homogeneity of the TV norm gives TV(P_a^pi,Q)=TV(P_b^pi,Q)=(1/2)TV(P_a^pi,P_b^pi)=1/4, so equality holds. Stage294-B already proved the pooled law is realized by the exact two-label weak Markov quotient for this initial prior. End proof.

## Exact observation scope counterexample
If the action word is **discarded**, the claimed source TV=1/2 can fail. At H=1, choose L and R independently with probabilities 1/2 each. For source a, the next visible output 1 has probability (1/2)(1/4)+(1/2)(3/4)=1/2; source b gives (1/2)(3/4)+(1/2)(1/4)=1/2. Thus source-conditional output-only TV=0, although source-conditional **(action,output)** TV=1/2. Hence the first action tag is an essential BRC observer/provenance coordinate for this theorem; it cannot be silently dropped. An intervention exposing the hidden state or source-aware action selection changes the allowed future operations, so this theorem is not licensed for that enlarged interface.

## Executed independent finite checks and boundaries
REPRO_STAGE295B_SOURCE_RESIDUAL.py uses only exact Python Fraction arithmetic; it runs 255 deterministic action words for H=0..7 (1793 source-conditioned positive observation/action cases), 32 additional source-blind randomized and history-adaptive policy/horizon checks, and the output-only action-erasure witness. Actual stdout is REPRO_STAGE295B_SOURCE_RESIDUAL_EXECUTED_STDOUT.txt, final marker STAGE295B_SOURCE_RESIDUAL_EXACT_PASS. The all-H proof is the signed-measure decomposition above, not the finite test.

Source and authority are inherited from this run: GLOBAL_KNOWLEDGE_V1 main@1da64e1589bd9a1b29ea40706df7e0189b657be5; EM main@96da51b79be3604143e7ffd6e27eb4faa5d28083; original current P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. BRC positive rational path mass/provenance applied mathematically, not an executed native project BRC tool. Native status research_authority_granted=false, owner query CONTROL_QUOTA; no formal task/CLAIM/Result, independent mathematical review or native X6 bridge.

**NEXT unfinished Stage295-B task:** determine the fully PRE-RANDOMIZED jointly shared Bernoulli port class under two labels and all retained source/history/action correlations. Find a strict LP relaxation gap that survives legal global port mixing (with exact global lower bound), or prove an exact attainability theorem for a declared small family. The Stage294 deterministic-only gap is already known to vanish under one two-atom randomized port mixture, so it is NOT admissible as the desired witness. Stage278-A N12 Bellman remains an independent frontier.
