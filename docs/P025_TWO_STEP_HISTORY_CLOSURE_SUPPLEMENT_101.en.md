# P025 Supplement 101 — Two-Step Action-History Closure Boundary

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-history-closure-stage101`  
Depends on: P025 Supplements 96–100  
Hard block: `NONE`

## 1. Question

Stage 100 gives a natural one-step response signature for primitive actions that either insert a threshold row `+T` or append one monotone orbit node `+J`.

Stage 101 asks a strictly stronger question:

> if the same signature predicts every one-step next area, does it remain sufficient after the first action changes the state?

The answer is **no**.

## 2. Generic finite model

Let

\[
\rho_0\le\cdots\le\rho_h
\]

be a finite nondecreasing scalar orbit and let

\[
T_1<\cdots<T_s
\]

be existing thresholds. Define

\[
B_{k,j}=\mathbf 1_{\{\rho_j\ge T_k\}},
\qquad
A=\sum_{k,j}B_{k,j}.
\]

For a prospective threshold `U` and next node value `v>=rho_h`, write

\[
L_U:=\#\{j:\rho_j\ge U\},
\]

\[
R_v:=\#\{k:v\ge T_k\},
\]

and define the mixed corner bit

\[
\boxed{C_{U,v}:=\mathbf1_{\{v\ge U\}}.}
\]

## 3. P025-T229 — exact mixed two-step law

After inserting `U` and appending `v`, in either order,

\[
\boxed{
A''=A+L_U+R_v+C_{U,v}.
}
\]

The first two increments are the Stage-100 one-step responses. The last term is a genuinely mixed second-order response.

Equivalently,

\[
\boxed{
\Delta_v\Delta_U A
=
\Delta_U\Delta_v A
=
C_{U,v}.
}
\]

Thus the extension diamond still commutes, but one-step marginal data need not determine the common two-step value.

## 4. P025-CE38 — exact mixed-history collision

Take one existing threshold

\[
T_1=\frac1{25},
\]

one old dyadic node at exponent `2`, and prospective threshold

\[
U=\frac{11}{20}.
\]

Compare the exact P025 dyadic difference orbits

\[
(q,p)=(3,5),
\qquad
(q,p)=(3,41).
\]

Through exponents `2,4`, their pressures are

\[
(3,5):\quad \left(\frac12,\frac12\right),
\]

\[
(3,41):\quad \left(\frac1{22},\frac{13}{22}\right).
\]

At the current one-node state both have

\[
A=1,
\qquad
j_U=\infty,
\qquad
R_{\rho_1}=1.
\]

Hence their Stage-100 one-step signatures for the family `{+U,+J}` are identical:

\[
\boxed{(A,j_U,R_{\rho_1})=(1,\infty,1).}
\]

Nevertheless,

\[
C_{U,\rho_1}=0
\]

for `(3,5)`, while

\[
C_{U,\rho_1}=1
\]

for `(3,41)`. Therefore the two-step final areas are

\[
\boxed{2\neq3.}
\]

So one-step sufficiency does not imply closure under the mixed two-action history.

## 5. Conditional mixed closure

If `j_U` is finite on the old horizon, then some old node already satisfies `rho_j>=U`. Monotonicity forces every appended node to satisfy `v>=U`, hence

\[
\boxed{C_{U,v}=1.}
\]

Therefore the new mixed bit is needed only when the candidate threshold remains unresolved on the old horizon (`j_U=infinity`).

This is an adaptive precision rule, not an unconditional extra coordinate.

## 6. P025-T230 — threshold-threshold histories are already closed

For two distinct inserted thresholds `U,V`,

\[
\boxed{
A_{+U,+V}=A+L_U+L_V.
}
\]

There is no threshold-threshold interaction term because the two actions add disjoint rows and do not change the orbit values.

Thus the Stage-100 threshold-response staircase is already closed under arbitrary finite sequences of threshold insertions drawn from a fixed candidate family.

## 7. P025-CE39 — repeated-node one-step failure

Take the current threshold set

\[
\{1\}
\]

and again compare `(3,5)` with `(3,41)` from exponent `2`.

The first three dyadic pressures are

\[
(3,5):\quad \left(\frac12,\frac12,\frac12\right),
\]

\[
(3,41):\quad \left(\frac1{22},\frac{13}{22},\frac{221}{22}\right).
\]

At the initial node both have current area zero. Their first future-node ranks are also both zero:

\[
\boxed{(A,R_1)=(0,0).}
\]

So the one-step `+J` signature agrees.

At the second future node, however,

\[
R_2=0
\]

for `(3,5)` and

\[
R_2=1
\]

for `(3,41)`. Hence after two node appends the final areas are

\[
\boxed{0\neq1.}
\]

A one-step next-node rank is therefore not closed under repeated node actions.

## 8. Stage101 boundary theorem

The exact conclusion is

\[
\boxed{
\text{one-step sufficient response signature}
\not\Rightarrow
\text{finite-history sufficient response signature}.
}
\]

The failure is structured rather than arbitrary:

- `+T;+T` needs no new interaction;
- mixed `+T;+J` needs the corner bit `C_{U,v}` when unresolved;
- `+J;+J` needs the second future-node rank.

This identifies the next precision layer rather than merely producing a negative example.

## 9. Architectural meaning

A declared future language must specify whether it contains only primitive one-step actions or finite action histories. The two languages induce different quotients.

Stage 101 therefore sharpens the distinction among:

1. one-step response sufficiency;
2. pairwise interaction sufficiency;
3. history closure.

This is the concrete P025 pressure test promised in the Stage91–100 Foundation Feedback Packet.

## 10. Prior-art / novelty boundary

State augmentation, finite differences, pairwise interaction terms and finite-history closure are broad prior ideas. P025 claims none in isolation.

The project-side contribution is the exact arithmetic realization, exact collision witnesses, and the use of those witnesses to separate one-step future precision from history-closed precision. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 11. Executable assets

Added:

- `src/enterprise_math/abc_two_step_history.py`;
- `tests/test_abc_two_step_history.py`.

## 12. Next frontier

The natural next question is whether the extra information proliferates without bound or closes at finite interaction order. The finite threshold/node incidence structure strongly suggests an exact second-order closure:

\[
A(I,J)
=
A
+\sum_{i\in I}L_i
+\sum_{j\in J}R_j
+\sum_{i\in I,j\in J}C_{ij}.
\]

Stage 102 will prove or falsify that formula for arbitrary finite action families and determine whether all third and higher action interactions vanish.