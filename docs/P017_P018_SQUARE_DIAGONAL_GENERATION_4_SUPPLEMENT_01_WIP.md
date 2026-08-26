# P017×P018 Generation 4 Supplement 01 — squarefree support-spectrum gap

Status: `PROVED_WIP STRUCTURE / analytic positivity open`

This supplement sharpens the fourth-root support-depth frontier in
`P017_P018_SQUARE_DIAGONAL_GENERATION_4_WIP.md`.

## S1. Squarefree fourth-root survivors have support spectrum {0,1,3}

Let

\[
U=k^2+2k,\qquad z=z_3(k)=\lfloor U^{1/4}\rfloor,
\]

and let `n` be a `z`-rough, squarefree state in `(k^2,U]`.  Write

\[
c(n)=\#\{p:z<p\le k,\ p\mid n\}.
\]

The root cutoff gives `Omega(n)<=3`.

- If `Omega(n)=1`, then `n` is prime and `n>k`, so `c(n)=0`.
- If `Omega(n)=2`, write `n=pq`, `p<q`.  Both factors cannot be at most `k`,
  since then `n<=k^2`; both cannot exceed `k`, since then
  `n>=(k+1)^2>U`.  Hence exactly one factor lies in `(z,k]`, so `c(n)=1`.
- If `Omega(n)=3`, write `n=abc`, `a<b<c`.  Since

  \[
  ab\ge(z+1)^2>\sqrt U,
  \]

  one has

  \[
  c<\frac U{ab}<\sqrt U<k+1.
  \]

  Thus all three primes lie in `(z,k]`, so `c(n)=3`.

Therefore

\[
\boxed{c(n)\in\{0,1,3\}.}
\]

The missing depth `2` is a square-window factor-size theorem, not a generic
property of a P3 sieve.

## S2. Exact triangular inversion of prime / P2 / P3 mass

Let `P,E,T` denote respectively the numbers of prime, squarefree-semiprime and
squarefree-triple states in the squarefree fourth-root survivor set.  Let
`R,S_1,S_2` be its total count and first two support moments.  The support
spectrum gives

\[
R=P+E+T,
\]

\[
S_1=E+3T,
\]

\[
S_2=3T.
\]

Hence

\[
\boxed{T=\frac{S_2}{3},}
\]

\[
\boxed{E=S_1-S_2,}
\]

and

\[
\boxed{P=R-S_1+\frac23S_2.}
\]

Thus the P3-only contamination, the P2 semiprime mass and the prime mass are
three linear coordinates of one second-order support-moment vector.  After the
squarefree repair there is no independent third-order moment left to estimate.

Equivalently,

\[
\boxed{3P=3R-3S_1+2S_2.}
\]

This is an exact identity, not a lower-bound truncation.

## S3. Why this is special to the fourth-root layer

At the next shallower P4 cutoff

\[
z_4=\lfloor U^{1/5}\rfloor,
\]

a squarefree triple may have exactly two factors at most `k` and one factor
above `k`, because `(z_4+1)^2` is no longer forced above `k`.

A bounded concrete example is

\[
k=35,\qquad U=1295,\qquad z_4=4,
\]

with

\[
1295=5\cdot7\cdot37.
\]

The state is squarefree and `z_4`-rough; only `5,7` lie in the medium band
`(4,35]`, so `c=2` occurs.  Hence no analogous `{0,1,3}` support-spectrum gap
holds generically one root level earlier.

Together with the token-reuse law from Generation 4, this makes the fourth-root
P3 cutoff a genuine resource knee:

- the pre-sieve is shallower than the P2 cubic-root cutoff;
- every support token of order at least two is already globally single-use;
- squarefree repair removes the only negative quadratic depth;
- the surviving support spectrum is exactly `{0,1,3}`, so degree two is enough
  for exact prime recovery.

## S4. Remaining negative boundary

The exact quadratic detector does not create positivity by itself.  A
prime-free squarefree incidence system may contain only depths `1` and `3`; the
quadratic weight is zero on both.  Therefore the unresolved theorem is still a
pointwise arithmetic correlation statement for the actual consecutive-square
sequence.

The preferred analytic target is now the exact pair

\[
(S_1,S_2),
\]

not a generic high-order Bonferroni table.  One must show that the repeatable
one-prime columns and their globally single-use pair intersections cannot realize
the prime-free extremal relation

\[
3R-3S_1+2S_2=0
\]

on the square diagonal.
