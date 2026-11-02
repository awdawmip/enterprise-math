# D25: falsify the scalar-only 216/2304 CM inverse-power transfer at its actual weighted observer

2026-11-03, TASK_RESEARCH author-side. Research lane chatgpt-research-onhour-enterprise-math-20260923, separate from maintenance and hourly20. Frozen task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, science pin c47e13e4aba0e006366f989d6334d443f6333ae3. Algebraic deduction in a specified candidate class + original integer counterexamples; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

## Candidate to be tested, not assumed

Retain both original and different-source weighted sums

    W_p = sum_{k=0}^{p-1} (6k+1) binom(2k,k)^2 binom(3k,k)/216^k,
    S_p = sum_{k=0}^{p-1} (8k+1) binom(4k,2k)binom(2k,k)^2/2304^k,

computed in Z/p^3 with all denominators units, p>3. The prior 216/2304 geometric CM twist gave u^2=3sqrt(2), u^4=18 and differential gauge u^(-1). The immediately preceding onhour unit proved the exact arithmetic-power unit A_p=u^(p^2-1)=18^((p^2-1)/4), epsilon_p=(-18/p), and A_p^(-1)=epsilon_p(1-p q_p(18)/4) mod p^2.

A tempting **new candidate only**, NOT a previously published or source-proved transport, is the scalar equality

    H_scalar(p): W_p ?= A_p^(-1) S_p (mod p^3).

We test H_scalar against the original weighted coefficients, not elliptic-curve j-invariants. Its success is not implied by the underlying curve isomorphism, because a period gauge and a finite weighted truncated observation are different operators.

## All-prime first-digit obstruction in one entire target class

Consume the previously accepted D24 first-digit statement W_p=p (mod p^2) in both frozen target classes, and the published Guo-Zudilin 2304 full weighted sum result S_p=p (mod p^3) in those classes, with the original normalization retained. For every prime p=13 (mod24), the exact new gauge theorem gives A_p^(-1)=-1 (mod p). Therefore

    W_p - A_p^(-1)S_p = 2p (mod p^2), for ALL p=13 (mod24).

Since p>2, 2p is not 0 modulo p^2. Thus H_scalar is rigorously false throughout the 13 class already at the FIRST p-adic digit. In the 19 class epsilon=+1; this argument shows first-digit compatibility but leaves the second digit undecided, requiring exact original sums to test. This is an obstruction to this PARTICULAR scalar-only candidate, not to CM/WZ transfer with an additional basis/sign/cutoff correction.

## Exact second-digit counterexample in the 19 class

Independently calculate both integer-binomial weighted sums modulo p^3, then the inverse power gauge modulo p^2. Direct original arithmetic gives:

| p | W_p mod p^3 | S_p mod p^3 | A^-1 mod p^2 | defect W_p-A^-1 S_p mod p^3 |
|---:|---:|---:|---:|---:|
| 13 | 13 | 13 | 103 | 871 |
| 19 | 19 | 19 | 267 | 1805 |
| 37 | 37 | 37 | 1368 | 74 |
| 43 | 43 | 43 | 1076 | 33282 |
| 109 | 109 | 109 | 4359 | 820007 |
| 373 | 373 | 373 | 5594 | 49808928 |

At p=19, 1805 = 5*19^2 is NONZERO modulo 19^3=6859, although H_scalar does agree through modulus 19^2. Thus the p=19 counterexample distinguishes the *required second carry* from the first-class sign mismatch. At p=13 the residue is 871=2*13-8*13^2 (mod 13^3). At p=373 it is 49808928=2*373-15*373^2 (mod 373^3). Each numeral is from full original weighted sum calculations, not a replacement theoretical 216/2304 object.

For these exact six tested prime instances, since W_p=S_p=p (mod p^3), the defect also agrees with the conditional precision expression

    p(1-epsilon_p) + epsilon_p*p^2*q_p(18)/4 (mod p^3).

The latter expression would apply to an arbitrary target prime **if** the still-open all-prime W216 target were established, in addition to the published S2304 theorem. We do not use it as a proof of W216. For p=19 the required additive correction to this specific raw scalar model is at least 19^2*5, not an ignorable term of order p^3.

## Interpretation and next exact construction

We have now tested the p-adically corrected arithmetic-power gauge against the actual original weighted-sum observer. The scalar-only model fails universally in the 13 class at order p and fails at p19 at order p^2. Any candidate source-backed CM transport must include an original-basis orientation/sign conversion in the 13 class and a genuine second-digit cutoff/derivative correction in the 19 class; a bare curve isomorphism plus arithmetic-power unit is insufficient for H_scalar. The precise claimed necessity is scoped to raw H_scalar and the stated original observers.

BRC preservation: two separately sourced weighted coefficient populations, original index/cutoff/denominator units, p-valuations, original signs, the arithmetic-power versus semilinear operator label, and the future mod p^3 comparison are all retained. The scalar model is falsified rather than silently replacing the original by a period or Frobenius norm.

Mother Delta_p-R_p=0 (mod p), p=13,19 (mod24), equivalent original W216=p (mod p^3), remains OPEN. Next: use existing original-216 half-tail / Gauss-Clausen signed ports to build a **non-scalar** basis-preserving CM/WZ transfer; define an explicit signed additive port and prove/test its recurrence on p13,19,373. The original p373 native H0/B0 divided-power experiment #1559 ([X]U mod139129, module rank, semilinear Frobenius eta, odd signed Green/Hesse/kappa, independent replay) remains NOT_EXECUTED / PENDING_OWNER. This is an ordinary integer-binomial falsification, not that native experiment.

Preceding same-lane author commit 68d88b41595c20c35f766009e176fa791f70b356 carries the all-order power gauge; older CM geometry 8ddead488745b4b0d1a73717aed869ac76613d9f. No Source session/claim/run/Result/admission. Sites currently read only; exact continuation returned CONTROL_QUOTA; old dispatch research-onhour-20261031-0205-dispatch-r15 remains FAILED UPSTREAM_CODE_REVIEW_REQUIRED at awdawmip/kimi-query-bridge#6633. No duplicate operation, borrowed maintenance identity, staging merge or scheduler changes.
