# Native filament longitudinal/transverse readout conic

Status: `FREE_RESEARCH_EXACT_ELIMINATION_IDENTITY / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on the split-hyperbola and lane-label Joukowski theorems.

## 1. Common carrier

For odd sector/curvature coefficient `s`, use the normalized split hyperbola

`s*a*b=-1`.

Set

`a=m`,

`b=-1/(s*m)`.

Two exact readouts live on this same point.

### Transverse lane label

`J=Lambda_s(a,b)=s*(b-2a)/2`

`=-s*a-1/(2a)`.

### Longitudinal common-dual value

For the zero-shift branch,

`P=-s*(b-a)^2/8`

`=-(s*a^2+1)^2/(8*s*a^2)`.

## 2. Parameter elimination

Eliminating `a` gives

`16*J^4 +160*s*J^2*P +8*s*J^2`

`+256*s^2*P^2 -32*s^2*P +s^2 =0`.

Equivalently, after dividing by `s^2`:

`16*(J^2/s)^2 +160*(J^2/s)*P +8*(J^2/s)`

`+256*P^2 -32*P +1=0`.

Thus the two quotient readouts are algebraically dependent before any primality condition is imposed.

## 3. Universal normalized conic

Define

`X=4*J^2/s`,

`Y=16*P`.

Then the relation becomes

`2X^2+5XY+2Y^2+4X-4Y+2=0`.

The quadratic part factors, and the full conic rewrites as

`(2X+Y-4)*(X+2Y+4)=-18`.

Freeze:

`LONGITUDINAL/TRANSVERSE READOUT PAIRS LIE ON ONE s-INDEPENDENT SPLIT CONIC`.

## 4. Exact inverse-square factors

The two affine factors have especially simple carrier meanings.

Before normalization:

`8J^2+16sP-4s = 6s^2*a^2`,

`4J^2+32sP+4s = -3/a^2`.

Their product is therefore

`-18s^2`.

So the readout conic is simply the multiplicative pairing of the square coordinate `a^2` and its inverse.

This also shows that the pair `(J^2,P)` generically recovers the square class of the original transverse parameter.

## 5. Interpretation

The same native central carrier now supports two quotient maps:

1. longitudinal K4/Dickson quotient -> dual overlap / breaker;
2. transverse Joukowski lane-label quotient -> C3/odd-sector lane divisibility.

The elimination identity shows that their outputs are not independent. They form a rational conic whose two split factors recover reciprocal carrier squares.

Hence the longitudinal and transverse arithmetic programs can be represented by one diagram:

`split-hyperbola carrier`

`-> (longitudinal P, transverse J)`

`-> universal readout conic`.

## 6. Scope guard on the constant 18

The normalized conic has right-hand side `-18`.

The native seven-Cell Poisson star also has Laplacian source `18`.

At present no presentation-invariant theorem identifies these two appearances. The normalization of `X,Y` was chosen to clear the natural denominators in the quotient formulas, so the numerical equality alone is not sufficient evidence of a common geometric source.

Freeze:

`18 COHERENCE = OBSERVED EXACT NUMERICAL COINCIDENCE / CAUSAL IDENTIFICATION NOT ESTABLISHED`.

## 7. Prior-art boundary

Parameter elimination, Joukowski/Dickson quotients and split conics are classical.

The research-specific value is the fact that the two quotient readouts selected independently by the native longitudinal and transverse constructions satisfy this exact common-carrier relation.