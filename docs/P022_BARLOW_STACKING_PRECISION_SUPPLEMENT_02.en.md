# P022 Barlow Stacking Precision Supplement 02 — Universal Integer Recurrence for Periodic Geodesic Growth

Status: `ACTIVE RESEARCH NOTE / EXACT EVENTUAL RECURRENCE / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: Barlow BG01–BG03  
Prior-art boundary: general geodesic growth of virtually abelian groups is established; this note proves a concrete integer recurrence for the present periodic close-packed contact graphs and does not claim historical priority before a focused audit

## 1. Why the asymptotic growth constant is not the end of the story

The preceding supplement proved that a periodic Barlow stacking of period `L` and drift `D` has shell-total geodesic multiplicity

\[
T_n=\Theta(\lambda^n),
\qquad
\lambda=2+2^{(1+|D|/L)/2}.
\]

That result collapses the infinite tail to one algebraic growth constant, but it discards all finite oscillations and subdominant exponential modes.

The exact shell formula contains more structure. Periodicity forces every prefix-imbalance term into finitely many residue classes, and each residue class generates a constant-coefficient recurrence.

The consequence is stronger:

> **the entire periodic shell-total sequence is eventually C-finite, with one explicit integer recurrence space determined only by `(L,|D|)`.**

Literal period order changes amplitudes and can cancel factors, but it does not create new eigenmodes outside that universal space.

## 2. Rewrite BG01 with signed imbalance

For a non-extreme layer `q=|k|<n`, BG01 gave

\[
L_n(k)=\binom nq
\left[
3\cdot2^n
\left(
2^{-(q+d_k)/2}+2^{-(q-d_k)/2}
\right)-6
\right],
\]

where `d_k=|delta_k|`.

The two exponential terms are symmetric under `delta_k -> -delta_k`. Therefore we may remove the absolute value and write exactly

\[
\boxed{
L_n(k)=\binom nq
\left[
3\cdot2^n
\left(
2^{-(q+\delta_k)/2}+2^{-(q-\delta_k)/2}
\right)-6
\right].
}
\]

Because `q` and `delta_k` have the same parity, both exponents are integers.

This signed form is the key: periodic imbalance is affine on every residue class without any eventual sign case split.

## 3. Periodic residue decomposition

For upward layers, write

\[
q=mL+r,
\qquad0\le r<L.
\]

Then

\[
\delta_q=mD+\delta_r.
\]

Hence

\[
2^{-(q-\delta_q)/2}
=
2^{-(r-\delta_r)/2}
\left(2^{-(L-D)/2}\right)^m,
\]

and

\[
2^{-(q+\delta_q)/2}
=
2^{-(r+\delta_r)/2}
\left(2^{-(L+D)/2}\right)^m.
\]

Downward layers have a different finite phase constant but the same two period multipliers, with the roles of `D` and `-D` exchanged. Thus only the absolute drift matters to the set of possible characteristic modes.

Define the two integer powers

\[
\boxed{
A_+=2^{(L+|D|)/2},
\qquad
A_-=2^{(L-|D|)/2}.}
\]

These are integers because a sum of `L` signs `±1` has the same parity as `L`.

## 4. Binomial residue sums

The weighted layer sums reduce to sequences of the form

\[
S_{r,u}(n)
=
\sum_{m\ge0}\binom n{mL+r}u^m.
\]

Introduce an algebraic element `z` with

\[
z^L=u
\]

and an `L`th root of unity `omega`. The standard root-of-unity filter gives

\[
\boxed{
z^r S_{r,u}(n)
=
\frac1L
\sum_{j=0}^{L-1}
\omega^{-rj}(1+z\omega^j)^n.}
\]

Therefore `S_{r,u}` is a finite linear combination of exponentials whose bases are roots of

\[
(x-1)^L-u.
\]

In BG01 the residue sums are multiplied by `2^n`. Their exponential bases are therefore multiplied by `2`, and the corresponding characteristic polynomial becomes

\[
\boxed{
(x-2)^L-2^L u.}
\]

For the two Barlow period multipliers, `2^L u` is exactly `A_+` or `A_-`.

Thus the non-extreme weighted binomial terms are annihilated by

\[
((x-2)^L-A_+)((x-2)^L-A_-).
\]

## 5. Why unshifted `x^L-A_±` factors also appear

The root-of-unity-filter sums naturally include the residue term `q=n` whenever `n` lies in the selected residue class.

But BG01 applies only to non-extreme layers `q<n`; the true extreme layers have contribution

\[
3^n
\]

rather than the continuation of the non-extreme face formula.

Subtracting the would-be `q=n` residue terms introduces sequences proportional to

\[
2^{(n+\delta_n)/2}
\quad\text{and}\quad
2^{(n-\delta_n)/2}.
\]

Across one full period these multiply by

\[
A_+
\quad\text{or}\quad
A_-.
\]

Hence these boundary-correction sequences are annihilated by

\[
\boxed{
(x^L-A_+)(x^L-A_-).}
\]

The actual extreme-layer replacement itself contributes the pure mode `3^n`.

## 6. The remaining scalar modes

The `-6` part of every non-extreme layer is independent of stacking phase. Summing it over the central layer and the two layers of each positive height produces only constant and `2^n` modes.

Thus the residual scalar factors are

\[
(x-1)(x-2).
\]

The two true extreme layers contribute `2*3^n`, adding

\[
(x-3).
\]

No other exponential mode is needed.

## 7. P022-BG04 — universal eventual characteristic polynomial

Define

\[
\boxed{
\begin{aligned}
Q_{L,D}(x)=\;&(x-1)(x-2)(x-3)\\
&\cdot(x^L-A_+)(x^L-A_-)\\
&\cdot((x-2)^L-A_+)((x-2)^L-A_-),
\end{aligned}}
\]

with

\[
A_\pm=2^{(L\pm|D|)/2}.
\]

Then every periodic Barlow stacking with period length `L` and absolute period drift `|D|` has shell-total geodesic sequence `T_n` satisfying the constant-coefficient recurrence encoded by `Q_{L,D}` for every sufficiently large `n`.

The polynomial is monic, integral, and has degree

\[
\boxed{4L+3.}
\]

With the radius-zero convention `T_0=1` used in the repository, the executable formula satisfies the recurrence from the first index strictly larger than the degree:

\[
\boxed{
Q_{L,D}(E)T_n=0
\qquad(n>4L+3),}
\]

where `E` is the forward-shift operator.

This is a uniform bound, not a minimality claim.

## 8. P022-BG05 — same drift class, one recurrence space

Suppose two periodic stacking words have the same

\[
(L,|D|)
\]

but different interface order.

Their finite prefix phases `delta_r` can differ, so their finite shell totals can differ.

However all phase dependence appears only in the coefficients multiplying the residue-class exponential modes. The possible bases themselves depend only on `L` and `|D|`.

Therefore

\[
\boxed{
\text{same }(L,|D|)
\Longrightarrow
\text{same universal recurrence space}.}
\]

This is strictly stronger than the earlier asymptotic theorem: equal drift density alone fixed only the dominant exponential rate, while equal integer pair `(L,|D|)` fixes a finite universal set of all allowable exponential modes.

Different periods with the same reduced drift density can share the same dominant root but have different subdominant mode sets.

## 9. Rational generating function

Let

\[
G(z)=\sum_{n\ge0}T_nz^n.
\]

An eventually constant-coefficient recurrence is equivalent to a rational ordinary generating function.

A universal integer denominator is the reciprocal characteristic polynomial

\[
\boxed{
\begin{aligned}
R_{L,D}(z)=\;&(1-z)(1-2z)(1-3z)\\
&\cdot(1-A_+z^L)(1-A_-z^L)\\
&\cdot((1-2z)^L-A_+z^L)\\
&\cdot((1-2z)^L-A_-z^L).
\end{aligned}}
\]

After cancellation, the actual denominator of a particular stacking can be smaller.

Therefore

\[
\boxed{
G(z)\in\mathbb Q(z)
}
\]

for every periodic Barlow stacking in this contact-graph geodesic-count language.

This rationality is a property of the concrete close-packed family and should not be confused with a universal statement about all exponential geodesic-growth systems.

## 10. Dominant root recovered automatically

Among the factors of `Q`, the largest positive real root comes from

\[
(x-2)^L-A_+.
\]

Therefore

\[
(x-2)^L=A_+
=2^{(L+|D|)/2},
\]

which gives

\[
\boxed{
x=2+2^{(1+|D|/L)/2}.}
\]

Thus BG03's drift-controlled growth constant is not an independent asymptotic accident. It is the dominant root of the exact recurrence space.

The recurrence theorem therefore strengthens and structurally explains the growth theorem.

## 11. Examples and factor cancellation

### FCC

Take `L=1`, `|D|=1`. Then

\[
A_+=2,
\qquad A_-=1.
\]

The universal polynomial contains repeated copies of roots `1,2,3`, while the actual FCC closed form uses only

\[
1,2,3,4.
\]

After cancellation/minimalization, the familiar order-four recurrence remains.

### HCP

Take `L=2`, `D=0`. Then

\[
A_+=A_-=2.
\]

The two unshifted factors coincide and the two shifted factors coincide. The universal polynomial is therefore highly nonminimal.

The actual HCP sequence is annihilated by the smaller characteristic

\[
(x-1)(x-2)(x-3)(x^2-2)(x^2-4x+2),
\]

which is exactly the order-seven recurrence already recorded in the HCP supplement.

### Period `(-,-,+)`

Here

\[
L=3,
\quad |D|=1,
\quad A_+=4,
\quad A_-=2.
\]

The universal mode factors are

\[
x^3-4,
\quad x^3-2,
\]

and

\[
(x-2)^3-4,
\quad (x-2)^3-2,
\]

plus `1,2,3`.

The dominant root is

\[
2+2^{2/3}.
\]

## 12. Finite-state interpretation

For the shell-total future language of a periodic Barlow stacking, the infinite future sequence does not require preserving all future shell values independently.

BG04 gives a uniform recurrence-state bound:

\[
\boxed{
\text{after a finite warm-up, at most }4L+3
\text{ previous integer values suffice to generate the entire future}.}
\]

This bound is often reducible after factor cancellation, but it is explicit and depends only on period length.

So the sequence of legal compressions now extends one step further:

\[
\text{literal stacking word}
\to
\text{queried prefix imbalances}
\to
\text{finite shell trajectory}
\to
(L,|D|)+\text{finite recurrence amplitudes/state}
\to
\text{dominant drift growth constant}.
\]

Each arrow corresponds to a weaker declared future language.

## 13. Prior-art discipline

General geodesic growth in finitely generated/virtually abelian settings has an established literature, including results on holonomicity and exponential versus polynomial geodesic growth.

This P022 result is narrower and more explicit: a concrete rational generating function / integer recurrence family for periodic Barlow contact graphs, derived from their exact close-packing interface polynomial.

Until a dedicated source search establishes historical independence, retain

`NOVELTY_UNVERIFIED`.

## 14. Executable reference

`p022_barlow_growth.py` now provides:

- `period_exponential_weights`;
- `universal_growth_characteristic_polynomial`;
- `universal_growth_generating_denominator`;
- `recurrence_residual`.

Tests construct the recurrence from `(L,|D|)` **before** generating the shell sequence and verify it on every ± period of length at most four. They also verify that different finite sequences with the same `(L,|D|)` are annihilated by the same universal characteristic.
