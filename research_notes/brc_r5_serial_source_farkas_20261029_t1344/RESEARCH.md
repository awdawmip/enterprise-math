# R5 | source-sensitive interacting serial mergers: exact all-real Farkas separator

Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. 2026-10-29 (Asia/Shanghai). This is a finite external two-measure policy model, not a native Heartbeat-X6 theorem or a formally admitted Result.

## Frozen scientific input and authority
GLOBAL_KNOWLEDGE_V1 main@a37fa4ab30818265e57b5f75ab3b9897a92642c8 (global bootstrap/manual, P000 original with matching startup projection, ACTIVE worldview, TASK route, BRC, math/code and activity policies). Enterprise Math main@da4c8cf06b8411e9e44ff6de29b33738e9969b48 (AGENTS, current control authority and portable research protocol). Exact predecessor: PR #1663 head c3488066ceb11f3c0bfc0a17f2b23147a95f6ad7, research_notes/brc_r5_two_merger_lumpability_20261029_t1240/RESEARCH.md.

Native research authority_granted=false; em_control_tasks returned CONTROL_QUOTA. Own em_session_start(RESEARCHER) returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Source owner, CLAIM, Result, independent Driver review and acceptance were NOT established. No protected worldview or control record was changed.

## Four-observer experiment and full BRC provenance
Horizon t=1,2,3,4. At each t<4 a controller may stop/declare P or Q, or continue; t=4 forces declaration. FULL policies see origin and entire path. Seedless LR policies see only the key (t,r), r=dP/dQ. Randomizations are fresh behavioral choices, never a shared persistent seed. The observer vector is O=(eP,eQ,TP,TQ)=(P(declare Q),Q(declare P),E_P[stop time],E_Q[stop time]).

At t=1 two origin histories A,B each have positive Q and P mass 1/2 and share r=1. Continuing generates multiplier s in {1/2,1,3/2}. For origin i use K_Q^i=(p_i,1-2p_i,p_i), p_A=1/4, p_B=1/8. Define K_P^i(s)=s*K_Q^i(s). All six entries are positive and each row sums to 1 under each law. At t=2 and t=3, for every origin/path use the common strictly positive multiplier kernels K_Q=(1/4,1/2,1/4), K_P=(1/8,1/2,3/8), so r←r*s. The source-dependent t=1 Q and P rows each differ by total variation 1/4: this *breaks* the exact predictive-lumpability premise of the previous R5 result.

The t=1 key (1,1) merges A/B. A later nonterminal key (3,3/4) merges ordered paths (1/2,3/2) and (3/2,1/2). Under a permitted all-continue policy each ordered route contributes Q mass 3/64 and P mass 9/256 at that key. Earlier t=1 stop/continue choices change whether this downstream merger is reached; these are serially interacting, not independent tagged parallel components. The later merger alone has a common future multiplier kernel. BRC keeps positive source/path P and Q flow until the stated four-observer quotient is justified.

## Source-sensitive first-collision theorem with arbitrarily long predictively lumpable tail
Assume one first collision at fixed r, with Q weights rho_i>0 summing to 1, an origin-dependent first continue transition, and *all subsequent* LR-key action costs and next-LR kernels origin-independent. For any REAL signed observer direction w, let S be the best immediate-stop cost per initial Q mass, V_2(k) the common optimal tail Bellman value, and C_i the expected optimal continue-then-tail cost conditional on origin i. Then for all real behavioral FULL and seedless LR strategies,
 min_FULL w·O = sum_i rho_i min(S,C_i),
 min_LR   w·O = min(S,sum_i rho_i C_i).
With d_i=S-C_i the exact nonnegative gap is
 Delta(w)=[sum_i rho_i |d_i| - |sum_i rho_i d_i|]/2.
It is strictly positive iff the positive and negative d_i each carry positive rho mass.

Proof: source-independent tail kernels and costs yield a single backward-inducted V_t(k) for all origins and paths. FULL chooses the initial stop/continue action separately at each origin; the LR decision must share one action probability across origins. Its expected cost is affine in that probability, hence is minimized at stop or continue. Backward induction covers every later real behavior. Apply min(S,C)=S-(S-C)_+ and x_+=(x+|x|)/2. The strictness criterion is equality/strictness of the scalar triangle inequality. No enumeration assumption or independence of subsequent merger paths is made. The initial origin weights are fixed before any policy action (not policy-dependent arrivals). QED.

## Exact entire theta interval and optimal integer separating plane
For w_theta=(1,1,theta,theta), 13/272<=theta<=1/16, per-Q-flow stop cost at (t,r) is S_t(r)=min(r,1)+t theta(r+1). At t=4 force S_4; at t=2,3 use the exact Bellman recursion
 V_t(r)=min[S_t(r),sum_s K_Q(s)V_(t+1)(rs)].

A complete calculation at t=3 yields stop at all reachable r∈{1/4,1/2,3/4,3/2,9/4}, and continue at r=1 (tie at theta=1/16). The respective continue thresholds for r=3/4,3/2,1 are theta<1/56,theta<1/40,theta<1/16; at the other reachable r a positive time penalty dominates because another observation cannot change the optimal classification error. At t=2 stop at r=1/2 and 3/2, continue at r=1 (tie at upper endpoint), since its continue advantage is 3/16-3theta. Explicit substitution gives
 V_2(1/2)=1/2+3theta,
 V_2(1)=13/16+7theta,
 V_2(3/2)=1+5theta.

At the t=1 collision, immediate S=1+2theta, and origin-p continuation cost is
 C(p)=13/16+7theta-p(1/8+6theta).
Thus C_A=25/32+(11/2)theta and C_B=51/64+(25/4)theta. Over the ENTIRE declared interval C_A<=S<=C_B (equalities possible at endpoints). The exact all-real support gap is therefore
 Delta(theta)=min{(7/4)(1/16-theta), (17/8)theta-13/128}.
It is positive in the interior, vanishes at the two endpoints, and its UNIQUE maximum occurs at theta*=27/496, with Delta_max=7/496.

At theta*, the rational Bellman data are:
 S=275/248; C_A=67/62; C_B=141/124;
 min_FULL w·O=543/496; min_LR w·O=275/248=550/496.
A deterministic FULL witness: stop and declare P at origin B at t=1; continue at origin A; follow common Bellman-optimal actions afterwards; at every terminal key declare P when r>=1, otherwise Q. This produces O*=(7/64,25/32,15/8,15/8). Therefore the exact integer hyperplane
 496 eP + 496 eQ + 27 TP + 27 TQ >= 550
holds for **every real seedless LR policy**, while its value at the legal FULL witness is exactly 543. Its L-infinity separation from EVERY LR observer is at least 7/(496+496+27+27)=7/1046. The four-observer convex hulls are UNEQUAL. The source-sensitive interacting double-merger candidate is rejected for the mother question. This says nothing about the existence of a different model with equal hulls and unequal actual images.

## Computation, source and scope
The included VERIFY.py is a runnable standard-library Fraction checker; EXACT_OUTPUT.txt is its actual local execution output. It checks strict positivity and P/Q normalization, both row TVs, the two positive second-merger incoming path masses, the signed Bellman values, the FULL witness, 1024 different LR deterministic continue/stop masks at all ten nonterminal (t,r) keys (optimal terminal declaration is pointwise), and 101 exact rational theta checkpoints. Finite checks are independent regression of calculations, not the source of the universal theta and behavioral-policy proof. Last line PASS_EXACT_R5_SERIAL_SOURCE_FARKAS.

Related prior art: Laroche & Tachet des Combes, On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs (ICML/PMLR 2023, https://proceedings.mlr.press/v202/laroche23a.html), is classical occupancy-measure context for exact Markovization, not a justification for source-dependent (t,LR) compression. Kara & Yüksel, Approximations and Learning for Continuous State and Action MDPs under Average Cost Criteria (JMLR 2026, https://www.jmlr.org/beta/papers/v27/24-0395.html), treats different approximation assumptions. No originality priority, external physical fact or native X6 transfer is asserted.

VERIFIED AUTHOR FRONTIER: an explicit serially interacting NON-LUMPABLE rational candidate fails the *all signed* convex hull equality test by one complete integer Farkas witness, with a sharp interval maximum of 7/496. The preceding positive theorem under exact predictive lumpability remains untouched. NEXT_TASK.md specifies a coupled source-sensitive double-merger search that must first establish exact all-signed convex-hull equality and only then examine actual real four-observer nonmembership.
