# Spectral denominator Frobenius and the Jordan-weight intertwiner

Status: `FREE_RESEARCH / EXACT FINITE+FORMAL THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- internal phase quantization of finite Dirichlet roots;
- integer decimation semigroup `R_n`;
- primitive denominator factorization;
- common formal phase `ell`.

## 1. Denominator transition under integer decimation

Let a primitive denominator-`e` mode be represented by a reduced phase fraction `r/e`, with `gcd(r,e)=1`.

Under `R_n`, phase multiplication sends

`r/e -> nr/e`.

After reduction, the new denominator is

\[
\boxed{
\frac{e}{\gcd(e,n)}.
}
\tag{DF-1}
\]

The key point is that `gcd(r,e)=1`, so

`gcd(nr,e)=gcd(n,e)`.

Thus the denominator transition depends only on `(e,n)`, not on the primitive numerator.

---

## 2. Exact primitive-factor pullback law

Let `widehatPsi_d(u)` denote the primitive denominator-`d` spectral factor normalized by

\[
\widehat\Psi_d(0)=1.
\]

For every `d>1` and `n>=1`, the roots of

\[
\widehat\Psi_d(R_n(u))
\]

are exactly the primitive roots whose denominator `e` satisfies

\[
\frac{e}{\gcd(e,n)}=d.
\]

All these roots are simple: a critical point of `R_n` maps to an endpoint `0` or `4`, whereas primitive denominator roots lie in the open spectral interval `(0,4)`.

Both sides have constant term one, hence

\[
\boxed{
\widehat\Psi_d(R_n(u))
=
\prod_{\substack{e>1\\e/\gcd(e,n)=d}}
\widehat\Psi_e(u).
}
\tag{DF-2}
\]

The finite degree identity behind completeness is

\[
\boxed{
\sum_{e/\gcd(e,n)=d}\varphi(e)
=n\varphi(d).
}
\tag{DF-3}
\]

For a prime `p`, (DF-2) simplifies to

\[
\boxed{
\widehat\Psi_d(R_p)
=
\begin{cases}
\widehat\Psi_{pd},&p\mid d,\\
\widehat\Psi_d\widehat\Psi_{pd},&p\nmid d.
\end{cases}
}
\tag{DF-4}
\]

This is the primitive spectral analogue of a Frobenius pullback law.

---

## 3. Denominator Frobenius operators

For an arithmetic function `f` on positive integers define

\[
\boxed{
(\mathsf F_n f)(d)
:=
\sum_{e/\gcd(e,n)=d}f(e).
}
\tag{DF-5}
\]

The denominator reduction maps compose, therefore

\[
\boxed{
\mathsf F_m\mathsf F_n=\mathsf F_{mn}
=\mathsf F_n\mathsf F_m.
}
\tag{DF-6}
\]

This is a commuting representation of the positive-integer multiplicative semigroup on denominator arithmetic.

---

## 4. Jordan totients are the common eigenfunctions

For every integer weight `k>=1`,

\[
\boxed{
\mathsf F_n J_k=n^k J_k.
}
\tag{DF-7}
\]

Equivalently,

\[
\boxed{
\sum_{e/\gcd(e,n)=d}J_k(e)
=n^kJ_k(d).
}
\tag{DF-8}
\]

For `d=1`, this reduces to the standard divisor identity

\[
\sum_{e\mid n}J_k(e)=n^k.
\]

For a prime `p`, the eigen-relation is transparent:

- if `p|d`, only `e=pd` contributes and `J_k(pd)=p^kJ_k(d)`;
- if `p∤d`, `e=d,pd` contribute and
  `J_k(d)+J_k(pd)=p^kJ_k(d)`.

The general case follows multiplicatively/compositionally.

---

## 5. The geometric side has exactly the same characters

The common formal phase from #1159 satisfies

\[
\boxed{
\ell(R_n(u))=n^2\ell(u).
}
\tag{DF-9}
\]

Therefore each formal monomial `ell(u)^s` transforms by the character

\[
\boxed{n^{2s}.}
\tag{DF-10}
\]

On the denominator side, the arithmetic eigenfunction with the same character is precisely

\[
J_{2s}(d).
\]

Thus the matching

\[
\boxed{
\ell^s
\longleftrightarrow
J_{2s}
}
\tag{DF-11}
\]

is forced by the common integer-scale semigroup, not inserted as an ansatz.

---

## 6. Primitive spectral logarithm as an intertwiner

Let

\[
\mathcal P_d(t)
:=-\log\widehat\Psi_d(U(t)),
\]

where `U=ell^{-1}`.

The exact factor pullback (DF-2) becomes

\[
\boxed{
\mathcal P_d(n^2t)
=
\sum_{e/\gcd(e,n)=d}\mathcal P_e(t).
}
\tag{DF-12}
\]

So `P` intertwines:

- geometric scale `t -> n^2 t`;
- arithmetic denominator Frobenius `F_n`.

Expand

\[
\mathcal P_d(t)=\sum_{s\ge1} c_s(d)t^s.
\]

Equation (DF-12) gives

\[
\mathsf F_n c_s=n^{2s}c_s.
\]

The Jordan eigenbasis therefore forces

\[
\boxed{
c_s(d)=\kappa_sJ_{2s}(d),}
\tag{DF-13}
\]

with universal rational constants `kappa_s` independent of `d`.

Hence

\[
\boxed{
-\log\widehat\Psi_d(U(t))
=
\sum_{s\ge1}\kappa_sJ_{2s}(d)t^s.
}
\tag{DF-14}
\]

This recovers the Jordan diagonalization from a representation/intertwining principle rather than from a termwise Mobius calculation.

---

## 7. Conceptual consequence

There are two commuting nonlinear/arithmetic systems:

```text
geometric finite spectrum:
    u --R_n--> R_n(u)
    | ell
    v
    t --x n^2--> n^2 t

primitive denominator arithmetic:
    d <--preimages under denominator reduction-- e
    | J_(2s)
    v
    scalar --x n^(2s)--> scalar
```

The primitive spectral logarithm is the exact bridge between them.

Thus the appearance of Jordan totients in the reciprocal spectral moments is not merely a consequence of applying Mobius inversion to a polynomial in `M^2`.  It is a common-eigencharacter theorem for the same integer decimation semigroup.

Freeze at free-research strength:

`INTEGER_DECIMATION_GEOMETRY_AND_DENOMINATOR_ARITHMETIC_SHARE_THE_SAME_CHARACTERS`.

`FORMAL_PHASE_WEIGHT_2s <-> JORDAN_TOTIENT_WEIGHT_2s`.

`PRIMITIVE_SPECTRAL_LOG = FROBENIUS_INTERTWINER`.

This is termed “Frobenius/intertwiner” structurally; no claim is made that the construction already supplies a full Witt ring, lambda ring, or algebro-geometric Frobenius object without further axioms and operations.
