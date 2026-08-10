# P023 — Scheduling Slack Decomposition and Primitive-Task Overhead, Supplement 17

Status: `PROVED RESEARCH NOTE`  
Owner: A2 / P023, with a bridge to P018 mixed-radix precision  
Depends on: P023-S14 scheduling, S13 realized joint incidence, P018 integer radix/carry discipline  
Discipline: integer ceiling codes and finite incidence products are established mathematics. The project role is to separate two mathematically different causes of sequential precision overhead.

## 1. One scalar slack hides two different defects

For a task order `sigma`, S14 defines stage repair factors

\[
\rho_1,\ldots,\rho_m
\]

and total base-`B` symbol depth

\[
C_B(\sigma)=\sum_j L_B(\rho_j).
\]

Let

\[
P_\sigma=\prod_j\rho_j
\]

be the stagewise product capacity and let

\[
N_*=|X/E_*|
\]

be the actual final joint class count.

S14 gives

\[
N_*\le P_\sigma.
\]

The total scheduling slack

\[
C_B(\sigma)-L_B(N_*)
\]

contains two different sources of inefficiency.

## 2. P023-S17-T01 — Exact two-term slack decomposition

Status: `PROVED`.

Define

\[
\boxed{
S_{\rm radix}(\sigma)
=
\sum_jL_B(\rho_j)-L_B(P_\sigma),
}
\]

and

\[
\boxed{
S_{\rm inc}(\sigma)
=
L_B(P_\sigma)-L_B(N_*).
}
\]

Then both are nonnegative integers and

\[
\boxed{
C_B(\sigma)-L_B(N_*)
=
S_{\rm radix}(\sigma)
+
S_{\rm inc}(\sigma).
}
\]

### Proof

Submultiplicativity of integer symbol depth gives

\[
L_B(P_\sigma)
=L_B\!\left(\prod_j\rho_j\right)
\le
\sum_jL_B(\rho_j),
\]

so `S_radix>=0`.

Because `N_*<=P_sigma`, monotonicity of `L_B` gives

\[
L_B(N_*)\le L_B(P_\sigma),
\]

so `S_inc>=0`.

The displayed identity is exact telescoping. ∎

## 3. Interpretation of the two terms

### Radix packing slack

`S_radix` is present even when every stage capacity is fully realized.

It comes from encoding each stage in a separately rounded base-`B` alphabet depth rather than packing the full mixed-radix product into one code.

This is the scheduling analogue of the project's integer radix/carry discipline: separate local radices may use more whole base-`B` symbols than their combined product requires.

### Incidence capacity slack

`S_inc` compares the stagewise product capacity with the actual joint state count.

It is caused by realized incidence failing to fill the formal stagewise worst-case product. Nonuniform branching and higher-order dependency are canonical sources.

This is the task-scheduling analogue of candidate-product versus realized-state defects throughout P017/P023.

## 4. P023-S17-T02 — Incidence slack can exist with zero radix slack

Status: `PROVED BY EXPLICIT WITNESS`.

Take five states and two three-block tasks whose realized incidence edges are

\[
(A,X),(A,Y),(A,Z),(B,X),(C,X).
\]

Both directed repair factors are three:

\[
\rho(E,F)=\rho(F,E)=3.
\]

Thus either order has

\[
P_\sigma=3\cdot3=9.
\]

But only five joint classes are realized:

\[
N_*=5.
\]

In base two,

\[
C_2=2+2=4,
\qquad
L_2(P_\sigma)=L_2(9)=4,
\qquad
L_2(N_*)=L_2(5)=3.
\]

Therefore

\[
\boxed{
S_{\rm radix}=0,
\qquad
S_{\rm inc}=1.
}
\]

The entire one-bit overhead is structural incidence overcapacity.

## 5. P023-S17-T03 — Radix slack can exist with zero incidence slack

Status: `PROVED BY EXPLICIT WITNESS`.

Take the complete incidence product of a three-block task and a five-block task on 15 realized states.

Then

\[
\rho(E,F)=5,
\qquad
\rho(F,E)=3,
\]

and every formal pair is realized, so

\[
P_\sigma=N_*=15.
\]

For order `E -> F` in base two,

\[
C_2=L_2(3)+L_2(5)=2+3=5,
\]

while

\[
L_2(P_\sigma)=L_2(15)=4.
\]

Hence

\[
\boxed{
S_{\rm radix}=1,
\qquad
S_{\rm inc}=0.
}
\]

The one-bit overhead remains despite perfect complete incidence; it is purely a radix-packing effect.

## 6. P023-S17-T04 — Optimal ordering need not reach the final class-count lower bound

Status: `PROVED BY THE FIVE-STATE WITNESS`.

In the incidence-only witness of Section 4, both task orders have binary cost four, while the final joint quotient has only five classes and lower bound three.

Thus

\[
\boxed{
\min_\sigma C_2(\sigma)=4>3=L_2(N_*).
}
\]

So positive scheduling slack can be **unavoidable for the declared primitive task language**.

This is stronger than saying that one order is suboptimal: every available sequential order is suboptimal relative to a hypothetical direct code of the final joint state.

## 7. Primitive-task interface overhead

Define

\[
\boxed{
H_B(\mathcal T)
=
\min_\sigma C_B(\sigma)-L_B(N_*).
}
\]

This is the minimum overhead forced by acquiring the final precision through the declared primitive tasks `T`.

It depends on the task language, not only on the final joint partition.

If a direct bundled task

\[
E_*(x)=([x]_{E_1},\ldots,[x]_{E_m})
\]

is added as an allowed primitive, it has exactly `N_*` classes and can be acquired in

\[
L_B(N_*)
\]

symbols, so the interface overhead becomes zero.

Thus

\[
\boxed{
\text{same final precision}
\not\Rightarrow
\text{same acquisition overhead under different primitive task languages}.
}
\]

## 8. P023-S17-T05 — Bundling can remove interface overhead without changing final semantics

Status: `PROVED`.

Adding a bundled task equal to the final joint observation does not change the final joint partition. It only changes the permitted acquisition language.

Therefore a positive `H_B(T)` is not an intrinsic defect of the final precision state itself. It is a defect of representing/acquiring that state through the chosen primitive task interface.

This distinction mirrors the project's broader separation between:

- represented state semantics;
- allowed operations/queries;
- task-relative repair cost.

## 9. Relation to P018 radix calculus

P018 already studies mixed-radix precision state and exact carry/coherence.

S17 gives that machinery a new proof-state interpretation:

\[
\boxed{
\text{radix slack}
=
\text{cost of separately rounded stage alphabets compared with packed product capacity}.
}
\]

This suggests a future optimization layer in which a schedule may choose not only task order but also how consecutive repair alphabets are packed into mixed-radix symbols.

Such packing cannot remove incidence capacity slack, because unrealized joint states are a different structural defect.

## 10. Research-tool rule

When a schedule has positive slack, diagnose it before inventing another heuristic:

1. compute product capacity `P_sigma`;
2. split total slack into `S_radix` and `S_inc`;
3. if radix slack dominates, change coding/packing rather than task semantics;
4. if incidence slack dominates, exploit dependency closure, realized tuples, or a different task order;
5. if the optimum still has positive overhead, the primitive task interface itself is the limiting object;
6. distinguish adding a bundled primitive from changing the final precision state.

This prevents two different defects from being treated as one generic “inefficiency.”

## 11. Executable specification

- `src/enterprise_math/precision_scheduling_slack.py`
- `tests/test_precision_scheduling_slack.py`

Tests isolate pure incidence slack and pure radix slack, verify the exact two-term decomposition, prove unavoidable optimal interface overhead in the five-state family, and show that adding the direct bundled joint task reduces that overhead to zero.

## 12. Prior-art and novelty discipline

Mixed-radix coding, integer ceiling effects, product capacities, and task bundling are established ideas.

The project-specific synthesis is the exact decomposition of P023's endogenous repair schedule cost into a radix component and a realized-incidence component, together with its use as a research diagnostic across precision and number-theoretic proof states.
