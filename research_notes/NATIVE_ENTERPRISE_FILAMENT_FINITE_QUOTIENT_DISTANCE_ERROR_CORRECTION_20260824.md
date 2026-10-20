# Native Enterprise filament codes: finite-quotient distance and error correction

Status: `FREE_RESEARCH_EXACT_DISTANCE_THEOREM / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_FILAMENT_FINITE_QUOTIENT_MULTIPROBE_GCD_ACCESS_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_FINITE_QUOTIENT_CODE_CARDINALITY_TOWER_20260824.md`.

## 1. Statement

Let

`M=6U`

and let `C_k(M)` be the native finite quotient filament code of length `k>=3`.

Then its minimum Hamming distance is exactly

`d_min(C_k(M))=floor(k/2)`.

This holds for every modulus divisible by6, not only squarefree primorial moduli.

## 2. Upper bound from one parity layer

Let

`E=ceil(k/2)`

be the number of even positions and

`O=floor(k/2)`

the number of odd positions.

Projection to all E even positions lies entirely in one parity layer.

The multiprobe fiber theorem gives fiber size at least2, so there exist two distinct codewords agreeing on every even coordinate.

They differ on at most O coordinates.  Therefore

`d_min<=O=floor(k/2)`.

The same argument can use the odd layer, but the larger even layer gives the sharp upper bound.

## 3. No larger agreement set

Suppose two distinct codewords agree on a coordinate set S with

`|S|>E`.

Then S must meet both parity classes.

By the multiprobe theorem, a mixed-parity projection can fail to be injective only when

`gcd(g(S),U)>1`.

Let q be a prime divisor of this gcd.  Since S is mixed parity, its step gcd is odd, so q is odd and at least3.

All positions of S lie in one residue class modulo q.  Inside k consecutive indices, such a class contains at most

`ceil(k/q)<=ceil(k/3)<=E`

positions.

This contradicts `|S|>E`.

Hence no two distinct codewords agree on more than E coordinates.

Therefore their distance is at least

`k-E=O`.

Combining the bounds gives

`d_min=O=floor(k/2)`.

## 4. Distance table for the global island spectrum

| island/code length k | minimum distance |
|---:|---:|
| 3 | 1 |
| 4 | 2 |
| 5 | 2 |
| 6 | 3 |
| 7 | 3 |
| 8 | 4 |
| 9 | 4 |

The distance is independent of collapse dimension once the modulus contains channels2 and3.

## 5. Error and erasure consequences

A code of distance delta:

- detects up to `delta-1` arbitrary coordinate errors;
- uniquely corrects up to `floor((delta-1)/2)` arbitrary coordinate errors;
- uniquely reconstructs under any `delta-1` erasures.

For the sharp nine-Cell code, `delta=4`, so it

- detects3 residue errors;
- corrects1 arbitrary residue error;
- tolerates3 arbitrary erasures.

The worst-case erasure bound is conservative.  The exact access law shows that many much smaller surviving sets already reconstruct the word when they bridge parity and have good step gcd.

## 6. Dimension/access interpretation

Adding prime channels changes which particular two-probe baselines are information sets, but it does not change the global minimum distance.

The reason is structural:

- the permanent largest ambiguous observation is one full parity layer;
- every bad mixed-period sublattice is sparser than a parity layer;
- later channels only create aliases on those sparser sublattices.

Thus the high-dimensional collapse tower refines the access geometry without degrading the sharp worst-case distance.

## 7. Relation to the good-odd-field double cover

Over a sufficiently large odd field, the two-sheet union also has distance `floor(k/2)`.

The finite quotient theorem shows that restoring the small-channel integer locks changes the code cardinality and two-probe access spectrum but preserves this distance.

So the chiral parity split is the persistent extremal error pattern at every level.

## 8. Boundary

Hamming distance and error-correction bounds are classical.  The research-specific result is that the native alternating-curvature code has an exact dimension-independent distance across the entire 2-to-19 primorial collapse tower.
