# P018 — Finite-Precision Proof Calculus: Supplement 17

Status: `ACTIVE RESEARCH NOTE`  
Scope: observation kernels, dynamic closure of precision states, semiconjugacy, merger-time contraction, quotient-operation descent, and carry as exact closure data  
Depends on: P005, P008, P009, P010, P011, P018-T71–T149  
Discipline: quotient factorization, congruence relations, semiconjugacy, and descent of operations are established mathematics. This stage tests their exact role in Enterprise Math finite-precision semantics and does not claim those general constructions as inventions.

---

## 1. True state merging and observed equality are not the same statement

Let

\[
F:X\to X
\]

be fine deterministic dynamics and let

\[
O:X\to Y
\]

be an observation or precision projection.

At time `n`, define observed equality by

\[
\boxed{
O(F^{[n]}x)=O(F^{[n]}y).
}
\]

This is weaker than true state equality

\[
F^{[n]}x=F^{[n]}y.
\]

True equality is permanent under every later common deterministic suffix. Observed equality need **not** be permanent because hidden fine detail may reappear in later observations.

This distinction is necessary before applying P010 irreversibility language to a coarse precision level.

---

## 2. P018-T150 — Fixed-time postprocessing can only coarsen an observation kernel

Status: `PROVED / EXECUTABLE`

Let

\[
O_1:X\to Y,
\qquad
H:Y\to Z,
\qquad
O_2=H\circ O_1.
\]

For every fixed time `n`,

\[
\boxed{
\ker(O_1\circ F^{[n]})
\subseteq
\ker(O_2\circ F^{[n]}).
}
\]

### Proof

If

\[
O_1(F^{[n]}x)=O_1(F^{[n]}y),
\]

then applying `H` gives

\[
H(O_1(F^{[n]}x))=H(O_1(F^{[n]}y)).
\]

∎

Thus **precision coarsening is always kernel-coarsening at one fixed time**. No dynamical closure assumption is needed for this axis.

---

## 3. P018-C14 — Coarse observational equality can split again

Status: `COUNTEREXAMPLE / FOUNDATIONAL WARNING`

Take natural coordinates with

\[
F(n)=2n,
\qquad
O(n)=n//2.
\]

At time zero,

\[
O(0)=O(1)=0.
\]

So the histories `0` and `1` are observationally indistinguishable.

After one fine step,

\[
F(0)=0,
\qquad
F(1)=2,
\]

and therefore

\[
O(F(0))=0,
\qquad
O(F(1))=1.
\]

The observed pair leaves the diagonal.

Hence

\[
\boxed{
\text{observed equality at one precision}
\not\Rightarrow
\text{persistent future observed equality}.
}
\]

This does not contradict P010. The fine histories never became the same fine state; only their coarse readouts happened to coincide.

---

## 4. P018-T151 — Dynamic closure is exactly preservation of the observation kernel

Status: `PROVED`

Define the observation kernel congruence condition

\[
\boxed{
O(x)=O(y)
\Longrightarrow
O(Fx)=O(Fy).
}
\]

Then the following are equivalent:

1. the condition above holds;
2. the time-zero observed kernel is contained in the time-one observed kernel;
3. for every `n`,
   \[
   \ker(O\circ F^{[n]})
   \subseteq
   \ker(O\circ F^{[n+1]}).
   \]

### Proof

`3 -> 2` is immediate, and `2 -> 1` is exactly the definitions at times zero and one.

For `1 -> 3`, if

\[
O(F^{[n]}x)=O(F^{[n]}y),
\]

apply the kernel-congruence condition to the two intermediate fine states `F^[n]x` and `F^[n]y`. This yields equality after one more fine step. ∎

Thus a coarse observation has a P010-like irreversible kernel filtration **if and only if its fibers are forward-compatible with the fine dynamics**.

---

## 5. P018-T152 — Surjective dynamic closure is equivalent to autonomous coarse dynamics

Status: `PROVED / ESTABLISHED QUOTIENT-FACTORIZATION THEOREM`

Assume

\[
O:X\twoheadrightarrow Y
\]

is surjective.

Then the kernel-congruence condition

\[
O(x)=O(y)
\Rightarrow
O(Fx)=O(Fy)
\]

holds if and only if there exists a unique deterministic map

\[
G:Y\to Y
\]

such that

\[
\boxed{
O\circ F=G\circ O.
}
\]

### Proof sketch

If `G` exists, equal `O`-images stay equal after applying `G`, so kernel compatibility follows.

Conversely, for every `y in Y` choose any `x` with `O(x)=y` and set

\[
G(y):=O(Fx).
\]

Kernel compatibility makes this independent of the chosen representative. Surjectivity gives existence for every `y` and also gives uniqueness. ∎

### Meaning for precision

A precision coordinate is dynamically self-contained under `F` exactly when `F` descends through the precision quotient.

If this fails, the coarse coordinate is not enough to evolve exactly; hidden detail is dynamically relevant.

---

## 6. P018-T153 — Semiconjugacy transports finite coalescence at the same time

Status: `PROVED / LEAN TARGET`

Suppose

\[
O\circ F=G\circ O.
\]

Then by finite iteration,

\[
O\circ F^{[n]}=G^{[n]}\circ O.
\]

Therefore

\[
F^{[n]}x=F^{[n]}y
\Longrightarrow
G^{[n]}(O x)=G^{[n]}(O y).
\]

In the `CoalescedBy` language,

\[
\boxed{
\operatorname{CoalescedBy}_F(n;x,y)
\Longrightarrow
\operatorname{CoalescedBy}_G(n;Ox,Oy).
}
\]

The new Lean theorem `coalescedBy_semiconj` formalizes this relation-level statement using mathlib's established `Semiconj.iterate_right` machinery.

---

## 7. P018-T154 — Merger time contracts under coarse semiconjugacy and is invariant under injective chart change

Status: `PROVED / LEAN RELATION-LEVEL SUPPORT`

When finite merger times exist, T153 gives

\[
\boxed{
\bar\tau_G(Ox,Oy)
\le
\bar\tau_F(x,y).
}
\]

A noninjective coarse representation may identify histories strictly earlier.

If `O` is injective, then equality of the observed iterates implies equality of the fine iterates, so every finite coalescence level is equivalent:

\[
\boxed{
F^{[n]}x=F^{[n]}y
\iff
G^{[n]}(Ox)=G^{[n]}(Oy).
}
\]

Hence

\[
\boxed{
\bar\tau_G(Ox,Oy)=\bar\tau_F(x,y).
}
\]

In particular, a bijective precision-chart change with conjugated dynamics preserves the entire labelled merger-time geometry exactly.

This resolves P018-Q112 under the correct hypothesis: **legitimate invertible chart transition plus conjugated dynamics**.

---

## 8. P018-T155 — A compatible precision chain gives a genuine precision-time bifiltration

Status: `PROVED STRUCTURAL CONSEQUENCE`

Suppose precision observations form a coarsening chain

\[
O_c=H\circ O_f
\]

and each level is dynamically closed, so autonomous coarse dynamics exist and commute with the observation maps.

For the same labelled fine histories define the precision-time kernel

\[
K_{O,n}
=
\{(x,y):O(F^{[n]}x)=O(F^{[n]}y)\}.
\]

Then two monotonicities hold:

### Precision axis

For fixed `n`,

\[
\boxed{
K_{O_f,n}\subseteq K_{O_c,n}.
}
\]

This is T150.

### Time axis

For fixed dynamically closed `O`,

\[
\boxed{
K_{O,n}\subseteq K_{O,n+1}.
}
\]

This is T151.

Therefore compatible precision and deterministic time generate an increasing two-parameter family of kernel relations.

Without dynamic closure, only the precision-axis inclusion is guaranteed; the time axis can reverse as C14 shows.

This is a finite bifiltration statement. No categorical duality between precision and time is claimed.

---

## 9. P018-T156 — P011 spectra are monotone under precision coarsening at fixed time

Status: `DERIVED FROM P011 / PROVED`

Fix a finite labelled history set `H` and time `n`.

A coarser observation is a postcomposition of a finer observation. Therefore its kernel partition is a coarsening of the finer partition. P011-S02 then gives coefficientwise

\[
\boxed{
K_{O_f,n}(t)
\preceq_{\rm coeff}
K_{O_c,n}(t).
}
\]

Thus precision coarsening can only increase or preserve the observed collision counts at every order **at the same time**.

Along the time axis, the same monotonicity is valid only when the observation is dynamically closed.

C14 gives an explicit failure without closure: on histories `{0,1}`, `F(n)=2n`, `O(n)=n//2`, the observed quadratic collision count falls from `1` at time zero to `0` at time one.

So observed collision-spectrum monotonicity is not an automatic law of coarse readout; it is a law of dynamically closed quotient evolution.

---

## 10. P018-C15 — Quotient coordinates alone cannot carry exact addition

Status: `COUNTEREXAMPLE / DESCENT OBSTRUCTION`

Let

\[
Q_r(n)=n//r,
\qquad r>1.
\]

Suppose there were a binary operation `boxplus` on coarse coordinates such that

\[
Q_r(x+y)=Q_r(x)\boxplus Q_r(y)
\]

for every `x,y`.

Compare the fine input pairs

\[
(0,0)
\]

and

\[
(r-1,1).
\]

Both have the same coarse coordinate pair:

\[
(Q_r(0),Q_r(0))=(0,0),
\]

and

\[
(Q_r(r-1),Q_r(1))=(0,0).
\]

But their coarse sums differ:

\[
Q_r(0+0)=0,
\qquad
Q_r((r-1)+1)=Q_r(r)=1.
\]

Therefore no coarse binary operation on quotient coordinates alone can reproduce exact fine addition.

This is stronger than saying floor projection is not an additive homomorphism. It says the quotient coordinate itself is **not sufficient state for exact addition**.

---

## 11. P018-T157 — Detail plus carry is exact extension data restoring additive closure

Status: `DERIVED FROM T72–T75 / PROVED`

Write

\[
x=ra+u,
\qquad
y=rb+v,
\qquad 0\le u,v<r.
\]

Then

\[
\boxed{
Q_r(x+y)
=a+b+\kappa_r(u,v),
}
\]

and

\[
\boxed{
(x+y)\bmod r
=(u+v)\bmod r.
}
\]

Thus the enriched state

\[
(a,u)
\]

supports an exact closed twisted addition, while the coarse coordinate `a` alone does not.

Carry is therefore not merely an arithmetic correction term. In the descent language it is part of the **extension data required to restore exact operation closure after a noncongruent quotient**.

The fact that this extension data forms a cocycle is established prior mathematics; the present point is its role in precision-state sufficiency.

---

## 12. P018-T158 — Critical-square defect measures failure of a proposed coarse operation to be the descent

Status: `PROVED / REINTERPRETATION`

Given

\[
\pi:X_e\to X_d,
\qquad
F_e:X_e\to X_e,
\qquad
F_d:X_d\to X_d,
\]

Supplement 12/13 compares the two endpoints

\[
\pi(F_e(x))
\quad\text{and}\quad
F_d(\pi(x)).
\]

The proposed coarse operation is an exact descent precisely when every such critical-square pair lies on the diagonal:

\[
\boxed{
\pi\circ F_e=F_d\circ\pi.
}
\]

A nonzero critical-square defect therefore certifies failure of **that proposed** `F_d` to realize the fine dynamics.

Important distinction:

- failure of one proposed `F_d` does not by itself prove that no coarse descent exists;
- absolute nonexistence of any descent is proved by failure of the kernel-congruence condition in T151/T152.

This separates representation choice from a genuine state-sufficiency obstruction.

---

## 13. P018-T159 — Dynamic-closure criterion for a precision state

Status: `FOUNDATIONAL SYNTHESIS / NOT FROZEN`

For a surjective precision map

\[
\pi:X_e\twoheadrightarrow X_d,
\]

and fine deterministic operation `F_e`, the coarse state `X_d` is exact and autonomous for that operation if and only if

\[
\boxed{
\pi(x)=\pi(y)
\Longrightarrow
\pi(F_e x)=\pi(F_e y).
}
\]

Equivalently, the precision kernel must be a congruence for the operation.

When this holds, there is a unique descended operation `F_d` and coarse history has a genuine monotone kernel/merger-time calculus.

When it fails, one must do at least one of the following:

1. retain additional detail state;
2. retain an exact defect/extension datum such as carry;
3. accept that the coarse representation is observational only and not an autonomous dynamical state.

This gives a sharper candidate foundational rule:

> **Finite precision is not only a partition of values. A precision state is dynamically complete for an operation exactly when that partition is operation-congruent.**

This rule is still a research synthesis and is not promoted into `FOUNDATIONS` by this note.

---

## 14. Executable and formal pressure tests

Added executable checks:

- `src/enterprise_math/observation_kernel.py`
- `tests/test_observation_kernel.py`

They test:

1. fixed-time postprocessing only coarsens observation kernels;
2. observed equality can split under `F(n)=2n`, `O(n)=n//2`;
3. a semiconjugate coarse evolution is dynamically closed;
4. coarse equality may occur strictly earlier than true state coalescence;
5. observed P011 collision count can decrease with time when closure fails;
6. compatible observed kernels are monotone in time;
7. quotient coordinates fail exact binary addition for every tested radix `r>1`.

Lean support in `EnterpriseMath/State/Coalescence.lean` now includes:

- finite coalescence transport under `Function.Semiconj`;
- exact finite coalescence-level invariance under injective semiconjugacy;
- eventual-coalescence transport and injective invariance.

---

## 15. Feedback into the bottom logic

The current deterministic precision/time hierarchy is therefore not simply two monotone axes by default.

The correct structure is:

\[
\boxed{
\text{fine State}
\xrightarrow{\text{precision quotient}}
\text{coarse representation}
}
\]

with a separate question:

\[
\boxed{
\text{does the operation descend through the quotient?}
}
\]

If yes, the coarse representation becomes an autonomous state space and inherits monotone merger-time geometry.

If no, observational equality can split and the missing detail/defect remains dynamically relevant.

This explains, in one framework, why:

- P005 insists on typed precision states;
- P009 warns against erased-type fake dynamics;
- carry survives as exact detail-dependent operation data;
- critical-square holonomy matters;
- P010 irreversibility applies to true deterministic state merging, not arbitrary coarse equality;
- P011 spectrum monotonicity along an observed time axis requires dynamic closure.

---

## 16. Next questions

### P018-Q116 — Minimal extension restoring congruence

Given a noncongruent precision quotient and an operation, characterize the smallest finite detail object that makes the operation descend exactly. Carry solves one additive prototype; seek the general finite-state analogue.

### P018-Q117 — Binary and multi-ary operation congruence

Generalize T152 from unary dynamics to binary/multi-ary operations. Determine when the required extension data forms cocycles or higher coherence objects and when that language is unnecessary.

### P018-Q118 — Precision-time bifiltration invariants

For dynamically closed precision chains, study finite invariants of the two-parameter kernel filtration without importing continuous persistence machinery as an ontology.

### P018-Q119 — Approximate closure is not yet defined

Do not replace exact congruence failure by a floating error tolerance. If an approximate closure notion is needed, define it using explicit finite states, fibers, and certificates first.

---

## 17. Current conclusion

The strongest new foundational criterion in this stage is exact:

\[
\boxed{
\text{coarse state is dynamically autonomous}
\iff
\text{its precision kernel is an operation congruence}.
}
\]

Semiconjugacy then transports finite coalescence without delay, injective chart change preserves it exactly, and noninjective coarsening may make histories indistinguishable earlier.

When congruence fails, observed equality is not irreversible and may split later. In the additive quotient prototype, coarse coordinates fail closure exactly because hidden residues control carry; enriching the state by detail plus carry restores a closed exact operation.

This links precision, defect, time, and irreversibility without introducing a hidden continuum or an error-bar ontology.
