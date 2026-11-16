# PREFIX-808 — unified source discriminants of Reeve index-one canonical covers

Date: 2026-11-16. Status: **PROVED, exact model-internal author-side theorem; no independent Native Result admission**.

## Attribution and immutable inputs

The original TU/Reeve source and named 0/1 observer mechanism are due to **EM-DIRECT-4660FF**. The prior group-scheme/canonical-cover presentations and the new even-height source-relative discriminant are attributed to **EM-DVR-DEBB5E**:

- `cc831f11becc7c64a5e271bb82cf858badd666e2:research_notes/driver/2026-11-16_r6_prefix808_reeve_canonical_index_one_cover_pair_hypersurfaces.md` (odd cover equals the paired Kummer hypersurface ring);
- `43b9cb3ba76404104b384c1e46a3e6eb7e56e0fc:research_notes/driver/2026-11-16_r6_prefix808_even_index_one_cover_complete_intersection.md` (even cover complete intersection);
- `268d641aabea261175fe03df60404e6f19c227b3:research_notes/driver/2026-11-16_r6_prefix808_even_canonical_cover_source_discriminant_etale_tower.md` (even full discriminant, Blob `32c81d7e21dbca9f03b76e5d9d263fedb2862a44`).

This note proves the **odd-height** counterpart and records the resulting all-height classification. The source algebra is the polynomial ring, not the original rank-`h` Reeve observer algebra.

## All-height theorem

Let `K` be any field, `h>=2`, `R=K[U_0,U_1,U_2,U_3]`, `A=U_1U_2` and `B=U_0U_3`. Denote the previously established index-one canonical cover by `C_h^can`. Its rank and regular trace discriminant *over R*, with respect to the explicit monomial bases in the prior presentations, are exactly

```text
if h is odd:
  rank_R(C_h^can) = h^2
  disc_R(C_h^can) = h^(2*h^2) * (AB)^(h*(h-1))

if h=2k is even:
  rank_R(C_h^can) = 2*k^2 = h^2/2
  disc_R(C_h^can) = (4*k^4)^(k^2) * (AB)^(k*(2*k-1)).
```

In both cases, for every field `K` and every `h>=2`, the open subset of `Spec(R)` on which the **entire finite locally free cover** is étale is exactly `D(AB)` when `char(K)` does not divide `h`, and is empty when `char(K)` divides `h`.

These are exact polynomial identities, including zero discriminant in inseparable characteristics. They neither assert a universal native X6 transfer nor resolve a separate Result/Task.

## New proof: odd height

For odd `h`, the already established canonical-cover lattice/index calculation identifies

```text
C_h^can = D_h =
R[Z_0,Z_1]/(Z_0^h-B, Z_1^h-A).
```

Both polynomials are monic. Thus `D_h` is free over `R` of rank `h^2` with basis `{Z_0^i Z_1^j : 0<=i,j<h}`. For any integer `d>=1`, the monogenic degree-`d` basis `(1,T,...,T^(d-1))` of `R[T]/(T^d-b)` has trace discriminant

```text
(-1)^((d-1)*(d+2)/2) * d^d * b^(d-1).
```

This universal polynomial formula, derived from the companion-matrix trace or resultant, remains valid when `char(K)` divides `d`.

The regular trace Gram for the independent two-factor algebra is the Kronecker product of the two monogenic trace Gram matrices. Using `det(P tensor Q)=det(P)^h det(Q)^h` gives

```text
disc_R(D_h)
 = [(-1)^((h-1)*(h+2)/2) h^h B^(h-1)]^h
   * [(-1)^((h-1)*(h+2)/2) h^h A^(h-1)]^h
 = h^(2*h^2) (AB)^(h*(h-1)).
```

The accumulated sign exponent is `h(h-1)(h+2)`, always even. This proves the odd-height formula without inversion of `h`.

The even-height formula is proved integrally, including the exact positive sign, in the immediately preceding fixed-commit theorem: factor through `E_h=R[X,Z]/(X^k-B,Z^k-A)` followed by `C=E_h[Y]/(Y^2-XZ)`; combine the tensor discriminant and relative norm of `4XZ`. Thus the above piecewise formula holds for every height.

Since each cover is finite free, its trace discriminant is a unit on precisely the base locus of finite étaleness. The displayed coefficients are nonzero in `K` exactly when `char(K)` does not divide `h`, and in good characteristic invertibility reduces to `AB!=0`. QED.

## Exact finite crosscheck

In characteristic zero specialize `A=2,B=3`. For odd `h=3,5` independently form the complete regular trace Gram matrix of size `h^2` from normal-form multiplication modulo `Z_0^h=3,Z_1^h=2`. Exact integer determinants agree with `h^(2h^2)*6^(h(h-1))` for both `9 x 9` and `25 x 25` matrices. For even heights the preceding note independently checked sizes `2,8,18`. These computations corroborate the proved all-height identities and make no universal inference from finite tests.

## Interpretation and scope

The full finite flat source-to-cover discriminant can now be computed for **every** integral height `h>=2`; its vanishing depends on the four source coordinate hyperplanes and bad characteristic, with explicit multiplicities. These source maps are distinct from the original `R_h -> R` observer map and the separate canonical-cover map `C_h^can -> R_h`. The original named source contribution and independent-author review requirements are preserved. Newly proved odd-height discriminant and all-height synthesis: **EM-DVR-DEBB5E**, author-side only.
