# Stage279-B: exact multi-source fiber-compression minimax residual

Author-side research, 2026-10-29. Evidence class: PORTABLE_AUTHOR_PROOF / FINITE_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED. This is a mathematical result for finite labeled-word, nonnegative source-mass models. No P000-native X6 dynamics, physical law, Stage278-A Bellman optimum, formal CLAIM, Source Result, or independent Driver admission is asserted.

## Fixed source provenance
GLOBAL_KNOWLEDGE_V1 canonical main 58d45740faf07023e70932066cd35339ef9cbfa3; Enterprise Math main 5c3a63b7794b7dd8ae209435a020ea8e5d554a1e; original current P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488 (the global P000 startup projection's older blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc differs). Read ACTIVE heartbeart X6, residual-fidelity and joint-relation-preservation constraints without changing them. Predecessor Stage278-B: PR #1571 @ca3840044bacfc330fc8afaf4c43c9f6460e1c52, PROOF_STAGE278_BRC_MARKOVIZATION.md. Existing positive-rational labeled BRC branch carrier reused by typed law from definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json, current blob f375a059fa4af8c6eefaddb4d4a8689a0c063674 (REUSE_APPLIED, not a claim of executing shared toolbox). Current native Site research authority=false; active owner listing failed CONTROL_QUOTA. Evidence storage is not formal authorization.

## Exact declared observer
Let C be a nonempty finite fiber of distinguishable ordered words. Let source i have fixed reaching masses mu_i(h)>=0 on h in C, w_i=sum_h mu_i(h)>0, and conditional p_i(h)=mu_i(h)/w_i. A binary terminal action is selected by the original path policy with conditional probability f(h) in [0,1]. Its source-i action mass is A_i(f)=sum_h mu_i(h)f(h)=w_i u_i(f), u_i(f)=sum_h p_i(h)f(h). A quotient erasing the word label must use one common coin x in [0,1], producing w_i x. The declared error is E(f,x)=max_i w_i |u_i(f)-x|, an unconditional, source-indexed single-fiber action-mass error. It is not a general trajectory-observer error.

## Theorem A: exact minimax for every fixed f
For every f define d(f)=max_{i<j} [w_i*w_j/(w_i+w_j)] |u_i(f)-u_j(f)| (zero for a single source). Then

  min_{0<=x<=1} E(f,x) = d(f).

The nonempty interval of all optimizers is
  [0,1] intersect (intersection_i [u_i-d/w_i, u_i+d/w_i]).
An exact rational optimizer is x*=max(0,max_i(u_i-d/w_i)). If the input masses and f are rational, this expression and all errors are rational.

Proof: for each i,j, |u_i-u_j| <= |u_i-x|+|x-u_j| <= E(f,x)(1/w_i+1/w_j); hence E>=d. For E=d, every pair of intervals [u_i-d/w_i,u_i+d/w_i] intersects. Closed intervals on the line have a nonempty global intersection whenever all pairs intersect. Since all u_i belong to [0,1], this global intersection intersects [0,1], and the displayed x* lies in it. Thus E(f,x*)<=d, proving equality. No floating point or finite-exhaustion assumption is involved.

## Theorem B: sharp source-fiber residual over ALL original terminal decisions
Let TV(p_i,p_j)=(1/2)sum_h |p_i(h)-p_j(h)|. Then

  R_C := sup_{f:C->[0,1]} min_{x in [0,1]} E(f,x)
       = max_{i<j} [w_i*w_j/(w_i+w_j)] TV(p_i,p_j).

The supremum is attained by a DETERMINISTIC original decision f=1_A for a subset A of C. Thus R_C=0 iff all positive-mass source conditional laws p_i are identical word by word, i.e. the source measures are proportional within that fiber. Equivalently, such proportionality is necessary and sufficient for one source-blind quotient action coin to reproduce the local action masses for EVERY binary action rule f. With rational masses, R_C and an extremal decision are exact rational/integer certificates.

Proof: Theorem A gives d(f)=max_{i<j} c_ij |sum_h (p_i(h)-p_j(h))f(h)|, c_ij=w_i*w_j/(w_i+w_j)>0. The supremum over all f commutes with a finite maximum. For a fixed pair, the signed coefficients sum to zero; maximizing their dot product over the finite cube [0,1]^C chooses f(h)=1 on the positive coefficients and zero on the others, achieving TV(p_i,p_j). Applying this to the maximizing pair proves the identity and attainment. Since every c_ij is strictly positive, R_C=0 iff all pairwise TVs vanish. QED.

Quantifier boundary: arrival masses are held fixed while optimizing the final decision. For stopping policies, earlier decisions can change arrival masses. This is a local theorem; it alone does not prove a global non-IID Markovization or future-operation safety. All sources share the same quotient action x: this is not permission to condition on a hidden source label.

## Example: strict non-IID impossibility with SHARP lower bound
Reuse Stage278-B's two distinct strictly positive 2-letter word laws (word order 00,01,10,11):
  P=(1/2,1/4,1/8,1/8), Q=(1/2,1/8,1/4,1/8).
For the unordered count fiber C={01,10}, wP=wQ=3/8, pP=(2/3,1/3), pQ=(1/3,2/3), TV=1/3. Therefore R_C=(3/16)*(1/3)=1/16.

For f(01)=1 and f(10)=0, the source actions have masses 1/4 and 1/8. The UNIQUE best shared coin is x=1/2: both quotient masses are 3/16, leaving absolute error exactly 1/16 for each source; no common x does better. The conditional error is 1/6, distinct from the mass-level residual 1/16. Earlier Stage278-B only showed impossibility; this sharp bound is additional information. Under IID sources, conditional within-count word laws agree and R_C=0 for this particular action-mass observer, but a path-sensitive future observer can still detect lost word order.

## Theorem C: a DIFFERENT trajectory-safe bound
Take a fixed finite-horizon possibly non-IID external source law, whose next-symbol distribution may depend on full history but does not depend on which policy is used. Two stopping policies pi and rho use the same legal actions and differ only in action distributions pi_h and rho_h at each ordered history. Let Reach_pi^source(h) be the probability of reaching h under pi. For ANY terminal trajectory observer F with values in [0,1],

  |E_pi F - E_rho F|
    <= min(1, sum_{|h|<=N} Reach_pi^source(h)*TV(pi_h,rho_h)).

Proof: Couple both policies with common initial history. While histories/actions agree, maximally couple the two local action kernels. If both continue, share the very same next symbol drawn from the fixed history-conditioned source law. The first action disagreement at a given h has probability at most Reach_pi^source(h)*TV(pi_h,rho_h). These first-disagreement events are disjoint. Summing yields the displayed upper bound, also bounded by 1. Off the disagreement event complete stopped histories and terminal actions agree, so the absolute difference for F in [0,1] is bounded by the disagreement probability. QED.

Theorem C cannot be inferred from R_C alone: Stage278-B has a count-only IID quotient with R_C=0 but nonzero difference for a first-symbol-and-action path observer. Future X6 use would first need a typed native source process, time/update monoid, joint provenance and allowed observer; no such bridge has been established here.

## Exact computational witnesses
The accompanying Python 3 standard-library Fraction program enumerates all 4 deterministic decisions on 2-word fibers with 2, 3 and 4 sources, including unequal source masses. It checks 16 additional rational randomized decisions and all 64 deterministic decisions on a 6-word fiber under 3 sources. It checks the proposed optimizing interval and the analytic TV formula exactly. Observed terminal marker: STAGE279_BRC_SOURCE_FIBER_MINIMAX_EXACT_PASS. Outputs: 2-source R_C=1/16 and x*=1/2; 4-source R_C=7/64; 6-word 3-source R_C=3/40. This finite script is a reproducibility witness; universal theorems A/B/C rest on the proofs above, not extrapolation from tested cases. No signed amplitudes/phase, indefinite time horizon, or physical calibration is included.

## Next
Stage280-B: derive a properly typed global finite-DAG source/observer error recurrence that combines action-mass and future-operation residuals; show exactly why local R_C alone is insufficient. The independent Stage278-A Bellman face beyond R277 remains OPEN: see predecessor NEXT_TASK_PACKET_278A_279B.md. Preserve all formal owner/CLAIM and independent review gates.