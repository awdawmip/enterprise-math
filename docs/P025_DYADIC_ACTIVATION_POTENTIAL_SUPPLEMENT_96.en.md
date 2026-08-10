# P025 Supplement 96 — Ferrers Activation Area as a Biaxial Discrete Potential

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-orbit-normal-stage91`  
Depends on: P025 Supplements 93–95  
Hard block: `NONE`

## 1. Stage 93 already supplied a scalar invariant

For the finite activation matrix

\[
B_{k,j}=\mathbf1_{\{\rho_j\ge T_k\}},
\]

Stage 93 defines the activation area

\[
\boxed{
A:=\sum_{k=1}^s\sum_{j=0}^hB_{k,j}.
}
\]

It is the number of active threshold/node cells in the declared finite future grid.

Stage 96 studies how this scalar changes under the two primitive axis extensions from Stage 94.

## 2. P025-T229 — threshold-axis first difference

Insert one new threshold `T` while keeping the old `h+1` orbit nodes fixed.

Let its crossing depth be

\[
j_T\in\{0,\ldots,h,\infty\}.
\]

The new row contributes exactly the number of old nodes on which `T` is active. Therefore

\[
\boxed{
\Delta_TA
=
\begin{cases}
h+1-j_T,&j_T<\infty,\\0,&j_T=\infty.
\end{cases}}
\]

Thus the threshold-centric crossing coordinate is precisely the local data needed to compute the threshold-direction area increment.

## 3. P025-T230 — orbit-axis first difference

Append one new orbit node while keeping the old `s` thresholds fixed.

Let its node rank be

\[
r_{h+1}
=
\#\{k:\rho_{h+1}\ge T_k\}.
\]

The new column contributes exactly `r_{h+1}` active cells. Hence

\[
\boxed{
\Delta_JA=r_{h+1}.
}
\]

Thus the node-centric rank coordinate is precisely the local data needed to compute the orbit-direction area increment.

## 4. Directional coordinates are finite differences of one potential

Stages 93–94 showed that crossing and rank coordinates are dual but have different update locality.

P025-T229–230 sharpen that statement:

\[
\boxed{
\text{crossing depth controls }\Delta_TA,
\qquad
\text{node rank controls }\Delta_JA.
}
\]

So the two natural charts can be read as directional first-difference coordinates of the same scalar activation potential.

This explains their axis locality without choosing one as intrinsically preferred.

## 5. P025-D41 — the new corner bit

Now add both one new threshold `T` and one new orbit node.

Define the new corner activation bit

\[
\boxed{
c:=\mathbf1_{\{\rho_{h+1}\ge T\}}.}
\]

This is the only cell that belongs simultaneously to the newly inserted row and newly appended column.

## 6. P025-T231 — mixed second difference equals the corner bit

Write:

- `A` for the old area;
- `A_T` after threshold extension;
- `A_J` after orbit extension;
- `A_{T,J}` after both extensions.

Then

\[
\Delta_J\Delta_TA
=
(A_{T,J}-A_T)-(A_J-A),
\]

and

\[
\Delta_T\Delta_JA
=
(A_{T,J}-A_J)-(A_T-A).
\]

Every old-grid contribution cancels. The only surviving cell is the new corner. Therefore

\[
\boxed{
\Delta_J\Delta_TA
=
\Delta_T\Delta_JA
=c
\in\{0,1\}.
}
\]

This is the exact **corner law**.

## 7. P025-T232 — area reconstruction after one biaxial extension

The corner law gives

\[
\boxed{
A_{T,J}
=
A
+\Delta_TA
+\Delta_JA
+c.
}
\]

So the enlarged activation area is reconstructed from:

1. the old area;
2. the threshold-axis first difference;
3. the orbit-axis first difference;
4. one new corner bit.

No other cells need independent accounting.

## 8. Exact working fixture with active corner

Use the Stage-93 state for

\[
(q,p,m)=(3,41,2)
\]

with thresholds

\[
\frac1{22},\frac12,1,11
\]

through depth three. Its old activation area is

\[
\boxed{A=9.}
\]

Insert

\[
T=10.
\]

The new threshold first crosses at depth two, so among the four old nodes

\[
\boxed{\Delta_TA=2.}
\]

The appended dyadic node has an old-threshold rank equal to the orbit-axis first difference.

Because the old final pressure is already

\[
\frac{221}{22}>10
\]

and the orbit is nondecreasing, the new corner is certainly active:

\[
\boxed{c=1.}
\]

The executable layer verifies both mixed differences equal one and reconstruct the final area exactly.

## 9. Exact fixture with inactive corner

On the same finite state, insert an extremely high threshold, for example

\[
T=10^{100}.
\]

It is not reached on the old horizon and remains above the next finite arithmetic pressure used by the executable check. Thus

\[
\boxed{\Delta_TA=0,
\qquad c=0.}
\]

The mixed second difference vanishes.

This demonstrates that the corner law is a genuine Boolean local response, not a constant one.

## 10. Multi-threshold orbit jump still has one mixed corner

For

\[
(q,p,m)=(7,17,2),
\]

start at horizon zero with old thresholds

\[
\frac12,1,2.
\]

The appended exponent-four node has pressure `13/6`, so

\[
\boxed{\Delta_JA=3.}
\]

because it crosses all three old thresholds simultaneously.

Now insert a new threshold `T=3`. The new node does not reach it, so

\[
\boxed{c=0.}
\]

Even though the orbit-axis first difference is large, the mixed second difference remains one local corner bit.

## 11. P025-T233 — extension diamond has a scalar potential

Stage 95 proves the threshold/orbit semantic extension diamond commutes.

Stage 96 shows a stronger scalar statement: its area increments are exact finite differences of one potential and satisfy

\[
\boxed{
\Delta_J\Delta_TA
=
\Delta_T\Delta_JA.
}
\]

The common mixed derivative is not merely zero; it records the newly created corner cell.

Thus the flat extension diamond carries a nontrivial but completely local mixed response.

## 12. What Stage 96 does **not** say

The scalar area `A` is an aggregate invariant. Stage 96 does **not** prove that `A` determines the full activation matrix, Ferrers boundary, crossing depths, or node ranks.

That stronger collapse would require injectivity and is not implied by the potential law.

The next stage must actively test this boundary rather than silently treating the scalar potential as a sufficient semantic state.

## 13. Architectural meaning

The exact lesson is layered:

- boundary state stores the full finite threshold semantics;
- crossing/rank charts encode directional local derivatives;
- activation area is a scalar potential useful for aggregate update accounting;
- the mixed derivative is the new corner activation.

A useful scalar response law therefore need not replace the state on which it is defined.

This distinction is important for any future precision calculus that separates state, coordinate, potential and local response.

## 14. Prior-art / novelty discipline

Finite differences, scalar potentials and mixed-difference identities are classical/general concepts.

P025 claims none of them in isolation.

The project-side result is the exact arithmetic Ferrers instantiation and its interpretation as a precision-state update law. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 15. Executable assets

Added:

- `src/enterprise_math/abc_dyadic_activation_potential.py`;
- `tests/test_abc_dyadic_activation_potential.py`.

The executable layer verifies both first-difference formulas, active and inactive corner fixtures, mixed-difference commutation and exact area reconstruction.

## 16. Next frontier

No hard block exists. Continue with:

1. search for exact arithmetic collisions with the same threshold grid, horizon and area but different Ferrers boundaries;
2. if found, record `potential != sufficient state` as a reusable negative boundary;
3. identify which future queries are safe on the scalar area alone;
4. compare with P024 response-law layering and P023 future-safe quotient language;
5. then decide whether to Relay Stage91–97 as a coherent foundation pressure-test packet.
