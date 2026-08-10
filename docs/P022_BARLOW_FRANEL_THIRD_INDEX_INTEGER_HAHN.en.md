# P022 — Integer and Hahn normal forms for the Franel one-third obstruction

Status: `PROVED_WIP / EXACT NORMAL-FORM REDUCTION`  
Owner: `P022 / program/p022-geometry-v2`  
Depends on: `P022_BARLOW_FRANEL_THIRD_INDEX_BAILEY_TAIL.en.md`  
Scope: replace the symmetric rational tail by an integer binomial sum and a dual-Hahn diagonal

## 1. Starting point

For a prime

\[
p=6M-1,
\]

the Bailey-tail reduction and the terminating transformation already give

\[
p\mid F_{2M}
\iff
T_M\equiv0\pmod p,
\]

where

\[
T_M={}_3F_2
\left(
\begin{matrix}
-M,-M,-M\\
-3M,3M
\end{matrix};1
\right).
\]

This note removes the remaining rational denominators and identifies the same
object inside the classical Hahn/dual-Hahn family.

## 2. P022-TI05 — positive binomial form for every summand

Using

\[
(-M)_j=(-1)^j j!\binom Mj,
\]

\[
(-3M)_j=(-1)^j j!\binom{3M}{j},
\]

and

\[
(3M)_j=j!\binom{3M+j-1}{j},
\]

the symmetric tail becomes

\[
\boxed{
T_M=
\sum_{j=0}^M
\frac{\binom Mj^3}
{\binom{3M}{j}\binom{3M+j-1}{j}}.
}
\]

Thus `T_M` is a positive rational number over `Q`; any zero modulo `p` is a
finite-field cancellation phenomenon, not an analytic zero of the rational
sum.

## 3. P022-TI06 — exact integerization

Define

\[
D_M=\binom{3M}{M}\binom{4M-1}{M}.
\]

Two elementary binomial identities give

\[
\binom Mj
\frac{\binom{3M}{M}}{\binom{3M}{j}}
=
\binom{3M-j}{2M},
\]

and

\[
\binom Mj
\frac{\binom{4M-1}{M}}{\binom{3M+j-1}{j}}
=
\binom{4M-1}{M-j}.
\]

Multiplying the summand of `T_M` by `D_M` therefore yields an integer term.
After the change of variable `k=M-j`, one obtains

\[
\boxed{
U_M:=D_MT_M
=
\sum_{k=0}^M
\binom Mk
\binom{2M+k}{k}
\binom{4M-1}{k}.
}
\]

The first values are

\[
10,\ 386,\ 18712,\ 1004866,\ 57203510,\ 3381504920,\ldots
\]

for `M=1,2,3,...`.

No OEIS or literature identity for this exact sequence was found in the
bounded search performed for this note.  That absence is only a route-audit
result and is **not** a novelty claim.

## 4. P022-TI07 — one-third Franel zero is an integer divisibility problem

When

\[
p=6M-1
\]

is prime, every factorial entering

\[
D_M=\binom{3M}{M}\binom{4M-1}{M}
\]

has argument strictly smaller than `p`.  Hence

\[
\boxed{p\nmid D_M.}
\]

The symmetric-tail criterion therefore becomes

\[
\boxed{
 p\mid F_{2M}
 \iff
 p\mid U_M,
 \qquad p=6M-1\text{ prime}.
}
\]

This is currently the most elementary exact form of the one-third obstruction:
no Franel integer, p-adic pole, or rational hypergeometric denominator remains.

For the exact witness `p=149`, `M=25`, this gives

\[
\boxed{149\mid U_{25}},
\]

and the independent Franel-rank layer proves `r_149=50`, so the divisor is
primitive and supplies the simple defect pivot `v_149(D_50)=1`.

## 5. P022-TI08 — dual-Hahn diagonal

The DLMF definition of the dual Hahn polynomial is

\[
R_n(y(y+\gamma+\delta+1);\gamma,\delta,N)
=
{}_3F_2
\left(
\begin{matrix}
-n,-y,y+\gamma+\delta+1\\
\gamma+1,-N
\end{matrix};1
\right).
\]

Take

\[
n=y=M,
\qquad
\gamma=3M-1,
\qquad
\delta=-5M,
\qquad
N=3M.
\]

Then

\[
y+\gamma+\delta+1=-M
\]

and

\[
y(y+\gamma+\delta+1)=-M^2.
\]

Therefore

\[
\boxed{
T_M
=
R_M(-M^2;3M-1,-5M,3M).
}
\]

The standard Hahn/dual-Hahn duality then also gives a diagonal Hahn
interpretation.

This identification is classical-special-function bookkeeping, not a new
orthogonal-polynomial theorem.  Its value is strategic: the remaining
one-third zero problem is a **moving-parameter diagonal evaluation inside a
classical discrete orthogonal-polynomial family** rather than an isolated
hypergeometric sum.

The usual positive-weight orthogonality regime does not apply directly because
`delta=-5M`; any use of Hahn zero-location theorems must therefore check its
parameter hypotheses rather than importing them formally.

## 6. Recurrence pressure test — not yet a theorem

Because `U_M` and `T_M` are proper hypergeometric definite sums, creative
telescoping guarantees holonomic structure in `M`.

An exact recurrence-guessing experiment in this research session found a
candidate order-2 recurrence with polynomial coefficients of degree 16 for
`T_M`.  It was fitted from exact rational values and then checked on held-out
values through `M=58`.

A Gosper/Zeilberger telescoping certificate has **not** yet been obtained.
Therefore this recurrence remains `EXPERIMENTAL / UNPROVED` and is not stored
as a theorem or production dependency.

The integer normal form `U_M` is the preferred target for a future certified
creative-telescoping derivation.

## 7. New frontier

The one-third route has now compressed through

\[
F_{(p+1)/3}
\longrightarrow
H_d
\longrightarrow
S_M
\longrightarrow
T_M
\longrightarrow
U_M,
\]

with

\[
p=6M-1.
\]

The next concrete questions are:

1. derive and certify the minimal recurrence for `U_M` or `T_M`;
2. determine whether the diagonal Hahn form exposes a finite-field or
   orthogonal-polynomial nonvanishing criterion;
3. classify primes `p=6M-1` for which `p|U_M`;
4. among those primes, characterize when `r_p=2M`, so the divisibility event is
   primitive and enters the Barlow defect lattice directly.

For the Barlow composite-boundary subfamily `p=5 mod 72`, every such primitive
one-third zero lands automatically on a composite odd boundary.

## 8. Executable assets

`src/enterprise_math/p022_barlow_franel_third_index_bailey_tail.py` now exposes:

- `bailey_symmetric_binomial_denominator`;
- `bailey_symmetric_integer_sum`;
- `bailey_symmetric_integer_identity`;
- `bailey_dual_hahn_parameters`;
- `third_index_zero_via_integer_sum`.

The companion test file locks the first integer values, the exact
integerization, the p-unit denominator, the dual-Hahn parameter map, and the
same `p=149` zero through the integer route.
