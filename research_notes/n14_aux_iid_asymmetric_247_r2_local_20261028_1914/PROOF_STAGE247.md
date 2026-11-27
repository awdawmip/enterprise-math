# Stage247 — exact asymmetric error-cap sharpness locus (external ternary IID)

**2026-10-28; portable author theorem, UNREVIEWED / NOT_ADMITTED.** Local author ID EM-R2-T11-20261028-1914-LOCAL is NOT a service-issued identity. GLOBAL_KNOWLEDGE_V1 main@39a41424091c5ec8512e5c6ebf9c43c7fef0682d; Enterprise Math main@737cd7689de9692617a5e2c04ef0e81a19504ed4; predecessor Stage246 exact proof at immutable e38ba8ca0dfe5defa82652effcb55ee8253a0e89. Native em_status reported research_authority_granted=false, and the active owner read via em_control_tasks returned CONTROL_QUOTA (active native job quota 5/5). This author research does not take over any live Source claim.

## Theorem (all integer N≥1, all real caps)

Consider two IID laws P=(3,1,20)/24 and Q=(2,2,20)/24 on {0,1,2}. A common randomized policy can use all ordered observations and stop at time τ∈{0,...,N}; its terminal guess is P or Q. Put eP=Pr_P(guess Q), eQ=Pr_Q(guess P), tP=E_P τ, tQ=E_Q τ and

\[
V_N(a,b)=\inf_{\pi:\ e_P\le a,\ e_Q\le b}\max(t_P,t_Q),\qquad 0\le a,b\le1,
\]

where an empty feasible set has infimum +∞. The sequential total-variation lower bound is \(L(a,b)=\max\{0,24(1-a-b)\}\).

**Exact characterization:** \(V_N(a,b)=L(a,b)\) if and only if either (i) \(a+b\ge1\), or (ii) \(a+b<1\) and all three conditions hold:

\[
\boxed{a+b\ge\frac{3+(5/6)^N}{4},\qquad 2a+b\ge1,\qquad 2a+3b\ge2.}\tag{247.1}
\]

In case (ii), both errors are tight and \(t_P=t_Q=24(1-a-b)\). This holds for every real pair including irrational caps, and for the unrestricted finite-horizon full-history policy class.

## Proof: positive source-aware coupling, equality rigidity

The exact maximal coupling consists of four labeled positive branches (P-sample,Q-sample;weight): (0,0;2/24), (1,1;1/24), (2,2;20/24), and (0,1;1/24). Its marginals are exactly P,Q and its only mismatch has probability d=1/24. Couple all policy random seeds identically across experiments. Let A_k mean both copies are active before sample k and all preceding sampled symbol pairs matched. Until the first mismatch their histories and actions coincide.

If the terminal decisions differ, an observed mismatch must have happened. First mismatches at successive k are disjoint and each occurs with probability d Pr(A_k). Let D_P and D_Q be indicators that the respective terminal decision is P. Then

\[
1-e_P-e_Q=E(D_P-D_Q)
\le d\sum_{k=1}^N\Pr(A_k)
\le d\min(t_P,t_Q)\le d\max(t_P,t_Q). \tag{247.2}
\]

Suppose a+b<1 and equality with \(L(a,b)\) holds. Cap monotonicity and (247.2) imply equality at EVERY step: \(e_P=a,e_Q=b\), \(t_P=t_Q=\sum_k\Pr(A_k)\), and the nonnegative differences \(\Pr_R(\tau\ge k)-\Pr(A_k)\) vanish for each k and both R=P,Q. Thus no copy remains active at a sample after any earlier mismatch.

For any positive-mass active matching history and fixed shared policy seed, the next paired samples can be (0,1) with positive conditional weight 1/24. If a policy continued after observing 0, the P copy would stay active after this mismatch, contradicting equality for tP; if it continued after observing 1, the Q copy would violate equality for tQ. Therefore every active reachable policy must stop upon a 0 or a 1. Equality in \(E(D_P-D_Q)\le \Pr(\text{first mismatch})\) also forces D_P-D_Q=1 on every mismatch branch, so after 0 it must decide P and after 1 it must decide Q. This extends to matched (0,0)/(1,1) branches by the common history-and-seed policy kernel. By induction all active prefixes consist solely of 2s; the policy may randomize after those prefixes and at a no-signal stop. This is a NECESSITY result for the full randomized full-history class, not an assumption selecting a convenient family.

Let s be probability of seeing a first symbol other than 2 before stopping, and let z be the total probability of stopping without any such signal and guessing Q. As the probability of symbol 2 is the same 5/6 under both laws, s,z and the survival probabilities of all2-prefix paths are shared. Each active sample detects a non2 signal with common hazard 1/6. Therefore

\[
0\le s\le s_N:=1-(5/6)^N,\quad 0\le z\le1-s,\quad
t_P=t_Q=6s. \tag{247.3}
\]

A signal symbol is 1 under P with conditional probability 1/4 and 0 under Q with conditional probability 1/2, giving

\[
\boxed{e_P=s/4+z,\qquad e_Q=s/2+1-s-z,\qquad t_P=t_Q=6s.} \tag{247.4}
\]

Conversely EVERY \((s,z)\) in that exact triangle is achievable for finite N: at time 0 activate the first-non2 policy with probability \(w=s/[1-(5/6)^N]\) and otherwise stop immediately; if activated, sample until 0 or 1 or N total observations, decide P at 0 and Q at 1; at a no-signal stop guess Q with probability \(q=z/(1-s)\). Since \(s_N<1\), q is defined. All these probabilities lie in [0,1], even for real irrational inputs, and no P/Q mass is collapsed before a final observer is applied.

Error tightness gives \(s=4(1-a-b)\), \(z=a-s/4=2a+b-1\). The constraints \(s\le s_N\), \(z\ge0\), \(z\le1-s\) are exactly (247.1). This proves case (ii). If a+b≥1, a time-zero guess with probability u of Q for any \(1-b\le u\le a\) attains zero time and satisfies both caps. QED.

For fixed finite N, all randomized full-history policies are mixtures of finitely many deterministic contingent plans, whose observation vectors form a compact convex polytope. Hence if the cap pair lies outside the characterized sharpness set, but a policy is feasible, its optimum is strictly above L; absence of equality cannot be evaded by a limiting sequence.

## Exact horizon separation and verification

Choose \(a=3/10,\ b=19/40\). Then \(a+b=31/40\), \(s=9/10\), \(z=3/40\). At N=14, choose

\[
w=\frac{352638738432}{361303242355},\qquad q=\frac34.
\]

The resulting policy has exact observation vector

\[
(e_P,e_Q,t_P,t_Q)=(3/10,19/40,27/5,27/5),
\]

attaining the universal lower bound 24(1-a-b)=27/5. An actually executed Python Fraction checker separately computes the analytic observer map and traverses 32 unmerged ordered decision leaves, retains distinct P/Q rational masses and verifies their normalization and the four coupling atoms.

At N=12 the signal bound fails by an EXACT rational positive margin
\[
\frac9{10}-[1-(5/6)^{12}]=\frac{132311957}{10883911680}>0.
\]
Thus the TV bound cannot be attained by ANY N≤12 full-history randomized policy at this cap pair, while the N14 feasibility margin is
\[
[1-(5/6)^{14}]-\frac9{10}=\frac{8664503923}{391820820480}>0.
\]

Horizon cap-sum thresholds: N9 32186213/40310784; N12 6774487633/8707129344; N14 241196007913/313456656384.

Reproduce with: python verify_stage247.py. Output saved in EXACT_RUN_STAGE247.txt, terminal flag STAGE247_ASYMMETRIC_EXACT_PASS. The 45 rational spot cases validate the witness implementation, while the universal all-real theorem follows from the preceding proof. Source-labeled positive rational paths and their ordered stopping observers are BRC-compatible; no native BRC executable, P000-X6 correspondence, native time dynamics, or independent Driver review was invoked. The theorem is only for the declared external IID model.

Next frontier: characterize the strict gap V_N(a,b)-L(a,b) outside (247.1), beginning with exact cap pair (3/10,19/40) at N12; determine actual cap feasibility and an exact primal/dual rational certificate for its optimal expected-time maximum. Preserve separate P/Q errors, stopping-time measures, ordered path identity, and P000 observer scope; do not reinterpret this portable result as a native Source Result or formal mathematical admission.
