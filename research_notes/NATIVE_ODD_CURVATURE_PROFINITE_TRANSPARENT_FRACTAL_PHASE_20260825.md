# Odd-curvature filament: profinite transparent-fractal phase theorem

Status: `FREE_RESEARCH_EXACT_PROFINITE_PHASE + CLASSICAL_DIMENSION_METHOD / EXTERNAL_NOVELTY_UNRESOLVED / NOT_CANONICAL_ENTERPRISE_GEOMETRY`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on `NATIVE_ODD_CURVATURE_TRANSPARENT_BASIN_PRODUCT_AND_ASYMPTOTIC_PHASE_20260825.md`.

Only `B=3` is the current native Enterprise tri-sector specialization. Other odd B are controlled deformation families.

## 1. Squarefree profinite collapse carrier

Let

`P_d=product_(i=1)^d p_i`

be the first-d-prime primorial.

The inverse system under reduction defines the squarefree prime-channel carrier

`S = inverse_limit_d Z/P_d Z`.

By CRT,

`S ~= product_p F_p`.

This is the natural infinite collapse-channel completion for the present model, because each prime channel is represented once. It is deliberately not identified with the full profinite integer ring, which also contains prime-power precision directions.

Equip S with the primorial ultrametric:

if x!=y and d(x,y) is the largest d such that x and y agree modulo P_d, set

`dist(x,y)=P_d^(-1)`

(up to the harmless convention at d=0).

A level-d cylinder has diameter `P_d^(-1)`, and there are exactly P_d ambient cylinders.

Therefore the ambient Hausdorff dimension in this metric is1.

## 2. Infinite transparent set

For each prime p, let

`T_B(p) subset F_p`

be the full-filament transparent transverse classes, with cardinality

`tau_B(p)`.

Define

`Tcal_B = product_p T_B(p) subset S`.

Equivalently, Tcal_B is the inverse limit of the finite transparent basins

`T_B(P_d)`.

At level d, the number of cylinders meeting Tcal_B is exactly

`Theta_B(P_d)=product_(i<=d) tau_B(p_i)`.

## 3. Extinction phase

If B has any universal breaker prime q, then

`T_B(q)=empty`.

Hence

`Tcal_B=empty`.

For the native coefficient B=3, q=5 is the first breaker, so the inverse-limit transparent set is empty already after the third collapse channel.

## 4. No-breaker phase: nonempty compact Cantor-type set

For

`B=15,39,51 mod60`,

every local factor `tau_B(p)` is positive.

Thus every finite cylinder system is nonempty and compatible, so

`Tcal_B != empty`.

Moreover `tau_B(p)>1` for all sufficiently large p, so infinitely many coordinates admit at least two choices. Therefore Tcal_B has no isolated points and has cardinality continuum:

`|Tcal_B|=2^(aleph_0)`.

It is a closed compact totally disconnected product set.

## 5. Haar measure is zero

Let mu be the product Haar probability measure on

`S=product_p F_p`.

The level-d transparent density is

`mu_d=Theta_B(P_d)/P_d`.

The exact asymptotic theorem gives

`mu_d ~ C_B * 4^(-d)/(log p_d)^3`.

Hence

`mu(Tcal_B)=lim_d mu_d=0`.

So every no-breaker infinite transparent set is Haar-null.

## 6. Full Hausdorff dimension

The same asymptotic gives

`log Theta_B(P_d)`

`= log P_d - d log4 -3 log log p_d + O(1)`.

By the prime number theorem,

`log P_d ~ p_d ~ d log d`.

Therefore

`log Theta_B(P_d)/log P_d -> 1`.

This cylinder ratio gives the upper box dimension1.

For the Hausdorff lower bound, place the uniform product probability measure nu on Tcal_B. Every level-d allowed cylinder has mass

`1/Theta_B(P_d)`.

Fix any `s<1`. Since the logarithmic ratio above tends to1, for all sufficiently large d,

`Theta_B(P_d) >= P_d^s`.

Hence every sufficiently small cylinder/ball satisfies

`nu(ball) <= diameter(ball)^s`.

The mass-distribution/Frostman argument gives

`dim_H(Tcal_B)>=s`.

Letting `s->1` and using the ambient upper bound yields

`dim_H(Tcal_B)=1`.

Thus

`mu(Tcal_B)=0` but `dim_H(Tcal_B)=dim_H(S)=1`.

Freeze:

`NO-BREAKER TRANSPARENT SET = HAAR-NULL + FULL-DIMENSION + UNCOUNTABLE`.

## 7. Entropy-loss law

Define the information loss after d prime channels by

`Loss_B(d)=log_2(P_d/Theta_B(P_d))`.

The basin-density asymptotic yields

`Loss_B(d)`

`= 2d + 3 log_2 log p_d - log_2 C_B + o(1)`.

So every generic new prime channel removes asymptotically two bits of transverse entropy.

But the ambient information is

`log_2 P_d ~ d log_2 d`.

Therefore

`Loss_B(d)/log_2 P_d ->0`.

This is the information-theoretic reason the set can have measure zero while retaining full Hausdorff dimension: the absolute loss is linear in channel number, whereas the ambient information per channel grows like log d.

## 8. Infinite-dimensional phase dichotomy

The odd-curvature family has a sharp topological/measure phase split.

### Extinction

A breaker channel appears at dimension1,2 or3, and the infinite transparent set is empty.

### Sparse full-dimension survival

No breaker exists; then the infinite transparent set is

- nonempty;
- uncountable;
- compact and totally disconnected;
- Haar measure zero;
- full Hausdorff dimension1 in the primorial ultrametric.

Thus the finite-dimensional `EXTINCTION vs SPARSE-EXPANDING` dichotomy lifts to

`EMPTY vs HAAR-NULL FULL-DIMENSION FRACTAL`

on the infinite squarefree collapse carrier.

## 9. Native specialization

The actual tri-sector coefficient is B=3, so the native model lies on the extinction side:

`B=3 -> breaker5 -> d_*=3 -> Tcal_3=empty`.

The no-breaker odd-sector comparator classes `15,39,51 mod60` lie on the full-dimension null-measure side.

This comparison gives a controlled way to say that the native tri-sector allocation is not merely sparse in high dimension: its full-filament transparent state space is annihilated at finite collapse depth.

## 10. Boundary

Product Cantor constructions, Haar measure on profinite groups, ultrametric Hausdorff dimension, and Frostman/mass-distribution arguments are classical.

No novelty claim is made for those general tools.

The research-specific candidate is the exact coupling

`sector/curvature breaker phase`

`-> finite transparent-basin product`

`-> infinite squarefree profinite survivor set`

`-> extinction versus Haar-null/full-dimension phase`.

External novelty remains unresolved pending independent statement-level literature audit.