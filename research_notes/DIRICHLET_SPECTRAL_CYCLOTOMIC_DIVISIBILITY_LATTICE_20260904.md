# Spectral cyclotomic divisibility lattice for finite Dirichlet chains

Status: `FREE_RESEARCH / EXACT FINITE POLYNOMIAL ARITHMETIC / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on the primitive denominator decomposition and internal phase quantization.

## 1. Monic length polynomial

Define

\[
\boxed{
Q_M(u):=(-1)^{M-1}D_{M-1}(u).
}
\tag{SCD-1}
\]

This is the monic characteristic polynomial of the length-`M` finite Dirichlet chain, of degree `M-1`.

Its roots are the strictly ordered finite mode roots

\[
u_{1,M},\ldots,u_{M-1,M}.
\]

## 2. Primitive spectral polynomial

For every `d>1`, define the monic primitive spectral polynomial

\[
\boxed{
\Psi_d(u)
:=
\prod_{\substack{1\le r<d\\\gcd(r,d)=1}}
(u-u_{r,d}).
}
\tag{SCD-2}
\]

There are `phi(d)` primitive residues, so

\[
\boxed{\deg\Psi_d=\varphi(d).}
\tag{SCD-3}
\]

The root sets of `Psi_d` and `Psi_e` are disjoint for `d\ne e`: equality of two mode roots in the first completion phase forces equality of their reduced phase fractions, hence equality of reduced denominators.

Therefore the primitive factors are pairwise coprime.

## 3. Spectral cyclotomic factorization

Every mode fraction `k/M` has a unique reduced denominator `d|M`, `d>1`. Consequently the complete root set decomposes disjointly into primitive denominator root sets.

Both sides below are monic and have the same roots with multiplicity one, hence

\[
\boxed{
Q_M(u)
=
\prod_{\substack{d\mid M\\d>1}}
\Psi_d(u).
}
\tag{SCD-4}
\]

The degree identity is Euler's divisor sum

\[
\sum_{d\mid M}\varphi(d)=M,
\]

with the `d=1` term accounting for the missing zero/boundary mode.

This is the finite Dirichlet spectral analogue of a cyclotomic factorization.

## 4. Divisibility follows integer divisibility

If `m|n`, every divisor of `m` is a divisor of `n`. By (SCD-4),

\[
\boxed{Q_m\mid Q_n.}
\tag{SCD-5}
\]

The same result follows directly from the exact finite scale cocycle

\[
H_n=H_m(H_{n/m}\circ R_m)
\]

up to the harmless monic normalization.

## 5. Converse divisibility

Assume `m>=2` and

\[
Q_m\mid Q_n.
\]

Then the smallest mode root `u_(1,m)` of `Q_m` is also a root of `Q_n`. Hence for some `1<=k<n`,

\[
u_{1,m}=u_{k,n}.
\]

Using the internal phase formula

\[
u_{r,M}=2-2C(r\tau/M),
\]

and strict decrease of `C` on `(0,tau)`, equality of roots forces

\[
\frac1m=\frac{k}{n}.
\]

Thus

\[
n=km,
\]

so

\[
\boxed{m\mid n.}
\tag{SCD-6}
\]

Combining (SCD-5) and (SCD-6):

\[
\boxed{
Q_m\mid Q_n
\iff
m\mid n.
}
\tag{SCD-7}
\]

The polynomial divisibility poset of the finite spectral family faithfully embeds the ordinary integer divisibility poset.

## 6. Exact polynomial gcd law

Let

\[
g=\gcd(m,n).
\]

By primitive factorization, the common primitive factors of `Q_m` and `Q_n` are exactly those `Psi_d` with

\[
d\mid m,\qquad d\mid n,
\]

i.e. exactly `d|g`.

Therefore the monic gcd is

\[
\boxed{
\gcd(Q_m,Q_n)=Q_g.
}
\tag{SCD-8}
\]

In particular,

\[
\boxed{
Q_m\text{ and }Q_n\text{ are coprime}
\iff
\gcd(m,n)=1.
}
\tag{SCD-9}
\]

## 7. Primitive factor divisibility criterion

Equation (SCD-4) also gives

\[
\boxed{
\Psi_d\mid Q_M
\iff
d\mid M.
}
\tag{SCD-10}
\]

Thus each primitive spectral polynomial is a precise divisor detector for finite chain length.

This mirrors the defining divisibility role of classical cyclotomic factors, but it was obtained from reduced finite mode phases and the native Dirichlet characteristic family.

## 8. Constant term / primitive mass

The absolute root product of `Psi_d` is the primitive spectral mass

\[
P_d
=
\prod_{\substack{1\le r<d\\(r,d)=1}}u_{r,d}.
\]

The earlier Möbius theorem gives

\[
P_d
=\begin{cases}
p,&d=p^a,\\1,&\omega(d)\ge2.\end{cases}
\]

Therefore, for `d>2` where `phi(d)` is even,

\[
\boxed{
\Psi_d(0)
=
\begin{cases}
p,&d=p^a,\\1,&\omega(d)\ge2.\end{cases}
}
\tag{SCD-11}
\]

For `d=2`, `Psi_2(u)=u-2`, so `Psi_2(0)=-2`; the absolute root mass remains `2`.

## 9. Complement symmetry of primitive factors

The reduced primitive residue set is closed under

\[
r\mapsto d-r.
\]

Internal phase reflection gives

\[
u_{d-r,d}=4-u_{r,d}.
\]

Thus

\[
\boxed{
\Psi_d(4-u)
=(-1)^{\varphi(d)}\Psi_d(u).
}
\tag{SCD-12}
\]

For every `d>2`, `phi(d)` is even, hence

\[
\boxed{\Psi_d(4-u)=\Psi_d(u).}
\tag{SCD-13}
\]

So every nontrivial primitive spectral factor beyond `d=2` is centered-symmetric about `u=2`, and can be written as a polynomial in `(u-2)^2`.

## 10. Research consequence

The finite Dirichlet characteristic family carries a full divisor algebra:

```text
integer length M
  -> monic spectral polynomial Q_M
  -> primitive factors Psi_d indexed by divisors d
  -> Q_M = prod_(d|M,d>1) Psi_d
  -> Q_m | Q_n iff m | n
  -> gcd(Q_m,Q_n)=Q_gcd(m,n)
```

This is stronger than merely observing that the roots have a classical cosine formula.

Freeze:

`INTEGER_DIVISIBILITY = SPECTRAL_POLYNOMIAL_DIVISIBILITY`.

`INTEGER_GCD = MONIC_SPECTRAL_POLYNOMIAL_GCD`.

`PRIMITIVE_DENOMINATOR_FACTORS = SPECTRAL_CYCLOTOMIC_FACTORS`.
