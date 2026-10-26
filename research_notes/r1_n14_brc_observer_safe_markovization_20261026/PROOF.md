# R1 auxiliary IID N14: exact BRC observer-safe Markovization

**Status: author hand-proof; independently unreviewed; external finite IID auxiliary model.** Date: 2026-10-26. Not an X6/P000 result and not a native CLAIM/Result.

Pinned source: GLOBAL_KNOWLEDGE_V1 main@963ab7e46932d388b01f256e5d3957de6fe13661; enterprise-math main@7f51e8633d1d429c31a2bc4b5ccf70b4bfe005f5. Read global bootstrap/manual, P000 startup and ACTIVE worldview, math/code/BRC research rules, P000 project foundation, current `docs/PORTABLE_RESEARCH_PROTOCOL.md` and Stage170-to-171 packet. Stage171 has a separate R2 activity record; this result does not claim its live ownership or repeat Stage171 primal work.

## Exact theorem

Let A be any finite alphabet, N a finite stopping horizon, and P,Q strictly positive IID laws on A. Let pi be any adapted randomized policy whose internal randomization is independent of which law is true. It stops by time N and declares P or Q. The policy may depend on the full ordered history and correlated internal coins. Then there is a randomized policy pi_count depending only on the count vector k of observed letters (and thus t=sum k) which preserves **under each law** the entire joint distribution of (terminal time T, terminal count vector k(T), terminal decision). In particular both errors err_P=Pr_P(decide Q), err_Q=Pr_Q(decide P) and both mean sample counts t_P=E_P[T], t_Q=E_Q[T] are exactly preserved.

This theorem establishes equality of the four-observer feasible sets for count-only and fully history-dependent randomized policies. It does NOT preserve arbitrary ordered-path/branch observers, internal coin correlations, or native X6 observables.

## Positive ordered-prefix BRC carrier

For an ordered history h, define u_h as the probability, over the policy coins, of reaching the pre-action node h without prior stopping when the observations begin with h. Let a_h,b_h,c_h be the conditional probabilities, given this pre-action node, of stop/decide P, stop/decide Q and continue. All are nonnegative with a+b+c=1; for |h|=N, c=0. Even with persistent internal random memory, these conditional quantities are common to P and Q: the fixed-prefix likelihood factor is independent of the coins and cancels upon conditioning.

Let k(h) be the letter-count vector and lambda_L(k)=prod_i L(i)^k_i for L in {P,Q}. For a fixed h, its exact IID likelihood is lambda_L(k(h)), with **no** multinomial coefficient. The multiplicity belongs to the sum over genuinely ordered h.

For each count k of depth t, define the unweighted ordered-prefix survival and action flows:
 F_t(k)=sum_{h:k(h)=k}u_h;
 A_t(k)=sum_h u_h a_h;
 B_t(k)=sum_h u_h b_h;
 C_t(k)=sum_h u_h c_h.
Then F=A+B+C. Unique-prefix extension and nonanticipation give u_{hi}=u_h c_h, hence
 F_0(0)=1, and
 F_{t+1}(k)=sum_{i:k_i>0} C_t(k-e_i).              (1)
This is an exact integer-multiplicity recurrence independent of the observation law.

## Constructive proof

At every reachable k with F_t(k)>0 define count-policy probabilities (stop P, stop Q, continue)=(A_t(k),B_t(k),C_t(k))/F_t(k). They are nonnegative, sum to one, and have zero continuation at t=N. At F=0 states choose any valid triple; their unreachable choices are immaterial.

Let F'_t be the unweighted ordered-prefix survival flow of this new policy. F'_0=F_0=1. If F'_t=F_t, the new continuation flow at every reachable k is F'_t C_t/F_t=C_t, and zero at unreachable states. Applying exactly recurrence (1), F'_{t+1}=F_{t+1}. Induction holds through t=N. The new stop-action flows are identically A_t and B_t for every k. Thus under law L the probability of terminal decision P at (t,k) is lambda_L(k) A_t(k), and terminal decision Q is lambda_L(k) B_t(k), **for both policies**. This proves equality of the entire asserted terminal joint law.

For clarity, the four exact observer identities are
 err_P = sum_{t,k} lambda_P(k) B_t(k),
 err_Q = sum_{t,k} lambda_Q(k) A_t(k),
 t_L = sum_{t,k} t lambda_L(k)(A_t(k)+B_t(k)), L=P,Q.
They are finite sums; no limits, approximation or unproved policy restriction are involved. Conversely every count-policy is an ordered-history policy, giving equality of attainable observer sets. QED.

## Exact failure of naive equal-path averaging

Under P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=2, use: after initial 0 continue always; after initial 1 continue with probability 1/2, otherwise stop P; after initial 2 stop P. At depth 2, decide Q only on the ordered prefix 01, otherwise P. In count fiber k=(1,1,0), the two genuinely ordered prefixes 01,10 have survival weights 1,1/2. Hence F=3/2, B=1 and the observer-safe count action is decide-Q probability 2/3, **not** the naive 1/2.

The true contribution of this fiber to Pr_P(decide Q) is 1/192, whereas naive uniform averaging gives 1/256; under Q the corresponding numbers are 1/144 and 1/192. This is an exact rational counterexample to compressing away live-branch provenance before constructing the occupancy-weighted count policy.

## BRC reuse, verifier, and limits

BRC interface: positive rational ordered-prefix branches; exact alternative-sum and serial-prefix continuation. Retained information is (F,A,B,C) per count fiber and the letter likelihood lambda_L(k). `REUSE_APPLIED`; the required observer algebra consists of terminal time/count/decision under P and Q. The quotient is **policy-dependent** and observer-scoped, not a lossless encoding of history. Strictly positive IID likelihood equality within fibers is load-bearing. The result does not transfer to general path-dependent observation laws, order-sensitive readouts or native six-axis cell operations without a separate observer/future-operation certificate.

The companion Python `VERIFY.py` executes an exact Fraction ordered-prefix recursion and an independently aggregated count recursion for nonconstant policies at horizons N=3,4,5, respectively 20,35,56 count-time states, checks all four observer values, and reproduces the N=2 uniform-averaging counterexample. These finite tests illustrate the hand proof and do not exhaust policies or prove X6 applicability. Independent Research Driver review, native Result, and Lean formalization remain pending. No novel-prior-art claim is made; classical occupancy-measure Markovization is a plausible external antecedent.

## Next

Determine the maximal future-operation observer family for which a count-fiber quotient remains safe. Add an order-sensitive fifth observer (e.g. probability of the ordered prefix 01 followed by decision Q), prove an exact factorization criterion or construct the smallest rational failure, preserving the original four observer values. This is a separate unit from the Stage171 primal R2 activity.
