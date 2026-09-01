# R005-B — Supercritical Cubic Gap Amplification

Status: `PROVED WIP / CONDITIONAL ON GAP SIZE + PEER-REVIEWED ALMOST-ALL PRIME INPUT / NOT CANONICAL`  
Date: `2026-08-10`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: Supplement 08; R005-B upper density-zero Supplement 07  
External input: Gafni–Tao, *Essential Number Theory* 5 (2026), 221–241

## 1. Result

Supplement 08 identified the exact PRE_HORIZON activation scale

\[
g_{\rm crit}(a)=3a^{1/3}+O(1).
\]

This supplement shows that a genuinely supercritical gap is not merely capable
of producing one cubic lower-band exception.

It is an **amplifier**.

Fix

\[
\eta>0.
\]

Suppose a sequence of consecutive prime gaps

\[
a_j<b_j,\qquad g_j=b_j-a_j
\]

satisfies

\[
a_j\to\infty
\]

and

\[
\boxed{
g_j\ge(3+\eta)a_j^{1/3}.
}
\]

Then each such gap creates a block of order

\[
a_j^{2/3}
\]

PRE_HORIZON cubic basins, and for all but

\[
o(a_j^{2/3})
\]

of those basins the reciprocal q-window actually contains a prime q.  That q
lies above k and is therefore a **fully non-forced** lower-band witness by
Supplement 08.

Consequently,

\[
\boxed{
\text{one supercritical cofactor gap}
\Longrightarrow
\gg_{\eta} a^{2/3}
\text{ full cubic non-forcing basins}
}
\]

up to an `o(a^(2/3))` exceptional loss.

Thus if such supercritical gaps occur infinitely often, cubic full-forcing
fails infinitely often.

This is a conditional transfer theorem.  It does **not** prove that infinitely
many prime gaps satisfy the supercritical hypothesis.

---

## 2. The external almost-all input

Gafni and Tao prove a prime number theorem in almost all intervals

\[
[x,x+x^\theta]
\]

for every fixed

\[
\theta>\frac{2}{15}.
\]

Their paper is published as:

A. Gafni and T. Tao, *On the number of exceptional intervals to the prime
number theorem in short intervals*, Essential Number Theory 5 (2026),
221–241, DOI `10.2140/ent.2026.5.221`.

For the present transfer we use only the very comfortable exponent

\[
\boxed{\theta=\frac14}.
\]

Since

\[
\frac14>\frac{2}{15},
\]

the set of starting points `x` in any dyadic scale for which the PNT fails on

\[
[x,x+x^{1/4}]
\]

has density zero.

In particular, outside a set of measure `o(X)` on `[X,2X]`, such a short
interval contains a prime for large X.  Prime powers do not change this
consequence: an interval of length `X^(1/4)` with no prime has only
`O(log^2 X)` von Mangoldt mass from higher prime powers, which is
`o(X^(1/4))`, so it cannot satisfy the short-interval PNT.

No quantitative exceptional exponent from Gafni–Tao is required below; density
zero is sufficient.

---

## 3. B40 — a supercritical gap opens a macroscopic PRE block

Fix one consecutive prime gap

\[
a<b=a+g
\]

with

\[
g\ge(3+\eta)a^{1/3}.
\]

Choose fixed real constants

\[
\boxed{
\frac{3}{3+\eta}<t_0<t_1<1.
}
\]

Consider integers k in

\[
\boxed{
I_a=
[t_0a^{2/3},t_1a^{2/3}]
\cap\mathbb Z.
}
\]

For sufficiently large a, every such k is PRE_HORIZON.

Indeed,

\[
k+1<t_1a^{2/3}+1<a^{2/3}
\]

eventually, so

\[
(k+1)^3<a^2.
\]

By Supplement 08 this is equivalent to

\[
F_3(k)<a.
\]

Thus the whole block lies before the horizon reaches the left endpoint of the
gap.

Its cardinality is

\[
\boxed{
|I_a|
=
(t_1-t_0+o(1))a^{2/3}.
}
\]

---

## 4. B41 — uniform reciprocal-window width

For k in `I_a`, the real reciprocal q-window is

\[
W_k=
\left(
\frac{U}{b},
\frac{A}{a}
\right],
\]

where

\[
A=k^3,\qquad U=A+3k^2+3k.
\]

Its exact length is

\[
\begin{aligned}
|W_k|
&=
\frac{A}{a}-\frac{U}{b}\\
&=
\frac{Ab-aU}{ab}\\
&=
\boxed{
\frac{k^3g-3ak(k+1)}{ab}.
}
\end{aligned}
\]

Write

\[
k=t\,a^{2/3}
\]

with `t` in the fixed compact interval `[t0,t1]`, up to integer rounding.

Using

\[
g\ge(3+\eta)a^{1/3},
\]

the numerator has leading coefficient

\[
t^2\bigl((3+\eta)t-3\bigr)a^{7/3}.
\]

Our choice

\[
t_0>\frac{3}{3+\eta}
\]

makes this coefficient uniformly positive.

Also

\[
b=a+O(a^{1/3})=(1+o(1))a.
\]

Therefore there is a constant

\[
c_{\eta,t_0,t_1}>0
\]

such that, for all sufficiently large a and every k in `I_a`,

\[
\boxed{
|W_k|
\ge
c_{\eta,t_0,t_1}a^{1/3}.
}
\]

Moreover both endpoints are at scale a:

\[
\boxed{
W_k\subset[c_0a,c_1a]
}
\]

for positive constants `c0,c1` depending only on `t0,t1`.

Thus one supercritical cofactor gap creates an entire family of q-windows of
cube-root length at the prime scale a.

---

## 5. B42 — the selected q-windows have bounded overlap

Let

\[
H_k=\frac{k^3}{a}
\]

be the right endpoint of `W_k`.

Then

\[
H_{k+1}-H_k
=
\frac{3k^2+3k+1}{a}.
\]

On `I_a`,

\[
k\asymp a^{2/3},
\]

so

\[
\boxed{
H_{k+1}-H_k
\asymp
a^{1/3}.
}
\]

For the theorem below we do not need an upper bound on the full `W_k`
length.  Since B41 gives the uniform lower bound
`|W_k| >= c_1 a^(1/3)`, choose a fixed terminal subwindow

\[
J_k\subset W_k
\]

of length

\[
c a^{1/3}
\]

for some `0<c<c_1`, placed immediately to the left of `H_k`.  Thus every
`J_k` lies in

\[
[H_k-ca^{1/3},H_k].
\]

Because the right endpoints advance by `asymp a^(1/3)`, the selected `J_k`
have

\[
\boxed{O_{\eta,t_0,t_1}(1)}
\]

overlap multiplicity, regardless of whether the original prime gap is merely
critical-scale or much larger.

This bounded-overlap fact is what converts an almost-all theorem in q-space
into an almost-all statement in k-space.

---

## 6. B43 — almost every activated q-window contains a prime

Let

\[
\theta=\frac14.
\]

Suppose `W_k` contains no prime.

Because

\[
|W_k|\gg a^{1/3}
\]

while

\[
x^{1/4}\asymp a^{1/4}
=o(a^{1/3})
\]

throughout the q-scale under consideration, one can choose a real subinterval

\[
J_k'\subset J_k
\]

of length

\[
\gg a^{1/3}
\]

such that, for every starting point x in `J_k'`,

\[
[x,x+x^{1/4}]
\subset W_k.
\]

Every one of these short intervals contains no prime.  Hence every x in
`J_k'` belongs to the Gafni–Tao exceptional set for the short-interval PNT
once a is sufficiently large.

The relevant q-scale is contained in finitely many dyadic intervals
`[X,2X]` with `X\asymp a`.  The external theorem therefore gives total
exceptional measure

\[
o(a).
\]

The selected `J_k'` have bounded overlap, so if `E_a` is the set of k in
`I_a` whose reciprocal window contains no prime, then

\[
|E_a|\,a^{1/3}
\ll
o(a).
\]

Therefore

\[
\boxed{
|E_a|
=
o(a^{2/3}).
}
\]

Equivalently,

\[
\boxed{
\#\{k\in I_a:W_k\text{ contains a prime}\}
=
|I_a|-o(a^{2/3}).
}
\]

---

## 7. B44 — prime occupancy becomes full cubic non-forcing

For k in `I_a`, every prime q in `W_k` satisfies

\[
q\asymp a.
\]

But

\[
k\asymp a^{2/3}.
\]

Thus, for all sufficiently large a,

\[
\boxed{q>k.}
\]

Supplement 08 B38 then applies: the e=1 failure generated by `(a,b)` is already
a full singleton-support non-forcing witness.

Hence, for all but `o(a^(2/3))` k in `I_a`,

\[
\boxed{
\text{the cubic basin has a fully non-forced lower-band candidate}.
}
\]

Since `|I_a|\asymp a^(2/3)`, one fixed supercritical gap creates

\[
\boxed{
\gg_{\eta}a^{2/3}
}
\]

full cubic non-forcing basins.

---

## 8. Corollary — infinite supercritical gaps imply infinite cubic failures

Suppose there are infinitely many consecutive prime gaps

\[
a_j<b_j
\]

with

\[
a_j\to\infty
\]

and, for one fixed `eta>0`,

\[
b_j-a_j
\ge
(3+\eta)a_j^{1/3}.
\]

B44 produces full non-forcing cubic basins at k-scale

\[
k\asymp a_j^{2/3}.
\]

These scales tend to infinity with `a_j`.

Therefore

\[
\boxed{
\text{infinitely many }(3+\eta)\text{-supercritical cofactor gaps}
\Longrightarrow
\text{infinitely many cubic full-forcing failures}.
}
\]

More strongly, each gap produces a burst of asymptotically positive relative
size inside its own activation block.

This is conditional on the supercritical gaps.  No such infinite prime-gap
theorem is known or claimed here.

---

## 9. Why the upper density-zero strategy reverses in the lower band

Supplement 07 proved that cubic **upper** pure-cap failures have natural
density zero.

There the logic was:

1. one upper opening event requires a long prime-free interval to the right of
   the factor horizon;
2. the cubic horizons themselves are spaced on the same cube-root scale;
3. each exceptional prime gap can therefore hit only a small number of sampled
   horizons;
4. almost-all short-interval results suppress the sampled opening events.

The lower PRE_HORIZON band behaves in the opposite way.

A fixed supercritical cofactor gap can remain ahead of the horizon for a block

\[
\asymp a^{2/3}
\]

long in k.

During that whole block it generates reciprocal q-windows of length

\[
\asymp a^{1/3}.
\]

The almost-all short-interval theorem now says that **almost all those windows
contain primes**.

Therefore the external theorem fills the failure windows rather than removing
them:

\[
\boxed{
\text{upper band: almost-all prime theory suppresses failures;}
}
\]

\[
\boxed{
\text{lower band: conditional on one supercritical gap,
almost-all prime theory amplifies failures.}
}
\]

This is a sharp negative boundary for any attempt to copy the upper density-zero
proof directly to the lower cofactor band.

---

## 10. Lifecycle interpretation — a long precursor and a short horizon pulse

For a gap on the fixed critical scale

\[
g\asymp a^{1/3},
\]

the PRE activation block, once genuinely supercritical, has length

\[
\asymp a^{2/3}.
\]

By contrast, while the factor horizon is physically inside the fixed gap, its
k-duration is approximately

\[
\frac{g}{dF_3/dk}
\asymp
\frac{a^{1/3}}{a^{1/3}}
=
O(1).
\]

The exact endpoints are

\[
K_{\ge}(a)
\le k<
K_{\ge}(b).
\]

Thus one fixed supercritical gap has a strongly asymmetric lifecycle:

\[
\boxed{
\text{long lower PRE precursor}
\quad\to\quad
\text{short upper horizon pulse}
\quad\to\quad
\text{retirement}.
}
\]

This explains why counting only post-horizon events can dramatically
underestimate the effect of a gap on the full forcing language.

---

## 11. Conditional trichotomy for the remaining cubic frontier

The lower cubic frontier can now be separated into three regimes.

### A. Eventually subcritical gaps

If, for every sufficiently large consecutive prime gap,

\[
g<g_{\rm crit}(a),
\]

then the PRE_HORIZON lower mechanism eventually disappears completely.

This condition is sufficient, not currently proved.

### B. Uniformly supercritical gaps infinitely often

If there exists one fixed

\[
\eta>0
\]

and infinitely many gaps with

\[
g\ge(3+\eta)a^{1/3},
\]

then B44 gives infinitely many full cubic failures, in large bursts.

### C. Critical boundary

The unresolved knife-edge is

\[
\boxed{
g=3a^{1/3}+o(a^{1/3}).}
\]

Here the reciprocal q-window may have only lower-order width, so the fixed
`theta=1/4` amplification argument above no longer gives a uniform
`a^(1/3)` window.

The exact arithmetic compiler remains valid, but sharper information about
prime gaps and reciprocal prime occupancy would be required.

---

## 12. Relation to current external prime-gap technology

Gafni–Tao's published short-interval theorem gives:

- PNT in **all** intervals only above exponent `17/30` using the zero-density
  input stated in their paper;
- PNT in **almost all** intervals above exponent `2/15`.

The cubic critical gap exponent is

\[
\frac13.
\]

Thus the almost-all theorem is strong enough for the amplification theorem once
a supercritical gap is supplied, but the all-interval statement does not rule
out cube-root-scale prime gaps.

This is exactly why the remaining question is now located at the **existence
and frequency of cube-root-scale consecutive prime gaps**, not at ordinary
prime occupancy inside the reciprocal q-windows.

---

## 13. Status and ownership boundary

Internal R005-B results:

- supercritical activation block;
- exact reciprocal-window width formula;
- bounded-overlap transport geometry;
- q>k promotion from e=1 failure to full non-forcing;
- gap-amplification interpretation;
- lower-vs-upper no-go boundary.

External prior mathematics:

- prime number theorem in almost all short intervals;
- specifically the Gafni–Tao 2026 theorem used at `theta=1/4`.

Generic witness semantics remain R005-A/A2/A4 ownership.

No claim is made that:

- infinitely many `(3+eta)a^(1/3)` prime gaps exist;
- only finitely many exist;
- cubic full forcing is eventually true or false;
- lower-band failures have density zero;
- the conditional amplification theorem is a classical-priority novelty claim.

The practical frontier has therefore changed from

`scan cubic witnesses`

to

\[
\boxed{
\text{classify consecutive prime gaps relative to }
3a^{1/3}
}
\]

with the exact critical boundary retained.
