# P025 Supplement 34 — Certificate Image Rank, Saturation Defect, and Access Index

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-certificate-index-stage34`  
Depends on: P025 Supplements 29, 33  
Hard block: `NONE`

## 1. Rank is not the last certificate precision coordinate

Stage 29 computes the rational dimension added by a certificate family after shared-prime coupling:

\[
\Delta_H
=
\operatorname{rank}_{\mathbb Q}
\begin{pmatrix}LB\\HB\end{pmatrix}
-
\operatorname{rank}_{\mathbb Q}(LB).
\]

This determines how many independent rational certificate directions survive on the relation-adapted state.

It does **not** determine the integral certificate image.

Let `Lambda` be the exact integer relation lattice and let

\[
H:\Lambda\to\mathbb Z^q
\]

be a labelled integer-linear certificate map. Define

\[
\boxed{C=H(\Lambda).}
\]

Its saturated lattice in the same labelled rational subspace is

\[
\boxed{
\operatorname{Sat}(C)
=
\operatorname{span}_{\mathbb Q}(C)\cap\mathbb Z^q.
}
\]

Even when the rational certificate rank is already complete, `C` may be a proper finite-index sublattice of its saturation.

## 2. P025-D22 — intrinsic certificate congruence defect

Define

\[
\boxed{
\delta_H
=
[\operatorname{Sat}(C):C].
}
\]

This is an **intrinsic certificate congruence defect**. It belongs to the declared certificate map itself and need not disappear with greater witness-access radius.

If a relation basis is `g_1,...,g_k`, the labelled certificate vectors

\[
H(g_1),\ldots,H(g_k)\in\mathbb Z^q
\]

generate `C`. Let their rational rank be `d`. Standard determinantal-divisor / Smith theory gives

\[
\boxed{
\delta_H
=
\gcd\{ |\det M| : M\text{ is a }d\times d\text{ minor of the generator matrix}\}.
}
\]

For `d=0`, the zero image has defect one inside its zero-dimensional saturation.

This algebra is standard prior mathematics; P025 uses it as an integral precision coordinate.

## 3. Radius-generated certificate image

Let Stage 33's radius-generated relation subgroup be

\[
\Gamma_R
=
\langle Z_R(B)\cap\Lambda\rangle.
\]

Define the certificate subgroup visible/generated through radius `R` by

\[
\boxed{C_R=H(\Gamma_R)\subseteq C.}
\]

The certificate ranks are nondecreasing because

\[
\Gamma_R\subseteq\Gamma_{R+1}.
\]

Once

\[
\operatorname{rank}_{\mathbb Q} C_R
=
\operatorname{rank}_{\mathbb Q} C,
\]

define the finite **access-induced certificate defect**

\[
\boxed{
J_H(R)=[C:C_R].
}
\]

Before full certificate rank, use `J_H(R)=infinity` semantically.

## 4. P025-T93 — certificate image indices form a divisibility chain

After full certificate rank,

\[
C_R\subseteq C_{R+1}\subseteq C
\]

are full-rank sublattices of the same rational certificate space. Therefore

\[
\boxed{J_H(R+1)\mid J_H(R).}
\]

In particular `J_H(R)` is nonincreasing and eventually reaches one because Stage 33 guarantees a finite radius with

\[
\Gamma_R=\Lambda.
\]

Define the **certificate-complete radius**

\[
\boxed{
\rho_H
=
\min\{R:C_R=C\}
=
\min\{R:J_H(R)=1\}.
}
\]

Then

\[
\boxed{
\rho_H\le\rho_{\rm gen}.
}
\]

The inequality can be strict.

## 5. P025-T94 — exact factorization of total integral defect

Whenever `C_R` has full certificate rank, `C_R`, `C`, and `Sat(C)` have the same rational span. Ordinary index multiplication gives

\[
\boxed{
[\operatorname{Sat}(C):C_R]
=
[\operatorname{Sat}(C):C]\,[C:C_R]
=
\delta_H J_H(R).
}
\]

So there are two independent reasons why the currently generated certificate states may miss labelled integer certificate vectors:

1. **intrinsic congruence:** the complete certificate image itself is not saturated (`delta_H>1`);
2. **finite access:** the current radius has not yet generated the complete certificate image (`J_H(R)>1`).

Increasing radius can remove the second defect but not the first.

## 6. Strict task-relative separation: `3+4=7`

For

\[
3+4=7
\]

the raw block derivative image generators are

\[
A(3)=1,
\qquad
A(4)=4,
\qquad
A(7)=1.
\]

A basis of the exact block-value relation lattice is

\[
\boxed{
g_1=(1,0,1),\qquad g_2=(0,4,4).}
\]

For the Wronskian certificate

\[
H(u,v,w)=3v-4u,
\]

one has

\[
H(g_1)=-4,
\qquad
H(g_2)=12,
\]

so the complete raw certificate image is

\[
\boxed{C=4\mathbb Z.}
\]

At radius one, the only nonzero relation-compatible states are

\[
\pm g_1.
\]

They generate only a rank-one subgroup of the rank-two relation lattice. Thus the relation state is **not** full rank at radius one.

But

\[
H(\pm g_1)=\mp4
\]

already generates all of `4Z`. Therefore

\[
\boxed{
\rho_H=1
<
\rho_{\rm rank}=2
=
\rho_{\rm gen}.
}
\]

This is a strict exact counterexample to the idea that certificate completeness requires relation-state completeness.

The declared future certificate can become exact while an entire independent relation direction remains unresolved.

## 7. Pure access defect: `1+22=23`

For the unit relation

\[
1+22=23,
\]

the Wronskian certificate is simply the common derivative value. Its complete image is

\[
C=\mathbb Z,
\qquad
\delta_H=1.
\]

At radius two the accessible nonzero certificate values generate only

\[
C_2=2\mathbb Z,
\]

so

\[
\boxed{J_H(2)=2.}
\]

At radius four, values with gcd one are accessible and

\[
C_4=\mathbb Z,
\qquad
\boxed{J_H(4)=1.}
\]

Hence its strict certificate profile contains

\[
\boxed{
(R=2;\ \operatorname{rank}=1,J=2)
\longrightarrow
(R=4;\ \operatorname{rank}=1,J=1).
}
\]

Here the defect is entirely access-induced; the full certificate image is already saturated.

## 8. P025-T95 — `eta_min` is a normalized certificate saturation index

For primitive abc, let

\[
M=m(a)m(b)m(c)
\]

be the multiplicity-residual product and let the raw Wronskian image be

\[
W(\Lambda)=D\mathbb Z.
\]

Pasten's residual-product divisibility implies

\[
M\mid W(x)
\qquad
\text{for every }x\in\Lambda.
\]

Therefore

\[
\widetilde W=W/M:\Lambda\to\mathbb Z
\]

is an integer-valued group homomorphism. Its image is

\[
\boxed{
\widetilde W(\Lambda)
=
(D/M)\mathbb Z
=
\eta_{\min}\mathbb Z.
}
\]

The saturation of any nonzero subgroup of `Z` is `Z`. Consequently

\[
\boxed{
\eta_{\min}
=
[\mathbb Z:\widetilde W(\Lambda)].
}
\]

Thus the P025 absorption floor has a sharper interpretation:

> **`eta_min` is exactly the intrinsic integral congruence defect of the normalized Wronskian certificate image.**

It is not merely a quality score or a minimum magnitude.

### Examples

- `2+3=5`: `eta_min=1`; the normalized certificate image is saturated.
- `5+7=12`: `eta_min=2`; only even normalized Wronskian values occur.
- `3+4=7`: `eta_min=2`; its certificate image is already access-complete at radius one but remains intrinsically index two in `Z`.
- `1+242=243`: `eta_min=5`; the normalized certificate image is `5Z`.

## 9. Stage-06 obstruction spectrum becomes a defect-group prime spectrum

For the scalar normalized Wronskian,

\[
\mathbb Z/\widetilde W(\Lambda)
\cong
\mathbb Z/\eta_{\min}\mathbb Z.
\]

Therefore the Stage-06 local absorption-obstruction spectrum is exactly the prime-power decomposition of this finite certificate congruence defect.

In particular, the earlier phenomenon that an obstruction prime may lie outside `rad(abc)` can now be read as:

> the finite certificate quotient can contain a prime torsion factor generated by valuation-exponent arithmetic even when that prime is absent from first-order abc support.

This does not make the underlying finite-abelian-group algebra new; it sharpens the project interpretation of the already-computed obstruction spectrum.

## 10. Precision ladder after Stages 29, 33, and 34

For a declared certificate family the exact hierarchy is now:

\[
\boxed{
\text{certificate rational rank}
\to
\text{access image index }J_H(R)
\to
\text{complete image }C
\to
\text{intrinsic saturation index }\delta_H.
}
\]

The first coordinate asks how many rational certificate directions are visible. The second asks how much of the complete integer image has been generated at the current access radius. The last asks whether the complete certificate image itself fills its saturated labelled lattice.

No one of these coordinates generically determines the others.

## 11. Prior-art / ownership boundary

Lattice saturation, Smith normal form, determinantal divisors, finite subgroup index, and index multiplication are standard algebra. P025 claims no priority for them.

The reusable project-side finding is the **layering law** exposed by the abc/arithmetic-derivative pressure test:

- relation-state precision and declared certificate precision can complete at different radii;
- rational certificate rank and integral certificate completeness are different resources;
- finite-access defect and intrinsic certificate congruence defect factor multiplicatively;
- `eta_min` is the scalar normalized-Wronskian instance of the intrinsic certificate saturation defect.

This should be relayed to A3/P023 for mother-layer ownership review rather than promoted as an ABC-private foundational primitive.

## 12. Executable assets

Added:

- `src/enterprise_math/certificate_image_index.py`
  - maximal-minor saturation index;
  - radius-generated certificate image rank/index;
  - divisibility profile;
  - certificate-complete radius;
  - exact intrinsic/access defect factorization.
- `src/enterprise_math/abc_certificate_index.py`
  - normalized Wronskian image generator;
  - equality of `eta_min` and normalized scalar saturation index;
  - reconstruction of the local obstruction spectrum.
- `tests/test_certificate_image_index.py`;
- `tests/test_abc_certificate_index.py`.

## 13. Next frontier

No hard block exists. Continue with:

1. retain the **full finite defect group**, not only its cardinality `delta_H`, for multi-certificate languages;
2. distinguish equal-index but non-isomorphic congruence defects using Smith invariant factors;
3. define the radius-dependent finite certificate quotient once full certificate rank is reached;
4. compare certificate-complete radius with relation full-rank / generator radii in higher-rank examples;
5. route the resulting generic rank/index/saturation layering law to A3/P023 without duplicating standard Smith theory.
