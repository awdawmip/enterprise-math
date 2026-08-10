# P022 — A Universal Midpoint-Offset Companion for Franel Zero Geometry

Status: `ACTIVE RESEARCH NOTE / EXACT UNIVERSAL REDUCTION / PRIOR-ART SENSITIVE`  
Owner: `program/p022-geometry-v2`  
Depends on: Franel recurrence; Jarvis--Verrill forced midpoint zero; p-Lucas zero-digit geometry  
Cross-route relevance: P011 collision identifiability; P018 defect/holonomy; P023 task-relative repair

## 1. Problem

For an odd prime

\[
p\equiv5,7\pmod8,
\]

put

\[
m=\frac{p-1}{2}.
\]

The half-index theorem gives

\[
F_m\equiv0\pmod p.
\]

The complete zero-digit set

\[
Z_p=\{1\le j\le p-1:p\mid F_j\}
\]

was previously described by mirror symmetry, p-Lucas, and the Franel recurrence.  Those facts still appear prime-by-prime.

This note removes the prime from the local midpoint recurrence entirely.  One universal rational sequence encodes the zero geometry of **every** forced-midpoint prime.

---

## 2. Recenter the Franel recurrence at the forced midpoint

The Franel recurrence is

\[
(n+1)^2F_{n+1}
=(7n^2+7n+2)F_n+8n^2F_{n-1}.
\]

At the forced midpoint, modulo `p`,

\[
m\equiv-\frac12.
\]

For an offset `d>=0`, set

\[
n=m-d.
\]

Then

\[
n\equiv-\frac{2d+1}{2},
\qquad
n+1\equiv-\frac{2d-1}{2}
\pmod p.
\]

Also

\[
7n^2+7n+2
\equiv\frac{28d^2+1}{4}\pmod p.
\]

Because adjacent Franel zeros are impossible and `F_m=0`, we have

\[
F_{m-1}\not\equiv0\pmod p.
\]

Normalize by this unit and define

\[
R_d^{(p)}
:=
\frac{F_{m-d}}{F_{m-1}}\pmod p.
\]

Then

\[
R_0^{(p)}=0,
\qquad
R_1^{(p)}=1.
\]

Substituting the recentered coefficients into the recurrence gives

\[
\boxed{
8(2d+1)^2R_{d+1}^{(p)}
=
(2d-1)^2R_{d-1}^{(p)}
-(28d^2+1)R_d^{(p)}.
}
\]

The prime `p` has disappeared from the coefficients.

---

## 3. P022-LI27 — universal midpoint companion

Define a rational sequence

\[
G_0=0,
\qquad
G_1=1,
\]

and for `d>=1`,

\[
\boxed{
8(2d+1)^2G_{d+1}
=
(2d-1)^2G_{d-1}
-(28d^2+1)G_d.
}
\]

For `0<=d<m`, every odd denominator factor appearing in this recurrence is strictly smaller than `p`; hence all denominators are `p`-adic units.

The normalized Franel offsets and `G_d` have identical initial values and satisfy the same recurrence modulo `p`.  Therefore

\[
\boxed{
F_{m-d}
\equiv
G_dF_{m-1}
\pmod p
\qquad(0\le d<m).
}
\]

This is the universal midpoint-companion theorem.

Equivalently, the half-integer recentering of the classical Franel recurrence has a fixed rational solution whose reductions modulo forced-midpoint primes control the entire local zero geometry.

---

## 4. P022-LI28 — zero digits are prime divisors of one universal numerator sequence

Write `G_d` in lowest terms:

\[
G_d=\frac{N_d}{Q_d},
\qquad
\gcd(N_d,Q_d)=1.
\]

For `1<=d<m`, `p` does not divide `Q_d`.  Since `F_(m-1)` is a unit modulo `p`, LI27 yields

\[
\boxed{
p\mid F_{m-d}
\iff
p\mid N_d.}
\]

Thus the **entire** left-half zero geometry is encoded by prime divisors of the fixed integer sequence

\[
N_1,N_2,N_3,\ldots
\]

independently of `p`.

The first values are

\[
\begin{array}{c|r}
d&N_d\\
\hline
1&1\\
2&-29\\
3&157\\
4&-929\\
5&53185\\
6&-42700613\\
7&291801013\\
8&-2037217865
\end{array}
\]

with, for example,

\[
53185=5\cdot11\cdot967.
\]

The signs are irrelevant to the zero criterion.

---

## 5. P022-LI29 — complete zero alphabet and rank of apparition

Jarvis--Verrill reflection gives

\[
j\in Z_p
\iff
p-1-j\in Z_p.
\]

Hence if

\[
H_p
=
\{1\le d<m:p\mid N_d\},
\]

then

\[
\boxed{
Z_p
=
\{m\}
\cup
\{m-d,m+d:d\in H_p\}.}
\]

Therefore

\[
\boxed{
z_p=1+2|H_p|.}
\]

The first zero occurs at the farthest left displacement, so

\[
\boxed{
r_p=m-\max(H_p\cup\{0\}).}
\]

Consequently the earlier primitive-midpoint criterion becomes

\[
\boxed{
p\text{ primitive at }F_m
\iff
p\nmid N_d\text{ for every }1\le d<m.}
\]

So midpoint primitivity is now a universal companion-prime avoidance condition rather than a separate prime-by-prime Franel computation.

---

## 6. Exact examples

### `p=29`

Here

\[
m=14,
\qquad
29\mid N_2.
\]

There are no other companion hits below `m`, so

\[
Z_{29}=\{12,14,16\}
\]

and

\[
r_{29}=12.
\]

This explains the earliest nonprimitive forced midpoint directly from the universal numerator

\[
N_2=-29.
\]

### `p=157`

Here

\[
m=78,
\]

and the companion hits are

\[
d=3,62.
\]

Thus

\[
\boxed{
Z_{157}=\{16,75,78,81,140\},
\qquad
r_{157}=16.}
\]

The near-midpoint pair `75,81` comes from `N_3=157`; the much earlier zero `16` comes from the later numerator `N_62`.

### `p=173`

Here

\[
m=86
\]

and the only left companion hit is

\[
d=82.
\]

Therefore

\[
\boxed{Z_{173}=\{4,86,168\},\qquad r_{173}=4.}
\]

This example shows why the companion theorem is stronger than a bounded-neighborhood midpoint analysis: a zero can occur extremely far from the midpoint while remaining encoded by the same universal sequence.

---

## 7. Consequence for the p-Lucas basin

The p-Lucas zero alphabet no longer needs to be computed directly from all

\[
F_1,\ldots,F_{p-1}.
\]

For forced-midpoint primes it is enough to know which universal companion numerators

\[
N_1,\ldots,N_{m-1}
\]

are divisible by `p`.

Hence the exact nonzero count in a `p^L` block becomes

\[
\boxed{
\left(
 p-1-2\#\{1\le d<m:p\mid N_d\}
\right)^L.
}
\]

This converts the Franel p-Lucas basin into a prime-divisor statistic of one universal companion sequence.

---

## 8. Consequence for the half-defect support problem

Let the canonical central-binomial elimination at the midpoint use earlier indices

\[
S_p\subset\{1,\ldots,m-1\}.
\]

For each `j in S_p`, write the corresponding offset

\[
d=m-j.
\]

Then LI28 gives the exact equivalence

\[
\boxed{
S_p\cap Z_p=\varnothing
\iff
p\nmid N_{m-j}
\quad\text{for every }j\in S_p.}
\]

Thus the empirical support-avoidance question has been reduced to an integer sequence problem:

> do the prime divisors of the universal companion numerators avoid the offset image of the canonical A-elimination support?

This does not yet prove the desired avoidance for the `p=5,23 mod 24` half-defect family, but it removes the Franel table itself from the unknown.

---

## 9. Prior-art boundary

Established mathematics used here includes:

- the classical Franel recurrence;
- Jarvis--Verrill reflection;
- ordinary second-order recurrence uniqueness;
- the general study of the two-dimensional Franel recurrence solution space.

Recent work also explicitly studies the Franel recurrence solution space and its Casoratian/continued-fraction basis.  That is prior art and should not be repackaged as an Enterprise Math invention.

The P022-specific result is the **forced-midpoint half-integer recentering** and the use of its universal rational companion numerator sequence to encode `Z_p`, `r_p`, and the support-avoidance problem across all forced-midpoint primes.

A targeted search has not yet located this exact midpoint-offset numerator formulation.  That absence is not proof of novelty; status remains

`NOVELTY_UNVERIFIED`.

---

## 10. Executable assets

Added:

- `src/enterprise_math/p022_barlow_franel_midpoint_offset.py`;
- `tests/test_p022_barlow_franel_midpoint_offset.py`.

The tests verify the rational recurrence, the first exact numerators, complete reconstruction of Franel zero alphabets on multiple forced primes, and the rank examples `p=29,157,173`.
