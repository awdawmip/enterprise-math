# BRC Horizontal–Vertical Multiplier Coverage Bridge — Round 9

Status: `PROVED DERIVED GEOMETRIC BRIDGE / EXISTING PRIORITY SCORE EXPLAINED / NO OPTIMALITY OR NOVEL FACTORIZATION CLAIM`
Date: `2026-09-07`
Parents: `t0.brc_multiplier_priority_jump`, `brc_multiplier_factor_scan`, `brc_multiplier_vertical_wheel`

## 1. Question

The current multiplier factor scan contains the experimental structural score

`score(m)=nu(m)^4/m`,

where `nu(m)` counts nontrivial same-parity factor pairs `m=u*v`.

Round 6 showed that this score gives a useful multiplier order, while the current
vertical wheel separately searches offsets

`x_t=x_0+t`.

Is the factor-pair score merely an empirical heuristic, or does it arise from the
joint horizontal-multiplier / vertical-Fermat geometry?

It has an exact geometric origin at small normalized vertical budget.

The derivation is elementary/classical difference-of-squares mathematics; the
Enterprise contribution here is the typed bridge between the existing
horizontal BRC multiplier state, the vertical wheel, and the already deployed
priority score.  No novelty claim for the classical identities is made.

## 2. Exact factor-ratio coordinate

Let

`N=p*q`, `1<p<q`,

and let one admissible multiplier factorization be

`m=u*v`,

with `u` and `v` of the same parity so that the usual difference-of-squares
coordinates are integral.  After exchanging the two factors if needed, define

`r=q/p > 1`,
`rho=u/v > 1`.

The corresponding exact classical witness coordinates are

`x=(u*p+v*q)/2`,
`b=(v*q-u*p)/2`,

and

`m*N=x^2-b^2`.

Put

`s=sqrt(m*N)`.

Then

`x/s`
`= (1/2)(sqrt(rho/r)+sqrt(r/rho))`
`= cosh((1/2) log(rho/r))`.

Therefore the exact real height above the multiplier square-root surface is

`h=x-s`
`= sqrt(m*N) * [cosh((1/2) log(rho/r))-1]`
`= sqrt(N)*sqrt(m) * [cosh((1/2) log(rho/r))-1]`.

This is the horizontal/vertical bridge: horizontal factor-pair mismatch becomes
vertical Fermat height through a hyperbolic distance on the log factor-ratio
axis.

## 3. Exact integer vertical offset

The current vertical wheel starts at

`x_0=ceil(sqrt(m*N))`.

Since `x` is an integer, its vertical offset is

`t=x-x_0`
`= floor(x-s)`
`= floor(h)`.

Thus a vertical search budget `0<=t<=T` contains the witness if and only if

`h<T+1`.

This `+1` is exact and comes only from the integer ceiling/floor boundary; it is
not an asymptotic approximation.

## 4. Exact log-ratio coverage interval

Define the normalized vertical budget

`theta=(T+1)/sqrt(N)`.

The witness condition becomes

`sqrt(m) * [cosh((1/2) log(rho/r))-1] < theta`.

Since cosh is even and increasing on the nonnegative line,

`|log(r/rho)|`
`< 2 arcosh(1+theta/sqrt(m))`.

Hence one same-parity factor pair `u*v=m` covers the exact open interval on the
log factor-ratio axis centered at `log(rho)` with half-width

`w_m(theta)=2 arcosh(1+theta/sqrt(m))`.

The full interval length is therefore

`4 arcosh(1+theta/sqrt(m))`.

This formula is independent of the unknown absolute scale of p and q once the
vertical budget is normalized by `sqrt(N)`.

## 5. Small-budget asymptotic

For `z -> 0+`,

`arcosh(1+z)=sqrt(2z)*(1-z/12+O(z^2))`.

With `z=theta/sqrt(m)`, one factor pair has log-ratio coverage length

`4*sqrt(2*theta)*m^(-1/4)`
`+ O(theta^(3/2)*m^(-3/4))`.

For a fixed multiplier m, its finitely many nontrivial same-parity factor-pair
centers are distinct.  Therefore, for sufficiently small theta, their intervals
are disjoint.  If `nu(m)` is their count, the exact union length has leading law

`L_m(theta)`
`= 4*sqrt(2*theta)*nu(m)*m^(-1/4)`
`+ O_m(theta^(3/2))`.

Define the normalized leading coefficient

`C_m = lim_{theta->0+} L_m(theta)/(4*sqrt(2*theta))`.

Then

`C_m=nu(m)*m^(-1/4)`.

Taking the fourth power gives the exact rational identity

`C_m^4 = nu(m)^4/m`.

Thus the existing multiplier score is precisely the fourth power of the
small-vertical-budget leading log-ratio coverage coefficient.

Because fourth power is monotone on nonnegative numbers, sorting by

`nu(m)^4/m`

is exactly the same as sorting by this leading geometric coverage coefficient.

## 6. Immediate square-gap surface

For the immediate multiplier scan, `T=0`, hence

`theta=1/sqrt(N)`.

As N grows, theta tends to zero.  The score therefore has a natural large-N
interpretation: among same-parity multiplier factor pairs, it ranks the first
order amount of log-factor-ratio axis covered by an immediate square-gap test.

This does **not** make the order universally optimal.  A probability statement
requires a prior/density on `log(q/p)`.  Under a locally flat density the leading
coverage coefficient is directly proportional to first-order hit mass; a
strongly nonuniform factor-ratio distribution can favor different centers and
therefore a different order.  This boundary is consistent with the earlier
training-order and kernel-compression distribution-shift failures.

## 7. Connection to the vertical wheel

The same exact interval formula explains the horizontal/vertical tradeoff.
Increasing T widens every center by

`2 arcosh(1+(T+1)/(sqrt(N)*sqrt(m)))`.

For fixed normalized vertical budget, larger m narrows each individual interval
as `m^(-1/4)` at first order, while a highly composite admissible m can provide
more centers through larger `nu(m)`.

The horizontal priority score is therefore not independent of the vertical
wheel: it is the small-budget leading coefficient of the same two-dimensional
search geometry.

This also suggests that future budget allocation should compare **union coverage
across centers**, rather than treating horizontal multiplier count and vertical
offset depth as unrelated costs.

## 8. Finite diagnostic

`experiments/brc_horizontal_vertical_coverage_bridge.py` computes exact floating
readouts of the analytic interval union for m<=100 and compares them with the
proved leading term.  Floating output is regression/diagnostic evidence only.

Across the 73 multipliers with at least one nontrivial same-parity factor pair:

| theta | max relative error | mean relative error |
|---:|---:|---:|
| 1e-2 | 4.8050e-4 | 1.4139e-4 |
| 1e-3 | 4.8106e-5 | 1.4145e-5 |
| 1e-4 | 4.8112e-6 | 1.4146e-6 |
| 1e-5 | 4.8112e-7 | 1.4146e-7 |
| 1e-6 | 4.8148e-8 | 1.4158e-8 |

The linear decrease in relative error with theta is consistent with the next
term of the arcosh expansion after factoring the leading square-root behavior.

## 9. Status of the existing score

This round upgrades the *interpretation* of

`multiplier_priority_score(m)=nu(m)^4/m`

from a purely empirical ratio-coverage score to a proved leading-order
horizontal/vertical coverage coefficient (up to a monotone fourth power).

It does **not** upgrade the resulting total multiplier order to a universal
optimality theorem.  Existing production ordering remains a heuristic beyond
this local geometric statement, and `m=1` remains a separately protected first
candidate for the near-square case.

## 10. Next

The new bridge changes the most useful `m>100` question.

Instead of asking only how to stream every multiplier cheaply, ask for a
budgeted two-dimensional cover:

`horizontal same-parity ratio centers`
`+ vertical-wheel interval widening`
`-> maximum log-ratio union coverage per unit cost`.

A theorem-backed sparse long-horizon family would need to control overlap and
coverage gaps across these intervals without learning a factor-ratio
distribution from the target population.
