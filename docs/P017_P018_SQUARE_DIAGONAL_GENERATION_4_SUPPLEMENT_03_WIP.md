# P017×P018 Generation 4 Supplement 03 — parity-resource Pareto frontier

Status: `PROVED_WIP CONDITIONAL RESOURCE THEOREMS / analytic inputs open`

This supplement does not add a new sieve estimate.  It records the exact amount
of unsigned and signed information which would suffice once the fourth-root
support identities are in place.

## R1. Affine occupancy/sign tradeoff

At the fourth-root cutoff let

\[
R=R_3,\qquad M=M_3,\qquad S=S_1,
\]

and let `C<=1` be the rough prime-cube correction.  Generation 4 proves

\[
3P=2R-M-S-C,
\]

where `P` is the prime count in the consecutive-square interval.

Suppose numerical/analytic bounds of the form

\[
M\le\eta R,
\qquad
S\le\sigma R
\]

are available.  Then

\[
\boxed{
3P\ge(2-\eta-\sigma)R-1.
}
\]

Hence

\[
\boxed{
(2-\eta-\sigma)R>1
\Longrightarrow P>0.
}
\]

After the squarefree repair the cube correction disappears, and the strict
asymptotic resource condition is simply

\[
\boxed{\eta+\sigma<2.}
\]

This is the exact Pareto line between medium-prime occupancy information and
rough Möbius sign information.

## R2. Consequence at the fourth-root first-moment critical line

Generation 4 identified the independent linear-sieve break-even point

\[
s=3,
\]

where the separate extremal first-moment ratio reaches the same `log 2` local
mass and no strict unsigned margin remains after the worst-case sieve
constants.

The affine Pareto theorem shows what is needed there: if an unsigned argument
can reach only a critical bound

\[
S\le(1+o(1))R,
\]

then one does **not** need a full estimate `M=o(R)`.  Any fixed nontrivial
one-sided sign deficit

\[
M\le(1-\delta)R
\]

with `delta>0` leaves a positive main margin.  More generally an improvement of
one resource can compensate a loss in the other exactly along

\[
\eta+\sigma=2.
\]

Thus the correct parity-breaking target is weaker than pointwise square-root
Möbius cancellation.

## R3. Ordered-transport tradeoff

The signed Buchstab descent gives the independent exact representation

\[
P=-M-B_{\rm ord},
\]

where

\[
B_{\rm ord}
=\sum_{z_3<p\le k}
  \sum_{k^2<pq\le U\atop P^-(q)>p}\mu(q).
\]

If

\[
B_{\rm ord}\le-\beta R,
\qquad
M\le\eta R,
\]

then

\[
\boxed{P\ge(\beta-\eta)R.}
\]

Consequently

\[
\boxed{\beta>\eta\Longrightarrow P>0.}
\]

This is a second resource frontier.  It asks for directional negativity of the
ordered P2-quotient transport rather than a separate estimate of the first
support moment.

## R4. One-dimensional quotient sign separation

After swapping the ordered transport, each fourth-root rough quotient `q>k`
has at most one parity-compatible prime candidate `p_*(q)`.  The exact sign
barrier from the one-dimensional quotient normal form is

\[
q^3\le k^4
\Longrightarrow
\text{every nonzero transport row has sign }-1.
\]

Positive semiprime-quotient transport is confined to

\[
q^3>k^4.
\]

Therefore a proof of a positive `beta` may be split into two unequal tasks:

1. retain enough negative prime-quotient mass in the lower band;
2. upper-bound the positive semiprime-quotient mass in the top band.

This is more specific than estimating the absolute value of the complete
ordered transport.

## R5. Floor-prime prior-art near miss

For a fourth-root rough quotient, the unique candidate is a parity-shifted
floor value (`floor(k^2/q)+1` or `+2`, equivalently `floor(U/q)` or `-1`).  The
quotient range is

\[
X^{1/2}<q<X^{3/4},\qquad X=k^2.
\]

Runbo Li's floor-prime theorem (`arXiv:2308.16301`) gives asymptotics for the
unweighted condition `floor(X/n)` prime for every fixed exponent

\[
\theta>435/923<1/2.
\]

Thus the *size range* of the quotient variable is not the missing ingredient.
The project target additionally requires a parity shift and, more importantly,
rough Möbius weight

\[
\mu(q)1_{(q,P_{X^{1/4}})=1}.
\]

The preferred new analytic statement is therefore a

`rough-Mobius weighted shifted-floor-prime correlation`,

not another unweighted floor-prime distribution theorem.

## R6. Exact-sqrt large-prime-factor near miss

Runbo Li's 2025 short-interval largest-prime-factor result proves that every
sufficiently large interval

\[
[X,X+X^{1/2}]
\]

contains an integer with a prime factor exceeding

\[
X^{0.7437}.
\]

For `X=k^2`, the complementary cofactor is below `X^0.2563`; the fourth-root
boundary is `X^0.25`.  The exponent gap is therefore only

\[
0.2563-0.25=0.0063.
\]

This is a useful scale alignment, not a Legendre proof.  Without an additional
fourth-root roughness condition the small cofactor can contain small prime
factors.  If such a witness were fourth-root rough, the current exponent would
already force it to be `P2`; an exponent strictly above `3/4` together with
fourth-root roughness would force the cofactor to be 1 and hence produce a
prime.  No such combined theorem is claimed here.

## R7. Current resource priority

The most economical analytic targets are now:

1. prove a one-sided bound for the affine pair `(M/R,S/R)` crossing
   `eta+sigma=2`;
2. or prove ordered transport negativity strong enough to cross `beta>eta`;
3. preferentially use the one-dimensional quotient sign split rather than an
   undirected norm;
4. treat the exact-sqrt large-prime-factor `0.7437` result as a near-threshold
   auxiliary resource, not as a substitute for roughness/parity transport.

No new claim is made for generic linear sieve, Harman sieve, floor-prime theory,
or large-prime-factor theory; those are prior analytic inputs.
