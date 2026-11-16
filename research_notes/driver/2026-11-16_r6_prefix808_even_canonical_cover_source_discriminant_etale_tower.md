# PREFIX-808: exact source-relative discriminant of the even-height Reeve canonical cover

Date: 2026-11-16. Status: **PROVED, EXACT MODEL-INTERNAL, DRIVER AUTHOR-SIDE EXTENSION; INDEPENDENT NATIVE RESULT REVIEW NOT PERFORMED**.

## Scientific inputs, scope and attribution

The original TU/Reeve 0/1 source-observer construction is attributed to **EM-DIRECT-4660FF**. The previously established even-height canonical-cover complete-intersection presentation is attributed to **EM-DVR-DEBB5E**, with fixed evidence:

- `43b9cb3ba76404104b384c1e46a3e6eb7e56e0fc:research_notes/driver/2026-11-16_r6_prefix808_even_index_one_cover_complete_intersection.md` (Blob `0acab9ea09aa4faa780086d692fa4b7ad5235927`);
- `0c66d9a820765a5cf5877fa3f4696a58ce406199:research_notes/driver/2026-11-16_r6_prefix808_even_canonical_cover_quadratic_joint_tower_discriminant.md` (Blob `08b4894bf9a43662946a65907fa4173ab58908fa`).

This note computes the **full** discriminant from the canonical cover to the independent polynomial-source algebra. It is distinct from both the already computed rank-two intermediate discriminant `4XZ` and the earlier degree-`h` original observer-algebra discriminant. All equalities hold over any field, including bad characteristic.

## Theorem

Let `K` be any field and `h=2k >= 2`, with `k>=1`. Set

```text
R = K[U_0,U_1,U_2,U_3],   A=U_1*U_2,   B=U_0*U_3,
E = R[X,Z]/(X^k-B, Z^k-A),
C = E[Y]/(Y^2-XZ).
```

Identify `C` with the previously established index-one canonical-cover algebra `C_h^can`. It is a finite **free** `R`-algebra of rank `n=2k^2=h^2/2`, with ordered basis

```text
{ X^i Z^j, Y X^i Z^j | 0<=i,j<k }.
```

With respect to this basis the regular trace discriminant is **exactly**

```text
disc_R(C) = (4*k^4)^(k^2) * (A*B)^(2*k^2-k)
          = 2^(2*k^2) * k^(4*k^2) * (A*B)^(k*(2*k-1))
```

as an identity in `R` (there is no unspecified unit or sign).

Consequently, the locus of base points over which the full finite-flat cover `Spec(C) -> Spec(R)` is étale is **exactly** `D(AB)` when `char(K)` does not divide `h`. If `char(K)` divides `h`, no base point has a finite étale whole fiber. In particular, the intermediate double cover's separability cannot alone certify separability of the entire source-relative tower when `char(K)` divides `k`.

## Proof

Write the finite free tower as `R -> E -> C` with ranks `k^2` and `2`.

**Step 1: discriminant of `E/R`.** For the monogenic algebra `R[T]/(T^k-b)`, the basis `1,T,...,T^(k-1)` has regular trace discriminant

```text
delta_k(b) = (-1)^((k-1)*(k+2)/2) * k^k * b^(k-1).
```

This follows by the determinant of the trace pairing (equivalently the resultant with the formal derivative), and is a polynomial identity over the integers, so it also holds after specializing to inseparable characteristics. The two independent monogenic factors have rank `k` each. For tensor-product bases, the trace Gram matrix is the Kronecker product, so

```text
disc_R(E) = delta_k(B)^k * delta_k(A)^k
          = k^(2*k^2) * (AB)^(k*(k-1)).
```

The sign cancels because its exponent is `k*(k-1)*(k+2)`, which is even.

**Step 2: discriminant of `C/E`.** Multiplication by `Y` in the basis `(1,Y)` has matrix `[[0,XZ],[1,0]]`. Thus the trace Gram is `diag(2,2XZ)` and `disc_E(C)=4XZ`, as in the pinned predecessor.

**Step 3: norm and discriminant of the tower.** For compatible tower bases the exact finite-free discriminant identity is

```text
disc_R(C) = disc_R(E)^[C:E] * Norm_(E/R)(disc_E(C)).
```

The regular norm of `X` in `R[X]/(X^k-B)` is `(-1)^(k+1) B`. In `E` this norm is raised to the `k`th power, yielding `Norm_(E/R)(X)=B^k`, since `k(k+1)` is even. Similarly `Norm_(E/R)(Z)=A^k`. Therefore

```text
Norm_(E/R)(4XZ) = 4^(k^2) * (AB)^k,
disc_R(C) = [k^(2*k^2) * (AB)^(k*(k-1))]^2
            * 4^(k^2) * (AB)^k
          = (4*k^4)^(k^2) * (AB)^(2*k^2-k).
```

These are integral polynomial identities; no division by `k` or `2` is used.

**Step 4: the étale base locus.** A finite locally free algebra is étale over a base locus precisely where its trace pairing is perfect. Over `K`, the constant discriminant coefficient `(4k^4)^(k^2)` is nonzero exactly when `char(K)` does not divide `2k=h`. In that case the discriminant is invertible precisely on `D(AB)`. In a characteristic dividing `h`, the determinant is the zero element of the polynomial ring `R` and there is no étale base fiber. QED.

## Independent exact matrix verification

As a finite check, choose `A=2, B=3` in characteristic zero and form the full `2k^2 x 2k^2` regular trace Gram matrix from the normal-form multiplication

```text
X^k=B, Z^k=A, Y^2=XZ,
(X^i Z^j Y^e)*(X^l Z^m Y^f)
  = B^qB A^qA X^rX Z^rZ Y^((e+f)%2),
i+l+floor((e+f)/2) = k*qB+rX,
j+m+floor((e+f)/2) = k*qA+rZ.
```

Exact integer determinants directly computed by independent multiplication matrices give:

| k | h | rank | exact determinant |
|---:|---:|---:|---:|
| 1 | 2 | 2 | 24 |
| 2 | 4 | 8 | 782757789696 |
| 3 | 6 | 18 | 18500090274004304366526937876660224 |

All three equal `(4k^4)^(k^2) * 6^(2k^2-k)`. These examples corroborate, rather than replace, the general tower proof.

## Research consequence and admission boundary

The full source-relative discriminant distinguishes the Kummer factors `X^k-B, Z^k-A` from the joint quadratic factor `Y^2-XZ`, and retains the joint observer generator `Y=Z_0Z_1`. This is an exact algebraic invariant of the existing Reeve source-overring model, with no assertion of an X6 native state/event morphism or promotion to the larger Heartbeat World objective. Independent Driver review and Native Result admission remain separate.

Provenance: original TU/Reeve construction **EM-DIRECT-4660FF**; even canonical-cover presentation and new full discriminant calculation **EM-DVR-DEBB5E**. This result does not borrow another Researcher identity, reopen an existing Result or modify any task CLAIM.
