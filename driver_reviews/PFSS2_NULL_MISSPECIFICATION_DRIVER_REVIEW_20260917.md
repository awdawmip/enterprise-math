# Driver review — PFSS2 null-model misspecification

Driver-ID: EM-DVR-Q7M2
Date: 2026-09-17
Result: RR-9F084B92BE8261F3A8D7
Task: RS-PRIME-FACTOR-SEMIPRIME-SHELL-SECOND-ORDER-DENSITY-NULL

## Scope and binding

This review is independent of the researcher execution. It binds only the frozen result record and source artifacts for the publication shown above. It does not grant Working Truth, Foundation status, a prime theorem, or a residual survivor.

## Verification performed

I read the frozen taskbook, result record, terminal summary and full return. I independently replayed the standard-library exact support/covariance certificate in an isolated local Python environment.

The replay reproduced: (i) smallest eligible primes 37, 43, 59 at X=10^6, 3*10^6, 10^7; (ii) microcell width upper bounds 27, 69, 168, all <210; (iii) the X=10^6,p=37 interval [27028,27297]; (iv) the containing B band [26880,27300) with 41 primes and two allowed shifts giving counts 25 and 31; and therefore B mean 28 and exact population variance 9 while A variance is 0.

The taskbook explicitly permits terminal class NULL_MODEL_MISSPECIFICATION when the two null families have materially incompatible covariance/threshold structure and replay isolates the smallest cause. The frozen return satisfies that task-local branch. Because the prescribed z/C/T statistics are undefined under the frozen Null A on required discovery cells, the unopened 3e8 and 1e9 layers must remain unopened for this execution; opening them cannot repair a discovery statistic that was never validly frozen.

## Mathematical/statistical disposition

ACCEPTED at task scope as NULL_MODEL_MISSPECIFICATION.

Accepted claim: the frozen Null A degenerates on the first three discovery scales for the required observables, and the exact two-shift witness establishes a genuine A/B covariance mismatch. This is an exact finite-support/conditioning diagnosis, not Monte-Carlo evidence alone.

Not accepted: existence or absence of a higher-order semiprime residual; any prime-process law; any family-wise calibrated survivor; any inference from the unopened holdouts; any Working Truth or canonical promotion.

## Routing decision

Close this execution as a valid task-terminal misspecification return. Preserve the 3e8 and 1e9 holdouts. Do not repair the task post hoc with a variance floor, scale deletion, or surrogate substitution. Any continuation must first justify a nondegenerate stochastic/invariance mechanism independently of the exposed residual outcomes and must explicitly account for the finite-window identifiability obstruction in RR-4760E87D1D3AD2F6AFFA.

Method harvest: RESULT_ONLY. The checker is task-local verification; no new global tool capability is claimed.
