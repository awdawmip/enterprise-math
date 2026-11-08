# R5: complete five-parameter middle-ratio Blackwell equivalence by two new rational F-face prisms

Date: 2026-11-09 Asia/Shanghai. Evidence: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is a theorem about the frozen seven-LR-node P/Q-BRC terminal-observer model, not a claim about native X6 physical dynamics.

## Frozen inputs and immediate predecessor
Frozen scientific pins: GLOBAL_KNOWLEDGE `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Current rules were independently read at global main `75235a191480a97d84399ebf1061842094d87dc9` and EM main `f16a0d6b5c57f94d8225e4dbcdcb88836350e13b`. P000 and ACTIVE worldview unchanged. The previous author-side result is Draft PR #1827, immutable research commit `c96cc0c30eb18a740f9f95bacad55fa339601706`; its `RESEARCH.md`, `VERIFY.py`, `G_PRISM.md` and `VERIFY_G_PRISM.py` give the earlier prisms.

## Statement, including actual quantifiers
Likelihood-ratio grid r=(1/10,1/2,3/4,1,5/4,3/2,19/10). For a FULL_HIST source in coordinates (g,a,b,u,v,w,z), set
[
x(t,p,q,\theta,\kappa)=(1,t,1,(13t/40+1/80)p, 9\kappa/40+t\theta/10, (3t/40+21/80)q, t\theta/10).
]
The common seedless F face is z'=a'/10 and v'-z'=9b'/40, a sufficient restriction of 9b'z'=4a'(v'-z').

**New theorem A (low q, full kappa).** For all real 3/20<=t<=7/39, 0<=p<=303/2450, 0<=q<=1/2, 0<=theta,kappa<=1, there exists a lawful seedless F-face y with exact T_P,T_Q agreement and all five convex-order hinge inequalities on the LR grid.

**New theorem B (high kappa, full q).** For all real 3/20<=t<=7/39, 0<=p<=303/2450, 0<=q,theta<=1, 1/4<=kappa<=1, a lawful seedless F-face y has the same equalities and inequalities.

Each theorem is supported by 32 independent exact rational endpoint targets, all seven masses, both mass moments, physical capacities, the seedless equation, both stop times and all five hinge inequalities checked using Python `fractions.Fraction` without tolerances.

For any interior real point, choose the product barycentric weights lambda_b of the 5 endpoint choices (b in {0,1}^5). The source is separately affine in each parameter (including tp, tq, ttheta), hence x=sum_b lambda_b x_b. Define y=sum_b lambda_b y_b. The F-face constraints, all physical capacities, the seven LR masses, both time equalities and the five hinge inequalities are affine, so hold for y at every real point. Finite ordered-grid convex order is characterized by the five interior hinges once unit mass and LR first moments agree. The finite martingale coupling theorem (Strassen) supplies a nonnegative 7x7 matrix E satisfying
[
\sum_j E_{ij}=M_i(y),\quad \sum_i E_{ij}=M_j(x),\quad
\sum_i r_i E_{ij}=r_j M_j(x).
]
This matrix is independent of terminal declarations and preserves all seven nodewise randomized declarations and both stopping times.

**Corollary (entire five-parameter slab).** For ALL real 3/20<=t<=7/39 and 0<=p,q,theta,kappa<=1 the frozen FULL_HIST source admits a lawful seedless LR Blackwell representation with the same (e_P,e_Q,T_P,T_Q). The exact covering uses: (1) p>=303/2450: preceding PR #1827 F face, all q,theta,kappa; (2) p<=303/2450 and q<=1/2: new A; (3) p<=303/2450, q>=1/2, kappa>=1/4: new B; (4) p<=303/2450, q>=1/2, kappa<=1/4: preceding PR #1827 G face (requires only q>=3/20, kappa<=7/20). These four cases exhaust the box. The construction may switch charts at boundaries, without affecting existential equivalence. Source historical residual R=9t(theta-kappa)/10 may be positive, zero or negative.

## Concrete nonseedless witness
At (t,p,q,theta,kappa)=(1/6,0,0,1,1/2),
[
x=(1,1/6,1,0,31/240,0,1/60),
]
and a valid F-face y is
[
(403649/517950, 462959/2071800, 403649/517950, 455051/5524800, 20479/103590, 279431/1841600, 462959/20718000).
]
Its five exact hinge margins (target minus source) are
(375781/12430800,3227713/99446400,0,94567/4143600,94567/2071800); both stopping times agree exactly.

## Verification and next research unit
Local original execution: `python -S VERIFY_EXACT.py` on 2026-11-09 Asia/Shanghai, exit 0: 32 A corners, 32 B corners, 101 exact rational regression points per box, special witness; min of each hinge over all 64 corners is 0. Regressions are quality checks; universal proof follows from the exact vertices and multiaffine interpolation. Independent mathematical review and formal CLAIM/Result admission are pending. Next: connect the full physical slab 1/13<t<3/20 (known full t<=1/13 from PR #1821; p<=q up to 3/20 from #1823) with precise F/G corner certificates and a new chart seam. Preserve frozen pins, current owner/claim and independent-review rules.
