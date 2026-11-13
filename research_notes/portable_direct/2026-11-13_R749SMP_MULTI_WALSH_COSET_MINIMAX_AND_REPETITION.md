# R749SMP — Sharp multi-Walsh quotient minimax and repeated-observation amplification

Date: 2026-11-13, Asia/Shanghai. Author-side independent abstract continuation of R749SMO.
Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (unchanged).
Predecessor: research_notes/portable_direct/2026-11-13_R749SMO_SINGLE_WALSH_MINIMAX_AND_HORIZON_AMPLIFICATION.md at 1ccc183cfc3517439672abab204755ec411ca8a3.
Current behavioral rules read separately; the source is not rebased.
Scope: finite abstract signed-source/Walsh observation kernels; NOT a native V29/V39 Cell/Link/Port event license or new X6 spatial dimension. Complete author-side algebra; independent mathematical review pending.

## 1. Sharp multiple-deletion quotient theorem

Let G=F_2^d (d>=1), chi_a(x)=(-1)^(a dot x), and mu be any probability prior on G. Fix an r-dimensional linear subspace W of retained Walsh characters, 0<=r<=d, with the constant character 0 in W. The decoder keeps exactly m_a(mu)=sum_x mu(x) chi_a(x), a in W, and may discard all other Walsh moments.

Put H=W^perp, and let C=G/H denote the 2^r cosets, each of size m=2^(d-r). By character orthogonality, the retained moments determine precisely the coset masses:
p_c(mu)=sum_(x in c) mu(x)=2^(-r) sum_(a in W) m_a(mu) chi_a(x_c)
for any representative x_c. Conversely, these masses determine all retained moments.

Let K(y|x) be any stochastic observer into a finite public output set Y; write K_x for its distribution on Y. A decoder D receives only these retained moments and outputs any probability law on Y. Define its minimax TV prediction loss
R_W(K) = inf_D sup_(mu in Delta(G)) TV(D(m_W(mu)), K mu).
For a coset c put rho_c(K)=min_(q in Delta(Y)) max_(x in c) TV(q,K_x).

**Theorem A.** For every finite G,W,Y,K as above,
R_W(K) = max_(c in G/H) rho_c(K).
This formula is exact and requires no independence among source masks or output columns. Each rho_c is an explicit finite linear program: minimize t over q_y>=0, sum_y q_y=1, with
K_x(A)-q(A)<=t for every x in c and every subset A of Y.
These are equivalent to TV(K_x,q)<=t, since TV(P,Q)=max_A(P(A)-Q(A)).
The retained quotient is prediction-lossless for every source prior iff K_x=K_x' whenever x and x' belong to the same coset.

**Proof.** Given retained coset masses p_c, compatible priors are exactly all conditional distributions on each coset. Choose a TV-Chebyshev center q_c attaining rho_c (existence follows by simplex compactness). The decoder D(p)=sum_c p_c q_c is a valid output distribution. For any compatible prior mu, its prediction loss is at most sum_c p_c rho_c<=max_c rho_c by convexity and the triangle inequality. Conversely, take a prior supported entirely in one selected coset c. All these priors have identical retained moments, while their output laws fill the convex hull of the columns K_x (x in c). Since TV(q,.) is convex, its maximum on that hull equals max_(x in c) TV(q,K_x). Every decoder therefore suffers at least rho_c for this retained-information fiber. Maximize over c. QED.

**Corollary B (perfect readout and erasure).** For the identity observer K_x=e_x, R_W(I)=1-1/m=1-2^(-(d-r)). For the observer K_alpha that outputs label x with probability alpha and otherwise a common erasure symbol * (0<=alpha<=1),
R_W(K_alpha)=alpha(1-1/m).
Proof: symmetrize any center q over permutations of the m labels in a coset, and move any probability mass outside the coset to *; these operations do not raise the maximum TV loss. A symmetric center has probability t/m on each coset label and 1-t on *. Its distance to every K_x is
[abs(alpha-t/m)+(m-1)t/m+abs(t-alpha)]/2.
This is minimized at t=alpha (check the linear pieces divided at alpha and m alpha), with value alpha(1-1/m). QED.

**Exact multiple-deletion counterexample.** For d=3, r=1 and K=I, each retained coset has four source labels. R_W(K)=3/4, while its largest compatible-output pairwise TV distance is 1. Hence R_W(K)>diameter/2=1/2. The sharp midpoint formula in R749SMO applies to deleting ONE nonconstant Walsh moment with every other moment retained; it does not generalize to arbitrary multiple-deletion fibers. This is a concrete eight-source witness.

**Corollary C (binary public output).** If Y={0,1} and u_x=K(1|x), then
R_W(K)=(1/2) max_c (max_(x in c)u_x - min_(x in c)u_x).
Indeed, TV between Bernoulli laws equals the absolute difference of success parameters, and the midrange is the exact one-dimensional Chebyshev center. For d=3,r=1 and u_x=(x+1)/10 with labels x=0,...,7, the exact loss is 3/10.

## 2. Infinite-horizon repeatability

Fix the hidden source x while executing the same public observer independently n times with fresh channel randomness. Retain the complete sequence of n outputs. Its column is K_x^(tensor n). For each coset c let k_c be the number of DISTINCT one-step probability columns among {K_x:x in c}, and k=max_c k_c. Equal one-step laws are counted as one public hypothesis.

**Theorem D (sharp horizon limit).** R_W(K^(n)) is nondecreasing in positive integer n, and
lim_(n->infinity) R_W(K^(n)) = 1-1/k.
In particular, when k=1 the quotient is exactly lossless for every horizon.

For k_c>=2, put
Delta_c=min_(P != Q among distinct K_x, x in c) ||P-Q||_infinity > 0,
s=|Y|.
The individual coset radius obeys, for every positive n,
1-1/k_c-2s exp(-n Delta_c^2/2) <= rho_c(K^(n)) <= 1-1/k_c.

**Proof.** Marginalizing the (n+1)-output record yields the n-output record. TV contraction under this deterministic map and Theorem A imply monotonicity of the optimal radius. For the upper bound, select one representative column for each of the k_c distinct laws, and use as center the uniform average of their n-fold product laws. Every source column equals one representative; its TV distance from this mixture is at most 1-1/k_c.

For the lower bound, classify an n-output record by comparing its empirical vector of output frequencies to each of the k_c distinct one-step columns in infinity norm (with deterministic tie breaking). Under each true column, an incorrect classification requires at least one empirical coordinate to differ from its true mean by at least Delta_c/2. Hoeffding's inequality plus a union bound gives classification error at most eta_n=2s exp(-n Delta_c^2/2). Push any putative center q through this classifier to a distribution v on k_c labels. Some label j satisfies v_j<=1/k_c. By TV contraction and the triangle inequality,
TV(q,K_j^(tensor n)) >= TV(v,e_j)-eta_n >= 1-1/k_c-eta_n.
Thus the displayed lower bound holds for every center. Since there are finitely many cosets, taking the maximum of their limits proves the theorem. QED.

The limit counts the genuinely distinguishable PUBLIC source behaviors inside a retained fiber, not the number of raw bits. This is a quantitative future-operation criterion for preserving or discarding historical residuals.

## 3. Exact computational evidence

Companion file R749SMP_COSET_MINIMAX_CHECK.py uses Python fractions.Fraction and deterministic seed 749016. It checks all 1<=d<=6, 0<=r<=d, with 16 strictly positive rational source priors and 16 binary-channel profiles per dimension pair, five erasure probabilities for 1<=d<=5, and four binomial sample sizes. The program reports 8,483 counted exact validation cases (including 16 exact classifier-hypothesis error calculations), plus separate global consistency assertions; every Python assertion passes. Fraction arithmetic is exact for coset Walsh inversion, binary midranges, TV, erasure, and binomial classifier errors. Only reported decimal approximations use floating point.

For d=3,r=1,K=I: exact loss 3/4. For binary u_x=(x+1)/10: exact loss 3/10. For four distinct Bernoulli columns 0,1/3,2/3,1, k=4 so the asymptotic loss is 3/4; an explicit nearest-frequency classifier has exact worst error 2977/6561 for n=8 and 6267548402980196919710902699/1144561273430837494885949696427 for n=64, approximately 0.00547594. Full reproducible output is in R749SMP_COSET_MINIMAX_RESULTS.json. The universal conclusions are established by the proofs above; finite tests cover the stated parameter grid.

## 4. Remaining research

For retained Walsh families that are not subspaces, solve the affine-fiber Chebyshev minimax problem and identify efficient exact LP reductions. Then extend to adaptive feedback composition instead of only IID repeatable kernels. Native V29/V39 event kernels and the BRC provenance map must be extracted from licensed Source events before interpreting this as an X6 event theorem. Independent review is pending.
