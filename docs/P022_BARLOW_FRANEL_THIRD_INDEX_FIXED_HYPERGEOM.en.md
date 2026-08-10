# P022 — Fixed full-truncation hypergeometric form of the Franel one-third obstruction

Status: `PROVED_WIP / EXACT MOD-p NORMAL FORM`  
Owner: `P022 / program/p022-geometry-v2`  
Depends on: Bailey-tail integerization  
Scope: replace the moving one-third Franel value by a standard full `p-1` truncated fixed-parameter hypergeometric datum

## 1. Starting point

Let

\[
p=6M-1
\]

be prime.  The integerized Bailey-tail analysis gives

\[
U_M=
\sum_{k=0}^M
\binom Mk
\binom{2M+k}{k}
\binom{4M-1}{k}
\]

and proves

\[
\boxed{
p\mid F_{2M}\iff p\mid U_M.}
\]

The parameter `M` still moves with `p`.  The purpose of this note is to remove
that moving hypergeometric datum.

## 2. P022-TI09 — fixed hypergeometric summand

Because

\[
6M\equiv1\pmod p,
\]

we have

\[
-M\equiv-\frac16,
\qquad
2M\equiv\frac13,
\qquad
2M+1\equiv\frac43
\pmod p.
\]

Termwise,

\[
\binom Mk
\binom{2M+k}{k}
\binom{4M-1}{k}
\equiv
\frac{(-1/6)_k(1/3)_k(4/3)_k}{(1)_k^3}
\pmod p.
\]

Hence

\[
\boxed{
U_M\equiv
\sum_{k=0}^M
\frac{(-1/6)_k(1/3)_k(4/3)_k}{(1)_k^3}
\pmod p.
}
\]

The parameters are now independent of `p`; only the truncation horizon remains.

## 3. P022-TI10 — the short truncation is already the full `p-1` truncation

The ratio of consecutive fixed-datum terms is

\[
\frac{a_{k+1}}{a_k}
=
\frac{(6k-1)(3k+1)(3k+4)}{54(k+1)^3}.
\]

At

\[
k=M,
\]

the factor `6M-1` is exactly `p`.  Since `M+1<p`, the denominator is a p-unit.
Therefore

\[
a_{M+1}\equiv0\pmod p,
\]

and every later term through `k=p-1` remains zero modulo `p` because the same
Pochhammer numerator already contains that factor `p`.

Thus

\[
\boxed{
\sum_{k=0}^M a_k
\equiv
\sum_{k=0}^{p-1}a_k
\pmod p.
}
\]

Combining with the integer bridge gives the exact standard form

\[
\boxed{
 p\mid F_{(p+1)/3}
 \iff
 {}_3F_2\!\left[
 \begin{matrix}
 -1/6,\ 1/3,\ 4/3\\
 1,\ 1
 \end{matrix};1
 \right]_{p-1}
 \equiv0\pmod p,
 \qquad p\equiv5\pmod6.
}
\]

Here the subscript denotes truncation after `k=p-1`.

## 4. P022-TI11 — differential-companion form

The integer-separated numerator pair satisfies

\[
\frac{(4/3)_k}{(1/3)_k}=3k+1.
\]

Define the base series

\[
G(z)=
{}_3F_2\!\left(
\begin{matrix}
-1/6,\ 1/3,\ 1/3\\
1,\ 1
\end{matrix};z
\right)
\]

and let

\[
\theta=z\frac{d}{dz}.
\]

Coefficientwise,

\[
\boxed{
{}_3F_2\!\left(
\begin{matrix}
-1/6,\ 1/3,\ 4/3\\
1,\ 1
\end{matrix};z
\right)
=(1+3\theta)G(z).
}
\]

The same identity holds for every finite truncation.  Therefore the P022
one-third obstruction is the value at `z=1` of a first-order differential
companion of the repeated-parameter base datum

\[
(-1/6,1/3,1/3;1,1).
\]

This is useful structurally: a future Picard--Fuchs, Hasse-invariant, or
p-adic-hypergeometric interpretation should target `G` and its Gauss--Manin
first derivative rather than treat the `4/3` parameter as unrelated data.

No geometric realization is claimed in this note.

## 5. Exact witness `p=149`

For

\[
p=149,
\qquad
M=25,
\]

the full fixed-datum truncation vanishes modulo `149`.  The independent Franel
rank scanner gives

\[
Z_{149}=\{50,74,98\},
\qquad
r_{149}=50,
\]

and the primitive-defect module gives

\[
v_{149}(D_{50})=1.
\]

Thus the same simple composite-boundary pivot is visible through the chain

\[
F_{50}
\longleftrightarrow
U_{25}
\longleftrightarrow
{}_3F_2[-1/6,1/3,4/3;1,1]_{148}.
\]

## 6. Literature boundary and route audit

The general framework is established prior art:

- McCarthy's p-adic hypergeometric functions provide fixed rational-parameter
  analogues over finite fields;
- Neelam Saikia has studied zeros of generic p-adic hypergeometric families;
- Adolphson--Sperber relate Hasse invariants of exponential-sum families to
  mod-`p` solutions of `A`-hypergeometric systems;
- the Rodriguez--Villegas/Mortenson/Sun literature supplies many full
  `p-1`-truncation congruences for rational hypergeometric data.

A targeted search did not locate a published theorem for the exact P022 datum

\[
(-1/6,1/3,4/3;1,1)
\]

or its repeated-parameter differential base

\[
(-1/6,1/3,1/3;1,1)
\]

that classifies its zeros for primes `p=5 mod 6`.

This is only a route-audit result.  It is **not** a novelty proof.

## 7. Current research target

The original moving-index question

\[
p\mid F_{(p+1)/3}
\]

has now been converted into a standard fixed-datum question:

\[
\boxed{
H_p:=
{}_3F_2[-1/6,1/3,4/3;1,1]_{p-1}\pmod p.
}
\]

The next useful theorem would be any structural description of the primes
`p=5 mod 6` for which `H_p=0`.  For Barlow purposes one then separately checks
whether the corresponding index `(p+1)/3` is the first Franel zero.

The `p=149` example proves that the zero locus is nonempty and can produce a
simple primitive composite-defect pivot.

## 8. Executable assets

- `src/enterprise_math/p022_barlow_franel_third_index_fixed_hypergeom.py`;
- `tests/test_p022_barlow_franel_third_index_fixed_hypergeom.py`.

The tests compare against an independent exact `Fraction`/Pochhammer oracle for
small primes and lock the zero set below `500` as `{5,149}` for this special
prime class.
