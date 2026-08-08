# P023 — Composition-Safe Collapse and Future-Compatible Quotients

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact criterion for when finite-state detail may be collapsed without changing chosen future observations  
Depends on: P010 history merge, P011 collision spectrum, P018 finite-precision calculus, P021 witness transport  
Discipline: quotient factorization, automata distinguishability, bisimulation/congruence, and partition refinement are established prior art. P023 does not claim those general theories as new.

## 1. Motivation

P021 direction transport exposed a recurrent Enterprise Math problem.

A fine witness relation can be replaced by a smaller cardinality summary only in special regimes. Outside those regimes, two fine states that look identical at the current precision can behave differently after later composition.

The foundational question is therefore not merely

> can information be collapsed?

but

> when is a proposed collapse compatible with the future operations that matter?

P023 isolates that question from black-hole physics and treats it as a finite exact quotient problem.

## 2. P023-T01 — Fiber-constancy / descent criterion

Let

\[
q:X\to Q,
\qquad
F:X\to Y,
\qquad
r:Y\to R.
\]

Write

\[
h=r\circ F:X\to R.
\]

Then there exists a unique map

\[
\bar h:q(X)\to R
\]

such that

\[
h=\bar h\circ q
\]

if and only if

\[
\boxed{
q(x)=q(y)\Longrightarrow h(x)=h(y)
}
\]

for all `x,y in X`.

### Proof

If `h=\bar h\circ q`, equal `q`-values give equal `h`-values immediately.

Conversely, if `h` is constant on every `q`-fiber, define

\[
\bar h(a)=h(x)
\]

for any `x` with `q(x)=a`. Fiber constancy makes the definition independent of the chosen representative. Uniqueness holds on `q(X)` because every coarse state has a representative.

### Enterprise Math reading

A collapse is safe for the chosen future observable exactly when the forgotten distinctions are invisible to that observable.

No error norm or hidden real completion is required.

## 3. P023-T02 — Coarsest one-step repair

If the original quotient `q` is not safe for `h`, define

\[
q_1(x)=\bigl(q(x),h(x)\bigr).
\]

Then:

1. `q_1` refines `q`;
2. `h` descends through `q_1`;
3. if another quotient `s` refines `q` and `h` descends through `s`, then `s` refines `q_1`.

Therefore

\[
\boxed{q_1=(q,h)}
\]

is the **coarsest repair** that restores one-step composition safety.

### Proof

The first two statements are immediate from the pair definition. For the third, if `s(x)=s(y)`, refinement gives `q(x)=q(y)` and descent gives `h(x)=h(y)`, hence `q_1(x)=q_1(y)`.

This theorem gives an exact answer to the question “how much detail must be restored?”: restore exactly the distinctions required by the failed future observable and no more.

## 4. Deterministic future closure

Now let `X` be finite, let

\[
F:X\to X
\]

be a deterministic transition, and let

\[
q_0:X\to Q_0
\]

be the currently visible precision/observation partition.

Define recursively

\[
\boxed{
q_{t+1}(x)=\bigl(q_t(x),q_t(F(x))\bigr).
}
\]

Only the induced partition matters; arbitrary tuple labels may be replaced by finite integer class identifiers.

## 5. P023-T03 — Monotone refinement

For every `t`, `q_{t+1}` refines `q_t`.

Hence the process never merges two classes that were already distinguishable.

### Proof

Equality of `q_{t+1}` values includes equality of the first coordinate `q_t`.

## 6. P023-T04 — Finite stabilization bound

Let `c_t` be the number of classes represented by `q_t` and let `N=|X|`.

Every strict refinement increases `c_t` by at least one, while `c_t<=N`.

Therefore the number of strict refinement rounds is at most

\[
\boxed{N-c_0.}
\]

In particular, some finite stage `q_*` satisfies

\[
q_{*+1}=q_*.
\]

No infinite limit is required.

## 7. P023-T05 — Stable quotient is transition-compatible

At stabilization,

\[
q_*(x)=q_*(y)
\Longrightarrow
q_*(F(x))=q_*(F(y)).
\]

Therefore `F` induces a unique deterministic transition on the stable quotient:

\[
\boxed{
\bar F:q_*(X)\to q_*(X).
}
\]

### Proof

Since `q_{*+1}=q_*`, equal stable classes have equal pair signatures

\[
(q_*(x),q_*(F(x))).
\]

The second coordinates are therefore equal.

## 8. P023-T06 — Depth semantics

For every finite `t`,

\[
\boxed{
q_t(x)=q_t(y)
\iff
q_0(F^j(x))=q_0(F^j(y))
\text{ for all }0\le j\le t.
}
\]

### Proof

Induction on `t`.

The case `t=0` is the definition. For the induction step, equality of

\[
q_{t+1}(x)=\bigl(q_t(x),q_t(F(x))\bigr)
\]

is equivalent to agreement of depth-`t` signatures beginning at `x,y` and agreement of depth-`t` signatures beginning at `F(x),F(y)`, which together are exactly agreement of the original observation through time `t+1`.

Thus each refinement round adds exactly one further unit of future distinguishability.

## 9. P023-T07 — Coarsest future-compatible refinement

Let `s:X->S` be any partition satisfying:

1. `s` refines `q_0`;
2. `F` descends through `s`, i.e.
   \[
   s(x)=s(y)\Longrightarrow s(F(x))=s(F(y)).
   \]

Then `s` refines every `q_t`, hence it refines `q_*`.

Therefore

\[
\boxed{
q_*
\text{ is the coarsest transition-compatible refinement of }q_0.
}
\]

### Proof

Induct on `t`. The base case is assumption 1. If `s` refines `q_t`, then `s(x)=s(y)` implies both `q_t(x)=q_t(y)` and, by transition compatibility followed by the induction hypothesis, `q_t(F(x))=q_t(F(y))`. Therefore `s` refines `q_{t+1}`.

## 10. Interpretation: legal information loss

P023 gives a precise hierarchy.

### Unsafe collapse

Two states are merged even though some chosen future composition distinguishes them.

### One-step safe collapse

The current chosen observable is constant on every collapse fiber.

### Future-safe collapse

The transition itself descends to the quotient, so all later iterations are well-defined without restoring hidden representatives.

This suggests the project-wide rule

\[
\boxed{
\text{discard witness identity only after proving future compatibility.}
}
\]

The rule does **not** say that all microscopic detail must always be stored. It says that a coarser state is mathematically legitimate only relative to the operations/observations it is required to support.

## 11. Relation to P010, P011, P018, and P021

### P010 / P011

History merging and collision spectra show that many-to-one maps can destroy reconstructive information while preserving coarse observables. P023 asks when such a quotient still supports future composition.

### P018

P018 treats precision projection as a first-class operation. P023 adds a general compatibility gate: a precision projection may be used as a closed coarse dynamics only when the transition/observable factors through it. If it fails, the coarsest repair is a finite refinement rather than an appeal to hidden reals.

### P021

P021 showed that direction-transport cardinality matrices are not composition-complete because middle-incidence witness identity matters. The Stage-12 uniform-fiber theorem is a special safe-reduction regime. P023 generalizes the question from that example to arbitrary finite deterministic quotients.

## 12. Prior art and novelty discipline

The abstract mathematics here has close established relatives:

- factorization through quotient maps / congruences;
- finite-state distinguishability and Myhill–Nerode style future equivalence;
- bisimulation and deterministic quotient systems;
- partition refinement, including classical coarsest-partition algorithms such as Paige–Tarjan.

Accordingly, Enterprise Math does **not** claim the general partition-refinement or quotient-factorization theorems as original.

The project-specific contribution under test is the integration of these established tools with the existing finite-precision / collapse / collision / witness program and the interpretation of quotient compatibility as a proof obligation for legal precision loss.

## 13. Executable reference layer

Reference implementation:

- `src/enterprise_math/composition_safe_collapse.py`
- `tests/test_p023_composition_safe_collapse.py`

The test suite includes bounded exhaustive checks of the coarsest one-step repair and the coarsest stable compatible refinement, delayed future distinguishability examples, finite stabilization bounds, and a no-float/no-true-division audit.

## 14. Next questions

1. Extend from one deterministic transition to a finite family of operations.
2. Define the coarsest quotient compatible with a typed operation algebra rather than one endomap.
3. Relate the amount of required refinement to P011 collision spectra.
4. Determine when a P018 divisibility projection is already future-compatible and when its minimal repair can be expressed by bounded precision detail/carry coordinates.
5. Formalize T01/T02 and the finite deterministic closure theorem in Lean using standard quotient/partition machinery rather than bespoke abstractions.
