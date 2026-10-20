# P017×P018 square diagonal — Generation 2 frontier

Status: `PROVED_WIP STRUCTURE / analytic frontier open`

Relation to `P017_P018_SQUARE_DIAGONAL_TYPE_II_WIP.md`:

- all exact half-cutoff / reciprocal-staircase identities in Generation 1 remain valid;
- this note **supersedes only the old Active frontier** which treated `k/2` as
  the primary analytic cutoff;
- the half-cutoff is retained as a terminal microscope, not as the minimal P2
  precision required by a proof.

No statement below claims a proof of Legendre's conjecture.

## G2.1 Square covering height is the Archimedean endpoint

For `y>=2`, put

\[
P_y=\prod_{p\le y}p
\]

and define

\[
h(y)=\min\{x\ge1:\gcd(x^2+r,P_y)>1\ \forall 1\le r\le2y\},
\]

with `h(y)=infinity` if no fixed-`y` square covering root exists.

Bertrand gives the unconditional floor

\[
h(y)\ge\lceil\sqrt y\rceil.
\]

If `h(y)<=y`, the minimizing root has `x^2>=y`; its first `2x` covered states
are all strictly above `y`, so they cannot contain a prime.  Conversely a
Legendre counterexample at `y` makes `x=y` a fixed-`y` covering root.  Hence

\[
\boxed{
\text{Legendre for all }k
\iff
h(y)>y\quad\forall y.
}
\]

This is the exact Archimedean form of the moving-diagonal problem.

Fixed-cutoff phase data cannot see this height.  If
`x^2=k^2 (mod P_z)`, every fixed-`z`, fixed-horizon survivor pattern is
identical.  Independent local sign choices give an exponential square-root
orbit.  When `P_z>k^2`, however, the distinguished root has an exact height gap:

\[
x^2\equiv k^2\pmod{P_z},\quad0<x<P_z
\Longrightarrow
x=k\ \text{or}\ x\ge\sqrt{P_z+k^2}.
\]

Thus the small root is genuinely isolated, but exploiting the isolation
requires a language that moves the cutoff/horizon with the integer lift.

## G2.2 Cover phase feasibility and covering height are different layers

A fixed-`y` covering phase is the finite CSP:

- for each prime `p<=y`, choose at most one
  \(a_p\in\{-u^2\pmod p\}\);
- cover every offset `1,...,2y` by at least one chosen congruence
  \(r\equiv a_p\pmod p\).

Arbitrary local choices glue by CRT, so this CSP is exactly equivalent to the
existence of *some* fixed-`y` square covering root.  The least positive CRT root
of one feasible phase is a second optimization layer; `h(y)` minimizes over all
feasible phases.

A new explicit `y=73` phase certificate has a finite sign-orbit minimum

\[
627431388493620297650,
\]

which is still about `8.59e18` times the diagonal height 73.  This gives only an
upper bound for `h(73)`; it is not claimed globally minimal.  The older witness
has a different phase and a still larger minimum sign lift.

## G2.3 Moving-cutoff dynamics

If `y+1` is composite, `P_{y+1}=P_y` and only the horizon grows.  Therefore

\[
\boxed{h(y+1)\ge h(y)}
\]

on composite cutoff steps.  Downward jumps are possible only at prime cutoffs.

If `y>=3` is the least Legendre counterexample, then

\[
\boxed{h(y-1)=h(y)=y}.
\]

Thus the first failure is a rigid one-step covering-height plateau hit by the
moving diagonal.

If `p` is prime and `q` is the next prime, a counterexample anywhere in the
prime block `p<=y<q` forces `h(p)<=q-1`.  Hence

\[
h(p)>q-1\quad\text{for every prime }p
\]

is a sufficient prime-block criterion for Legendre.

The strict wheel also has an exact endpoint correction:

\[
\#\{1\le r\le2k:\gcd(k^2+r,P_{<k})=1\}
=
\pi((k+1)^2)-\pi(k^2)
+1_{\{k,k+2\text{ prime}\}}.
\]

At a prime cutoff the new modulus deletes at most the single right-end twin
semiprime `k(k+2)`; the generic difficulty already lives below the self-cutoff.

## G2.4 Root-cutoff ladder: minimal precision for P3, P2 and primes

Let

\[
U_k=k^2+2k=(k+1)^2-1.
\]

If every prime factor of a survivor exceeds `z` and

\[
(z+1)^{m+1}>U_k,
\]

then the survivor has at most `m` prime factors counted with multiplicity.  The
least product-certified cutoff is

\[
\boxed{
z_m(k)=\lfloor U_k^{1/(m+1)}\rfloor.
}
\]

Therefore

\[
z_1(k)=k\quad\text{(prime-only)},
\]

\[
z_2(k)\asymp k^{2/3}\quad\text{(prime or semiprime)},
\]

\[
z_3(k)\asymp k^{1/2}\quad\text{(at most three prime factors)}.
\]

This exact ladder explains why the half-cutoff `k/2` is over-resolved from the
P2 point of view: the *minimal* P2 precision is the cubic root of the interval
top.

At `z=z_2`, every rough composite is uniquely

\[
n=pq,\qquad z<p\le k<q,
\]

and

\[
\boxed{
\pi((k+1)^2)-\pi(k^2)=R_z(k)-H_z(k)
}
\]

with

\[
H_z(k)=
\sum_{z<p\le k\atop p\text{ prime}}
\#\left\{q\text{ prime}:\frac{k^2}{p}<q\le\frac{k^2+2k}{p}\right\}.
\]

This is the minimal exact binary/hyperbolic interface for P2.

## G2.5 Cubic resonance negative boundary at the P2 cutoff

Let

\[
H_c(k)=\lfloor(2k^2-1)^{1/3}\rfloor+1
\]

be the existing P018 candidate-channel horizon.  For a minimal-P2 semiprime
`pq`, `p>=z_2+1`, so

\[
q\le\frac{U_k}{z_2+1}<(z_2+1)^2.
\]

Hence its quotient root `j=floor(sqrt(q))` satisfies `j<=z_2`.  Since
`U_k<2k^2-1` for `k>=3`,

\[
z_2\le H_c(k)-1,
\]

and therefore the complete two-point candidate channel obeys

\[
\boxed{\{j,j+1\}\subseteq[0,H_c(k)]}.
\]

So **every** minimal-P2 terminal quotient channel lies inside the P018 cubic
ambiguity zone.  Existing cubic-high injectivity cannot terminate this tail.
This is `CUBIC_RESONANCE_NEGATIVE_BOUNDARY`.

## G2.6 The correct positive splice is P3 -> P2

At the P3 cutoff `z_3`, a triple-prime rough state has

\[
n=abc,\qquad z_3<a\le b\le c,
\]

and necessarily `a<=z_2`.

Put

\[
L(k)=\left\lfloor\frac{k^2}{(H_c(k)+1)^2}\right\rfloor+1.
\]

For the least-factor quotient channel

\[
j_a=\left\lfloor\sqrt{\left\lfloor k^2/a\right\rfloor}\right\rfloor,
\]

there is an exact split:

\[
a<L(k)\Longrightarrow j_a>H_c(k),
\]

\[
a\ge L(k)\Longrightarrow j_a\le H_c(k).
\]

Thus the existing cubic-high regime routes every unbalanced triple with least
factor below `L(k)`.  All remaining cubic-low ambiguity is confined to

\[
\boxed{
L(k)\le a\le b\le c\le U_k/L(k)^2.
}
\]

Asymptotically

\[
L(k)\sim2^{-2/3}k^{2/3},
\qquad
U_k/L(k)^2\sim2^{4/3}k^{2/3}.
\]

The unresolved P3-to-P2 obstruction is therefore a **balanced cubic three-factor
box** at the `X^(1/3)` scale for `X=k^2`.  This is the structural analogue of a
Type-III/trilinear regime.  Cubic routing localizes it but does not yet provide
the required analytic cancellation/counting.

## G2.7 External frontier alignment

Peter J. Campbell, arXiv:2603.10356v2 (2026), proves that every consecutive-
square interval contains a `P3`, using explicit Richert weights and a linear
sieve for the large range.  The paper explicitly places a P2 upgrade beyond the
present weighted-sieve framework and points toward stronger bilinear-capable
sieve input.

Runbo Li, arXiv:2308.04458 (latest 2025 revision), proves primes in
`[X-X^0.52,X]` for all sufficiently large `X`.  Applied to the covering-height
language, this gives for sufficiently large `y`

\[
h(y)>
\sqrt{(2y)^{25/13}-2y}
=
y^{25/26+o(1)}.
\]

Thus the current best all-interval prime exponent `0.52` translates into a
covering-height exponent `25/26`; Legendre is exactly the endpoint exponent 1.
This confirms that the height language aligns with, rather than evades, the
known short-interval barrier.

## G2.8 Current active attack surfaces

Generation 2 leaves three non-equivalent surfaces:

1. **Covering-height / moving-cutoff:** obtain a structural lower bound on
   `h(y)` which uses phase feasibility plus integer lift height, not merely a
   fixed-wheel norm.
2. **P3 -> P2 balanced cubic box:** add Type-III/bilinear information capable of
   controlling the remaining balanced triple regime localized above.
3. **P2 -> prime binary tail:** after P2 is reached, control the hyperbolic
   prime-prime tail.  The half-cutoff reciprocal staircase remains the cleanest
   microscope for this binary correlation, but is no longer the minimal sieve
   cutoff.

Do not return to higher Bonferroni order, more p-adic precision, period means,
generic Fourier norms, local negative-square compatibility, or direct use of
cubic-high uniqueness on the minimal-P2 tail.  Those branches now have explicit
negative endpoints.
