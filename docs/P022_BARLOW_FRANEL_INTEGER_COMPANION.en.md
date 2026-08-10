# P022 — Integer Normal Form for the Franel Midpoint Companion

Status: `ACTIVE RESEARCH NOTE / EXACT NORMALIZATION / SAME MIDPOINT-COMPANION FAMILY`  
Owner: `program/p022-geometry-v2`  
Depends on: `P022_BARLOW_FRANEL_MIDPOINT_OFFSET`  
Boundary: this is an integer normalization of the same theorem family, not a second mother theorem.

## 1. Rational companion recalled

For a forced-midpoint prime `p = 5 or 7 (mod 8)`, put

\[
m=(p-1)/2.
\]

The midpoint-offset result defines

\[
G_0=0,\qquad G_1=1,
\]

with

\[
8(2d+1)^2G_{d+1}
=(2d-1)^2G_{d-1}-(28d^2+1)G_d,
\]

and proves

\[
F_{m-d}\equiv G_dF_{m-1}\pmod p
\qquad(0\le d<m).
\]

## 2. P022-LI30 — integer companion

For `d>=1`, define

\[
S_d=8^{d-1}((2d-1)!!)^2,
\qquad
H_d=S_dG_d,
\]

and set `H_0=0`.

Since

\[
\frac{S_{d+1}}{8(2d+1)^2}=S_d,
\qquad
\frac{S_d}{S_{d-1}}=8(2d-1)^2,
\]

the rational recurrence becomes

\[
\boxed{
H_{d+1}
=-(28d^2+1)H_d
+8(2d-1)^4H_{d-1}.}
\]

The initial values are

\[
H_0=0,\qquad H_1=1,
\]

so this recurrence proves inductively that every `H_d` is an integer.

The first values are

\[
0,1,-29,3925,-1138025,586364625,-470774258325,\ldots
\]

## 3. P022-LI31 — zero geometry from one integer recurrence

If `0<d<m`, then every prime factor of `S_d` is smaller than `p`, hence

\[
p\nmid S_d.
\]

Therefore multiplication by `S_d` does not change the zero test modulo `p`:

\[
\boxed{
p\mid F_{m-d}\iff p\mid H_d.}
\]

Thus the complete left-half Franel zero alphabet for every forced-midpoint prime is controlled by prime divisors of one fixed integer sequence `H_d`.

This removes both fraction reduction and modular inversion from the zero query.

## 4. P022-LI32 — reversible two-state transfer

Write

\[
\binom{H_{d+1}}{H_d}
=
T_d
\binom{H_d}{H_{d-1}},
\qquad
T_d=
\begin{pmatrix}
-(28d^2+1)&8(2d-1)^4\\
1&0
\end{pmatrix}.
\]

Then

\[
\boxed{\det T_d=-8(2d-1)^4.}
\]

For `d<m`, this determinant is a unit modulo `p`.  Hence the companion dynamics is reversible as a two-coordinate state throughout the entire forced-midpoint window.

For two independent solutions with initial data `(0,1)` and `(1,0)`, their Casoratian is

\[
\boxed{
W_d=(-8)^d((2d-1)!!)^4.}
\]

In particular, the two coordinates cannot simultaneously lose rank modulo a forced prime inside the legal window.

## 5. Prior-art boundary

The generic facts that the Franel three-term recurrence has a two-dimensional solution space, and that a Casoratian controls two independent solutions, are not new.  Joseph Tonien (2026) explicitly develops the two-dimensional Franel sequence space, its standard basis, and an exact Casoratian formula for the ordinary Franel recurrence while studying a Ramanujan-Machine continued fraction.

Accordingly, this note does **not** claim novelty for two-dimensional recurrence spaces, transfer matrices, or Casoratian arguments.  The research-specific object here is the forced-midpoint re-centering together with the fixed integer sequence `H_d` and its use as an exact zero-alphabet coordinate for the P022 half-defect problem.  Historical novelty of that package remains unverified.

## 6. Interpretation and boundary

The zero event `p|H_d` is therefore not caused by a singular transfer step.  It is a genuine crossing of a coordinate-zero set inside an otherwise reversible finite two-state dynamics.

This is useful for P018/P023 language, but the recurrence remains a P022/Franel specialization.  No generic foundation claim is made here.

## 7. Executable assets

- `src/enterprise_math/p022_barlow_franel_integer_companion.py`
- `tests/test_p022_barlow_franel_integer_companion.py`

The regression checks exact normalization against the rational companion, forced-prime zero-alphabet reconstruction, transfer determinants, and the Casoratian product identity.
