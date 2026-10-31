# R5: Complete late-collision rigidity theorem for the fixed strict-stop diamond

Date: 2026-10-30 Asia/Shanghai. Type: author-side analytic proof with exact rational regression. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Formal owner/claim/review not obtained.

Scientific inputs frozen for this derivation: GLOBAL_KNOWLEDGE_V1 main@1660a8fd0a3ac8d37df01915161b6b367b825c3d; Enterprise Math main@9f480ad58175bdf4f82d9c1bbc973453b9fa3828. Exact predecessor: UNIFORM_NO_GO.md in research_notes/brc_r5_stop_only_censor_overlap_20261030_t1744, PR #1663 commit 891d3ba0280c3ecd033ad924289de0530ec549ce. This result expands the predecessor's whole early-error rectangle to independently adjustable late-collision error coefficients. It does not cover arbitrary path weights, distinct P/Q terminal kernels, or further stopping topologies.

## Finite probability model, decisions and observers

At time 2, observed natural label X=0/1; the action is actual STOP at 2 or CONTINUE, not a route choice. If continued, nature reveals U=0/1 and at time 3 action STOP at 3 or CONTINUE to mandatory stop at 4. Under FULL, early continuation probabilities are s_x and late stop probabilities y_xu, all real in [0,1]. Under seedless LR, early s_x remain distinct (time-2 ratios differ) and late y_u must be shared across X (time-3 ratios collide); no policy-level random seed is kept.

Ordered by (X,U)=(00,01,10,11), strictly positive masses are
 P=(7/40,9/40,3/40,21/40)
 Q=(7/20,3/20,3/20,7/20).
The time-2 likelihood ratios are 4/5 and 6/5. At the time-3 collisions, wP_x0/wQ_x0=r0=1/2 for BOTH X; wP_x1/wQ_x1=r1=3/2 for BOTH X. The source labels are retained in the weighted-BRC positive branch carrier and quotient only for allowed late decisions.

Terminal Bernoulli error probability on early STOP is kE(x)=1/4+x/8+d_x. On continued paths conditional on actual late stop indicator Y=0 or1 it is kL(x,u,Y)=1/4+x/8+x*t_u*Y, common under P and Q. Strict probability legality is exactly
 -1/4 < d0 < 3/4,  -3/8 < d1 < 5/8,
 -3/8 < t0 < 5/8,  -3/8 < t1 < 5/8.
At t_u=1/8 the original late XY/8 kernel is restored; t_u=0 makes the error readout independent of time-3 action at collision u.

For L=P,Q, letting wL denote these path masses and y_xu the FULL probabilities (replace by y_u for LR), the four actual real observations O=(eP,eQ,TP,TQ) are
 eL = sum_xu wL_xu [(1-s_x)(1/4+x/8+d_x) + s_x(1/4+x/8+x*t_u*y_xu)],
 TL = sum_xu wL_xu [2(1-s_x) + s_x(4-y_xu)].

## Complete theorem

For every legal REAL tuple (d0,d1,t0,t1), the four-observer convex hulls of FULL and seedless LR REAL behavioral strategies are EQUAL IF AND ONLY IF t0=t1=0. At that locus, the actual real images are themselves equal (not just their hulls), and are a compact convex polytope. This equal common image has affine dimension FOUR iff d0*d1 is nonzero; its explicit 5-point affine determinant is d0*d1/40.

Conversely, if t0!=0 then there is a signed direction with exact positive FULL-minus-LR support gap 3|t0|/80; if t1!=0 another direction yields 9|t1|/80. These all-real formulas include arbitrary independent legal early errors d0,d1 and arbitrary legal other-late-error t_other. For the exhibited FULL maximizing witness, distance to every LR real observation in unscaled coordinate infinity norm is at least gap/(1+|A|+|B|)>0.

Hence this WHOLE fixed stopping topology/terminal-kernel family cannot solve the mother problem of four-dimensional equal hulls with unequal actual images. The original unrestricted stop-only mother question remains open.

## Proof A: an explicit direction gives uniform strictly positive late conflict

Choose u=0 or1 with t_u!=0. Put sigma=sgn(t_u), r_u as above, epsilon=r_u|t_u|/2 >0, and
 A=5 if u=0; A=-5 if u=1,
 B=-A*r_u+epsilon,
 L(O)=sigma*eP + A*TP+B*TQ.
For each branch (x,v) the signed time coefficient for choosing early CONTINUE rather than STOP is A*wP_xv+B*wQ_xv=(A*r_v+B)*wQ_xv. It is epsilon if v=u and 5+epsilon if v!=u, both strictly positive.

For a fixed set of arbitrary late real actions, the marginal signed utility of changing early s_x from zero to one is
 D_x = sum_v (2-y_xv)*(A*wP_xv+B*wQ_xv)
       +sigma*sum_v wP_xv*(kL(x,v,y_xv)-kE(x)).
Since 2-y>=1 and all terminal probabilities lie strictly in (0,1), D_x>5*wQ_x,other - piP_x, where other=1-u, piP_x=sum_v wP_xv. These exact lower bounds are, for u=0: (7/20,23/20) at x=0,1, and for u=1: (27/20,3/20). Therefore BOTH FULL and LR maximize L only with both early branches surviving, s0=s1=1. This is uniform over the complete real legality rectangle.

With full early survival, the signed gain from choosing time-3 STOP on late branch (x,v) rather than CONTINUE is
 g_xv = sigma*x*t_v*wP_xv -(A*r_v+B)*wQ_xv.
At the selected collision v=u these gains have opposite strict signs:
 g_0u=-epsilon*wQ_0u=-|t_u|*wP_0u/2<0,
 g_1u=+epsilon*wQ_1u=+|t_u|*wP_1u/2>0.
At the other collision v!=u: g_0v=-(5+epsilon)*wQ_0v<0 and
 g_1v/wQ_1v = sigma*t_v*r_v-(5+epsilon) < (5/8)(3/2)-5 <0.
Thus FULL uniquely maximizes by y_1u=1 and all other late y=0. LR always uses y_other=0 and must choose a single y_u, with common signed gain epsilon*(wQ_1u-wQ_0u). Hence the EXACT full-minus-LR support gap is
 epsilon*wQ_1u - max(0,epsilon*(wQ_1u-wQ_0u))
 = epsilon*min(wQ_0u,wQ_1u)
 = |t_u|*min(wP_0u,wP_1u)/2
 = 3|t0|/80 (u=0) or 9|t1|/80 (u=1).

This separates the actual images and convex hulls for EVERY real legal parameter point with at least one nonzero t_u, without parameter sampling. A norm inequality gives the stated distance bound. One exact rational specialization d0=d1=0,t0=t1=1/8, u=0 has L=eP+5TP-(79/32)TQ; FULL O*=(107/320,53/160,157/40,77/20) reaches 6691/640, whereas all LR policies satisfy L<=209/20. The exact gap is 3/640. The earlier stronger but less general signed direction at this baseline has gap 3/80.

## Proof B: a constructive seedless LR realization at t0=t1=0

When both t vanish, late errors kL(x,u,y)=1/4+x/8 are independent of late decisions. For arbitrary FULL real s_x and y_xu, retain s_x in LR and choose for each u the single genuine local behavioral probability
 Y_u = [sum_x wQ_xu*s_x*y_xu]/[sum_x wQ_xu*s_x],
with Y_u=0 on zero denominator. Then 0<=Y_u<=1. Since wP_xu=r_u*wQ_xu with the SAME r_u for both X, this choice reproduces simultaneously the P and Q late STOP masses. Therefore it preserves TP,TQ, and since eP,eQ at t=0 depend only on early s_x, those are also preserved. No persistent seed or convex mixture of complete policies is used. FULL observations are realized by LR and the reverse inclusion is obvious; the ACTUAL real sets coincide.

For compact convexity, replace each FULL product s_x*y_xu by a positive flow variable z_xu. Exactly the region 0<=s_x<=1, 0<=z_xu<=s_x (all x,u) is feasible: choose y_xu=z_xu/s_x when s_x>0 and any value when s_x=0. All FOUR observations are affine-linear in s,z (indeed for every t); hence FULL images are compact convex polytopes. At t=0 the equal LR real image is that same polytope.

## Proof C: exact four-dimensional rank classification on the equality locus

With t0=t1=0 the error coordinates are affine in s0,s1:
 (eP,eQ)=(13/40,5/16)+(2d0/5+3d1/5,d0/2+d1/2)
            -d0*s0*(2/5,1/2)-d1*s1*(3/5,1/2).
Select five deterministic LR points (s0,s1;y0,y1):
 (0,0;0,0), (1,0;0,0), (0,1;0,0), (1,1;1,0), (1,1;0,1).
Form the 4x4 matrix of the latter four observation differences from the first, in row order (eP,eQ,TP,TQ). Subtract its first two difference columns from each of the final two. The block determinant is
 det[(-2d0/5,-d0/2),(-3d1/5,-d1/2)] *
 det[(-1/4,-1/2),(-3/4,-1/2)]
 =(-d0*d1/10)*(-1/4)=d0*d1/40.
For d0*d1 !=0 the affine dimension is 4. If d0*d1=0, the two errors span at most a 1D affine line as s varies; together with at most two time coordinates this bounds total rank by 3. QED.

## Verification, scope and next

The standalone standard-library Fraction VERIFY.py enumerates the 64 FULL and 16 LR Boolean strategies for each exact rational parameter test, checks 13 signed support formulas across nine legal parameter tuples, exact LR ratios, positivity and late-gain signs, verifies 4096 rational continuous FULL -> LR policy constructions on the equality locus, and independently checks rank determinant 1/8000 for d0=1/10,d1=1/20. Executed EXACT_OUTPUT.txt ends PASS_EXACT_R5_STOP_ONLY_LATE_COLLISION_RIGIDITY. Exhaustive Boolean searches certify the tested instances; universal REAL conclusions are proved in A-C, not extrapolated from finite search.

BRC: REUSE_APPLIED for the source-labelled strictly positive weighted branch-flow carrier in definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json. The quotient losing X at a collision is safe for these four observations only on the equality locus; no claim of future-observer or native X6 preservation. No Heartbeat/BRC-Shor computation, external physical calibration, Lean check, novelty priority or independent review was performed. P000 and ACTIVE worldview remain unchanged.

Next: add one GENUINE stopping epoch or nonnested interacting LR mergers with strictly positive path kernels and source-labelled BRC masses, or change P/Q-specific terminal readouts/path weights. First require all-signed hull equality by exact rational full-vertex LR combinations with <=5 terms each, or reject via Farkas. Only after full rank hull equality seek exact real-image nonmembership. Do not rescan early d and late t in this fixed family. Native session creation denied STATIC_READONLY_SCOPE_DENIED; control owner lookup returned CONTROL_QUOTA; preservation in this PR is NOT a Source CLAIM/Result/Driver admission.
