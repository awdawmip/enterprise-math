# R5 — global 3-response observer rank and hull no-go
2026-10-31 (Asia/Shanghai). **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** Theorem about a declared auxiliary positive P/Q finite stopping model, not Heartbeat X6 and not the original mother problem's solution.

## Frozen provenance
GLOBAL_KNOWLEDGE_V1 canonical-main \`2276d70f2925a43e8ad1e5cf32e09035f30c9c06\`; Enterprise Math canonical-main \`c68fd26c8e605f2434a38f17f786a3bc2b26b6f7\` throughout this run. Read the global bootstrap/manual, project and TASK startup, P000 startup and the original matching P000 blob \`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc\`, ACTIVE worldview, and current portable/autonomous protocols. Neither P000 nor worldview modified. Mathematical predecessor: immutable author-verified \`f3125bf5bb065ef787ca954535381894adbc409b:research_notes/brc_r5_three_response_uniform_20261031_t2240/RESEARCH.md\`, which proved only a local 3-response exclusion box. This turn proves **all-real global exclusion** of every possible full-rank equal-hull candidate within that 3-response family.

Native \`em_status\` read: \`research_authority_granted=false\`, \`executor_binding_configured=false\`; owner query \`em_control_tasks\` gave \`CONTROL_QUOTA\`, checkpoint list gave \`ACCESS_DENIED\`. No formal CLAIM, owner, Result or Driver review is asserted; the publication is portable author evidence only.

## Exact typed model
Two hidden sources i=0,1 carry Q mass 1/2 each and begin at A at time 1, likelihood ratio 1. Strictly positive source parameters \`(alpha0,kappa0)=(1/4,3/4)\`, \`(alpha1,kappa1)=(1/5,1/6)\` yield compensated \`theta_i=[1+kappa_i*(1-2alpha_i)]/alpha_i=11/2\`. On A CONTINUE, D,C,Y at time 2 receive Q fractions \`alpha_i,1-2alpha_i,alpha_i\` and likelihood ratios \`1/2,1,3/2\`. D CONTINUE yields DH at time 3 with Q fraction 2/3 and likelihood ratio 1/4, or L at time 3 with 1/3 and ratio 1. Y CONTINUE yields YH at time 3 with Q fraction 1/2 and ratio 2, or L with fraction 1/2 and ratio 1. C naturally stops at time 2 with Q fraction 1-kappa_i or enters L at time 3 with fraction kappa_i. L STOPs at time 3 or CONTINUEs to L4 at time 4, both likelihood ratio 1. A/D/Y may STOP at their own nodes. P(leaf)=lambda(leaf)*Q(leaf), total P=total Q=1 for all policies.
FULL uses six binary action keys \`(A,D,Y,LD,LY,LC)\` per source, 4096 deterministic policies. Seedless LR uses the common four \`(A,D,Y,L)\` time/likelihood keys, 16 deterministic policies. Every LR decision key is visited at most once on a history; a linear observation score is multi-affine in the four independent real behavioral probabilities, thus its maximum over real LR policies is at one of 16 vertices. The four-dimensional *convex hull* is kept distinct from the actual real LR image.

Shared terminal Bernoulli-error responses are all 1/2 except \`r_DH=1/2+v\`, \`r_L4=1/2+w\`, \`r_YH=1/2+z\`, for **every legal real** \`(v,w,z) in [-1/2,1/2]^3\`. \`gamma=2r_C-r_A-r_L=0\`. Use the positive source/route-labeled BRC probability carrier, then take the explicit aggregate \`x=Q(DH)\`, \`y=Q(L4)\`, \`u=Q(YH)\`, \`t=T_Q\`. Signed support functionals are dual coordinates, not signed branch masses. The aggregate is sufficient for *this* four-observer snapshot; origin and route provenance remain retained at full state and no future-safe compression is claimed.

## Theorem (complete legal cube)
For every legal real triple, the LR four-observer convex hull has affine rank exactly four **iff \`w*(z-v)!=0\`**. For every such rank-four triple, \`conv(O_FULL) != conv(O_LR)\`; indeed a legal FULL witness admits a parameter-transported separating signed direction. On \`w=0\` or \`z=v\`, the entire four-observer image has affine dimension at most three. Thus **no triple in this model family has both full LR four-rank and equal FULL/LR four-observer convex hulls**. We do not assert that hulls coincide when the rank collapses.

### Lemma 1: universal time identity
For any FULL or LR deterministic or real behavioral policy:
\`T_P-T_Q=u-3*x/4\`. Since sum of \`(lambda-1)*Q(leaf)\` is zero, use time reference 3: \`T_P-T_Q=sum_leaf(time-3)*(lambda-1)*Q(leaf)\`. Only D and Y STOP leaves contribute: \`(Q(D)-Q(Y))/2\`. Before those STOPs the D and Y incoming Q masses are equal per source. For every source, D continuation contributes \`3*x/2\` to removed D STOP mass; Y continuation contributes \`2*u\` to removed Y STOP mass. Hence \`Q(D)-Q(Y)=-3x/2+2u\`, establishing the identity.

### Lemma 2: exact observer factorization and kernel
For \`O=(e_P,e_Q,T_P,T_Q)\`:
\`e_P=1/2+(v/4)*x+w*y+2*z*u\`;
\`e_Q=1/2+v*x+w*y+z*u\`;
\`T_P=t+u-3*x/4\`, \`T_Q=t\`.
The affine linear map from \`(x,y,u,t)\` has determinant \`3*w*(z-v)/4\`, by expanding the block
\`[[v/4,w,2z],[v,w,z],[-3/4,0,1]]\`.
When \`w*(z-v)!=0\` its inverse is exact:
\`x=4*(e_P-e_Q-z*(T_P-T_Q))/(3*(z-v))\`,
\`u=(T_P-T_Q)+3*x/4\`,
\`y=(e_Q-1/2-v*x-z*u)/w\`, \`t=T_Q\`.
On either singular surface the map has rank <=3. These are real algebraic identities, not numeric observations.

### Lemma 3: the LR aggregate carrier is exactly 4-dimensional
The five LR policies \`0000,1000,1001,1010,1100\` (action ordering A,D,Y,L) give the \`(x,y,u,t)\` vectors:
\`(0,0,0,1)\`,
\`(0,0,0,179/80)\`,
\`(0,19/80,0,99/40)\`,
\`(0,0,9/80,197/80)\`,
\`(3/20,0,0,197/80)\`.
The 4x4 determinant of their differences from 0000 equals \`-50787/10240000 != 0\`. The corresponding four-*observer* determinant is therefore
\`D(v,w,z)=-152361*w*(z-v)/40960000\`.
Together with Lemma 2 this gives the claimed exact rank classification, for all real parameters, including cube boundaries.

### Lemma 4: an error-parameter-independent carrier separation
Define \`F=(985/8)*x+70*y-130*u-23*t\`.
The eight LR policies that STOP at A all give score \`-23\`. For the other eight, ordering D,Y,L lexicographically as 000,001,010,011,100,101,110,111, the exact scores are
\`-4117/80,-403/10,-5701/80,-877/16,-6107/160,-3757/160,-1855/32,-6079/160\`.
All are < -23, so \`sup_(real LR) F=-23\`, using multi-affinity.
A valid deterministic FULL witness has origin 0 actions \`(A,D,Y,LD,LY,LC)=(1,1,0,1,0,1)\`, and origin 1 STOPs at A. Its feature vector is \`(x,y,u,t)=(1/12,11/48,0,49/24)\`, hence \`F(W)=-661/32\`. The exact support gap is
\`F(W)-sup_LR F=75/32>0\`.
This is an actual FULL-vs-LR separation in the four-dimensional aggregate carrier, irrespective of v,w,z.

### Finish
For \`w(z-v)!=0\`, compose F with the explicit inverse in Lemma 2. This is an affine-linear signed direction on O and preserves exactly the same \`75/32\` support gap. Thus FULL and LR four-observer convex hulls are unequal whenever LR rank is 4. On the singular surfaces observer rank<=3. QED.

The transported direction depends on parameters and its \`l1\` norm may diverge as \`w(z-v)->0\`; **75/32 is not a uniform normalized geometric distance** in observed coordinates. For any nondegenerate parameters, if \`h\` is the transported nonconstant coefficient vector, the witnessed infinity distance from \`conv(O_LR)\` is >= \`(75/32)/||h||_1\`. No equality or nonmembership assertion is made at singular parameters. No native X6/three-dimensional-slice embedding, physical bridge, formal theorem checker, mathematical admission or independent scientific review is claimed.

## Computation and continuation
Actually executed local standard-library \`fractions.Fraction\` program \`VERIFY.py\`; actual stdout in \`EXACT_OUTPUT.txt\`. It exhausts all **4096 FULL plus 16 LR** deterministic policy cylinders for probability normalization and the time identity, checks the five-point rank determinant, all LR support values and exact FULL witness, tests several rational nonsingular/singular observation determinants and inverse maps, and prints \`PASS_EXACT_R5_GLOBAL_THREE_RESPONSE_OBSERVER_NO_GO\`. The continuum conclusion comes from the displayed symbolic identities, full LR finite support table and multi-affinity, not finite parameter sampling.

**New structural scientific frontier:** the prior apparently five-feature \`(x,y,u,T_P,T_Q)\` polytope is constrained to a four-dimensional affine hyperplane for **every policy**. The response triple only makes a bijective observation of this 4D aggregate or a lower-rank quotient. Consequently more searches of the same 3-response cube cannot solve the full-rank equal-hull target. Change the carrier itself by adding an independently variable terminal-event statistic, e.g. \`Q(D)\` via a fourth legal shared error response, and first check whether FULL/LR aggregate rank actually increases. Then attempt all-four-dimensional support/equality certificates. See \`NEXT_TASK.md\`.
