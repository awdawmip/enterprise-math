# BRC N=4: policy-uniform conditional sufficiency and exact pathwise memory gap

2026-10-30. AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED. This theorem applies to the frozen external finite 16-leaf P/Q experiment, conditional on BU. It neither establishes native P000 X6 dynamics nor claims mathematical admission. Frozen antecedent: PR #1757, head 022dbc470b1fe01d57d394ad197e3ae800be3938.

## Frozen source and lawful-operation scope

For s in (AU,AV,BU,BV), j,k in {0,1}, let Q(s,j,k)=q_s/4 and P(s,j,k)=q_s r_(s,j)/4. Here q=(1/6,1/3,1/4,1/4) and r_AU=(9/10,11/10), r_AV=(1/4,1/4), r_BU=(1/5,9/5), r_BV=(2,2). Each law has sixteen strictly positive leaves and total mass one. Both have BU mass 1/4. Conditioning on BU yields

\[
Q(J=j,K=k)=1/4,\quad P(J=j,K=k)=r_j/4,\quad r_0=1/5,\quad r_1=9/5.
\]

K is fair given J for each source law. The auxiliary source sensor is Z=J xor Bernoulli(epsilon) with independent noise 0<=epsilon<=1/2. We study a finite, possibly randomized encoder E_z(s|j,k) with a single output S, common to P and Q, and a reverse kernel R(j,k|z,s) also common to both. The reconstruction target is the *complete joint conditional law* of (Z,J,K), not just separate marginals, after retaining observed (Z,S).

Frozen original behavioral S2/S23 permits stop/continue decisions on contemporaneous information; on reaching T4 it reads the pre-sampled K and makes a terminal P/Q decision. S23 further equates equal-likelihood-ratio action kernels, so its terminal decision at fixed J must be independent of K. In this *specified four-stage experiment*, there is no transition kernel that rewrites K or a hidden leaf, and the T4 terminal event is absorbing. An additional postterminal read or intervention is not part of this grammar unless independently declared. Theorems below do not manufacture such an operation.

## Theorem A: all-encoder exact reversible quotient criterion

For every epsilon in [0,1/2] and every finite randomized common encoder E, the following are equivalent.

(1) A common reverse kernel R exactly recovers P_(Z,J,K) and Q_(Z,J,K) from their respective (Z,S) distributions.

(2) For every output (z,s) with positive probability, its encoder preimage of positive Q-weight contains only one J value.

(3) J is a function of (Z,S) almost surely under both P and Q.

Thus if 0<epsilon<=1/2, the sets of S labels accessible from J=0 and J=1 must be disjoint **for each z**. At least two S labels are necessary and S=J attains the bound; it is causal already at T3. If epsilon=0, J=Z, and a constant S already suffices. The lower bound holds even for randomized encoders, not merely deterministic partitions.

*Necessity.* On the conditional BU raw state x=(j,k,z), the density ratio P(x)/Q(x) is r_j wherever Q(x)>0. P-Q has strictly negative sign for J=0 and strictly positive sign for J=1. The raw total variation distance is exactly 2/5. A reversible encoder and decoder gives the data-processing chain

\[
2/5=TV(P_{\rm raw},Q_{\rm raw})\le TV(P_{Z,S},Q_{Z,S})\le 2/5.
\]

The TV triangle inequality is equality under E only if no output (z,s) mixes contributions with positive and negative signed masses. Since the magnitude of each signed contribution is nonzero on the source support, this forces J to be uniquely determined by (z,s). This reasoning applies to arbitrary nonnegative stochastic E entries.

*Sufficiency.* If all positive contributors at (z,s) have the same J, r_J is constant over that fiber. Therefore the raw conditional posterior given (z,s) is identical under P and Q. Define R(j,k|z,s)=Q(J=j,K=k|Z=z,S=s) on outputs of positive mass, arbitrary on null outputs. The same R reconstructs both raw joint distributions, and in fact the complete coupling (Z,S,J,K). QED.

**Policy-uniform consequence.** Any finite well-defined source-independent *causal* S2/S23 transcript kernel H on the declared (J,K,Z) source, using independent behavioral coins and reusing an actually read K consistently, can be composed with this common R. The joint generated law of (Z,S, transcript) then equals the original under P and Q. To implement causal decisions, the sufficient S must be available before the corresponding action; the optimal S=J satisfies this at T3. More general encoders that depend on K are mathematical post-read encodings, not an authorization to use unseen K prematurely. A source-independent auxiliary read-only H can also be composed, but does not become a lawful original postterminal action.

## Theorem B: exact noise-induced statistical loss

The raw BU two-law TV is 2/5 independently of epsilon, while

\[
P(Z=0|BU)=1/10+4\epsilon/5,\quad Q(Z=0|BU)=1/2,
\]
\[
\boxed{TV(P_{Z|BU},Q_{Z|BU})=\frac25(1-2\epsilon),\qquad
TV_{\rm raw}-TV_Z=\frac45\epsilon.}
\]

Since both laws assign BU mass 1/4, its unconditional TV contribution falls from 1/10 to (1-2epsilon)/10; the exact missing discrimination is epsilon/5. The repair S=J restores the raw *statistical* joint experiment. This data-processing gap must not be misreported as an actual-path prediction error.

## Theorem C: sharp gap to authentic-path recovery

If the decoder must recover the actual realized (J,K) rather than generate its *law*, at positive epsilon it needs at least four S symbols; at epsilon=0 it needs at least two. These are attained respectively by S=(J,K) and S=K. This holds even for stochastic encoders and decoders: for each fixed observed z, exact almost-sure recovery makes the encoder output supports for each distinct possible raw (J,K) pair disjoint. At positive epsilon all four pairs have positive mass at every z; at zero epsilon exactly two K values remain at each z.

With the statistically optimal S=J and no old K-dependent side information, the original K remains fair given (Z,S), so every predictor using fresh independent randomness misses the *actual* K with probability 1/2 on a reached T4 BU path. If branch J=0,1 continues to T4 at respective K-independent rates u,v in [0,1], then

\[
P(T4,BU)=(u+9v)/40,\qquad Q(T4,BU)=(u+v)/8,
\]
\[
\boxed{\inf_{\widehat K}\max_{L=P,Q}
\Pr_L(\widehat K\ne K,\ T4,\ BU)
=\tfrac12\max\{(u+9v)/40,(u+v)/8\}.}
\]

This generalizes the previously computed u=0,v=1 value 9/80 to *all real continuation rates*. It separates distributional reconstruction using a freshly sampled, retained fair K from authentic fixed-path memory. Neither K nor J is a seventh native spatial dimension.

## Exact validation, scientific and governance limits

VERIFY.py was actually executed using Python Fraction. It reconstructs each strictly positive 16-leaf distribution and checks four rational epsilons (0, 1/4, 1/3, 1/2), all 256 deterministic binary encoders E on (J,K,Z), the exact TV criterion, common S=J reconstruction for P and Q, and S2/S23 stagewise causal transcript kernels. It checks three sharp rational realized-K examples. The all-real, all-finite-randomized-encoder and arbitrary finite causal-kernel statements are proved by the signed-mass/data-processing argument and kernel composition; the finite grid is only an implementation crosscheck.

This is a concrete source-provenance BRC example of common Markov-kernel statistical sufficiency, not a novel proof of Blackwell's general experiment comparison. External positioning: Khan, Yu, Zhang, *Economics Letters* 247 (Feb 2025), 112146, DOI 10.1016/j.econlet.2024.112146. Rosenthal, *Economic Theory Bulletin* 14, 4 (2026-03-17), DOI 10.1007/s40505-026-00307-6, gives a distinct prior-free ranking, not an exact inverse-kernel theorem for this source.

Native P000 V5 six-axis Cell/path, three-dimensional 晶包 layer, independently typed time, and physically meaningful operations require a separately established commuting bridge. This result has no live canonical Owner CLAIM, native Result, independent Driver review, Lean verification, or theorem admission.
