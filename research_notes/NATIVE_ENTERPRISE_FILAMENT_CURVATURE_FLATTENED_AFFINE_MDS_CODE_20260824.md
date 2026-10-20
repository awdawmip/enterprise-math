# Native Enterprise filament windows: curvature-flattened affine MDS code

Status: `FREE_RESEARCH_EXACT_CODE_CLASSIFICATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_GLOBAL_PRIME_ISLAND_ENDPOINT_HOLOGRAPHY_3_TO_9_20260823.md`;
- `NATIVE_ENTERPRISE_FILAMENT_CHARACTERISTIC_MODE_DECOMPOSITION_20260823.md`;
- `NATIVE_ENTERPRISE_FILAMENT_DUAL_TANGENT_EXCEPTION_CUTOFF_STAIRCASE_20260823.md`.

## 1. Long-filament window

For a constant-`h` typed filament, fix a start shell and its parity chirality

`chi in {+1,-1}`.

For a window of length `k`, indexed by

`j=0,1,...,k-1`,

the integer values have the exact form

`V_j = c + 3*R*j + (3*j^2 + chi*epsilon_j)/2`,

where

`epsilon_j=0` for even `j` and `epsilon_j=1` for odd `j`.

The global prime-incidence classification restricts realized long prime islands to

`k in {5,6,7,8,9}`.

## 2. Curvature flattening over a finite field

Fix an odd prime `q>max(3,k-1)`. Define

`eta_j^chi=(3*j^2+chi*epsilon_j)/2 in F_q`.

Subtract the geometry-forced curvature packet:

`W_j=V_j-eta_j^chi`.

Then

`W_j=a+b*j`,

with

`a=c mod q`,

`b=3R mod q`.

Since 3 is invertible modulo q, `(a,b)` runs over all of `F_q^2`.

Therefore the fixed-chirality residue family is exactly

`C_k,q^chi = eta^chi + RS_q(k,2)`,

where

`RS_q(k,2)={(a+b*j)_{j=0}^{k-1}: a,b in F_q}`.

Thus each chirality packet is an affine coset of the length-k, dimension-2 Reed-Solomon evaluation code.

No claim is made that Reed-Solomon theory itself is new. The research-specific result is that it is selected automatically by the native curvature flattening.

## 3. MDS distance and endpoint holography

The difference of two words in the same chirality coset is a nonzero affine function of `j`.

Because the evaluation points `0,...,k-1` are distinct modulo q, such a function has at most one zero.

Hence

`minimum Hamming distance(C_k,q^chi)=k-1`.

So each fixed-chirality family is an affine MDS code.

Any two distinct coordinate positions are an information set. In particular, the two endpoint residues determine `(a,b)` and therefore all interior residues.

This gives the finite-field coding explanation of the exact integer endpoint-holography formulas already proved for the prime islands.

## 4. Curvature syndrome

The unflattened words obey

`V_j-2*V_{j+1}+V_{j+2}=3-chi*(-1)^j`.

Thus the two chiral packets have the alternating second-difference syndromes

- `chi=+1`: `2,4,2,4,...`;
- `chi=-1`: `4,2,4,2,...`.

After subtracting `eta^chi`, every syndrome vanishes:

`W_j-2*W_{j+1}+W_{j+2}=0`.

Therefore the primitive incidence curvature code and the endpoint reconstruction law are two readouts of the same affine-code structure.

## 5. The two-chirality union

The offset difference is

`eta^+ - eta^- = epsilon`,

where `epsilon` is the parity indicator word.

For `k>=3`, this word is not affine in `j`, so the two chirality cosets are disjoint.

For `k=5,...,9`, the minimum distance between opposite chirality cosets is

`floor(k/2)`.

Proof: a cross-coset difference has the form

`a+b*j+epsilon_j`.

If `b!=0`, it has at most one zero on the even indices and at most one zero on the odd indices. If `b=0`, choosing `a=0` kills every even position and choosing `a=-1` kills every odd position. Therefore the maximum possible zero count is `ceil(k/2)`, and the minimum cross distance is `k-ceil(k/2)=floor(k/2)`.

Hence the two-chirality union has

- size `2*q^2`;
- fixed-chirality distance `k-1`;
- global union distance `floor(k/2)`.

## 6. Puncturing / downward island collapse

Deleting an endpoint coordinate maps

`C_k,q^chi -> C_{k-1,q}^chi`

by the same affine parameters `(a,b)`.

Thus the realized long-island size hierarchy

`9 -> 8 -> 7 -> 6 -> 5`

is a puncturing tower of curvature-flattened affine MDS cosets.

This is value-level downward collapse, not a Euclidean coordinate projection.

## 7. Generic local weight spectrum

The condition that coordinate `j` vanishes modulo q is one affine line in the parameter plane `(a,b)`.

Let `Q_k` be the exact exceptional-prime cutoff from the dual-tangent classification. For every prime `q>Q_k`, the k zero-lines have distinct slopes, all pair intersections are distinct, and no triple concurrence occurs.

Therefore every codeword has at most two zero coordinates, and the exact zero-count spectrum is

- zero zeros:
  `q^2-k*q+C(k,2)` words;
- exactly one zero:
  `k*(q-k+1)` words;
- exactly two zeros:
  `C(k,2)` words;
- three or more zeros:
  `0` words.

Equivalently the only Hamming weights are

`k, k-1, k-2`.

For the maximal `k=9` window, every prime channel `q>53` can divide at most two of the nine filament values for any parameter pair.

## 8. Interpretation

The current structural chain is

`NATIVE TYPED FILAMENT`

`-> QUADRATIC + PARITY CURVATURE`

`-> CURVATURE FLATTENING`

`-> AFFINE RS(2) COSET`

`-> MDS ENDPOINT HOLOGRAPHY`

`-> PUNCTURING COLLAPSE TOWER`

`-> GENERIC THREE-LEVEL LOCAL BRIGHTNESS SPECTRUM`.

The prime events are all-unit realizations inside these geometry-selected affine code cosets. Their finite abundance remains compatible with the previously frozen Hardy-Littlewood-type null model; this note classifies the exact carrier/code structure rather than claiming a nonclassical prime-frequency law.
