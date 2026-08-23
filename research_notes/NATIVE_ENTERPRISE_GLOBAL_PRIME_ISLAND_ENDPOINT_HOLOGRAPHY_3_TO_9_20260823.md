# Native Enterprise global prime-incidence islands: endpoint holography for the full size spectrum 3 through 9

Status: `FREE_RESEARCH_EXACT_BOUNDARY_DECODING_CLASSIFICATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_GLOBAL_PRIME_INCIDENCE_TIGHT_PATH_ISLAND_SPECTRUM_3_TO_9_20260823.md`;
- `NATIVE_ENTERPRISE_TRIPLE_PRIME_INCIDENCE_SELF_LOCALIZATION_20260823.md`;
- `NATIVE_ENTERPRISE_SHARP_NINE_ENDPOINT_HOLOGRAPHY_AND_DUAL_TANGENT_SIEVE_20260823.md`.

## 1. Goal

Every nonempty global prime-incidence component in the frozen typed-Cell allocation is a 3-uniform tight path of size

`k in {3,4,5,6,7,8,9}`.

This note asks whether the two boundary prime values of the component determine the missing interior prime values and native location.

Answer:

`YES`, with three geometric decoder classes.

## 2. Size 3: one elementary incidence triangle

Let the ordered prime values be

`p0 < p1 < p2`, all greater than 3.

For either elementary orientation,

`p2-p0 = 6r+4+2sigma`.

Set

`u=(p2-p0-4)/2`.

Then

`sigma=u mod 3`,

`r=(u-sigma)/3`.

The two orientation candidates for the middle label are

`p0+u` and `p0+u+1`.

They are consecutive. Since the actual middle value is a prime greater than 3, it must be the unique odd candidate.

Equivalently:

- if `u` is even, the triangle is A-type and `p1=p0+u`;
- if `u` is odd, the triangle is B-type and `p1=p0+u+1`.

Thus the two endpoint primes reconstruct the middle prime, orientation, shell and C3 slot. The side coordinate follows from the first label and the shell-base formula.

## 3. Size 4: two adjacent incidence triangles

Let

`p0 < p1 < p2 < p3`

be a fully-prime 4-Cell tight path. The two adjacent triangle curvatures are 2 and 4 in opposite order, hence

`p3-p2-p1+p0=6`.

Set

`D=p3-p0`.

The first triangle curvature `K0=p0-2p1+p2` is determined by the endpoint residue:

- `D == 1 mod 3` implies `K0=4`;
- `D == 2 mod 3` implies `K0=2`.

No valid fully-prime 4-path has `D==0 mod3`.

Since

`p1+p2=p0+p3-6`,

we obtain

`p1=(2*p0+p3-6-K0)/3`,

`p2=p0+p3-6-p1`.

The first reconstructed triple `(p0,p1,p2)` then feeds the exact triple-incidence localizer to recover `(r,t,sigma)`.

Therefore a 4-Cell prime diamond/tight path is also determined by its two endpoint prime values.

## 4. Sizes 5 through 9: constant-h filament decoder

Every global component of size at least 5 lies on the unique long constant-h filament species.

Let

`p_i=C_{R+i}(h)`, `i=0,...,d`,

where

`d=k-1`.

The prime-free filament potential is

`C_r(h)=h+3*r^2/2+1+(1-(-1)^r)/4`.

Let

`D=p_d-p_0`.

### Odd k (even d)

The two endpoints have the same parity correction, so

`D=3*d*(R+d/2)`.

Hence the integer central shell is

`M=D/(3*d)`.

Let

`J=d/2`, `chi=(-1)^M`.

The endpoint curvature is

`K_J=3*J^2 + chi*1_{J odd}`.

Thus the central Cell value is

`c=(p_0+p_d-K_J)/2`,

and

`h=c-3*M^2/2-1-(1-chi)/4`.

Finally `R=M-J`, and every interior value is regenerated from `C_{R+i}(h)`.

### Even k (odd d)

Now the parity correction flips. With `chi_R=(-1)^R`,

`2D = 3*d*(2R+d)+chi_R`.

Therefore

`2D mod (3d)`

is exactly `+1` or `-1`, which recovers `chi_R`.

Then

`R = (((2D-chi_R)/(3d))-d)/2`,

and

`h=p_0-C_R(0)`.

Again all interior values are regenerated exactly.

## 5. Replay on the frozen prime-island spectrum

The existing explicit witnesses decode as follows:

- k=3: `37,53,73` -> exact middle value and local incidence coordinates;
- k=4: `17,29,43,61` -> exact two interior values;
- k=5: start shell `50`, `h=16`;
- k=6: start shell `206`, `h=-44`;
- k=7: start shell `492`, `h=172`;
- k=8: start shell `956`, `h=-434`;
- k=9: start shell `10686`, `h=-2474`.

Every reconstructed packet is exactly the frozen prime witness.

## 6. Unified classification

Thus for every allowed nonempty global prime-incidence island size

`3 <= k <= 9`,

the two boundary prime values, together with the known component size k, determine the whole island.

Freeze:

`GLOBAL PRIME-INCIDENCE ISLANDS ARE TWO-BOUNDARY SELF-LOCALIZING`.

This does not mean arbitrary prime sets have a two-point reconstruction law. It is a consequence of the native typed incidence geometry plus the frozen integer allocation, specialized to prime-realized tight paths.

## 7. Information hierarchy

The result gives a concise value-level hierarchy:

`BOUNDARY PRIME PAIR + ISLAND SIZE`

`-> LOCAL GEOMETRY TYPE`

`-> NATIVE SHELL/POSITION PARAMETERS`

`-> ALL INTERIOR INTEGER LABELS`

`-> PRIME ISLAND REALIZATION`.

For k>=5 this is the boundary form of the parity-corrected quadratic filament law; for k=3,4 it follows directly from the primitive incidence curvatures 2/4.

## 8. Boundary

The decoding formulas are exact for the frozen Enterprise typed-Cell allocation. They are not an external novelty claim about classical prime constellations independently of this coordinate system.
