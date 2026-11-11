# D25/LIFT — p² arithmetic Frobenius-port versus literal-power defect on the frozen Hesse parameter (2026-11-12)

**Classification:** TASK_RESEARCH author-side exact lemma and exact counter-witness to a false second-digit normalization substitution; five target-prime integer tests **EXECUTED**. **UNREVIEWED / NOT_ADMITTED / original native H0/B0 [X]U NOT_RUN.** This is an exact acceptance discriminator, not a replacement for the original native benchmark or an all-prime proof of LIFT.

## Fixed source, prior evidence and original obligation

Mother: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Scientific input remains frozen at `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`. Accepted D24 UR/JT0, the 19 predecessor native units and Green units are consumed, not recredited.

The exact canonical prior Source checkpoint `onhour-d25-20261112-0121-source-lambda-checkpoint-release-v1` succeeded, and its HANDOFF(CONTINUATION) was verified at `be9d843d23d5ac65d1869fae86689cd1b99a454c` (GitHub bridge issue `awdawmip/kimi-query-bridge#6801`); its old CLAIM was released. This author-side study creates no new CLAIM/open or role-bound semantic checkpoint.

Prior frozen source Hesse parameter: `lambda^3=t=4+2T`, `T²=2`, `u=lambda^-3=(2-T)/4`. The already completed source-sign and full Gauss–Manin interface is at `research_returns/D25_HESSE_LAMBDA_E3_SIGNED_CONNECTION_20261112_ONHOUR.md`, commit `90f199a9aa81fd07c6192f838845b95e2bf78e3b`, blob `27ce350841e7c3bb212a8ebd234b5b780b53055a`. That result proves the signed observer coefficient formula used below. Original native same-class H0/B0 divided-power `[X]U mod139129`, rank, semilinear Frob, eta, kappa and Delta-R remain `NOT_RUN / PENDING_OWNER` at existing issue `enterprise-math#1559`.

## Theorem 1 — two distinct p² parameter operations

Let `p ≡ 13 or 19 (mod 24)` be prime, `R_2=(Z/p² Z)[T]/(T²-2)`, and `sigma(a+bT)=a-bT`. Let `lambda in R_2` be **a specified unit root** of `lambda³=t=4+2T`. We do not claim a particular native evaluator or all-prime root choice has been supplied.

Since `(2/p)=-1`, residue-field p-th power agrees with `sigma` modulo p. Thus the following integral second digits are defined in `R_1=(F_p)[T]/(T²-2)`:

```
Q_t       = (t^p      - sigma(t))     / p     (mod p),
D_lambda  = (lambda^p - sigma(lambda))/ p     (mod p).
```

The exact difference-of-cubes factorization gives

```
(lambda^p)^3 - (sigma(lambda))^3
  = (lambda^p - sigma(lambda))
    * ((lambda^p)^2 + lambda^p*sigma(lambda) + (sigma(lambda))^2).
```

Because the second factor reduces modulo p to the unit `3(sigma lambda)^2`, division by p yields

```
3*(sigma lambda)^2*D_lambda = Q_t            (mod p),
D_lambda = Q_t/[3*(sigma lambda)^2]          (mod p).    (1)
```

Consequently the formal substitution `T -> -T`, `lambda -> lambda^p` **does not respect** `lambda³=4+2T` modulo p² whenever `Q_t !=0`: its relation defect is precisely `t^p - sigma(t)=p Q_t`. The compatible algebraic conjugation sends `lambda -> sigma(lambda)`. Literal p-th powering is not automatically an additive coefficient-ring Frobenius lift, and neither substitution is asserted to be the authenticated native H0/B0 operator.

This is a rigorous, appropriately scoped **precision/semilinearity discriminator**, not a claim of native crystal rank or Frobenius normalization.

## Theorem 2 — defect at the exact original signed Hesse observer

The previously completed source-coordinate bridge gives the original `Omega_H=omega_H+6 nabla_lambda omega_H` in its Hesse de Rham basis as the rational coordinate-function vector

```
O(lambda) = [ 2 - 9*lambda²/(lambda³-1),
              -1/(lambda³-1) ]^T.
```

All its denominators are units on the selected CM parameter because `Norm(t-1)=Norm(3+2T)=1`. Differentiating **the coordinate functions** gives

```
O'(lambda) = [ 9*lambda*(lambda³+2)/(lambda³-1)²,
                3*lambda²/(lambda³-1)² ]^T.
```

The exact Taylor identity `lambda^p=sigma(lambda)+p D_lambda (mod p²)` yields

```
O(lambda^p) - O(sigma(lambda))
     = p*D_lambda*O'(sigma(lambda))            (mod p²).  (2)
```

The two sides are values of one explicitly written coordinate-function vector at distinct parameter points **under the same coordinate convention**. The formula does **not** identify separate de Rham fibers or calculate any native semilinear Frobenius. A genuine native Frobenius comparison must declare parameter-lift and horizontal-fiber identification, both full matrix columns, H0/B0-to-geometric gauge, coefficient sigma and eta. If a proposed comparison uses literal-power evaluation, its neglected second-digit term is exactly (2).

## Exact executed witnesses: both original residue classes

A self-contained exact integer checker `tools/check_d25_hesse_frob_lambda_defect_20261112.py` was executed for `p=13,19,37,43,373`. It uses exact pairs `a+bT`, inverse by norm `a²-2b²`, explicit residue cube-root search, Hensel lifting, modular powers and **independent direct-versus-first-order observer evaluation**; all declared assertions passed, with no floats and no native H0/B0 substitute.

For `p=373`, `p²=139129`, using the **previously published frozen signed source root**:

```
lambda         = 91441 + 93269T,    lambda³=4+2T,
sigma(lambda)  = 91441 + 45860T,
lambda^373     = 90695 + 91366T,    (mod 139129)
Q_t            = 303 + 309T,        (mod 373)
D_lambda       = 371 + 122T.        (mod 373)
```

The difference of the exact *signed-observer coordinate vectors* is therefore

```
O(lambda^373)-O(sigma(lambda))
    = 373 * (249+323T, 258+310T)^T            (mod 139129).
```

Both coefficient coordinates retain a nonzero second-digit discrepancy, including the `T`-odd branch. This **refutes the candidate simplification** `lambda^p == sigma(lambda)` modulo p² at the original signed Hesse observer; it does **not** refute D25 LIFT/JT2.

For the smallest primes of each target class: at `p=13`, `Q_t=5+4T`, `D_lambda=4+3T`, observer defect divided by p is `(3+6T,12+11T)`; at `p=19`, `Q_t=10+18T`, `D_lambda=8+16T`, defect/p is `(6,13+8T)`. These are exact computed instances; no all-prime nonvanishing assertion is made. Formulae (1)-(2) remain exact even if `Q_t=0` at some prime.

## BRC observer audit and original next action

BRC interface `REUSE_APPLIED`: retain labels for the two operations `sigma` and literal power on the same `R_2` carrier, full `T`-signed coefficient pairs, p-adic digit `D_lambda`, original observer `O` and allowed future `O mod p²`. Collapsing to only modulo-p equality destroys `D_lambda` and fails fiber constancy for that future observation. This coefficient-ring chart is **not** a claimed native six-dimensional Heartbeat spatial coordinate. Prior full lambda-to-E3 signed Gauss–Manin map is reused, not reproved; no separate tool family or new worldview axiom is proposed.

**Native acceptance unchanged:** an authorized actual executor must produce the exact same-original-class H0/B0 divided-power `[X]U mod139129` at p373, native module rank and both semilinear Frobenius columns, actual lift/eta and the retained `T`-odd Green/Hesse kappa and frozen Delta-R comparison; check this parameter-power vs sigma distinction only if its actual Frobenius convention makes it relevant. Continue to both residue classes and independent review. Source support issue `#1559` remains `OPEN/PENDING_OWNER`. The author's new parameter test is `UNREVIEWED/NOT_ADMITTED`; no canonical native Result/freeze/Driver review or closure is claimed.

**Status:** `AUTHOR_PROVED / FIVE_EXACT_MODULAR_TESTS_EXECUTED / NOT_ADMITTED / NATIVE_NOT_RUN / PENDING_OWNER`.
