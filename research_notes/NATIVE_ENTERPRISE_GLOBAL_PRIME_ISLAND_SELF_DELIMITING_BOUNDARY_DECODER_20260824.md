# Native Enterprise global prime islands: self-delimiting boundary decoder

Status: `FREE_RESEARCH_EXACT_BOUNDARY_SELF_DELIMITATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_GLOBAL_PRIME_INCIDENCE_TIGHT_PATH_ISLAND_SPECTRUM_3_TO_9_20260823.md`;
- `NATIVE_ENTERPRISE_GLOBAL_PRIME_ISLAND_ENDPOINT_HOLOGRAPHY_3_TO_9_20260823.md`;
- `NATIVE_ENTERPRISE_TYPED_CELL_LIFT_OF_TRI_SECTOR_ALLOCATION_20260823.md`;
- `NATIVE_ENTERPRISE_FILAMENT_INTEGER_ARITHMETIC_GLUE_TWO_PROBE_DECODER_20260824.md`.

## 1. Previous decoder and the missing input

The previous endpoint-holography theorem proved:

`BOUNDARY PRIME PAIR + ISLAND SIZE k`

`-> COMPLETE ISLAND + NATIVE LOCATION`.

This note removes the supplied size k.

Assume only that

`p_min < p_max`

are the two boundary Cell labels of one nonempty global prime-incidence component in the frozen typed allocation.

## 2. One integer label already localizes one Cell

For typed shell s define

`B_s^C=1+3*s*(s+1)/2`.

Shell s contains exactly the consecutive block

`B_s^C <= n < B_(s+1)^C`,

of length `3*(s+1)`.

Given any positive integer n, find the unique s with this inequality and set

`j=n-B_s^C`,

`sigma=floor(j/(s+1))`,

`t=j mod (s+1)`.

Thus one boundary value `p_min` recovers its exact typed Cell coordinate `(s,t,sigma)` before primality is used.

## 3. No-branching makes the forward path deterministic

The global prime-incidence classification proved that every nonempty component is a 3-uniform tight path and that no typed Cell has two admissible forward branch directions inside one component.

The local mod-6 incidence type and the typed coordinate of the lower endpoint determine the unique eligible forward tight-path trajectory:

- short sigma0/sigma2 packets terminate by size4;
- long sigma1 packets follow one constant-h shell filament;
- typed-sector seams admit no prime-incidence bridge.

Therefore, after localizing `p_min`, there is at most one ordered carrier path on which a component with that lower boundary can lie.

## 4. Strict label monotonicity

Along every admissible forward path, Cell labels strictly increase.

For the long sigma1 filament the exact potential is

`C_r(h)=h+3*r^2/2+1+(1-(-1)^r)/4`.

Its consecutive gaps are

- `C_(r+1)-C_r=3r+2` for even r;
- `C_(r+1)-C_r=3r+1` for odd r.

Both are positive.

The short triangle/diamond dictionaries likewise have positive gaps, explicitly given by the primitive incidence formulas.

Hence a fixed forward path can hit the numeric endpoint `p_max` at most once.

## 5. Self-delimiting decoder

The complete decoder is:

1. invert `p_min` to its typed Cell coordinate;
2. select the unique eligible forward tight-path trajectory from the local incidence dictionary;
3. generate its strictly increasing Cell labels;
4. stop at the unique label equal to `p_max`;
5. the number of generated Cells is the island size k;
6. all generated intermediate labels are the reconstructed interior prime values.

The global sharp-nine theorem guarantees termination after at most nine Cells for an actual component.

Thus

`BOUNDARY PRIME PAIR`

`-> ISLAND SIZE`

`-> COMPLETE PRIME PACKET`

`-> NATIVE LOCATION`.

Freeze:

`GLOBAL PRIME-INCIDENCE ISLANDS ARE SELF-DELIMITING FROM THEIR TWO BOUNDARY VALUES`.

## 6. Closed long-filament span decoder

For a long packet beginning at shell R, let

`d=k-1`

and

`chi=(-1)^R`.

Its endpoint span is

`S_R(d)=3*R*d+(3*d^2+chi*epsilon_d)/2`.

The increment is

`S_R(d+1)-S_R(d)=3R+eta_(d+1)^chi-eta_d^chi>0`.

Therefore, once `p_min` has supplied R through the inverse typed coordinate,

`p_max-p_min=S_R(d)`

has at most one nonnegative integer solution d.

This gives a closed arithmetic version of the monotone path decoder for every long island.

## 7. Relation to the arbitrary-two-probe theorem

The universal two-probe filament decoder assumes the probe positions i,j are known and reconstructs the infinite value trajectory.

The self-delimiting boundary decoder solves the complementary problem:

- the probes are known to be component boundaries;
- their separation `d=k-1` is not supplied;
- the inverse allocation localizes the first probe;
- strict path monotonicity recovers d.

Together they show that the frozen prime islands carry both

`POSITION-KNOWN TWO-PROBE HOLOGRAPHY`

and

`BOUNDARY-KNOWN SELF-DELIMITATION`.

## 8. Explicit spectrum replay

The frozen witnesses decode to the unique sizes

- `(37,73) -> k=3`;
- `(17,61) -> k=4`;
- `(3767,4391) -> k=5`;
- `(63611,66739) -> k=6`;
- `(363269,372179) -> k=7`;
- `(1370471,1390621) -> k=8`;
- `(171283421,171539981) -> k=9`.

No island-size input is used.

## 9. Boundary

The result is exact for the frozen typed Enterprise allocation and its no-branching prime-incidence graph.  It does not say that arbitrary classical prime sets are reconstructible from two extrema.
