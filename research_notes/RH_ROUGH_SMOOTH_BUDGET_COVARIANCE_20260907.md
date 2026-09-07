# RH rough/smooth product-budget covariance and first-mode renormalization

Status: `RESEARCH FRONTIER / PROVED ASYMPTOTIC + EXACT BRC IDENTIFICATION + NO-GO / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Scope: `RH / Möbius / rough-smooth coupling / Alladi polynomial / hyperbola budget / BRC`
Parent frontier:

- `RH_ROUGH_DIVISOR_DUHAMEL_QUOTIENT_CELL_BRC_20260907.md`
- `RH_KUBILIUS_SUFFIX_PREFIX_SHIFT_INTENSITY_BARRIER_20260907.md`

## 0. Purpose and typing guard

The parent note reduced the unresolved dependence to the centered correlation

`C_X(z)=Cov_X((-z)^(h_Y(N_X)), A^suf_(N_X,f)(z)).`

It was still possible that centering the suffix innovation might automatically annihilate the one-dimensional dominant Green mode. This note tests that possibility at the first nontrivial rough-depth derivative.

P000 remains unchanged. The arithmetic cutoff hyperbola `pq<=X` is a relation/budget constraint, not a native X6 boundary. Prime labels remain provenance.

BRC discipline:

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

No positive covariance or branch count is interpreted as Möbius cancellation.

---

## 1. Exact first-variation identity

Let `N_X` be uniform on `1,...,X`. Fix a cutoff `Y` and define

`H_Y(n)=sum_(Y<p<=X) 1_(p|n),`

`S_(beta,Y)(n)=sum_(q<=Y) q^beta 1_(q|n),`

where both sums are over primes and `beta>0`.

Take the suffix prime test function

`f_(beta,Y)(q)=q^beta 1_(q<=Y).`

Write `t=1+z`. The exact rough-prefix factor is

`(-z)^(H_Y)=(1-t)^(H_Y).`

At `t=0`, the suffix Alladi polynomial satisfies

`A^suf_(n,f)(-1)=-S_(beta,Y)(n).`

If

`C_X(t)`
`= Cov_X((1-t)^(H_Y(N_X)), A^suf_(N_X,f)(t-1)),`

then differentiation at `t=0` gives

`C_X'(0)=Cov_X(H_Y(N_X),S_(beta,Y)(N_X)).`

The derivative of the suffix polynomial contributes no extra term because the rough factor equals the constant `1` at `t=0`, and covariance with a constant vanishes.

Expanding divisibility indicators gives the exact finite identity

`C_X'(0)`
`= sum_(q<=Y) q^beta sum_(Y<p<=X)`
`  [floor(X/(pq))/X`
`   -floor(X/p)floor(X/q)/X^2].`

This is the first rough-prime/small-prime coupling coefficient of the full Duhamel carrier.

---

## 2. Hyperbola-wedge asymptotic

### Proposition

Fix `kappa>0` and `beta>0`. Let

`Y=(log X)^kappa`

(up to an immaterial integer part). Then, as `X->infinity`,

`Cov_X(H_Y,S_(beta,Y))`
`= -Y^beta/(beta log X) (1+o(1)).`

Equivalently,

`C_X'(0)`
`= -(1/beta)(log X)^(kappa beta-1)(1+o(1)).`

### Proof

For `pq<=X`, the two divisibility events satisfy

`floor(X/(pq))/X`
`=1/(pq)+O(1/X),`

while

`floor(X/p)floor(X/q)/X^2`
`=1/(pq)+O(1/(Xp)+1/(Xq)+1/X^2).`

Their main terms cancel.

For `pq>X`, the joint event is impossible, whereas the product of the marginal densities still has main term `1/(pq)`. Summing the floor errors by the prime number theorem and partial summation gives

`Cov_X(H_Y,S_(beta,Y))`
`= -sum_(q<=Y) q^(beta-1)`
`    sum_(X/q<p<=X) 1/p`
`  +O(Y^beta/(log X log Y))`
`  +o(Y^beta/log X).`

The ranges satisfy `X/q>Y` for all `q<=Y` once `X` is large, so the explicit lower restriction `p>Y` is automatic in the main wedge.

Mertens' prime-harmonic estimate, uniformly for `q<=Y`, gives

`sum_(X/q<p<=X)1/p`
`= loglog X-loglog(X/q)+O(1/log X)`
`= -log(1-log q/log X)+O(1/log X)`
`= (log q)/(log X)`
`  +O((log q)^2/(log X)^2+1/log X).`

Since `log Y=o(log X)`, partial summation and the prime number theorem give

`sum_(q<=Y) q^(beta-1)log q`
`=Y^beta/beta (1+o(1))`

and

`sum_(q<=Y) q^(beta-1)(log q)^2`
`=O(Y^beta log Y).`

Substitution yields

`Cov_X(H_Y,S_(beta,Y))`
`= -Y^beta/(beta log X)(1+o(1)).`

QED.

The proof uses only classical prime-number-theorem scale input. It does not assume RH or a square-root prime discrepancy.

---

## 3. Critical balance law

The covariance has three regimes determined by the product `kappa beta`:

- if `kappa beta<1`, the first coupling mode tends to zero;
- if `kappa beta=1`, it tends to the nonzero constant `-1/beta=-kappa`;
- if `kappa beta>1`, its magnitude grows like a power of `log X`.

Thus the exact critical balance is

`CUTOFF_EXPONENT x PRIME_WEIGHT_EXPONENT = 1.`

For the RH source used throughout the current route,

`Y=(log X)^2`, `beta=1/2`,

so

`C_X'(0)->-2.`

This is the geometric meaning of the first surviving rough/smooth mode:

> the weight `sqrt(q)` exactly compensates the shrinking harmonic width of the forbidden hyperbola wedge `X/q<p<=X`.

The constant `2` is not inserted by hand. It is the reciprocal weight exponent `1/beta` at the critical relation `kappa beta=1`.

---

## 4. Consequence for the Green-mode strategy

The result disproves the naive annihilation hypothesis

`CENTERED_SUFFIX_INNOVATION -> AUTOMATIC_ZERO_FIRST_ROUGH_MODE.`

Even after the trivial late rough state has been removed by covariance centering, the first nontrivial rough-prime layer survives with a nonzero constant limit.

Freeze:

`CENTERING_KILLS_CONSTANT_MODE, NOT_HYPERBOLA_BUDGET_MODE`.

The obstruction is not internal small-prime correlation. The Kubilius parent result already replaces that dependence by an independent Bernoulli carrier at square-root total-variation scale. The surviving first mode is created by the finite product budget `pq<=X` linking the rough and small sectors.

In BRC terms, independent branching would include all rough/small prime pairs. The arithmetic Cell budget deletes the branches lying beyond the multiplicative hyperbola. Their missing signed/weighted mass is exactly the covariance main term.

---

## 5. Unconditional first-mode counterterm

The proposition supplies a deterministic continuum counterterm. Define

`B_(kappa,beta)(X)=Y^beta/(beta log X).`

Then

`C_X'(0)+B_(kappa,beta)(X)`
`=o(Y^beta/log X).`

At the critical balance `kappa beta=1`,

`C_X'(0)+1/beta=o(1).`

In particular,

`C_X'(0)+2=o(1)`

for `Y=(log X)^2`, `f(q)=sqrt(q)`.

Thus the first dependence mode is not merely identified; its universal product-budget main term can be removed unconditionally.

Freeze:

`FIRST_ROUGH_SMOOTH_BUDGET_MODE = EXPLICIT_CONTINUUM_COUNTERTERM + o(MAIN_SCALE)`.

This is only a first-order renormalization near `z=-1`. It does not control the full Alladi polynomial, growing jets, or the critical observer required by RH.

---

## 6. Exact relation to prime intensity

The first-mode covariance and the one-point intensity discrepancy are different objects.

The one-point source is

`J_(1/2)(Y)`
`=sum_(q<=Y)q^(-1/2)`
` -int_2^Y dt/(sqrt(t)log t).`

The covariance main term instead comes from the two-sector exclusion wedge

`-sum_(q<=Y)q^(-1/2)`
`  sum_(X/q<p<=X)1/p.`

Therefore removing the `-2` budget mode does not estimate `J_(1/2)(Y)`. It only prevents the deterministic product boundary from being mistaken for an unexplained parity/prime-discrepancy effect.

This separation is important:

- `J_(1/2)` measures discrete one-point prime intensity against its continuum carrier;
- `C_X'(0)` measures rough/small incidence lost to the finite product hyperbola;
- both must be tracked in a complete critical source model.

---

## 7. Finite numerical pilot

The exact checker evaluates the covariance directly and by the prime-pair floor formula. For the critical case it gives:

| `X` | `Y=floor((log X)^2)` | exact finite covariance |
|---:|---:|---:|
| `10,000` | `84` | `-1.792583271041...` |
| `100,000` | `132` | `-1.908435203657...` |
| `1,000,000` | `190` | `-1.922508157264...` |

The convergence is slow, as expected from the logarithmic error terms, but the values are consistent with the proved limit `-2`.

The table is diagnostic only; the theorem is supplied by the preceding asymptotic argument.

---

## 8. Exact checker

Task-local checker:

`experiments/rh_rough_smooth_budget_covariance_check.py`.

It verifies:

- the exact equality between direct covariance and the prime-pair floor formula for integer prime weights;
- the critical finite pilot for `f(q)=sqrt(q)`;
- numerical approach toward the continuum main term.

No finite computation is used as a proof of the asymptotic or of RH.

---

## 9. New smallest research unit

The constant mode and the first hyperbola-budget mode are now separated:

1. covariance centering removes the constant rough state exactly;
2. the first rough-prime mode has the explicit universal counterterm `-Y^beta/(beta log X)`;
3. the renormalized first mode is lower order unconditionally.

The next unresolved object is the collective higher-order remainder in the critical neighborhood:

`C_X(t)-t C_X'(0)`

with `t=1+z`, after replacing `C_X'(0)` by its explicit continuum main term.

A valid next step should derive the two-rough-prime / first-suffix-jet coefficient exactly and determine whether its leading hyperbola-budget contribution also has a universal continuum counterterm. The calculation must retain:

- ordered rough-prime provenance;
- suffix Alladi jets;
- quotient/product budget;
- the high-arity repair;
- signs until the final observer.

If every fixed Taylor layer admits an explicit continuum counterterm but uniform control fails when the layer number grows to `K~log X/(2loglog X)`, that failure will identify the precise transition from finite-order renormalization to the RH-strength collective problem.

No RH proof is claimed.
