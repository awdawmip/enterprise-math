# P022 — The Midpoint Companion Is a Half-Integer Franel Solution

Status: `ACTIVE RESEARCH NOTE / EXACT RECURRENCE IDENTIFICATION / PRIOR-ART SENSITIVE`  
Owner: `program/p022-geometry-v2`  
Depends on: universal midpoint-offset companion; classical Franel recurrence-space theory  
Cross-route relevance: P011 identifiability; P018 defect/holonomy; P023 quotient-stable witness state

## 1. The rational companion has a cleaner gauge

The midpoint-offset theorem introduced the universal rational sequence

\[
G_0=0,
\qquad
G_1=1,
\]

\[
8(2d+1)^2G_{d+1}
=(2d-1)^2G_{d-1}-(28d^2+1)G_d.
\]

Define

\[
\boxed{Y_d=(-8)^dG_d.}
\]

Then `Y_0=0`, `Y_1=-8`, and the sign/scale gauge transforms the recurrence into

\[
\boxed{
(2d+1)^2Y_{d+1}
=(28d^2+1)Y_d
+8(2d-1)^2Y_{d-1}.}
\]

This is no longer an unfamiliar recurrence.

---

## 2. P022-LI34 — exact half-integer specialization of the Franel recurrence

The classical Franel recurrence is

\[
(n+1)^2f_{n+1}
=(7n^2+7n+2)f_n+8n^2f_{n-1}.
\]

Substitute the half-integer parameter

\[
n=d-\frac12.
\]

Then

\[
4(n+1)^2=(2d+1)^2,
\]

\[
4(7n^2+7n+2)=28d^2+1,
\]

and

\[
4\cdot8n^2=8(2d-1)^2.
\]

Therefore the recurrence becomes exactly

\[
(2d+1)^2f_{d+1/2}
=(28d^2+1)f_{d-1/2}
+8(2d-1)^2f_{d-3/2}.
\]

Hence:

\[
\boxed{
Y_d\text{ is a canonical solution of the Franel recurrence on the half-integer lattice }d-\tfrac12.}
\]

The midpoint companion is therefore not a new unrelated recurrence object.  It is a specific half-integer member of the same polynomial recurrence family.

---

## 3. P022-LI35 — half-integer Casoratian

Let `X,Y` be the two canonical half-integer-lattice solutions defined by

\[
X_0=1,\quad X_1=0,
\]

\[
Y_0=0,\quad Y_1=-8.
\]

Define

\[
W_d=X_dY_{d+1}-X_{d+1}Y_d.
\]

Writing the recurrence in forward form gives the second-solution coefficient

\[
B_d=
\frac{8(2d-1)^2}{(2d+1)^2}.
\]

For any second-order recurrence,

\[
W_d=-B_dW_{d-1}.
\]

Since

\[
W_0=-8,
\]

telescoping the odd-factor ratios gives

\[
\boxed{
W_d
=
\frac{(-8)^{d+1}}{(2d+1)^2}.}
\]

This is the exact half-integer analogue of the classical Franel Casoratian formula.

It proves in particular that the two half-lattice solutions remain linearly independent at every finite step.

---

## 4. P022-LI36 — positive integer normalization

Define

\[
K_0=0,
\qquad
K_1=1,
\]

and for `d>=1`,

\[
\boxed{
K_{d+1}
=(28d^2+1)K_d
+8(2d-1)^4K_{d-1}.}
\]

All coefficients are positive integers, so

\[
\boxed{K_d\in\mathbb Z_{>0}\quad(d\ge1).}
\]

Direct normalization gives

\[
\boxed{
K_d
=
-\frac{((2d-1)!!)^2}{8}Y_d
=
(-1)^{d-1}8^{d-1}((2d-1)!!)^2G_d.}
\]

Thus the denominator-clearing implicit in the rational companion is controlled by one natural odd-double-factorial gauge.

The first values are

\[
\boxed{
0,1,29,3925,1138025,586364625,470774258325,\ldots}
\]

No direct prior sequence match was found in the current targeted search; this is not a novelty claim.

---

## 5. P022-LI37 — zero geometry can be read directly from the integer sequence

Let `p` be a forced-midpoint prime and

\[
m=\frac{p-1}{2}.
\]

For every

\[
1\le d<m,
\]

we have

\[
p>2d+1.
\]

Hence `p` divides none of

\[
8,1,3,5,\ldots,2d-1.
\]

The normalization factor between `G_d` and `K_d` is therefore a `p`-adic unit.  Combining with the midpoint companion theorem gives

\[
\boxed{
p\mid F_{m-d}
\iff
p\mid G_d
\iff
p\mid K_d.}
\]

So the rational numerator `N_d` may be replaced by the positive integer sequence `K_d` throughout the actual forced-midpoint zero window.

Consequently

\[
\boxed{
Z_p
=
\{m\}
\cup
\{m-d,m+d:1\le d<m,\ p\mid K_d\}.}
\]

and

\[
\boxed{
r_p=m-\max\{d<m:p\mid K_d\},}
\]

with the maximum interpreted as zero when there is no hit.

---

## 6. Connection with the Franel continued-fraction recurrence

A 2026 study of Franel numbers and a Ramanujan-Machine continued fraction uses the Euler--Wallis recurrence

\[
p_n
=(7n^2+7n+2)p_{n-1}+8n^4p_{n-2}
\]

and shows that factorial normalization connects it to the ordinary Franel recurrence.

Set

\[
P_d=\frac{K_d}{4^{d-1}}
\qquad(d\ge1).
\]

Then the integer recurrence for `K` gives

\[
P_{d+1}
=\left(7d^2+\frac14\right)P_d
+\frac{(2d-1)^4}{2}P_{d-1}.
\]

With

\[
x=d-\frac12,
\]

we have

\[
7x^2+7x+2=7d^2+\frac14,
\]

and

\[
8x^4=\frac{(2d-1)^4}{2}.
\]

Therefore

\[
\boxed{
P_{d+1}
=(7x^2+7x+2)P_d+8x^4P_{d-1},
\qquad x=d-\frac12.}
\]

So `P_d` is exactly the **half-integer polynomial specialization** of the Euler--Wallis recurrence appearing in that continued-fraction theory.

The published work studies the ordinary integer-index recurrence/solution space.  The present midpoint half-integer specialization and its use for Franel zero geometry remain P022-specific unless prior art is later found.

---

## 7. Why this is useful for the remaining arithmetic problem

The support-cancellation frontier is now entirely integer:

\[
\boxed{
\text{canonical A-support offset }d
\quad\text{is dangerous iff}\quad
p\mid K_d.}
\]

The sequence `K_d` has a positive second-order recurrence and an exact half-integer Franel/continued-fraction interpretation.  This opens tools that were awkward in the rational `G_d=N_d/Q_d` formulation:

- gcd and primitive-divisor questions for an integer sequence;
- modular recurrence/orbit analysis;
- Casoratian arguments;
- continued-fraction/recurrence-space comparison;
- prime-halving support-tree intersection tests.

It does not by itself prove support avoidance.

---

## 8. Prior-art boundary

Established inputs:

- the classical Franel recurrence;
- generic second-order recurrence/Casoratian algebra;
- the 2026 integer-index Franel sequence-space and continued-fraction recurrence analysis.

Reference: Joseph Tonien, *Franel Numbers and a Continued Fraction Conjecture Discovered by the Ramanujan Machine*, The Mathematical Intelligencer (2026), DOI `10.1007/s00283-025-10497-9`.

P022-specific results:

- the half-integer gauge identification of the midpoint companion;
- its natural positive integer normalization `K_d`;
- the exact forced-midpoint zero criterion `p|F_(m-d) iff p|K_d`;
- the use of that sequence as the integer state of the remaining support-avoidance problem.

Historical novelty remains `NOVELTY_UNVERIFIED`.

---

## 9. Executable assets

Added:

- `src/enterprise_math/p022_barlow_franel_half_integer_solution.py`;
- `tests/test_p022_barlow_franel_half_integer_solution.py`.

The tests verify the shifted recurrence, integer normalization, exact first values, zero-offset reconstruction, Casoratian formula, and the half-step Euler--Wallis recurrence with rational arithmetic only.
