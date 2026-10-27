# R5 — Quantitative predictive-diameter LR compression, sharpness, and an exact 12-leaf separation

Date: 2026-10-27. Status: PORTABLE AUTHOR / UNREVIEWED / NOT_ADMITTED; local author label EM-R5-PREDICTIVE-DIAMETER-20261027-1636. GitHub storage is not a native Source CLAIM, frozen Result, independent Driver review, P000 amendment, or native X6 theorem.

## Fixed research input and frontier

Account canonical input: awdawmip/chatgpt-global-knowledge main@9a98adbf15fe74f714c01dd2480595fe5e56d50a (00_BOOTSTRAP.md, OPERATING_MANUAL.md, ACTIVE 我眼中的世界.md, mathematical and BRC policies). Full P000 was read; its Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc agrees with P000_STARTUP.json. Enterprise Math control and predecessor were read at c91d798c220e09147713a2cfb7c5947deb2adb60, including docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md, docs/PORTABLE_RESEARCH_PROTOCOL.md, and brc_n3_signed_fourdim_robust_separation_cone_20261027_r5/NEXT_TASK.md. The prior ten-leaf strict Bellman cone candidate was excluded from the equal-hull question. Earlier mixture-compression TV bounds concern averages of already seedless LR policies; the new theorem below instead approximates ANY full-history behavioral strategy.

The native active-owner lookup in this run returned CONTROL_QUOTA; formal research session/CLAIM/Result/review were not issued. Exact role-bound activity registration awaits the current authorized Source path.

## 1. Model, BRC mass, fiber residue, observer

Fix a finite strictly positive two-measure observation tree of depth N>=1. Observations at each time t precede a stop/continue decision; at t<N an agent may stop and declare P, stop and declare Q, or continue, and at t=N it must declare. Observation kernels depend on observed history but not on the random coins of the stopping policy. Full-history policies use arbitrary real local behavioral probabilities conditional on full observation history. Seedless LR behavioral policies depend on (t,R_t) only, with independent local randomization and no persistent seed.

For history h let Q(h)>0 be BRC positive branch mass, P(h)>0, and R(h)=P(h)/Q(h). For each nonterminal history h, define its next-LR Q kernel K_h(y)=Q(R_{t+1}=y | h,continue). Repeated child labels with the same y are summed, while their exact branch provenance is kept in the underlying tree. For a nonterminal LR fiber G_{t,r}={h at time t: R(h)=r}, set

    delta_t(r)=max_{h,k in G_{t,r}} TV(K_h,K_k),

where TV(p,q)=(1/2) sum_y |p(y)-q(y)|, and singleton fibers have diameter zero. Finite rational P,Q trees have exactly rational computable diameters. The erased information is the branch-dependent NEXT LR kernel, not the existence of a native spatial coordinate or of a physical force.

The final observer is Z=(tau,R_tau,D), with tau in {1,...,N}, D in {P,Q}. Define

    O(pi)=(P_pi(D=Q), Q_pi(D=P), E_{P_pi}tau, E_{Q_pi}tau).

This is an external finite probability-tree model; native Heartbeat/X6 or three-dimensional-slice transfer requires a separately proved relation-preserving interpretation.

## 2. Theorem: occupancy-weighted full-to-seedless TV reconstruction

For EVERY full-history randomized policy pi, there exists a seedless LR policy bar_pi such that

    TV(L_Q^pi(Z),L_Q^bar_pi(Z)) <= B_pi,

    B_pi = sum_{t=1}^{N-1} sum_r gamma_pi(t,r) delta_t(r),

    gamma_pi(t,r)=Q_pi(tau>t,R_t=r).

One may cap B_pi at 1. When all diameters are zero, the entire full-history four-observer set is exactly equal to the seedless LR set. The quantifiers cover ALL real local behavioral probabilities, without a finite-grid assumption.

Proof. For each state (t,r) with positive Q-alive mass under pi, average the three conditional action probabilities over hidden histories:

    alpha_t(a|r)=Q_pi(A_t=a | tau>=t,R_t=r),

where a ranges over continue, stop/P, stop/Q. On zero-mass states choose an arbitrary valid probability vector. Let bar_pi use these tables at (t,r), drawing a fresh local coin whenever a state is visited; thus there is no persistent random seed.

Under pi, the conditional projected transition row from alive (t,r) assigns to stopping with P or Q precisely alpha_t(stop/P|r) or alpha_t(stop/Q|r). Under bar_pi those two stop probabilities are the same. Conditioned on continuation, the next-LR law under pi is a convex combination of K_h for h in G_{t,r}, with weights obtained from hidden Q continuation masses. The corresponding next-LR law under bar_pi is another convex combination of the SAME finite kernels, with its own conditional hidden Q weights. For any two probability vectors p,q on the fiber,

    TV(sum_i p_i K_i,sum_j q_j K_j)
      <= sum_{i,j} p_i q_j TV(K_i,K_j) <= delta_t(r).

This follows by inserting the product mixture and the triangle inequality. Because stop outcomes coincide, total variation of the two projected full rows is at most alpha_t(continue|r)*delta_t(r). Terminal rows at t=N are identical.

The full projected process may have history-dependent trace correlations. Nonetheless its one-time alive-state and absorbing-outcome marginals satisfy exactly the forward recursion of the finite inhomogeneous stochastic matrices formed from the actual conditional projected rows. The seedless process has its corresponding projected row matrices. Their initial LR distributions coincide, because the initial observation occurs before the first action.

Telescope the two products of stochastic matrices with full-process prefix and seedless-process suffix, retaining absorbed outcomes as identity states. Stochastic maps contract TV. Hence

    TV(final Q-laws) <= sum_{t,r} Q_pi(tau>=t,R_t=r)
                                     *alpha_t(continue|r)*delta_t(r)
                      = B_pi.

This is a finite algebraic argument and includes arbitrary real behavioral randomization. QED.

## 3. Four-observer and arbitrary signed support bounds

On each stopped history, the likelihood ratio of the stopped P law to the stopped Q law equals R_tau. Therefore each four-observer component is a Q expectation of respectively

    f1(t,r,D)=r 1_{D=Q},
    f2(t,r,D)=1_{D=P},
    f3(t,r,D)=t r,
    f4(t,r,D)=t.

For any bounded f on the finite terminal-state universe, the expectation difference between two probability laws of TV at most B is <= osc(f) B, osc(f)=max f-min f. Put R_min and R_max equal to the minimum and maximum of R(h) among all possible stopping histories. Then

    |Delta O1|<= R_max B_pi,   |Delta O2|<=B_pi,
    |Delta O3|<= (N R_max-R_min)B_pi,
    |Delta O4|<= (N-1)B_pi.

For an arbitrary SIGNED real lambda=(a,b,u,v), set

    f_lambda(t,r,D)=a*r*1_{D=Q}+b*1_{D=P}+u*t*r+v*t,

and let V_full(lambda),V_LR(lambda) be the corresponding global minimum objective values. Since the LR class is included in full-history strategies, and every full optimizer pi* admits the reconstruction above,

    0 <= V_LR(lambda)-V_full(lambda)
      <= min(1,B_pi*) osc(f_lambda)
      <= min(1,sum_{t<N} max_r delta_t(r)) osc(f_lambda).

This bounds all signed directions at once; a positive upper bound is NOT an equal-convex-hull certificate. All suprema/oscillations are finite, and for rational models and rational lambda are exactly computable.

## 4. Strictly positive 12-leaf family: coefficient 1 is sharp

Take rationals 0<eta<1 and 0<s<3/8. At t=1 there are first observations a,b with Q=P masses eta and 1-eta. At t=2 each splits into u,v with conditional Q=P probabilities 1/2 each; thus every history at t=1 and t=2 has LR=1. At t=3 the possible LR values are

    Y=(1/2,1,3/2),

and the conditional Q probability vectors, identical for u,v within a or b, are

    K_a=(1/8+s,3/4-2s,1/8+s),
    K_b=(1/8,3/4,1/8).

Each vector sums to 1, its likelihood-ratio-weighted mean sum_y y*K(y) equals 1, and every P terminal mass is Q mass times y. Hence there are exactly 12 STRICTLY POSITIVE leaf masses under both measures, with P and Q normalized. All next LR values at t=1 are 1, so delta_1(1)=0. At t=2, delta_2(1)=TV(K_a,K_b)=2s.

Consider this valid full policy: always continue at t=1; at t=2 continue for a histories and stop/declare P for b histories; at t=3 declare Q ONLY at LR=3/2 and declare P otherwise. This deliberately non-Bayes classification is allowed for the reconstruction theorem. The Q-conditional-average seedless LR policy continues at t=2 with probability eta at the common state.

    B_pi = 2s eta,
    TV(L_Q^pi(Z), L_Q^bar_pi(Z)) = 2s eta(1-eta),
    TV/B_pi = 1-eta -> 1 as eta -> 0 through positive rationals.

Thus the multiplicative constant 1 in the occupancy-weighted diameter bound is uniformly SHARP even among strictly positive rational finite trees. The four observables are

    O_full=((3/2)eta(1/8+s),1-eta(1/8+s),2+eta,2+eta),
    O_bar =((3/2)eta(1/8+eta s),1-eta(1/8+eta s),2+eta,2+eta),

hence O_bar-O_full=(-(3/2)eta(1-eta)s,eta(1-eta)s,0,0).
At eta=1/2,s=1/8 this is (-3/64,+1/32,0,0), TV=1/16, B_pi=1/8. The error has first-order dependence on the LR-kernel diameter.

## 5. A second exact test: reject this different candidate by one signed direction

The mother problem asks whether there is a strictly positive rational N=3 tree with conv(O_LR)=O_full but O_LR != O_full. Use the SAME parametrized tree with the DIFFERENT candidate parameters eta=9/10,s=1/4, and exact signed direction

    lambda=(1,1,0,1/12), J=e_P+e_Q+(1/12)E_Q tau.

At LR r, Bayes stopping classification cost per Q mass is min(r,1). At t=2 LR=1, stopping cost 1. After sampling a third time, the optimal expected terminal error is H_a=13/16 or H_b=15/16; the respective one-step information gains are G_a=3/16 and G_b=1/16. Price c=1/12 lies strictly between these gains.

A full-history optimizer after first observation a continues at t=1 and t=2, costing H_a+3c=17/16, strictly better than immediate stop 1+c=13/12; after b it stops at t=1. Thus

    V_full=(9/10)(17/16)+(1/10)(13/12)=511/480.

A seedless LR policy must share first- and second-time actions, since all these LR values are 1. Its expected information gain from the third observation is G_bar=(9/10)(3/16)+(1/10)(1/16)=7/40. First stop costs 13/12; stop at t=2 costs 7/6; continue through t=3 costs 1+3c-G_bar=43/40. Therefore

    V_LR=min(13/12,7/6,43/40)=43/40=516/480,
    V_LR-V_full=1/96>0.

This is a complete rational STRICT SUPPORT SEPARATION certificate, rejecting the candidate from the equal-hull class. For arbitrary real local randomization the objective is multiaffine in action probabilities, so a deterministic vertex is optimal; independent exact enumeration checks all 64 full-history deterministic stopping descriptions (2 choices at a,b and 2 choices at each of a/u,a/v,b/u,b/v) and all 4 seedless LR descriptions. Classification at stopping is pointwise Bayes-optimal; arbitrary real randomization cannot improve either optimum.

## 6. Validation scope, status and remaining question

The author locally ran Python fractions.Fraction for all 12 leaves, P/Q normalization and conditional LR conservation. Checks include eta=1/2,1/4,1/16,1/64 with s=1/8; a finite grid of 162 further rational behavioral policies; and complete 64 versus 4 deterministic stopping-mode enumeration for the specific rational signed separator, all exact. The executed output ends ALL EXACT CHECKS PASSED. The universal theorem and sharp eta->0 limit are proved algebraically here; they do NOT follow from the finite tests.

The convex-hull equality / seedless-set nonconvexity mother question remains open. Next unit: choose a new N=3 strictly positive rational tree, use diameter bounds for prioritization only, and certify every full deterministic four-vector's membership in the seedless deterministic convex hull with exact rational LP weights, or reject with a rational signed separating dual. Only a candidate passing the complete hull test merits exact all-real seedless nonmembership analysis. Native Source owner/CLAIM/Result and independent review remain separate control work.