# Enterprise ECC Stage 0 — Hessian Kummer / Montgomery bridge closure

Status: `FREE_RESEARCH / PHASE_B / STAGE0_CLOSURE`
Date: `2026-08-23`
Researcher-ID: `EM-FREE-ACE4FF`

## Question

Does the three-axis Hessian route produce a genuinely new or faster ECC scalar-multiplication primitive, especially through the quotient coordinate `s=x+y`?

## Exact Hessian Kummer coordinate

For

`H_d: x^3+y^3+1=3dxy`, `d^3 != 1`,

Hessian negation swaps coordinates:

`-(x,y)=(y,x)`.

Therefore

`s(P)=x(P)+y(P)`

is invariant under `P -> -P` and is a coordinate on the Kummer quotient.

The Hessian-to-short-Weierstrass map has

`u = 12(d^3-1)/(d+s) - 9d^2`,

so `s` and ordinary Weierstrass `x` are related by a Mobius transform.

The one-coordinate doubling law is

`s(2P)=-(s^4+4s+3d)/(2s^3+3ds^2-1)`.

## Exact Montgomery-convertibility criterion

Assume field characteristic is not 2 or 3 and the Hessian is nonsingular.

A nontrivial rational 2-torsion point is fixed by negation, hence has affine form `(t,t)`. Substitution gives

`2t^3+1=3dt^2`,

so

`d=(2t^3+1)/(3t^2)`.

For the associated short-Weierstrass curve

`v^2=u^3+a u+b`,

with

`a=-27d(d^3+8)`,

let `alpha` be the x-coordinate of the image of `(t,t)`:

`alpha=12(d^3-1)/(d+2t)-9d^2`.

The standard Montgomery conversion criterion requires

`beta^2=3 alpha^2+a`

to be a nonzero square in the base field. After imposing the Hessian 2-torsion relation, this simplifies exactly to

`beta^2 = 16 (t^3-1)^3 / t^5`

`         = [4(t^3-1)/t^2]^2 * [(t^3-1)/t]`.

Therefore:

`H_d IS MONTGOMERY-CONVERTIBLE OVER THE BASE FIELD`

iff there exists `t` such that

1. `2t^3+1=3dt^2`, and
2. `(t^3-1)/t` is a nonzero square,

with `d^3 != 1`.

## Exact s-to-Montgomery Kummer bridge

Choose `beta` with `beta^2=3alpha^2+a`. One valid Montgomery model is

`B Y^2 = X^3 + A X^2 + X`,

with

`A=3 alpha / beta`,

`B=beta`.

The Hessian Kummer coordinate `s` maps to Montgomery `X` by

`X = kappa * (2t-s)/(d+s)`,

where

`kappa = 12(d^3-1)/(beta(d+2t))`.

Thus, on the Montgomery-convertible Hessian subfamily, the `s`-Kummer dynamics and Montgomery `x`-Kummer dynamics are conjugate by a Mobius transformation.

Consequences:

- a fast `sDBLADD` on this subfamily is not a new cryptographic group law; it is Montgomery ladder arithmetic in another quotient coordinate;
- any arithmetic advantage must be compared against the existing Montgomery `xDBLADD`, not against full Hessian projective addition;
- changing the geometric/execution representation does not change the ECDLP security assumption.

## Nonconvertible branch

If the criterion fails, `s` is still Mobius-equivalent to a generic short-Weierstrass x-coordinate, but not to a Montgomery x-coordinate over the base field.

Current EFD large-characteristic counts give approximately:

- Montgomery mixed ladder: `5M+4S`;
- generic short-Weierstrass XZ mixed ladder: `8M+7S` (plus parameter multiplications).

Therefore the generic non-Montgomery Hessian Kummer branch currently has no arithmetic-count advantage over choosing a Montgomery-compatible curve from the start.

## Finite checker

Committed checker:

`research_checks/ENTERPRISE_ECC_STAGE0_CHECK_20260823.py`

Pressure tests over `F_239`:

### Non-Montgomery witness

Earlier toy Hessian `d=5`:

- affine 2-torsion equation `2t^3-15t^2+1=0` has no root in `F_239`;
- group order is 249 (odd), consistent with absence of rational 2-torsion;
- the derived `s`-doubling formula checks on all 248 affine points with 0 mismatches.

### Montgomery-convertible witness

Choose `t=16`, giving `d=6`.

The checker derives:

- associated short-Weierstrass coefficients: `a=40`, `b=155` mod 239;
- image 2-torsion x-coordinate `alpha=159`;
- one square root `beta=169`;
- Montgomery model `169 Y^2 = X^3 + 140 X^2 + X`;
- Kummer bridge constant `kappa=17`;
- Hessian group order = Montgomery group order = 264.

Exhaustive bridge check:

- 263 affine Hessian points checked;
- 0 mismatches;
- 0 map poles in this finite example;
- Hessian 2-torsion `(16,16)` maps to Montgomery `X=0`.

## Stage 0 final verdict

`FULL_COORDINATE_HESSIAN_THREE_LANE_AUTOMATIC_SPEEDUP = REFUTED`.

`HESSIAN_s_KUMMER_IS_NEW_CRYPTO_DIFFICULTY = REFUTED`.

`MONTGOMERY_CONVERTIBLE_HESSIAN_s_LADDER = MONTGOMERY_LADDER_UP_TO_MOBIUS_CONJUGACY`.

`NONCONVERTIBLE_HESSIAN_s_LADDER_CURRENTLY_FASTER_THAN_MONTGOMERY = NOT_SUPPORTED`.

The surviving Enterprise-specific direction is not a new ECC group law. It is an implementation/architecture question:

`CAN THREE-POSITIVE-AXIS FIXED PLACEMENT / SCHEDULING REDUCE REAL HARDWARE COST, ENERGY, OR SIDE-CHANNEL LEAKAGE FOR AN ALREADY-STANDARD CONSTANT-TIME LADDER?`

That question requires an equal-hardware implementation benchmark rather than more algebraic reparameterization.
