# Enterprise Math R5 — Complete real-linear ingress-observer exclusion

2026-11-01 Asia/Shanghai. AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This result is about a finite auxiliary two-measure stopping model; it does not establish a native X6 or Heartbeat World theorem.

## Immutable source and authority

Global Knowledge V1 canonical main 40c95779c44d4c55e420d207e1b20e9a6f9c9a80, Enterprise Math canonical main ace20a3785eb79ba4f7f4fa7299871fffc07a96e. Read their canonical bootstrap and operating manual, the Enterprise Math project/TASK research entry, the P000 startup and locked original, ACTIVE worldview, weighted BRC substrate, joint-observer rule, Heartbeat World X6, and active autonomous/portable research protocol. P000 and the protected worldview are unchanged. Immutable predecessor: commit e6710da5b74972b591457a28138d04187d10adaa, research_notes/brc_r5_ingress_q_all_real_nogo_20261101_t0242/RESEARCH.md and VERIFY.py.

The native service reported research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED, and active-job quota 5/5. The bounded active-owner query returned CONTROL_QUOTA. GitHub author publication is not native CLAIM, Result, Review, activity registration or admission.

## Model and positive labelled BRC carrier

Two origins each start with P=Q mass 1/2. Origin-specific alpha=(1/4,1/5), kappa=(3/4,1/6); both have theta=(1+kappa*(1-2*alpha))/alpha=11/2. Each origin has six binary FULL action keys (A,D,Y,LD,LY,LC), giving 4096 deterministic FULL policies. Seedless LR sees only four common keys (A,D,Y,L), giving 16 deterministic LR policies. L cannot access the source or ingress path.

Keep the twelve terminal Q masses labelled (A,D,Y,C,DH,YH,LD,LY,LC,L4D,L4Y,L4C). The P/Q ratios per label are (1,1/2,3/2,1,1/4,2,1,1,1,1,1,1) and stop times are (1,2,2,2,3,3,3,3,3,4,4,4). Each source continuing from A branches to D,Y,C in Q proportions alpha,alpha,1-2alpha. D continuation sends 2/3 to DH and 1/3 to L; Y continuation sends 1/2 to YH and 1/2 to L; C enters L with probability kappa. The complete source and route-labelled positive rational mass carrier is retained for future operations (BRC algebraic REUSE_APPLIED, not a native BRC runtime execution).

Define x=Q(DH), u=Q(YH), t=T_Q, y=Q(L4D)+Q(L4Y)+Q(L4C), c=Q(LC), d=Q(LD). The observed fourth coordinate is s=a*y+b*c+h*d, where (a,b,h) are arbitrary real coefficients. Write V_(a,b,h)=(x,u,t,s). The two-parameter question from the prior NEXT_TASK is the slice (a,b,h)=(1,q,r).

## Theorem: entire real-linear ingress family is classified

For every real a,b,h, the affine dimension of the LR observation convex hull is 3 and its hull equals FULL when a=b=h=0. For every nonzero coefficient triple, the LR affine dimension is 4 and conv(V(FULL)) is strictly larger than conv(V(LR)). In particular, for ALL real (q,r), the LR hull for V_(q,r)=(x,u,T_Q,y+qQ(LC)+rQ(LD)) has rank 4, yet the two hulls are strictly unequal.

### Proof 1 — exact all-real affine rank

Enumerate LR deterministic vertices in lexicographic bits (A,D,Y,L), indices 0..15. Determinants of the following four difference rows from the first index are exactly

  indices (0,9,11,12,14): 24057*a/10240000
  indices (0,8,9,10,12): 513*(118*b-99*a)/10240000
  indices (0,9,10,13,14): -81*(118*h-99*a)/5120000.

The first forces a=0 if all minors vanish, the second then b=0, and the third then h=0. Each expression is linear in the coefficient triple because just one matrix column depends on the fourth observer. Therefore any nonzero triple gives rank four. When all coefficients vanish, (x,u,t) has rank three, explicitly witnessed by the seven-facet polytope below. For a=1 the first minor is the nonzero constant 24057/10240000 independently of q and r.

### Proof 2 — two exposed-edge fiber obstructions

Every LR vertex has x<=3/20 and u<=9/80, with simultaneous equality only at LR vertex indices 14 and 15. Every other LR vertex has deficit D=(3/20-x)+(9/80-u)>=9/80. The full six-observable values at the endpoints are

  L14=(3/20,9/80,43/16,0,19/80,3/40)
  L15=(3/20,9/80,249/80,17/40,0,0).

A FULL point with maximal x,u, if contained in the LR convex hull, must lie on precisely this LR edge. Its t uniquely determines the weight lambda=(t-43/16)/(17/40) on L15.

FULL index 3643 (bits 111000111011) has lambda=4/17 and labelled fourth-observer residual (Delta y,Delta c,Delta d)=(0,1/170,3/170) relative to that forced LR mixture. FULL index 3647 (bits 111000111111) has lambda=16/51 and residual (0,5/204,-1/102). Thus inclusion of both FULL witnesses in the LR hull requires b+3h=0 and 5b-2h=0. The 2x2 determinant is -17, so b=h=0. This proves strict hull inequality for every real pair (b,h)!=(0,0) regardless of a. It is a fiber-constancy failure of the proposed compressed observer; the missing origin/route information is genuinely relevant.

### Proof 3 — explicit support functional for any b,h not both zero

Choose witness 3643 when b+3h != 0; otherwise choose 3647, for which 5b-2h != 0. Its scalar residual delta is respectively (b+3h)/170 or (5b-2h)/204. Let sigma=sign(delta), N=|a|+|b|+|h|, M=40N, t0=43/16, t1=249/80, s14=19b/80+3h/40, s15=17a/40. Let

  g(t)=s14+(s15-s14)*(t-t0)/(17/40)
  H(x,u,t,s)=sigma*(s-g(t))+M*(x+u-3/20-9/80).

Both LR edge vertices score H=0. Every other LR vertex has D>=9/80 and all times lie in [1,4]. On this interval lambda=(t-t0)/(17/40) ranges in [-135/34,105/34], hence |lambda|<4 and |1-lambda|<5. As y,c,d lie in [0,1], the estimate

  |s-g(t)| <= 3|a|+(35/16)|b|+(11/8)|h| <= 3N

holds. Thus H<=3N-40N*(9/80)=-3N/2<0 at all other LR vertices. At the chosen feasible FULL point, x,u equal their maxima, t fixes the same edge mixture and H=|delta|>0. This is a complete parameter-explicit separating certificate, without a real parameter grid.

### Proof 4 — the residual b=h=0 line

For any nonzero a with s=a*y, all 16 LR vertices satisfy the exact supporting inequality

  -21x-61u-19t+(118/a)s <= -19.

FULL vertex 4032 (bits 111111000000) has support score -27/2, exceeding the LR bound by 11/2. Therefore the remaining nonzero coefficient triples are all separated.

### Proof 5 — zero observer gives exactly the three-dimensional common hull

When a=b=h=0 the fourth coordinate vanishes. In (x,u,t), the LR polytope has these exact seven facet halfspaces:

  -x<=0
  -u<=0
  3x+26u-2t+2<=0
  39x+8u-4t+4<=0
  -80x-120u+40t-99<=0
  80u-9<=0
  20x-3<=0.

Exhaustive rational triple-plane intersections show that this is a bounded polytope with exactly eight vertices, all LR vertices. Boundedness follows from x,u lower and upper bounds and the t upper/lower bounds. Every one of the 4096 FULL deterministic vertices satisfies all seven inequalities, while LR is included in FULL. Their three-dimensional convex hulls are equal.

Since each policy key is visited at most once along a trajectory, observed coordinates are multi-affine in the real independent local behavioral probabilities. Every real behavioral observation is a convex combination of the complete deterministic policy corners; all stated hull and support conclusions thus hold for all real behavior strategies, not merely deterministic strategies. This completes the classification.

## Verified execution and exact evidence

The companion VERIFY.py uses Python standard-library fractions.Fraction and exhaustively evaluates 4096 FULL and 16 LR policies. It confirms both P/Q mass normalizations, three symbolic rank-minor coefficient laws, the exclusive LR edge and exact FULL residuals, the b=h=0 rational separator, five signed rational regressions of the general all-real hyperplane, all seven facets against every FULL point and the eight exact polytope intersections. EXACT_OUTPUT.txt contains the actual locally executed program output with final PASS_EXACT_R5_INGRESS_LINEAR_SPAN_GLOBAL_CLASSIFICATION marker.

The universal quantifiers follow from the algebraic, convex-geometric and multi-affine proofs, not from parameter sampling. An independent Driver reviewer and native Source admission remain pending. This result neither proves the original four-observer mother question for all possible observables nor changes P000.

Next: leave the completely classified span{y,Q(LC),Q(LD)}; choose a genuinely new source-conditioned or causal interaction observer outside this span. Compute its full 12-port kernel and LR exposed-face residual before searching support equality; for any candidate prove four-dimensional rank and all-signed convex-hull equality by exact LR mixtures, then separately examine actual seedless LR behavioral-set nonmembership.