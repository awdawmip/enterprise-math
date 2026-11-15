# PREFIX-808 Reeve observer extension: exact trace, discriminant, and étale locus

Date: 2026-11-16 (Asia/Taipei). Author-side, source-exposed mathematical extension by `EM-DVR-DEBB5E`. The original named-source PREFIX-808 work remains attributed to `EM-DIRECT-4660FF`. This note is **not** an independent review, a Native Result, a Claim, or an assertion about native X6/Port/Link.

## Verified input and scope

Retain exactly the TU source polytope `P_h`, 0/1 observer `W_h`, Reeve lattice cone, and disjoint normal forms proved in:

- `research_notes/driver/2026-11-16_r6_prefix808_reeve_saturation_free_module_and_exact_multiplication.md`, GitHub commit `ebd02fad57e4ca25052749afdcb9bada7940b329`, Git blob `03e46deb12303dc8dedfb39651ffb4460a653779`.
- Its foundational contribution: `EM-DIRECT-4660FF`; subsequent proof and finite-free extension: `EM-DVR-DEBB5E`.

Fix any integer `h >= 2` and any field `K`. Write

```
R = K[U_0,U_1,U_2,U_3],   A = U_1 U_2,   B = U_0 U_3,
S = K[C_h] = R (+) R V_1 (+) ... (+) R V_(h-1).
```

The sum is a *direct sum of R-modules*, not a ring direct product. The previously proved multiplication rule is

```
V_r V_s = A V_(r+s)              if r+s<h,
        = A B                    if r+s=h,
        = B V_(r+s-h)            if r+s>h,
```

with `1 <= r,s < h`. Each `V_r` has observer height congruent to `r mod h`, so this decomposition and the rule are exact in the ambient lattice; the source-realizable semigroup is still `S_h`, and the larger `C_h` contains non-realizable observed lattice states.

## Theorem: cyclic generic equation and discriminant

1. `S` is finite locally free of degree `h` over `R`. Upon inverting `A`, set `T=V_1/A`; then

   ```
   S[A^(-1)] = R[A^(-1)][T] / (T^h - B/A),
   V_r = A T^r  (1<=r<h).
   ```

   The polynomial `T^h-B/A` is irreducible over `F=Frac(R)`, in **every** characteristic. Thus `Frac(S)/F` is a degree-`h` extension. If `char(K)=p>0` divides `h`, it is generically inseparable; otherwise it is generically separable. Over a field containing the `h`-th roots of unity in the separable case, the generic cover is cyclic Kummer.

2. For the free basis `(1,V_1,...,V_(h-1))`, its trace pairing satisfies

   ```
   Tr(1)=h;    Tr(V_r)=0  (1<=r<h);
   Tr(V_r V_s)=hAB  if r+s=h, and 0 otherwise.
   ```

   Its **exact discriminant** (with this ordered basis) is

   ```
   disc(S/R) =
      (-1)^((h-1)(h-2)/2) * h^h * (U_0 U_1 U_2 U_3)^(h-1).
   ```

3. If `char(K)` does not divide `h`, the finite flat morphism `Spec(S) -> Spec(R)` is étale **precisely** over `D(U_0 U_1 U_2 U_3)`; every point in the four coordinate hyperplanes belongs to the non-étale base locus. If `char(K)=p>0` divides `h`, the morphism is **nowhere étale**, including over the dense torus. This is a relative finite-cover statement in the larger ambient observation lattice, not normalization of the polynomial source algebra within its *own* fraction field.

## Proof

The free basis and multiplication rule are established in the pinned predecessor and imply (1). Inductively, `V_1 V_r=A V_(r+1)` for `r<h-1`, hence `V_r=A(V_1/A)^r`. The closing relation is `V_1^h=A^(h-1) B`. Because both sides of the asserted quotient isomorphism are free rank `h` over `R[A^(-1)]` with these respective bases, the indicated map is an isomorphism. At the DVR `R_(U_0)`, the element `B/A=U_0 U_3/(U_1U_2)` has valuation exactly 1. Eisenstein's criterion shows irreducibility of `X^h-B/A` over `F`, in every characteristic; the derivative `h X^(h-1)` then gives the separability statement.

For (2), after tensoring with `F`, multiplication by `V_r` sends the `h` one-dimensional residue-class summands cyclically, with no diagonal terms for `1<=r<h`; hence its trace is zero. Multiplication by an element of `R` is scalar on all `h` summands and has trace `h` times that scalar. Apply the exact multiplication rule to `V_rV_s`. The trace Gram matrix consists of a `1 x 1` block `[h]` and an `(h-1) x (h-1)` reverse-identity block multiplied by `hAB`. A reverse-identity matrix of size `h-1` has sign `(-1)^((h-1)(h-2)/2)`, yielding the formula by determinant. The trace formula and determinant are polynomial identities and remain meaningful in characteristic dividing `h`.

For (3), a finite locally free commutative algebra is étale at a base point if and only if its trace pairing is perfect there. The displayed determinant is a unit exactly where `h` and all four `U_i` are units. The assertion follows in both characteristic regimes. Independently, on `D(AB)` the Kummer description has invertible derivative exactly when `h` is invertible. QED.

## Independent finite algebra check and boundary

As a consistency check only, the exact symbolic determinant of the trace Gram matrix was verified for every `2<=h<=8` against the closed formula. The arbitrary-`h` result is the preceding algebraic proof, not numerical extrapolation.

This extension adds a precise algebraic and characteristic-sensitive interface to the source/observer distinction, but proves **no** named native signed-Port/Link correspondence. No change to the original researcher's contribution, no independent proof review, no Native Result admission, no Task DONE, and no mother-objective completion is asserted.
