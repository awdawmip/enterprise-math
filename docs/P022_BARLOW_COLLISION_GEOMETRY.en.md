# P022 — Collision Polynomial as an Unordered Checkpoint-Geometry Code

Status: `ACTIVE RESEARCH NOTE / EXACT P011 SPECIALIZATION / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: P011 collision-polynomial completeness; `P022_BARLOW_FIBER_CONVOLUTION.*`

## 1. Two inverse theorems compose

P011 proves that the complete collision coefficients

\[
(J_1,J_2,\ldots,J_M)
\]

recover the complete finite fiber-size profile by integer binomial inversion.

The P022 fiber-convolution theorem proves that a selected-layer Barlow fiber profile recovers

\[
(\{\ell_1,\ldots,\ell_m\},u),
\]

the multiset of observed segment lengths together with the completely unobserved tail length.

Therefore these two inverse maps compose exactly.

## 2. P022-CG01 — exact collision-polynomial inversion

Let

\[
K_O(t)=\sum_{k\ge1}J_k(O)t^k
\]

be the complete P011 collision polynomial of a Barlow selected-layer quotient.

Then

\[
\boxed{
K_O(t)
\Longleftrightarrow
(\{\ell_1,\ldots,\ell_m\},u).
}
\]

The right-hand side is the unordered checkpoint interval geometry plus hidden tail.

The inversion is entirely integer and finite:

1. P011 binomial inversion reconstructs each `c_s`;
2. the minimum represented fiber size gives `2^u` and hence `u`;
3. divide all fiber sizes by `2^u`;
4. triangular binomial-profile peeling recovers every segment length and multiplicity.

## 3. Segment order is the sharp current loss

The collision polynomial cannot distinguish segment order because the complete fiber profile is a commutative multiplicative convolution.

For example segment sequences

\[
(1,2,3)
\]

and

\[
(3,2,1)
\]

produce the same collision polynomial, but their checkpoint layers are

\[
(1,3,6)
\]

and

\[
(3,5,6).
\]

Thus the collision polynomial identifies the **multiset geometry**, not the ordered placement.

## 4. Low-order coefficients do not suffice

The exact `J_2` alias theorem gives different segment multisets with fixed `N,m,J_2`. Hence CG01 genuinely needs the complete finite collision state, not merely its first nontrivial coefficient.

The current result does not claim that some small universal prefix `(J_2,...,J_k)` always identifies the geometry. Determining the minimal sufficient collision order is a separate open problem.

## 5. Consequence for P011 interpretation

In general P011's collision polynomial is a complete encoding only of fiber-size statistics, not of the mechanism that created the quotient.

In this Barlow specialization, the quotient fibers have enough triangular binomial structure that the same collision polynomial additionally reconstructs the unordered observation geometry.

Therefore the implication

\[
\boxed{
\text{irreversibility statistics}
\to
\text{observation geometry}
}
\]

is not a universal P011 theorem. It is a P022 structural specialization enabled by the binomial segment factorization.

## 6. Executable assets

- `src/enterprise_math/p022_barlow_collision_geometry.py`;
- `tests/test_p022_barlow_collision_geometry.py`.

The tests round-trip P011 collision coefficients through fiber profiles and recover the segment multiset plus hidden tail across complete finite selected-layer schedule families, while preserving segment-order counterexamples.
