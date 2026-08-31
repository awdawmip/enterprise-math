# Native Enterprise filament codes: finite-quotient two-probe baseline spectrum

Status: `FREE_RESEARCH_EXACT_PROJECTION_FIBER_CLASSIFICATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_FILAMENT_FINITE_QUOTIENT_CODE_CARDINALITY_TOWER_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_PROBE_CHANNEL_DUALITY_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_INTEGER_ARITHMETIC_GLUE_TWO_PROBE_DECODER_20260824.md`.

## 1. Setup

Let `M` be divisible by6 and write

`M=6U`.

For `k>=3`, the finite native filament code `C_k(M)` has

`|C_k(M)|=M^2/3`.

Fix two coordinate positions `i<j` and let their separation be

`ell=j-i`.

Consider the projection

`rho_(i,j): C_k(M) -> (Z/MZ)^2`.

This note classifies its exact uniform fiber size.

## 2. Effective shell coordinate

Since `M=6U`, the effective shell parameter R has period

`M/3=2U`.

Once the first observed value is fixed, the second observation depends on R through

`F_ell(R)`

`=3*ell*R + constant_geometry`

`+ ((-1)^R/2)*(epsilon_j-epsilon_i)`.

Two shell classes `R,R+delta` project to the same pair exactly when this difference vanishes modulo M.

## 3. Even separation

If ell is even, the two probe positions have the same parity, so

`epsilon_j-epsilon_i=0`.

The chirality term disappears.  Collision requires

`6U | 3*ell*delta`,

or

`2U | ell*delta`.

The shell domain is `Z/(2U)Z`, so the kernel has exactly

`gcd(ell,2U)`

elements.

Hence every projected pair has fiber size

`f_M(ell)=gcd(ell,2U)`

for even ell.

In particular every even separation has fiber size at least2 and is never an information set.

## 4. Odd separation

If ell is odd, the two positions have opposite parity.

A shell shift delta of odd parity flips chirality.  The resulting projection difference is

`3*ell*delta +-1`,

which is never divisible by3.  Therefore cross-parity shell classes never collide.

For an even shift write

`delta=2e`, `e mod U`.

The collision condition becomes

`U | ell*e`.

Thus every projected pair has fiber size

`f_M(ell)=gcd(ell,U)`

for odd ell.

Therefore an odd separation is an information baseline exactly when

`gcd(ell,U)=1`.

## 5. Exact theorem

For every `M=6U`, `k>=3`, and any two positions separated by ell, the projection has uniform fiber size

`f_M(ell)=`

- `gcd(ell,U)` if ell is odd;
- `gcd(ell,2U)` if ell is even.

Consequently

`rho_(i,j) is injective`

iff

`ell is odd and gcd(ell,M/6)=1`.

The criterion depends only on the baseline separation, not on the absolute probe positions or window length.

## 6. Initial primorial dimensions

For the primorial tower `P_d`:

### d=2, M=6, U=1

Every odd baseline is injective.

Within a nine-Cell window the protected separations are

`1,3,5,7`.

### d=3, M=30, U=5

The 5-baseline acquires fiber5.  Protected separations are

`1,3,7`.

### d=4, M=210, U=35

The 7-baseline also collapses.  Protected separations are

`1,3`.

### d=5 through19

Every new prime channel exceeds the maximal separation8 of a nine-Cell island, so the protected set remains

`{1,3}`.

Thus the two-probe access structure stabilizes at collapse dimension4, long before the residue-state tower reaches dimension19.

## 7. Infinite-channel protected baselines

Let ell be any fixed positive separation and send the primorial tower through all prime channels.

The condition

`gcd(ell,P_d/6)=1`

for every d means that ell has no prime divisor at least5.

Together with the required oddness, this is equivalent to

`ell=3^a`

for some integer `a>=0`.

Freeze:

`BASELINES PROTECTED THROUGH THE ENTIRE PRIME-CHANNEL TOWER`

`= POWERS OF 3`.

The factor3 is not removed from the baseline because it has already been absorbed into the native slope law `b=3R`; the quotient parameter is controlled by `M/6`, not M itself.

## 8. Uniform aliasing interpretation

If ell has a prime factor q contained in U, then every two-probe residue pair has exactly q or more compatible native trajectories, according to the full gcd above.

So collapse channels do not create irregular ambiguity.  They produce uniform covering multiplicities indexed by the arithmetic of the geometric baseline.

For example at M=210:

- ell=1 or3: fiber1;
- ell=2,4,6,8: fiber2;
- ell=5: fiber5;
- ell=7: fiber7.

## 9. Integer lift versus finite quotient

The full integer two-probe theorem recovers the trajectory from **every** distinct baseline.

The finite quotient forgets exact divisibility and allows aliases according to `f_M(ell)`.

Thus downward residue collapse has a precise information cost:

`INTEGER LEVEL: ALL BASELINES HOLOGRAPHIC`,

`PRIMORIAL FINITE LEVEL: ONLY 3-POWER BASELINES SURVIVE FOREVER`.

## 10. Boundary

Projection kernels over residue rings are classical.  The research-specific result is the exact baseline spectrum selected by the native slope factor3, parity chirality and the primorial collapse tower.
