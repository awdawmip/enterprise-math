# Native Enterprise global prime-incidence islands: affine MDS code spectrum 3 through 9

Status: `FREE_RESEARCH_EXACT_GLOBAL_CODE_UNIFICATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_GLOBAL_PRIME_INCIDENCE_TIGHT_PATH_ISLAND_SPECTRUM_3_TO_9_20260823.md`;
- `NATIVE_ENTERPRISE_GLOBAL_PRIME_ISLAND_ENDPOINT_HOLOGRAPHY_3_TO_9_20260823.md`;
- `NATIVE_ENTERPRISE_FILAMENT_CURVATURE_FLATTENED_AFFINE_MDS_CODE_20260824.md`.

## 1. Two universal curvature modes

For every allowed global island size

`k in {3,4,5,6,7,8,9}`,

write its ordered Cell values as

`V_0,...,V_{k-1}`.

There are exactly two local curvature modes, encoded by

`chi in {+1,-1}`,

with second differences

`V_j-2*V_{j+1}+V_{j+2}=3-chi*(-1)^j`.

For `k=3`, these are the primitive triangle curvatures 2 and4.

For `k=4`, they are the two possible curvature words `(2,4)` and `(4,2)`.

For `k>=5`, they are the two parity chiralities of the long constant-h filament.

Thus the short triangle/diamond packets and the long filament packets are restrictions of one common alternating-curvature law.

## 2. Unified affine-code formula

For an odd prime

`q>max(3,k-1)`, define

`eta_j^chi=(3*j^2+chi*epsilon_j)/2`,

where `epsilon_j` is the odd-index indicator.

Every valid island residue packet in curvature mode chi has the form

`V_j=a+b*j+eta_j^chi`.

Conversely, varying the native shell/location parameters makes `(a,b)` range over `F_q^2` inside the corresponding geometric mode.

Therefore for every size 3 through9:

`C_k,q^chi = eta^chi + RS_q(k,2)`.

The entire global value-packet spectrum is a union of two affine Reed-Solomon cosets.

## 3. Fixed-mode distance

Inside one mode, the difference of two packets is a nonzero affine function of j and has at most one zero.

Hence

`d_min(C_k,q^chi)=k-1`.

Every fixed-mode island packet is an affine MDS word, and every pair of coordinate positions is an information set.

This single statement explains:

- two-endpoint recovery of one triangle;
- two-endpoint recovery of the 4-Cell diamond;
- two-endpoint recovery of every long island size5 through9.

## 4. Two-mode union distance

The two mode offsets differ by the parity word `epsilon_j`.

The maximum number of zeros of

`a+b*j+epsilon_j`

is `ceil(k/2)`. Therefore the distance between the two affine cosets is

`floor(k/2)`.

The complete two-mode code has:

| island size k | fixed-mode distance | two-mode union distance |
|---:|---:|---:|
| 3 | 2 | 1 |
| 4 | 3 | 2 |
| 5 | 4 | 2 |
| 6 | 5 | 3 |
| 7 | 6 | 3 |
| 8 | 7 | 4 |
| 9 | 8 | 4 |

Thus longer native islands become increasingly rigid inside a known curvature mode, while forgetting the mode retains exactly one parity-derived ambiguity family.

## 5. Puncturing hierarchy

Deleting an endpoint maps each mode by puncturing:

`C_k,q^chi -> C_{k-1,q}^chi`.

Therefore the complete size spectrum

`9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3`

is one affine-MDS puncturing tower.

At the geometry level, maximality and seam conditions decide which punctured packets occur as standalone connected components; at the value-code level, the same two-parameter packet law persists throughout.

## 6. Generic local weight spectrum

For k=3, every odd q>=5 is generic.

For k=4, q=5 is the only post-3 exceptional channel; every q>=7 is generic.

For k=5 through9, the exact cutoff staircase already classifies the finite exceptional support.

At every generic q, the local packet has at most two q-divisible coordinates and the exact nonzero-weight spectrum is

- weight k:
  `q^2-kq+C(k,2)`;
- weight k-1:
  `k*(q-k+1)`;
- weight k-2:
  `C(k,2)`.

Thus the whole global island spectrum shares one three-level generic local brightness law.

## 7. Unified interpretation

The strongest value-level organization currently found is

`PRIMITIVE TRIPLE-CELL CURVATURE 2/4`

`-> TWO ALTERNATING CURVATURE MODES`

`-> TWO AFFINE RS(2) COSETS`

`-> GLOBAL ISLAND SIZE PUNCTURING TOWER 3..9`

`-> ENDPOINT HOLOGRAPHY AS MDS INFORMATION RECOVERY`

`-> FINITE EXCEPTIONAL-PRIME SINGULARITIES`.

The code structure is prime-free; primality selects all-unit realizations of these exact geometry-generated words. The observed event frequencies remain compatible with classical singular-series statistics.
