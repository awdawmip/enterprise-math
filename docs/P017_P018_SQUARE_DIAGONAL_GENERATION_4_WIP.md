# P017×P018 square diagonal — Generation 4 frontier

Status: `PROVED_WIP STRUCTURE / analytic correlation frontier open`

Generation 4 supersedes only the active-frontier interpretation of Generation
3.  The previous covering-height, root-cutoff, cubic-resonance, thin-shell and
parity-transport identities remain valid.  This note corrects one repeated-
factor capacity claim from the preceding exploratory generation and replaces
the broad `prime versus squarefree triple` target by a sharper finite support-
depth interface.

No statement below claims a proof of Legendre's conjecture.

## G4.1 Fourth-root pre-sieve gives an exact degree-three prime polynomial

Put

\[
I_k=\{k^2+1,\ldots,k^2+2k\},\qquad
U_k=k^2+2k,
\]

and

\[
z=z_3(k)=\lfloor U_k^{1/4}\rfloor.
\]

For a `z`-rough survivor `n` define its medium support depth

\[
c(n)=\#\{p\text{ prime}:z<p\le k,\ p\mid n\}.
\]

The fourth-root cutoff gives `Omega(n)<=3`.  If `n` is composite, its least
prime factor is at most `sqrt(n)<k+1`, hence at most `k`; roughness forces that
factor above `z`.  Therefore

\[
\boxed{n\text{ prime}\iff c(n)=0},\qquad 0\le c(n)\le3.
\]

Consequently

\[
\boxed{
1_{\mathbb P}(n)
=1-c(n)+\binom{c(n)}2-\binom{c(n)}3.
}
\]

Writing

\[
R_3=\sum_n1,
\qquad
S_j=\sum_n\binom{c(n)}j
\]

over the fourth-root rough survivors gives the exact finite identity

\[
\boxed{
\pi((k+1)^2)-\pi(k^2)=R_3-S_1+S_2-S_3.
}
\]

This is a finite residual-support form of inclusion--exclusion after the
fourth-root pre-sieve.  It is an exact coordinate, not by itself a parity-
breaking theorem.

## G4.2 A quadratic lower polynomial kills the dominant squarefree triple core

On the only possible depths `c=0,1,2,3`, define

\[
w_2(c)=\frac{(c-1)(c-3)}3
      =1-c+\frac23\binom c2.
\]

Its values are

\[
3w_2(c)=3,0,-1,0.
\]

Thus it is exact on prime depth `0`, semiprime/one-column depth `1`, and
squarefree-triple depth `3`; the only negative slack is depth `2`.

Let

\[
N_2=\#\{n:c(n)=2\}.
\]

Then

\[
\boxed{
3\pi(I_k)=3R_3-3S_1+2S_2+N_2.
}
\]

Equivalently, with

\[
\mathcal W_2(k)=3R_3-3S_1+2S_2,
\]

\[
\boxed{\mathcal W_2(k)=3\pi(I_k)-N_2.}
\]

Hence

\[
\boxed{\mathcal W_2(k)>0\Longrightarrow\pi(I_k)>0.}
\]

The squarefree fully-`k`-smooth triple core which dominated the Generation-3D
Möbius aliasing is annihilated *exactly* by this degree-two support weight.  The
remaining negative class is the repeated-factor triple `p^2 q` / `p q^2`.

This does not evade parity: a prime-free squarefree model consisting only of
support depths `1` and `3` has `w_2=0` pointwise.  The new value is that the
factor-depth obstruction is now concentrated into a two-moment arithmetic
correlation rather than an undifferentiated Möbius sign problem.

## G4.3 Correction: the repeated prime lives up to the three-quarter scale

An earlier exploratory bound placed the repeated prime of every depth-two
state below the cubic P2 cutoff.  That is false.  For example

\[
10051=19\cdot23^2
\]

lies between `100^2` and `101^2`, while `z_3(100)=10` and `z_2(100)=21`.

The correct statement is as follows.  A depth-two fourth-root survivor has
exactly three prime factors counted with multiplicity and exactly two distinct
medium primes, so it has a unique repeated prime `p>z`.  Since

\[
(z+1)^2>\sqrt{U_k}>k,
\]

the odd `p^2` column has spacing `2p^2>2k` and is globally single-use.  The
other rough prime factor is at least `z+1`, hence

\[
\boxed{
p\le
\left\lfloor\sqrt{\frac{U_k}{z+1}}\right\rfloor
\asymp k^{3/4}.}
\]

Therefore

\[
N_2
\le
\#\left\{p\text{ prime}:z<p\le
\sqrt{U_k/(z+1)}\right\}.
\]

The corrected layer is still lower-order compared with a `k/log k` prime-scale
main term, but it is not confined to `p<=z_2`.

## G4.4 General root-cutoff token reuse law and the P3 Pareto knee

At the general product cutoff

\[
z_m(k)=\lfloor U_k^{1/(m+1)}\rfloor,
\]

a squarefree token formed from `j` distinct residual medium primes satisfies

\[
D\ge(z_m+1)^j.
\]

If

\[
2j\ge m+1,
\]
then

\[
D^2\ge(z_m+1)^{2j}
\ge(z_m+1)^{m+1}>U_k>k^2,
\]
so

\[
\boxed{D>k.}
\]

Parity plus divisibility then places odd incidences in one residue class modulo
`2D`; because `2D>2k`, every such token is globally single-use across the
square interval.

Thus the first structurally single-use support order is

\[
\boxed{j_*(m)=\left\lceil\frac{m+1}{2}\right\rceil.}
\]

For `m=3`, `j_*=2`: every pair and triple correction is single-use, while only
the first-order medium-prime columns may repeat.  For `m=4`, pair tokens can
repeat again.  The fourth-root P3 layer is therefore a genuine resource knee:
it is shallow enough to leave the linear sieve in a potentially positive
regime, yet deep enough to make every support correction of order at least two
globally single-use.

## G4.5 First-moment criterion and its exact linear-sieve criticality

Dropping the nonnegative exact corrections gives the elementary certificate

\[
\boxed{S_1<R_3\Longrightarrow\pi(I_k)>0.}
\]

The natural local-density ratio is

\[
\frac{S_1}{R_3}
\sim
\sum_{z<p\le k}\frac1p
\longrightarrow\log2.
\]

So the raw density heuristic has a substantial margin `1-log 2`.

However ordinary *separate* upper/lower linear-sieve extremal bounds eat this
margin exactly at a critical level.  Let `X=k^2`, so `z~X^(1/4)`, and put

\[
s=\frac{\log D}{\log z}.
\]

The standard linear-sieve delay system gives, for `2<=s<=3`,

\[
F(s)=\frac{2e^\gamma}{s},\qquad
f(s)=\frac{2e^\gamma\log(s-1)}{s},
\]

hence

\[
\frac{f(s)}{F(s)}=\log(s-1).
\]

At the endpoint `s=3`,

\[
\boxed{\frac{f(3)}{F(3)}=\log2,}
\]

which is exactly the asymptotic medium-prime harmonic mass.  Therefore a proof
which lower-sieves `R_3`, upper-sieves every first-order column independently,
and simply subtracts them is only at break-even when `s=3`.

Since `z~X^(1/4)`, this endpoint is

\[
\boxed{D=X^{3/4}.}
\]

Call this `FOURTH_ROOT_FIRST_MOMENT_CRITICAL_LEVEL`.  Below this effective
level, independent extremal upper/lower constants cannot recover the genuine
`1-log 2` density margin.  Any improvement must use correlation between the
first-order columns and their pair overlaps, or some different parity-breaking
input.

The formulas above follow directly from the standard linear-sieve delay system;
Campbell's 2026 explicit square-interval P3 paper records that system in its
Lemma 2.2 and explains why a P2 upgrade needs bilinear-capable error terms.

## G4.6 The quadratic certificate identifies the missing correlated object

The degree-two certificate says that the correct next object is not `S_1`
alone but

\[
\boxed{
\mathcal W_2=3R_3-3S_1+2S_2.
}
\]

Equivalently,

\[
\boxed{
2S_2>3(S_1-R_3)
\Longrightarrow
\pi(I_k)>0.
}
\]

The pair term is especially rigid: every pair token `D=pq` satisfies `D>k`.
There is at most one parity-compatible odd multiple in the square interval.  If
`q_D` denotes the least odd integer strictly larger than `k^2/D`, then that
pair token contributes exactly when

\[
Dq_D\le U_k
\]

and `q_D` remains `z`-rough.  Thus `S_2` is a sum of single-use floor/roughness
gates, not a high-multiplicity incidence count.

Formally expanding only the small-prime pre-sieve gives

\[
R_3=\sum_{d\mid P_z}\mu(d)|A_d|,
\]

\[
S_1=
\sum_{z<p\le k}\sum_{d\mid P_z}\mu(d)|A_{pd}|,
\]

\[
S_2=
\sum_{z<p<q\le k}\sum_{d\mid P_z}\mu(d)|A_{pqd}|.
\]

Writing `|A_m|=2k/m+rho_k(m)`, the formal local-density main coefficient of
`mathcal W_2` is

\[
3-3L_1+2L_2,
\]

where

\[
L_1=\sum_{z<p\le k}\frac1p,
\qquad
L_2=\sum_{z<p<q\le k}\frac1{pq}.
\]

As `k` grows,

\[
L_1\to\log2,
\qquad
L_2\to\frac{(\log2)^2}{2},
\]

so the normalized quadratic main coefficient tends to

\[
\boxed{
1-\log2+\frac{(\log2)^2}{3}
\approx0.467003824>0.
}
\]

The unresolved issue is the correlated remainder

\[
\sum_{d\mid P_z}\mu(d)
\left(
3\rho_k(d)
-3\sum_p\rho_k(pd)
+2\sum_{p<q}\rho_k(pqd)
\right).
\]

This is the minimal Generation-4 analytic target.  Treating its three pieces by
independent norms returns to the sieve parity barrier; the needed input must
preserve the correlation between one-column occupancy and the single-use pair
overlap which the exact support polynomial exposes.

## G4.7 Structural exactness alone still has a countermodel

The facts

- every state has support depth at most three;
- pair/triple tokens are globally single-use;

are not sufficient by themselves.  An abstract prime-free incidence system may
place every state in exactly one repeatable first-order column.  Then every
state has `c=1`, all pair/triple intersections are empty (hence trivially
single-use), and the exact prime polynomial returns zero everywhere.

Therefore Generation 4 must not be promoted as a proof from finite capacity
alone.  The missing theorem must use arithmetic correlation specific to the
square interval, not merely the cardinality ceiling on higher support tokens.

This is `SUPPORT_DEPTH_CAPACITY_NOT_ENOUGH`.

## G4.8 Current active frontier

The main square-diagonal attack is now:

1. **quadratic support correlation:** prove a pointwise positive lower bound for
   `mathcal W_2=3R_3-3S_1+2S_2`, or an equivalent bound on the correlated
   remainder above;
2. **single-use pair arithmetic:** exploit the exact odd candidate attached to
   each medium-prime pair rather than replacing `S_2` by an independent sieve
   density;
3. **covering height:** continue the independent Archimedean route `h(y)>y`;
4. **terminal P2 microscope:** retain the half-cutoff reciprocal prime-pair
   problem as a later binary endpoint, not as the current pre-sieve resource.

Do not return to generic higher Bonferroni precision, generic Fourier norms, or
an independent estimate of `R_3` and `S_1` that ignores their pair-overlap
correlation.  The first-moment extremal constants have an explicit critical
boundary at `s=3`.

## Prior-art boundary used here

- P. J. Campbell, *On the Existence of Integers with at Most 3 Prime Factors
  Between Every Pair of Consecutive Squares*, arXiv:2603.10356v2 (2026),
  especially the explicit linear-sieve delay system and the discussion of the
  bilinear input needed beyond the weighted P3 framework.
- H. Iwaniec and M. Laborde, *P2 in short intervals*, Ann. Inst. Fourier 31
  (1981), no. 4, 37--56, DOI `10.5802/aif.848`, for the classical bilinear
  remainder architecture.  These are prior analytic tools; no novelty claim is
  made for generic linear/bilinear sieve theory.
