# P017×P018 square diagonal — Generation 3 frontier

Status: `PROVED_WIP STRUCTURE / PRIOR-ART CORRECTED / analytic frontier open`

This note supersedes only the **active-frontier interpretation** of
`P017_P018_SQUARE_DIAGONAL_GENERATION_2_WIP.md`.  All exact Generation-2
covering-height, root-cutoff, cubic-resonance and balanced-box localization
statements remain valid.

No statement below claims a proof of Legendre's conjecture.

## G3.1 Prior-art correction: P3 -> P2 existence is not the open problem

Generation 2 correctly identified the cubic-root product cutoff and localized
P3 triple-prime survivors into a balanced `X^(1/3)` factor box, where
`X=k^2`.  It was too strong, however, to interpret this localization as a new
unsolved P3-to-P2 **existence** barrier.

Classical work already proves much more asymptotically:

- Chen (1975) proved that intervals of square-root length contain a `P2` for
  sufficiently large scale; Campbell's 2026 consecutive-square P3 paper states
  this prior-art boundary explicitly.
- Iwaniec--Laborde, *P2 in short intervals*, Ann. Inst. Fourier 31 (1981),
  37--56, proves that every sufficiently large real `x` has a `P2` in
  `[x,x+x^0.45]`.  At `x=k^2`, this is a window of size `k^0.9`, much shorter
  than the consecutive-square width `2k+1`.

Campbell's 2026 contribution is instead an **explicit all-k P3 theorem**.  His
finite range even has P2; the remaining analytic range is handled by an
explicit Richert/linear-sieve argument.  Campbell explicitly notes that an
all-k P2 upgrade would require a bilinear-capable error-term input of the type
introduced by Iwaniec, for which no suitable explicit version is presently
available in that framework.

Therefore this bridge must not claim novelty for asymptotic P2 existence.  The
project-local value of the Generation-2 cubic box is structural: it identifies
how the square-shell geometry specializes the classical bilinear remainder
mechanism and where an explicit/all-k implementation would have to spend its
error budget.

## G3.2 Thin-shell collapse: the balanced cubic box has only two free variables

Retain the Generation-2 notation

\[
U_k=k^2+2k,\qquad
H_c(k)=\lfloor(2k^2-1)^{1/3}\rfloor+1,
\]

and

\[
L(k)=\left\lfloor\frac{k^2}{(H_c(k)+1)^2}\right\rfloor+1.
\]

The exact threshold is

\[
\boxed{L(k)^2>2k\qquad(k\ge202).}
\]

The last failure is `k=201`.

A convenient proof is finite only on the short range `202<=k<=223`.  For
`k>=224`, use

\[
2^{1/3}<\frac{63}{50},
\qquad
\frac{2}{k^{2/3}}<\frac{3}{50},
\]

so

\[
H_c(k)+1<\frac{33}{25}k^{2/3}.
\]

Hence

\[
L(k)>\left(\frac{25}{33}\right)^2 k^{2/3}
\]

and therefore

\[
L(k)^2>
\left(\frac{25}{33}\right)^4 k^{4/3}>2k,
\]

where the last inequality already holds at `k=224` and then strengthens with
`k`.

Now let a Generation-2 balanced triple be

\[
n=abc,\qquad L(k)\le a\le b\le c,\qquad k^2<n\le U_k.
\]

For fixed `(a,b)`, put `d=ab`.  Since `d>=L(k)^2>2k`, the allowed interval for
the third factor

\[
\frac{k^2}{d}<c\le\frac{U_k}{d}
\]

has length

\[
\frac{2k}{d}<1.
\]

Thus there is **at most one integer third factor** for every pair `(a,b)`.
The unique candidate is

\[
\boxed{c_0(a,b)=\left\lfloor\frac{U_k}{ab}\right\rfloor.}
\]

Writing `d=ab`, this candidate lies strictly above the lower square boundary
exactly when

\[
\boxed{U_k\bmod d<2k.}
\]

The ordering condition `c_0>=b` is equivalent to

\[
\boxed{ab^2\le U_k.}
\]

Consequently, for `k>=202`, the balanced prime-triple count has the exact
2-dimensional form

\[
T_{\mathrm{bal}}(k)=
\sum_{\substack{a,b\ \mathrm{prime}\\
L(k)\le a\le b\\ab^2\le U_k}}
1_{\{U_k\bmod(ab)<2k\}}
1_{\mathbb P}\!\left(\left\lfloor\frac{U_k}{ab}\right\rfloor\right),
\]

with the already-known P3/P2 cutoff restrictions imposed when this is consumed
inside the root-cutoff ladder.

So the `X^(1/3) x X^(1/3) x X^(1/3)` factor **box** is Type-III in scale but
not in discrete freedom at square-shell thickness `X^(1/2)`: the third
coordinate is a deterministic floor of the first two.

This is the `THIN_SHELL_TYPE_III_TO_TYPE_II_COLLAPSE`.

## G3.3 Exact divisor gate = short-interval sieve remainder

Let

\[
A_k=(k^2,U_k]\cap\mathbb Z,
\qquad H=|A_k|=2k,
\]

and for an integer `d>H` define

\[
g_k(d)
=
\left\lfloor\frac{U_k}{d}\right\rfloor
-
\left\lfloor\frac{k^2}{d}\right\rfloor.
\]

Because the interval has length less than `d`, `g_k(d)` is `0` or `1`.  More
precisely,

\[
\boxed{
g_k(d)=1_{\{U_k\bmod d<H\}}.}
\]

Define the centered divisor discrepancy

\[
\rho_k(d)=g_k(d)-\frac{H}{d}.
\]

Then the balanced-pair gate is exactly

\[
\boxed{
1_{\{U_k\bmod(ab)<2k\}}
=
\frac{2k}{ab}+\rho_k(ab).
}
\]

This is not merely analogous to the classical sieve remainder.  For the
consecutive interval `A_k`,

\[
|A_{k,d}|=g_k(d),
\]

so with local density `1/d`,

\[
\boxed{
\rho_k(d)=|A_{k,d}|-\frac{|A_k|}{d}=r(A_k,d).
}
\]

Iwaniec's 1980 linear-sieve error term and Iwaniec--Laborde's 1981 short-
interval P2 argument organize the sieve remainders into bilinear forms of the
shape

\[
\sum_m\sum_n \alpha_m\beta_n\,r(A,mn),
\qquad |\alpha_m|,|\beta_n|\le1.
\]

The square-diagonal balanced cubic gate is therefore a **specialization of the
same mother remainder object** at the rigid endpoint `U_k=k^2+2k` and the
balanced divisor scale `mn\asymp k^{4/3}`.

Relation: `SAME_MOTHER / SPECIALIZATION`, not a new sieve theorem.

## G3.4 A useful upper-bound projection drops the third primality condition

For proving P3 -> P2 inside a quantitative weighted-sieve argument, it is enough
to upper-bound the number of balanced triple contaminants.  Dropping the
condition that `c_0` be prime only enlarges the contaminant set.  Therefore

\[
T_{\mathrm{bal}}(k)
\le
G_{\mathrm{bal}}(k)
:=
\sum_{\substack{a,b\ \mathrm{prime}\\
L(k)\le a\le b\\ab^2\le U_k}}
 g_k(ab).
\]

The exact decomposition is

\[
\boxed{
G_{\mathrm{bal}}(k)
=
2k
\sum_{\substack{a,b\ \mathrm{prime}\\
L(k)\le a\le b\\ab^2\le U_k}}
\frac1{ab}
+
\sum_{\substack{a,b\ \mathrm{prime}\\
L(k)\le a\le b\\ab^2\le U_k}}
\rho_k(ab).
}
\]

The first term is a smooth local-density main term.  Since both prime variables
live in constant-ratio intervals on the `k^(2/3)` scale, its natural size is
`k/log^2 k`.  The genuinely nonlocal input is the second, bilinear remainder
sum.  This is precisely the kind of term the classical Chen/Iwaniec machinery
was designed to control.

This observation does **not** by itself give an all-k P2 theorem.  In
particular, existing P018 cubic-high uniqueness only routes the unbalanced
triples; it does not prove that those triples are absent.  The correct
conclusion is narrower: the balanced low-channel component needs no genuinely
three-variable analytic estimate after `k>=202`.

## G3.5 Campbell's quantitative P3 mass changes the explicit-upgrade target

For the large range in Campbell's 2026 proof, with
`A(N)=Z cap (N,N+2 sqrt(N))`, the final explicit inequality is

\[
r_3(A)>0.0249\frac{\sqrt N}{\log X}.
\]

Thus an explicit P3 -> P2 upgrade does not need to manufacture positive mass
from zero.  It needs an explicit upper bound on the P3-only contaminants that
is strictly smaller than the already-positive weighted P3 budget, together
with control of the other weighted-sieve loss terms.

Generation 3 therefore reframes the explicit problem as a **constant-budget
problem for bilinear remainder terms**, not as discovery of an asymptotic P2
existence mechanism.

## G3.6 P2 -> prime is now the genuine almost-prime frontier

After this prior-art correction, the root-cutoff ladder has different roles:

- `P3 -> P2`: asymptotically solved in classical short-interval sieve theory;
  project work is useful only insofar as it produces an explicit/all-k or
  square-specialized simplification.
- `P2 -> prime`: still the genuine parity-sensitive step relevant to Legendre.
- covering height `h(y)>y`: the equivalent Archimedean endpoint remains open.

At the minimal P2 cutoff

\[
z_2(k)=\lfloor U_k^{1/3}\rfloor,
\]

we retain the exact identity

\[
\pi((k+1)^2)-\pi(k^2)=R_{z_2}(k)-H_{z_2}(k),
\]

where `H_{z_2}` is the hyperbolic prime-prime semiprime tail.  The earlier
`CUBIC_RESONANCE_NEGATIVE_BOUNDARY` still applies: existing P018 cubic-high
uniqueness does not terminate this binary tail.

Likewise the Generation-1 half-cutoff reciprocal staircase remains a clean
microscope for the P2 contamination, but not a minimal sieve cutoff.

## G3.7 Balanced Chen mirror route remains much narrower than generic Chen

The existing project route `p017_p018_balanced_chen_mirror.py` asks for a
representation

\[
2k(k+1)=p+P_2,
\qquad
|p-k(k+1)|<k.
\]

Its centered window has radius about `N^(1/2)`.  This is not supplied by the
classical short-interval P2 theorem above, nor by ordinary Chen's theorem.  It
is a genuinely much more localized additive requirement.

The literature contains localized forms of Chen's theorem (for example
Y. Cai--M. Lu, *Chen's theorem in short intervals*, Acta Arith. 91 (1999),
311--323), but no result consumed in this note reaches the square-root-centered
window required by the balanced mirror criterion.  Therefore the mirror route
remains an open project target; it must not be marked solved merely because
P2 exist between consecutive squares asymptotically.

## G3.8 Current active attack surfaces

The current hierarchy is:

1. **P2 -> prime binary tail** — primary almost-prime frontier.  Seek a
   square-specific parity-breaking correlation, not another local-density
   reparametrization.
2. **Covering height / moving cutoff** — primary Archimedean frontier.  Seek a
   mechanism that uses `x=z, H=2x` and therefore distinguishes the diagonal
   lift from fixed-wheel sign orbits.
3. **Explicit square P2 auxiliary route** — optional but useful: specialize the
   Chen/Iwaniec bilinear remainder to the exact square endpoint, and determine
   whether Campbell's positive explicit P3 margin can absorb a fully explicit
   contaminant bound.
4. **Balanced Chen mirror** — separate additive route requiring localization
   at the `N^(1/2)` centered scale.

Do not reopen `P3 -> P2` as an asymptotic existence problem, and do not describe
the balanced cubic box as a genuinely three-free-variable Type-III analytic
obstruction once `k>=202`.

## References used for the prior-art boundary

- J.-R. Chen, *On the distribution of almost primes in an interval*, Scientia
  Sinica 18 (1975), 611--627.
- H. Iwaniec, *A new form of the error term in the linear sieve*, Acta Arith.
  37 (1980), 307--320.
- H. Iwaniec and M. Laborde, *P2 in short intervals*, Ann. Inst. Fourier 31
  (1981), no. 4, 37--56, DOI `10.5802/aif.848`.
- Y. Cai and M. Lu, *Chen's theorem in short intervals*, Acta Arith. 91 (1999),
  311--323, DOI `10.4064/aa-91-4-311-323`.
- P. J. Campbell, *On the Existence of Integers with at Most 3 Prime Factors
  Between Every Pair of Consecutive Squares*, arXiv:2603.10356v2 (2026).
