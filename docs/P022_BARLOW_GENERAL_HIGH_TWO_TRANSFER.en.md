# P022 Barlow — General simple-high two-transfer reduction

Status: **owner-branch research theorem + pressure frontier / not canonical**

This note records the current reduction of the deep secondary-quadratic
`quotient-zero / simple-high` branch.  It generalizes the already closed
`source-high` case without claiming that the resulting coprimality pattern is
proved uniformly.

## 1. Setup

Let `q` be a Franel prime primitive at a nontrivial twin center `r`, and suppose
complete defect escape has passed the first terminal collision and the seven-rank
barrier.  The secondary quadratic index is

\[
Q=2(2r-3)^2=8r^2-24r+18.
\]

In the quotient-zero branch write

\[
Q=a q+b,
\qquad a=r+h,
\]

and suppose the high digit `a` is another **simple** hidden Franel zero.  Since
both `r` and `a` are nontrivial twin centers,

\[
3\mid r,\qquad 3\mid h.
\]

Minimal two-digit saturation from the existing P022 theorem then forces the low
digit `b` to be a zero as well.

Define

\[
q=8(r-h)-1-c.
\]

## 2. The c-window has real width below six

Substituting the affine expression for `q` into `Q=(r+h)q+b` gives

\[
b=r(c-23)+h(c+1)+8h^2+18.
\]

The reflection-symmetric primitive band

\[
r\le b\le q-1-r
\]

is therefore exactly

\[
\left\lceil
\frac{24r-8h^2-h-18}{r+h}
\right\rceil
\le c\le
\left\lfloor
\frac{30r-8h^2-9h-20}{r+h+1}
\right\rfloor.
\]

Before taking floors/ceilings, the width is

\[
\frac{6r^2-2hr-26r-h+18}{(r+h)(r+h+1)}<6,
\]

because subtracting the numerator from six times the denominator gives

\[
6h^2+14hr+7h+32r-18>0.
\]

Since `r-h` is divisible by three,

\[
q\equiv-1-c\pmod{24}.
\]

Hence the forced-midpoint target classes `q=5,23 (mod 24)` require respectively

\[
c\equiv18\pmod{24},
\qquad
c\equiv0\pmod{24}.
\]

The union of these two residue lattices has minimum spacing six.  Therefore the
strictly-sub-six c-window contains **at most one** target value.  For each fixed
`(r,h)`, the forced prime candidate is unique if it exists.

## 3. First fixed transfer: the hidden high zero

Modulo the affine candidate `q`,

\[
8r\equiv 8h+c+1,
\]

so the moving source parameter reduces to

\[
\rho=h+\frac{c+1}{8}.
\]

Let `H_j(x)` be the normalized forward Franel transfer with

\[
H_0(x)=0,\qquad H_1(x)=1,
\]

and

\[
(x+j)^2H_j(x)
=
\bigl(7(x+j-1)^2+7(x+j-1)+2\bigr)H_{j-1}(x)
+8(x+j-1)^2H_{j-2}(x).
\]

The two single-digit zeros at `r` and `r+h` therefore force

\[
\boxed{
q\mid C_1(h,c):=\operatorname{num}H_h(\rho).
}
\]

Crucially, `C_1` depends only on `(h,c)`, not on `r`.

## 4. Second fixed transfer: the universal quadratic pair

Complete escape also forces the universal quadratic transported zeros

\[
K_-=2(r-1)^2,
\qquad
K_+=2(r+1)^2-1.
\]

Put

\[
\delta=8h+c=8\rho-1,
\qquad
x=2(\rho-1)^2=\frac{(\delta-7)^2}{32}.
\]

Then

\[
K_-\equiv x\pmod q,
\qquad
K_+-K_-=8r-1\equiv\delta\pmod q.
\]

The seven-rank barrier gives

\[
0<\delta<r.
\]

If both quadratic remainders lie in the symmetric primitive band, the wrapped
alternative `delta-q` is larger in absolute value than the entire band.
Consequently their **actual** difference is exactly

\[
\boxed{b_+-b_-=\delta.}
\]

The second zero pair therefore forces another fixed transfer

\[
\boxed{
q\mid C_2(h,c):=\operatorname{num}H_\delta(x).
}
\]

Thus every complete simple-high escape branch must satisfy

\[
\boxed{q\mid\gcd(C_1(h,c),C_2(h,c)).}
\]

This is the general form of the fixed-transfer mechanism that closed the
special source-high branch by the coprime `C18/C24` pair.

## 5. Correct conjecture boundary

The tempting universal statement

\[
\gcd(C_1(h,c),C_2(h,c))=1
\]

is **false**.

The first exact counterexample found in the broad forced-residue parameter scan
is

\[
(h,c)=(51,-120),
\qquad
\gcd(C_1,C_2)=701.
\]

However this common factor is arithmetically incompatible with the branch:
`c=-120=0 (mod 24)` requires `q=23 (mod 24)`, whereas

\[
701\equiv5\pmod{24}.
\]

Therefore the surviving candidate law is weaker and better aligned with the
actual Barlow problem:

> **Compatible-common-prime conjecture.**  No prime divisor common to
> `C_1(h,c)` and `C_2(h,c)` lies in the forced residue class
> `q=-1-c (mod 24)` for an admissible simple-high branch.

This is not proved universally.

## 6. Pressure evidence

An exact rational-recurrence scan was performed on the deliberately broad
necessary parameter box

\[
3\le h\le90,\qquad 3\mid h,
\]

\[
-8h<c<30,
\qquad c\equiv0\text{ or }18\pmod{24}.
\]

This contains **990** `(h,c)` patterns, including many that are not realized by
an actual twin/prime `r` and is therefore a stronger pressure box than the
arithmetic candidate set.

Result:

- 989 pairs had `gcd(C_1,C_2)=1`;
- the sole nontrivial gcd was `(51,-120)` with gcd `701`;
- **zero** pairs had a common prime compatible with the branch-required
  `q (mod 24)` class.

This is pressure evidence only, not a proof for unbounded `h`.

## 7. Deep branch is now a separate multiple-root problem

The p-square reflection theorem gives, for a deep digit zero `a` and
`a^vee=q-1-a`,

\[
(-8)^a\frac{F_{a^\vee}}q\equiv-F'_a\pmod q.
\]

Therefore a deep digit has a simple mirror whenever `F'_a` is nonzero, while a
deep/deep reflected pair occurs exactly on the single-digit multiple-root
locus

\[
F_a\equiv F'_a\equiv0\pmod q.
\]

So arbitrary higher q-adic depth no longer needs to remain an undifferentiated
branch.  The unresolved deep arithmetic is concentrated in that multiple-root
locus plus the task of routing a transverse deep zero through its simple
mirror.

## 8. Current frontier

The source-high line `a=r` is already closed exactly by the existing coprime
18-step/24-step theorem.  The remaining simple-high problem is now a family of
finite two-transfer certificates indexed by `(h,c)` with at most one forced q
candidate for each `(r,h)`.

The shortest next target is to prove the compatible-common-prime conjecture,
or to derive a recurrence/Casoratian relation that bounds the common prime
support of `C_1(h,c),C_2(h,c)` uniformly.  Independently, the deep branch should
be attacked through single-digit multiple-root exclusion rather than generic
p^3 valuation casework.
