# P022 Barlow Coordination Precision Supplement 01 — Periodic Quasi-Polynomial and Root-of-Unity Recurrence

Status: `ACTIVE RESEARCH NOTE / EXACT INTEGER QUASI-POLYNOMIAL / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: BC04 whole-shell drift-energy formula  
Purpose: characterize the entire future coordination sequence of a periodic stacking, and contrast its algebraic type with geodesic witness multiplicity

## 1. Starting point

For every Barlow stacking and every positive radius `n`, BC04 proved

\[
\boxed{
4S_n=42n^2+8-\delta_n^2-\delta_{-n}^2.}
\]

Now assume the interface word is periodic with period length `L` and signed period drift

\[
D=\sum_{j=0}^{L-1}\sigma_j.
\]

The shell sequence is then much simpler than the geodesic-path sequence.

## 2. P022-BCR01 — every residue subsequence is exactly quadratic

Write

\[
n=mL+r,
\qquad 0\le r<L.
\]

Define the finite phase imbalances

\[
a_r=\delta_r,
\qquad
b_r=\delta_{-r}.
\]

Periodicity gives

\[
\delta_n=mD+a_r,
\]

and

\[
\delta_{-n}=-mD+b_r.
\]

Substitute into BC04:

\[
\boxed{
4S_{mL+r}
=C_{0,r}+C_{1,r}m+C_2m^2,
}
\]

where

\[
\boxed{
C_2=42L^2-2D^2,}
\]

\[
\boxed{
C_{1,r}=84Lr-2D(a_r-b_r),}
\]

and

\[
\boxed{
C_{0,r}=42r^2+8-a_r^2-b_r^2.}
\]

For residue `r=0`, this polynomial is used for `m>=1`; the repository convention `S_0=1` is one special initial value rather than the polynomial continuation.

Therefore

\[
\boxed{
S_n\text{ is an exact quadratic quasi-polynomial of period dividing }L
\text{ for }n>0.}
\]

This is a stronger finite statement than merely knowing the leading `n^2` coefficient.

## 3. Finite phase signature

For a declared period length `L`, define the coordination phase signature

\[
\boxed{
\mathcal C
=\bigl((C_{0,r},C_{1,r},C_2)\bigr)_{r=0}^{L-1}.}
\]

Together with `S_0=1`, this finite integer tuple reconstructs every future shell cardinality exactly.

So an infinite periodic stacking word admits another legal task-relative collapse:

\[
\boxed{
\text{periodic literal word}
\longrightarrow
\mathcal C
\longrightarrow
(S_n)_{n\ge0}.}
\]

The phase signature can be strictly smaller than the literal repeated history. It is not claimed minimal over all possible choices of period representation: a word may have a smaller primitive period, and different signatures may themselves admit a smaller common recurrence.

## 4. P022-BCR02 — universal shell recurrence

Fix one residue class `r`. A quadratic polynomial in `m` has zero third forward difference:

\[
\Delta_m^3 S_{mL+r}=0.
\]

In the original radius variable, one forward step in `m` is a shift by `L`. Therefore

\[
\boxed{
(E^L-1)^3S=0
}
\]

once all four involved shell radii are positive.

Explicitly,

\[
\boxed{
S_n-3S_{n-L}+3S_{n-2L}-S_{n-3L}=0,
\qquad n>3L.}
\]

This recurrence is universal for **every** period-`L` Barlow coordination sequence, regardless of drift or phase.

Its characteristic polynomial is

\[
\boxed{(x^L-1)^3.}
\]

All characteristic roots are roots of unity, with multiplicity at most three. This is exactly the algebraic signature expected from quadratic quasi-polynomial growth.

## 5. P022-BCR03 — universal ball recurrence

Let

\[
B_n=\sum_{r=0}^{n}S_r.
\]

Then

\[
(E-1)B=S
\]

up to the ordinary index convention. Apply BCR02:

\[
\boxed{
(E-1)(E^L-1)^3B=0
}
\]

for sufficiently large indices.

A universal characteristic is

\[
\boxed{
(x-1)(x^L-1)^3,}
\]

with degree

\[
\boxed{3L+1.}
\]

Thus the entire periodic crystal-ball sequence is also C-finite, but with only unit-modulus characteristic roots.

## 6. Rational generating functions

The shell ordinary generating function

\[
G_S(z)=\sum_{n\ge0}S_nz^n
\]

has denominator dividing

\[
\boxed{(1-z^L)^3.}
\]

The ball generating function has denominator dividing

\[
\boxed{(1-z)(1-z^L)^3.}
\]

Finite initial corrections, including the special radius-zero shell value, modify only the numerator.

So periodic coordination sequences are rational for a much simpler reason than periodic path-multiplicity sequences: they are quasi-polynomial rather than exponentially growing.

## 7. Cardinality and multiplicity live in different recurrence algebras

For the same periodic Barlow contact graph we now have two exact future-sequence structures.

### Vertex cardinality

Universal shell characteristic:

\[
(x^L-1)^3.
\]

All roots lie on the unit circle. Polynomial growth arises from repeated unit-modulus roots.

### Geodesic path multiplicity

The preceding BG04 theorem requires expanding factors such as

\[
(x-2)^L-A_+
\]

with dominant real root

\[
2+2^{(1+|D|/L)/2}>3.
\]

So witness multiplicity is not merely “a larger coefficient” on the same sequence type. It belongs to a genuinely different finite recurrence algebra with expanding modes.

This gives a structural version of the earlier precision inequality:

\[
\boxed{
\text{support/cardinality shadow}
\text{ destroys the expanding witness modes}.}
\]

The loss is exact and observable in the characteristic spectrum.

## 8. Same leading coefficient, different finite phase

The quadratic coefficient

\[
C_2=42L^2-2D^2
\]

depends only on `(L,|D|)`.

Lower-order residue coefficients retain finite phase information through

\[
a_r,\ b_r.
\]

Therefore two stacking words with the same period length and absolute drift have the same asymptotic shell coefficient but can have different finite coordination sequences.

For example, two zero-drift period-four words can share

\[
C_2=42\cdot4^2
\]

while differing in `C_{0,r}` / `C_{1,r}` and hence in some finite shell radii.

This is the coordination analogue of the path-growth result: the asymptotic language needs less state than the exact finite future language.

## 9. Relation to known coordination-sequence phenomena

Periodic crystal/contact graphs are often studied through coordination sequences and rational generating functions. The present result should therefore be treated as a concrete Barlow specialization unless a dedicated novelty audit proves otherwise.

The project-specific value is the exact derivation from the stacking precision variable `delta` and its integration with the path-multiplicity hierarchy:

\[
\text{stacking prefix}
\to
\delta
\to
\delta^2
\to
\text{quadratic quasi-polynomial coordination}
\]

versus

\[
\text{stacking prefix}
\to
|\delta|\text{ trajectory}
\to
\text{expanding geodesic-count recurrence}.
\]

These are two different future-language quotients of the same hidden geometry.

## 10. Executable assets

Added:

- `src/enterprise_math/p022_barlow_coordination_recurrence.py`;
- `tests/test_p022_barlow_coordination_recurrence.py`.

The tests verify residue quadratics, shell recurrence, ball recurrence, and finite phase signatures over all short ± periods rather than fitting recurrences from generated data.
