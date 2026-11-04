# R5: complete continuous four-parameter classification of the source-route-sensitive two-merger BRC model

Date: 2026-11-04. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Auxiliary two-law finite model; no native X6 or physical theorem asserted.

## Frozen input and model

This result extends immutable predecessor awdawmip/enterprise-math@4d31cd27e140665bdf2fa5da7dd293252e826024:research_notes/brc_r5_two_merger_jensen_20261104_t1341/RESEARCH.md, which defines the positive two-merger source-route topology. Frozen scientific pins: GLOBAL_KNOWLEDGE_V1 a01383f825ef9d43b4b754254303298c64041568 and enterprise-math 86149263e38c22292c9def1e0f69092efa1be77e. Current norms read separately. P000 and ACTIVE worldview unchanged.

Under both P and Q initial origins A/B have mass 1/2 and LR r=1 at time 1. Stop declaring P/Q or continue. After continuing, L/R route under Q=(1/2,1/2), P=(1/4,3/4). At time 3, each route goes to a second merged key (time 3,r=1) with Q probability 1/4, or its terminal side node with Q probability 3/4 and LR r_Lside=1/3, r_Rside=5/3; P probabilities are obtained by LR moment consistency. The four source-route histories j=(A,L),(A,R),(B,L),(B,R) reach the merged key with Q mass 1/16 each if origins continue. Side nodes declare P/Q; at M2 one may stop P/Q or continue. After continuation at M2, conditional terminal time-4 LR values are (1/2,1,3/2), with Q probabilities (u_j,1-2u_j,u_j) and P probabilities (u_j/2,1-2u_j,3u_j/2), for arbitrary real 0<u_j<1/2. Every P/Q edge has positive mass. FULL can condition on source and route; seedless LR is constrained to current (time,r), with no common persistent random seed.

Observer O4=(eP,eQ,TP,TQ): eP=P[declare Q], eQ=Q[declare P], TP=E_P[t_stop], TQ=E_Q[t_stop]. Policy probabilities are arbitrary real values in [0,1].

## Theorem (all-real parameter domain)

For all u in (0,1/2)^4, conv O4(FULL)=conv O4(seedless LR) if and only if u_AL=u_AR=u_BL=u_BR. Under equality of the u_j, the actual real behavioral observation sets O4(FULL) and O4(seedless LR) are equal.

For heterogeneous u, choose a=min_j u_j, b=max_j u_j, t=(a+b)/2, lambda=t/10=(a+b)/20, and n=(1,3/5,-lambda,0). Then 0<lambda<1/20 and the exact signed support gap is

  Delta(n)=[sum_j (u_j-t)_+ - (sum_j u_j-4t)_+]/160
          =min{sum_j (u_j-t)_+,sum_j (t-u_j)_+}/160 >0.

Here h_X(n)=max_{pi in X} n·O4(pi). A constructive FULL witness W satisfies dist_infinity(W,conv O4(LR)) >= Delta(n)/(8/5+lambda). The complete classification is for this precise fixed topology and readout, not the mother R5 problem.

## Proof: all-real strict separation

For n=(1,3/5,-lambda,0), at a history of Q mass q, LR r and stopping time tau, the per-Q-mass reward for declaration P is 3/5-lambda*tau*r, and for declaration Q is r-lambda*tau*r.

Time-3 side nodes have LR 1/3 and 5/3, so unique maximizing decisions are P for L-side and Q for R-side. When both origins continue, their total contribution is
  SIDE=(3/8)[(3/5-lambda)+(5/3-5lambda)]=17/20-(9/4)lambda.

At time-3 merged key r=1, best immediate declaration is Q with reward S=1-3lambda per Q mass. If history j continues to time 4, terminal optimum is P at r=1/2 and Q at r=1 and 3/2. The terminal LR moment equals 1, hence
  C(u_j)=(3/5)u_j+(1-2u_j)+(3/2)u_j-4lambda=1+u_j/10-4lambda,
  C(u_j)-S=(u_j-10lambda)/10.

All upstream decisions are included: stopping at time 1 gives 1-lambda per initial Q mass. Continuing both origins and selecting the best side declarations and at least stopping at merged time-3 nodes gives SIDE+(1/4)S=11/10-3lambda. Its advantage is 1/10-2lambda>0, and the same positive comparison holds sourcewise (upstream origin transition kernels are identical). Therefore an optimizing FULL policy continues at each origin, and an optimizing seedless LR policy continues at the first merged key. Finite-horizon Bellman maximization is valid for all real behavioral randomization because local rewards are affine on each local action simplex.

Each of the four M2 histories then has Q mass 1/16. FULL separately maximizes S versus C(u_j); LR uses a single shared action at M2. The terminal maximizing action depends only on terminal LR, so there is no suppressed source restriction there. Thus exactly
  h_FULL(n)=SIDE+(1/16)sum_j max{S,C(u_j)};
  h_LR(n)=SIDE+(1/4)max{S,(1/4)sum_j C(u_j)}.
Subtracting at t=10lambda gives the displayed Delta. For arbitrary real x_j, sum(x_j)_+-(sum x_j)_+=min{sum(x_j)_+,sum(-x_j)_+}, by splitting positive and negative sums. Heterogeneity makes a<t<b, ensuring Delta>0 and proving strict hull separation.

A maximizing deterministic FULL witness continues both origins, chooses P on all L-side and Q on all R-side nodes, continues exactly histories with u_j>t at M2 and otherwise stops declaring Q, and chooses terminal P at r=1/2, Q at r=1 or 3/2. Its dot product equals h_FULL. Every LR hull vector has dot product <= h_LR, while ||n||_1=8/5+lambda. Holder duality proves the explicit infinity-distance bound.

## Proof: homogeneous u gives equality of actual real images

If every u_j equals u, then the next-key conditional Q/P transition laws upon continuing at any (time,r) key depend only on that key, not hidden origin or route. The root origin kernels and the time-3 route-to-side/M2 kernels likewise depend only on the key and action. Each history at key k=(time,r) has P mass exactly r times its Q mass.

For any FULL real behavioral policy, aggregate its Q action flow F_Q(k,a) across all histories with the same key k; write F_Q(k)=sum_a F_Q(k,a). Define a seedless LR policy pi(a|k)=F_Q(k,a)/F_Q(k) when F_Q(k)>0 (arbitrary when unreachable). By induction on strictly increasing time, the seedless LR policy reproduces these Q action flows, their P action flows r F_Q(k,a), and the resulting next-key Q/P occupancies, because the kernels are predictive-lumpable and fixed. It therefore matches every P/Q terminal key/action/time mass and all four observer coordinates. Every FULL real observer is in the LR real image; reverse inclusion is immediate. This proves actual-image equality, not merely convex-hull equality.

## Exact witness and verification

For u=(5/32,6/32,7/32,8/32), all four parameters lie above the predecessor's 1/8 threshold, making that predecessor normal inconclusive. Here t=13/64, lambda=13/640, n=(1,3/5,-13/640,0). The explicit FULL policy gives W=(881/1024,207/512,25/8,25/8). Exact support values:
  h_FULL=2661/2560, h_LR=133/128, Delta=1/2560,
  dist_infinity(W,conv O4(LR))>=1/4148.

Executed standalone VERIFY.py uses fractions.Fraction with no floating-point tolerance. It independently enumerates all 288 deterministic seedless LR policies for each of five rational models, checks exact maxima, the FULL witness, Jensen support formulas and separation bounds; stdout is EXACT_OUTPUT.txt. Five models include same-side high, low, mixed, near-u=1/2 and homogeneous. Full continuous real-domain quantifiers are justified by the analytic proof above, not by finite samples. No formal proof assistant or independent mathematical review is claimed.

## Scientific context and next

This closes the fixed four-parameter topology: heterogeneous u always yields strict hull separation, homogeneous u yields equality of actual real images. The R5 mother target remains open for more interacting BRC topologies. The homogeneous-case construction is a finite-key instance of occupancy-flow Markovization; related independently published literature includes Laroche and Tachet des Combes, ICML 2023, https://proceedings.mlr.press/v202/laroche23a.html, and Belly et al., AAAI 2025, https://doi.org/10.1609/aaai.v39i25.34845. Neither source is claimed to prove this exact four-parameter result.

Next: construct a new positive source-route-sensitive topology allowing an ALL-SIGNED convex-hull identity without predictive lumpability; require exact rational FULL-vertex primal combinations (at most five LR vertices in R4) or Farkas separators, then rigorously test actual real-image nonmembership. No R5 mother counterexample is inferred from this fixed-family result.
