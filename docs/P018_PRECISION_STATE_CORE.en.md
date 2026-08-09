# P018 — Precision State Core

Status: `SEMANTIC REPLAY / PROVED CORE`  
Source: State Pair / critical-grid route from historical PR #68  
Current owner: `program/p018-precision-v2`  
Discipline: this document reorganizes already-proved structure and adds no new mathematical claim.

## 1. Why Pair comes first

Many historical P018 defect formulas use an integer difference

\[
h=b-a.
\]

But asking whether two states are equal, whether an observation merges them, or whether two paths end at the same state does not require subtraction.

The weaker comparison object is therefore

\[
\boxed{(a,b)\in X\times X.}
\]

For any deterministic map

\[
F:X\to Y,
\]

define pair transport

\[
\boxed{F_\times(a,b)=(F(a),F(b)).}
\]

No additive, order, metric, or topological structure is required. Product maps and kernel relations are established mathematics; the P018-specific use is to place them beneath numeric defect coordinates in the precision stack.

---

## 2. Diagonal and kernel

Define

\[
\Delta_X=\{(x,x):x\in X\}.
\]

Determinism immediately gives

\[
F_\times(\Delta_X)\subseteq\Delta_Y.
\]

Once two states are genuinely equal, a common deterministic suffix cannot separate them again.

The kernel relation is

\[
\boxed{
\ker F
=
\{(x,y):F(x)=F(y)\}
=
F_\times^{-1}(\Delta_Y).
}
\]

This lets P010-style strict history merging be understood first at the Pair/kernel level before integer multiplicity or spectrum coordinates are added.

---

## 3. Difference is a coordinate on Pair

When the state space is `N`, a pair can be encoded losslessly as

\[
(a,b)
\longleftrightarrow
(a,h),
\qquad h=b-a\in\mathbb Z,
\]

with the admissibility condition

\[
a+h\ge0.
\]

The appearance of `Z` here does not force physical/natural states themselves to become signed. It is only a coordinate for an oriented state difference. P006 signed-state semantics and P018 signed defects therefore remain distinct layers.

---

## 4. Precision critical square

Let a fine operation, a coarse operation, and a projection form a square. For one input `x`, write the two path endpoints as

\[
a=\pi(F_e(x)),
\qquad
b=F_d(\pi(x)).
\]

P018 first retains the endpoint pair

\[
\boxed{(a,b).}
\]

The square commutes at this state exactly when the pair is diagonal. If integer coordinates are available, signed holonomy is then defined as

\[
\boxed{b-a.}
\]

Thus numeric defect is a coordinate on endpoint-pair failure, not a prerequisite for defining path disagreement.

---

## 5. 2x2 rectangle interchange

Take first-stage maps `F_0,F_1` and second-stage maps `G_0,G_1`. Let

\[
\begin{aligned}
a&=G_0(F_0(x)),\\
b&=G_0(F_1(x)),\\
c&=G_1(F_0(x)),\\
d&=G_1(F_1(x)).
\end{aligned}
\]

Adjacent-pair composition erases only the shared middle endpoint:

\[
(a,b);(b,d)=(a,d)
\]

and

\[
(a,c);(c,d)=(a,d).
\]

Hence

\[
\boxed{
(a,b);(b,d)
=
(a,c);(c,d)
=
(a,d).
}
\]

This endpoint result uses no additive, metric, or continuum structure.

Lean module: `EnterpriseMath.State.CriticalGrid`.

---

## 6. Exact integer rectangle identity

When the endpoints lie in `Z`, the same outer difference has two exact finite telescoping decompositions:

\[
\boxed{d-a=(b-a)+(d-b)}
\]

and

\[
\boxed{d-a=(c-a)+(d-c).}
\]

Subtracting them gives

\[
\boxed{
(d-b)-(c-a)
=
(d-c)-(b-a).
}
\]

This is a finite integer identity, not a derivative, limit, or continuous curvature construction.

---

## 7. Negative boundary: outer flatness does not imply local flatness

The following distinction must remain explicit:

\[
\boxed{
\text{equal outer endpoints}
\not\Rightarrow
\text{every local edge defect is zero}.
}
\]

Nonzero local defects may cancel exactly while the final outer pair returns to the diagonal. Therefore confluence / equal final endpoint is different from every local square commuting. This is one reason P009 mixed scheduling and P010 eventual merging must not be collapsed into a single global-commutativity notion.

---

## 8. Ownership boundaries

### A1 / P010 / P011 / P020

Generic deterministic kernels, coalescence, and stabilization belong to A1. P018 consumes those results and studies their interaction with precision observations.

### A2 / P023

The generic question of which observation quotient is a congruence for a declared operation/future language belongs to A2/P023 and is not duplicated here.

### P018

P018 keeps:

- precision endpoint-pair interpretation;
- critical-square / holonomy coordinates;
- defect/transport under precision projection;
- concrete interfaces to carry, detail, and context separation.

---

## 9. Executable and formal assets

Python:

- `src/enterprise_math/state_pair.py`
- `src/enterprise_math/critical_grid.py`

Tests:

- `tests/test_state_pair.py`
- `tests/test_critical_grid.py`

Lean:

- `EnterpriseMath/State/CriticalGrid.lean`

These assets were semantically replayed from historical PR #68 onto current-main P018 v2. Historical Supplement/T identifiers remain provenance and no longer determine the long-term module structure.

---

## 10. P018 v2 dependency order

The current precision-specific order is

\[
\boxed{
\text{Typed State}
\to
\text{State Pair / Kernel}
\to
\text{optional Difference coordinates}
\to
\text{critical-grid defect / holonomy}
\to
\text{context sufficiency}
\to
\text{operation-specific transport}.
}
\]

This is not a new Foundation declaration. It is the current minimum-dependency order for P018 v2, pending A2/P023 deduplication and broader prior-art audit before any lower-level promotion.
