# R225 — Nonuniform reset Markov source ideal spectra: collision classes and sharp 64-mode witness

Date: 2026-11-17 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Physical BRC EffectHistogram: NOT_EXECUTED.

## Scientific inputs and declared scope

Frozen task-science pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Direct preceding results: R215 (Stirling-fibre ideal sizes), R221 (killed-Markov survival decomposition), R223 (uniform exchangeable spectrum, degree 7), R224 (unrestricted positive Markov kernel, generic degree 250). This R225 work concerns only the scalar source-support principal-ideal observable of the abstract paired-event observer J_(m,k,L). Its observation/readout is not a physical X6 state codec, full 21-bit event-action codec, native BRC update, signed phase, branch history, joint source relation, port/multiplicity carrier or physical mass transport. Full native relations remain separately typed and preserved.

Assume integers m>=1,k>=1,L>=1. There are k+1 labels 0,...,k with 0 neutral and m direction choices. Let S_n subseteq [k] denote the nonneutral source labels seen in the first n events. For all n>=L the fully filled tail's principal ideal cardinality equals F_n=T_|S_n|, where the established R215 weights and inclusion transform are

    W_r=r! m^L sum_(j=0)^min(r,L) Stirling2(L+1,j+1)>0,
    T_r=sum_(s=r)^k binom(k-r,s-r) W_s,
    T_|S|=sum_(U subseteq [k], S subseteq U) W_|U|.          (Z)

Let pi=(pi_0,...,pi_k) be a positive probability vector and alpha<1. Define a reset Markov source kernel

    P_ij=alpha delta_ij+(1-alpha)pi_j.                      (P)

It is nonnegative and row-stochastic exactly when -pi_min/(1-pi_min)<=alpha<=1, where pi_min=min_i pi_i; its interior is strictly positive when alpha exceeds the lower bound and alpha<1. Use the stationary initial row pi. Direction realizations may be arbitrary conditional on this exact source marginal.

For U subseteq [k] define D_U={0} union U, q_U=pi_0+sum_(i in U)pi_i, lambda_U=alpha+(1-alpha)q_U, and c_U=W_|U|q_U>0.

## Theorem 1 — Exact spectrum and complete monotonicity

For every n>=L,

    f_n=E[F_n]=sum_(U subseteq [k]) c_U lambda_U^(n-1).     (1)

Every lambda_U belongs to [0,1]. For all n>=L and j>=0,

    (-1)^j Delta^j f_n
      =sum_U c_U lambda_U^(n-1)(1-lambda_U)^j >=0.          (2)

Consequently the observable tail is a positive finite Hausdorff moment sequence; its Hankel matrices are positive semidefinite. It obeys log convexity f_n^2<=f_(n-1)f_(n+1) whenever all three terms lie in the tail. This remains true for admissible negative alpha, even though P has k negative eigenvalues equal to alpha.

Proof: The killed submatrix on D_U is P_U=alpha I+(1-alpha)1 pi_D^T. The restricted stationary initial row pi_D^T is a left eigenvector of P_U with eigenvalue lambda_U. Thus

    Pr(S_n subseteq U)=pi_D^T P_U^(n-1)1
                       =q_U lambda_U^(n-1).

Taking expectation of (Z) gives (1). Since lambda_empty=P_00>=0, q_U>=pi_0, alpha<1, and q_U<=1, we have 0<=lambda_U<=1. Equation (2) follows by finite differences, and Cauchy–Schwarz applied to the positive atomic measure gives the other properties. QED.

## Theorem 2 — Sharp recurrence degree and all collision strata

Let G be the set of distinct lambda_U and group repeated eigenvalues with positive coefficients C_lambda=sum_(U:lambda_U=lambda)c_U. Define

    G_L={lambda in G:lambda>0}
        union ({0} if L=1 and 0 in G, otherwise empty).

The minimum constant-coefficient recurrence order of the tail (n>=L) is exactly

    d_L=|G_L|,
    chi_L(x)=product_(lambda in G_L)(x-lambda).              (3)

For all alpha<1, two modes coincide exactly when the nonneutral subset sums coincide:

    lambda_U=lambda_V
      iff sum_(i in U)pi_i=sum_(i in V)pi_i.                (4)

In the strictly positive-kernel interior all lambda_U>0; the minimum degree equals the number of *distinct subset sums* of pi_1,...,pi_k. It is generically 2^k: the exceptional parameters are contained in the finite union of proper affine subset-sum collision hyperplanes. If all k nonneutral probabilities are equal, the degree is k+1. The alpha=1 static-kernel boundary instead has degree 1. At lambda_empty=0, the zero eigenvalue contributes a one-step impulse if L=1 and is absent from the tail if L>=2.

Proof: After combining identical modes, for any d=|G_L| the d-by-d Hankel matrix of the tail factors as

    H_(i,j)=f_(L+i+j)
           =V diag(C_lambda lambda^(L-1)) V^T,
    V_(i,lambda)=lambda^i, 0<=i<d.

Use 0^0=1 for the L=1 boundary. Every retained diagonal entry is positive and the Vandermonde determinant is nonzero, so H has rank d. A recurrence of order <d would make this matrix rank deficient. chi_L annihilates the tail, giving equality. Equation (4) follows because 1-alpha>0. With positive pi, each collision between unequal subsets defines one proper hyperplane, and finitely many such hyperplanes cannot cover the positive probability simplex. Binary-weight vectors give explicit noncollision points. QED.

For k=6, the progression of *scalar* observable minimal orders is R223 exchangeable: 7; R225 generic reset, nonuniform pi: 64; R224 unrestricted positive stochastic Markov kernels: 250. This classification is parameter-conditional and preserves the distinct full-state query and BRC-carrier types.

## Theorem 3 — Exact leading spectral relaxation

Assume alpha<1, positive pi, and define p_*=min_(1<=i<=k) pi_i, t=# of nonneutral i attaining this minimum. The exact limit is lim_(n->infty)f_n=W_k. The maximum eigenvalue of a proper U subsetneq[k] is

    rho=1-(1-alpha)p_* in [0,1).

When rho>0,

    f_n-W_k=t W_(k-1)(1-p_*)rho^(n-1)+o(rho^(n-1)).        (5)

If rho=0 the tail reaches its limit after finite steps. Proof: among all proper U, the largest q_U results from omitting exactly one nonneutral label with minimum pi; these t modes have the same positive coefficient W_(k-1)(1-p_*), and every other proper mode has smaller eigenvalue. QED.

## Six-source native-direction alphabet witness: exact degree 64

Choose (m,k,L)=(12,6,2), pi=(1,2,4,8,16,32,64)/127 and alpha=1/4. With s(U)=sum_(i in U) 2^i for i=1,...,6, the s(U) are precisely the 64 even integers 0,2,...,126; hence

    q_U=(1+s(U))/127,
    lambda_U=(130+3s(U))/508.

There are 64 strictly positive, pairwise distinct modes. W=[144,576,1440,4320,17280,86400,518400]; minimal degree is exactly 64. The asymptotic ratio rho=251/254, leading coefficient 10800000/127, and limiting ideal cardinality 518400.

Exact check values:

    f_2  = 17478964872/16129
    f_3  = 2083322540628/2048383
    f_4  = 251482108027194/260144641
    f_12 = 1759150558550710811224562876602317/2253484738076257826811740288

Independent modular Hankel full-rank certificates from 64 exact rational moment atoms (all denominators invertible):

    mod 1000000007: det(H_64)=651567929, rank 64
    mod 1000000009: det(H_64)=632163607, rank 64.

The positive-Vandermonde argument proves rank over Q; each nonzero modular determinant also supplies a finite exact certificate for this witness.

## Reproduction and evidence

The companion standalone standard-library script R225_nonuniform_reset_spectral_check.py uses Python Fraction and integers only. Running it regenerates R225_nonuniform_reset_verification.json. It passed 216 rational parameter configurations (k=1..3, m in {1,12}, L=1..3, three initial-distribution variants and four admissible alpha choices), 1084 exact dynamic-support versus spectral comparisons including four k=6 examples, 216 finite Hankel rank tests, 4320 alternating-difference tests, and two exact 64x64 modular determinant checks. No floating approximations are used.

The preceding general claims are supported by the written algebraic proofs, with the finite computations serving as regression checks and explicit witnesses. The source model has exact rational probabilities and a 64-atom representation; input conversion, large-integer bit cost and physical BRC EffectHistogram integration have not been benchmarked. Independent review: NOT_REVIEWED. Task CLAIM, Result, Review, Foundation admission: NONE.

## Next unresolved units

1. Classify the sharp recurrence order of partially lumpable, reversible but nonreset, and block-symmetric seven-state source kernels.
2. Compare 64-atom scalar evaluation with full 256-state cumulative-support/current-source transfer and 250-dimensional general reduced linear realization, including conversion, precision, and rational bit-growth.
3. Add a *read-only* support-ideal observer to native typed BRC EffectHistogram, preserving signed ports, multiplicities, branch identity, provenance and cross-moments; permit a many-to-one state projection only after a future-operation safety certificate.

Scientific conclusion scope: scalar, source-support query of the abstract J_(m,k,L) monoid under stationary reset Markov inputs and the R215 ideal weights, not a primitive-native six-dimensional physical evolution statement.