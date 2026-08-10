# P025 Supplement 159 — State repair versus action promotion forms a Pareto frontier

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-state-support-stage155`

## 1. Support-growth layers

Let

\[
Q^{(0)}\subsetneq Q^{(1)}\subsetneq\cdots\subsetneq Q^{(h)}=\downarrow Q
\]

be the strict predecessor-expansion layers from Stage156, where `h` is the Stage157 support horizon.

Choose a promotion depth `t`.

- Actions in `Q^(t)` are executable.
- Helpers outside `Q^(t)` are not executable by this subsystem.
- To interpret the `Q^(t)` actions while the next hidden layer stays static, Stage155 requires state support `Q^(t+1)` when `t<h`.
- At `t=h`, the action family is predecessor-closed, so state and action support coincide.

Thus define

\[
A_t=Q^{(t)}
\]

and

\[
R_t=
\begin{cases}
Q^{(t+1)},&t<h,\\
Q^{(h)},&t=h.
\end{cases}
\]

## 2. Three-resource cost vector

Each promotion depth has the structural cost

\[
\boxed{
C_t=
\left(
|A_t|,
|R_t|,
h-t
\right).
}
\]

The coordinates mean:

1. number of executable helper actions included in the subsystem;
2. number of helper state coordinates that must be retained to interpret those actions;
3. number of additional predecessor-promotion rounds still required to reach a fully autonomous closed action subsystem.

## 3. Every strict layer is nondominated

As `t` increases:

- `|A_t|` strictly increases along a strict support-growth layer;
- `|R_t|` is nondecreasing and typically increases;
- the remaining horizon `h-t` strictly decreases.

Therefore moving deeper in the promotion chain buys less future closure obligation only by paying more executable-action and state-support resources.

No point can dominate another simultaneously in all three minimization coordinates:

\[
\boxed{
\{C_0,\ldots,C_h\}
\text{ is a Pareto frontier.}
}
\]

No scalar `best support level` exists without an external workload/cost criterion.

## 4. Perfect binary exact frontiers

For one highest pre-output action:

### Eight-way compiler

\[
\boxed{(1,3,1),\ (3,3,0).}
\]

### Sixteen-way compiler

\[
\boxed{(1,3,2),\ (3,7,1),\ (7,7,0).}
\]

### Thirty-two-way compiler

\[
\boxed{
(1,3,3),\ (3,7,2),\ (7,15,1),\ (15,15,0).
}
\]

The first point keeps a tiny executable action language but leaves more closure obligation. The last point pays the full autonomous dependency support and has zero remaining horizon.

## 5. Precision interpretation

The same dependency system therefore supports a continuum of legal implementation/future contracts:

- **state-heavy / action-light** — hidden prerequisite status is stored but not executable;
- **mixed** — some prerequisite layers are executable, deeper layers remain static state;
- **fully autonomous** — all dependency actions are included and support is closed.

These are not merely different encodings of the same operation language: they declare different future freedoms.

## 6. Relation to earlier Pareto results

Stages 94–95 showed that semantically equivalent coordinate charts can be incomparable under storage/update costs. Stage159 is different: here the **future operation envelope itself** changes along the frontier, while raw declared intent can still be viewed as originating from the same top action.

Thus action freedom and support precision are coupled Pareto resources.

## 7. Prior-art boundary

Multiobjective/Pareto optimization and dependency-layer promotion are classical. No generic novelty claim is made. P025 contributes the exact support-promotion specialization and its future-relative precision interpretation.
