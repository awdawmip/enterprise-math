# P025 Supplement 155 — Static state support and executable action support are different repairs

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-state-support-stage155`

## 1. Two ways to repair a nonclosed action family

Stage 152 showed that an arbitrary visible helper-action set

\[
Q\subseteq P_{gate}
\]

may depend on hidden predecessors. Stage 153 repaired this by enlarging the **executable action subsystem** to the predecessor-closed support `down(Q)`.

That is not the only possible future contract.

Assume instead:

- all raw antecedents are fixed during the helper-only phase;
- only actions in the original set `Q` may fire;
- hidden helper statuses outside `Q` are static unless the corresponding helper itself belongs to `Q`.

Then hidden dependencies can be retained as state inputs without becoming executable actions.

## 2. Exact Q-only state support

Let `Pred(q)` denote the direct helper predecessors of action `q` in the compiler DAG. Define

\[
\boxed{
R_Q
=
Q\cup\bigcup_{q\in Q}\operatorname{Pred}(q).
}
\]

For global ideal `I`, a declared action `q` is enabled exactly when

\[
q\notin I
\quad\text{and}\quad
\operatorname{Pred}(q)\subseteq I.
\]

Every coordinate in this test lies in `R_Q`. Therefore current legality of every `q in Q` depends only on

\[
I\cap R_Q.
\]

When `q` fires, the only changed helper coordinate is `q` itself, which also lies in `R_Q`. Hidden predecessor statuses outside `Q` remain fixed by the declared operation language.

Hence every finite Q-only action word, including prefix legality and projected results, factors through

\[
\boxed{I\mapsto I\cap R_Q.}
\]

One-step factorization suffices by induction because all state changes under the declared word remain inside `Q subseteq R_Q`.

## 3. Direct hidden predecessors are genuinely needed

For the balanced helper tree, each hidden direct predecessor of a declared action can independently change that action's enabledness on suitable legal ideals while all other coordinates of `R_Q` remain fixed.

Therefore the direct predecessor coordinates are not merely a convenient sufficient set; they have exact finite necessity witnesses within the label-projection representation used here.

## 4. Static state support can be far smaller than action closure

For a perfect `k=2^d` compiler, choose one highest pre-output helper action.

Its autonomous executable action closure from Stage154 contains the entire helper subtree:

\[
|\downarrow\{q\}|
=
\frac{k}{2}-1.
\]

But the Q-only static state support contains only

- the action `q`;
- its two direct helper predecessors.

Thus for `k>=8`,

\[
\boxed{
|R_{\{q\}}|=3,
\qquad
|\downarrow\{q\}|=\frac{k}{2}-1.
}
\]

Examples:

\[
\begin{array}{c|c|c}
k & \text{Q-only state support} & \text{autonomous action support}\\
\hline
8 & 3 & 3\\
16 & 3 & 7\\
32 & 3 & 15
\end{array}
\]

For two top actions in the perfect 16-way compiler, static support has six helper coordinates while the autonomous executable support contains all fourteen pre-output helpers.

## 5. Architectural consequence

A hidden dependency can be repaired in at least two inequivalent ways:

1. **state repair** — expose/store prerequisite status while keeping it operationally frozen;
2. **action repair** — include prerequisite actions and recursively close the executable subsystem.

Therefore

\[
\boxed{
\text{required state support}
\neq
\text{required action support}.
}
\]

Which repair is correct depends on the future operation envelope, not only on the dependency graph.

## 6. Boundary for the next stage

The small support `R_Q` is sufficient only because non-Q helper statuses are static. If the environment may asynchronously update hidden predecessors, this contract changes. Stage 156 should test whether interference forces the support back toward `down(Q)`.

## 7. Prior-art boundary

Static inputs versus executable subsystem closure is standard systems/modular-verification reasoning. No generic novelty claim is made. P025 contributes the exact helper-tree separation and precision-accounting boundary.
