# P022 — Two-Sided Barlow Repair as Wall Local Time of a Rotated `Z^2` Walk

Status: `ACTIVE RESEARCH NOTE / EXACT INTEGER COORDINATE EQUIVALENCE / PRIOR-ART SENSITIVE`  
Owner: `program/p022-geometry-v2`  
Depends on: two-sided event repair; `B_2/C_2` quotient-path interpretation  
Cross-route relevance: P018/P023 quotient repair; A5 symmetry geometry

## 1. Integer rotation

Let the two labelled signed Barlow prefix drifts be

\[
S_t=\sum_{j\le t}\sigma_j,
\qquad
T_t=\sum_{j\le t}\tau_j,
\]

with `sigma_j,tau_j in {−1,+1}`.

Define

\[
\boxed{
U_t=\frac{S_t+T_t}{2},
\qquad
V_t=\frac{S_t-T_t}{2}.
}
\]

Because `S_t` and `T_t` have the same parity, `U_t,V_t` are always integers.

For one microscopic step:

- if `(sigma,tau)=(+,+)`, then `(Delta U,Delta V)=(+1,0)`;
- if `(−,−)`, then `(−1,0)`;
- if `(+,-)`, then `(0,+1)`;
- if `(−,+)`, then `(0,−1)`.

Hence

\[
\boxed{(U_t,V_t)}
\]

is exactly a standard nearest-neighbor cardinal walk on `Z^2`, with the four steps occurring once each among the four microscopic sign pairs.

This is a bijective integer coordinate change on the reachable parity sublattice.

## 2. P022-RW01 — orientation repair is diagonal-wall local time

A one-sided orientation bit is born whenever `S_t=0` or `T_t=0` before the next microscopic step.

Under the rotation,

\[
S_t=U_t+V_t,
\qquad
T_t=U_t-V_t.
\]

Therefore the two zero conditions become the two diagonal reflection walls

\[
\boxed{U+V=0,\qquad U-V=0.}
\]

Every cardinal step from one of these lines leaves that line.  At the origin both lines are present simultaneously, matching the two independent initial orientation bits.

Thus the total zero-departure/orientation count equals the multiplicity-weighted number of visits to the two diagonal walls before a next step.

## 3. P022-RW02 — side-label repair is coordinate-wall departure count

The side-label ambiguity occurs exactly when the two absolute drifts agree and are nonzero:

\[
|S_t|=|T_t|>0.
\]

Since

\[
S_t^2-T_t^2=4U_tV_t,
\]

this is equivalent to

\[
\boxed{U_tV_t=0,\qquad (U_t,V_t)\ne(0,0).}
\]

So the relevant locus is the union of the two coordinate axes, with the origin excluded.

At a nonzero point on a coordinate axis, exactly two of the four cardinal steps remain on that axis and exactly two leave it.  The latter are precisely the microscopic transitions for which the two equal absolute channels split and one side-label bit is born.

Therefore

\[
\boxed{
B=\#\{\text{departures from the nonzero coordinate-axis union}\}.
}
\]

## 4. P022-RW03 — total repair is a four-wall statistic

The four lines

\[
U=0,
\quad V=0,
\quad U=V,
\quad U=-V
\]

are exactly the four reflection walls of the rank-two `B_2/C_2` arrangement.

The total repair dimension is therefore

\[
\boxed{
r=E+B,
}
\]

where

- `E` is diagonal-wall local time counted before departure, with wall multiplicity at intersections;
- `B` is nonzero coordinate-wall departure count.

This recovers the earlier path-lift theorem in a simpler dynamical coordinate system: instead of two coupled signed one-dimensional walks, the microscopic state is one ordinary two-dimensional lattice walk interacting with a four-wall arrangement.

## 5. Mean formulas become wall-local-time formulas

The previous microscopic-average theorem gives

\[
\overline E_N
\sim
2\sqrt{\frac{2N}{\pi}},
\]

and

\[
\overline B_N
=
2\sqrt{\frac N\pi}
-
\frac{\log N}{\pi}
+O(1).
\]

The rotated-walk theorem identifies their geometric meaning:

- the first term is the combined local time of the two diagonal walls;
- the second is the departure local time of the two coordinate walls;
- the negative logarithmic correction removes the intersection state at the origin, where both coordinate walls meet but no side-label split occurs.

Thus

\[
\boxed{
\overline r_N
=
2(1+\sqrt2)\sqrt{\frac N\pi}
-
\frac{\log N}{\pi}
+O(1)
}
\]

is a four-wall interaction law for a standard `Z^2` walk.

## 6. Why this is a stronger structural reduction

The earlier `B_2/C_2` quotient note identified repair with stabilizer release in orbit space.  The present theorem additionally gives an explicit **free microscopic dynamics**:

\[
\boxed{
\text{two Barlow sign streams}
\longleftrightarrow
\text{one cardinal }\mathbb Z^2\text{ walk}.
}
\]

All repair complexity is moved from the transition rule into four static integer walls.

That makes several previously separate questions one problem:

- exact mean repair;
- repair variance and covariance;
- tail bounds;
- wall-type collision statistics;
- extension to higher signed-permutation quotients.

The next high-value frontier is therefore the joint local-time law of these walls, especially the covariance between diagonal-wall visits and coordinate-wall departures needed for the exact total repair variance.

## 7. Foundation/backflow candidate

The project-level structure suggested by this specialization is:

> when an observation quotient is a finite reflection-group orbit map and microscopic dynamics becomes a free lattice walk in adapted integer coordinates, exact repair can be represented by stabilizer-wall interaction counts.

P022 does not promote this as a general A2 theorem.  A valid abstraction must first test higher-rank arrangements, nonreflection actions, simultaneous wall intersections, and cases where path-lift branching is not local in one quotient transition.

## 8. Prior-art discipline

The linear coordinate change, planar simple random walk, Weyl/reflection arrangements and random-walk local time are classical.  No novelty claim is made for them.

The P022-specific result is the exact identification of the two-sided Barlow coordination repair process with this four-wall `B_2/C_2` walk statistic and its use as a finite-precision state-repair model.

## 9. Executable assets

Added:

- `src/enterprise_math/p022_barlow_rotated_walk.py`;
- `tests/test_p022_barlow_rotated_walk.py`.

The tests exhaust short microscopic sign-pair words and verify that the integer rotation is always a cardinal `Z^2` walk and that both wall mechanisms exactly equal the pre-existing `E` and `B` repair counts.
