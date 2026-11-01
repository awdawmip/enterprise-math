# BRC N=4 / S23 — rigorous 11D cell bound, anisotropic mesh error, sharp 2D witness

2026-11-01. Author-side proof and exact-rational computation. Status: UNREVIEWED / NOT_ADMITTED. This is a finite six-source statistical stopping-time theorem and a certification method, not a native P000 dynamics theorem or a resolution of R_beh(k,10).

## Model, observer and quantifiers

Six latent sources x=(AU0,AU1,AV,BU0,BU1,BV), six preparations, and four stopping times are retained exactly. The nonnegative row-stochastic BRC mixing matrix is M=M20/20 with

~~~text
M20 = [[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
       [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]].
~~~

The legal S23 behavioral policy has 11 real parameters theta=(aA,aB,bU,bAV,bBV,c0,c1,c2,c3,c4,c5) in [0,1]^11. The first-stage group is A for x=0,1,2 and B for x=3,4,5; the second-stage information set is h=(U,U,AV,U,U,BV). The per-source stopped law is

~~~text
Fx(theta)=(ag, (1-ag)bh, (1-ag)(1-bh)cx, (1-ag)(1-bh)(1-cx))
pi(theta)=sum_x M[i,x] Fx(theta).
~~~

Fix ahead of theta any row-stochastic common encoder E (with any finite number k of states) and any finite bank of row-stochastic decoder kernels D_l. The decoded preparation law q_li=(M E D_l)_i is independent of theta. The label l is selected after the policy but before observing the stop time. Define TV(u,v)=sum_t |u_t-v_t|/2, L_l(theta)=max_i TV(p_i(theta),q_li) and G(theta)=min_l L_l(theta).

## Theorem A. Sound exact continuum certificate on any rational or real rectangle

For every coordinate box Q=product_j [u_j,v_j], including lower-dimensional fixed-coordinate faces, let V(Q) be its distinct corners. Then

~~~text
LOW(Q) = max_(v in V(Q)) G(v)
       <= sup_(theta in Q) G(theta)
       <= UP(Q) = min_l max_(v in V(Q)) L_l(v).
~~~

Proof. For each latent source, every entry of Fx is affine in each individual control; although controls are shared across sources, no control is repeated on a single causal path. Every preparation p_i is therefore multiaffine. On Q the same nonnegative barycentric weights w_v(theta), summing to 1, satisfy p_i(theta)=sum_v w_v(theta)p_i(v) for all i. For a fixed decoded law q_li, total variation is convex in its first argument, so TV(p_i(theta),q_li)<=sum_v w_v TV(p_i(v),q_li). Taking max_i gives L_l(theta)<=max_v L_l(v) for each fixed l, and selecting one common l for the entire box gives UP(Q). The lower bound follows by evaluating actual corner strategies. In general max_v min_l L_l(v) cannot replace min_l max_v L_l(v) on the upper side: the preferred label can vary among corners. QED.

## Theorem B. Explicit source-sensitive continuity and grid error

Let A_j be the subset of sources whose causal stopping law uses parameter j, and set lambda_ij=sum_(x in A_j) M[i,x]. For all real legal theta,phi,

~~~text
TV(p_i(theta),p_i(phi)) <= sum_j lambda_ij |theta_j-phi_j|,
|G(theta)-G(phi)| <= max_i sum_j lambda_ij |theta_j-phi_j|.
~~~

Proof. Change the coordinates one at a time, keeping the others fixed. The TV effect on a source law of changing a is |delta a|; for changing b it is (1-a)|delta b|; and for changing c it is (1-a)(1-b)|delta c|. Each is bounded by the corresponding coordinate change. Positive row-stochastic mixing M and the triangle inequality give the first bound. For each fixed decoder, reverse triangle inequality bounds changes of each TV loss; finite max_i and min_l preserve the same uniform modulus. QED.

For widths h_j=v_j-u_j, rounding every free coordinate of theta to its nearest endpoint gives some corner v with |theta_j-v_j|<=h_j/2, whence the certified gap

~~~text
0 <= sup_Q G - LOW(Q) <= (1/2) max_i sum_j lambda_ij h_j.
~~~

Each source has exactly 3 controls and every row of M sums to one, hence sum_j lambda_ij=3 for all six i. Thus any uniform mesh of spacing h gives global grid underestimate at most 3h/2. For a nonuniform mesh or a face, use the sharper coefficient-weighted formula above. An adaptive finite subdivision with exact rational vertex losses is sound: if r is strictly above the fixed-bank supremum, sufficient refinement gives UP<=r on every cell; if r is strictly below it, sufficient refinement produces LOW>r on some cell. Equality may not terminate. Indeed, for a chosen cell vertex v0 and a label minimizing L at v0, all its other corner losses are <=G(v0)+max_i sum_j lambda_ij h_j, giving convergence of UP as widths tend to zero.

## Theorem C. Sharp two-control missed interior and finite four-cell repair

Take the legal S23 face bU=bAV=bBV=0, c=(0,1,1,1,0,1), and let s=aA and t=aB vary independently on [0,1]. Set the common encoder to the identity on six sources (k=6). Fix four source-specific decoders D_(alpha,beta), for (alpha,beta) in {0,1}^2: D_(alpha,beta) assigns to each source precisely its stopped law at the face parameter pair (alpha,beta). These are four fixed stochastic kernels; M is used in both actual and decoded preparation distributions.

For every A preparation, actual and decoded conditional distributions on the residual times 3 and 4 agree; only the mass of time 1 changes from s to alpha. The TV distance is exactly |s-alpha|, including the mixed AU0/AU1 rows. For every B preparation it is |t-beta|. Both A and B preparations occur, so

~~~text
L_(alpha,beta)(s,t) = max(|s-alpha|,|t-beta|),
G(s,t) = max(min(s,1-s),min(t,1-t)).
~~~

All four corners of [0,1]^2 have G=0, whereas at (1/2,1/2) the loss is 1/2. Consequently a corner-minimum grid misses the exact continuum worst loss by 1/2, achieving equality in the nearest-vertex bound of Theorem B for this face. For the whole square, UP=1 because any single decoder mismatches an opposite corner. After splitting at s=t=1/2, each of the four closed quadrants admits the fixed decoder associated with its adjacent outer corner and its worst corner loss is exactly 1/2. Theorem A now proves loss <=1/2 throughout all four quadrants; the center attains 1/2. Thus the exact supremum on this two-dimensional continuum is 1/2, **proved with a finite sound cell certificate**, despite the misleading zero loss on the four original corners. QED.

## Exact executable verification and limits

The sibling VERIFY.py was executed using Python standard-library Fraction without any float threshold. It verified a full 2048-corner multiaffine barycentric identity at one nontrivial rational 11-vector, 81 exact 2D face grid comparisons against the closed form, six lambda row sums, mixed AU/BU weights, whole-cell and four-quadrant UP bounds, and the attaining center. RUN_EVIDENCE.txt records its stdout. The real-parameter conclusions follow from the proofs above, not from finite sampling.

For ongoing k=4/6, m=10 research, Theorems A and B supply a rigorous certification method for any **frozen** ten-decoder bank, including shared-source mixing and behavior randomness. Theorem C itself uses four labels and k=6 and does not alter the as-yet-open unrestricted interval [1/2,2/3]. An unrestricted lower bound must quantify over all encoders and all banks. S2 information-set legality and P000's native X6 Cell/independent-time transfer remain separate proof duties; none of these six latent statistical sources is identified with a native P000 spatial axis. No formal or independent review is claimed.
