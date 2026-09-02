# Enterprise Math BRC Logarithm Runtime Protocol

Status: `RESEARCH BRANCH OPERATIONAL / NO LOGARITHM-COLLAPSE THEOREM CLAIM`  
Effective: `2026-09-02`

## 1. Scope

This protocol extends the BRC-gated exact-arithmetic materialization layer to
real logarithms of positive rational carriers.

Native states may travel without evaluation:

```text
LN(DIV(n,d))
LOG_base(DIV(n,d))
```

with positive argument and positive base, and `base != 1` for `LOG`.

Freeze:

```text
LN_AND_LOG_MAY_TRAVEL_UNEVALUATED
LOGARITHM_MATERIALIZATION_REQUIRES_BRC_INTERVAL_CERTIFICATE
FLOAT_IS_READOUT_NOT_NATIVE_EVIDENCE
BIGINT_IS_THE_NATIVE_HIGH_PRECISION_CARRIER
R023_BOOLEAN_SUPPORT_THEOREMS_ARE_UNCHANGED
```

This is operational infrastructure. It does not add a logarithm theorem to the
canonical R023 Branch-Recoalescence Collapse Boolean-support semantic core.
That core still does not preserve multiplicity, provenance, probability or
weights, or signed/amplitude cancellation.

## 2. Why a direct power-basin formula is not enough

For base `b > 1` and positive `x`, a finite-scale logarithm index `q` formally
obeys

```text
q <= S*log_b(x) < q+1
```

which is equivalent to

```text
b^q <= x^S < b^(q+1).
```

This is an exact multiplicative basin description. But for decimal precision
`S = 10^d`, directly constructing `x^S` has bit size proportional to `10^d`.
It is therefore a bad precision algorithm even though the identity is exact.

The runtime instead builds exact rational analytic bounds whose integer size
grows with requested precision rather than with `10^d` as an exponent.

## 3. Natural logarithm range reduction

For a positive rational `x`, separate sign and magnitude:

```text
x = 1       -> ln(x) = 0
x > 1       -> sign = +1, y = x
0 < x < 1   -> sign = -1, y = 1/x
```

so `y >= 1` and `abs(ln x) = ln y`.

Choose the unique integer `k >= 0` satisfying

```text
2^k <= y < 2^(k+1).
```

Write `y = 2^k r`, where `1 <= r < 2`, and set

```text
z = (r - 1) / (r + 1).
```

Then

```text
0 <= z < 1/3
ln(r) = 2 * sum_{j>=0} z^(2j+1)/(2j+1).
```

The implementation never needs to materialize `r` or `z` as a floating value.
For `r = N/D`, the coordinate is carried exactly as

```text
z = (N-D)/(N+D).
```

## 4. Exact lower and upper bounds

After `N` positive terms, define

```text
L_N(z) = 2 * sum_{j=0}^{N-1} z^(2j+1)/(2j+1).
```

For `0 < z < 1`, the omitted positive tail satisfies

```text
0 < ln((1+z)/(1-z)) - L_N(z)
  < 2*z^(2N+1) / ((2N+1)*(1-z^2)).
```

For `z = 0`, the value is exactly zero.

Both `L_N` and the remainder majorant are stored as literal non-negative
integer numerator / positive denominator pairs. The series is evaluated in a
Horner form so unreduced denominator growth remains controlled. No `Fraction`,
`Decimal`, float, native `/`, `//`, or `%` state is required.

Bounds for `abs(ln x)` are then

```text
k * lower(ln 2) + lower(ln r)
k * upper(ln 2) + upper(ln r).
```

Since every reduced coordinate has `z <= 1/3`, the remainder contracts
geometrically. The implementation doubles the term count until the requested
precision cell is decided.

## 5. BRC finite-scale cell

Let exact rational bounds be

```text
L <= abs(value) <= U
```

and let `S` be a positive integer scale. Decimal readout uses `S = 10^digits`.

The runtime sends both exact carriers

```text
DIV(S * numerator(L), denominator(L))
DIV(S * numerator(U), denominator(U))
```

through the existing BRC division facade.

If both BRC quotient traces return the same integer `q`, then

```text
q <= S * abs(value) < q + 1
```

is certified by exact rational bounds plus exact quotient/remainder evidence.
The native logarithm trace retains:

```text
operation
scale
sign
magnitude_index = q
exact lower and upper rational bounds
series term count
power-of-two range coordinates
lower BRC division trace
upper BRC division trace
exact-boundary marker
optional exact power-relation proof
```

Signed human text uses truncation toward zero. The exact interval, not the
printed decimal punctuation, is the mathematical evidence.

## 6. Arbitrary-base logarithm

For positive base `b != 1` and positive argument `x`, the runtime uses

```text
abs(log_b x) = abs(ln x) / abs(ln b)
sign(log_b x) = sign(ln x) * sign(ln b).
```

If

```text
Lx <= abs(ln x) <= Ux
Lb <= abs(ln b) <= Ub
```

with `Lb > 0`, exact rational interval arithmetic gives

```text
Lx / Ub <= abs(log_b x) <= Ux / Lb.
```

These quotients are represented symbolically by cross multiplication of
integer numerator/denominator carriers. They are not materialized as Python
native division.

## 7. Exact grid-boundary problem

A pure two-sided interval algorithm has a special failure mode for exact
rational logarithms.

Example:

```text
log_4(2) = 1/2.
```

At a decimal scale divisible by `2`, lower bounds remain below the exact grid
boundary while upper bounds remain above it. Refinement alone therefore never
places both bounds in one open precision cell.

When lower and upper BRC traces occupy adjacent cells, the shared boundary is
a candidate exact value

```text
q/S = m/n
```

in lowest terms.

For positive rational magnitudes, exactness is equivalent to

```text
x^n = b^m.
```

The runtime deliberately does **not** construct these potentially enormous
powers. Since `gcd(m,n)=1`, unique factorization implies that equality holds iff
there exists a positive rational `c` with

```text
x = c^m
b = c^n.
```

Therefore the implementation:

1. value-reduces the argument/base rational carriers only inside the requested
   evaluation, through BRC-gated exact integer division;
2. asks the existing BRC ROOT/perfect-power facade whether argument numerator
   and denominator are exact `m`-th powers;
3. asks whether base numerator and denominator are exact `n`-th powers;
4. compares the recovered rational roots by cross multiplication.

If the roots agree, the boundary receives an explicit
`BRC_LOG_EXACT_POWER_RELATION` proof trace.

This resolves examples such as

```text
log_10(1000) = 3
log_4(2) = 1/2
```

without floating equality tests and without exponentiation by the precision
scale.

## 8. Precision behavior

The reference implementation uses arbitrary-precision Python integers.

Representative regression:

```text
LN(2), 1000 decimal digits
```

is resolved by adaptive exact interval refinement; no floating logarithm is
called and no fixed-width integer is introduced.

There is no project-level mathematical digit ceiling. Memory/time limits are
implementation limits and must not be silently converted into false precision.

## 9. Hard boundaries

This V1 runtime does not cover:

- zero or negative real arguments;
- complex logarithm branches;
- an exact symbolic transcendence algebra for arbitrary expressions;
- weighted/probabilistic BRC semantics;
- multiplicity recovery after Boolean support has erased multiplicity;
- a theorem claiming that LN/LOG itself is a canonical BRC collapse operator.

A future weighted branch calculus may legitimately use logarithmic coordinates:
path-weight multiplication becomes addition of log weights, while alternative
branch aggregation becomes a log-sum-exp operation. That would require a new,
explicit weighted carrier and theorem surface. It is not smuggled into R023 by
this runtime change.

## 10. Reference implementation

- policy: `brc_logarithm_runtime_policy.json`
- runtime: `src/enterprise_math/brc_logarithm.py`
- regression: `tests/test_brc_logarithm_runtime.py`
- shared DIV/ROOT facade: `src/enterprise_math/exact_arithmetic.py`
- static arithmetic gate: `tools/check_exact_arithmetic_policy.py`

Tool reuse classification:

```text
T0_BRC
+ T5_PRECISION_REFINEMENT
+ P007_DISCRETE_DIVISION
+ existing ROOT/perfect-power BRC facade
-> EXTEND_EXISTING_TOOL / operational logarithm facade
```

No new general-purpose numerical oracle is introduced.
