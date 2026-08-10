# P023 — Two-Stage Normalization of Sequential Precision Codes, Supplement 18

Status: `PROVED RESEARCH NOTE`  
Owner: A2 / P023, with P018 mixed-radix reuse  
Depends on: P023-S17 slack decomposition, P023-S14 conditional repair schedules, P018 exact mixed-radix charts  
Discipline: mixed-radix packing and ranking finite realized subsets are established constructions. The project result is the exact normalization interpretation of the two P023 scheduling-slack components.

## 1. From diagnosis to exact normalization

S17 proves that a sequential precision schedule has two independent integer overheads:

\[
S_{\rm total}=S_{\rm radix}+S_{\rm inc}.
\]

The present supplement shows that these are not merely descriptive statistics.

Each term is removed by one exact finite normalization step:

\[
\boxed{
\text{separate local repair digits}
\longrightarrow
\text{packed mixed-radix code}
\longrightarrow
\text{realized joint-rank code}.
}
\]

The first arrow removes exactly `S_radix`; the second removes exactly `S_inc`.

## 2. Canonical local repair digits along a schedule

Fix an order of tasks and its S14 context chain

\[
C_0\supseteq C_1\supseteq\cdots\supseteq C_m=E_*.
\]

At stage `j`, let

\[
\rho_j
\]

be the maximum number of child blocks into which one `C_{j-1}` block splits.

Inside each current context block, number the actually realized child blocks by local digits

\[
d_j\in\{0,\ldots,\rho_j-1\}.
\]

The same digit alphabet may be reused in different parent blocks because the parent context is already known.

For each original state `x`, this yields a digit word

\[
\boxed{
\mathbf d(x)=(d_1(x),\ldots,d_m(x)).
}
\]

with radix vector

\[
\boxed{
(\rho_1,\ldots,\rho_m).
}
\]

## 3. P023-S18-T01 — Local repair words exactly represent final joint classes

Status: `PROVED`.

Two states have the same complete repair digit word if and only if they lie in the same final joint block `E_*`.

### Proof

Induct on stages. At stage one, the local digit identifies the realized child of the universal parent. Assume the prefix digits determine the current context block. The next local digit identifies the unique child block inside that parent. Hence the full prefix determines `C_j` exactly for every `j`.

At `j=m`, the complete word determines and is determined by the final joint block. ∎

Thus the local digit word is an exact sequential coordinate system for final precision.

## 4. P023-S18-T02 — Mixed-radix packing is a bijection on the full product alphabet

Define

\[
P=\prod_{j=1}^{m}\rho_j.
\]

The full formal digit product is

\[
\prod_j\{0,\ldots,\rho_j-1\}.
\]

Use the standard mixed-radix join

\[
\boxed{
J(d_1,\ldots,d_m)
=
(((d_1\rho_2+d_2)\rho_3+d_3)\cdots)\rho_m+d_m.
}
\]

Then

\[
\boxed{
J:
\prod_j[0,\rho_j)
\overset{\sim}{\longrightarrow}
[0,P)
}
\]

is a bijection, with inverse given by repeated quotient/remainder extraction.

This is the finite mixed-radix structure already used in P018.

## 5. P023-S18-T03 — Packing removes exactly radix slack

Status: `PROVED`.

Separate stage coding uses

\[
\sum_jL_B(\rho_j)
\]

base-`B` symbols in the S14 worst-case model.

The packed product code needs only

\[
L_B(P).
\]

Therefore the exact saving is

\[
\boxed{
\sum_jL_B(\rho_j)-L_B(P)
=S_{\rm radix}.
}
\]

No state semantics or realizability assumption changes in this step. The complete formal product alphabet is preserved bijectively.

Hence radix slack is purely a coordinate-packing defect.

## 6. Realized product support

Only some mixed-radix words may actually arise from states.

Let

\[
\mathcal C
=
\{J(\mathbf d(x)):x\in X\}
\subseteq[0,P).
\]

By T01,

\[
\boxed{
|\mathcal C|=|X/E_*|=N_*.
}
\]

The missing values in `[0,P)` are formal sequential codewords with no realizing state.

## 7. P023-S18-T04 — Realized-support ranking removes exactly incidence slack

Order the realized packed codes increasingly and define their rank map

\[
\boxed{
r:\mathcal C\overset{\sim}{\longrightarrow}[0,N_*).
}
\]

This is a bijective recoding of the actual final joint classes.

Its base-`B` depth is

\[
L_B(N_*).
\]

Starting from the packed product code of depth `L_B(P)`, the exact saving is

\[
\boxed{
L_B(P)-L_B(N_*)
=S_{\rm inc}.
}
\]

This second normalization changes no realized state. It only deletes unused formal product codes.

Hence incidence slack is exactly an unrealized-support defect.

## 8. P023-S18-T05 — Complete normalization reaches the final cardinality lower bound

Combining T03 and T04 gives

\[
\boxed{
\sum_jL_B(\rho_j)
\longrightarrow
L_B(P)
\longrightarrow
L_B(N_*).
}
\]

The total removed depth is

\[
S_{\rm radix}+S_{\rm inc}=S_{\rm total}.
\]

Therefore every finite sequential task code admits an exact normalization to a direct final-joint code at the information-theoretic integer cardinality lower bound.

The price is representational: the final rank code may no longer expose the original stage coordinates as independent digits.

## 9. Two different normalization mechanisms

The two arrows must not be conflated.

### Mixed-radix packing

- domain: the **entire formal product alphabet**;
- operation: bijective coordinate change;
- removes: separate-ceiling / radix slack;
- cannot remove: unrealized product tuples.

### Realized-support ranking

- domain: the **actually realized subset** of product codes;
- operation: quotient/relabeling of support;
- removes: incidence capacity slack;
- requires: actual realizability information.

This is exactly the same conceptual split seen elsewhere in the project:

\[
\boxed{
\text{coordinate normalization}
\neq
\text{state-space quotient}.
}
\]

## 10. Pure witnesses

The S17 radix-only `3 x 5` complete-incidence example has

\[
P=N_*=15.
\]

Packing changes base-two depth from `5` to `4`; realized ranking saves nothing.

The S17 incidence-only five-state example has

\[
P=9,
\qquad
N_*=5.
\]

Packing saves nothing (`4 -> 4` bits), while realized ranking gives the full `4 -> 3` bit saving.

Thus both normalization mechanisms are independently necessary.

## 11. Relation to P018

P018 mixed-radix charts already prove that finite detail coordinates can be joined and split exactly without hidden real arithmetic.

S18 reuses that arithmetic on **task-repair digits** rather than spatial/detail digits.

This yields a broader principle:

> whenever finite repair coordinates form a product alphabet, coordinatewise representation and packed integer representation are exactly interchangeable before any realizability quotient is taken.

The later support quotient remains a distinct A2 operation.

## 12. Research-tool consequence

A multi-stage proof state should not be declared irreducibly large merely because it carries many local repair coordinates.

Before accepting the state cost:

1. compute exact local repair radices;
2. mixed-radix pack them to remove coordinate-ceiling overhead;
3. compute the realized support of the packed code;
4. quotient/rank only the realized support;
5. compare the normalized state with downstream task requirements before discarding the original coordinate chart.

This is an exact compiler pipeline, not lossy compression.

## 13. Executable specification

- `src/enterprise_math/precision_schedule_normalization.py`
- `tests/test_precision_schedule_normalization.py`

The tests exhaust a `2 x 3 x 4` mixed-radix alphabet for pack/unpack bijectivity, verify that local digit words reproduce final joint classes, and independently isolate the radix-only and incidence-only normalization steps.

## 14. Foundation boundary

The direct final rank code is minimal for the declared final task quotient, but it may be a poor intermediate state if later tasks require access to the original repair coordinates.

Therefore normalization must remain future-language relative:

\[
\boxed{
\text{minimal final code}
\not\Rightarrow
\text{minimal state for every future extension}.
}

P023 future-safe refinement remains the authority for whether the normalized code is safe beyond the declared schedule horizon.
