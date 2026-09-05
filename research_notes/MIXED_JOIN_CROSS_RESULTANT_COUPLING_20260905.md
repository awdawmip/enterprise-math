# Cross-resultant coupling of the mixed spectral join defect

Status: `FREE_RESEARCH / EXACT FINITE-ALGEBRA THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- divisor spectral embedding `Q_n`;
- pairwise join-defect polynomial;
- native primitive resultant law;
- normalized scale cocycle.

## 1. Reduced pair and ancestral sectors

Let

\[
g=(m,n),\qquad
m=ga,\qquad
n=gb,\qquad(a,b)=1.
\]

Let

\[
L=[m,n]=gab.
\]

Define the two sectors which are present on one side but not already in the gcd sector:

\[
\boxed{
A_{m|g}(u):=\frac{Q_m(u)}{Q_g(u)},
\qquad
B_{n|g}(u):=\frac{Q_n(u)}{Q_g(u)}.
}
\tag{MJC-1}

They are monic integral polynomials of degrees

\[
\deg A_{m|g}=m-g,
\qquad
\deg B_{n|g}=n-g.
\]

The mixed join defect is

\[
\boxed{
\mathcal J_{m,n}(u)
=\frac{Q_L(u)Q_g(u)}{Q_m(u)Q_n(u)}.
}
\tag{MJC-2}

Equivalently,

\[
\frac{Q_L}{Q_m}=B_{n|g}\,\mathcal J_{m,n},
\qquad
\frac{Q_L}{Q_n}=A_{m|g}\,\mathcal J_{m,n}.
\tag{MJC-3}

## 2. The two exclusive ancestral sectors are resultant units

Every primitive factor of `A_(m|g)` has denominator `d|m` with `d\nmid g`; every primitive factor of `B_(n|g)` has denominator `e|n` with `e\nmid g`.

If `e/d` or `d/e` were an integer prime power, the smaller denominator would divide both `m` and `n`, hence divide `g`, contradicting its sector definition.

Thus every primitive cross-resultant is a unit.  Therefore

\[
\boxed{
|\operatorname{Res}(A_{m|g},B_{n|g})|=1.
}
\tag{MJC-4}

So the two exclusive ancestral sectors are integrally comaximal before the mixed join factor is inserted.

## 3. Scale quotient over the m-side

Since

\[
L=mb,
\]

the normalized scale cocycle gives

\[
\frac{Q_L(u)}{Q_m(u)}
=\pm b\,H_b(R_m(u)).
\tag{MJC-5}

At every root `alpha` of `Q_m`,

\[
R_m(\alpha)\in\{0,4\},
\]

and

\[
|H_b(0)|=|H_b(4)|=1.
\]

Hence at every root of the subfactor `A_(m|g)` as well,

\[
\left|\frac{Q_L}{Q_m}(\alpha)\right|=b.
\]

There are `m-g` such roots, so

\[
\boxed{
\left|
\operatorname{Res}
\left(A_{m|g},\frac{Q_L}{Q_m}\right)
\right|
=b^{m-g}.
}
\tag{MJC-6}

Using (MJC-3) and multiplicativity,

\[
\left|
\operatorname{Res}(A_{m|g},B_{n|g})
\right|
\cdot
|\operatorname{Res}(A_{m|g},\mathcal J_{m,n})|
=b^{m-g}.
\]

Apply (MJC-4):

\[
\boxed{
|\operatorname{Res}(A_{m|g},\mathcal J_{m,n})|
=b^{m-g}
=\left(\frac ng\right)^{m-g}.
}
\tag{MJC-7}

## 4. Symmetric n-side formula

Interchanging `m,n`,

\[
\boxed{
|\operatorname{Res}(B_{n|g},\mathcal J_{m,n})|
=a^{n-g}
=\left(\frac mg\right)^{n-g}.
}
\tag{MJC-8}

Therefore the mixed factor stores the opposite reduced scale through cross-resultant coupling:

\[
\boxed{
|\operatorname{Res}(A_{m|g},\mathcal J)|^{1/(m-g)}
=\frac ng,
}
\tag{MJC-9}

\[
\boxed{
|\operatorname{Res}(B_{n|g},\mathcal J)|^{1/(n-g)}
=\frac mg.
}
\tag{MJC-10}

## 5. Coprime specialization

If `(m,n)=1`, then `g=1`, `Q_g=1`, and

\[
A_{m|g}=Q_m,
\qquad
B_{n|g}=Q_n.
\]

Thus

\[
\boxed{
|\operatorname{Res}(Q_m,\mathcal J_{m,n})|
=n^{m-1},
}
\tag{MJC-11}

\[
\boxed{
|\operatorname{Res}(Q_n,\mathcal J_{m,n})|
=m^{n-1}.
}
\tag{MJC-12}

Example: `m=3,n=5` has `J_(3,5)=Psi_15` and

\[
|\operatorname{Res}(\Psi_3,\Psi_{15})|=5^2=25.
\]

## 6. Mixed information is relational rather than endpoint mass

The earlier join theorem gives

\[
|\mathcal J_{m,n}(0)|=|\mathcal J_{m,n}(4)|=1
\]

for incomparable `m,n`, while its reciprocal moments are strictly positive.

Now (MJC-7)--(MJC-8) add a third independent observer:

```text
self endpoint mass of mixed factor:
    1

internal reciprocal moments:
    positive

cross resultant against m-exclusive ancestral sector:
    (n/g)^(m-g)

cross resultant against n-exclusive ancestral sector:
    (m/g)^(n-g)
```

So the mixed factor is mass-neutral at the endpoints but carries exact relational scale coupling to both parents.

This is a finite algebraic example of

`SELF_MASS != INTERNAL_SUPPORT != CROSS_RELATIONAL_COUPLING`.

## 7. Boundary on a stronger module claim

Exact computations suggest a possible stronger statement that, in the quotient order by `A_(m|g)`, the class of `J_(m,n)` may be associated to the integer `b=n/g`, with a symmetric statement on the other side.  That would upgrade (MJC-7) from determinant magnitude to a flat `Z/bZ` Smith layer.

This stronger element-level claim is **not frozen here**; (MJC-7)--(MJC-10) are the currently justified theorem-candidate statements.

Freeze:

`EXCLUSIVE_ANCESTRAL_SECTORS = RESULTANT_COMAXIMAL`.

`MIXED_JOIN_CROSS_RESULTANT = OPPOSITE_REDUCED_SCALE^ANCESTRAL_RANK`.

`MIXED_ENDPOINT_MASS_1 != MIXED_RELATIONAL_COUPLING_TRIVIAL`.
