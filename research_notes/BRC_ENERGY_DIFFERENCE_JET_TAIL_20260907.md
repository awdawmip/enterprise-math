# BRC Square-Increment Difference Jet — Round 13

Status: `PROVED THIRD-DIFFERENCE PRODUCT TRANSPORT / POST-SEED GENERAL-MULTIPLICATION-FREE TAIL / FINITE PIPELINE CROSSOVER`
Date: `2026-09-07`
Parents: `t0.brc_quotient_jet_tail`, `t0.brc_linear_deep_tail`, `t0.brc_square_gap_cascade`
Reuse resolution: `EXTEND_EXISTING_TOOL`

## 1. Question

The quotient/remainder jet removes the repeated division in the order-one linear
BRC tail.  Its remaining general hot-loop multiplication is

`E_m = q_m(2J_m+q_m)`,

used in

`G_m = R_m + hN - E_m`.

Can the same derivative/finite-difference program transport this square
increment without recomputing a product of two N-growing integers at every
retained multiplier?

Yes.  On each fixed mod-8 source orbit, a third-difference identity plus one
retained mixed coordinate makes the post-seed loop general-multiplication-free.

## 2. Fixed residue orbits

For odd N, the exact representative source multipliers have residues

`{0,1,3,5,7} mod 8`.

Each residue has a fixed outgoing step h:

| source residue | h |
|---:|---:|
| 0 | 1 |
| 1 | 2 |
| 3 | 2 |
| 5 | 2 |
| 7 | 1 |

Fix one orbit

`m_k = m_0 + 8k`.

Write

`J_k = floor(sqrt(m_k N))`,

`q_k = floor(2h J_k/(4m_k+h))`,

`E_k = q_k(2J_k+q_k)`.

The parent quotient jet already transports `q_k` and its Euclidean remainder
with three seed samples and a bounded exact repair.

## 3. Difference coordinates

Use backward differences at the current orbit point k:

`s = nabla q_k`,

`a = nabla^2 q_k`,

`t = nabla J_k`,

`u = nabla^2 J_k`.

At the next point define

`e = nabla^3 q_(k+1)`,

`w = nabla^3 J_(k+1)`.

Then

`q_(k+1) = q_k + s + a + e`,

`J_(k+1) = J_k + t + u + w`.

The quotient-jet theorem supplies

`-4 <= e <= 4`

and preserves

`-2 <= a+e <= 98`.

## 4. Exact root third-difference bound

Let

`f(x)=sqrt(Nx)`.

For stride 8, the iterated-integral identity gives

`Delta_8^3 f(m)`
`= integral_[0,8]^3 f'''(m+x+y+z) dx dy dz`.

Since

`f'''(x)=3 sqrt(N)/(8x^(5/2))`

is positive and decreasing,

`0 < Delta_8^3 f(m) <= 8^3 f'''(m)`
`= 192 sqrt(N)/m^(5/2)`.

On the common linear tail

`4m^5 >= N`,

so

`sqrt(N)/m^(5/2) <= 2`

and therefore

`0 < Delta_8^3 f(m) <= 384`.

Write

`J(m)=f(m)+eta(m)`

with

`-1 < eta(m) <= 0`.

The positive and negative coefficient masses of a third difference are both 4,
so

`-4 < Delta_8^3 eta(m) < 4`.

Thus

`-4 < Delta_8^3 J(m) < 388`.

Because the left side is an integer,

`-3 <= w <= 387`.

Both endpoints are populated by exact witnesses retained in regression:

- `w=-3` at `N=18432563335758795797`, oldest `m=5412521`;
- `w=387` at
  `N=326270861943277281288965027192289443045`, oldest `m=38227135`.

The interval must not be silently tightened.

## 5. Exact third-difference law for the square increment

Put

`E(q,J)=q(2J+q)`.

Expand

`E_(k+1)-3E_k+3E_(k-1)-E_(k-2)`

using the difference coordinates above.  The result is the exact identity

`nabla^3 E_(k+1)`
`= e*(2*(J+q+s+a+t+u+w)+e)`
`  + 2*w*(q+s+a)`
`  + 6*(s*u + a*(s+t))`.

No approximation or asymptotic replacement occurs.

The square increment then advances by the ordinary Newton-difference shift

`E_(k+1)`
`= E_k + nabla E_k + nabla^2 E_k + nabla^3 E_(k+1)`.

Its first and second differences update by

`nabla E_(k+1)`
`= nabla E_k + nabla^2 E_k + nabla^3 E_(k+1)`,

`nabla^2 E_(k+1)`
`= nabla^2 E_k + nabla^3 E_(k+1)`.

## 6. Retaining the sole unbounded mixed product

The displayed third-difference identity contains one product whose two factors
both grow with N:

`M_k = s*u = (nabla q_k)(nabla^2 J_k)`.

Do not recompute it.  Retain it as a typed provenance coordinate.

At the next point,

`s_new = s + a_new`,

`u_new = u + w`,

where

`a_new=a+e`.

Therefore

`M_new`
`= (s+a_new)(u+w)`
`= M_k + s*w + a_new*u + a_new*w`.

Every newly evaluated product now has a fixed bounded integer factor:

- `e in [-4,4]`;
- `a_new in [-2,98]`;
- `w in [-3,387]`.

Consequently the recurrence hot path performs no multiplication of two
N-growing operands.

This is another observer/provenance result: collapsing `M_k` would force a new
general multiplication on the next visit.

## 7. Seed and steady-state operation counts

There are five source residue orbits and each needs three samples.

The exact seed budget is therefore:

- 15 Euclidean quotient divisions;
- 15 direct square-increment products;
- 5 mixed `s*u` products when the orbits activate;
- one initial square root for the starting multiplier state.

After all five orbits activate, every later transition uses:

1. quotient/remainder jet repair by at most four denominator additions or
   subtractions;
2. bounded-coefficient updates of the square-increment difference jet;
3. at most two ordinary BRC odd-width root corrections;
4. the unchanged staged square-gap residue cascade;
5. exact gap `isqrt` only on cascade survivors.

There is no per-multiplier square-root ratio table, fresh quotient division, or
fresh general square-increment product.

## 8. Seed accounting

The new energy-difference scanner computes exactly one Euclidean quotient and one
direct square-increment product on each of three seed visits to each of five
source residue classes.  Thus its own hot path has exactly 15 seed divisions and
15 seed products; later visits use the quotient and energy recurrences.

The existing parent quotient scanner remains an exact comparison oracle.  Its
internal constructor may rematerialize seed quotients, so benchmark conclusions
are stated for the new scanner's counted operations rather than as a parent-tool
implementation claim.

## 9. Exact lower-order identities considered

The quotient relation

`2hJ=q(4m+h)+rho`

also gives an exact reduced-scale provisional-gap identity.  With

`r=rho/h`

(which is integral for h=1,2),

`G = R + q*r + ((q+r)^2+4R)/(4m/h)`.

This removes the original `q(2J+q)` product algebraically, but introduces an
exact large-integer division at every step.  It was substantially slower than
the native product in the tested CPython implementation and is not promoted.

A first-order same-orbit transport of E also exists:

`E_new=E+2q(t+s_new)+s_new(2J_new+s_new)`.

It lowers operand scales but still evaluates two general products.  The
third-difference jet strictly subsumes it by retaining enough derivative state
to eliminate those products.

## 10. Validation

Repository regression includes:

- symbolic/numeric verification of the exact third-difference identity;
- exact endpoint witnesses for the root interval `[-3,387]`;
- exhaustive odd `N<500`, 200 transitions each;
- random 64..8192-bit scans, 500 transitions each;
- exact comparison of multiplier, root, root remainder, quotient, quotient
  remainder and square increment against direct integer oracles;
- root correction count at most 2;
- quotient third difference in `[-4,4]`;
- exactly 15 seed divisions and 15 seed square-increment products.

## 11. Finite full-pipeline benchmark

The committed benchmark uses five deterministic odd N values per bit size and
1,500 retained transitions per value.  All three paths use the same BALANCED
`4032 -> 12155 -> 12673` square-gap cascade and exact gap square-root check on
survivors.

The direct baseline incrementally updates the target by `hN` before each
`math.isqrt`; it does not pay an artificial full `mN` multiplication.

| N bits | direct isqrt / energy jet | fresh product / energy jet |
|---:|---:|---:|
| 1024 | 0.771x | 0.923x |
| 2048 | 1.149x | 0.655x |
| 4096 | 1.883x | 0.964x |
| 8192 | 2.517x | 1.264x |
| 16384 | 2.488x | 1.294x |

Interpretation:

- the added state and bounded-coefficient bookkeeping is not worthwhile for
  small integers;
- it is near parity with the fresh product around 4096 bits in this run;
- at 8192 and 16384 bits it improves the already division-free quotient-jet
  pipeline by about 26% and 29%;
- relative to direct per-state roots plus the same cascade, the complete path is
  about 2.5x faster in those two cohorts.

These are finite CPython/environment timings, not a machine-independent
asymptotic speed theorem.  An AUTO router should retain the native fresh product
below the measured crossover and select the energy jet only for sufficiently
large operands.

## 12. Decision and boundary

Promote as a T0_BRC extension:

`QUOTIENT/REMAINDER JET`
`+ ROOT DIFFERENCE JET`
`+ RETAINED (Delta q)(Delta^2 J)`
`-> EXACT SQUARE-INCREMENT DIFFERENCE JET`.

The result is an exact execution improvement.  It does not:

- reduce the multiplier search horizon;
- change Lehman/Hart-style factor-search complexity;
- prove RSA-scale practicality;
- create a new factorization principle;
- mutate Foundation or Working Truth.

The multiplication eliminated here was an execution cost after the factor-search
candidate had already been selected.

## 13. Next frontier

After Round 13, the large-integer steady-state loop consists mainly of:

- bounded-coefficient big-integer additions for the quotient and energy jets;
- at most two odd-width BRC corrections;
- three staged modular reductions for square-gap filtering.

The next discriminating attack is not another derivative order.  It is to ask
whether the three cascade residues of the completion gap can themselves be
transported from the retained difference-jet state, replacing three full
big-integer modulo operations with fixed-modulus residue recurrences.  That
attack must preserve zero false negatives and must be benchmarked against the
highly optimized native `%` operation.
