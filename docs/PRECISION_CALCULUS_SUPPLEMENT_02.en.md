# P018 — Finite-Precision Proof Calculus, Supplement 02

Status: `ACTIVE RESEARCH NOTE`  
Scope: coarse-cell proof certificates, persistence under refinement, operation-level naturality defects  
Depends on: P018 Stage 1 and Supplement 01

## 1. From arithmetic identities to proof rules

The first two P018 stages established:

- exact finite precision fibers;
- nested detail and carry;
- degree-aware transport;
- signed precision shells;
- bounded nonlinear naturality defects.

The next question is proof-theoretic:

> When can a statement be settled at a coarse precision so that no later refinement can overturn it?

The answer begins with the fact that a coarse integer state is not an approximate real value.  It is the label of a finite set of explicit finer integer states.

## 2. P018-T21 — Precision cells are nested under compatible refinement

Status: `PROVED`

Let

\[
d\mid e\mid f.
\]

Fix an explicit state `x` at precision `f`.

The `d`-cell containing `x` is

\[
I_d(x)
=
\left[
R\left\lfloor\frac{x}{R}\right\rfloor,
R\left(\left\lfloor\frac{x}{R}\right\rfloor+1\right)-1
\right],
\qquad R=f/d.
\]

The `e`-cell is defined similarly with `S=f/e`.

Then

\[
\boxed{I_e(x)\subseteq I_d(x).}
\]

Proof: both cells are fibers of compatible Euclidean projections and

\[
\pi_{f\to d}
=
\pi_{e\to d}\circ\pi_{f\to e}.
\]

Every state in the finer fiber therefore has the same `d`-projection as `x`. ∎

This simple inclusion is the basis of proof persistence.

## 3. P018-T22 — Monotone image enclosure of a finite precision cell

Status: `PROVED`

Let

\[
F:\mathbb N^m\to\mathbb N
\]

be coordinatewise nondecreasing.

For a product precision cell

\[
\mathcal C
=
\prod_{i=1}^m[L_i,U_i],
\]

we have for every `x in C`

\[
\boxed{
F(L_1,\ldots,L_m)
\le
F(x_1,\ldots,x_m)
\le
F(U_1,\ldots,U_m).
}
\]

No continuity, real interval, derivative, or infinite completion is involved.  The enclosure is a finite order consequence on integer states.

This is structurally adjacent to rigorous interval arithmetic, which is established prior art.  P018's distinction is semantic: the cell is the actual finite projection fiber, not an enclosure of an unrepresented real point.

## 4. P018-T23 — Threshold proof certificate

Status: `PROVED`

Consider the predicate

\[
P_T(x): F(x)<T.
\]

Let

\[
L_F=F(L),
\qquad
U_F=F(U)
\]

be the finite cell-image bounds from T22.

Then exactly three proof statuses are available:

\[
\boxed{
U_F<T
\Longrightarrow
P_T\text{ is TRUE on the entire cell};
}
\]

\[
\boxed{
L_F\ge T
\Longrightarrow
P_T\text{ is FALSE on the entire cell};
}
\]

otherwise the coarse precision is

\[
\boxed{\text{UNRESOLVED}.}
\]

This is a finite proof rule, not a heuristic.

The equality predicate `F(x)=T` has the analogous certificate:

- TRUE if `L_F=U_F=T`;
- FALSE if `T` lies outside `[L_F,U_F]`;
- otherwise UNRESOLVED.

## 5. P018-T24 — Proof certificates persist under refinement

Status: `PROVED`

Suppose a threshold predicate is certified TRUE or FALSE on a cell at precision `d`.

Every compatible later precision cell is a subset of that cell by T21.  Therefore the same universal statement remains valid.

Hence

\[
\boxed{
\text{TRUE}\to\text{TRUE},
\qquad
\text{FALSE}\to\text{FALSE}
}
\]

under refinement.

Only

\[
\boxed{
\text{UNRESOLVED}
\to
\{\text{UNRESOLVED},\text{TRUE},\text{FALSE}\}
}
\]

is possible.

This is the general P018 form of “prove at low precision, refine only if necessary.”

A proof that has crossed the decision boundary at coarse precision is permanent.  Refinement is not allowed to reopen a finished proof obligation.

## 6. P018-T25 — Stage-1 order stability is a cell certificate

Status: `PROVED`

For two one-dimensional precision cells `I_x` and `I_y`, the proposition

\[
x<y
\]

is universally TRUE if

\[
\max I_x<\min I_y,
\]

and universally FALSE if

\[
\min I_x\ge\max I_y.
\]

When the two states have different coarse quotients, the uniform Euclidean fibers are disjoint and ordered, so this recovers P018-T03 exactly.

Thus T03 was the first special case of the general coarse-cell certificate calculus.

## 7. Operation-level naturality defect

Stage 2 treated monomials.  The same structure can be stated for a much broader operation class.

Let

\[
F:\mathbb N^m\to\mathbb N
\]

satisfy:

1. coordinatewise monotonicity;
2. integer `q`-homogeneity:

\[
F(r x_1,\ldots,r x_m)=r^qF(x_1,\ldots,x_m)
\]

for every positive integer `r`.

Write fine inputs as

\[
x_i=ra_i+u_i,
\qquad0\le u_i<r.
\]

## 8. P018-T26 — General monotone homogeneous defect bound

Status: `PROVED`

Define

\[
\mathcal R_F
=
\left\lfloor\frac{F(x)}{r^q}\right\rfloor
\]

and

\[
D_F=\mathcal R_F-F(a).
\]

Then

\[
\boxed{D_F\ge0.}
\]

and

\[
\boxed{
D_F
\le
F(a+\mathbf1)-F(a).
}
\]

Proof: since

\[
r a_i\le x_i\le r(a_i+1),
\]

monotonicity and homogeneity give

\[
r^qF(a)
\le
F(x)
\le
r^qF(a+\mathbf1).
\]

Divide by `r^q` with integer projection. ∎

For strictly cell-increasing maps such as the positive monomials of Stage 2, the upper endpoint is not attained inside the half-open input cell and the sharper `-1` bound of P018-T16 is recovered.

Thus the precision defect is defined for an operation class, not only for multiplication and powers.

## 9. P018-T27 — Exact zero-defect certificate

Status: `PROVED`

The naturality defect vanishes exactly when the fine output has not crossed the first new coarse output boundary:

\[
\boxed{
D_F=0
\iff
F(x)<r^q\bigl(F(a)+1\bigr).
}
\]

This is the operation-level **no-carry certificate**.

It generalizes:

- binary no-carry in addition;
- multiplication no-cell-crossing;
- root/collapse zero precision defect.

The object that matters is not an estimated numerical error but whether the fine output crossed a discrete coarse boundary.

## 10. P018-T28 — General homogeneous recovery monotonicity

Status: `PROVED`

Let

\[
d\mid e\mid f
\]

and let compatible degree-one inputs satisfy

\[
x_f=sx_e+u,
\qquad s=f/e,
\qquad u_i\ge0.
\]

For a coordinatewise nondecreasing `q`-homogeneous operation,

\[
F(x_f)
\ge
F(sx_e)
=
s^qF(x_e).
\]

Therefore its recovered value at base precision `d` is monotone:

\[
\boxed{
\mathcal R_{F;e\to d}
\le
\mathcal R_{F;f\to d}.
}
\]

P018-T19 is the monomial case; P018-T12 is the root/power-collapse case.

## 11. A proof process is now finite and directional

For a monotone predicate problem, P018 now supports the following exact process:

1. choose a coarse finite precision;
2. identify the finite projection cell;
3. compute a certified image interval using integer order;
4. if the predicate is constant on the whole cell, stop;
5. otherwise refine only that unresolved cell;
6. never reopen a certificate already proved at a coarser precision.

This is not “compute an approximate answer and hope it converges.”

It is a monotone sequence of finite proof obligations:

\[
\boxed{
\text{large finite fiber}
\supseteq
\text{smaller finite fiber}
\supseteq\cdots
}
\]

until the decision boundary is excluded or the chosen finite precision is exhausted.

## 12. Precision proof and precision dynamics

There are now two monotone directions in P018:

### Proof uncertainty decreases

Under refinement, an unresolved finite cell shrinks.  Once a predicate is decided, its certificate persists.

### Recovered nonlinear structure increases

For monotone homogeneous operations, the coarse value recovered from finer computation is nondecreasing by T28.

These are related but not identical monotonicities:

\[
\text{refinement}
\Longrightarrow
\begin{cases}
\text{proof cell shrinks},\\
\text{recoverable nonlinear coarse structure grows}.
\end{cases}
\]

This pair is a stronger expression of the claim that **precision change itself is mathematical dynamics**.

## 13. Counterexample / boundary: not every operation has a scale degree

A map such as

\[
F(x)=x^2+1
\]

is monotone, but it is not degree-two homogeneous:

\[
F(rx)=r^2x^2+1
\ne
r^2(x^2+1).
\]

It may accidentally satisfy a numerical defect bound on a particular cell, so a sound graded operation theorem must require the homogeneity contract explicitly; fitting one example is not enough.

The executable P018 implementation checks the homogeneity identity at the scaled cell corners before using the general defect theorem.

## 14. Relation to interval arithmetic

Rigorous interval arithmetic already proves statements by propagating finite enclosures, and that prior art is explicitly registered in Enterprise Math.

P018's mathematical difference is not the generic idea “bounds can prove a statement.”  The proposed project-specific structure is the combination of:

- finite integer projection fibers as primary precision states;
- canonical divisibility refinement;
- persistent coarse proof certificates;
- graded exact transport;
- discrete carry/naturality defects;
- signed cross-scale shell cancellation;
- no required hidden real completion.

Whether that integrated package yields proofs unavailable or substantially simpler in standard frameworks remains an open research question.

## 15. Stage-3 status

- P018-T21 precision-cell nesting: `PROVED`
- P018-T22 monotone finite-cell image enclosure: `PROVED`
- P018-T23 threshold proof certificate: `PROVED`
- P018-T24 proof-certificate persistence: `PROVED`
- P018-T25 order stability as cell certificate: `PROVED`
- P018-T26 general monotone homogeneous defect bound: `PROVED`
- P018-T27 exact zero-defect/no-carry certificate: `PROVED`
- P018-T28 homogeneous operation recovery monotonicity: `PROVED`
- nonmonotone predicate calculus: `OPEN`
- adaptive precision-selection optimality: `OPEN`
- compositional certificates across several operations: `OPEN`
- P017 reinterpretation through this certificate calculus: `OPEN`

Executable checks live in `src/enterprise_math/precision_proof.py` and `tests/test_precision_proof.py`.
