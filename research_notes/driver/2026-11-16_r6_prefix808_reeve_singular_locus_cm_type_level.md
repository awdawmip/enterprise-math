# PREFIX-808 Reeve saturation: smooth locus, Cohen–Macaulay type and level canonical module

Date: 2026-11-16 (Asia/Taipei). **New author-side mathematical extension** by RESEARCH_DRIVER `EM-DVR-DEBB5E`, in a source-exposed context; not an independent Native Result review. The original named-source PREFIX-808 construction is credited to `EM-DIRECT-4660FF`. No operational X6/signed-Port/Link correspondence is asserted.

## Exact input and source pins

For every integer `h >= 2` and any field `K`, use the **already-proved** semigroup algebra `S=K[C_h]` from the Reeve observation model, finite free of rank `h` over `R=K[U0,U1,U2,U3]`. All `U_i` have degree one. Its homogeneous `R`-basis is `1,V1,...,V_(h-1)`, with `deg(V_r)=2`. Write `A=U1 U2` and `B=U0 U3`; the multiplication table is

```text
Vr Vs = A V_(r+s)    for r+s<h,
      = A B          for r+s=h,
      = B V_(r+s-h)  for r+s>h.
```

Exact inherited sources:

- Finite-free presentation and proof: `research_notes/driver/2026-11-16_r6_prefix808_reeve_saturation_free_module_and_exact_multiplication.md`, commit `ebd02fad57e4ca25052749afdcb9bada7940b329`, Git blob `03e46deb12303dc8dedfb39651ffb4460a653779`.
- Complete geometric-fiber classification: `research_notes/driver/2026-11-16_r6_prefix808_reeve_finite_flat_geometric_fibers_and_wild_strata.md`, commit `6065e5fa6e6617e34caaf299794b84a0486f1f2d`, Git blob `fccf40a76a1cd867b6ffaa5d65bb4b460618e666`.

This note concerns the absolute source variety `Spec S`, which must be distinguished from the morphism `Spec S -> Spec R` being étale.

## Theorem 1: exact absolute geometric singular support

Over an algebraic closure of `K` (equivalently, as a geometric singular-support assertion over `K`), the singular points of `Spec S` are **exactly** the inverse image of the locus of the base where at least two of `U0,U1,U2,U3` vanish:

```text
Sing(Spec S) = f^(-1)( union_{0<=i<j<=3} V(Ui,Uj) )
```

where this equality is about the underlying geometric point sets (not the scheme structure of a Jacobian ideal). This holds for `h>=2` in **every characteristic**.

In particular, even when `char(K)` divides `h` and `f` is nowhere étale, the source `Spec S` is smooth on a nonempty dense open subset; being non-étale over the base is **not** the same as absolute singularity.

### Proof

1. On `D(A)`, put `T=V1/A`. The inherited exact free presentation yields
   `S[A^(-1)] = R[A^(-1)][T]/(T^h-B/A)`.
   If `U0,U1,U2` are invertible, solve `U3=(U1 U2/U0)T^h`. This identifies that chart of `Spec S` with `G_m^3 x A^1` using `U0,U1,U2,T`. It is smooth in all characteristics. In particular it includes all points above base points where only `U3` vanishes. Similarly, after also inverting `U3`, solve for `U0`; this covers the case where only `U0` vanishes. The symmetric `D(B)` chart with `W=V_(h-1)/B`, `W^h=A/B`, handles a sole zero of `U1` or `U2`. Therefore the complement of the claimed pairwise-zero locus is smooth.

2. Suppose `U0=U3=0`, `A != 0` at a geometric point. The `D(A)` presentation is one hypersurface in a smooth five-dimensional ambient chart:
   `F=T^h-U0 U3/A`. Since the fiber has `T=0`, every first derivative of `F` vanishes at that point: `h T^(h-1)=0` for `h>=2`, and all derivatives of `U0 U3/A` vanish. Its tangent dimension is five, while its local dimension is four. Thus it is singular. The same argument using `W` treats `U1=U2=0`, `B != 0`.

3. Suppose `A=B=0`. Every `V_r` vanishes at every geometric point of the fiber because the fiber algebra is the square-zero algebra on the `V_r`. Present `S` as the quotient of `K[U0,U1,U2,U3,V1,...,V_(h-1)]` by the pair-product equations in the multiplication table. This presentation is exact: pair products reduce every polynomial to an `R`-linear combination of `1,V_r`, and freeness shows no additional linear relations. At the point, the first derivatives of every defining relation vanish: `V_r=0`, `A=B=0`, and `d(AB)=A\,dB+B\,dA=0`. Hence the geometric tangent space has dimension `4+(h-1)=h+3>4`, so the point is singular.

The cases cover every point with at least two vanishing base coordinates. The finite free extension has Krull dimension four throughout. QED.

## Theorem 2: exact Cohen–Macaulay type and level property

The positively graded `K`-algebra `S` is a four-dimensional **normal Cohen–Macaulay** domain. Its Hilbert series and graded canonical module as an `R`-module are

```text
Hilb_S(t) = (1+(h-1)t^2)/(1-t)^4,

omega_S = Hom_R(S,R(-4))  ~=  R(-4) (+) R(-2)^(h-1)
          (the displayed direct sum is as graded R-modules).
```

At the homogeneous maximal ideal `m=(U0,U1,U2,U3,V1,...,V_(h-1))`, the Cohen–Macaulay type is exactly `h-1`. Moreover, `S` is a **level algebra**, with `omega_S` minimally generated over `S` by `h-1` homogeneous elements, all of degree two (equivalently the standard graded Artin reduction has socle concentrated in degree two). Consequently,

```text
S is Gorenstein  <=>  h=2,       for h>=2.
a(S)=-2.
```

### Proof

The monoid `C_h = cone(u0,u1,u2,u3) intersect Z^4` is saturated in the ambient lattice, so the standard normality theorem for affine semigroup rings makes `S=K[C_h]` normal and a domain. Alternatively, the normality conclusion can be separated from the remaining CM/type proof if only the finite-free algebra presentation is available. As an `R`-free module, `S` has basis degrees `0,2,...,2`; the displayed Hilbert series follows immediately. The four variables `U_i` form a homogeneous `S`-regular sequence, and `S/(U0,U1,U2,U3)` has finite length `h`. Hence `S` is Cohen–Macaulay of dimension four.

Modulo all `U_i`, the multiplication table becomes

```text
S/(U0,U1,U2,U3)
 = K (+) K V1 (+) ... (+) K V_(h-1),
(V1,...,V_(h-1))^2 = 0.
```

Its socle is exactly the span of `V1,...,V_(h-1)`, of dimension `h-1`, entirely in degree two. The Cohen–Macaulay type at `m` equals this socle dimension. Since that socle is concentrated in a single degree, the standard graded Cohen–Macaulay ring is level. The graded finite-duality formula `omega_S=Hom_R(S,omega_R)` with `omega_R=R(-4)` proves the displayed canonical module decomposition as graded `R`-modules. Its minimal `S`-generator degrees are two, matching the Artin-reduction socle degrees. The Hilbert numerator has degree two, so `a(S)=2-4=-2`.

A Cohen–Macaulay ring is Gorenstein only if every relevant local type is one. When `h>=3`, the type at `m` is `h-1>1`, so `S` is not Gorenstein. When `h=2`, the multiplication table gives the hypersurface
`S=K[U0,U1,U2,U3,V1]/(V1^2-U0U1U2U3)`, which is Gorenstein in every characteristic. QED.

## Scope / new information

The preceding fiber and discriminant study classified the **relative** failure of étaleness. This result separately classifies **absolute** singular support, proves normality/CM/type/level properties and gives a sharp Gorenstein dichotomy; it does not use a numerical test as a universal proof. An independently authorized reviewer must still assess the complete source dependencies before Native Result admission. Nothing here marks the PREFIX-808 mother Task complete or identifies its abstract observer semigroup with native signed X6/Port/Link updates.
