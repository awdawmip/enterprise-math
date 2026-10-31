# Stage280-B: exact causal BRC source-fiber composition and future-operation residual

Author-side theorem, 2026-10-29. Evidence: PORTABLE_AUTHOR_PROOF / EXACT_FINITE_WITNESSES / UNREVIEWED / NOT_ADMITTED. External finite labeled-history stopping trees only, not a P000 native-X6 or empirical physics claim.

## Frozen input and source types

GLOBAL_KNOWLEDGE_V1 main 314ff1ecb8d348f87f9d97f51570d65256705595; Enterprise Math main b519a46c64db7b40581b618e67a3467cc40a542f; original project P000 and ACTIVE Heartbeat-X6/residual-fidelity constraints read. The global P000 projection blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc differs from the current project original, so original project P000 controls. Parent: Stage279-B immutable commit 92a1e4ce835bfba0e41af875ef7e4908b5e5fc65. BRC reuse: positive rational labeled-path mass; retain ordered word identity and source labels, as typed in definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json (blob f375a059fa4af8c6eefaddb4d4a8689a0c063674). REUSE_APPLIED (not toolbox execution).

## Setup

A finite rooted history tree has depth <=N. Finite source set I has fixed, possibly non-IID, history-conditioned next-symbol kernels, independent of the policy. The source-blind binary policy pi may depend on the full ordered word h. The completed path observer F_i is in [0,1] and may depend on stopped history, actions and order. Partition the decision histories into depth-homogeneous fibers C_1,...,C_m, ordered by depth; each fiber is a prefix antichain. A quotient policy chooses one shared action-1 probability x_C on each fiber.

At a given fiber in a specified hybrid policy, source i has exact reaching mass mu_i(h), w_i=sum_C mu_i(h), and p_i(h)=mu_i(h)/w_i when w_i>0. Put f(h)=pi(1|h) and u_i=sum_C p_i(h)f(h). For positive w_i, the Stage279-B exact local action-mass residuals are

  d_C(f)=max_{i<j} [w_i w_j/(w_i+w_j)] |u_i-u_j|;
  R_C   =max_{i<j} [w_i w_j/(w_i+w_j)] TV(p_i,p_j).

Use zero if fewer than two sources reach a fiber. Stage279-B proves d_C(f)<=R_C and the exact optimal shared coin

  x_C=max(0,max_i(u_i-d_C(f)/w_i)) in [0,1]

has max_i |sum_C mu_i(h)(f(h)-x_C)|=d_C(f). When all inputs are rational, x_C and d_C(f) are rational. Sources having zero reach are ignored for this fiber.

## Theorem 1: causal hybrid and the indispensable future-value residual

Start with pi^(0)=pi. In increasing depth order, choose x_{C_k} using reaching masses mu_i^k under pi^(k-1), then replace the decisions on C_k by x_{C_k}; leave all other decisions unchanged. Define pi^(k) as the resulting policy and rho=pi^(m).

For source i let D_i^k(h) be its conditional expected F_i after forcing action 1 at h minus after forcing action 0, using the COMMON downstream policy for pi^(k-1) and pi^(k). Since F_i lies in [0,1], D_i^k(h) lies in [-1,1]. Define the observer-sensitive fiber residue

  E_{i,k}=min_{g in [-1,1]} sum_{h in C_k} mu_i^k(h) |pi(1|h)-x_{C_k}| |D_i^k(h)-g|.

Then simultaneously for every source i,

  | E_i^pi F_i - E_i^rho F_i |
       <= sum_k [ d_{C_k}(pi) + E_{i,k} ]
       <= sum_k [ R_{C_k} + E_{i,k} ].                         (A)

The mu, d, R, x and E are all rational when the transition probabilities, policies and terminal observer are rational. The E-minimum is attained at a weighted median of the finitely many rational D_i^k(h).

PROOF: C_k is an antichain, so pi^(k-1) and pi^(k) share identical arriving probabilities at its nodes. They agree outside C_k and have identical downstream policies after any fixed action at h in C_k. Consequently conditional expectation gives the exact identity

  E_i^(pi^(k-1))F_i - E_i^(pi^(k))F_i
    = sum_{h in C_k} mu_i^k(h) [pi(1|h)-x_{C_k}] D_i^k(h).      (B)

For arbitrary g in [-1,1] write D_i^k(h)=g+[D_i^k(h)-g]. The absolute g term is <= |g|d_C <= d_C by the Stage279 minimax coin. The remainder is <= sum_C mu_i^k |pi-x_C| |D_i^k-g|. Minimize over g, telescope (B) over k, and apply the triangle inequality. Each median may be chosen at one of finitely many rational D-values. QED.

Sufficient corollary for the DECLARED observer: if at each hybrid stage the conditional ordered-word laws p_i agree across reached sources (R_C=0), and D_i^k is constant on every positive-mass word in the fiber for each source (E_{i,k}=0), all source-indexed expectations are preserved exactly. This is a scoped sufficiency condition, not a necessary characterization and not a universal all-future-operations claim.

## Theorem 2: a separate quotient-kernel and readout bound

Let q(h) be a quotient state, and record a time-ordered quotient trace of states and chosen actions. The compressed process uses action kernel rho(.|trace) and a source-i next-quotient-state kernel Kbar_i(.|trace,a). The original next-symbol kernel K_i(.|h,a) projects to K_i^q(.|h,a); the two processes share legal actions, stopping semantics and horizon. Put

  A_i(h)=TV(pi(.|h),rho(.|qtrace(h))),
  T_i(h,a)=TV(K_i^q(.|h,a),Kbar_i(.|qtrace(h),a)),
  B_i=E_i^pi |F_i(H)-Fbar_i(qtrace(H))|,

where T=0 for actions which terminate. Both F_i and Fbar_i lie in [0,1]. Then

 |E_i^pi F_i-E_i^(rho,Kbar) Fbar_i|
 <= min(1, B_i+sum_h Reach_i^pi(h)[A_i(h)+sum_a pi(a|h)T_i(h,a)]). (C)

PROOF: Couple action choices maximally while quotient traces agree; conditional on equal nonterminal actions, couple their projected next states maximally. The first divergence events are disjoint. Their probabilities are bounded by the original reaching mass times action TV or the original action mass times transition TV, respectively; summing gives the second term of (C). On the no-divergence event the final quotient traces coincide, leaving at most the original-projection observer discrepancy B_i. [0,1]-valued expectation differences are <=1. QED.

(A) is an exact action-mass-plus-continuation-residual inequality with unchanged source kernels. (C) is a distinct policy/kernels/readout coupling inequality for a simulated quotient process. Mixing these observers or omitting future-operation residue is not justified by local R_C.

## Counterexample I — IID R_C=0 yet an ordered-path observer changes

Binary IID sources P(0)=1/2, Q(0)=1/4. At length two, C={01,10} has equal word weights m_i=P_i(0)P_i(1) for each source. All p_i=(1/2,1/2), hence R_C=0. Original pi has f(01)=1, f(10)=0. Its shared minimax coin is x_C=1/2. The valid terminal observer F=1_{word=01 and action=1} has original expectation m_i, while compressed expectation is m_i/2. Errors: P=1/8, Q=3/32. The continuation contrast D=(1,0); choosing g=1/2 yields E_{i,C}=m_i/2. Thus the future-value residual is nonzero and (A) is sharp.

## Counterexample II — non-IID aggregate transition match is not path match

Both sources have probability 1/4 at each 2-bit prefix. At 01,10 their probabilities that the next bit equals 1 are P:(3/4,1/4), Q:(1/4,3/4); at 00,11 they are 1/2. All 3-bit paths have positive rational mass. Both use the same deterministic action continue. A count-only kernel assigning probability 1/2 to the next bit at C={01,10} exactly matches the source-wise total next-bit-1 mass: 1/4 in the original and surrogate for each source. Yet F=1_{prefix=01,next bit=1} has original expectations P=3/16, Q=1/16, while the count-kernel surrogate has 1/8 for both; errors are 1/16. An entire time-ordered count trace reveals prefix 01, so the observer projection residue B_i=0. Transition-TV at 01 and 10 is 1/4 each, giving bound (C) budget 1/8. Equal total mass does not preserve ordered future operations.

## Evidence, scope and successor

REPRO_STAGE280_BRC_DAG.py (Python 3 standard-library Fraction) was actually executed. It exhaustively checked the one-fiber hybrid inequality for all 4 binary deterministic policies times all 16 binary terminal observers (64 cases), checked the sharp IID counterexample for P and Q, and verified both non-IID source cases with exact rational arithmetic. Observed stdout ends STAGE280_BRC_DAG_RESIDUAL_EXACT_PASS. These 64 cases are finite witnesses; the universal finite-horizon conclusions are supplied by the proofs of (A) and (C). There is no assertion of a Lean/formal checker result or independent mathematical review.

Next Stage281-B: construct an observer-optimal quotient coin (rather than locally action-mass-optimal) and a typed native-X6 event/time/update/readout bridge, or show an exact obstruction. Preserve Stage278-A as a sibling unresolved Bellman face. Native authority status on 2026-10-29: research_authority_granted=false; current owner lookup returned CONTROL_QUOTA, so no CLAIM, Source Result or admission is asserted.
