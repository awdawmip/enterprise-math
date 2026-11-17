# R5 — exact affine-transport no-go for the entire two-terminal-response family

2026-10-31 (Asia/Shanghai). Claim type: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is an auxiliary finite stopping-model theorem, not native X6 or a solution of the mother question.

## Frozen sources / scope

GLOBAL_KNOWLEDGE_V1 main@9baccc3601d519bcc3a85938cad66a1886102494 and Enterprise Math main@b0b289e4d42cd5df4831fc990910c9d39e622e9b. At those snapshots the bootstrap, operating manual, P000, ACTIVE residual-faithful worldview, mathematical/BRC policies, current control authority, and portable/autonomous research operations were read. Nothing protected is changed. Primary scientific predecessor: immutable commit 9dda1142caa6f4e167b9ca2c4b62a1fb7a05d332, research_notes/brc_r5_terminal_interpolation_rank4_20261031_t2043/RESEARCH.md and VERIFY.py.

All paths carry positive Q masses and the exact cylinder relation P=lambda*Q. Signed linear observer supports are not signed branch masses. The terminal response is a Bernoulli-error observable shared between FULL/LR and P/Q, not a source-specific physical claim.

## Model and full parameter domain

Two origins i=0,1, each P=Q=1/2 at A=(time 1, LR 1), choose STOP/CONTINUE. Under continuation, Q conditional routes D,C,Y have probabilities (a_i,1-2*a_i,a_i), likelihood ratios (1/2,1,3/2), time 2. D may STOP at D or CONTINUE to DH=(3,1/4) and L=(3,1) with Q weights (2/3,1/3). Y may STOP at Y or CONTINUE to YH=(3,2) and L with weights (1/2,1/2). C terminates at C=(2,1) with probability 1-k_i, otherwise proceeds to L with k_i. At L choose STOP at time 3 or CONTINUE to L4=(4,1). Fix (a0,k0)=(1/4,3/4), (a1,k1)=(1/5,1/6), satisfying the compensated-source theta=(1+k_i(1-2*a_i))/a_i=11/2.

FULL sees origin and route history (12 independent binary deterministic controls); real seedless LR sees current key A,D,Y,L (4 binary deterministic controls), no persistent seed. No control key is revisited in one history. There are 4096 FULL and 16 LR deterministic strategies, and every signed four-observer score is multi-affine in the underlying real behavioural controls. Thus all-real support maxima occur among those finite deterministic strategies. Naturals remain strictly positive, both laws normalize.

The four-vector is O=(eP,eQ,TP,TQ). All eight terminal keys have error response r=1/2, except r_DH=1/2+v, r_L4=1/2+w, for arbitrary real -1/2<=v,w<=1/2. Bernoulli errors are strictly interior for -1/2<v,w<1/2. The gamma necessary condition 2*r_C-r_A-r_L=0 holds throughout.

## Theorem (complete classification of this response family)

For EVERY real legal pair (v,w):

(A) If v*w != 0, the LR four-observer convex hull has affine dimension 4 yet is strictly smaller than the FULL four-observer convex hull. More precisely, the parameter-dependent signed direction

H(v,w) = (19/(3w)-23/(12v), 23/(12v)-19/(12w), 1, -2)

has exact support gap

sup_FULL H·O - sup_LR H·O = 37/240 > 0.

A particular maximizing FULL observer is

O_star(v,w) = (1/2+v/48+7w/24, 1/2+v/12+7w/24, 107/48, 107/48).

It is separated from the ENTIRE LR convex hull in infinity norm by at least

(37/240)/(|19/(3w)-23/(12v)|+|23/(12v)-19/(12w)|+3).

Five fixed LR deterministic policies A,D,Y,L = (0000),(1000),(1001),(1010),(1100) give a nonzero affine-difference determinant

det = 152361*v*w/40960000.

(B) If v*w=0, both actual observation images and their hulls have affine rank <=3. If v=0, eP=eQ; if w=0, eP-1/2=(eQ-1/2)/4. Thus there is NO pair within this complete square having both four-rank and four-hull equality.

This covers opposite signs, vanishing axes, and allowable response boundaries. The constant 37/240 refers to a direction which depends on (v,w); it is NOT a uniform gap under a fixed normalized norm as (v,w) approaches an axis.

## Complete analytic argument

For any strategy, put x=Q(terminal DH) and y=Q(terminal L4), preserving their positive, source-labeled constituent cylinders. Q/P normalization gives a common baseline 1/2 for both error observers. The terminal LR values give for every policy:

eP = 1/2 + (v/4)*x + w*y,
eQ = 1/2 + v*x + w*y.

Writing b=(1/2,1/2) and C(v,w)=[[v/4,w],[v,w]], the two-error pair is b+C(v,w)(x,y). The time pair (TP,TQ) is independent of v,w. The determinant det C(v,w)=-3*v*w/4. If v*w!=0, the common observer map in the FULL and LR models is the same invertible affine transformation from any other nonzero parameter pair, including the baseline (v0,w0)=(1/8,1/4). Therefore rank and convex-hull equality/non-equality, and equality of actual real observer images, are invariant across this nonzero locus. If v or w vanishes, the displayed error equations imply the rank-3 identities in part (B).

For a constructive all-real signed witness, at baseline use H0=(10,9,1,-2). The coefficients of (x,y) in its score, after removing the policy-independent baseline, equal

x: v0*(10/4+9)=23/16;
y: w0*(10+9)=19/4.

For arbitrary nonzero (v,w), choose H=(p,q,1,-2) such that v*(p/4+q)=23/16 and w*(p+q)=19/4. Solving yields exactly the displayed H(v,w). Consequently for EVERY strategy pi,

H(v,w)·O_pi(v,w) = H0·O_pi(v0,w0) + (p+q-19)/2.

The last term is independent of pi. Independent exact enumeration of all 4096 FULL and 16 LR binary controls at baseline gives the maxima 1685/192 and 2759/320 respectively, whose difference is 37/240. By the no-revisit multi-affine argument this exhausts ALL real behavioural controls. The transported H therefore has the same 37/240 gap for every nonzero real v,w, and the baseline FULL maximizer remains a maximizer.

That FULL strategy CONTINUEs at A for origin 0 and STOPs at A for origin 1, with all reached D,Y,L decisions CONTINUE. Its direct positive Q-flow calculations are Q(DH)=1/12, Q(L4)=7/24, and TP=TQ=107/48, giving O_star(v,w). Every LR-hull point z satisfies H·(O_star-z)>=37/240, while |H·(O_star-z)|<=||H||_1||O_star-z||_infinity. This proves the stated metric bound. The LR affine determinant follows by multiplying the baseline determinant 152361/1310720000 by det C(v,w)/det C(v0,w0), producing 152361*v*w/40960000. QED.

## Verification, evidence and boundary

The adjoining actually executed VERIFY.py uses Python standard-library Fraction. It reconstructs all 4096 FULL and 16 LR positive Q cylinder flows, verifies P/Q normalization, checks the exact baseline maxima, and tests the transported score identity policy-by-policy for five rational (v,w) pairs from multiple sign quadrants. For each, it checks the identical exact gap, maximizing FULL witness, four-rank determinant, and quantitative separation bound. For three axis pairs it checks affine-rank identities for all FULL deterministic strategies. The saved actual output ends with PASS_EXACT_R5_AFFINE_RESPONSE_TWO_PARAMETER_GLOBAL_NO_GO.

The theorem covering the entire real square follows from the invertible affine-transform proof and complete deterministic extreme-point reduction; it is not an extrapolation from five sampled parameter points. This is an author proof with exact reproducible tests, not formal-machine proof admission, peer review, originality priority, or native X6 transfer.

## Research consequence and next decisive experiment

The previous open full-rank separating v,w region is actually the ENTIRE nonzero (v,w) locus. This closes the complete two-response-feature search, not all eight-key terminal response choices satisfying gamma=0. Next allow a third independent response deviation (YH or D), preserve strictly positive P/Q kernels and BRC provenance, and determine exact all-signed hull equality using <=5-LR-point rational primal representations or exact Farkas separators. Only if all four-hulls coincide should actual seedless-LR real observer nonmembership be studied. See NEXT_TASK.md.
