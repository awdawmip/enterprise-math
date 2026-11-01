# BRC N=4 / S23: certified open neighborhood of a strict lawful–hull Chebyshev gap

Date: 2026-11-01. Status: AUTHOR_ANALYTIC_PROOF / EXACT_BIGINT_EXECUTED / UNREVIEWED / NOT_ADMITTED. This independently verifiable perturbation certificate continues the exact frozen model of enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34 (PR #1765). It studies the joint SIX-preparation observation, not independently adjustable rows.

## Model and immutable scientific input

Keep six separately typed positive BRC sources AU0, AU1, AV, BU0, BU1, BV. Each has a four-stop distribution
\[
F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)).
\]
The six preparation rows use the positive mixture matrix with integer rows 20M=(10,10,0,0,0,0); (9,11,0,0,0,0); (0,0,20,0,0,0); (0,0,0,10,10,0); (0,0,0,2,18,0); (0,0,0,0,0,20). Parameter b=b_U is SHARED by the A and B source branches; retain source labels even when this particular freeze makes some statistical distributions coincide.

Freeze a_B=1/4, b_AV=0, b_BV=1/3, and all c controls except c_AV to 1/2. Legal varying controls are (a,b,c)=(a_A,b_U,c_AV). The original real box is
\[
Q=[1/2,7/8]\times[1/8,1/2]\times[1/2,7/8].
\]
Let P(θ) be the SIX rows of four-stop laws. The joint metric is D(P,P')=max_{i=1}^6 TV(P_i,P'_i), with TV=one-half the l1 distance. Define A_Q={P(θ):θ∈Q} and
\[
R_{\rm lawful}(Q)=\inf_{Z\in A_Q}\sup_{X\in A_Q}D(X,Z),\quad
R_{\rm hull}(Q)=\inf_{Z\in\operatorname{conv} A_Q}\sup_{X\in A_Q}D(X,Z).
\]

## New theorem: explicit six-endpoint open-neighborhood stability

Let Q' be ANY real parameter box whose six lower/upper endpoints deviate individually by at most δ from the matching endpoints of Q, where 0≤δ≤1/1024. (All such endpoints are within [0,1] and remain ordered.) Then
\[
\boxed{R_{\rm lawful}(Q')-R_{\rm hull}(Q')>1/160-6\delta.}
\]
In particular, **every** such perturbed box, including irrational endpoint boxes, has
\[
\boxed{R_{\rm lawful}(Q')-R_{\rm hull}(Q')>1/2560>0.}
\]
More generally, the first strict inequality holds whenever 0≤δ<1/960 and the six endpoints remain legal. This provides a concrete full six-dimensional neighborhood of boxes, not a single isolated counterexample.

### Lemma A: source-aware pairing of changed boxes

Write each coordinate of θ∈Q in the form lower_j+(upper_j−lower_j)t_j for t∈[0,1]^3. Pair it with θ'∈Q' using the SAME t_j. Every coordinate changes by at most δ. Conversely, every θ' has such a paired θ.

Couple Bernoulli stopping decisions with the same independent uniforms in the two policies. For sources AU0, AU1 the only changing stages are (a,b); for AV they are (a,c), with its intervening second-stage control identically 0. On matched policies the probability of different final stop labels is at most
\[
|a-a'|+[1-\max(a,a')]|v-v'|
\leq \delta+\tfrac12\delta=3\delta/2,
\]
where v=b or c. The key improvement over a global three-stage modulus is that the original member has a≥1/2, so joint survival past stage one is at most 1/2. For BU0, BU1 only b changes, yielding TV≤(3/4)δ; BV is constant. Convexity of total variation under the unchanged positive mixture rows yields
\[
\boxed{D(P(\theta),P(\theta'))\leq\eta:=3\delta/2.}
\]
This is an ALL-REAL uniform pairing statement. It implies Hausdorff distance d_H(A_Q,A_Q')≤η.

### Lemma B: radius stability, including joint convex hull

For nonempty compact A,B,C,E in any normed affine space, if d_H(A,B)≤η and d_H(C,E)≤η, then
\[
\left|\inf_{z\in C}\sup_{x\in A}\|x-z\|-
\inf_{w\in E}\sup_{y\in B}\|y-w\|\right|\leq2\eta.
\]
Indeed, match each center within η and each adversary within η, apply the triangle inequality, then reverse the roles. Convex hull is nonexpansive for Hausdorff distance in a normed space: map the SAME finite convex weights across η-close matched points. Thus both C=A_Q (lawful) and C=conv A_Q (hull) satisfy the lemma. Therefore
\[
|R_{\rm lawful}(Q')-R_{\rm lawful}(Q)|\leq2\eta,\quad
|R_{\rm hull}(Q')-R_{\rm hull}(Q)|\leq2\eta
\]
and their difference decreases by at most 4η=6δ. No assumption that the joint observation set is convex has been made.

### Lemma C: independent rational gap certificate at the base box

An explicit joint hull center is the convex combination of complete lawful observations with weights
\[
V=\tfrac49 P(1/2,1/8,7/8)+\tfrac1{18} P(1/2,1/2,1/2)
 +\tfrac29 P(7/8,1/8,7/8)+\tfrac5{18}P(7/8,1/2,1/2).
\]
All weights are positive and sum to one. Its AU, AV, BU, BV representative rows are respectively
\[
(11/16,1/16,1/8,1/8),\quad
(11/16,0,1/4,1/16),\quad
(1/4,3/16,9/32,9/32),\quad
(1/4,1/4,1/4,1/4).
\]
The other AU/BU preparations have the same distributions under this stated freeze, while their source labels remain distinct. Checking each of the eight corners establishes sup_{θ∈Q}D(P(θ),V)≤3/16. For each coordinate separately, the law P is multi-affine, and a convex norm of a one-coordinate affine map attains its maximum over that interval at an endpoint; repeated application proves that the eight-corner check covers all real θ. Hence R_hull(Q)≤3/16.

For ANY lawful center z=(x,y,t) with worst-case radius r, three event inequalities hold:
\[
r\geq7/8-x,\qquad
r\geq7/16-(1-x)(1-y),\qquad
r\geq(3/4)(1/2-y).
\]
The first and third give 1−x≤1/8+r and 1−y≤1/2+4r/3. Inserting their nonnegative product bound into the second gives
\[
32r^2+40r-9\geq0.
\]
This polynomial is strictly increasing for r≥0, and its value at r=31/160 is exactly −39/800. Consequently R_lawful(Q)>31/160. Since 3/16=30/160,
\[
R_{\rm lawful}(Q)-R_{\rm hull}(Q)>1/160.
\]
Combining Lemmas A–C yields the asserted strict gap >1/160−6δ. At δ=1/1024, exact fraction arithmetic gives 1/160−6/1024=1/2560.

## Executed verification and meaning

VERIFY.js uses exact reduced rational BigInt arithmetic, independently reconstructs the six source laws and six preparation mixture rows, verifies the four-vertex convex witness and its exact eight-vertex worst-case radius, checks the dual quadratic at 31/160, and verifies the exact positive 1/2560 neighborhood margin. It also compares 64 perturbed endpoint sign patterns, 1,728 matched rational parameter pairs, and 512 transported convex-center vertex inequalities. These finite checks validate source modeling and witness arithmetic; the real-continuum theorem follows from the explicit coupling, Hausdorff, and coordinatewise multi-affine arguments above.

Scientific interpretation: strict convexification error persists under actual perturbations to every endpoint while preserving shared causal controls and joint source observation. This is finite positive BRC/S23 statistics. Native P000 six-axis Cell/independent-time interpretation and full 11-control, ten-label minimax consequences require their own correspondence and minimax certificates. There is no native CLAIM, Result, independent review or mathematical promotion in this author-side proof.
