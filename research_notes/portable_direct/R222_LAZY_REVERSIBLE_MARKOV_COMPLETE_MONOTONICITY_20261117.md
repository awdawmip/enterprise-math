# R222 — Stationary positive-spectrum reversible Markov sources preserve complete monotonicity

Date: 2026-11-17 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Scientific pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Depends on R215@71e9d86c4fea71a0ff1b2da66fe2b5656998a68b, R220@a51ddb6ed7e91842c567855bf3fbee118a6816c8 and R221@72732a341aca3c5931df4a72b3c95ce557717111.

## Theorem and declared scope

Fix integers m>=1, k>=0, L>=1. Let J_(m,k,L) be the previously defined paired-event observer monoid. Its full-tail principal ideal-cardinality readout after n>=L events is F_n=T_|S_n|; its positive Stirling-fibre coefficients are

  W_r = r! m^L sum_{j=0}^{min(r,L)} Stirling2(L+1,j+1)>0.

Assume the *source labels alone* form a time-homogeneous Markov chain on {0,...,k}. Let P be its row-stochastic transition matrix and pi_i>0 a stationary probability distribution. Assume detailed balance pi_i P_ij=pi_j P_ji (reversibility) and that P has **nonnegative real spectrum**. Let the first source label be distributed according to pi. The direction component can be sampled conditionally without changing the source-label transition law.

Then the full-tail expectation sequence is completely monotone:

  (-1)^j Delta^j E[F_n] >= 0
  for all integers n>=L and j>=0.                        (R222.1)

In fact it has an explicitly constructed finite **positive spectral measure supported on [0,1]**. Therefore E[F_n] is a positive mixture of powers lambda^(n-1) on that restricted time domain. The claim is exact for finite k, m, L; no iid assumption is required.

### Proof

For each U subseteq [k], put D_U={0} union U, P_U=P[D_U,D_U], and let pi_U be the restricted stationary row. R221 proves

  E[F_n] = sum_U W_|U| a_U(n),
  a_U(n)=pi_U P_U^(n-1) 1, n>=L.

Let D=diag(sqrt(pi_i)) and H=D P D^(-1). Reversibility makes H symmetric; the spectrum hypothesis makes H positive semidefinite. As a symmetric transform of a stochastic matrix, all eigenvalues of H are at most 1, hence 0 <= H <= I in the Loewner order. Every principal submatrix H_U=H[D_U,D_U] therefore satisfies 0<=H_U<=I. With v_U=(sqrt(pi_i))_(i in D_U), direct multiplication yields

  a_U(n)=v_U^T H_U^(n-1) v_U.

The powers of H_U commute with (I-H_U). For any j>=0,

  (-1)^j Delta^j a_U(n)
    = v_U^T H_U^(n-1) (I-H_U)^j v_U >= 0,

because the symmetric matrix in the quadratic form has nonnegative eigenvalues lambda^(n-1)(1-lambda)^j for lambda in [0,1]. Multiplying by W_|U|>0 and summing proves (R222.1). Taking spectral decompositions of all H_U yields a finite positive measure on [0,1], with atom masses W_|U| times squared projection lengths. QED.

### Useful sufficient condition

Any reversible stochastic K with positive stationary pi gives a nonnegative-spectrum P by lazification:

  P = (I+K)/2.

Indeed a reversible stochastic K has real eigenvalues in [-1,1], so the eigenvalues of P lie in [0,1]. The same pi is stationary and reversible for P. Hence **stationary lazy reversible correlations** inherit the stronger iid-style complete monotonicity even though the source process need not be iid.

### Exact non-iid witness

Take m=1,k=2,L=1, pi=(1/3,1/3,1/3), and

  P = [[1/2,1/4,1/4],
       [1/4,1/2,1/4],
       [1/4,1/4,1/2]].

The source chain is correlated (diagonal persistence probability 1/2 differs from stationary 1/3). It is symmetric, stationary, strictly positive and has spectrum {1,1/4,1/4}. The restricted matrices' spectral modes yield, for every n>=1,

  E[F_n] = 4 + (1/3)(1/2)^(n-1) + (8/3)(3/4)^(n-1).

Thus E_1=7, E_2=37/6, E_3=67/12, E_4=31/6, E_5=467/96, and every alternating forward difference is nonnegative. This gives a concrete non-iid generalization of R220 and a precise contrast with R221's periodic non-reversible counterexample, whose negative second differences occur infinitely often.

## Reproducible finite checks and boundaries

Companion standard-library Python script R222_lazy_reversible_complete_monotonicity_check.py imports the published R221 Markov-source evaluator and runs exact Fraction arithmetic. It returned PASS on **16 model families**, **2,952 exact alternating-difference checks** up to order 8, plus the explicit non-iid five-term sequence and its all-n closed form on 12 initial horizons. The script applies symmetric positive-semidefinite lazy reversible P in source alphabet sizes 1..4, and m=1 or 12 with L=1 or 2. It is a finite implementation check, not the universal theorem's proof; the self-adjoint spectral argument above supplies the general conclusion.

This is a source-support ideal-cardinality query only. It neither identifies the full 21-bit observer action with a 7-bit scalar quotient, nor reduces native X6 cell identity, tagged physical branch/port/phase, exact mass, multiplicity or joint cross-moments. Native EffectHistogram integration: NOT_EXECUTED. Independent mathematical review: NOT_REVIEWED. Task CLAIM/Result/Review/Foundation admission: NONE.

## Next questions

1. Characterize minimal assumptions weaker than stationary reversible positive spectrum under which the weighted source-support readout is completely monotone; determine whether some negative-spectrum kernels can still pass because their observable weights cancel.
2. Compute the exact minimal scalar recurrence by controllability/observability reduction of the R221 Markov block model (and its resource/bit complexity), rather than equating the general 256-dimensional bound with minimal dimension.
3. Carry the full provenance and signed X6/BRC carrier through native EffectHistogram serialization and composition tests, keeping R221/R222's source-label law explicitly separate from physical dynamics.
