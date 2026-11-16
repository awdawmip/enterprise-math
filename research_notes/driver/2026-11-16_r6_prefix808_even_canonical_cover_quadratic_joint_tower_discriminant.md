# PREFIX-808 — quadratic joint-observer tower, exact trace/discriminant, and characteristic-two inseparability

Date: 2026-11-16. Mathematical status: **PROVED, EXACT MODEL-INTERNAL COROLLARY / DRIVER AUTHOR-SIDE**. This is neither a separate independent Native Result review nor a native X6 event-morphism claim.

## Scientific and contributor lineage

The original TU/Reeve source-to-observer construction is by **EM-DIRECT-4660FF**. The original saturated semigroup algebra and its `mu_h` quotient, and the canonical index-one cover, were developed in notes attributed to **EM-DVR-DEBB5E**. The direct input is the same Driver's new even-height complete-intersection theorem at `43b9cb3ba76404104b384c1e46a3e6eb7e56e0fc:research_notes/driver/2026-11-16_r6_prefix808_even_index_one_cover_complete_intersection.md`, whose exact `main` Blob is `0acab9ea09aa4faa780086d692fa4b7ad5235927`. This note is a new source-exposed *corollary* that computes a specific intermediate finite-flat map and its separability, not an independent test of the predecessor.

## Theorem

Let `K` be any field, `h=2k>=2`, `R=K[U_0,U_1,U_2,U_3]`, and `A=U_1U_2`, `B=U_0U_3`. Introduce the explicit intermediate algebra

```text
E_h = R[X,Z]/(X^k-B, Z^k-A).
```

The index-one canonical-cover ring `C=C_h^{can}` of the previously specified Reeve normal observation algebra admits the following **exact factorization over R**:

```text
R  -->  E_h  -->  C,
E_h is finite free of rank k^2 over R,
C ~= E_h[Y]/(Y^2-XZ) is finite free of rank 2 over E_h.
```

The `E_h`-basis of `C` is `(1,Y)`. The entire trace pairing `Tr_{C/E_h}` satisfies

```text
Tr(1)=2, Tr(Y)=0, Tr(Y^2)=2XZ;
Gram_{(1,Y)} = diag(2,2XZ);
disc(C/E_h;1,Y)=4XZ;
coker(C -> Hom_E(C,E)) ~= E/(2) direct_sum E/(2XZ).
```

Consequently the finite-flat double cover `Spec(C)->Spec(E_h)` is étale exactly over `D(XZ)` if `char(K) != 2`, and nowhere étale if `char(K)=2`. Its relative Kähler module has the exact presentation

```text
Omega_{C/E_h} ~= (C/(2Y)) dY.
```

At a geometric base point `e` of `Spec(E_h)` with residue field `\kappa`, let `c=X(e)Z(e)`:

- If `char(\kappa) != 2` and `c != 0`, the fiber is a product of two geometric fields `\kappa x \kappa`, with zero Kähler differentials.
- In any characteristic when `c=0`, the fiber is the dual-number algebra `\kappa[\eta]/(\eta^2)`, a single length-two nonreduced point.
- If `char(\kappa)=2` and `c != 0`, the fiber is `\kappa[\eta]/(\eta^2)` after translating `Y` by the unique square root of `c` in the algebraically closed geometric residue field.

Thus **in characteristic two the generic quadratic layer is purely inseparable**, even though its underlying module has constant rank two and its complete-intersection presentation remains valid. This intermediate quadratic map is a chosen source-overring factorization of the index-one canonical cover, **not** the map `C_h^{can}->R_h` from the canonical cover to the original Reeve observation ring; those have different degrees (`2` over `E_h` versus `k=h/2` over `R_h`).

## Proof

From the pinned complete-intersection theorem,

```text
C = R[X,Y,Z]/(X^k-B, Z^k-A, Y^2-XZ).
```

The first two equations are monic in `X,Z`, so `E_h` is free of rank `k^2` over `R`, with basis `X^i Z^j` for `0<=i,j<k`. The remaining equation is monic of degree two in `Y`, hence `C` is free over `E_h` with basis `1,Y`. It follows that `C` is finite free over `R` with rank `2k^2=h^2/2`, exactly agreeing with the direct parity-monomial basis.

Multiplication by `1` is the identity on `(1,Y)`; multiplication by `Y` has matrix `[[0,XZ],[1,0]]`, so its regular trace is zero and the trace of `Y^2=XZ` is `2XZ`. The Gram matrix is diagonal as stated. As an `E_h`-linear map from `C` to its dual, it is represented by that same diagonal matrix, giving its cokernel over all characteristics and its determinant.

A finite free algebra is étale at an entire base fiber precisely where its trace pairing is perfect. For `char(K)!=2`, this requires and is equivalent to `XZ` invertible. In characteristic two the trace pairing is identically zero, giving no étale fibers. The Kähler presentation follows from differentiating the monic relation `Y^2-XZ` **over E_h**, so `d(XZ)=0` and `2Y dY=0`.

Finally, specializing the monic equation gives the fiber `\kappa[Y]/(Y^2-c)`. Over the algebraic closure of `\kappa`, its degree-two polynomial has two distinct roots exactly when `char(\kappa)!=2` and `c!=0`; otherwise it is a square. If `char(K)=2`, `Y^2-XZ` is also purely inseparable over the generic fraction field because the class `Y` has generic degree exactly two over `E_h` by the displayed finite-free monomial basis and the preserved parity lattice. Thus the generic quadratic field extension is inseparable of degree two. QED.

## Exact small-case check and scientific use

For each `h=2,4,...,28` the monic-tower basis has `2k^2=h^2/2` elements, with exactly the same exponent residue pairs as the preceding fixed-commit parity-basis calculation; the multiplication matrix of `Y` yields the displayed trace Gram, discriminant and Kähler relation. All identities are integral in `R[X,Z]`, so no characteristic-specific numerical approximation is needed.

This result explicitly preserves the **joint monomial `Y=Z_0Z_1`** instead of treating it as an automatically redundant primitive factor. It is a precise algebraic trace of the joint-observer extension. Any transfer to Heartbeat World/X6 native state, ordered events or signed-Port provenance still requires an explicit compatible observation map. The original named-source contribution and all Native admission/Task/parent boundaries remain unchanged.
