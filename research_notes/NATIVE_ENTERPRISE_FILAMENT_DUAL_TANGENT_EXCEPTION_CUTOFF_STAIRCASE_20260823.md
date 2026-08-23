# Native Enterprise filament windows: dual-tangent exceptional-prime cutoff staircase

Status: `FREE_RESEARCH_EXACT_LOCAL_SIEVE_CUTOFF_CLASSIFICATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_SHARP_NINE_ENDPOINT_HOLOGRAPHY_AND_DUAL_TANGENT_SIEVE_20260823.md`.

## 1. Window of k consecutive filament Cells

Use a constant-h typed filament and a reference shell parity `chi in {+1,-1}`. For a window

`j=0,1,...,k-1`,

write the values relative to the first Cell as

`p_j = c + 3*r*j + (3*j^2 + chi*1_{j odd})/2`.

For an odd prime q, the q-divisibility locus of the j-th value is one affine line in the `(r,c)` plane.

As in the sharp-nine case, even-j lines are tangents to one parabola and odd-j lines are tangents to the parallel shifted parabola.

## 2. Only mixed-parity triple concurrence matters

Three same-parity lines cannot concur because they are distinct tangents to one nondegenerate parabola.

If `a,b` have the same parity and `l` the opposite parity, concurrence can occur only when q divides one of

`3*(l-a)*(l-b)+1`,

`3*(l-a)*(l-b)-1`.

Since the two differences are odd, their product is odd, and both obstruction integers are even.

## 3. Maximum distance product

Let

`M_k = max |(l-a)(l-b)|`

over indices `0<=a,b,l<=k-1` with `a,b` distinct and same parity and `l` opposite parity.

An exact extremal calculation gives

- for even k:
  `M_k=(k-1)(k-3)`;
- for odd k:
  `M_k=(k-2)(k-4)`.

Proof: for even k the maximum is attained by `(a,b,l)=(0,2,k-1)` or its reflection, giving `(k-1)(k-3)`; every other placement shortens at least one odd distance. For odd k the last usable opposite-parity extreme gives `(k-2)(k-4)`, again attained and maximal by reflection.

Equivalently, if e is the largest odd integer strictly below k, then

`M_k=e*(e-2)`.

## 4. Universal exceptional-prime cutoff

Any odd prime q dividing a nonzero obstruction integer satisfies

`q <= (3*M_k+1)/2`,

because the obstruction is even and has absolute value at most `3*M_k+1`.

Thus every prime above

`Q_k=(3*M_k+1)/2`

is automatically generic: the k bad lines have no triple concurrence.

For the filament sizes relevant to the global prime-island spectrum:

| k | M_k | Q_k | largest possible exceptional prime |
|---:|---:|---:|---:|
| 5 | 3 | 5 | 5 |
| 6 | 15 | 23 | 23 |
| 7 | 15 | 23 | 23 |
| 8 | 35 | 53 | 53 |
| 9 | 35 | 53 | 53 |

Each displayed bound is sharp: the top value comes from the obstruction `3*M_k+1` and is prime for k=5,6/7,8/9 respectively.

Formally continuing to k=3,4 gives the preliminary steps 2 and5, but global k=3,4 islands also have separate short triangle/diamond geometry and should not be conflated with the long-filament classification.

## 5. Exact exceptional sets for the realized filament lengths

With the additional requirement that line slopes are distinct modulo q, the actual non-generic prime channels are:

- k=5: `{5}`;
- k=6: `{7,11,23}` after the smaller slope-collision channel 5;
- k=7: `{7,11,13,23}` after the smaller slope-collision channel 5;
- k=8: `{11,13,23,31,53}` after smaller 5,7 effects;
- k=9: `{11,13,23,31,53}` after smaller 5,7 effects.

The k=8 and k=9 windows therefore already share the same post-small-prime exceptional support.

## 6. Generic survivor polynomial

Once q is above the cutoff, all k slopes are distinct and every pairwise line intersection is distinct, with no triple concurrence.

Hence the bad-line union has exactly

`k*q - C(k,2)`

points, and the q-avoiding parameter count is

`N_{k,q}=q^2-k*q+C(k,2)`.

Thus beyond Q_k the entire local finite-field geometry is frozen into one quadratic polynomial in q.

## 7. The 5 -> 53 cascade

The global typed-incidence classification proves:

- prime5 is the unique finite-wheel channel that destroys every unbounded filament;
- consequently actual prime-incidence islands have size at most9;
- the maximum filament window therefore has k=9;
- k=9 gives `M_9=35` and `Q_9=53`.

Hence the two extremal primes play different structural roles:

`5 = UNIQUE GLOBAL CONNECTIVITY BREAKER`,

`53 = FINAL LOCAL DUAL-TANGENT EXCEPTION ALLOWED BY THE RESULTING MAXIMAL WINDOW`.

This is an exact geometry-to-arithmetic cascade for the frozen allocation.

## 8. Boundary

Finite-field line arrangements and quadratic local sieves are classical. The research-specific content is the exact cutoff staircase selected by the native filament geometry and the sharp global island-size cap.
