# Finite parity spectral moments and the Dirichlet eta completion

Status: `FREE_RESEARCH / EXACT FINITE-PARITY + ANALYTIC-COMPLETION THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- full finite reciprocal spectral moments `Z_s(M)=P_s(M^2)`;
- exact even-site decimation;
- odd/even root-product determinant laws.

## 1. Signed parity reciprocal moment

For even length `M=2q`, define

\[
\boxed{
\mathfrak E_s(2q)
:=\sum_{k=1}^{2q-1}(-1)^{k-1}u_{k,2q}^{-s},
\qquad s\ge1.
}
\tag{PSE-1}

Odd mode indices enter positively and even mode indices negatively.  This is a signed reflection-parity observable, not a positive mass.

## 2. Exact finite decimation identity

For even mode index `k=2r`, internal phase quantization gives

\[
u_{2r,2q}=u_{r,q}.
\]

Hence

\[
\sum_{r=1}^{q-1}u_{2r,2q}^{-s}=Z_s(q).
\]

The odd-mode reciprocal sum is the full sum minus the even contribution:

\[
\sum_{k\text{ odd}}u_{k,2q}^{-s}=Z_s(2q)-Z_s(q).
\]

Therefore

\[
\boxed{
\mathfrak E_s(2q)
=Z_s(2q)-2Z_s(q).
}
\tag{PSE-2}

This is an exact finite spectral identity.

## 3. Closed polynomial form

The full moment is

\[
Z_s(M)=P_s(M^2)
\]

for a universal rational degree-`s` polynomial `P_s`.  Thus

\[
\boxed{
\mathfrak E_s(2q)
=P_s(4q^2)-2P_s(q^2).
}
\tag{PSE-3}

If

\[
P_s(X)=a_{s,0}+\sum_{r=1}^{s}a_{s,r}X^r,
\]

then

\[
\boxed{
\mathfrak E_s(2q)
=-a_{s,0}
+\sum_{r=1}^{s}a_{s,r}(4^r-2)q^{2r}.
}
\tag{PSE-4}

Examples:

\[
\boxed{
\mathfrak E_1(2q)=\frac{2q^2+1}{6}.
}
\]

Using

\[
P_2(X)=\frac{2X^2+5X-7}{180},
\]

\[
\boxed{
\mathfrak E_2(2q)
=\frac{28q^4+10q^2+7}{180}.
}
\]

## 4. Scaling limit gives Dirichlet eta

Recall

\[
\rho_{k,M}=M\sqrt{u_{k,M}}.
\]

Therefore

\[
(2q)^{-2s}\mathfrak E_s(2q)
=
\sum_{k=1}^{2q-1}
\frac{(-1)^{k-1}}{\rho_{k,2q}^{2s}}.
\]

For fixed `k`,

\[
\rho_{k,2q}\to k\tau,
\]

and the intrinsic bound `rho>=2k` gives absolute domination by `(2k)^(-2s)`.

Hence

\[
\boxed{
(2q)^{-2s}\mathfrak E_s(2q)
\longrightarrow
\frac{\eta(2s)}{\tau^{2s}},
}
\tag{PSE-5}

where

\[
\eta(2s)=\sum_{k\ge1}\frac{(-1)^{k-1}}{k^{2s}}.
\]

## 5. Polynomial leading term gives the eta/zeta factor

Let `beta_s=a_(s,s)` be the leading coefficient of `P_s`.  From (PSE-3),

\[
(2q)^{-2s}\mathfrak E_s(2q)
\longrightarrow
\beta_s\left(1-2^{1-2s}\right).
\]

But the independent full moment limit gives

\[
\zeta(2s)=\beta_s\tau^{2s}.
\]

Therefore

\[
\boxed{
\eta(2s)
=\left(1-2^{1-2s}\right)\zeta(2s).
}
\tag{PSE-6}

The classical eta factor is thus the scaling shadow of exact finite even/odd spectral decimation.

## 6. Parity spectral zeta polynomial

For each finite even length, define the entire finite exponential sum

\[
\Xi_{2q}(z)
:=\sum_{k=1}^{2q-1}(-1)^{k-1}e^{-z\log u_{k,2q}}.
\]

For positive integer `s`,

\[
\Xi_{2q}(s)=\mathfrak E_s(2q).
\]

At `z=0`, the value is merely the parity count difference.  The first derivative instead records the signed log determinant:

\[
-\Xi_{2q}'(0)
=\sum_{k=1}^{2q-1}(-1)^{k-1}\log u_{k,2q}.
\]

The exact parity root products are

\[
\prod_{k\text{ odd}}u_{k,2q}=2,
\qquad
\prod_{k\text{ even}}u_{k,2q}=q.
\]

Hence

\[
\boxed{
-\Xi_{2q}'(0)=\log\frac2q.
}
\tag{PSE-7}

So the Wallis parity determinant and the positive-integer eta moments are two jets/values of one finite signed spectral-zeta observable.

The logarithm is a derived readout; the native determinant ratio itself remains rational/algebraic.

## 7. Relation to Wallis

The original #1159 Wallis carrier separated even and odd reflection sectors and used their determinant ratio.  The present theorem shows that the same finite sector splitting controls the entire reciprocal-moment hierarchy:

```text
s=0 derivative / determinant jet:
    odd-vs-even root product
    -> Wallis parity determinant

s=1,2,... reciprocal moments:
    odd-vs-even signed spectral sums
    -> eta(2s) completion
```

Thus Wallis parity is not only a product-level phenomenon; it extends to a full finite signed spectral-moment family.

## 8. Typing

The signed parity observable is not reducible to positive mass.  If the reflection sign is erased, `mathfrak E_s` collapses to the full positive moment `Z_s` and the eta factor `1-2^(1-2s)` disappears.

Freeze:

`WALLIS_PARITY_DETERMINANT = z_EQ_0 LOG-JET OF FINITE PARITY SPECTRAL ZETA`.

`DIRICHLET_ETA_EVEN_VALUES = POSITIVE-INTEGER MOMENTS OF SAME PARITY OBSERVER`.

`EVEN_SITE_DECIMATION -> ETA/ZETA FACTOR`.
