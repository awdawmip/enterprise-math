# P018 — Finite-Precision Proof Calculus, Supplement 05

Status: `ACTIVE RESEARCH NOTE`  
Scope: predicate-specific conflict multiplicity, adaptive multi-axis precision selection, and finite integer decision-cost optimization  
Depends on: P018 Stages 1–5  
Discipline: decision trees and dynamic programming are established ideas. P018 studies them only on finite precision observations and does not claim those generic algorithms as inventions.

## 1. More information is not the same as more proof

Stage 5 introduced ambiguity multiplicity

\[
A_\lambda(x)=|[x]_\lambda|,
\]

the number of terminal states still compatible with the current precision observation.

That quantity measures state uncertainty, but a proof usually targets one predicate

\[
P:X\to\{\mathrm{true},\mathrm{false}\}.
\]

A refinement may remove many terminal states that agree with `x` on `P` while leaving every state that could overturn the proposition.

So adaptive proof precision needs a predicate-specific quantity.

Define the **predicate conflict fiber**

\[
K_{\lambda,P}(x)
=
\{y\in[x]_\lambda:P(y)\ne P(x)\}
\]

and its **conflict multiplicity**

\[
\boxed{
C_{\lambda,P}(x)=|K_{\lambda,P}(x)|.
}
\]

This counts exactly the currently compatible terminal states that still disagree with the target truth value.

## 2. P018-T45 — Predicate certificate iff conflict multiplicity is zero

Status: `PROVED`

For every finite precision observation,

\[
\boxed{
C_{\lambda,P}(x)=0
\iff
P\text{ is constant on }[x]_\lambda.
}
\]

Therefore

\[
\boxed{
C_{\lambda,P}(x)=0
\iff
\text{the P018 predicate certificate is TRUE or FALSE}.
}
\]

Proof: zero conflict means that no state in the fiber has truth value opposite to `P(x)`, so every state in the fiber has the same truth value. The converse is immediate. ∎

Thus conflict multiplicity is an exact integer measure of the remaining **proof obstruction**, not merely of the remaining state ambiguity.

## 3. P018-T46 — Conflict multiplicity is nonincreasing under refinement

Status: `PROVED`

If `mu` refines `lambda`, then

\[
[x]_\mu\subseteq[x]_\lambda.
\]

Intersecting both sides with the opposite-truth class gives

\[
K_{\mu,P}(x)
\subseteq
K_{\lambda,P}(x).
\]

Hence

\[
\boxed{
C_{\mu,P}(x)
\le
C_{\lambda,P}(x).
}
\]

Once this quantity reaches zero, T45 and Stage-5 certificate persistence imply it remains zero forever.

## 4. P018-T47 — Exact strict conflict-reduction criterion

Status: `PROVED`

For `mu` finer than `lambda`, the following are equivalent:

1. `C_(mu,P)(x) < C_(lambda,P)(x)`;
2. the fine fiber removes at least one opposite-truth terminal state;
3. there exists `y` such that

\[
O_\lambda(y)=O_\lambda(x),
\qquad
P(y)\ne P(x),
\]

but

\[
O_\mu(y)\ne O_\mu(x).
\]

So a refinement is proof-informative for `x` exactly when it separates a currently compatible **counter-truth witness**.

This is stricter than the Stage-5 ambiguity-drop condition, which counts separation of any compatible state.

## 5. P018-T48 — Ambiguity gain and proof gain can disagree

Status: `PROVED BY EXPLICIT COUNTEREXAMPLE`.

Let

\[
X=\{x,t_1,t_2,t_3,f\},
\]

with predicate true on `x,t1,t2,t3` and false only on `f`.

Start from the completely coarse observation, whose fiber at `x` is all five states.

Consider two refinements.

### Refinement A — proof useful

Separate `f` from the four true states.

At `x`:

- ambiguity falls from `5` to `4`, gain `1`;
- conflict falls from `1` to `0`, gain `1`;
- the predicate is completely decided.

### Refinement B — ambiguity useful but proof useless

Separate `t1,t2,t3` into other fibers but leave `x` and `f` together.

At `x`:

- ambiguity falls from `5` to `2`, gain `3`;
- conflict remains `1`, gain `0`;
- the predicate is still UNRESOLVED.

Therefore

\[
\boxed{
\text{larger ambiguity reduction}
\not\Rightarrow
\text{larger proof progress}.
}
\]

This blocks the naive adaptive rule “always choose the precision step that shrinks the state fiber most.”

## 6. P018-T49 — Product precision cannot increase predicate conflict

Status: `PROVED`

For precision observations `O_1,...,O_m`, define the joint observation

\[
O_\times(x)
=
(O_1(x),\ldots,O_m(x)).
\]

Its fiber is the intersection

\[
[x]_\times
=
\bigcap_i[x]_i.
\]

Therefore its conflict fiber is contained in every axis conflict fiber:

\[
K_{\times,P}(x)
\subseteq
K_{i,P}(x).
\]

Hence

\[
\boxed{
C_{\times,P}(x)
\le
\min_i C_{i,P}(x).
}
\]

So combining precision axes can never make a predicate less decided.

## 7. P018-T50 — Joint predicate completeness criterion

Status: `PROVED`

A finite family of observations is **jointly predicate-complete** for `P` iff every joint observation fiber is contained entirely in one truth class of `P`.

Equivalently, there do not exist states `x,y` with opposite predicate truth values such that

\[
O_i(x)=O_i(y)
\]

for **every** available observation `i`.

Equivalently again,

\[
\boxed{
C_{\times,P}(x)=0
\quad\text{for every }x\in X.
}
\]

This is the exact finite criterion for whether the available precision axes contain enough information to decide the target predicate at all.

It can hold even when the joint observation is not state-injective.

## 8. Integer observation costs

Assign each available observation `i` a positive integer cost

\[
c_i\in\mathbb N_{>0}.
\]

The cost may encode computational effort, experimental resolution, number of factor checks, memory, energy budget, or any other finite project-specific resource.

P018 does not require converting these costs into probabilities, logarithms, or real-valued utility.

## 9. P018-T51 — Optimal target-state precision path by Bellman recurrence

Status: `PROVED FINITE RECURRENCE`.

Fix the actual terminal state `x` and a current compatible block `B` containing `x`.

Let `R` be the finite set of observations not yet used.

Define

\[
V_x(B,R)
\]

as the minimum remaining integer cost needed to make `P` constant on the compatible block containing `x`.

If `P` is already constant on `B`,

\[
\boxed{V_x(B,R)=0.}
\]

Otherwise, choosing observation `i` reveals `O_i(x)` and restricts the compatible block to

\[
B_i(x)
=
\{y\in B:O_i(y)=O_i(x)\}.
\]

Therefore

\[
\boxed{
V_x(B,R)
=
\min_{i\in R,\ B_i(x)\subsetneq B}
\left(
 c_i+V_x(B_i(x),R\setminus\{i\})
\right),
}
\]

with value undefined if no available finite sequence can decide the predicate.

Proof: every adaptive path has a first observation. After that observation, only the matching finite sub-block remains possible for the fixed terminal state. Removing the first cost reduces the problem to the same optimization on that smaller block and the remaining observations. Finite induction on `|R|` proves the recurrence. ∎

This is a genuine finite optimal-precision theorem: for small systems the best proof path can be computed exactly.

## 10. P018-T52 — Optimal worst-case finite decision tree

Status: `PROVED FINITE RECURRENCE`.

If the actual terminal state is not known in advance, an observation may produce several possible child blocks.

For a current block `B`, define

\[
V(B,R)
\]

as the minimum **worst-case** remaining integer cost required to decide `P` for every terminal state in `B`.

If `P` is constant on `B`,

\[
V(B,R)=0.
\]

Otherwise, observation `i` partitions `B` into its nonempty observation blocks

\[
\mathcal P_i(B).
\]

Then

\[
\boxed{
V(B,R)
=
\min_{i\in R}
\left[
 c_i+
 \max_{C\in\mathcal P_i(B)}
 V(C,R\setminus\{i\})
\right],
}
\]

where useless observations that do not split `B` may be omitted, and candidates with an undecidable child have infinite/undefined cost.

This is a probability-free minimax decision tree. Every quantity is finite and integer-valued.

## 11. P018-T53 — Joint completeness iff a finite decision tree exists; sum-cost upper bound

Status: `PROVED`

Suppose the available observations have positive integer costs.

If their joint observation is predicate-complete, then sequentially evaluating **all** observations necessarily decides `P` on every terminal state. Therefore a finite decision tree exists and

\[
\boxed{
V(X,R)
\le
\sum_{i\in R}c_i.
}
\]

Conversely, if the joint observation is not predicate-complete, then there are opposite-truth states `x,y` sharing every available observation value. No decision tree built only from those observations can ever separate them, so no complete finite decision tree exists.

Hence

\[
\boxed{
\text{finite decision tree exists}
\iff
\text{joint observation is predicate-complete}.
}
\]

This is the adaptive counterpart of Stage-5 predicate completeness.

## 12. P018-T54 — Greedy immediate conflict gain is not globally cost-optimal

Status: `PROVED BY EXPLICIT COUNTEREXAMPLE`.

Let

\[
X=\{x,f_1,f_2,f_3\},
\]

with predicate true only on `x`.

Available observations:

- `A`: directly separates `x` from all three false states, cost `5`;
- `B`: separates `f1,f2` but leaves `x,f3` together, cost `1`;
- `C`: separates `f3` and, when combined with `B`, completes the decision, cost `1`.

From the completely coarse state, immediate conflict reduction is largest for `A`: it removes all three opposite-truth states at once.

But the two-step adaptive path `B` then `C` costs only

\[
1+1=2<5.
\]

Thus

\[
\boxed{
\text{maximum one-step conflict gain}
\not\Rightarrow
\text{minimum total proof cost}.
}
\]

The same example gives worst-case cost `2` for the optimal finite decision tree, while the greedy direct observation costs `5`.

Therefore Stage 6 needs the Bellman recurrence of T51–T52 rather than a universal greedy rule.

## 13. What adaptive precision now means

P018 can now distinguish three optimization targets.

### State ambiguity

Reduce

\[
A_\lambda(x).
\]

This is useful when the aim is terminal-state identification.

### Predicate conflict

Reduce

\[
C_{\lambda,P}(x).
\]

This is the correct local quantity when the aim is proof of one predicate.

### Total decision cost

Minimize

\[
V_x(B,R)
\quad\text{or}\quad
V(B,R)
\]

when precision operations have different integer costs and can be chosen adaptively.

These objectives need not choose the same next precision step.

This is a major consequence of treating precision as part of mathematics rather than as a fixed numerical parameter: **the proof is allowed to choose its next precision axis.**

## 14. Relation to scale precision and factor precision

### Scale precision

A candidate refinement can split an unresolved numerical fiber. For order/threshold predicates, conflict multiplicity counts only the subcell states capable of crossing the decision boundary.

### Factor precision

A candidate factor cutoff removes terminal states whose newly visible factor witnesses are incompatible with the current survivor state. For primality, conflict multiplicity tracks the composite survivors that still look prime at the current factor horizon.

### Product precision

Scale and factor observations can be used as separate candidates in one decision tree. Their combined fiber is an intersection, so the Bellman recurrence can compare which axis is worth refining next.

This is the first formal P018 route toward proofs that **change the kind of precision**, not merely the amount of one fixed precision.

## 15. Prior-art boundary

Finite decision trees, minimax recursion, and dynamic programming are established computer-science and optimization ideas. P018 does not claim the Bellman principle or decision-tree optimization as new.

The project-specific research question is whether they become a useful mathematical proof calculus when the available actions are the finite precision observations already developed by Enterprise Math:

\[
\boxed{
\text{precision fibers}
+
\text{predicate conflict}
+
\text{persistent certificates}
+
\text{multi-axis observations}
+
\text{integer precision costs}
+
\text{exact finite optimal proof paths}.
}
\]

No probabilities, entropy scores, or infinite-precision completion are required.

Historical novelty of the integrated package remains `NOVELTY_UNVERIFIED`.

## 16. Stage-6 status

- P018-T45 conflict-zero certificate criterion: `PROVED`
- P018-T46 conflict monotonicity: `PROVED`
- P018-T47 strict conflict-reduction criterion: `PROVED`
- P018-T48 ambiguity gain != proof gain counterexample: `PROVED`
- P018-T49 product conflict bound: `PROVED`
- P018-T50 joint predicate-completeness criterion: `PROVED`
- P018-T51 optimal target-state precision recurrence: `PROVED`
- P018-T52 optimal worst-case decision-tree recurrence: `PROVED`
- P018-T53 completeness / finite-tree equivalence and cost bound: `PROVED`
- P018-T54 greedy nonoptimality counterexample: `PROVED`
- large-system complexity and approximation algorithms: `OPEN`
- adaptive P017 proof path using scale + factor + shell observations: `NEXT`
- physically weighted precision costs: `OPEN / PHYSICAL MODEL REQUIRED`

Executable checks live in `src/enterprise_math/adaptive_precision.py` and `tests/test_adaptive_precision.py`.
