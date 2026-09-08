# BRC Neighbor-Square Lift Shortcut — N±1 Square Divisors as Adaptive Multipliers

Status: `PROVED EXACT IDENTITY / OPPORTUNISTIC BEYOND-HORIZON MULTIPLIER / FINITE RARE-HIT DIAGNOSTIC / NO COMPLEXITY CLAIM`
Date: `2026-09-08`
Parent: `t0.divisor_layer_lift_probe`, `T0_BRC multiplier-Fermat bridge`

## 1. Starting point

The divisor-layer experiment asked whether a prime or semiprime can be lifted to
the divisor-count layer of nearby composites.  For a squarefree semiprime
`N=pq`, target layer `T=2r` with r an odd prime forces the minimal lift to reuse
one source factor.

The first large-N question was whether a strong layer on `N±1` can be certified
without factoring the neighbor.  For an even integer

`M=2^e u`, u odd,

`tau(M)=(e+1)tau(u)`.

Thus `tau(M)=2r`, r odd prime, occurs exactly in one of three forms:

1. `e=r-1` and u is prime;
2. `e=1` and `u=l^(r-1)` for an odd prime l;
3. `u=1` and `e=2r-1`.

This makes the dominant even-neighbor strong layer N-visible up to one primality
certificate.  However finite tests did not show a robust routing advantage for
existing structural/learned multiplier orders.

The useful algebra appears after dropping the primality requirement entirely.

## 2. Neighbor-square identity

Let epsilon be +1 or -1 and suppose

`N=a^2 t + epsilon`,

or equivalently `a^2 | N-epsilon`.

Set

`m=2a-epsilon`.

Then exactly

`mN = a^2(mt+1) - (a-epsilon)^2`.

Proof is direct:

`mN=m(a^2t+epsilon)`
`=ma^2t + (2a-epsilon)epsilon`
`=ma^2t + 2a epsilon -1`,

while

`a^2(mt+1)-(a-epsilon)^2`
`=ma^2t+a^2-(a^2-2a epsilon+1)`
`=ma^2t+2a epsilon-1`.

Therefore if

`mt+1=c^2`,

then

`mN=(ac)^2-(a-epsilon)^2`.

This is a complete difference-of-squares witness at multiplier m.  Gcd of the
two sides with N recovers a proper factor whenever the witness splits the N
factors.

The construction is not a new factoring principle.  It is an N-dependent
specialization of multiplier-Fermat/BRC square completion with a prescribed
small gap root `|a-epsilon|`.

## 3. Why the divisor-layer idea led here

A strong squarefree target layer has shape

`M=s^(r-1) t = (s^((r-1)/2))^2 t`.

Thus every strong `2r` neighbor already exposes a square divisor a^2.  But the
identity above needs only that square divisor; the remaining quotient t need not
be prime and the neighbor need not actually have `tau=2r`.

So the durable shortcut is strictly more general than the original tau-layer
condition:

`STRONG DIVISOR LAYER -> KNOWN NEIGHBOR SQUARE DIVISOR -> ADAPTIVE MULTIPLIER`,

while the first implication is no longer required at execution time.

## 4. Power-of-two trigger

For odd N, square powers of two in `N-1` and `N+1` are especially cheap.  If

`v2(N-epsilon)=e`,

then every

`a=2^k`, `1<=k<=floor(e/2)`,

satisfies `a^2 | N-epsilon`.  No factorization or general modular division is
needed to discover these levels.

The resulting multiplier is

`m=2^(k+1)-epsilon`.

Examples include

- epsilon=+1: `m=3,7,15,31,63,127,255,511,...`;
- epsilon=-1: `m=5,9,17,33,65,129,257,513,...`.

The existing bounded multiplier program has concentrated heavily on `m<=100`.
Therefore the opportunistic policy is to ignore levels already covered by that
scan and probe only when the free v2 trigger produces `m>100` (or the caller's
current declared horizon).

Most integers do not trigger this branch.  That rarity is a feature: the miss
cost over the whole population is tiny.

## 5. Zero-false-negative prefilter

The only nonlinear test is whether

`z=mt+1`

is square.  Before paying `isqrt(z)`, the executable tool applies the existing
BALANCED quadratic-residue cascade.  A true square survives every stage, so this
cannot remove a factor witness.  Almost all opportunistic misses terminate at
small modular-table cost.

The probe therefore has three cheap stages:

1. read `v2(N±1)`;
2. construct a beyond-horizon m and z;
3. reject z through the square-residue cascade, with exact isqrt only on
   survivors.

A failure returns immediately to the ordinary complete factor pipeline.

## 6. Exact beyond-horizon witnesses

Three squarefree semiprime witnesses are retained as regression cases.

### m=127

`N=18,677,761=383*48,767`.

`N-1=64^2*4560`, so `a=64`, epsilon=+1 and `m=127`.

`127*4560+1=761^2`.

Hence

`127N=(64*761)^2-63^2`,

and gcd recovers 383 and 48,767.

### m=255

`N=1,523,713=389*3917`.

`N-1=128^2*93`, so `a=128`, `m=255`.

`255*93+1=154^2`, hence

`255N=(128*154)^2-127^2`.

### m=511

`N=6,094,849=761*8009`.

`N-1=256^2*93`, so `a=256`, `m=511`.

`511*93+1=218^2`, hence

`511N=(256*218)^2-255^2`.

These witnesses demonstrate real hits beyond the former m<=100 finite horizon.
They do not establish a useful positive density.

## 7. Finite opportunity rate

A frozen exhaustive small-number diagnostic scans odd squarefree semiprimes and
uses only the largest power-of-two square level on each side, with
`ordinary_horizon=100`.

| upper bound | odd squarefree semiprimes | beyond-100 triggers | square hits | factor hits |
|---:|---:|---:|---:|---:|
| 100,000 | 18,181 | 17 | 0 | 0 |
| 500,000 | 86,157 | 81 | 0 | 0 |
| 2,000,000 | 328,564 | 315 | 1 | 1 |

Thus the high-v2 trigger occurs at roughly the per-thousand level in this small
range, while observed factor hits are much rarer.  The correct interpretation
is not a new main algorithm.  It is a low-frequency free-option probe.

A separate 10,000-sample semiprime routing diagnostic also found that exact
strong `N±1` divisor-layer flags did not materially change the success coverage
of the existing m<=100 structural/learned scans.  The tau flag is therefore kept
as telemetry rather than a default routing switch.

## 8. RSA-270 checkpoint

For the public RSA-270 challenge integer, `N mod 8 = 7`.  Its immediate
2-adic data are

- `v2(N-1)=1`;
- `v2(N+1)=3`.

Therefore the power-of-two neighbor-square rule produces no multiplier above
100 at all.  Under the opportunistic stop policy, this branch terminates
immediately on RSA-270 and does not launch a wider search.

This is exactly the desired behavior for the portfolio: cheap signal, exact
success path, immediate stop on an ordinary miss.

## 9. Direct-gcd and natural-neighbor boundaries

If an actual neighbor is written as

`N+d=a^2 t`,

then

`gcd(N,a^2t)=gcd(N,d)`.

So for small nonzero d coprime to N, the known neighbor factors themselves are
guaranteed not to be factors of N.  The useful object is the induced multiplier
identity, not direct gcd with the neighbor's factors.

For an upper neighbor (`d>0`), the obvious large multiplier t gives

`tN=(at)^2-td`.

For d=1 its ceiling completion gap is exactly t, which is nonsquare when t is
prime.  This explains why merely discovering a strong tau neighbor does not
itself create an immediate multiplier-Fermat hit.

## 10. Decision

Register as an exact opportunistic T0_BRC subtool:

`KNOWN SQUARE DIVISOR OF N±1`
`-> m=2a-epsilon`
`-> test mt+1 for square`
`-> fixed-gap difference-of-squares witness`
`-> gcd factor or exact fallback`.

Default use should be narrow:

- power-of-two square divisor metadata is free;
- prefer multipliers beyond the caller's ordinary scan horizon;
- apply the square-residue cascade before isqrt;
- do not expand the horizon after a miss;
- if arbitrary neighbor square-factor metadata is already available from another
  task, reuse it, but do not factor N±1 merely to feed this shortcut.

No Foundation/Working Truth mutation and no factorization-complexity improvement
is claimed.
