# R005 — Even-Dimension Forcing Recursion

Status: `PROVED CONDITIONAL TRANSPORT / NOT A PROOF OF LOWER-DIMENSION PRIME EXISTENCE`  
Date: `2026-08-10`

## 1. Generalized lower-dimension premise

For integer `m>=1`, define `G_m(T)` to mean: for every integer `t>=T`, there exists a prime `r` with

`t^m < r < (t+1)^m`.

Consider the `2m`-power basin

`k^(2m) < n < (k+1)^(2m)`.

For even exponent `2m`, the R005-B screening horizon is

`F_(2m)(k)=(k+1)^m-1`.

## 2. T-A11 — prime-between-m-th-powers implies full forced saturation one doubled dimension up

Assume `G_m(T)`.  For k large enough that the constructed lower interval lies beyond T, every candidate prime witness `q<=F_(2m)(k)` is forced.

### Case 1: q>k^m

Then

`k^(2m)<q^2<=F_(2m)(k)^2<(k+1)^(2m)`.

Thus `q^2` is an exclusive collision.

### Case 2: q<=k^m

Let `A=k^(2m)` and

`x=(A/q)^(1/m)=k^2/q^(1/m)`.

Choose

`t=max(k+1,floor(x)+1)`.

Then `t>x`, so `t^m>A/q`; also `t>=k+1`, so every prime above `t^m` lies above the screening horizon.

By `G_m(T)`, choose a prime

`t^m<r<(t+1)^m`.

Then `q*r>A`.

For the upper bound, if `t=k+1`,

`q^(1/m)*(t+1)<=k*(k+2)<(k+1)^2`.

If `t=floor(x)+1`, then `t+1<=x+2`, hence

`q^(1/m)*(t+1)<=k^2+2*q^(1/m)<=k^2+2k<(k+1)^2`.

Raise to the m-th power:

`q*(t+1)^m<(k+1)^(2m)`.

Therefore `q*r` lies in the 2m-basin, and since `r>F_(2m)(k)`, q is its only candidate prime divisor.  So q is forced.

Hence:

`G_m(T) -> full forced-core saturation in exponent 2m for sufficiently large k`.

The unique least safe divisor-witness basis is then the full candidate prime set.

## 3. Legendre consequence

For m=2, `G_2(1)` is Legendre's conjecture.  Therefore:

**Legendre conjecture implies full divisor-witness forcing saturation in fourth-power basins.**

For the R005 regime k>=2, the construction works basin by basin under the conjecture.

This implication is one-way.  No reverse implication and no proof of Legendre are claimed.

## 4. Dimension-recursion interpretation

R005 now has two exact cross-dimensional mechanisms:

1. `prime in m-basin -> q^r exclusive collision in mr-basin -> q forced`;
2. `universal prime existence in m-power intervals -> complete forced-core saturation in 2m-power basins`.

Thus a lower-dimensional universal prime-existence law has a precise higher-dimensional minimum-observation consequence.

## 5. Relation to Baker–Harman–Pintz

Near x=t^m, consecutive m-th powers are separated on the scale `x^(1-1/m)`.  For m>=3, this exponent is at least 2/3, larger than 0.525.  Therefore the established Baker–Harman–Pintz short-interval prime theorem implies `G_m(T)` for some sufficiently large T when m>=3.

T-A11 consequently gives asymptotic full forcing saturation for even p=2m>=6.  The direct R005-A BHP argument is stronger in exponent coverage, already giving every fixed p>=5 including odd p.  T-A11 is retained because it exposes the dimension-recursion dependency rather than because it improves the numerical threshold.

Reference: R. C. Baker, G. Harman, J. Pintz, *The Difference Between Consecutive Primes, II*, Proc. London Math. Soc. 83 (2001), 532–562, DOI `10.1112/plms/83.3.532`.

## 6. Exceptional m=1 source

`G_1(T)` is false: there is no integer strictly between t and t+1.  Hence the recursion supplies no inherited full-forcing theorem for p=2.

This matches the R005 square-basin observation: the lower-positive-integer-exponent pure-power inheritance channel is empty, and residual witness-choice hypergraphs can occur.

## 7. Status

The conditional transport theorem is elementary after assuming the lower-dimensional prime-between-powers property.  No novelty is claimed for the classical inequalities or prime-existence conjectures/theorems.

Keep owner-local until the generic WitnessCover Lean candidate is compiler-validated and the basin specialization receives formal/owner review.
