# Projective spectral conductor and complement sheets

Status: `FREE_RESEARCH / EXACT FINITE SPECTRAL FIELD THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- irreducible projective factors `Omega_d`;
- projective denominator transition under `R_2`;
- complement involution `v -> 4-v`.

## 1. Odd denominator and its doubled denominator

Let `d>1` be odd. Primitive projective denominator-`d` roots and denominator-`2d` roots are exchanged by the complement map

\[
v\longmapsto4-v.
\]

More explicitly, internal phase indexing gives

\[
\boxed{
\operatorname{Roots}(\Omega_{2d})
=
\{4-\alpha:\alpha\in\operatorname{Roots}(\Omega_d)\}.
}
\tag{CS-1}
\]

Both polynomials are monic of the same degree

\[
h=\varphi(d)/2=\varphi(2d)/2.
\]

Therefore monic leading-coefficient comparison gives the exact polynomial identity

\[
\boxed{
\Omega_{2d}(v)
=(-1)^h\Omega_d(4-v)
\qquad(d>1\text{ odd}).
}
\tag{CS-2}
\]

This identity is purely finite and does not require a cyclotomic field model.

---

## 2. Equality of the projective spectral fields

Let `alpha` be a root of `Omega_d`. Then

\[
4-\alpha
\]

is a root of `Omega_(2d)`, and conversely.

Hence

\[
\mathbf Q(\alpha)=\mathbf Q(4-\alpha).
\]

Therefore, with compatible embeddings,

\[
\boxed{
K_{2d}=K_d
\qquad(d>1\text{ odd}).
}
\tag{CS-3}
\]

Thus doubling an odd projective denominator does **not** create a new projective spectral field; it changes the primitive generator by the complement sheet.

---

## 3. Oriented primitive block for odd denominator

The oriented primitive factor for odd `d` was shown to split as

\[
\Psi_d(v)=\Omega_d(v)\Omega_{2d}(v).
\]

Using (CS-2),

\[
\boxed{
\Psi_d(v)
=(-1)^h\Omega_d(v)\Omega_d(4-v).
}
\tag{CS-4}
\]

Thus the two irreducible factors of the oriented block are the two complement-coordinate sheets of the **same** Galois field `K_d`.

They are not independent number fields.

This sharpens the BRC interpretation:

```text
oriented primitive block Psi_d, d odd
   -> sheet + : Omega_d(v)
   -> sheet - : Omega_d(4-v)
   -> both sheets live in one projective spectral field
```

---

## 4. Spectral conductor normalization

Define the projective spectral conductor index

\[
\boxed{
\mathfrak c(d)
:=
\begin{cases}
 d/2,& d\equiv2\pmod4,\\
 d,& \text{otherwise}.
\end{cases}
}
\tag{CS-5}
\]

For `d>2`, repeated use of (CS-3) gives

\[
\boxed{
K_d=K_{\mathfrak c(d)}.
}
\tag{CS-6}
\]

So the only redundant denominator label at field level is a single factor of two attached to an odd denominator.

No further reduction occurs when `4|d`, because

\[
\varphi(d)>\varphi(d/2)
\]

and the projective field degrees differ.

---

## 5. Galois group compatibility

When `d=2m` with `m` odd,

\[
(\mathbf Z/2m\mathbf Z)^\times
\cong
(\mathbf Z/m\mathbf Z)^\times
\]

by reduction modulo `m`. Quotienting by `{±1}` gives

\[
\boxed{
(\mathbf Z/d\mathbf Z)^\times/\{\pm1\}
\cong
(\mathbf Z/\mathfrak c(d)\mathbf Z)^\times/\{\pm1\}.
}
\tag{CS-7}
\]

This agrees exactly with the field identity (CS-6) and the native Galois theorem.

---

## 6. Discriminant equality for the doubled odd label

A translation/reflection of the generator does not change pairwise root differences in absolute value. From (CS-2),

\[
\boxed{
\operatorname{Disc}(\Omega_{2d})
=
\operatorname{Disc}(\Omega_d)
\qquad(d>1\text{ odd}).
}
\tag{CS-8}
\]

This is also visible directly in the native projective discriminant formula: the apparent extra factor `2` in the denominator label cancels against the midpoint/primitive-mass term.

Examples:

```text
Disc Omega_5  = Disc Omega_10 = 5
Disc Omega_7  = Disc Omega_14 = 49
Disc Omega_9  = Disc Omega_18 = 81
Disc Omega_15 = Disc Omega_30 = 1125
```

---

## 7. Midpoint special value becomes a constant-term transfer

Setting `v=0` in (CS-2):

\[
\boxed{
|\Omega_d(4)|
=|\Omega_{2d}(0)|.
}
\tag{CS-9}
\]

The right side is the primitive projective mass at denominator `2d`. Since `d>1` is odd, `2d` has the distinct prime divisors `2` and at least one odd prime. Therefore `2d` is never a prime power, and the primitive mass law gives

\[
\boxed{
|\Omega_d(4)|=1
\qquad(d>1\text{ odd}).
}
\tag{CS-10}
\]

This is the correct odd-denominator midpoint law. In particular, even when `d=p^a` is an odd prime power, the doubled denominator `2p^a` is not a prime power, so the value remains one.

---

## 8. BRC meaning

In the projective BRC trace coordinate, the involution

\[
v\leftrightarrow4-v
\]

is the algebraic remnant of changing the oriented trace sheet.

For odd primitive denominator, the two oriented irreducible root blocks are therefore related by a trivial affine field automorphism of the coordinate, not by an unrelated algebraic extension.

A BRC root-block compiler may exploit this by storing:

- one projective irreducible block `Omega_d`;
- one explicit sheet involution `v -> 4-v`;

instead of treating `Omega_d` and `Omega_(2d)` as unrelated algebraic fields.

Hard boundary: whether this compression is operation safe depends on whether the requested BRC observation is invariant under the sheet involution.

---

## 9. Structural consequence

Freeze at free-research strength:

`ODD_DENOMINATOR_DOUBLING = COMPLEMENT_GENERATOR_CHANGE, NOT_NEW_PROJECTIVE_FIELD`.

`K_d = K_(2d) FOR d ODD > 1`.

`ORIENTED_ODD_PRIMITIVE_TWO_BLOCK_SPLIT = TWO_COMPLEMENT_SHEETS_OF_ONE_GALOIS_FIELD`.

`PROJECTIVE_SPECTRAL_CONDUCTOR = d WITH A SINGLE REDUNDANT FACTOR_2_REMOVED WHEN d=2 mod 4`.
