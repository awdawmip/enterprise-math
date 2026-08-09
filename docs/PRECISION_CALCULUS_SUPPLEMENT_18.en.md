# P018 — Finite-Precision Proof Calculus: Supplement 18

Status: `ACTIVE RESEARCH NOTE`  
Scope: finite future-observation refinement, canonical predictive closure, finite stabilization bounds, minimal dynamically autonomous quotient refinement, and the unary answer to P018-Q116  
Depends on: P005, P009, P010, P011, P018-T150–T159  
Prior-art boundary: finite deterministic state distinguishability, behavioral equivalence, automata congruences, and minimal quotient machines are established mathematics/computer science. See `docs/PRIOR_ART_P018_PREDICTIVE_CLOSURE.en.md`. [SRC-MOORE-1956-SEQUENTIAL] [SRC-NERODE-1958-AUTOMATON]

---

## 1. The exact problem left by Supplement 17

Supplement 17 proves that an observation

\[
O:X\to Y
\]

is dynamically autonomous for a deterministic endomap

\[
F:X\to X
\]

exactly when the observation kernel is forward compatible:

\[
O(x)=O(y)\Longrightarrow O(Fx)=O(Fy).
\]

When this fails, a coarse state is not sufficient for exact future evolution.

P018-Q116 asks what information must be restored.

For a **finite unary deterministic system**, there is a canonical answer: refine the observation only until states with different future observable behavior have been separated.

---

## 2. P018-T160 — Finite-horizon future-observation equivalence

Status: `PROVED / EXECUTABLE`

For each horizon `n>=0`, define

\[
\boxed{
x\equiv_n y
\iff
O(F^{[i]}x)=O(F^{[i]}y)
\quad\text{for every }0\le i\le n.
}
\]

Equivalently, assign to each state its finite observable signature

\[
\boxed{
\Sigma_n(x)
=
\bigl(O(x),O(Fx),\ldots,O(F^{[n]}x)\bigr).
}
\]

Then

\[
x\equiv_n y\iff \Sigma_n(x)=\Sigma_n(y).
\]

Thus every `equiv_n` is an ordinary finite equivalence relation and can be represented by an explicit finite partition.

---

## 3. P018-T161 — Predictive partitions refine monotonically

Status: `PROVED / EXECUTABLE`

One more future observation can only split an existing block:

\[
\boxed{
\equiv_{n+1}\ \subseteq\ \equiv_n.
}
\]

More precisely,

\[
\boxed{
x\equiv_{n+1}y
\iff
O(x)=O(y)
\ \text{and}\
Fx\equiv_n Fy.
}
\]

The second formula is the recursive refinement law.

This is the reverse orientation from P010 time-kernel growth: here we are **adding predictive information to a representation**, so indistinguishability becomes finer.

---

## 4. P018-T162 — Once predictive refinement stops, it stops forever

Status: `PROVED`

Suppose for some `n`

\[
\boxed{
\equiv_{n+1}=\equiv_n.
}
\]

Then

\[
\boxed{
\equiv_{n+k}=\equiv_n
\quad\forall k\ge0.
}
\]

### Proof

The recursive law says

\[
\equiv_{n+1}
=
\ker(O)\cap F^{-1}(\equiv_n).
\]

If `equiv_{n+1}=equiv_n`, then `equiv_n` is a fixed point of this refinement operator. Applying the same operator again returns the same relation, and induction gives permanent stabilization. ∎

At the same moment, the stabilized relation is forward compatible:

\[
x\equiv_n y\Longrightarrow Fx\equiv_n Fy.
\]

---

## 5. P018-T163 — Finite predictive closure has an explicit finite bound

Status: `PROVED / EXECUTABLE`

Assume `X` has

\[
N=|X|
\]

states and the original observation partition has

\[
c_0
\]

nonempty blocks.

Each strict refinement increases the number of blocks by at least one. No partition of `X` has more than `N` blocks.

Therefore the first stable horizon `h_*` satisfies

\[
\boxed{
h_*\le N-c_0.}
\]

No infinite limit is needed.

If all `N-c_0` possible strict refinements occur, the final partition is equality, which is automatically forward compatible, so stabilization occurs at that horizon at the latest.

---

## 6. P018-T164 — The stable relation is exactly all-future observational equivalence

Status: `PROVED`

Let `equiv_*` be the first stable predictive partition.

Then

\[
\boxed{
x\equiv_* y
\iff
O(F^{[n]}x)=O(F^{[n]}y)
\quad\forall n\in\mathbb N.
}
\]

### Proof

The forward implication follows because the stable relation is forward compatible and is contained in `ker(O)`. Repeatedly apply `F`; every future pair remains in the same stable relation and therefore has equal observation.

The reverse implication is immediate because equality of all future observations implies equality of the finite signature at the stable horizon. ∎

So the stable partition is not an approximation to infinite behavior. On a finite state space it is already reached after the finite bound in T163 and then certifies all later observation equality exactly.

---

## 7. P018-T165 — Predictive closure is the largest compatible equivalence inside the observation kernel

Status: `PROVED / EXECUTABLE`

Let `R` be any equivalence relation such that

\[
R\subseteq\ker(O)
\]

and

\[
xRy\Longrightarrow F(x)\,R\,F(y).
\]

Then

\[
\boxed{
R\subseteq\equiv_*.
}
\]

### Proof

If `xRy`, compatibility gives

\[
F^{[n]}x\ R\ F^{[n]}y
\]

for every finite `n`. Because `R` lies inside `ker(O)`, all those future states have equal observations. T164 then gives `x equiv_* y`. ∎

Therefore `equiv_*` is the **largest relation / coarsest partition** that simultaneously:

1. refines the original observation partition;
2. is dynamically closed under `F`.

---

## 8. P018-T166 — The quotient by predictive closure is the minimal exact autonomous refinement

Status: `PROVED STRUCTURAL CONSEQUENCE / EXECUTABLE`

Because `equiv_*` is forward compatible, `F` descends to a deterministic quotient map

\[
F_*:X/\!\equiv_*\to X/\!\equiv_*.
\]

Because `equiv_*` is contained in `ker(O)`, the original observation also descends to

\[
O_*:X/\!\equiv_*\to Y.
\]

The quotient therefore reproduces the original observation sequence exactly while evolving autonomously.

Now let `R` be any other dynamically compatible equivalence contained in `ker(O)`. T165 gives

\[
R\subseteq\equiv_*.
\]

Hence the quotient by `R` has at least as many blocks/states as the quotient by `equiv_*`.

Thus

\[
\boxed{
X/\!\equiv_*
}
\]

is the coarsest / smallest-state exact autonomous refinement of the original observation among quotient-state models of this form.

This is classical finite-state minimization territory; the Enterprise Math use is as an exact precision-state sufficiency criterion.

---

## 9. P018-T167 — The original precision is already dynamically closed exactly at horizon zero

Status: `PROVED / EXECUTABLE`

The following are equivalent:

1. the original observation kernel is forward compatible;
2. `equiv_1 = equiv_0`;
3. the first stable horizon is `0`;
4. predictive closure adds no new state distinction.

Therefore Supplement 17's dynamic-closure test is exactly the zero-step case of the canonical predictive-refinement construction.

---

## 10. P018-C16 — Sometimes exact future closure requires the full fine state

Status: `COUNTEREXAMPLE / INFORMATION BOUNDARY`

Take the finite state set

\[
X=\{0,1,2,3\}
\]

with deterministic transition

\[
F(0)=0,
\quad F(1)=0,
\quad F(2)=1,
\quad F(3)=2,
\]

and observation

\[
O(0)=O(2)=O(3)=0,
\qquad O(1)=1.
\]

The horizon partitions are

\[
\{\{0,2,3\},\{1\}\},
\]

then

\[
\{\{0,3\},\{1\},\{2\}\},
\]

then equality:

\[
\{\{0\},\{1\},\{2\},\{3\}\}.
\]

Thus `h_*=2=N-c_0`, attaining the T163 bound.

By T165, if predictive closure is equality then **no nontrivial equivalence quotient contained in the observation kernel can be both exact and dynamically autonomous**.

In such a system, exact future observation really requires retaining the full fine-state distinction.

---

## 11. P018-T168 — Unary P018-Q116 has a canonical finite answer

Status: `RESOLVED FOR FINITE UNARY DETERMINISTIC SYSTEMS`

For a finite deterministic endomap plus observation, the minimal exact state refinement required to restore dynamic closure is not arbitrary:

\[
\boxed{
\text{refine states by finite future-observation signatures until the partition stabilizes.}
}
\]

The construction:

- is finite;
- has explicit stopping bound `N-c0`;
- produces a forward-compatible equivalence;
- is the largest compatible equivalence inside the original observation kernel;
- yields the smallest quotient-state autonomous refinement preserving the original observations.

So P018-Q116 is resolved in this unary finite setting.

---

## 12. P018-C17 — The unary closure theorem does not solve binary operation descent

Status: `DESIGN BOUNDARY`

Supplement 17 C15 shows that quotient coordinates `Q_r(x)` do not support exact binary addition by themselves. Supplement 18 does not change that fact.

Unary future-observation refinement studies repeated application of one endomap

\[
F:X\to X.
\]

A binary operation

\[
\mu:X\times X\to X
\]

requires compatibility in **both input coordinates** and, more generally, compatibility under all allowed operation contexts.

Therefore the finite predictive closure above is not silently promoted to a solution of P018-Q117. Multi-ary congruence and minimal extension data remain a separate next problem.

---

## 13. Connection back to precision, time, and irreversibility

Supplement 18 sharpens the hierarchy from Supplement 17:

\[
\boxed{
\text{raw observation}
\to
\text{finite predictive refinement}
\to
\text{dynamically closed quotient state}
\to
\text{monotone time kernel / merger geometry}.
}
\]

If the raw precision is already closed, the first arrow is identity.

If it is not closed, predictive refinement restores exactly the distinctions needed for autonomous future observation and no more among quotient refinements.

After closure is restored, P010/P011/P018 merger-time machinery becomes valid on the quotient state itself rather than on a merely observational readout.

---

## 14. Executable pressure tests

Added:

- `src/enterprise_math/predictive_closure.py`
- `tests/test_predictive_closure.py`

Tests cover:

1. monotone refinement of finite-horizon partitions;
2. a bound-tight four-state example;
3. exhaustive `N<=4` deterministic endomaps with binary observations for the `N-c0` bound;
4. forward compatibility and observation refinement of the stable partition;
5. horizon-zero closure for already compatible observations;
6. maximality against all candidate partitions in a small finite example;
7. exact quotient dynamics and quotient observation;
8. the equality-closure case where no nontrivial exact quotient survives.

---

## 15. Current foundational feedback

The finite-precision state question can now be split into two exact tests:

### Static precision

Which fine states are identified by the observation?

### Dynamic sufficiency

Which of those identifications survive **all future allowed operations**?

For one finite deterministic endomap, predictive closure gives the canonical answer after finitely many refinements.

This suggests a stronger but still unfrozen design rule:

> **A finite precision state should not be judged only by present distinguishability. For the operations it is supposed to support autonomously, its equivalence relation must be a congruence; when it is not, the canonical repair is the coarsest operation-compatible refinement, not an arbitrary floating error margin.**

The unary theorem is now explicit. The multi-operation version remains open and should be attacked algebraically rather than by importing continuous approximation.
