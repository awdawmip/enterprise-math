# P017×P018 Generation 4 Supplement 04 — cutoff-depth / parity-band Pareto

Status: `PROVED_WIP STRUCTURAL FAMILY / analytic optimisation open`

Generation 4 used the minimal fourth-root cutoff because it is the first point
at which every residual support token of order at least two becomes globally
single-use.  The same residual algebra actually survives on a whole cutoff
band, which exposes a continuous resource tradeoff.

## C1. The fourth-root cutoff is the shallow endpoint of a stable P3 band

Let

\[
X=k^2,\qquad U=k^2+2k,
\]

and choose an integer cutoff `y` satisfying

\[
(y+1)^4>U.
\]

Every `y`-rough square-interval state has `Omega<=3`.  Moreover

\[
(y+1)^2>\sqrt U>k,
\]

so every pair of distinct residual primes already has product above `k` and is
globally single-use under odd parity.

After squarefree repair the medium support

\[
c_y(n)=\#\{p:y<p\le k,\ p\mid n\}
\]

still has spectrum

\[
\boxed{c_y(n)\in\{0,1,3\}},
\]

until the cutoff reaches the P2 cubic-root boundary where the depth-three class
disappears.  Therefore throughout the band

\[
z_3(k)\le y<z_2(k)
\]

the exact quadratic recovery remains

\[
\boxed{
3P=3R_y^{\rm sf}-3S_{1,y}^{\rm sf}+2S_{2,y}^{\rm sf}.
}
\]

The cutoff is thus an analytic gauge choice inside one exact finite prime
identity.

## C2. Asymptotic cutoff coordinate

Write

\[
y=X^{\alpha},\qquad \frac14\le\alpha<\frac13.
\]

The residual first-order medium-prime harmonic mass is

\[
L_1(\alpha)
=\sum_{y<p\le X^{1/2}}\frac1p
=\log\frac{1}{2\alpha}+o(1).
\]

Suppose one ignores the pair correlation and tries to prove the first-moment
certificate `S_1<R` by a standard separate lower/upper linear-sieve comparison.
For `2<s<=3`, the delay-system extremal functions satisfy

\[
\frac{f(s)}{F(s)}=\log(s-1).
\]

The asymptotic break-even equation is therefore

\[
\log(s-1)=\log\frac1{2\alpha},
\]

so

\[
\boxed{s_c(\alpha)=1+\frac1{2\alpha}.}
\]

Since `log y=alpha log X`, the corresponding sieve-level exponent is

\[
\boxed{
\delta_c(\alpha)=\alpha s_c(\alpha)=\frac12+\alpha.
}
\]

At the shallow endpoint `alpha=1/4` this recovers the Generation-4 critical
level `X^(3/4)`.  Raising the cutoff makes the independent first-moment route
strictly more expensive in sieve level.

## C3. The ordered positive-parity band shrinks in the opposite direction

For the ordered Möbius/Buchstab transport starting from cutoff `y`, every
quotient satisfies

\[
q<\frac{U}{y+1}=X^{1-\alpha+o(1)}.
\]

The exact sign barrier is cutoff-independent:

\[
\boxed{q^3\le k^4=X^2\Longrightarrow\text{nonzero ordered weight is }-1.}
\]

Thus positive semiprime-quotient transport is confined to

\[
X^{2/3}<q<X^{1-\alpha+o(1)}.
\]

Its logarithmic exponent width is

\[
\boxed{w_+(\alpha)=\frac13-\alpha.}
\]

Raising the pre-sieve toward the cubic-root P2 cutoff shrinks the dangerous
positive band linearly to zero.

## C4. Exact exponent conservation

The two costs move in opposite directions and satisfy

\[
\boxed{
\delta_c(\alpha)+w_+(\alpha)=\frac56.
}
\]

This is the cutoff-depth / parity-band Pareto law:

- deeper pre-sieve -> narrower positive ordered-parity band;
- deeper pre-sieve -> stronger sieve level required by an independent
  first-moment proof;
- one unit of logarithmic exponent saved on the positive band costs exactly one
  unit of first-moment sieve-level exponent.

At `alpha=1/4` one has

\[
(\delta_c,w_+)=(3/4,1/12),
\]

while as `alpha` approaches `1/3`,

\[
(\delta_c,w_+)\to(5/6,0).
\]

At the latter endpoint the state itself becomes P2 and the state-Möbius sign
freezes, so eliminating the positive transport band does not eliminate the
parity problem.

## C5. Relation to the current explicit P3 theorem

Campbell's 2026 all-square P3 proof uses Richert weights with the substantially
shallower choice

\[
z=X^{1/8},
\]

not the fourth-root cutoff.  Its explicit large-range optimisation proves

\[
r_3(\mathcal A)>0.0249\frac{\sqrt N}{\log X}
\]

for the analytic range.  The paper explicitly notes that an all-square P2
upgrade needs a more flexible linear-sieve remainder capable of incorporating
bilinear estimates.

Therefore the project fourth-root layer is not a restatement of the existing
explicit P3 sieve.  It spends a much deeper pre-sieve to obtain the exact
support-spectrum and parity-transport structure.  The missing analytic resource
is precisely the correlated/signed remainder needed to pay for the precision
jump from the explicit `X^(1/8)` regime toward `X^(1/4)`.

## C6. Current optimisation question

Do not assume the shallow endpoint `alpha=1/4` is automatically optimal for the
signed route.  The exact prime identities remain valid throughout the stable
P3 band.  The correct optimisation problem is to choose `alpha` jointly with
one of the two parity resources:

1. affine resource `M_y/R_y` versus first support occupancy `S_{1,y}/R_y`;
2. ordered resource: negative lower quotient mass versus positive top-band
   semiprime-quotient mass.

A useful theorem may occur at an interior cutoff even though neither endpoint
closes by itself.  What is ruled out is improving one resource while ignoring
the exact opposite movement of the other.
