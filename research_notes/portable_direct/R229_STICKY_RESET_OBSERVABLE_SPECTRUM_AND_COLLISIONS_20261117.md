# R229 — Stationary sticky-reset Markov source spectra: complete observable collision classification

Date: 2026-11-17 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Native BRC EffectHistogram integration: NOT_EXECUTED.

## Provenance, scope and source firewall

Continue R215, R221, R225 and R228, using unchanged frozen science pin awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Exact predecessor R228: awdawmip/enterprise-math@5a50387e02970a245848789707285a43edffcea2; R225: @de85fb7ea7a22924a4813c6a8a274432670645b2. Current procedural instructions have been read separately and do not repin scientific input.

This theorem concerns the scalar expected principal-ideal-cardinality observer of the abstract paired-event monoid J_(m,k,L). It does not claim a native physical X6 dynamical law or permission to erase source, branch, port, sign, joint relation, provenance, exact rational weight, multiplicity or cross-moment carriers of typed BRC EffectHistogram. Those remain explicitly preserved separately.

## Exact model

Assume integers m,k,L>=1, source labels 0,1,...,k with 0 neutral. Fix pi_i>0, sum_i pi_i=1, and holding probabilities 0<alpha_i<1. Values of alpha_i may repeat. The stationary sticky-reset source chain is

    P_ij = alpha_i * delta_ij + (1-alpha_i) * pi_j
    Z = sum_i pi_i/(1-alpha_i)
    rho_i = pi_i/((1-alpha_i)*Z).

For each U subseteq [k], let D_U={0} union U, P_D the corresponding killed submatrix. Using the exact R215 Stirling weights

    W_r = r! m^L sum_{j=0}^{min(r,L)} Stirling2(L+1,j+1) > 0,

the source-support scalar ideal readout for all n>=L is

    f_n = sum_{U subseteq [k]} W_|U| rho_D P_D^(n-1) 1_D.     (1)

Stationary reversibility yields a symmetric representation

    K_D = diag(sqrt(rho_i)) P_D diag(1/sqrt(rho_i))
        = diag(alpha_i : i in D) + a_D a_D^T,
    a_i = sqrt((1-alpha_i)*pi_i),
    b_i = sqrt(rho_i) = a_i/((1-alpha_i)*sqrt(Z)).

For each D, let G(D) be the distinct alpha values beta among indices i in D. For each beta set

    q_(D,beta) = sum_{i in D, alpha_i=beta} pi_i,
    t_(D,beta) = (1-beta)*q_(D,beta) > 0.

Define the degree-|G(D)| monic rational/real polynomial

    C_D(x) = product_{beta in G(D)}(x-beta)
          - sum_{beta in G(D)} t_(D,beta)
                product_{gamma in G(D), gamma!=beta}(x-gamma).       (2)

It is the characteristic polynomial of the observable holding-group-compressed matrix M_D = diag(beta)+u_D u_D^T, where u_beta=sqrt(t_(D,beta)).

## Theorem 1: exact minimal recurrence for all positive parameters

For any parameters above, including coincident alpha_i, the minimum order of a constant-coefficient scalar recurrence for the tail (f_n)_(n>=L) equals

    chi_obs(x) =
       monic_lcm( x-1, {C_(D_U)(x) : U proper subset of [k]} );
    d_min = deg chi_obs.                                          (3)

Equivalently, d_min is 1 plus the number of distinct eigenvalues appearing in all group-compressed proper killed blocks. Their spectral weights are strictly positive; hence eigenvalue coincidences are the entire mode-collapse mechanism. This yields

    d_min <= 1 + sum_{U proper subset of [k]} |G(D_U)|
           <= (k+2)2^(k-1)-k,                                   (4)

which is 250 when k=6 and distinct alpha_i maximize the block-count bound. The formula (3) classifies all parameter collision and repeated-holding strata exactly through polynomial gcd/lcm, avoiding any numerical tolerance.

### Proof

First, detailed balance holds: rho_i P_ij = pi_i*pi_j/Z for i!=j. Hence the symmetric K_D above has positive eigenvalues, because diag(alpha_i)>0. A proper killed block is strictly substochastic in the Perron sense: P has all positive entries, and deleting at least one state makes its spectral radius strictly below 1. Thus every eigenvalue of proper K_D belongs to (0,1); full P has stationary scalar mode 1.

Second, group the a_i having the same beta. The component of b_D in a beta-group is a fixed scalar multiple 1/((1-beta)*sqrt(Z)) of the a-vector in that group. Every intra-group vector perpendicular to a is therefore an eigenvector of K_D with eigenvalue beta, *and has zero b_D projection*. On the orthogonal span of normalized a-vectors for each beta, K_D restricts to M_D, whose characteristic polynomial is exactly (2).

Third, let lambda be an eigenvalue of M_D. For beta in G(D),

    C_D(beta) = -t_(D,beta) product_{gamma!=beta}(beta-gamma) !=0,

so lambda is not a holding pole beta. Eigenvalues satisfy the secular equation

    1 = sum_{beta in G(D)} t_(D,beta)/(lambda-beta).              (5)

On each interval avoiding poles the secular function has strictly negative derivative, and positive rank-one perturbation theory gives |G(D)| real, simple eigenvalues. An eigenvector for lambda has entries proportional to u_beta/(lambda-beta).

Fourth, the input vector in the grouped basis has coordinates c_beta=u_beta/((1-beta)*sqrt(Z)). Its eigenvector inner product is proportional to

    sum_{beta} t_(D,beta)/((1-beta)(lambda-beta))
      = sum_{i in D} pi_i/(lambda-alpha_i).                      (6)

Writing q_D=sum_{i in D}pi_i, equation (5) is exactly

    (1-lambda) sum_{i in D}pi_i/(lambda-alpha_i) = 1-q_D.        (7)

For every proper D, q_D<1 and lambda<1. Thus (6) is nonzero: *all observable group-compressed eigenvalues in a proper block have strictly positive squared spectral masses*. The omitted intra-group eigenvectors have zero mass. In the full block, rho P^(n-1)1=1, so its contribution is solely the eigenvalue 1.

Finally, all W_|U| are strictly positive. Equal eigenvalue contributions from different U add, never cancel. Consequently f_n is a finite positive linear combination of lambda^(n-1) over precisely the distinct roots in (3), each lambda in (0,1]. These roots are positive and distinct after grouping. Its d_min-by-d_min Hankel matrix starting at n=L factors into a Vandermonde matrix, a positive diagonal matrix with entries c_lambda lambda^(L-1), and the transpose Vandermonde. Therefore the rank is d_min, ruling out every recurrence of lower degree; the lcm polynomial itself annihilates the sequence. QED.

## Theorem 2: adjacent source sets cannot share an observable mode

Let U and U'=U union {j} be both proper subsets of [k]. Then C_(D_U) and C_(D_U') are coprime.

Indeed, if a common eigenvalue lambda is not alpha_j, the secular sums for these blocks differ by the nonzero term (1-alpha_j)pi_j/(lambda-alpha_j), a contradiction. If lambda=alpha_j, the enlarged observable block has no eigenvalue at any holding pole, again a contradiction. This holds even when some alpha values repeat.

This is a cover-edge statement only. For an extension by multiple distinct sources, added terms may have opposite signs across the target lambda; we make no general claim of collision absence for all nested pairs.

## Exact rational incomparable-subset collision

Take m=1, k=2, L=2, with

    alpha=(1/5,1/3,1/2),
    pi=(11/56,25/56,20/56),
    rho=(11/73,30/73,32/73),
    W=(1,4,10).

The three proper source sets have precisely

    C_(D_empty)(x) = x - 5/14,
    C_(D_{1})(x)   = (x-3/4)(x-5/21),
    C_(D_{2})(x)   = (x-3/4)(x-2/7).

For lambda=3/4 the shared neutral-state secular contribution is 2/7; each exclusive source contributes 5/7, so both proper blocks have secular sum exactly 1. Hence

    chi_obs(x)=(x-1)(x-3/4)(x-5/21)(x-2/7)(x-5/14),
    d_min=5.

The family bound from (4) equals D_2=6, so this is a genuine 6-to-5 mode collapse with *three pairwise distinct holding coefficients*, positive transition probabilities and nonzero observable weight on the shared eigenvalue. This is an exact algebraic collision between incomparable source subsets.

The same distinct alpha with pi=(1,2,4)/7 has degree 6; alpha=(1/4,1/4,1/4) and uniform pi has degree 3; replacing m=1 by m=12 changes positive W_r but retains the witness degree 5. The R225 equal-alpha special case is recovered exactly by (2)-(3): for constant alpha, C_D(x)=x-[alpha+(1-alpha)q_D], and the degree is the number of distinct subset sums.

## Reproducibility

R229_sticky_reset_collision_check.py uses only the Python 3 standard library. Its independent verification routes are:

- exact Fraction arithmetic for stochastic transitions, stationary rho and source-mask propagation;
- exact rational polynomial Euclidean gcd/lcm of the reduced characteristic polynomials, with repeated-alpha grouping;
- exact recurrence annihilation and full Hankel rank of the predicted minimal degree;
- explicit rational witness identities, full-degree comparator and uniform equal-alpha comparator.

Run: python R229_sticky_reset_collision_check.py

The program outputs PASS and regenerates R229_sticky_reset_collision_check_verification.json. Author execution passed 69 regression parameter configurations for k=1,2,3, m=1,L=2, plus four named cases including m=12 (73 configurations in total). The general arbitrary-(m,k,L) assertion is supported by the proof, not inferred merely from this finite regression.

Boundary alpha_i=0 or 1, zero pi_i, nonstationary initialization and nonsticky Markov chains remain outside the theorem. Review=NOT_REVIEWED; formal Claim/Result/Foundation: NONE.

## Next research frontier

1. Classify dimensions and intersections of resultant collision loci gcd(C_D,C_E)!=1, including maximal mode loss for k=6 and repeated holdings; test multi-source nested-set collisions.
2. Compile the recurrence by streaming polynomial gcd/lcm without floating roots, then evaluate exact rational bit growth, preprocessing, multi-query costs and comparison with 256-state source-mask propagation and 250-dimensional linear realization.
3. Implement a read-only scalar ideal-size observer against typed BRC EffectHistogram, checking equivalence of the observer output while maintaining all native signed ports, branch identity, provenance, multiplicity, exact weights and cross-moments in the underlying carrier.
