# EC48T — Terminal likelihood-ratio quotient and source-neutral refinement for finite positive BRC observers

Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASS / UNREVIEWED / NOT_ADMITTED. Date: 2026-10-28. Independent author-side portable research only; no Source CLAIM, review, or P000 promotion.

## Sources, authority and scope

GLOBAL_KNOWLEDGE_V1 immutable snapshot: awdawmip/chatgpt-global-knowledge main@c24f667c2a96deb856f9720fb34d92a29bbd1803; project snapshot: awdawmip/enterprise-math main@aa38fc8ff4dc0dff5ef04cdaccd6e2be1a528382. P000 and ACTIVE worldview retained; native active-task query returned CONTROL_QUOTA, so no owner/claim is asserted. The result is a finite, positive, auxiliary **two-source BRC probability-observer** result, not a claim about the native X6 heartbeat space, rotation or physics. Source identities, history, stopping-time information and allowed future operations remain typed explicitly.

Prior art: the Blackwell/garbling sufficiency idea is classical rather than a claimed new statistical theorem. See Rauh et al., Coarse-Graining and the Blackwell Order, Entropy 19(10):527 (2017), DOI 10.3390/e19100527; Khan, Yu & Zhang, A simple proof of Blackwell's theorem on the comparison of experiments for a general state space, Economics Letters 247:112146 (February 2025), DOI 10.1016/j.econlet.2024.112146. This note derives exact finite BRC observation-region and stop-cost certificates needed by the EC48S fixed-terminal-alphabet line.

## Theorem A — exact terminal likelihood-ratio quotient criterion

At a fixed terminal decision node, finitely many outcomes i have strictly positive unconditional prefix-and-terminal masses p_i=P(h,i), q_i=Q(h,i). Randomized acceptance x_i in [0,1] yields the **raw two-source acceptance zonotope**

Z = { (sum_i p_i x_i, sum_i q_i x_i): x_i in [0,1] } = sum_i [0,(p_i,q_i)].

Partition outcomes into nonempty classes C and write p_C=sum_{i in C}p_i, q_C=sum_{i in C}q_i. The quotient zonotope Z_pi=sum_C [0,(p_C,q_C)] equals Z **if and only if** p_i/q_i is constant on each class.

For any tau>=0, the precise support loss in direction (1,-tau) is

D_pi(tau) = sum_C [ sum_{i in C} (p_i-tau q_i)_+ - (p_C-tau q_C)_+ ] >= 0,

where u_+=max(u,0). If one merged class contains unequal ratios, any tau strictly between two ratios in that class gives D_pi(tau)>0. When masses are rational, such tau may be rational.

PROOF. Any quotient strategy lifts by x_i=x_C so Z_pi subset Z. When ratios agree, p_i=r_C q_i inside C. Given fine decisions x_i define x_C=(sum_{i in C}q_i x_i)/q_C. Then both P and Q accepted masses are exactly preserved class by class; thus Z subset Z_pi. Conversely choose tau strictly between unequal ratios in a class. Its coefficients p_i-tau q_i have opposite signs. The identity sum(a_i)_+>(sum a_i)_+ for mixed signs yields a strictly positive support defect for that class; each other class contributes a nonnegative defect. Hence Z_pi is strictly smaller. QED.

Implication: raw terminal label count alone does not determine terminal binary acceptance complexity. A lossless fiber quotient is by likelihood-ratio rays, under this explicitly terminal-only decision scope. It does not show likelihood ratio suffices for intermediate stopping or future memory-sensitive operations.

## Theorem B — m-state original-region invariance under neutral terminal cloning

Consider any finite-horizon strictly positive two-source branch tree. Before the final signal, a controller can stop/continue using at most m>=1 persistent memory states and source-independent private randomization. Terminal observation is followed by accept/reject; there are no subsequent actions. Let S_m be its achievable (P(accept),Q(accept),E_P T,E_Q T) vectors. S_full is the full-history class.

Refine each old terminal symbol i to visible symbols (i,j) using positive probabilities r_ij summing to 1. REQUIRE: the kernel r_ij is identical under P and Q **and independent of hidden prefix history and of controller memory conditioned on the old observable i**. The new j does not affect any earlier action, stop time, future transition or later operation; it is terminal only. The controller may inspect j for terminal acceptance.

Then, for every m and full-history policies,

S_m(refined)=S_m(original), and S_full(refined)=S_full(original).

Consequently the least m for exact raw-region retention is invariant under an arbitrary number of these terminal clones.

PROOF. Lift any old controller by ignoring j, showing original subset refined. Conversely, fix a refined m-controller. In the old experiment execute exactly its pre-terminal control and memory-update rules. On seeing old terminal symbol i, sample an independent private j with law r_i and perform the refined controller's terminal decision on this simulated symbol. Given any preterminal history/memory state and either source P or Q, simulated j has the same conditional distribution as the real refined j, so terminal acceptance probabilities under both sources agree. The stopping-time distribution was already fixed and unchanged. No extra persistent memory is used, since sampling occurs only at the terminal decision. Thus refined subset original. Identical reasoning applies to full-history policies. QED.

Boundary: if the split kernel depends on hidden history, j may reveal an otherwise lost branch to a limited-memory controller. If the clone has future consequences, the causal simulation need not preserve them. Without private randomness, raw deterministic-policy sets need not agree. For signed/phase BRC carriers one cannot re-use positive conditional-probability arguments without a typed extension.

## Theorem C — exact area and terminal variation-gain certificates

The terminal acceptance zonotope area is

area(Z)=sum_{i<j} |p_i q_j-p_j q_i|.

PROOF. Adding segment [0,v_i] to an existing planar zonotope increases area by the length of v_i times the old width perpendicular to v_i, which equals sum_{j<i}|det(v_i,v_j)|. Sum by induction. With positive q_i, area is zero exactly when all p_i/q_i coincide. Neutral proportional clones leave Z and area invariant.

Let p=sum p_i, q=sum q_i. The maximal extra discrimination payoff from observing one last terminal signal rather than stopping and optimally accepting/rejecting immediately is

G = sum_i(p_i-q_i)_+ - (p-q)_+ = (sum_i |p_i-q_i|-|p-q|)/2 >= 0.

PROOF. The optimum after seeing i accepts exactly when p_i-q_i>0; immediate stopping accepts exactly when p-q>0. Use u_+=(u+|u|)/2 and sum_i(p_i-q_i)=p-q. When this one extra step contributes c(E_P T+E_Q T) cost, continuation improves the linear objective alpha-beta-c(E_P T+E_Q T) **if and only if** G>c(p+q), with equality giving a tie. This local comparison assumes no other future control options.

Area(Z)>0 does not guarantee G>0 at a particular selected prefix: the signs of all p_i-q_i may coincide.

## Exact rational instance

At one prefix h take p=(3/8,1/8) and q=(1/8,3/8), so P(h)=Q(h)=1/2. (An identical-mass complementary branch makes both sources globally normalized.) Clone terminal symbol 1 with r=(1/3,2/3) and symbol 2 with r=(1/2,1/2). Then refined P'=(1/8,1/4,1/16,1/16), Q'=(1/24,1/12,3/16,3/16).

A refined deterministic terminal acceptance x'=(1,0,0,1) corresponds to old randomized acceptance x=(1/3,1/2). Both yield (alpha,beta)=(3/16,11/48). Both zonotope areas equal 1/8. G=1/4; with c=1/8, G-c(P(h)+Q(h))=1/8. Merging both **original** terminal outcomes into a single class instead produces a strict support defect D_pi(1)=1/4.

The actual Fraction verifier VERIFY.py checks 441 integer support directions, 41 rational safe quotient thresholds, mass normalization, exact acceptance-vector equality, area, stopping premium, and unsafe quotient defect. Its finite checks support the example and are not a universal proof. No Lean proof or independent review has occurred.

## Enterprise Math mapping and next question

BRC application: positive exact-rational branch-mass carrier, likelihood-ratio fiber aggregation, source/time preservation; REUSE_APPLIED at theorem level (no native BRC implementation execution claimed). The only discarded residual is the source-neutral terminal clone label, shown dispensable under the declared terminal observer/future-operation scope. The full prefix branch labels, joint P/Q information and chronological stopping decisions remain. P000 native X6 and the ACTIVE residual-fidelity worldview are unaltered. Native dynamical transfer still requires explicit X6 slice/embedding, time, readout and preserved update relations.

Next EC48U: analyze history-dependent clone kernels and pre-terminal clones, constructing a minimal rational counterexample or a causal-simulator sufficiency condition with explicit memory interface. See NEXT_TASK.md.
