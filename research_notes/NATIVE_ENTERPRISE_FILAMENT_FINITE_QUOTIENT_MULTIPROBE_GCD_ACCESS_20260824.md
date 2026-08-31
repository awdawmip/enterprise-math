# Native Enterprise filament codes: finite-quotient multiprobe gcd access law

Status: `FREE_RESEARCH_EXACT_MULTIPROBE_ACCESS_CLASSIFICATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_FILAMENT_FINITE_QUOTIENT_TWO_PROBE_BASELINE_SPECTRUM_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_CHIRAL_DOUBLE_COVER_ACCESS_STRUCTURE_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_FINITE_QUOTIENT_CODE_CARDINALITY_TOWER_20260824.md`.

## 1. Setup

Let

`M=6U`

and let `C_k(M)` be the native length-k finite quotient code.

Choose a probe set

`S subset {0,...,k-1}`

with at least two positions.

Define its step gcd

`g(S)=gcd{|i-j|: i,j in S}`.

Equivalently, after choosing one base position `i0 in S`,

`g(S)=gcd{|j-i0|: j in S}`.

We classify the exact uniform fiber size of the coordinate projection

`rho_S:C_k(M)->(Z/MZ)^S`.

## 2. Shell differences

The effective shell parameter is

`R mod 2U`.

Once the value at one base probe is fixed, two shell classes separated by delta give the same whole S-projection exactly when every relative probe difference is killed.

There are two cases.

## 3. Probe set contained in one parity layer

Assume every position in S has the same parity.

Then all chirality-offset differences vanish, including for odd shell shifts.  The collision equations are

`2U | delta*(j-i0)`

for every `j in S`.

The kernel size is therefore

`f_M(S)=gcd(2U,g(S))`.

Since every difference in a one-parity set is even,

`f_M(S)>=2`.

Thus no collection of probes confined to one parity layer is an information set at any modulus divisible by6.

This finite-ring statement refines the good-odd-field result that an arbitrarily large one-parity observation remains chirality-blind.

## 4. Probe set crossing the two parity layers

Assume S contains both even and odd positions.

An odd shell shift flips chirality.  On any opposite-parity probe difference the collision equation acquires an additive `+-1`, so it is not divisible by3.  Hence no odd shell shift lies in the kernel.

Write an allowed even shift as

`delta=2e`, `e mod U`.

The remaining equations are

`U | e*(j-i0)`

for every `j in S`.

Therefore

`f_M(S)=gcd(U,g(S))`.

The projection is injective exactly when

`gcd(U,g(S))=1`.

## 5. Exact multiprobe theorem

For every `M=6U`, `k>=3`, and probe set `|S|>=2`, all fibers of `rho_S` have the same size

`f_M(S)=`

- `gcd(2U,g(S))` if S lies in one parity class;
- `gcd(U,g(S))` if S meets both parity classes.

Hence

`S IS AN INFORMATION SET`

iff

`S meets both parities and gcd(g(S),M/6)=1`.

The full access structure depends only on

1. whether the probes bridge the parity split;
2. the gcd of their geometric separations.

It does not depend on the absolute starting position.

## 6. Examples

At `M=210`, `U=35`:

- `S={0,1}`: `g=1`, fiber1;
- `S={0,3,6}`: mixed parity, `g=3`, fiber1;
- `S={0,5}`: mixed parity, `g=5`, fiber5;
- `S={0,7}`: mixed parity, `g=7`, fiber7;
- `S={0,2,6}`: one parity, `g=2`, fiber2;
- `S={1,3,5,7}`: one parity, `g=2`, fiber2.

Adding more probes does not help if all added differences preserve the same bad gcd.

Conversely one extra probe that reduces the step gcd to a unit immediately collapses the entire aliasing fiber.

## 7. Primorial tower

For the primorial modulus

`P_d`, `d>=2`,

we have

`U_d=P_d/6=5*7*...*p_d`.

A mixed-parity probe set is injective at dimension d exactly when its step gcd has no prime factor among

`5,7,...,p_d`.

Thus every newly added prime channel q destroys precisely those probe geometries whose step gcd is divisible by q.

This is a sharp geometric interpretation of channel refinement:

`NEW PRIME CHANNEL q`

`-> COLLAPSE OF q-PERIODIC PROBE SUBLATTICES`.

## 8. Infinite-channel limit

A fixed finite probe set remains injective through every prime channel iff

- it meets both parity classes;
- `g(S)` has no prime factor at least5.

Because a mixed-parity set has odd step gcd, this is equivalent to

`g(S)=3^a`

for some `a>=0`.

Freeze:

`ALL-CHANNEL PROTECTED MULTIPROBE GEOMETRIES`

`= PARITY-BRIDGING SETS ON A 3^a STEP SUBLATTICE`.

The earlier protected two-probe baselines are the two-point special case.

## 9. Information repair by one probe

Suppose a mixed probe set has aliasing fiber q because `q|g(S)` for a channel q contained in U.

Adding one position whose difference from the old set is not divisible by q reduces the new gcd and removes that q-factor from the fiber.

So the theorem gives an exact repair rule:

`BREAK THE BAD PERIOD IN THE PROBE GEOMETRY`

rather than adding more probes at the same bad period.

## 10. Boundary

Kernel counts in cyclic modules are classical.  The research-specific result is the exact dependence of native filament observability on parity bridging and the geometric step gcd across the primorial collapse tower.
