# Native prime-power resultant law for spectral cyclotomic factors

Status: `FREE_RESEARCH / EXACT FINITE SPECTRAL ARITHMETIC THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- monic spectral factorization `Q_M=prod_(d|M,d>1) Psi_d`;
- finite scale cocycle;
- internal phase quantization at primitive roots.

This note upgrades the prime-power resultant pattern from a later classical compatibility observation to a proof route internal to the finite Dirichlet spectral family. No roots of unity or classical cyclotomic resultant theorem are needed.

## 1. Integer primitive factors

The monic length polynomial

\[
Q_M(u)=(-1)^{M-1}D_{M-1}(u)
\]

lies in `Z[u]` and factors as

\[
Q_M(u)=\prod_{\substack{d\mid M\\d>1}}\Psi_d(u),
\]

where every `Psi_d` is monic and its roots are the primitive denominator-`d` finite mode roots.

Inductively, each `Psi_d` also lies in `Z[u]`: all earlier primitive factors are monic integer divisors of the monic integer polynomial `Q_d`, so polynomial long division/Gauss integrality keeps integer coefficients.

Hence every pairwise resultant

\[
\operatorname{Res}(\Psi_m,\Psi_n)
\]

is an integer.  Distinct primitive root sets are disjoint, so for `m!=n` the resultant is nonzero and its absolute value is a positive integer.

## 2. Exact quotient along a scale multiple

Let

\[
N=mt.
\]

The normalized cocycle gives

\[
H_{mt}(u)=H_m(u)H_t(R_m(u)).
\]

Since

\[
Q_M=(-1)^{M-1}M H_M,
\]

we obtain the exact monic quotient identity

\[
\boxed{
\frac{Q_{mt}(u)}{Q_m(u)}
=(-1)^{mt-m}\,t\,H_t(R_m(u)).
}
\tag{NRL-1}
\]

The left side is a genuine polynomial because `Q_m|Q_(mt)`.

## 3. Evaluation at a primitive-m root

Let

\[
\alpha=u_{r,m}
\]

with `gcd(r,m)=1`.

Internal phase quantization gives

\[
\alpha=2-2C(r\tau/m).
\]

The `m`-fold decimation map multiplies phase by `m`, so

\[
R_m(\alpha)
=2-2C(r\tau).
\]

Internal phase periodicity gives

\[
C(r\tau)=(-1)^r.
\]

Therefore

\[
\boxed{
R_m(\alpha)
=\begin{cases}
0,&r\text{ even},\\
4,&r\text{ odd}.
\end{cases}
}
\tag{NRL-2}
\]

Now

\[
H_t(0)=1.
\]

Complement symmetry gives

\[
D_{t-1}(4)=(-1)^{t-1}D_{t-1}(0)=(-1)^{t-1}t,
\]

hence

\[
H_t(4)=(-1)^{t-1}.
\]

Thus in both cases

\[
\boxed{|H_t(R_m(\alpha))|=1.}
\tag{NRL-3}
\]

Combining with (NRL-1),

\[
\boxed{
\left|
\frac{Q_{mt}}{Q_m}(\alpha)
\right|=t.
}
\tag{NRL-4}
\]

## 4. Master resultant product identity

There are `phi(m)` primitive roots of `Psi_m`. Multiplying (NRL-4) over all of them gives

\[
\left|
\operatorname{Res}\left(
\Psi_m,
\frac{Q_{mt}}{Q_m}
\right)
\right|
=t^{\varphi(m)}.
\]

The primitive factorization of the quotient is

\[
\frac{Q_{mt}}{Q_m}
=
\prod_{\substack{d\mid mt\\d\nmid m}}
\Psi_d.
\]

Resultant multiplicativity therefore gives the master identity

\[
\boxed{
 t^{\varphi(m)}
=
\prod_{\substack{d\mid mt\\d\nmid m}}
\left|
\operatorname{Res}(\Psi_m,\Psi_d)
\right|.
}
\tag{NRL-5}
\]

Every factor on the right is a positive integer.

## 5. Multiple case: strong induction on t

Fix `m`.  We determine

\[
R_m(mt):=
|\operatorname{Res}(\Psi_m,\Psi_{mt})|
\]

by strong induction on `t>1`.

Assume the desired law is known for every proper multiplier `s<t`.

In (NRL-5), every divisor `d<mt` which is a multiple of `m` has the form

\[
d=ms
\]

for a proper divisor `s|t`.

By induction, its resultant is nontrivial exactly when

\[
s=p^a
\]

is a prime power, and then the value is

\[
p^{\varphi(m)}.
\]

All divisors `d` not divisible by `m` will be shown to contribute units in Section 7; alternatively they may be carried simultaneously in a double induction.

### t is a prime power

If

\[
t=p^a,
\]

the proper prime-power multipliers are

\[
p,p^2,\ldots,p^{a-1}.
\]

Their total contribution is

\[
p^{(a-1)\varphi(m)}.
\]

Since the left side of (NRL-5) is

\[
p^{a\varphi(m)},
\]

the remaining top factor must be

\[
\boxed{
R_m(mp^a)=p^{\varphi(m)}.
}
\tag{NRL-6}
\]

### t has at least two distinct prime factors

Write

\[
t=\prod_p p^{a_p}
\]

with at least two nonzero exponents.  The proper prime-power divisors of `t` include, for each `p`,

\[
p,p^2,\ldots,p^{a_p}.
\]

Their resultant contributions multiply to

\[
\prod_p p^{a_p\varphi(m)}
=t^{\varphi(m)},
\]

which already exhausts the entire left side of (NRL-5).

Since all remaining factors are positive integers,

\[
\boxed{
R_m(mt)=1
}
\tag{NRL-7}
\]

when `t` is not a prime power.

## 6. Aggregate contribution of all multiple-of-m new factors

The argument above also shows a useful stronger statement: for arbitrary `t`, the product of all new factors in (NRL-5) whose indices are multiples of `m` is exactly

\[
\boxed{t^{\varphi(m)}.}
\tag{NRL-8}
\]

Indeed each prime `p` appearing to exponent `a_p` contributes one factor `p^(phi(m))` at every prime-power level `p,...,p^(a_p)`, for total `p^(a_p phi(m))`.

Thus the multiple-of-`m` sector alone consumes the complete master resultant product.

## 7. Nonmultiple indices give unit resultants

Let `n>1` with `m` not dividing `n`, and set

\[
L=\operatorname{lcm}(m,n)=mt,
\qquad
 t=\frac{n}{\gcd(m,n)}.
\]

Then `n|L` but `n` does not divide `m`, so `Psi_n` appears among the new factors in the quotient `Q_L/Q_m`.

By (NRL-5), the product of all new resultant magnitudes is

\[
t^{\varphi(m)}.
\]

But Section 6 shows that the new factors whose indices are multiples of `m` already contribute exactly this full value.

All other new factors, including `Psi_n`, have positive-integer resultant magnitudes. Their product must therefore be one, forcing every one of them to be one.

Hence

\[
\boxed{
 m\nmid n
\quad\Longrightarrow\quad
|\operatorname{Res}(\Psi_m,\Psi_n)|=1.
}
\tag{NRL-9}
\]

## 8. Native spectral resultant theorem

Combining Sections 5 and 7, for `2<=m<n`,

\[
\boxed{
|\operatorname{Res}(\Psi_m,\Psi_n)|
=
\begin{cases}
 p^{\varphi(m)},& n/m=p^a\text{ for some prime }p,\\[1mm]
 1,&\text{otherwise}.
\end{cases}
}
\tag{NRL-10}
\]

By symmetry of absolute resultants, for arbitrary distinct `m,n>1`,

\[
\boxed{
|\operatorname{Res}(\Psi_m,\Psi_n)|
=
\begin{cases}
 p^{\varphi(\min(m,n))},&
 \max(m,n)/\min(m,n)=p^a,\\[1mm]
 1,&\text{otherwise}.
\end{cases}
}
\tag{NRL-11}
\]

The quotient in the first case is understood to be an integer prime power.

## 9. Sign

The native argument above determines the absolute value. The sign depends on the chosen monic root ordering/orientation conventions and is not needed for the prime-power arithmetic statement.

Exact symbolic examples include both signs:

```text
Res(Psi_2,Psi_4) = -2
Res(Psi_3,Psi_9) =  9
Res(Psi_3,Psi_15)= -25
```

The invariant arithmetic content is (NRL-11).

## 10. Relation to classical cyclotomic theory

A separate classical trace-compatibility theorem identifies the spectral primitive factors with real trace transforms of ordinary cyclotomic factors. Under that compatibility, (NRL-11) maps to the classical Apostol prime-power cyclotomic resultant law.

But the proof above uses only:

```text
finite monic spectral factorization
+ finite scale cocycle
+ internal primitive phase quantization
+ integer resultant multiplicativity
+ strong induction / lcm
```

Therefore the prime-power resultant law is already a finite spectral arithmetic theorem before root-of-unity naming.

Freeze:

`SPECTRAL_PRIMITIVE_RESULTANT_PRIME_POWER_LAW = NATIVE_FINITE_ARITHMETIC`.

The classical cyclotomic resultant theorem is now a compatibility image, not a proof input.
