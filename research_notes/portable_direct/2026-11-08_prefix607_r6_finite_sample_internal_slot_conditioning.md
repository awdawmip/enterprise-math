# PREFIX-607-R6 — Exact finite-sample risk and sharp conditioning of the native internal-slot BRC observer

Date: 2026-11-08 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Original native BRC source: research_notes/portable_direct/PREFIX565_positive_marginal_certificate.py, immutable Git blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41.
Dependencies: PREFIX-601/602 weighted twelve-incidence family; PREFIX-603 internal-slot recovery; PREFIX-605/606 binary-slot observer and exact total-variation theorems. This note extends their declared observer model without changing the frozen native graph.

## Exact scientific question and sampling scope

The native graph has 48 phases p, 12 incidence classes e(p), and three native slot actions. Each source phase p has slot probabilities

    Pr(slot=0 | p) = a_p = 1/(1+2 t_{e(p)}),
    Pr(slot=1 | p) = Pr(slot=2 | p) = t_{e(p)}/(1+2 t_{e(p)}),

for arbitrary *finite nonnegative* incidence weights t. At t_e=1 this is the original frozen native phase action law. The slot-0 successor sigma(p)=NEXT[p][0] is a permutation of the 48 phases (native one-step identity, independently checked against the frozen original source).

There are N >= 1 **independent one-step trials**: for each trial the initial phase is redrawn independently from a common unknown distribution pi on the 48 phases; then one weighted native slot action occurs. The retained observation is the Boolean tag 1{slot=0} together with the terminal phase. This is a repeated-experiment sampling regime, not one length-N trajectory. For each p let Z_p be the number of trials observing (slot=0, terminal phase=sigma(p)); set s_p=1+2 t_{e(p)} and

    pi_hat_p = s_p Z_p / N.

The map from source p to the tagged endpoint event is injective because sigma is a permutation.

## Theorem 1 — exact finite-N risk

For every N>=1, arbitrary initial probability law pi and every finite nonnegative t,

    E[pi_hat_p] = pi_p,
    Cov(pi_hat_p,pi_hat_q) = (1/N) [1{p=q} pi_p s_p - pi_p pi_q],

and

    E ||pi_hat-pi||_2^2
      = (1/N) [sum_p pi_p s_p - sum_p pi_p^2].                     (1)

Proof: the 48 distinguished tagged-endpoint events have probabilities q_p=pi_p/s_p. The remaining event is the disjoint union of all non-slot-0 observations. Their counts together are multinomial(N;(q_p)_p,1-sum q_p). In particular Cov(Z_p,Z_q)=N(1{p=q}q_p-q_p q_q), and scaling by s_p s_q/N^2 gives the displayed formula. Sum the diagonal entries to obtain (1). All identities are exact for every positive integer N; no normal approximation is used. The unprojected estimate is nonnegative and unbiased but need not sum to one on every sample; it is an estimator of the entire initial probability vector.

## Theorem 2 — exact worst-case quadratic risk for known t

For fixed finite t, define s=(s_p)_p. The sharp worst-case (over all initial phase probability laws) mean-squared error of this estimator equals

    R_max(N,t) = (1/N) max_{pi>=0, sum pi=1}
                         (sum_p s_p pi_p - sum_p pi_p^2).         (2)

The maximizer is unique and explicitly computable by a single water-filling threshold lambda:

    pi*_p = max{0,(s_p-lambda)/2},
    sum_p max{0,(s_p-lambda)/2}=1.                                (3)

The threshold is uniquely determined; sorting the 48 values s_p and scanning the active prefix computes it using rational arithmetic whenever the t_e are rational.

Proof: the objective is strictly concave on the compact simplex. The Lagrange multiplier/KKT stationarity conditions for positive coordinates give s_p-2pi_p=lambda; inactive coordinates require s_p<=lambda. Formula (3) satisfies all KKT conditions and therefore is the unique global maximizer. This yields a sharp, not merely asymptotic, worst-case risk.

In the original all-one model, s_p=3 for all 48 phases, so the maximizer is uniform, and

    R_max(N,all-one) = 143/(48 N).

For an initial point mass, the exact risk is 2/N. For the all-zero weighted extension, R_max=47/(48 N).

## Theorem 3 — confidence and a sharp rare-slot witness

Let s_max=max_p s_p=1+2 max_e t_e. By Hoeffding's inequality and a union bound, for any epsilon>0,

    Pr( ||pi_hat-pi||_infinity >= epsilon )
      <= 96 exp( -2 N epsilon^2 / s_max^2 ).                     (4)

Consequently N >= [s_max^2/(2 epsilon^2)] log(96/delta) is sufficient to make the right-hand side <=delta. This bound is a conservative nonasymptotic guarantee; the exact mean-squared error is (1).

Now choose any one of the six original critical incidence pairs (e,f), set t_e=x>0 and t_f=1/(4x), leaving other incidences finite nonnegative. The weighted untagged transition has a critical rank loss by PREFIX-601. Choose a source phase p with e(p)=f and the point-mass initial law pi=delta_p. Equation (1) yields

    E ||pi_hat-pi||_2^2 = (s_p-1)/N = 1/(2 x N).                 (5)

The probability of seeing no useful slot-0 event in N trials is exactly

    Pr(Z_p=0) = [1 - 1/s_p]^N.                                   (6)

As x tends to zero through positive values the coefficient 1/(2x) diverges, even though the exact algebraic reconstruction using the slot-0 bit remains injective on every finite-weight model. This quantifies a precise sampling cost of the simple exact inverse observer. It is a statement about this estimator, not a minimax lower bound for all estimators that use the entire tagged histogram.

At x=1/32 the paired weight is 8, s_p=17, and the exact risk is 16/N; the no-hit probability at N=16 is (16/17)^16.

## Executed exact evidence and reusable method

The standard-library certificate PREFIX607_R6_reproducible_certificate.py checks the original Git blob SHA1 and frozen pin, all nine original roots, the native 48-phase internal-slot permutation, twelve classes of four phases, the exact KKT threshold for all-one, all-zero and asymmetric rational weights, and a critical-pair example imported from the prior native PREFIX-605 certificate. For a four-phase supported rational pi and nonuniform rational weights, it exhausts all 25 ordered two-sample observation outcomes, verifies 48 coordinate means, 16 covariances and the exact total error. The result is

    ALL_CHECKS_PASS
    original model worst-case risk factor = 143/48
    asymmetric N=2 exact risk = 10/9
    critical x=1/32 point-mass risk factor = 16.

The companion PREFIX607_R6_RESULTS.json records the exact rational values and immutable dependencies. The proof of the all-N identities is the multinomial calculation and KKT argument above; finite enumeration independently checks their implementation.

BRC reuse resolution: REUSE_EXECUTED — frozen native PREFIX-565 graph; REUSE_APPLIED — PREFIX-601/602 weighted extension, PREFIX-603/605 observer identities, PREFIX-606 TV benchmark. Population, branch tag, terminal-phase observer, independent-trial sampling and exact future readout are kept explicit. The theorem is a model-internal author result, not a review or Foundation admission.

## Next discriminating research unit

Compare exact Fisher information and finite-sample error of efficient estimators that exploit BOTH outcomes of the binary tag and terminal phase, separately for tags slot=0,1,2. In particular, determine whether the slot-0 advantage in exact nullspace total variation (PREFIX-606) yields a uniform risk advantage under asymmetric critical weights, and identify the optimal sampling trade-off near the six critical surfaces. Keep a separate distinction between algebraic identifiability, total-variation contraction, and statistical reconstruction risk.
