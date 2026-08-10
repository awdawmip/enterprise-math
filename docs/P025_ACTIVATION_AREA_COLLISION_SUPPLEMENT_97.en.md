# P025 Supplement 97 — Activation-Area Collision and the `Potential != State` Boundary

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-orbit-normal-stage91`  
Depends on: P025 Supplement 96  
Hard block: `NONE`

## 1. Stage 96 left an explicit injectivity question

The activation area

\[
A=\sum_{k,j}B_{k,j}
\]

is a useful scalar potential for biaxial update accounting.

But a scalar potential is not automatically a sufficient semantic state.

Stage 97 tests the strongest possible failure mode:

> Can two exact arithmetic dyadic states use the same threshold grid and horizon, have the same activation area, yet answer a declared threshold/node future query differently?

Yes.

## 2. Fixed common future grid

Use base exponent

\[
m=2,
\]

horizon

\[
h=1
\]

corresponding to exponents `2,4`, and the same threshold grid

\[
\boxed{T_1=\frac12,
\qquad
T_2=1.}
\]

No threshold metadata or horizon change is allowed between the two compared states.

## 3. P025-C35 — exact equal-area collision

### Flat orbit

For

\[
(q,p)=(3,5),
\]

the exact difference pressures at exponents `2,4` are

\[
\boxed{
\rho_0=\frac12,
\qquad
\rho_1=\frac12.
}
\]

Therefore

\[
B^{\rm flat}
=
\boxed{
\begin{pmatrix}
1&1\\
0&0
\end{pmatrix}},
\]

with crossing depths

\[
\boxed{(0,\infty),}
\]

node ranks

\[
\boxed{(1,1),}
\]

and activation area

\[
\boxed{A^{\rm flat}=2.}
\]

### Jump orbit

For

\[
(q,p)=(7,17),
\]

the exact difference pressures are

\[
\boxed{
\rho_0=\frac16,
\qquad
\rho_1=\frac{13}{6}.
}
\]

Therefore

\[
B^{\rm jump}
=
\boxed{
\begin{pmatrix}
0&1\\
0&1
\end{pmatrix}},
\]

with crossing depths

\[
\boxed{(1,1),}
\]

node ranks

\[
\boxed{(0,2),}
\]

and activation area

\[
\boxed{A^{\rm jump}=2.}
\]

Thus

\[
\boxed{
A^{\rm flat}=A^{\rm jump}
}
\]

while every richer Ferrers representation differs.

## 4. P025-T234 — area does not determine the activation matrix

The two exact states lie in the same scalar-area fiber:

\[
A=2.
\]

But already the first declared cell differs:

\[
\boxed{
B^{\rm flat}_{1,0}=1,
\qquad
B^{\rm jump}_{1,0}=0.
}
\]

Therefore there is no function

\[
f
\]

such that, on this fine-state family,

\[
B=f(A).
\]

Equivalently:

\[
\boxed{
\text{activation area does not factor the full threshold matrix.}
}
\]

## 5. P025-T235 — area does not determine either dual boundary chart

The equal-area states have

\[
(0,\infty)\ne(1,1)
\]

in crossing coordinates and

\[
(1,1)\ne(0,2)
\]

in rank coordinates.

Their Ferrers boundary words also differ.

Hence

\[
\boxed{
A
\not\Rightarrow
(j_k),
\qquad
A
\not\Rightarrow
(r_j),
\qquad
A
\not\Rightarrow
\text{boundary path}.
}
\]

The scalar potential loses positional information even though it preserves total active mass.

## 6. P025-C36 — exact same-area semantics can be geometrically opposite

The two `2 x 2` matrices each contain two active cells, but their geometry is different:

- the flat orbit activates the low threshold immediately and never reaches the high threshold;
- the jump orbit starts below both thresholds and then reaches both simultaneously.

So area cannot distinguish

\[
\boxed{
\text{persistent low-level activation}
}
\]

from

\[
\boxed{
\text{late multi-level activation}.
}
\]

This is precisely the temporal/precision geometry that the Ferrers boundary retains.

## 7. P025-T236 — area is safe for the aggregate-area future only

For the declared future map

\[
F_A(B):=\sum_{k,j}B_{k,j},
\]

the scalar quotient is tautologically exact:

\[
F_A(B)=A.
\]

But for any future map that retains the distinguishing cell

\[
F_{1,0}(B):=B_{1,0},
\]

the equal-area collision gives

\[
F_{1,0}(B^{\rm flat})
e F_{1,0}(B^{\rm jump}).
\]

Therefore the area collapse is future-safe for the aggregate area query but unsafe for the richer threshold semantics.

This is exactly the future-relative distinction emphasized by P023 and Stage 90.

## 8. P025-C37 — useful potential does not imply sufficient state

Stage 96 proves that `A` has exact first- and mixed-difference laws under threshold/orbit extensions.

Stage 97 proves that those useful response laws do not make `A` injective on the semantic state.

Thus:

\[
\boxed{
\text{scalar potential}
\not\Rightarrow
\text{sufficient state}.
}
\]

This negative boundary is important because potentials are often attractive precisely because they make dynamics look simple.

## 9. State / chart / potential / response layering

Stages 93–97 now distinguish four layers:

1. **semantic boundary state** — exact finite threshold future;
2. **coordinate chart** — crossings, ranks, path;
3. **scalar potential** — activation area;
4. **local response law** — first and mixed finite differences of the area.

No implication lets a lower layer silently replace an upper one without a declared future query and a factorization proof.

## 10. P023 interpretation

Let

\[
q_A(B):=A.
\]

P023's fiber-constancy criterion says a future map descends through `q_A` exactly when it is constant on every equal-area fiber.

The Stage-97 collision supplies an explicit fiber on which the cell future is not constant.

So this is not a philosophical objection to scalar collapse. It is a literal future-compatibility counterexample.

No new P023 theorem is needed; P025 supplies a nontrivial number-theoretic pressure test for the existing theorem.

## 11. Prior-art / novelty discipline

Noninjective scalar invariants and equal-area Ferrers collisions are elementary/general phenomena.

P025 claims no generic novelty for them.

The project-side result is the exact arithmetic collision inside the dyadic projective-pressure state and the resulting negative boundary for the Stage-96 potential interpretation. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 12. Executable assets

Added:

- `src/enterprise_math/abc_activation_area_collision.py`;
- `tests/test_abc_activation_area_collision.py`.

The executable layer verifies the common grid/horizon, equal scalar area, different matrices/crossings/ranks/path, and an explicit distinguishing future cell.

## 13. Next frontier

No hard block exists. Continue with:

1. test whether the scalar area is even future-compatible with **future area after an extension**, not merely the present area;
2. search for two equal-area states whose areas diverge after the same new threshold is inserted;
3. if found, record the stronger `potential is not Markov under extension` boundary;
4. identify the one-step repair data needed for a declared extension;
5. then Relay Stages 91–98 to P023/A2 as a complete state/chart/potential/response pressure test.
