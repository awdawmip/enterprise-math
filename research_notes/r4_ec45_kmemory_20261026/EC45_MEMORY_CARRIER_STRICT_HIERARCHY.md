# R4-EC45 — K-memory BRC source-flow theorem and strict 1/2/3-state hierarchy

**Status:** author-side rigorous derivation and exact finite enumeration. Not a native Task CLAIM, Result, Guard, independent Driver review, mathematical admission or native X6 theorem.

## Fixed source and scope

Knowledge read snapshot: awdawmip/chatgpt-global-knowledge main@1f73bff7ce37e663922e3c8dd29411441b0e37a7. The canonical BOOTSTRAP, OPERATING_MANUAL, Enterprise Math project TASK router, P000 startup projection (canonical P000 Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc) and ACTIVE worldview were read at that immutable snapshot. EM source input main@2e021dce69085d80e3df06bda732f947705e95b2. Read portable research and activity protocols. Immediate predecessor EC44 is at commit 2a5f65affea1f759feccb766030d51c2a219f3e5, research_notes/r4_ec44_forgetful_observer_20261026/EC44_FORGETFUL_OBSERVER_EXACT_CARRIER.md.

**BRC REUSE_APPLIED:** EC44 original-source occupation flow and rank-one observer consistency, applied to private memory; positive integer source branch counts and joint relation observer-preservation. Actual original histories remain in the carrier even if the controller forgets their labels. This auxiliary finite labelled-source decision tree does not assert a native six-axis X6 heartbeat update or third-coordinate slice bridge. P000 remains ACTIVE_LOCKED and fixed_heartbeat_program=null. Probabilities here are positive source masses, not complex amplitudes or physical clock rates.

## EC45.1 — Exact source × K-memory quadratic carrier

Fix a finite source-history tree H_1,...,H_N with unique parent pa(k) for k beyond H_1. Let w_i(h)>0 for hypotheses i=P,Q, with sum over roots 1 and sum of children of h equal to w_i(h), independent of the controller. At time t the controller sees the current symbol T_t(h), its private memory m∈{1,...,K}, and t; it never sees the hidden original history h. The controller is a fresh-local-randomization kernel q_(t,m,x) on actions P,Q and continuation (C,m'), with no continuation at N. Initial memory is sampled from a distribution μ independently of original source history.

Define nonnegative r_(h,m), d^P_(h,m), d^Q_(h,m), c_(h,m,m') (c only if t<N), satisfying:

(1) r_(h,m)=μ_m on every initial root h, sum μ=1.

(2) For any child k of h, r_(k,m')=Σ_m c_(h,m,m').

(3) d^P_(h,m)+d^Q_(h,m)+Σ_m' c_(h,m,m')=r_(h,m), with the continuation sum absent at N.

(4) For h,k in the same time-t observation fibre T_t(h)=T_t(k), at the SAME memory m, the rank-one constraints for a=P,Q and every continuation destination m' are:

  d^a_(h,m) r_(k,m) = d^a_(k,m) r_(h,m),

  c_(h,m,m') r_(k,m) = c_(k,m,m') r_(h,m).

Then the complete four-observer attainable region for K-memory controllers is EXACTLY the linear image of these nonnegative quadratic-feasible variables:

e_P=Σ_(t,h,m) w_P(h)d^Q_(h,m),  e_Q=Σ_(t,h,m) w_Q(h)d^P_(h,m);

t_i=Σ_(t,h,m) t w_i(h)[d^P_(h,m)+d^Q_(h,m)], i∈{P,Q}.

**Necessity proof.** Conditional on each actual source history h, let r be the probability of surviving to (h,m). Its source-independent controller response q at (t,m,T_t(h)) gives d^a=r q(a), c=r q(C,m'). Independence of exogenous future source children yields (1)–(3). The same q on any observation fibre gives every identity (4). Source-mass summation gives the four outputs.

**Sufficiency proof.** On each (t,m,x) fibre that contains a positive-r history, set q(a)=d^a/r and q(C,m')=c_m'/r at that history. Each equality (4) makes the ratios independent of the chosen positive-survival history. Where r=0, all flows are zero by (3). An entirely unreachable fibre may receive any legal q. The normalization (3) makes q a probability kernel. Induction from μ and the child equations reproduces the proposed r,d,c, proving exact realizability and the four-output formula. QED.

The carrier is a polynomial/semialgebraic certificate, not a claim of algebraic minimality. With K=1 it specializes to EC44's nonprefix current-only rank-one carrier. Dropping (4) without retaining true observed history admits forbidden controllers.

## EC45.2 — The deterministic-plan hull and the ordinary LP boundary

A finite-horizon controller samples a local move at every time-indexed (t,m,x). Preselect independently a pure move for EACH such local node according to its q, and preselect its initial memory μ. Along any realized source path the time index increases strictly, so a particular preselected local triple is visited at most once. Averaging over the preselected pure moves recovers exactly the path law of the original stochastic controller; hence also its four-observer vector.

Writing D_K for all finitely many deterministic K-memory plan vectors and R_K for the region of K-memory controllers with fresh local randomness, we obtain D_K⊆R_K⊆conv(D_K), whence conv(R_K)=conv(D_K). In general R_K itself need NOT equal this hull: an external ex-ante random seed selecting complete plans is a persistent correlation resource, and EC44 exhibits nonconvexity already at K=1.

For this finite horizon model, an exact **ordinary continuous LP lift** of R_K exists iff R_K is convex: if convex, equality with conv(D_K) is a finite simplex projection; if a linear lift exists, its projection is necessarily convex. Mixed-integer/disjunctive or quadratic certificates are not excluded. A linear objective always has the same minimum on R_K and D_K, so exact deterministic enumeration suffices to optimize it even with all allowed fresh private randomization.

## EC45.3 — Strict exact K=1, K=2, K=3 separation

A three-stage positive BRC two-hypothesis source model:

Stage 1 observed root a,b,c, with original positive integer counts p=(20,10,1), q=(1,10,20) normalized by 31 for hypotheses P,Q respectively. **Stage-1 continuation is mandatory**; controller may update its private K-memory state based on the observed root. Stage 2 displays the same symbol x regardless of the root, thereby forgetting the root externally. The controller chooses declare P, declare Q, or continue. If continued, stage 3 terminal sensor z∈{R,B} has strictly positive conditional source counts P:(9,1)/10, Q:(1,9)/10 (independent of root); the controller decides P/Q upon z. These source paths have integer counts over 310 and retain their true root labels in the proof.

Minimize L=e_P+e_Q+(t_P+t_Q)/10. Since stage-1 sampling is mandatory, each hypothesis has at least two time steps, yielding baseline L=2/5=124/310. For a memory group G of initial roots set p_G=Σ_G p_i and q_G=Σ_G q_i. The minimum ADDITIONAL integer numerator over 310 from that group is

f(G)=min{10 q_G, 10 p_G, p_G+q_G+min(9p_G,q_G)+min(p_G,9q_G)}.

The first terms mean immediate stop P/Q. The last means continue: the p+q term is the third-step time penalty and the two minima are independent source-weighted Bayes-optimal terminal decisions at R and B. It is an observer-specific grouped decision cost, NOT a proof that source histories in G are identical.

Exact subset-cost table:

| G | p_G | q_G | f(G) | best stage-2 action |
|---|---:|---:|---:|---|
| {a} | 20 | 1 | 10 | P |
| {b} | 10 | 10 | 40 | C |
| {c} | 1 | 20 | 10 | Q |
| {a,b} | 30 | 11 | 82 | C |
| {b,c} | 11 | 30 | 82 | C |
| {a,c} | 21 | 21 | 84 | C |
| {a,b,c} | 31 | 31 | 124 | C |

**Proof of exact global bounds.** By EC45.2 it suffices to inspect deterministic transducers. After stage 1 they assign one of K memory states to each root. Stage-2 observation x is the same for all roots, so roots assigned one state must share the stage-2 action and, after continuing, the stage-3 terminal decoder. Continuing cannot benefit from a separate memory transfer because the next state depends only on the already shared memory and current symbol; retaining identity and choosing the desired terminal map is at least as strong. Therefore the minimum is [124+min_(partitions into ≤K groups) Σ_G f(G)]/310.

For K=1, the additional numerator is 124. For K=2, the three two-group partitions have costs 10+82=92, 40+84=124, and 82+10=92; one group costs 124. For K=3, three singleton groups cost 10+40+10=60. Hence

  min_(R_1) L = 248/310 = 4/5;

  min_(R_2) L = 216/310 = 108/155;

  min_(R_3) L = 184/310 = 92/155.

Both successive strict gaps equal **16/155**. External public mixtures of entire K-memory plans do not improve a linear minimum.

Concrete achieving policies: K=1 always continue at x, and terminal R→P,B→Q. K=2 remember whether the root was in {a,b} or {c}; continue from {a,b}, terminal R→P,B→Q, and stop Q for {c}. K=3 remember each root, stop P on a, continue on b and terminal R→P,B→Q, stop Q on c.

The respective exact four-observer vectors are

  K=1: (1/10, 1/10, 3, 3);
  K=2: (4/31, 11/310, 92/31, 73/31);
  K=3: (2/31, 2/31, 72/31, 72/31).

Within this three-stage architecture with just one intermediate forgotten symbol and no post-terminal decision, at least three distinct first-stage categories are necessary for K=3 to outperform K=2: two memory states can remember each of ≤2 first-stage roots exactly. **No global minimality claim over unrelated architectures.** Removing mandatory first-stage sampling changes the experiment; this theorem does not cover that altered protocol.

## Verification, exact scope, and next

Companion EC45_verify.js exhaustively checks **47,820** pure transducers: 12 for K=1, 1,152 for K=2, 46,656 for K=3, using original positive integer source counts with objective denominator 310, and yields minima 248,216,184. EC45_subset_check.js is an independent BigInt subset-cost calculation on all seven nonempty root groups with outputs 124,92,60 excluding the common baseline. A second local Python Fraction/source enumeration independently reproduced the winners and rational four-observer vectors (source included in user-delivered archive). The universal statements EC45.1–2 are proved symbolically, not inferred from this finite family enumeration.

Connected GitHub identity awdawmip has push/admin permission. Native owner/control_tasks failed CONTROL_QUOTA; native session_start was denied STATIC_READONLY_SCOPE_DENIED (operation_sent=false). No formal owner or CLAIM is asserted. Research evidence is author-side, not formally accepted. An exact local-source session metadata activity is separately registered on EM main.

**EC46 next:** characterize the least K preserving the entire four-observer attainable region rather than just one linear objective, and characterize when a finite observation-memory automaton eliminates all rank-one quadratic constraints. Any transfer to native Heartbeat World requires actual X6 updater, selected three-dimensional slice and third coordinate, future-operation-preserving observation and separately typed time.
