# R226 — Reversible exchangeable non-reset Markov source observer: sharp 2k modes and block-orbit reduction

Date: 2026-11-17 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Native BRC integration: NOT_EXECUTED.

## Scientific inputs, typed interpretation

Frozen task-science pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Previous science: R215 exact ideal weights; R221 killed-Markov source-survival identity; R223 exchangeable reset degree 7; R224 generic unrestricted degree 250; R225 nonuniform reset degree 64.

This is a scalar ideal-cardinality observer on the abstract paired-event monoid J_(m,k,L). It is not a complete native X6/BRC operator or physical claim. Preserve source identities, branches, signed ports, multiplicities, exact rational weights and cross-moments before applying this many-to-one scalar observer. P000's six native spatial dimensions and three-dimensional slice remain unchanged.

Let m,k,L be integers >=1. There are k nonneutral sources and neutral source 0. Put

    W_r = r! m^L sum_(j=0)^min(r,L) Stirling2(L+1,j+1) > 0.
    T_|S| = sum_(U subseteq [k], S subseteq U) W_|U|.

For a full tail (n>=L), F_n=T_|S_n| where S_n is the set of sources observed in the first n source events. Hence

    f_n=E[F_n]=sum_(U subseteq [k]) W_|U| Pr(S_n subseteq U).        (0)

## Theorem A: exchangeable stationary reversible source kernel

Choose positive rational a,b,c,d,e with a+k*b=1 and c+d+(k-1)*e=1. Define a stochastic source matrix P:

    P_00=a; P_0j=b (j>=1);
    P_i0=c; P_ii=d; P_ij=e (i!=j, i,j>=1).

It is reversible with stationary probabilities pi0=c/(c+k*b) and pi_i=b/(c+k*b), since pi0*b=pi_i*c. This includes nonreset kernels with b!=e.

For each 0<=r<=k, define M_0=[a], u_0=[pi0]; for r>=1 define

    M_r = [[a,r*b],[c,d+(r-1)*e]],   u_r=[pi0,r*pi_i].

For n>=L:

    f_n=sum_(r=0)^k binom(k,r)*W_r*u_r*M_r^(n-1)*ones.           (1)

For r=k the inner survival is 1, so this block contributes constant W_k. Consequently f_n has a rational linear realization of dimension at most 2k and satisfies the polynomial recurrence

    Q(x)=(x-1)(x-a) product_(r=1)^(k-1) [(x-a)(x-d-(r-1)*e)-r*b*c].     (2)

Proof. For any allowed source subset U of size r, the killed matrix P_U and initial/final vectors are invariant under permutations of the r retained nonneutral labels. Their action on the invariant subspace is exactly M_r. All binom(k,r) subsets yield the same scalar survival. The r=0 block is 1-dimensional, partial r=1,...,k-1 blocks each need at most 2 dimensions, and the full r=k block is the constant scalar. Thus 1+2(k-1)+1=2k dimensions suffice, establishing (1) and (2).

## Theorem B: generic sharp degree 2k

Suppose k>=2; P, considered as a reversible self-adjoint operator in the stationary weighted inner product, is positive definite; b!=e; and

    b*c != e*(a+e-d).                                                  (3)

Then the *minimal* constant-coefficient recurrence order of the tail f_n (n>=L) is exactly 2k.

Proof. Reversibility makes each killed M_r self-adjoint in the corresponding strictly positive weighted inner product. Positive definiteness of P implies its principal killed matrices have strictly positive eigenvalues. Each partial r<k has spectral radius <1 because the positive P has leakage to excluded sources. Each 2x2 partial M_r has two distinct eigenvalues since rbc>0. Its scalar survival is the positive spectral quadratic form of the ones vector. The projections onto both eigenspaces are nonzero: M_r*ones=[1-(k-r)b,1-(k-r)e], which is nonproportional to ones when b!=e and r<k.

Set q_r(x)=(x-a)(x-d-(r-1)e)-rbc. For distinct r,s,

    q_r(x)-q_s(x)=-(r-s)[e(x-a)+bc].

Any shared root would be x=a-bc/e. Substitution yields a shared root iff bc=e(a+e-d), excluded by (3). Moreover q_r(a)=-rbc !=0, and no proper killed block has eigenvalue 1. The spectrum therefore has exactly 1+2(k-1)+1=2k distinct positive eigenvalues, all with strictly positive scalar coefficients. Its 2k Hankel matrix factors as a Vandermonde matrix, a nonzero diagonal of coefficients times powers of the positive eigenvalues, and a second Vandermonde matrix. Its determinant is nonzero, forcing minimal order at least 2k. Theorem A gives the matching upper bound. QED.

For every k>=2, the explicit rational family

    a=3/4, b=1/(4k), c=1/8, e=1/(8k), d=3/4+1/(8k)

is positive stochastic and reversible. Its eigenvalues are 1, a-c=5/8, and d-e=3/4 with multiplicity k-1, so it is positive definite. Also b!=e, while bc/e=1/4 and a+e-d=0. Thus the bound 2k is sharp for every k>=2. For k=1, the neutral-survival and constant-full-source modes are distinct and give degree 2. The nonzero Hankel determinant at these rational witnesses shows degree 2k on a nonempty relatively Zariski-open, Euclidean-dense subset of strictly positive permutation-exchangeable stochastic kernels, initialized at their reversible stationary distribution.

When b=e, P is a stationary reset kernel: the reduced survival for each r becomes a single spectral mode. The strictly positive reset case has degree k+1, agreeing with R225. The nonreset family therefore supplies intermediate exact complexity 2k between R223/R225 exchangeable reset and R224 generic Markov kernels.

## Theorem C: source-block symmetry and a dimension formula

Partition k nonneutral labels into B nonempty source types of sizes k_1,...,k_B. Assume P and its initial distribution are invariant under independent permutations inside each type (group G=product_j S_(k_j)). For an allowed source subset U, write r_j=|U intersect type_j|, and s(r)=number of j with r_j>0. Every subset with the same count vector r yields the same survival, with multiplicity prod_j binom(k_j,r_j). The relevant killed transition is restricted exactly to the fixed subspace whose coordinates are neutral plus one for each included type, of dimension 1+s(r). The full-set contribution is constant 1, replacing dimension 1+B by dimension 1.

Therefore the scalar source-support expectation has a rational realization of dimension at most

    D(k_1,...,k_B)
      = product_j(k_j+1)
        + sum_j k_j*product_(h!=j)(k_h+1) - B.                  (4)

Proof. For each r the subset stabilizer preserves the killed operator and initial/final vectors; the scalar survival lies entirely in the fixed subspace. Group by the source-count orbit. Sum 1+s(r) over all r and subtract B for the full set. The first sum counts the orbit vectors; the second counts the configurations in which each group appears (k_j*product_(h!=j)(k_h+1)). This yields (4).

For k=6, symmetry partitions yield the certified *upper bounds*: (6) -> 12; (3,3) -> 38; (1,1,1,1,1,1) -> 250. Sharpness for intermediate partitions, such as (3,3), remains a further problem.

## Six-source exact witness, independent computations

Take (m,k,L)=(12,6,2) and

    a=d=7/10, b=1/20, c=1/10, e=1/25,
    pi0=1/4, pi_i=1/8.

The full reversible P has eigenvalues 1, 3/5, 33/50 (the latter of multiplicity five), all positive. Here bc=1/200 and e(a+e-d)=1/625, so the 12 modes are distinct. The R215 weights are

    W=[144,576,1440,4320,17280,86400,518400].

For H_ij=f_(2+i+j), 0<=i,j<12, exact computation gives rank(H)=12, det(H) mod 1000000007=146616006 and det(H) mod 1000000009=156237222. A separate propagation tracking (seen-source mask,current source) agrees for n=1..8 with the 12-mode reduced transition, and the characteristic recurrence is checked for 13 consecutive shifts.

An independent block-symmetric positive rational 7x7 model with source-group sizes (3,3) has an exact 38-dimensional orbit realization. Six exact terms agree with independent 256-state propagation. The companion standard-library Python program and JSON evidence provide explicit parameters, computation and reproducible checks. All arithmetic is integer or Fraction, with modular inverses on invertible denominators.

The finite checks support the concrete witness and guard implementation errors; the general formulas and sharpness follow from Theorems A–C. Independent review: NOT_REVIEWED. No Task CLAIM, Result, Review or Foundation admission is claimed.

## Next unresolved problems

1. Prove or refute generic sharpness of the block-orbit bound D for (3,3), including an explicit full-rank Hankel certificate.
2. Compare exact arithmetic and bit growth for the 12-, 38-, 64-, 250- and 256-state calculations, including input projection and output recovery.
3. Add this scalar ideal readout as a read-only observer over native typed BRC EffectHistogram; test ports, signs, exact rational mass, provenance, multiplicities and cross-moments before any native state quotient.
