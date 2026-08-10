# P025 Supplement 160 — A support level becomes optimal only after a workload cost is declared

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-state-support-stage155`

## 1. No canonical scalarization

Stage 159 gives a Pareto frontier

\[
C_t=(|A_t|,|R_t|,h-t)
\]

of executable-action count, static-state support size and remaining support-promotion horizon.

There is no canonical way to add these three different resources.  To choose one implementation level, a workload must declare how much each resource costs.

Let

\[
\alpha>0,
\qquad
\beta>0,
\qquad
\gamma>0
\]

be respectively the unit costs of

1. one executable helper action;
2. one retained helper state coordinate;
3. one unit of remaining future support-closure obligation.

Define

\[
\boxed{
\mathcal C_t
=
\alpha|A_t|
+
\beta|R_t|
+
\gamma(h-t).
}
\]

This scalar cost is a declared workload model, not an intrinsic precision invariant.

## 2. Exact local promotion threshold

For two adjacent frontier levels,

\[
\mathcal C_{t+1}-\mathcal C_t
=
\alpha\Delta A_t
+
\beta\Delta R_t
-
\gamma,
\]

where

\[
\Delta A_t=|A_{t+1}|-|A_t|,
\qquad
\Delta R_t=|R_{t+1}|-|R_t|.
\]

Therefore promoting one more dependency layer strictly reduces workload cost iff

\[
\boxed{
\gamma
>
\alpha\Delta A_t+eta\Delta R_t.
}
\]

Equality gives an exact tie.

Interpretation: one unit reduction of future closure obligation is worth buying only when its workload value exceeds the new executable-action and state-support costs.

## 3. Perfect 32-way example

The Stage159 frontier is

\[
(1,3,3),
\quad
(3,7,2),
\quad
(7,15,1),
\quad
(15,15,0).
\]

Choose

\[
\alpha=4,
\qquad
\beta=1.
\]

The adjacent promotion thresholds are

\[
\boxed{12,24,32.}
\]

Indeed:

- first promotion adds 2 actions and 4 state coordinates: cost `8+4=12`;
- second adds 4 actions and 8 state coordinates: cost `16+8=24`;
- final promotion adds 8 actions but no new state coordinates: cost `32`.

The exact workload optima include

\[
\boxed{
\begin{array}{c|c}
\gamma & \text{optimal promotion depth}\\
\hline
5 & 0\\
15 & 1\\
26 & 2\\
40 & 3
\end{array}}
\]

and at

\[
\gamma=12
\]

depths 0 and 1 tie exactly.

Thus every point of this structural frontier is genuinely optimal for some positive declared workload.

## 4. Structural theorem versus policy decision

The mathematics supplies:

- the exact Pareto frontier;
- exact marginal resource increments;
- exact switching inequalities once costs are supplied.

The mathematics does **not** supply the weights `alpha,beta,gamma`.  Those belong to the declared task/runtime/environment.

Therefore

\[
\boxed{
\text{optimal precision level}
=
\text{structural frontier}
+
\text{declared workload valuation}.
}
\]

## 5. Precision consequence

This gives a concrete reason not to encode `precision` as one globally ordered scalar.  Even on one fixed compiler and one dependency graph, different legitimate workloads choose different support layers.

A future architecture should therefore preserve the resource vector until the task supplies a valuation, rather than collapsing it prematurely.

## 6. Prior-art boundary

Weighted scalarization of Pareto fronts and marginal-cost switching are classical optimization ideas. No generic novelty claim is made. P025 contributes the exact support-promotion specialization and the explicit separation between mathematical structure and workload policy.
