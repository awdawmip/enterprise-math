# S23/AV finite-future observer: first failure at h=71 and exact N(71)=439

Date: 2026-11-07. Status: AUTHOR_SIDE_EXACT_FINITE_PROOF; independent review pending.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: Draft PR #1777@89680f793a00d62459f71d75315e4489ed4a702d, FINITE_HORIZON.md.

## Experiment and definition

For the fixed lawful S23/AV hypotheses theta0=(1/2,1/2), theta1=(5/7,7/8), the single-observation laws on labels (1,3,4) are P0=(1/2,1/4,1/4) and P1=(5/7,1/4,1/28). Both compress to the same Bernoulli observation z=1/4. An ordered prefix with k copies of label 1 and ell copies of label 4 has likelihood ratio

    Lambda(k,ell)=7^ell (7/10)^k=7^(k+ell)/10^k.

For allowed future suffix length <=h, possible suffix likelihoods are 7^j (7/10)^i, with i,j nonnegative and i+j<=h. Their reciprocal sign thresholds form

    T_h={10^i/7^(i+j): i,j>=0, i+j<=h}.

All M=binom(h+2,2) thresholds are distinct by prime factorization. A nontrivial prefix likelihood cannot equal a threshold: equality in the concatenated word forces k=ell=i=j=0. The unique equality class is Lambda=1 (all 3s).

The exact minimal deterministic future-sign observer identifies prefix states by threshold-sign vectors. Consequently S(n,h) equals the number of open intervals among the M+1 threshold intervals that contain a feasible prefix ratio, plus the singleton equality class. Define N(h) as the first n at which all M+1 open intervals are occupied; padding by label 3 makes the saturation permanent.

## New theorem

The previous conjecture

    N(h) = floor(h log 7 / log(10/7)) + 1

is true for every integer 1<=h<=70, but is FALSE at its first counterexample h=71. Exactly,

    floor(71 log 7 / log(10/7))+1 = 388,
    N(71) = 439,
    S(438,71) = 2629,  S(439,71) = 2630.

This establishes a 51-step correction to the proposed horizon-71 saturation length. The result is a finite exact theorem for the fixed auxiliary sign-observer problem; it does not assert the mother-model minimax error.

## Proof of sharp lower bound N(71)>=439

There are binom(73,2)=2628 distinct thresholds at h=71. Exact rational ordering shows the threshold immediately below 1 is

    L=10^60/7^71<1

(index 2195 in the sorted list; 1 is index 2196). Any saturated observer must occupy the interval (L,1).

Fix ell. Let k_min(ell) be the smallest nonnegative integer k for which 7^(ell+k)<10^k, i.e. Lambda(k,ell)<1. Since Lambda strictly decreases as k increases, k_min maximizes the below-one likelihood for this ell. k_min is nondecreasing in ell.

The attached exact-integer verifier performs 69 first-below-one searches, confirms k_min(68)=371 (so ell+k_min(ell)>=439 for ell>=68), and confirms for all ell=0,...,67 that

    7^(ell+k_min(ell))/10^k_min(ell) <= 10^60/7^71.

Hence no length-n prefix with n<=438 has likelihood in (L,1). Thus N(71)>=439. At n=439, the prefix (k,ell)=(371,68) satisfies the exact two inequalities

    10^60/7^71 < 7^439/10^371 < 1.

This fills the missing interval for the first time. Both inequalities are proved by arbitrary-precision integer comparison, not logs.

## Proof of sharp upper bound and first failure

VERIFY.py enumerates all 2628 distinct Fraction thresholds and every feasible nontrivial (k,ell) pair in the finite triangles k+ell<=388, <=438, and <=439. It locates the exact open interval for each ratio by sorting and rational binary search. At n=388 and n=438 exactly 2628/2629 open intervals are occupied, with only index 2196, the interval (L,1), absent. At n=439 all 2629 are occupied; the all-3 prefix supplies the equality class. Hence N(71)<=439, completing N(71)=439.

VERIFY_FIRST_70.py determines for every integer h in 1..70 the integer n_h as the least n with 7^(n+h)<10^n. This equals the previously conjectured formula because equality is excluded by prime factorization. Each h is exhaustively verified using all binom(h+2,2) exact Fraction thresholds and all nontrivial prefix count pairs k+ell<=n_h. In every case all M+1 open intervals are occupied; the leftmost interval requires n>=n_h because the smallest prefix ratio is (7/10)^n and the smallest threshold is 7^-h. Hence N(h)=n_h for all h<=70.

Both verifiers were actually executed using the Python standard library only. RUN_EVIDENCE.txt and RUN_FIRST_70.txt preserve their stdout. The proof uses complete finite enumeration of explicitly bounded integer triangles and exact rational inequalities; no numerical tolerances, simulation, or extrapolation are involved.

## BRC scope and follow-up

BRC reuse: REUSE_APPLIED to the exact joint-count/rational-likelihood observer, with concatenation as the future operation. The quotient retains the full joint-count source until the finite horizon is declared; collapsing to a sign-only or Boolean observer loses relevant future information. Here an *interior* threshold gap, not the extreme left tail, controls finite-horizon saturation. This statistical auxiliary experiment does not by itself assert a Heartbeat-X6 dynamic or six-source ten-label mother-model theorem.

Next: classify interior threshold gaps and obtain exact/bounded N(h) beyond 71; test continued-fraction families for infinite counterexamples with integer certificates. The full-lawful n=4 minimax delta4 question and the lawful mother-model mapping remain separate open units.
