# Native Enterprise filament codes: finite-quotient cardinality and collapse fibers

Status: `FREE_RESEARCH_EXACT_FINITE_QUOTIENT_TOWER / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_FILAMENT_CHIRAL_DOUBLE_COVER_ACCESS_STRUCTURE_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_INTEGER_ARITHMETIC_GLUE_TWO_PROBE_DECODER_20260824.md`;
- `NATIVE_ENTERPRISE_PRIME_INCIDENCE_CONNECTIVITY_TOWER_D2_D19_20260823.md`.

## 1. Native value code modulo M

For `k>=3` and modulus `M>=2`, define

`C_k(M)`

as the set of length-k residue words obtained from all native integer filament trajectories

`V_j=c+3*R*j+(3*j^2+chi*epsilon_j)/2`,

where

`chi=(-1)^R`,

`j=0,...,k-1`,

and the values are reduced modulo M.

This is the finite quotient of the actual integer lift, not the larger two-sheet carrier in which chi and the slope are declared independent.

## 2. Effective shell parameter

A residue word depends on R only through

`chi=(-1)^R`

and

`b=3R mod M`.

Two integers R and R' give the same pair `(chi,b)` exactly when

`R'-R` is even

and

`M | 3*(R'-R)`.

Let

`g=gcd(3,M)`.

The exact period of the effective shell parameter is

`L_M=lcm(2,M/g)`.

For `M>2`, the pair `(chi,b)` therefore has exactly `L_M` possible values.

## 3. Injectivity from three coordinates

Suppose two effective parameter pairs with the same intercept c give the same first three coordinates.

The j=1 equality gives

`Delta b + (Delta chi)/2 = 0 mod M`.

The j=2 equality gives

`2*Delta b=0 mod M`.

Doubling the first equation and subtracting the second gives

`Delta chi=0 mod M`.

Since `Delta chi` is `0` or `+-2`, for `M>2` this forces equal chirality, and then the j=1 equation forces equal slope.

Thus `(c,chi,b)` is recovered from a length-three word for every `M>2`.

At `M=2`, the parity word becomes affine because `epsilon_j=j mod2`; the two chirality sheets collapse and only the constant word c remains.

## 4. Exact cardinality theorem

For every `k>=3`:

### Exceptional modulus 2

`|C_k(2)|=2`.

### Every modulus M>2

`|C_k(M)|=M*L_M`.

Equivalently, writing

`alpha(M)=1` if `2|M` and0 otherwise,

`beta(M)=1` if `3|M` and0 otherwise,

we have

`|C_k(M)|`

`=2*M^2 / (2^alpha(M)*3^beta(M))`.

So the two special channels act as exact quotient factors:

- presence of channel2 removes the independent two-sheet parity cover;
- presence of channel3 removes the threefold slope redundancy;
- no other prime changes the two-parameter degree of freedom.

The count is independent of k once `k>=3`; increasing k raises redundancy/distance but not the number of native trajectories modulo M.

## 5. Ambient density / code codimension

The ambient residue space has `M^k` words.

For `M>2`, the exact native-code density is

`2 / (2^alpha(M)*3^beta(M)) * M^(2-k)`.

In particular, when `6|M`,

`|C_k(M)|=M^2/3`,

and

`density(C_k(M))=1/(3*M^(k-2))`.

Thus the code has exact finite-quotient codimension `k-2`.

For the sharp nine-Cell packet the density is

`1/(3*M^7)`.

## 6. Reduction maps and uniform fibers

If `M|N`, reduction modulo M gives a surjection

`C_k(N) -> C_k(M)`.

For moduli above the exceptional M=2 collapse, the parameter description makes the fibers uniform.

### Adding a generic prime channel q>3

If `q` is a new prime not dividing M and `M>2`, then

`|C_k(Mq)|/|C_k(M)|=q^2`.

One factor q comes from lifting the intercept c and one from lifting the effective shell parameter.

### Adding channel2

When starting from an odd modulus, the naive q^2 factor4 is reduced to2 because parity and slope become correlated by the integer lift.

### Adding channel3

When starting from a modulus not divisible by3, the naive factor9 is reduced to3 because the slope is constrained to `3R`.

These are the code-cardinality shadows of the two small-channel glue laws.

## 7. Primorial collapse tower

Let

`P_d=product_{i=1}^d p_i`

for the first d primes.

Then

- `|C_k(P_1)|=|C_k(2)|=2`;
- for every `d>=2`, since `6|P_d`,
  `|C_k(P_d)|=P_d^2/3`.

The first projection

`C_k(6)->C_k(2)`

has uniform fiber size6.

For every `d>=3`, the downward map

`C_k(P_d)->C_k(P_(d-1))`

has uniform fiber size

`p_d^2`.

Hence after the exceptional 2/3 base, each new collapse-channel dimension contributes exactly two finite-field degrees of lift.

At d=19,

`P_19=7858321551080267055879090`,

so

`|C_k(P_19)|=20584405866724191423702130398265558985510899742700`

for every `k=3,...,9`.

For k=9 this set occupies only about `10^-174.7444` of the full `P_19^9` residue-word space.

## 8. Relation to survivor basins

`C_k(M)` classifies every geometry-admissible native value packet modulo M.

The all-unit / prime-eligible basin studied in the affine-MDS local-count notes is a further subset obtained by deleting every word with a zero coordinate in each prime channel.

Thus there are two distinct thinning stages:

1. native curvature/incidence code:
   ambient `M^k -> C_k(M)` with exact power `M^(2-k)`;
2. arithmetic all-unit sieve inside the code:
   additional logarithmic/local-product thinning.

## 9. Boundary

Finite quotient codes and CRT are classical.  The research-specific result is the exact cardinality selected by the native integer locks `chi=(-1)^R` and `b=3R`, together with the exceptional roles of channels2 and3 in the collapse tower.
