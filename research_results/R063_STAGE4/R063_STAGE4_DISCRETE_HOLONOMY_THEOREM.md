# R063 Stage 4 — Discrete Holonomy Theorem

Status: `PROVED`

## Pure-translation theorem

Let the three orientation bits be `epsilon_12,epsilon_23,epsilon_31`.

The unique minimal overlap translations preserving the native shared-axis identity are

`k_12,23 = epsilon_12 + epsilon_23 - 1`,

`k_23,31 = epsilon_23 + epsilon_31 - 1`,

`k_31,12 = epsilon_31 + epsilon_12 - 1`

in `C4`.

Therefore the loop transport is

`H = k_12,23+k_23,31+k_31,12`

`  = 2(epsilon_12+epsilon_23+epsilon_31)-3 mod 4`.

If the number of opposite-oriented sectors is even, `H=1`; if it is odd, `H=3`.

Thus:

`H in {1,3}` for all eight assignments,

and in particular

`H != 0`.

So there is no path-independent global phase trivialization.

## Stronger affine theorem

Allow an arbitrary affine automorphism on each edge,

`F_e(x)=s_e x+k_e`, `s_e in {1,3}`,

subject only to matching the declared shared-axis phase.

Modulo `2`, every slope satisfies `s_e=1`. Hence

`k_e = target_phase - s_e source_phase`

has parity equal to the sum of the source and target shared-axis phases.

Around the three-sector cycle, these six boundary phases contain exactly the pair `{0,1}` from each sector. Their total parity is

`1+1+1 = 1 mod 2`.

The translation part of the composite affine loop is therefore always odd. Consequently no allowed affine loop can be the identity map.

This proves a stronger obstruction than the pure-translation enumeration.

## Interpretation

The holonomy is a finite `C4` process-transport invariant. It is not a continuum angle, classical complex phase, or native negative direction.

The eight-case table is recorded in `R063_STAGE4_CYCLIC_TRANSITION_TABLE.json`.
