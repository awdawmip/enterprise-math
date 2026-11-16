# R221 — Exact Markov-source support spectrum and loss of iid complete monotonicity

Date: 2026-11-17 (Asia/Shanghai).
Research classification: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Native EffectHistogram integration: NOT_EXECUTED.

## Scientific origin and declared observer

Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Exact antecedents: R209@27656bb342b9035c6e991f29e013ef9399ff7154, R215@71e9d86c4fea71a0ff1b2da66fe2b5656998a68b, R219@eb35761dc71fa06f96361e6bbc9e6592b3bbc7a3, R220@a51ddb6ed7e91842c567855bf3fbee118a6816c8.

P000 retains six native spatial axes, twelve signed primitive directions, separately typed time, native provenance and the richer typed BRC effect carrier. This proposition concerns only the **abstract paired-event observer monoid** and a *source-label* stochastic experiment. It does not derive physical Heartbeat dynamics, perform a native EffectHistogram operation, erase joint provenance, or identify signed amplitudes with positive masses.

Fix m>=1, k>=0, L>=1. Events come from [m] times ({0} union [k]), with neutral source label 0. J_(m,k,L) stores the final-occurrence order of selected labels and the last min(L,n) paired events. For r=0,...,k define (Stirling2 = second-kind Stirling number)

  W_r = r! m^L sum_{j=0}^{min(r,L)} Stirling2(L+1,j+1),
  T_r = sum_{j=r}^k binom(k-r,j-r) W_j.

By R215/R220, for any history of n>=L events, its full-tail principal two-sided ideal cardinality is F_n=T_|S_n|, with S_n the set of selected nonneutral source labels already seen. Further, the Boolean zeta identity is

  T_|S| = sum_{U subseteq [k], S subseteq U} W_|U|.

We retain that observer/future-query scope exactly.

Now let X_1,X_2,... be a time-homogeneous Markov chain on {0,...,k}, with initial probability row pi and row-stochastic matrix P (nonnegative rational entries in the exact-computation case). Conditional direction choices may be arbitrary provided they do not modify this source-label marginal Markov law; this particular F_n depends only on the source-label history. For U subseteq [k], set D_U={0} union U, pi_U = pi restricted to D_U, P_U = P[D_U,D_U], and 1_U the corresponding all-ones column. Write

  a_U(0)=1,
  a_U(n)=pi_U (P_U)^(n-1) 1_U  (n>=1).

These are exact rational matrix operations.

## Theorem A — support distribution and all ideal moments

For n>=1 and every U subseteq [k],

  Pr(S_n subseteq U) = a_U(n),
  Pr(S_n = U) = sum_{V subseteq U} (-1)^(|U|-|V|) a_V(n).       (A1)

For n>=L and every positive integer p,

  E[F_n] = sum_{U subseteq [k]} W_|U| a_U(n),                (A2)

  E[F_n^p] = sum_{U_1,...,U_p subseteq [k]}
       (prod_{j=1}^p W_|U_j|) a_(intersection_j U_j)(n).     (A3)

The exact distribution of F_n is obtained by summing the second expression of (A1) over supports with equal numeric value T_|U| (collisions are aggregated).

**Proof.** S_n subseteq U if and only if all n source-label states stay in D_U. The restricted first-step row and n-1 internal transitions yield a_U(n). Möbius inversion on the Boolean subset lattice gives the exact-support expression. The zeta identity expresses F_n as a positive sum of indicators 1[S_n subseteq U]; expectation gives (A2). Expanding the p-th power, the conjunction of p subset conditions is exactly S_n subseteq intersection_j U_j, yielding (A3). No independence between those indicators is assumed. QED.

If every row of P equals pi=p, then a_U(n)=(p_0+sum_{i in U}p_i)^n; hence this theorem strictly recovers the R220 iid spectral and arbitrary-moment formulas.

## Theorem B — rational generating function and recurrence

For the full-tail sequence (n>=L), the formal generating function is

  sum_{n>=L} E[F_n] z^(n-L)
     = sum_{U subseteq [k]} W_|U| pi_U P_U^(L-1)
                (I-z P_U)^(-1) 1_U.                          (B1)

It is rational. E[F_n] satisfies some constant-coefficient recurrence over the rationals of degree at most

  D = sum_{U subseteq [k]} (|U|+1)
    = (k+2) 2^(k-1), k>=1;  D=1 for k=0.                  (B2)

Thus for six selected sources the general upper bound is 256, versus the iid uniform minimal recurrence order 7 from R220. This is an upper bound, not an assertion of generically minimal order; its coefficients and minimal degree depend on the exact source transition matrix.

Moreover F_(n+1)<=F_n pathwise for every n>=L, hence E[F_(n+1)]<=E[F_n], even for non-Markov dependence. If every selected source label is eventually visited with probability 1, then E[F_n] tends to W_k.

**Proof.** Summing the geometric series for P_U gives (B1), valid formally even when I-P_U is singular at z=1. Place all P_U along the diagonal of a D-dimensional matrix B, and stack the corresponding initial/output vectors. The expected sequence is a scalar bilinear form in B^(n-1); Cayley–Hamilton supplies a recurrence of degree at most D. Each support set can only grow with n, and the positive zeta identity proves that T_|S| can only decrease on enlarging S. Thus F_n is nonincreasing after the tail is full. When all labels have appeared, its value is W_k; almost-sure eventual appearance and bounded convergence give the stated limit. QED.

## Theorem C — explicit homogeneous Markov failure of complete monotonicity

R220 proved (-1)^j Delta^j E[F_n]>=0 for iid labels. It is **false** for a general time-homogeneous source Markov chain, even when each selected source is eventually observed almost surely.

Take m=1, k=2, L=1. Exactly,

  (W_0,W_1,W_2)=(1,2,4), (T_0,T_1,T_2)=(9,6,4).

Set X_1=0 almost surely and take the transition matrix, in source order 0,1,2,

    [ 0    1    0  ]
P = [ 1/2  0   1/2 ]
    [ 0    0    1  ].

Event 2 sees source 1. At events 3,5,7,... the chain has another independent probability 1/2 to jump from source 1 to the absorbing source 2; otherwise it alternates through neutral label 0. In particular,

  E_1=9, E_2=6, E_3=5, E_4=5, E_5=9/2, E_6=9/2,...

For every integer r>=1,

  E_(2r+1) = E_(2r+2) = 4 + 2^(1-r),
  Delta^2 E_(2r+1)
    = E_(2r+3) - 2 E_(2r+2) + E_(2r+1)
    = -2^(-r) < 0.                                         (C1)

Source 2 is visited with probability 1 in the geometric limit, hence the limiting ideal-cardinality expectation is still W_2=4. Failure of complete monotonicity occurs infinitely many times *after* the full tail has filled; it is not a startup anomaly or floating-point artifact. QED.

**Consequence.** The iid positive-exponential mixture is a stronger conditional theorem. The correct arbitrary-Markov replacement is the finite restricted-matrix spectral realization (A2/B1), preserving pathwise monotonicity and rational recurrences while allowing alternating finite differences with either sign. These negative finite differences are diagnostic signs of a scalar expectation sequence, not signed physical BRC branch cancellation or negative mass.

## Exact execution and verification

The executable standard-library reference program R221_markov_source_support_check.py uses Fraction and exact integer/Stirling arithmetic, enumerating independent source paths to verify the restricted-matrix and Boolean formulas. Actual execution PASS on:

- 108 (m,k,L,n) finite model/horizon cases with k=0..3, m in {1,2,12}, L in {1,2,3};
- 7,134 enumerated Markov source histories and 405 exact-support probability checks;
- 90 iid reduction equalities, with the transition rows set exactly equal to the initial marginal;
- six successive odd-index negative second differences in (C1);
- exact X6-compatible W/T vectors for (m,k,L)=(12,6,2).

Companion JSON records exact results and test coverage. General theorems A–C are supported by the written proofs, while executed checks substantiate only their declared finite cases. No physical BRC runtime or EffectHistogram adapter was executed. Independent review: NOT_REVIEWED; formal Task CLAIM: NONE; formal Result/Review/Foundation admission: NONE.

## Unfinished questions and continuation

1. Characterize exact Markov kernels for which this particular ideal-cardinality readout retains complete monotonicity without imposing iid as an unproved default.
2. Minimize the block realization's *observable and reachable* dimension over Q; compute sharper minimal recurrences and account for bit/precision cost.
3. Build and run the typed native EffectHistogram adapter preserving the 21-bit complete action and separate future-query quotient, exact source associations, ports, phase/sign, multiplicity, positive rational mass and cross-moments. No shortcut from a scalar ideal-size observer to complete BRC state is claimed.
