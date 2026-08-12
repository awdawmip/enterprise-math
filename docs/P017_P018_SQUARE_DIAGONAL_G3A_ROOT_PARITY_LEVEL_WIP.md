# P017×P018 square diagonal — G3A root/P2 parity bridge

Status: `PROVED_WIP STRUCTURE / PRIOR-ART PARAMETER ALIGNMENT / analytic frontier open`

Companion to `P017_P018_SQUARE_DIAGONAL_GENERATION_3_WIP.md`.  No Legendre
proof is claimed.

## A. Root-certified P3 triples globally have only two free variables

Put

\[
U=k^2+2k,
\qquad
z_3=\lfloor U^{1/4}\rfloor.
\]

A `z_3`-rough triple-prime state has

\[
n=abc,
\qquad
z_3<a\le b\le c,
\qquad
k^2<n\le U.
\]

Since

\[
ab\ge(z_3+1)^2>\sqrt U>k,
\]

the admissible third-factor interval has length

\[
\frac{2k}{ab}<2.
\]

For `k>=4`, `z_3>=2`, so all three prime factors are odd.  Among at most two
consecutive integer candidates for `c`, at most one can therefore be prime.

Writing

\[
U=q(ab)+s,
\qquad 0\le s<ab,
\]

let

\[
\varepsilon=1_{\{q\text{ even}\}},
\qquad
c_*=q-\varepsilon.
\]

Then `c_*` is the unique possible odd prime candidate and

\[
\boxed{
c_*\text{ lies in }(k^2/(ab),U/(ab)]
\iff
s+\varepsilon ab<2k.
}
\]

Moreover

\[
\boxed{c_*\ge b\iff ab^2\le U.}
\]

Thus **every** root-certified P3 contaminant, not merely the balanced
Generation-2 sub-box, is determined by two prime variables `(a,b)`, one exact
endpoint remainder gate, and primality of a deterministic odd floor candidate.

This is a global `ROOT_P3_TWO_FREE_VARIABLES` theorem.  It does not by itself
bound the number of such pairs.

## B. The minimal-P2 cutoff is an exact Möbius parity endpoint

Put

\[
z_2=\lfloor U^{1/3}\rfloor.
\]

Every `z_2`-rough state has at most two prime factors counted with
multiplicity.  A rough composite cannot be `p^2`, because the square interval
contains no perfect square.  Therefore the rough set is exactly a disjoint
union of

- primes, with `mu=-1`;
- squarefree semiprimes `pq`, with `mu=+1`.

Define

\[
R_2(k)=
\#\{k^2<n\le U:(n,P_{z_2})=1\},
\]

and

\[
M_2(k)=
\sum_{k^2<n\le U\atop(n,P_{z_2})=1}\mu(n).
\]

Then

\[
\boxed{
\pi((k+1)^2)-\pi(k^2)
=\frac{R_2(k)-M_2(k)}2,
}
\]

and the minimal-P2 semiprime tail is

\[
\boxed{
H_{z_2}(k)=\frac{R_2(k)+M_2(k)}2.
}
\]

Consequently

\[
\boxed{
\text{Legendre failure at }k
\iff
M_2(k)=R_2(k).
}
\]

A failure is therefore **complete positive Möbius polarization** of the
minimal-P2 rough set.  Unsigned rough-count precision alone cannot see this
sign statistic.  This is `P2_PARITY_ENDPOINT`.

The same endpoint can be written as a high-prime incidence selector.  Every
rough semiprime has exactly one divisor `p` in `(z_2,k]`, while a rough prime
has none, so

\[
\pi((k+1)^2)-\pi(k^2)
=
R_2(k)
-
\sum_{z_2<p\le k\atop p\text{ prime}}
\#\{n\in I_k:p\mid n,\ (n,P_{z_2})=1\}.
\]

This is the same binary parity endpoint in unsigned incidence language.

## C. Iwaniec--Laborde's bilinear level crosses P3 root precision but not P2

Iwaniec--Laborde (1981) work with a short interval of length

\[
y=X^\theta.
\]

Their linear-sieve lemma has

\[
s=\frac{\log(MN)}{\log z}
\]

and bilinear remainder terms of the form

\[
\sum_m\sum_n a_m b_n\,r(\mathcal A,mn).
\]

With their final parameter choice (`a=6`), equation (19) gives the exact level
exponent

\[
\boxed{
\delta(\theta)
:=\frac{\log D}{\log X}
=2\theta-\frac5{14}.
}
\]

At the proved value

\[
\theta=\frac9{20},
\]

this is

\[
\boxed{
\delta=\frac{19}{35}.
}
\]

Therefore at the root-P3 cutoff `z=X^(1/4)`,

\[
\boxed{
s_3=\frac{19/35}{1/4}=\frac{76}{35}>2.}
\]

The dimension-one lower linear sieve is in its positive range.  At the direct
root-P2 cutoff `z=X^(1/3)`, however,

\[
\boxed{
s_2=\frac{19/35}{1/3}=\frac{57}{35}<2.}
\]

So the same unsigned lower linear sieve is still below its positive threshold.
This cleanly aligns classical bilinear remainder technology with the project's
root-cutoff ladder: it naturally reaches root-certified P3 precision but not
direct root-P2 precision.

Taking only the **formal parameter limit** `theta -> 1/2` gives

\[
\delta\to\frac9{14}.
\]

This remains below the direct-P2 lower-sieve requirement `2/3` by exactly

\[
\boxed{
\frac23-\frac9{14}=\frac1{42}.
}
\]

This `1/42` is a scale diagnostic only.  It is not a claim that the 1981 theorem
extends to the endpoint with identical constants, and it is not a statement
that P2 itself is unavailable: Iwaniec--Laborde reach P2 by weighted-sieve
arguments despite the direct lower-sieve deficit.

## D. Consequence for the research hierarchy

The root-cutoff/level ladder now has a precise interpretation:

1. `P3 root precision` (`X^(1/4)`): classical bilinear remainder level is
   already on the positive side of the lower linear-sieve threshold.
2. `P2 root precision` (`X^(1/3)`): direct unsigned lower sieve remains below
   threshold; weighted/bilinear almost-prime machinery is needed.
3. `prime precision` (`X^(1/2)`): ordinary lower linear sieve would require a
   level beyond `X`, exposing the parity endpoint rather than a small parameter
   optimization.

Thus the active Legendre problem is not to squeeze the `1/42` direct-P2 gap.
That can at most simplify/explicitize the already-classical P2 layer.  The
actual final obstruction is the restricted-Möbius polarization in Section B,
or an equivalent square-specific parity-breaking statement.

## Prior-art source

- H. Iwaniec and M. Laborde, *P2 in short intervals*, Ann. Inst. Fourier 31
  (1981), no. 4, 37--56, DOI `10.5802/aif.848`.  Lemma 2 records the lower
  linear-sieve parameter `s=log(MN)/log z` and bilinear remainder forms; their
  final equation (19) yields the level exponent used above.
