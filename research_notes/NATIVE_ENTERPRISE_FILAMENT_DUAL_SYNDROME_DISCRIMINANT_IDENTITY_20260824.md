# Native Enterprise filament codes: dual-syndrome / arrangement-discriminant identity

Status: `FREE_RESEARCH_EXACT_UNIFICATION_THEOREM / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_GLOBAL_ISLAND_DUAL_MDS_TRIPLE_CHECKS_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_CHIRAL_DOUBLE_COVER_ACCESS_STRUCTURE_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_ARRANGEMENT_DISCRIMINANT_STAIRCASE_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_P_ADIC_EXCEPTION_DESINGULARIZATION_20260824.md`.

## 1. Oriented three-position check

Take two same-parity indices

`u<v`

with common parity e, and one opposite-parity index w.

For a value packet V define the affine-annihilating triple check

`T_(u,v;w)(V)`

`=(v-u)*V_w + (w-v)*V_u - (w-u)*V_v`.

The coefficients sum to zero and their index-weighted sum is zero, so every affine word is annihilated.

For the native curvature packet

`V_j=a+b*j+(3*j^2+chi*epsilon_j)/2`,

a direct factorization gives

`T_(u,v;w)(V)`

`=(v-u)/2 * [3*(w-u)*(w-v)+chi*(-1)^e]`.

Define the normalized syndrome

`D_(u,v;w)^chi`

`=2*T_(u,v;w)(V)/(v-u)`

`=3*(w-u)*(w-v)+chi*(-1)^e`.

It is independent of the placement parameters `(a,b)` and depends only on the relative index geometry and chirality.

## 2. The old concurrence obstruction is exactly a dual-code syndrome

The previous line-arrangement classification found the exceptional triple-concurrence obstruction

- `3*(w-u)*(w-v)+chi` for an even same-parity pair;
- `3*(w-u)*(w-v)-chi` for an odd same-parity pair.

These are precisely the two cases of `D_(u,v;w)^chi` above.

Therefore the arrangement-discriminant factors are not an independent construction.  They are the normalized minimum-support dual MDS syndromes of the unflattened native value code.

Freeze:

`DUAL TRIPLE CHECK SYNDROME = ARRANGEMENT CONCURRENCE OBSTRUCTION`.

## 3. Curvature flattening isolates the hidden mode

Define

`Y_j=2*V_j-3*j^2`.

Then

`Y_j=A+B*j+chi*epsilon_j`.

Applying the same triple check gives

`T_(u,v;w)(Y)=chi*(v-u)*(-1)^e`.

Thus the unflattened syndrome splits canonically into

1. a quadratic geometric backbone `3*(w-u)*(w-v)`;
2. one chiral bit `chi*(-1)^e`.

Subtracting curvature converts the full arrangement obstruction into the pure parity-bridge mode detector.

## 4. Polarization of the minimum-weight dual checks

Let

`E=ceil(k/2)`

be the number of even positions and

`O=floor(k/2)`

the number of odd positions in a length-k window.

The `C(k,3)` minimum-support dual checks split into

- mode-blind same-parity triples:
  `C(E,3)+C(O,3)`;
- mode-sensitive mixed-parity triples:
  `C(E,2)*O+E*C(O,2)`
  `=E*O*(k-2)/2`.

The mixed-parity counts for `k=3,...,9` are

`1,4,9,18,30,48,70`.

For the sharp nine-Cell packet there are exactly

`70`

mode-sensitive minimum dual checks.  This is the same set of 70 factors used in each sharp-nine arrangement-discriminant product.

## 5. Exceptional prime channels as syndrome divisors

Assume

`q>max(3,k-1)`.

Then `v-u` is a unit modulo q, and three coordinate-zero lines are concurrent modulo q exactly when

`D_(u,v;w)^chi=0 mod q`.

Hence the post-slope exceptional support is exactly the set of prime divisors of the product

`Delta_k^chi=product |D_(u,v;w)^chi|`

over all mode-sensitive dual triples.

The previously frozen factorization staircase follows immediately from these dual syndromes.

For `k=9`, the two products have common radical

`2*5*7*11*13*23*31*53`.

After removing the small channels, the final local singular prime is 53.

## 6. p-adic depth is dual-syndrome valuation

The same three lines are concurrent modulo `q^a` exactly when

`q^a | D_(u,v;w)^chi`.

Therefore the p-adic thickness of every exceptional singularity is exactly

`v_q(D_(u,v;w)^chi)`.

For the sharp-nine post-small channels `11,13,23,31,53`, every obstruction has absolute value at most106, so every q-adic depth is one and the arrangement becomes generic at `q^2`.

Thus the p-adic desingularization theorem is the valuation refinement of the dual-check syndrome identity.

## 7. Prime-valued specialization

When the coordinates are realized by primes in a native island, any mixed-parity triple of prime values computes the exact integer syndrome above.

This readout is not reconstructible from the three prime/composite bits alone:

- the bits only say that all three coordinates are nonzero in every local prime channel;
- the weighted prime values determine the exact geometry/chirality syndrome;
- the prime divisors of that syndrome determine which external residue channels can create line-arrangement singularities.

It is therefore a genuine value-level multi-Cell invariant selected by the native incidence geometry.

## 8. Unified chain

The previously separate structures now form one exact chain:

`TRIPLE-CELL INCIDENCE`

`-> MINIMUM-WEIGHT DUAL CHECK`

`-> QUADRATIC + CHIRAL SYNDROME`

`-> PARITY-BRIDGE MODE DECODER`

`-> EXCEPTIONAL LINE CONCURRENCE`

`-> ARRANGEMENT DISCRIMINANT`

`-> P-ADIC DESINGULARIZATION DEPTH`.

## 9. Boundary

Dual codes, line arrangements and discriminants are classical.  The research-specific theorem is that the native filament's incidence curvature makes all three descriptions literally the same normalized integer quantity.
