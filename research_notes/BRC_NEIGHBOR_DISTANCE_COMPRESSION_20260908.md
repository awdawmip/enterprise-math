# BRC Neighbor-Distance Compression — One Low-Bit Residue for a Whole Local Window

Status: `PROVED EXACT DISTANCE-WINDOW COMPRESSION / OPPORTUNISTIC HORIZON EXTENSION / FINITE BALANCED DIAGNOSTIC / NO ASYMPTOTIC CLAIM`
Date: `2026-09-08`
Parent: `t0.brc_neighbor_square_lift_shortcut`

## 1. Generalize N±1 to N±d

The unit-distance parent law extends without approximation.  Let

`N=a^2 t + epsilon d`,

where `d>=1`, `epsilon in {+1,-1}`, and set

`m=2a-epsilon d`.

Then

`mN=a^2(mt+1)-(a-epsilon d)^2`.

Thus `mt+1=c^2` yields

`mN=(ac)^2-(a-epsilon d)^2`.

The proof is the same cancellation as at d=1:

`m epsilon d = (2a-epsilon d)epsilon d = 2a epsilon d-d^2`

and

`a^2-(a-epsilon d)^2=2a epsilon d-d^2`.

This is still a multiplier-Fermat / difference-of-squares specialization.  The
only new question is whether many local distances can be inspected without
paying one divisibility test per distance.

## 2. Exact one-residue compression theorem

Fix an ordinary multiplier horizon H and a local distance budget D.  Consider
only square roots `a=2^k` of power-of-two square divisors.

Choose a power of two `a0=2^k` satisfying

`2*(a0/2)+D <= H < 2*a0+D`,

and

`2D<a0^2`.

These two inequalities have distinct jobs.

### Lower levels are already covered

At every smaller power-of-two root `a<a0`, the largest possible induced
multiplier occurs for epsilon=-1 and d=D:

`m=2a+D <= 2*(a0/2)+D <= H`.

Therefore no lower square level can contribute a new multiplier beyond H.

### The signed distance is unique

At level `a0^2`, a local candidate must satisfy

`N == epsilon d (mod a0^2)`, `1<=d<=D`.

Because `2D<a0^2`, the two radius-D arcs around residue 0 do not overlap.  Hence
there is at most one signed local distance.  It is read directly from

`r=N mod a0^2`

as

`d=min(r,a0^2-r)`.

The sign is epsilon=+1 when r=d and epsilon=-1 otherwise.

Since `a0^2` is a power of two, r is a low-bit mask rather than a general
integer division.

### No-return theorem

If this unique start-level distance exceeds D, no larger power-of-two square
level can later produce any local distance <=D.

Indeed, divisibility by `a1^2` for `a1>a0` implies divisibility by `a0^2`.
Any later signed distance d'<=D would therefore already solve the unique
start-level congruence, contradicting its absence.

If the distance is present, compute `v2(N-epsilon*d)` once.  That valuation
reveals every higher square level on the **same** signed neighbor.  Consequently
all beyond-H power-of-two candidates in the complete radius-D window are found
without scanning d=1,...,D.

## 3. Exact H=100,D=64 specialization

For the project's long-used bounded multiplier horizon H=100 and local radius
D=64, the certified start root is

`a0=32`.

Check:

`2*16+64=96 <=100`,

`100 < 2*32+64=128`,

and

`2*64=128 < 32^2=1024`.

Therefore the entire power-of-two radius-64 search beyond m=100 reduces to

`r = N mod 1024 = N & 1023`.

Set

`d=min(r,1024-r)`.

If `d>64`, the exact result is: **there is no power-of-two neighbor-square
candidate with m>100 anywhere in the whole radius-64 window, at any higher
square level**.

If `d<=64`, one `v2(N±d)` determines the full candidate chain.

Repository regression compares this compressed enumeration against explicit
scans of every distance and every power-of-two square level for all odd
`101<=N<2500` and `D in {8,16,32,64}`.  The candidate sets agree exactly when
`all_levels=True`.

## 4. Balanced horizon-extending witness

The compression finds a nontrivial balanced semiprime witness missed by the
m<=100 immediate multiplier scan:

`N=7,245,781=1847*3923`.

At the start modulus 1024,

`N+43` is divisible by `64^2`, so

`d=43`, `epsilon=-1`, `a=64`,

and

`m=2*64+43=171`.

The quotient is

`(N+43)/64^2=1769`,

and

`171*1769+1=550^2`.

Hence

`171N=(64*550)^2-(64+43)^2`

`=(35200)^2-107^2`.

Gcd of the two sides with N recovers 1847 and 3923.  A direct m<=100
multiplier-Fermat check has no proper factor witness for this N, so this is a
genuine horizon extension rather than only a reordered bounded candidate.

## 5. Finite balanced diagnostics

The committed diagnostic fixes H=100,D=64, uses only the maximum square level on
the unique signed neighbor, and samples 20,000 balanced semiprimes per cohort.

| cohort | prime source | triggers | factor hits | incremental vs m<=100 |
|---|---|---:|---:|---:|
| A | primes 1009..4999 | 926 | 1 | 1 |
| B | primes 10007..50000 | 999 | 0 | 0 |
| C | random 24-bit primes | 872 | 0 | 0 |

The trigger frequency is a few percent because it asks only whether one low
residue lies within 64 of zero modulo the start power of two.  The expensive
part is still rare: almost every candidate is rejected by the existing square
residue cascade before exact square-root confirmation.

The hit frequency, however, falls rapidly as factor size grows.  This is why the
local-window theorem is kept as an **overhead reduction**, not promoted as an
asymptotic factoring gain.

A heuristic explanation is simple.  Conditional on a square-divisor trigger,

`z=mt+1`

is still a large integer.  Generic square spacing near z is on the order of
`sqrt(z)`, so accidental squarehood becomes sparser as N grows.  This scaling
comment is diagnostic only, not a proof of an asymptotic hit probability.

## 6. Why not enlarge D indefinitely

Explicit small-N experiments show more hits when D is enlarged, but many of the
new examples have tiny factors (31, 97, etc.) that trial division would recover
more cheaply.  Increasing D also destroys the one-residue compression regime
unless H and the start power are adjusted.

The portfolio policy is therefore:

1. use only declared (H,D) pairs for which `compressed_neighbor_distance_start_level`
   certifies exact window compression;
2. keep D modest; H=100,D=64 is the current reference pair;
3. use the largest square level as the cheapest default free option;
4. permit `all_levels=True` only when a caller explicitly wants every exact
   candidate on the unique signed neighbor;
5. after a miss, do not enlarge D automatically.

## 7. Relation to the divisor-layer idea

The original tau-layer experiment remains valuable because it suggested looking
at exponent-shape changes in nearby composites.  But the durable execution law
is now simpler:

`LOCAL TAU SHAPE`
`-> notice a square divisor`
`-> drop the tau/primality requirement`
`-> known a^2 | N±d`
`-> adaptive fixed-gap multiplier`.

The local divisor-count spectrum is still useful telemetry/provenance, but it is
not needed to run the square-divisor shortcut.

## 8. Decision

Extend, do not replace, `t0.brc_neighbor_square_lift_shortcut`:

`BOUNDED LOCAL DISTANCE WINDOW`
`-> ONE LOW-BIT RESIDUE`
`-> UNIQUE SIGNED NEIGHBOR OR EXACT EMPTY RESULT`
`-> ONE v2 CHAIN`
`-> BEYOND-HORIZON ADAPTIVE MULTIPLIER`
`-> QR FILTER / EXACT SQUARE TEST`
`-> GCD FACTOR OR ORDINARY FALLBACK`.

No Foundation/Working Truth mutation.  No factorization-complexity or RSA
practicality claim.  The exact contribution is the fixed-gap identity plus the
no-distance-scan compression of the power-of-two neighborhood.
