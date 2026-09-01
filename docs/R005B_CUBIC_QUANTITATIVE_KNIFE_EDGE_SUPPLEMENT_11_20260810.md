# R005-B — Quantitative Cubic Knife-Edge Compression

Status: `PROVED WIP / EXTERNAL-TABLE TRANSFER + INTERNAL GEOMETRY / NOT CANONICAL`  
Date: `2026-08-10`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: Supplements 08–10  
External input: Gafni–Tao 2026, Theorem 1.2 and current zero-density table

## 1. Result

Supplement 09 handled a fixed relative supercriticality

\[
g\ge(3+\eta)a^{1/3}.
\]

The true knife edge is thinner.  Write

\[
\boxed{
g=3a^{1/3}+h.}
\]

When

\[
h=o(a^{1/3}),
\]

the cubic PRE_HORIZON geometry has the second-order scales

\[
\boxed{
\text{activation lifetime in k}
\asymp h\,a^{1/3},
}
\]

and

\[
\boxed{
\text{largest reciprocal q-window width}
\asymp h.
}
\]

Combining these scales with Gafni–Tao's quantitative exceptional-set theorem
pushes the amplification mechanism below fixed relative excess.

Define

\[
\boxed{
\theta_*
=
\frac{31}{107}
=0.289719626\ldots.
}
\]

Then for every fixed

\[
\boxed{\beta>\theta_*}
\]

the following transfer holds:

> If a consecutive prime gap satisfies
> \[
> g\ge3a^{1/3}+a^\beta
> \]
> for sufficiently large a, then that one gap creates
> \[
> \gg a^{\beta+1/3}
> \]
> activated PRE_HORIZON cubic basins, and all but
> \[
> o(a^{\beta+1/3})
> \]
> of a suitable terminal subblock contain a prime reciprocal witness and
> therefore fail full forcing.

Consequently, if such gaps occur infinitely often for one fixed
`beta>31/107`, cubic full forcing fails infinitely often.

The contrapositive gives a stronger hardness statement:

\[
\boxed{
\text{eventual cubic full forcing}
\Longrightarrow
p_{n+1}-p_n
\le
3p_n^{1/3}
+
p_n^{31/107+o(1)}.
}
\]

Thus the unresolved lower-band shell is no longer the whole
`o(a^(1/3))` neighborhood of the constant 3.  Current quantitative
exceptional-set technology compresses it to a second-order thickness no larger
than

\[
\boxed{a^{31/107+o(1)}}
\]

for purposes of the eventual-forcing hardness reduction.

The exponent `31/107` is a transfer threshold from the current external
zero-density table, not claimed as a universal intrinsic R005 constant.

---

## 2. Second-order geometry near the critical gap

Fix consecutive primes

\[
a<b=a+g
\]

and write

\[
g=3a^{1/3}+h.
\]

Assume for the moment that

\[
h\to\infty,
\qquad
h=o(a^{1/3}).
\]

The exact PRE activation inequality from Supplement 08 is

\[
gk^2>3a(k+1).
\]

Its positive real equality root is

\[
\boxed{
\kappa(a,g)
=
\frac{3a+\sqrt{9a^2+12ag}}{2g}.
}
\]

The active integer PRE states begin immediately above this root and end at

\[
K_-(a)=\lfloor\sqrt[3]{a^2}\rfloor-1.
\]

A direct expansion gives

\[
\boxed{
\kappa(a,g)
=
a^{2/3}
-
\frac{h}{3}a^{1/3}
+
o(h a^{1/3}),
}
\]

uniformly whenever `h=o(a^(1/3))` and `h->infinity`.

Therefore

\[
\boxed{
K_-(a)-\kappa(a,g)
=
\left(\frac13+o(1)\right)h a^{1/3}.
}
\]

So a second-order excess h creates a PRE lifetime of scale

\[
h a^{1/3}.
\]

---

## 3. B49 — reciprocal q-window width scales like h

For one active k the exact real q-window width is

\[
W(k)
=
\frac{k^3g-3ak(k+1)}{ab}.
\]

At the final PRE scale

\[
k=a^{2/3}+O(1),
\]

substituting

\[
g=3a^{1/3}+h
\]

gives

\[
\boxed{
W(k)=h+o(h).
}
\]

Moreover, throughout any fixed terminal fraction of the activation interval,

\[
\boxed{
W(k)\gg h.
}
\]

Hence there exists a terminal block `J_a` of active k-values with

\[
\boxed{
|J_a|\gg h a^{1/3}
}
\]

such that every reciprocal q-window attached to `k in J_a` has length

\[
\boxed{\gg h}
\]

and lies at q-scale `asymp a`.

The right endpoints

\[
H_k=\frac{k^3}{a}
\]

continue to satisfy

\[
H_{k+1}-H_k\asymp a^{1/3}.
\]

Therefore when `h=o(a^(1/3))` these terminal windows are actually separated at
the scale relevant below; bounded overlap is more than sufficient.

---

## 4. External exceptional-set exponent

Gafni and Tao define `mu(theta)` so that the prime number theorem on intervals
of length

\[
x^\theta
\]

fails only on a set of starting points of measure

\[
\boxed{X^{\mu(\theta)+o(1)}}
\]

inside `[X,2X]`.

Their Theorem 1.2 gives, from any continuous majorant `A_tilde(sigma)` for the
zero-density exponent,

\[
\mu(\theta)
\le
\sup_{\widetilde A(\sigma)\ge1/(1-\theta)}
\left(
(1-\theta)(1-\sigma)\widetilde A(\sigma)
+2\sigma-1
\right).
\]

Substitute the current piecewise upper bounds from their Table 1.

For

\[
\boxed{
\frac{31}{107}
\le\theta\le
\frac{5}{17},
}
\]

a finite piecewise rational check shows that the controlling right endpoint is
in the table segment

\[
\frac{31}{34}<\sigma<\frac{14}{15},
\qquad
\widetilde A(\sigma)
=
\frac{11}{48\sigma-36}.
\]

The admissible right endpoint is obtained from

\[
\widetilde A(\sigma_\theta)
=
\frac{1}{1-\theta},
\]

namely

\[
\boxed{
\sigma_\theta
=
\frac{47-11\theta}{48}.
}
\]

At this endpoint the `mu_2` expression collapses exactly to

\[
\sigma_\theta.
\]

The remaining earlier table segments are no larger on this theta range.
Therefore the direct Gafni–Tao table transfer gives

\[
\boxed{
\mu(\theta)
\le
\frac{47-11\theta}{48}
\qquad
\left(
\frac{31}{107}\le\theta\le\frac{5}{17}
\right).
}
\]

At

\[
\boxed{
\theta_*=\frac{31}{107},
}
\]

there is the exact identity

\[
\boxed{
\frac{47-11\theta_*}{48}
=
\frac{293}{321}
=
2\theta_*+\frac13.
}
\]

Hence for every fixed

\[
\boxed{
\theta>\theta_*,
\qquad
\theta<\frac{5}{17},
}
\]

one has the strict inequality

\[
\boxed{
\mu(\theta)
<
2\theta+\frac13.
}
\]

This exact rational coincidence is the source of the R005-B transfer exponent
`31/107`.

The zero-density estimates and the exceptional-set theorem are external prior
mathematics.  The finite substitution/audit and its use in the cubic lifecycle
are project-side transfer steps.

---

## 5. B50 — quantitative knife-edge amplification

Fix

\[
\boxed{\beta>\frac{31}{107}.}
\]

Choose a fixed exponent theta satisfying

\[
\boxed{
\frac{31}{107}<\theta<\min\left(\beta,\frac{5}{17}\right).
}
\]

Suppose a large consecutive prime gap obeys

\[
\boxed{
g\ge3a^{1/3}+a^\beta.}
\]

If the relative excess is already bounded below by a positive constant times
`a^(1/3)`, Supplement 09 applies directly.  We therefore focus on the thinner
case

\[
h=o(a^{1/3}),
\qquad
h\ge a^\beta.
\]

B49 supplies

\[
\gg h a^{1/3}
\ge
a^{\beta+1/3+o(1)}
\]

terminal active k-states whose q-windows have length

\[
\gg h
\ge
a^\beta.
\]

Since

\[
\theta<\beta,
\]

one has

\[
a^\theta=o(h).
\]

If one such q-window contains no prime, then a set of `gg h` starting points
inside it have their entire `x^theta` interval contained in the prime-free
window.  They therefore belong to the Gafni–Tao PNT exceptional set at
x-scale `asymp a`.

The q-windows in the terminal block have bounded overlap.  If `B_a` is the
number of prime-free windows in that block, then

\[
B_a h
\ll
a^{\mu(\theta)+o(1)}.
\]

Using `h>=a^beta`,

\[
\boxed{
B_a
\ll
a^{\mu(\theta)-\beta+o(1)}.
}
\]

But the total number of terminal activated states is

\[
N_a
\gg
a^{\beta+1/3+o(1)}.
\]

Because

\[
\mu(\theta)
<
2\theta+\frac13
<
2\beta+\frac13,
\]

we obtain

\[
\boxed{B_a=o(N_a).}
\]

Thus almost every state in that terminal activation block contains a prime in
its reciprocal q-window.

Those q-values lie at scale a while k lies at scale `a^(2/3)`, so q>k for
large a.  Supplement 08 B38 upgrades them from e=1 failures to fully non-forced
candidates.

Therefore

\[
\boxed{
\#\{\text{full cubic failures generated by this gap}\}
\gg
a^{\beta+1/3}
}
\]

up to a lower-order exceptional loss.

---

## 6. Corollary — second-order infinite-failure criterion

For any fixed

\[
\beta>\frac{31}{107},
\]

if infinitely many consecutive prime gaps satisfy

\[
\boxed{
 p_{n+1}-p_n
\ge
3p_n^{1/3}+p_n^\beta,
}
\]

then cubic full forcing fails infinitely often.

In fact, every sufficiently large such gap generates a burst of at least

\[
p_n^{\beta+1/3-o(1)}
\]

full-forcing failures.

This strictly strengthens the fixed-eta criterion from Supplement 09.

---

## 7. Corollary — second-order hardness of eventual full forcing

Take the contrapositive.

If cubic full forcing is eventually true, then for every fixed

\[
\beta>\frac{31}{107}
\]

all sufficiently large consecutive prime gaps satisfy

\[
 p_{n+1}-p_n
<
3p_n^{1/3}+p_n^\beta.
\]

Equivalently,

\[
\boxed{
 p_{n+1}-p_n
\le
3p_n^{1/3}
+
p_n^{31/107+o(1)}.
}
\]

Thus an eventual cubic full-forcing theorem would not merely prove

\[
\limsup\frac{p_{n+1}-p_n}{p_n^{1/3}}\le3.
\]

It would force a second-order approach to that constant with error exponent at
most

\[
\boxed{31/107=0.2897196\ldots}
\]

under the current Gafni–Tao external transfer.

For comparison, Baker–Harman–Pintz prove an all-interval exponent `0.525`.
The R005-B hardness consequence would therefore be far stronger than the
currently available general all-gap upper bound.

This is a hardness/reduction statement, not a claim that R005-B has proved the
prime-gap estimate independently.

---

## 8. What remains after quantitative compression

The lower cubic frontier is now split more finely.

### Definitely amplifying under current external technology

For every fixed

\[
\beta>31/107,
\]

excesses

\[
h\ge a^\beta
\]

above the critical `3a^(1/3)` shell generate bursts.

### Remaining second-order shell

The unresolved region for this transfer is

\[
\boxed{
0<h
\le
a^{31/107+o(1)}.
}
\]

The exact arithmetic compiler remains valid there, but current
exceptional-set exponents no longer beat the shrinking activation volume by
the argument above.

### Exact critical and subcritical gaps

If `h<=0` eventually by a fixed power-scale margin, Supplement 10's order
parameter theorem controls the lower band.  The exact `h=O(1)` and
`h=a^{o(1)}` boundary remains a genuine prime-gap / reciprocal-prime occupancy
problem.

So the practical next frontier is no longer

`g = 3a^(1/3) + o(a^(1/3))`

in full generality.  It has been compressed to

\[
\boxed{
g
=
3a^{1/3}
+
O\left(a^{31/107+o(1)}\right).}
\]

---

## 9. Status boundary

External facts consumed:

1. Gafni–Tao Theorem 1.2 relating `mu(theta)` to zero-density exponents;
2. the current piecewise zero-density majorant in their Table 1;
3. PNT-exceptional-set semantics at fixed theta;
4. Baker–Harman–Pintz `0.525` only as an external comparator.

Internal R005-B steps:

1. exact second-order activation geometry;
2. reciprocal-window width/lifetime coupling;
3. bounded-overlap transfer;
4. the rational table substitution producing `31/107`;
5. prime occupancy -> q>k -> full non-forcing;
6. the second-order hardness corollary.

No claim is made that:

- `31/107` is an intrinsic optimal exponent;
- the Gafni–Tao table bound is optimal;
- infinitely many gaps enter the remaining shell;
- eventual cubic full forcing is true or false;
- the historical novelty of this transfer threshold has been established.

Any future improvement to quantitative short-interval exceptional-set bounds
can be fed back into the same inequality

\[
\boxed{\mu(\theta)<2\theta+\frac13}
\]

to move the second-order shell boundary automatically.
