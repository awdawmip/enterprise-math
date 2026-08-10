# P025 Supplement 150 — Completing trace count is the linear-extension count

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-fairness-stage147`

## 1. From fairness to complete firing words

Stage 149 identifies weakly fair executions with eventually completing executions for the finite monotone helper system.  Ignore terminal stuttering after completion and record only the finite labelled helper firing word.

A complete firing word must respect every helper dependency, and any total ordering respecting those dependencies is a legal complete firing word. Therefore

\[
\boxed{
\{\text{complete helper firing words}\}
=
\{\text{linear extensions of }P_{gate}\}.
}
\]

Thus full fair/completing trace precision is an order-extension problem.

## 2. Perfect binary tree recurrence

Let `T_h` be the helper/gate dependency poset of a perfect binary gate tree of height `h`, including its root. It has

\[
n_h=2^h-1
\]

internal gates. Let `L_h` be its number of linear extensions.

For `h=1`, there is one gate:

\[
\boxed{L_1=1.}
\]

For `h>=2`, the root must be last. Before it, one chooses a linear extension of each child subtree and interleaves the two words while preserving their internal orders. Each child has `n_(h-1)` gates. Therefore

\[
\boxed{
L_h
=
\binom{2n_{h-1}}{n_{h-1}}
L_{h-1}^2.
}
\]

## 3. Full pre-output helper schedules

For the perfect `k=2^d` conjunction compiler, before output `z` fires the helper poset is the disjoint union of the two height-`d-1` child gate trees of `z`.

The number of complete helper firing words is therefore exactly the same interleaving expression as `L_d`:

\[
\boxed{
N_{trace}(2^d)=L_d.
}
\]

Exact values begin

\[
\boxed{
N_{trace}(4)=2,
\quad
N_{trace}(8)=80,
\quad
N_{trace}(16)=21{,}964{,}800.
}
\]

## 4. Endpoint, state, and trace are different resources

Compare three quantities for the same perfect compiler:

\[
\begin{array}{c|c|c|c}
k & \text{endpoint classes} & \text{async progress states} & \text{complete labelled traces}\\
\hline
4 & 1 & 4 & 2\\
8 & 1 & 25 & 80\\
16 & 1 & 676 & 21{,}964{,}800
\end{array}
\]

The counts are not ordered by a single notion of `precision`: endpoint classes quotient state heavily, progress states record current configuration, and trace words record the entire legal ordering history.

In particular, a relatively modest finite state space can support vastly more complete histories.

## 5. Operation-word precision returns

Stages 105–106 separated endpoint word quotients from trace word quotients in the dyadic threshold setting. The same distinction reappears here in concurrency form:

- endpoint future forgets all firing order;
- progress state remembers only the current ideal;
- trace future remembers which linear extension path produced completion.

Thus scheduler history is an operation-word precision resource, not automatically a state-coordinate requirement.

## 6. Prior-art boundary

Linear extensions of posets and interleaving counts of independent subtrees are classical enumerative order theory. No generic novelty claim is made. P025 contributes the exact helper-compiler specialization and the endpoint/state/trace precision separation.
