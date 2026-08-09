# P023 — Safe-Precision Interior, Supplement 06

Status: `ACTIVE RESEARCH NOTE`  
Scope: future-safe precision as an interior-like selector on finite quotient relations  
Depends on: P023 first-stage quotient safety, P020 well-founded finite stabilization, and P008 interior-like collapse structure  
Discipline: quotient congruences, automata distinguishability, partition refinement, and fixed-point operators are established mathematics. The project-specific content is the finite-precision interpretation, the bridges among existing Enterprise Math modules, and the arithmetic consequences proved below.

## 1. Why Stage 2 changes the object being studied

P023 Stage 1 starts from a coarse observation `q` and repeatedly adds only future distinctions that are required to make selected operations well-defined on coarse states.

A labeled partition is only a representation. The invariant object is its equivalence relation

\[
E_q=\{(x,y):q(x)=q(y)\}.
\]

Larger relations identify more fine states and therefore represent coarser precision. Refinement means relation inclusion decreases.

For a finite operation family

\[
\mathcal A=\{F_a:X\to X\},
\]

define

\[
\boxed{
\Phi_{\mathcal A}(E)
=
E\cap\bigcap_{a\in\mathcal A}(F_a\times F_a)^{-1}(E).
}
\]

The pair `(x,y)` survives one precision round exactly when it was already identified and every generator still sends it to an identified pair.

## 2. P023-S2-T01 — Safe relation step is monotone and reductive

Status: `PROVED`.

On equivalence relations ordered by inclusion,

\[
\boxed{\Phi_{\mathcal A}(E)\subseteq E}
\]

and

\[
E\subseteq E'
\Longrightarrow
\Phi_{\mathcal A}(E)\subseteq\Phi_{\mathcal A}(E').
\]

Moreover, `Phi_A(E)` is again an equivalence relation.

### Proof

Reductivity is immediate from the leading intersection with `E`. Monotonicity follows because both intersection and inverse image preserve inclusion. Each `(F_a x,F_a y) in E` condition is an equivalence relation whenever `E` is; intersections of equivalence relations remain equivalence relations. ∎

## 3. P023-S2-T02 — Fixed points are exactly operation-compatible precisions

Status: `PROVED`.

For an equivalence relation `E`,

\[
\boxed{
\Phi_{\mathcal A}(E)=E
\iff
(xEy\Rightarrow F_a(x)E F_a(y)\text{ for every }a).
}
\]

So the fixed points of `Phi_A` are exactly the quotients on which every generator induces a well-defined coarse operation.

## 4. P023-S2-T03 — P023 future closure is an instance of P020 stabilization

Status: `PROVED` for finite `X`.

For finite `X`, the set of equivalence relations on `X` is finite. Hence strict relation inclusion is well-founded. By T01, `Phi_A` is monotone and reductive. P020 therefore applies directly.

Starting from the initial observation relation `E_0`, finite iteration of `Phi_A` reaches

\[
\boxed{
\operatorname{Safe}_{\mathcal A}(E_0),
}
\]

the **greatest `Phi_A`-fixed relation contained in `E_0`**.

Equivalently, it is the coarsest refinement of the original precision on which every selected operation descends.

This identifies the earlier P023 partition-refinement algorithm with a canonical P020 finite-stabilization problem rather than a separate convergence principle.

## 5. P023-S2-T04 — Safe precision selector is itself interior-like

Status: `PROVED` for finite `X`.

The map

\[
E_0\longmapsto\operatorname{Safe}_{\mathcal A}(E_0)
\]

is:

- monotone;
- reductive;
- idempotent;
- fixed exactly on `A`-compatible equivalence relations.

Thus P023 produces an **interior-like operator on precision relations**. This mirrors the P008 algebraic pattern, but the object being collapsed is now a precision relation rather than an integer value.

Two useful monotonicities follow immediately:

\[
E'_0\subseteq E_0
\Longrightarrow
\operatorname{Safe}_{\mathcal A}(E'_0)
\subseteq
\operatorname{Safe}_{\mathcal A}(E_0),
\]

and for operation families

\[
\mathcal A\subseteq\mathcal B
\Longrightarrow
\operatorname{Safe}_{\mathcal B}(E_0)
\subseteq
\operatorname{Safe}_{\mathcal A}(E_0).
\]

Finer initial knowledge cannot require a coarser safe state, and asking the quotient to support more operations cannot reduce the required precision.

## 6. P023-S2-T05 — Idempotent operation closes after one repair

Status: `PROVED`; mother statements added to Lean on this research branch.

Let

\[
T:X\to X,
\qquad T^2=T,
\]

and let `q` be any coarse observation. Define

\[
\boxed{r(x)=(q(x),q(Tx)).}
\]

Then:

1. `r` refines `q`;
2. `T` descends through `r`;
3. every `T`-compatible refinement of `q` refines `r`.

Therefore `r` is already the **full coarsest future-safe refinement for every repeated application of the idempotent T**. No second refinement round is needed.

### Proof

If `r(x)=r(y)`, then `q(Tx)=q(Ty)`. By idempotence,

\[
r(Tx)=(q(Tx),q(T^2x))=(q(Tx),q(Tx)),
\]

and similarly for `y`, so `r(Tx)=r(Ty)`.

Now let `s` refine `q` and support `T`. From `s(x)=s(y)`, compatibility gives `s(Tx)=s(Ty)`; because `s` refines `q`, this implies `q(Tx)=q(Ty)`. Hence `s` refines `(q,qT)`. ∎

This theorem does not require finiteness or integer arithmetic.

## 7. P023-S2-T06 — One pass of single-operation selectors is not enough

Status: `DISPROVED` as a general shortcut.

It may be tempting to compute a safe quotient for `F`, then one for `G`, and stop. This is not valid in general: refining for a later operation can destroy compatibility with an earlier operation.

A five-state counterexample uses

\[
F=(0,4,3,2,3),
\qquad
G=(2,0,1,2,2),
\]

with initial observation

\[
E=(0,0,0,0,1).
\]

The simultaneous safe selector is the discrete partition

\[
(0,1,2,3,4).
\]

But one pass gives

\[
F\to G:\ (0,1,2,0,3),
\]

which is not `F`-compatible, while

\[
G\to F:\ (0,1,0,0,2),
\]

which is not `G`-compatible.

Thus the family problem genuinely requires simultaneous or repeated common closure. A composition of individual selectors is not automatically a common selector.

## 8. Monotone reductive idempotent maps on the integer chain

Now specialize to

\[
T:\mathbb N\to\mathbb N
\]

that is monotone, reductive, and idempotent. P008 identifies exactly this interior-like pattern.

For every `n`, `T(n)` is the greatest `T`-fixed point not exceeding `n`: it is fixed by idempotence, and if `f<=n` is fixed then monotonicity gives

\[
f=T(f)\le T(n).
\]

Therefore the action of `T` is completely controlled by the placement of its fixed points along the integer chain.

## 9. P023-S2-T07 — Fixed-point alignment criterion for uniform floor precision

Status: `PROVED`.

Fix

\[
Q_r(n)=n//r,
\qquad
D_r(n)=r(n//r),
\qquad r\ge2.
\]

Then

\[
\boxed{
Q_r\circ T\text{ descends through }Q_r
\iff
f\in\operatorname{Fix}(T)
\Rightarrow
D_r(f)\in\operatorname{Fix}(T).
}
\]

In words: the fixed set of `T` must be closed under projection to the left boundary of every `r`-cell it enters.

### Proof

Consider one cell

\[
I_q=[qr,(q+1)r-1].
\]

If `qr` is fixed, then for every `n in I_q`, monotonicity and reductivity give

\[
qr=T(qr)\le T(n)\le n<(q+1)r,
\]

so `Q_r(T(n))=q` throughout the cell.

If `qr` is not fixed and the cell contains no fixed point, then the greatest fixed point below every member of the cell is the same one below `qr`; hence `T` is constant on that cell.

If `qr` is not fixed but an interior point `f in I_q` is fixed, then before the first fixed point the coarse output is below `q`, while at `f` the output is `q`; descent fails.

Therefore failure occurs exactly when some fixed point lies in an `r`-cell whose left endpoint is not fixed. This is exactly the stated closure condition. ∎

## 10. P023-S2-T08 — Every floor cell has at most two coarse outputs

Status: `PROVED` under the same hypotheses.

For every `q`,

\[
\boxed{
\left|\{Q_r(T(n)):n\in I_q\}\right|\le2.
}
\]

If the cell contains no new fixed point, the output is constant. If it does, the only two possibilities are the older fixed-point cell and the current cell `q`.

Consequently the canonical repair

\[
(Q_r,Q_rT)
\]

requires at most one local bit inside each `Q_r` cell. Because `T` is idempotent, T05 upgrades that one-step repair to the full future-safe quotient for repeated `T`.

## 11. P023-S2-T09 — P007 multiple-collapse classification is a fixed-point corollary

Status: `PROVED`.

For

\[
D_d(n)=d(n//d),
\]

one has

\[
\operatorname{Fix}(D_d)=d\mathbb N.
\]

Applying T07, closure under `D_r` holds exactly when

\[
\boxed{d\mid r\quad\text{or}\quad r\mid d.}
\]

Thus the earlier P023/P007 compatibility theorem is not an isolated arithmetic coincidence; it is a special case of fixed-set alignment for interior-like collapses.

## 12. P023-S2-T10 — Perfect-power collapse has a global uniform-precision no-go

Status: `PROVED`.

Let

\[
C_p(n)=R_p(n)^p,
\qquad p\ge2,
\]

and let `r>=2`. Then

\[
\boxed{Q_r\circ C_p\text{ never descends globally through }Q_r.}
\]

A uniform witness is

\[
y=(r+1)^p,
\qquad
x=y-1.
\]

Because `y congruent 1 mod r`,

\[
Q_r(x)=Q_r(y).
\]

But

\[
C_p(y)=y,
\qquad
C_p(x)=r^p,
\]

and their `Q_r` images differ for `p>=2`.

The fixed-point proof is even shorter: `y` is fixed, but

\[
D_r(y)=y-1
\]

is strictly between `r^p` and `(r+1)^p` and therefore is not fixed by `C_p`. T07 fails.

So no nontrivial uniform floor precision alone can carry the global perfect-power collapse dynamics. Yet T05 and T08 show that a localized one-bit repair per split cell is sufficient for the full repeated-collapse future.

## 13. P023-S2-T11 — Uniform scale factors are not closed under minimal safe repair

Status: `PROVED` for the P007 incompatible multiple-collapse case.

Take `Q_r` and `D_d` with neither `d|r` nor `r|d`. Stage 1 proved that the coarsest repair splits some `Q_r` fibers and leaves others unsplit.

Any uniform quotient `Q_s` that refines `Q_r` must satisfy

\[
\boxed{s\mid r.}
\]

If `s=r`, it splits no `Q_r` fiber. If `s<r`, it divides **every** `Q_r` fiber into the same `r/s` regular subcells. Neither behavior equals a repair that splits only selected fibers.

Therefore

\[
\boxed{
\text{the uniform divisibility scale family is not closed under operation-safe repair.}
}
\]

The P005/P018 divisibility lattice remains an important regular-precision subfamily, but the general future-safe precision object must allow a regular coarse tag plus localized bounded detail, or equivalently nonuniform finite partitions.

## 14. De-duplication with P018

P018 already defines the exact finite response

\[
\mathcal R_F(x,h)=F(x+h)-F(x).
\]

For a reductive `T`, with gap

\[
G_T(n)=n-T(n),
\]

P023 Stage-1 borrow satisfies

\[
\boxed{
B_{T,r}(n)
=Q_r(n)-Q_r(T(n))
=\mathcal R_{Q_r}(T(n),G_T(n)).
}
\]

So P023 should not maintain a competing primitive borrow theory. P018 owns the concrete finite-response/carry transport. P023 contributes the separate statement that the response value is exactly the minimal additional observable required for safe descent in this setting.

## 15. Feedback to P021

The P021 phase/magnitude correction now has a precise P023 interpretation.

If the same finite clock magnitude occurs on negative, zero, and positive causal phases, then causal phase is not constant on magnitude fibers. By P023 Stage-1 factorization,

\[
\boxed{\text{phase does not descend through the magnitude-only quotient}.}
\]

The coarsest one-step repair for that causal observation is exactly

\[
\boxed{(\text{magnitude},\text{phase}).}
\]

Likewise, P021's direction-transport count matrix loses the identity of shared middle incidences and therefore is not composition-safe for exact multi-step path transport; the witness relation is the required repair layer.

These are not new black-hole assumptions. They are applications of the same general quotient-safety criterion.

## 16. Computational audit

`src/enterprise_math/p023_safe_precision_interior.py` implements the relation selector, fixed-point iteration, idempotent one-step repair, and the deliberately noncanonical sequential-selector shortcut.

`tests/test_p023_safe_precision_interior.py` checks selector agreement with the Stage-1 partition implementation, reductivity/fixed-point compatibility, selector monotonicities, exhaustive three-state idempotent repair, and the explicit five-state two-operation counterexample.

Independent research-session enumeration additionally checked the integer-chain fixed-point alignment criterion and two-output bound on all monotone reductive idempotent maps through eight finite chain states, with no counterexample found. Finite checks audit the implementation; the proofs above carry the theorem claims.

## 17. Next gate

The highest-value next steps are:

1. compile the new Lean idempotent-repair theorems under the repository warning-fatal gate;
2. formalize `Phi_A` as a monotone reductive endomap on finite equivalence relations and connect its stabilization directly to the existing P020 Lean theorem;
3. decide the minimal typed representation for `regular scale + localized bounded detail` without replacing P005's useful divisibility lattice;
4. pressure-test the fixed-point alignment criterion against additional P008-style collapse families rather than adding more unrelated diagnostics.
