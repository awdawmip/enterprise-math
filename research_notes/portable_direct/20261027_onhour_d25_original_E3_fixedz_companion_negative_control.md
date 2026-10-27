# D25 original E3 invariant differential: p=373 fixed-z negative control (2026-10-27)

**Type:** TASK_RESEARCH / author-side exact finite original-model experiment / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NOT_NATIVE_H0_B0 / NOT_SOURCE_CHECKPOINT / NOT_A_RESULT. No winning claim, authorized OPEN, original H0/B0 run, independent mathematical review, or Source-native result is asserted.

**Identity:** chatgpt-research-onhour-enterprise-math-20260923 (Research lane only; never the maintenance lane).
**Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
**Publication:** TP2-B6F4FC938FF94941C1B7. Mother Objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
**Frozen scientific Source:** c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).

## Why this diagnostic is needed

The Source proof d25_alpha_p3_source_refinement_20260924.md has already computed the raw original curve coefficient H_{3,p-1}(t) to p^3. Its explicit remaining problem is the true normalized Gauss-Manin companion and original H0/B0 Frobenius; it warns that differentiating the raw coefficient at a fixed coordinate cannot simply be declared the native companion. This turn consumes that raw source result and executes an original-E3 first-digit implementation negative control, rather than repeating the earlier raw coefficient theorem or enlarging the 815-prime W scan.

Source: Chisholm, Deines, Long, Nebe and Swisher (2013), p-Adic Analogues of Ramanujan Type Formulas for 1/pi, Lemma 12 and Proposition 16, https://www.math.rwth-aachen.de/~Gabriele.Nebe/papers/Ramanujan.pdf . Proposition 16 supplies a supersingular p^2 product comparison; it is not a p^3 computation of the missing D25 LIFT digit.

## Exact original model and two independent computations

In R_r=(Z/p^r)[T]/(T^2-2), choose lambda=1/2, t=(2-T)/4 and c=t/27. The **actual E3 model**, rather than the external Hesse scalar surrogate, is

    E3(t): y^2+x*y+c*y=x^3,   z=-x/y,   w=-1/y.

Its formal relation is w(1-z)-c*w^2=z^3. Hence the original invariant differential, with constant-term-one branch, is

    omega = dx/(2y+x+c) = dz/sqrt((1-z)^2-4c*z^3).

Thus the z^(p-1) coefficient is the exact Lemma-12 polynomial

    a(p-1)=sum(j=0..(p-1)/3) binom(2j,j)*binom(p-1-j,2j)*(t/27)^j.

The raw fixed-formal-coordinate derivative is

    J_plain = partial_lambda|z a(p-1) = (T/4) partial_t a(p-1).

Its name and derivative direction are explicit: J_plain is NOT established as a normalized Gauss-Manin eigendifferential, a native Frobenius operator, or H0/B0.

The linked executable independently evaluates a and J_plain by (1) the exact ODE 2D H'(z)+D'(z)H(z)=0, D=(1-z)^2-4c*z^3, differentiated in t, and (2) the original Lemma-12 integer-binomial polynomial and its termwise derivative. Every inversion has a p-unit denominator, all values are integral modular pairs with T^2=2, and no floating-point or unrelated curve is used.

## Executed p=373 exact original-model witness

At p=373, p^2=139129, p^3=51895117:

    a(372)                     = 46042747 + 33130606*T  (mod 51895117)
    a(372)/373                 = 123439 + 88822*T        (mod 139129)
    J_plain                    = 50822957 + 27267792*T  (mod 51895117)

For a **specific falsifiable naive implementation only**, set b_plain=a+6*J_plain. Here 6 comes from splitting the weighted Clausen-square observer 1+6*lambda*partial_lambda into f*(f+12*lambda*f_prime), then substituting lambda=1/2; this does NOT make b_plain the geometric normalized companion.

    b_plain(372)                = 39609787 + 41052007*T  (mod 51895117)
    (a(372)/373) mod 373       = 349 + 48*T
    b_plain(372) mod 373       = 171
    (a(372)/373)*b_plain(372)  = 372+2*T = -1+2*T        (mod 373).

The Source supersingular Proposition-16 quartic-normalized Frobenius *eigen-companion* with determinant choice b2=p would instead require a*b/p=-1 (mod p). The displayed discrepancy 2*T is a nonzero unit; it is not numerical rounding.

**Scope:** This rules out directly substituting the naive fixed-z coefficient derivative with factor 6 for the Source-normalized eigen-companion *under that proposed identification* already at first-digit precision. It does not reject the true Gauss-Manin companion, change the Frobenius sign/twist, calculate native [X]U, or refute original LIFT/JT2. An implementation must establish the actual coordinate transport/normalizer, not silently declare the two derivatives identical.

For regression context, eight small primes p=13,19,37,43,61,67,211,373 all produced the same first-digit naive product -1+2*T, with ODE/polynomial cross-checks passing. This is FINITE evidence only; no all-prime statement is made. The proof of the generating-function identity is algebraic; the p=373 pair is an executed exact finite diagnostic.

**Reproducer:** research_notes/portable_direct/d25_original_E3_formal_differential_p373_20261027.py, initially persisted at GitHub commit 45389c9c23ada9ea65cb2e5702f756b5c69f3ff8 (blob 224f8742d7476a2c03d9356821b4b3d26b65b6f5), and read back from that immutable commit.

## BRC, continuation and unfinished native obligations

BRC=COMPOSE_APPLIED: the carrier retains original E3, fixed z direction, lambda/t relation, full T-branch, a/p, the *labelled naive derivative* and the signed first-digit product. A norm, total-only readout, untyped derivative substitution or taking a classical quadratic ring to be a native X6 plane would lose the exact source discrepancy. The existing accepted D24 UR/CM0, earlier raw coefficient p^3 theorem and the 815-prime W regression remain separate and are not recredited.

D25/LIFT/JT2 stays OPEN. The *actual original-class native* H0/B0 divided-power evaluator at p=373 is still missing an identified executing owner and verified reproducible raw data: [X]U mod 139129, module rank, Frobenius direction/twist and two-digit normalization, odd signed Hesse/Green observer, kappa and Delta-R. Existing support #1559 stays PENDING_OWNER / NOT_EXECUTED. This negative control is an acceptance test for avoiding a *wrong* implementation, not a substitute for that native run.

Next exact step: authorized owner supplies the fixed original H0/B0 representative plus authentic Gauss-Manin/coordinate/Frobenius map, executes the p=373 native object, demonstrates that the naive fixed-z substitution is excluded or explicitly repaired, retains the sign and source/observer labels, and sends a native checkpoint/Result through a legitimately claimed and opened Research run for independent review. The read-only Site has research_authority_granted=false, and fresh exact continuation returned CONTROL_QUOTA; the older original dispatch research-onhour-20261026-1355-dispatch-r11 ended FAILED/TimeoutExpired. No Source authority was invented, no old staging was merged, no blocked mutation replay, and no scheduling changes were made.
