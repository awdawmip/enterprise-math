# R228 — Sharp 250-mode scalar recurrence within a reversible, positive-spectrum seven-source chain

Date: 2026-11-17 (Asia/Shanghai). Evidence: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Native BRC EffectHistogram integration: NOT_EXECUTED.

## Source, scope, and provenance

Frozen task-science pin: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Previous immutable sources: R215 ideal cardinalities; R221 killed-source Markov identity; R222 reversible complete-monotonicity sufficient condition; R224 unrestricted-generic 250-mode certificate (branch @a3276716dc072ef653783c0d054fbecd2a399819); R225 stationary reset 64-mode witness (@de85fb7ea7a22924a4813c6a8a274432670645b2); R226 source-exchangeable 12-mode and R227 two-block exchangeable 38-mode results (@57d472f22dcaff1e611c12220fc545469387e7f5). R228 develops a **distinct**, nonsymmetric and nonreset **reversible** family and proves the unrestricted 250 upper bound is attained even when all observable spectral weights are nonnegative.

This is the exact scalar source-support principal-ideal-cardinality readout on the abstract paired-event observer `J_(m,k,L)`. It is a typed auxiliary mathematical model embedded in the six-axis Heartbeat World research program. It is not a native X6 physical law, a full 21-bit observer-state codec, or an information-safe reduction of signed BRC EffectHistogram, port, branch, positive-rational weight, multiplicity, provenance, joint relation, phase or cross-moment carriers. Preserve those carriers separately.

## Definitions

Let integers `m,k,L>=1`. Event directions have `m` choices and source labels `0,1,...,k` with `0` neutral. For the set `S_n` of nonneutral sources observed in the first `n` events, let the R215 Stirling-fibre weights be

    W_r = r! m^L sum_(j=0)^min(r,L) Stirling2(L+1,j+1)>0,
    T_|S| = sum_(U subseteq [k], S subseteq U) W_|U|.

For any filled tail `n>=L`, the scalar ideal size is `F_n=T_|S_n|`.

Fix positive source probabilities `pi_i>0`, `sum_i pi_i=1`, and independent state-specific holding parameters `0<alpha_i<1`, for `i=0,...,k`. Define the **sticky-reset chain**

    P_ij = alpha_i * delta_ij + (1-alpha_i) * pi_j.         (1)

At each step, the current source `i` either persists with probability `alpha_i`, or redraws from `pi` with probability `1-alpha_i`. Initialize at the stationary distribution

    rho_i = [pi_i/(1-alpha_i)] / Z,
    Z = sum_j pi_j/(1-alpha_j).                           (2)

For `U subseteq[k]`, write `D_U={0} union U`; `P_D` is the principal killed matrix indexed by `D_U`.

## Theorem 1 — Reversible positive-spectrum Hausdorff moments

For all `n>=L`,

    f_n=E[F_n]
       =sum_(U subseteq[k]) W_|U| rho_D P_D^(n-1) 1_D.     (3)

This sequence is a finite positive Hausdorff moment sequence. Equivalently, for every integer `n>=L` and `j>=0`,

    (-1)^j Delta^j f_n >=0.                              (4)

All finite Hankel matrices of the tail are positive semidefinite.

**Proof.** The expansion of `T_|S|` into `W_|U|` and the event `S_n subseteq U` gives (3). Detailed balance holds:

    rho_i P_ij = pi_i*pi_j/Z = rho_j P_ji     (i!=j).

Let `B=diag(sqrt(rho_i))` and `A_i=sqrt((1-alpha_i)pi_i)`. The reversible similarity transform `K=B P B^(-1)` has the exact form

    K = diag(alpha_0,...,alpha_k) + A A^T.                (5)

Every killed principal block `K_D=diag(alpha_i)_(i in D)+A_D A_D^T` is strictly positive definite. It is similar to the killed substochastic matrix `P_D`, so all its eigenvalues lie in `(0,1]`. Writing `v_D=(sqrt(rho_i))_(i in D)` gives

    rho_D P_D^(n-1) 1_D = v_D^T K_D^(n-1) v_D.

The spectral theorem expresses each summand as a positive combination of `lambda^(n-1)` with `0<lambda<=1`. Combining with `W_r>0` proves (4), via differences of the positive atoms, and the Hankel claim. QED.

## Theorem 2 — General dimension bound, including the unobservable full-block modes

For every such source chain, the least scalar constant-coefficient recurrence degree of the tail satisfies

    d_min <= D_k = 1+sum_(U proper subset of [k])(1+|U|)
                  = (k+2) 2^(k-1) - k.                  (6)

In particular, `D_6=250`.

**Proof.** Every proper `U` contributes a killed block of dimension `|U|+1`. For the full set `U=[k]`, `P_D=P` is stochastic and the probability of staying inside the full alphabet is exactly `1`; its entire scalar contribution is the constant `W_k`, requiring only one state rather than `k+1`. Taking the direct sum of the remaining exact rational killed realizations and this constant gives `D_k` states; the characteristic polynomial yields an annihilating recurrence of degree at most `D_k`. The sum of `|U|` over all `2^k` subsets is `k2^(k-1)`; subtracting the full-set `k+1` block gives (6). QED.

## Theorem 3 — Explicit reversible sharpness at six sources

Set `(m,k,L)=(12,6,2)`, `pi_i=(i+1)/28` and `alpha_i=(i+1)/20` for `i=0,...,6`. All entries of `P` are positive; the chain is reversible, nonexchangeable, nonreset, and has strictly positive real spectrum by Theorem 1. The stationary distribution is exactly

    rho=(55692,117572,186732,264537,352716,453492,569772)/2000513.

The established ideal weights are

    W=(144,576,1440,4320,17280,86400,518400).

For `H_250=(f_(2+i+j))_(0<=i,j<250)`, the exact modular calculations are

    prime 1000000007: rank=250, det(H_250) mod prime = 8827868;
    prime 1000000009: rank=250, det(H_250) mod prime = 569768765.

Every denominator used in the finite-field reconstruction is invertible modulo both primes. A zero rational determinant would reduce to zero at both primes, so `rank_Q(H_250)=250`. A recurrence of order below 250 would make this Hankel matrix rank deficient. Theorem 2 gives the matching upper bound. Therefore

    d_min = 250.                                         (7)

Independent exact cross-checks of the moment formula yield

    f_2 = 10703531240028/10002565,
    f_3 = 55145714582097/56014364,
    f_4 = 143749360496201427/156840219200.

The companion standalone Python standard-library checker computes all `f_2` through `f_500` in modular arithmetic, assembles the actual Hankel matrices and evaluates their determinants by finite-field Gaussian elimination. It also compares the killed-chain representation with an independent `(current source, seen-source mask)` dynamic program for 24 exact small configurations.

**Genericity corollary.** Within the connected parameter domain `pi_i>0`, `sum pi=1`, `0<alpha_i<1`, the 250x250 determinant is a rational function with nonvanishing denominators and is not identically zero by this witness. Its nonzero locus is relatively Zariski open and Euclidean dense. Thus for `k=6,m=12,L=2` the generic minimum order in the reversible sticky-reset family is also **250**. Theorem 1 holds simultaneously: maximal scalar recurrence complexity and complete monotonicity coexist.

## Meaning and verification

R224 established a 250-mode witness in general stochastic Markov kernels. R228 strengthens its scope to a **seven-source reversible, strictly positive-spectrum** subfamily and shows that complete monotonicity does not force the 7/12/38/64 low-mode patterns. The explicit method preserves positive probabilities, exact rationals and source identities. This is a new structural statement, not an optimization claim for native physical BRC or signed-event algebra.

Reproducibility: `R228_reversible_sticky_source_check.py` and `R228_verification.json`. Python Fraction and integer arithmetic, 24 independent finite configurations with 252 exact comparisons/difference checks; two complete 250x250 modular determinants. Program run returned `PASS`. Argument status: author proof plus reproducible exact finite witnesses; independent review `NOT_REVIEWED`.

## Remaining work

1. Characterize sharp lower-dimensional strata in sticky-reset kernels (shared eigenvalues, missing observable spectral projections and equal holding/reset parameters), including collision signatures.
2. Analyze exact-bit complexity of 7/12/38/64/250-mode recurrences against 256-state propagation: parameter conversion, intermediate numerators, input reconstruction, repeated-query amortization and error-free final output.
3. Add a read-only source-support ideal observer to actual typed BRC EffectHistogram while maintaining all native direction, signed port, provenance, branch, exact rational weight, multiplicity and cross-moment structures. Any state quotient requires a separate future-operation preservation certificate.

This note is an independent portable research artifact. Formal CLAIM/Result/Review/Foundation: NONE.