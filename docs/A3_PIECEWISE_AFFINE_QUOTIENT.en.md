# A3 Piecewise Affine Quotient — Hidden-Guard Erasure and Non-Monotone Refinement

Status: `RESEARCH WIP / EXACT BINARY THRESHOLD CRITERION PROVED + EXECUTABLE REFERENCE`

## 1. Problem

A3 already has exact partition criteria for integer linear/affine dynamics

\[
c'=Bc+u
\]

and observation-aware minimum exact partitions for linear observations.

Now consider a genuinely hidden-relation-sensitive binary piecewise map:

\[
T(c)=
\begin{cases}
B_+c+u_+,&w^Tc+b\ge0,\\
B_-c+u_-,&w^Tc+b<0.
\end{cases}
\]

The state space is the full integer lattice `Z^k`. A partition matrix `A:k->ell` observes only block sums `Ac`.

The question is:

> If branch identity itself is not readable from the coarse state, can it still be safely erased?

Yes, exactly when both branches induce the same coarse effect.

## 2. When the guard descends

Let

\[
K_A=\ker_{\mathbb Z}A.
\]

The linear guard score `w^Tc+b` is exactly readable from `Ac` iff

\[
w^T\eta=0\quad\forall\eta\in K_A.
\]

For a coordinate partition this is equivalent to `w` being constant inside every coarse block.

If this fails, some `eta in K_A` has `w^T eta != 0`. Since every integer multiple `t eta` remains in the same coarse fiber, the guard score is unbounded in both directions along that fiber. Therefore

\[
\boxed{\text{every coarse fiber contains both true-branch and false-branch states}.}
\]

This is the key strengthening supplied by the full-integer-lattice domain.

## 3. A3-PW01 — Exact criterion when the guard is visible

If

\[
w^T=\bar w^TA,
\]

branch choice is a coarse-state function.

### Nonconstant guard

If `bar w != 0`, both guard outcomes occur somewhere on `Z^ell`. The piecewise program descends exactly iff both active affine branches descend:

\[
AB_+=\bar B_+A,
\qquad
AB_-=\bar B_-A.
\]

Offsets aggregate normally:

\[
\bar u_+=Au_+,
\qquad
\bar u_-=Au_-.
\]

The coarse program keeps the threshold guard.

### Constant guard

If `bar w=0`, the guard is globally determined by `b`. Only the active branch must descend. The inactive branch may read hidden detail because it is never executed.

## 4. A3-PW02 — Hidden-Guard Erasure Theorem

If the guard does **not** descend, every coarse fiber contains both branch outcomes.

Therefore exact descent requires:

1. each branch to be insensitive to the kernel, hence each branch descends;
2. the descended affine maps to be identical:

\[
\boxed{
\bar B_+=\bar B_-=ar B,
\qquad
Au_+=Au_-=\bar u.
}
\]

Then, regardless of which hidden branch executes,

\[
AT(c)=\bar B(Ac)+\bar u.
\]

Conversely, if the two coarse branch effects differ, the same coarse fiber contains fine states taking both branches and therefore produces two different coarse outputs. The quotient is not exact.

Hence on the full integer lattice:

\[
\boxed{
\text{hidden guard exact}
\iff
\text{both branches descend and have identical coarse affine effect}.
}
\]

This resolves the open case left by the earlier observation-aware work: hidden branch identity may be erased when coarse output is identical.

## 5. Branch identity is not automatically required state

The theorem says that the need to retain branch identity is controlled by its effect on future coarse output, not by whether the fine program internally followed different branches.

Thus

\[
\boxed{
\text{different fine histories}
\not\Rightarrow
\text{different required coarse states}.
}
\]

This is exactly the A3 future-safe-collapse principle: preserve only relation detail that the declared future language can actually distinguish.

## 6. A3-PW03 — Exactness is not monotone under refinement

The linear-dynamics solver works by monotone partition refinement. Piecewise maps do not inherit that property automatically.

There is a 3-coordinate example with:

- coarse partition `{{0,1,2}}`: the guard is hidden, but both branches have zero total coarse effect, so the quotient is exact;
- intermediate partition `{{0},{1,2}}`: the guard is still hidden, but the branch effects are now distinguishable, so the quotient is **not exact**;
- singleton partition: the guard becomes visible and exactness returns.

Therefore

\[
\boxed{
P_0\text{ exact},\quad P_1\succ P_0\text{ not exact},\quad P_2\succ P_1\text{ exact}.
}
\]

So

\[
\boxed{\text{piecewise quotient exactness need not be monotone under refinement}.}
\]

The linear signature-splitting algorithm cannot simply be reused as a general piecewise minimum solver.

## 7. Relationship to A2/P023

General future-compatible quotient / behavioral-equivalence mother theorems remain owned by A2/P023.

This note is an A3 `SPECIALIZATION`: the coordinate partition kernel plus the full integer lattice give a closed exact criterion for binary linear-threshold affine programs.

Reusable consequences are:

- a hidden linear guard realizes both outcomes inside every coarse fiber;
- coarse-output equality can erase branch identity completely;
- exact partitions for piecewise programs can fail refinement monotonicity.

These results should be relayed to A2/P023 rather than duplicated as a second general theory.

## 8. Implementation

Added:

- `src/enterprise_math/piecewise_relation_quotient.py`;
- `tests/test_piecewise_relation_quotient.py`.

Tests cover hidden-guard erasure, failure with different coarse effects, visible guards with different branches, globally constant guards, and the exact → non-exact → exact refinement counterexample.

## 9. Next

Do not jump directly to arbitrary nonlinear programs. The next focused tasks are:

1. determine whether binary-threshold exact partitions can have multiple incomparable maximal/coarsest candidates;
2. build a small-`k` partition-lattice oracle for the exact criterion;
3. seek structural decomposition stronger than exhaustive partition search;
4. relay output-equivalence consequences to P023/A2;
5. construct an A3 weighted-relation hidden-feedback example where output-equivalence requires less precision than a branch-identity-sensitive solver.
