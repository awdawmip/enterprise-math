# P025 Supplement 98 — Activation Area Is Not Extension-Markov

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-orbit-normal-stage91`  
Depends on: P025 Supplements 96–97  
Hard block: `NONE`

## 1. Stage 97 disproved present-state sufficiency

Stage 97 gives two exact arithmetic Ferrers states on the same threshold grid and horizon with

\[
A^{\rm flat}=A^{\rm jump}=2
\]

but different activation matrices.

A stronger question remains:

> Even if we only care about the scalar area in the future, can the current area determine its own evolution under a declared extension?

Stage 98 shows that the answer is still no.

## 2. Reuse the equal-area fiber

Fix the current threshold grid

\[
\boxed{\left(\frac12,1\right)}
\]

and horizon `h=1`.

The two exact states are:

### Flat state

\[
(q,p)=(3,5),
\qquad
(\rho_0,\rho_1)=\left(\frac12,\frac12\right),
\]

with

\[
A=2.
\]

### Jump state

\[
(q,p)=(7,17),
\qquad
(\rho_0,\rho_1)=\left(\frac16,\frac{13}{6}\right),
\]

also with

\[
A=2.
\]

## 3. Apply the same future action

Insert the same new threshold

\[
\boxed{T=\frac34}
\]

into both states.

For the flat state,

\[
\rho_0=\rho_1=\frac12<\frac34.
\]

So the new threshold is never reached on the current horizon:

\[
\boxed{j_T^{\rm flat}=\infty.}
\]

The new row contains no active cells and

\[
\boxed{A_{\rm next}^{\rm flat}=2.}
\]

For the jump state,

\[
\frac16<\frac34<\frac{13}{6},
\]

so

\[
\boxed{j_T^{\rm jump}=1.}
\]

The new row contains one active cell and

\[
\boxed{A_{\rm next}^{\rm jump}=3.}
\]

## 4. P025-C38 — equal current area, unequal future area

The two states satisfy

\[
\boxed{A^{\rm flat}=A^{\rm jump}=2,}
\]

but under the same declared threshold-insertion action,

\[
\boxed{
A_{\rm next}^{\rm flat}=2
\ne
3=A_{\rm next}^{\rm jump}.
}
\]

Therefore there is no function

\[
G_T
\]

such that

\[
A_{\rm next}=G_T(A)
\]

for all states in this exact arithmetic family.

Hence:

\[
\boxed{
\text{current activation area is not a Markov state for threshold extension.}
}
\]

## 5. P025-T237 — the area quotient is not composition-safe for this future

Let

\[
q_A(B):=A(B)
\]

be the scalar area collapse.

Let `E_T` mean "insert threshold `T=3/4`" and let the future observation be the resulting area

\[
F_T(B):=A(E_T(B)).
\]

The Stage-98 pair satisfies

\[
q_A(B^{\rm flat})=q_A(B^{\rm jump})
\]

but

\[
F_T(B^{\rm flat})\ne F_T(B^{\rm jump}).
\]

So P023's fiber-constancy criterion fails:

\[
\boxed{
F_T\text{ does not descend through }q_A.
}
\]

This is a literal composition-safety failure, not merely a loss of descriptive detail.

## 6. P025-T238 — exact one-step repair by crossing depth

For one declared new threshold `T`, Stage 96 gives

\[
\Delta_TA
=
\begin{cases}
h+1-j_T,&j_T<\infty,\\0,&j_T=\infty.
\end{cases}
\]

Therefore

\[
\boxed{
A_{\rm next}
=A+\Delta_TA
}
\]

is determined exactly by

\[
\boxed{(A,j_T).}
\]

Thus adding the one crossing coordinate repairs the scalar area state for this one-step future action.

## 7. P025-T239 — crossing depth and area increment are equivalent repairs

At fixed horizon `h`, the map

\[
j_T
\mapsto
\Delta_TA
\]

is

\[
0\mapsto h+1,
\quad
1\mapsto h,
\quad\ldots\quad
h\mapsto1,
\quad
\infty\mapsto0.
\]

It is bijective.

Therefore the following repaired states are equivalent for the one-step future:

\[
\boxed{(A,j_T)}
\]

and

\[
\boxed{(A,\Delta_TA).}
\]

P023's generic one-step repair

\[
(A,A_{\rm next})
\]

is also equivalent because

\[
A_{\rm next}=A+\Delta_TA.
\]

So the abstract repair theorem specializes to a theorem-native arithmetic response coordinate.

## 8. Exact repaired states for the collision pair

For the flat state,

\[
\boxed{(A,j_T)=(2,\infty),}
\]

which reconstructs

\[
A_{\rm next}=2.
\]

For the jump state,

\[
\boxed{(A,j_T)=(2,1),}
\]

which reconstructs

\[
A_{\rm next}=3.
\]

The additional coordinate separates exactly the equal-area fiber that caused the future incompatibility.

## 9. Potential versus dynamic state

Stages 96–98 now establish three distinct facts:

1. `A` is a useful scalar potential with exact finite-difference laws;
2. `A` does not determine the present Ferrers semantic state;
3. `A` does not even determine its own next value under all declared extension actions.

Therefore:

\[
\boxed{
\text{potential}
\not\Rightarrow
\text{dynamic sufficient state}.
}
\]

A response law can be simple while the state needed to choose that response remains richer.

## 10. Action-relative repair

The repair coordinate `j_T` is not universal metadata. It is indexed by the declared future threshold `T`.

If the future action changes, the required repair may change.

Thus the correct object is not

\[
\text{area plus all possible crossing depths},
\]

but rather

\[
\boxed{
\text{current coarse state}
+
\text{minimal response coordinate for the declared action}.
}
\]

This is an exact number-theoretic instance of action-relative precision.

## 11. Relation to P023 and P024

P023 supplies the generic logic:

- test fiber constancy;
- if unsafe, refine by enough future information to restore factorization.

P024 studies action-language precision.

Stage 98 connects the two in one exact arithmetic fixture:

- the coarse scalar potential fails fiber constancy under a specific action;
- the action selects one directional coordinate `j_T`;
- that coordinate gives an exact one-step repair.

No new canonical theorem is claimed here. This is a research-pressure bridge among existing project layers.

## 12. Prior-art / novelty discipline

Markov sufficiency, state augmentation and one-step repairs are broad prior concepts.

P025 claims none of them in isolation.

The project-side result is the exact arithmetic future collision and the explicit crossing-depth repair supplied by the Ferrers precision geometry. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 13. Executable assets

Added:

- `src/enterprise_math/abc_activation_area_future.py`;
- `tests/test_abc_activation_area_future.py`.

The executable layer verifies the equal-area future divergence, exact crossing-depth repair, area-increment equivalence and rejection of non-extension thresholds.

## 14. Next frontier

No hard block exists. Continue with the exact dual statement:

1. test area future-safety under **orbit-node extension**;
2. identify the node-rank response coordinate as the dual one-step repair;
3. formulate a single action-relative repair compiler choosing crossing depth for threshold actions and rank for orbit actions;
4. verify the two repairs are related by the Stage-96 potential derivatives;
5. then Relay Stages 91–99 to P023/P024/A2 as one coherent pressure-test packet.
