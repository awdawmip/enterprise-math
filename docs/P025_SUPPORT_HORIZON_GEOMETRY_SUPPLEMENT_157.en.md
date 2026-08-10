# P025 Supplement 157 — Operation-support growth is reverse dependency-ball geometry

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-state-support-stage155`

## 1. Predecessor expansion as metric growth

Stage 156 defines

\[
Q^{(0)}=Q,
\qquad
Q^{(t+1)}=Q^{(t)}\cup\operatorname{Pred}(Q^{(t)}).
\]

This is exactly breadth-first growth in the dependency graph with edges followed backward from consumer action to prerequisite helper.

For helper `x in down(Q)`, define the reverse dependency distance

\[
d_Q(x)
=
\min\{\text{number of helper-dependency edges from }x\text{ forward to some }q\in Q\}.
\]

Then

\[
\boxed{
Q^{(t)}
=
\{x\in\downarrow Q:d_Q(x)\le t\}.
}
\]

Thus the Stage156 support-growth layers are exact closed balls for this directed dependency distance.

## 2. Exact support horizon

Define

\[
H_{supp}(Q)
=
\min\{t:Q^{(t)}=\downarrow Q\}.
\]

By the ball identity,

\[
\boxed{
H_{supp}(Q)
=
\max_{x\in\downarrow Q}d_Q(x).
}
\]

So the number of operation-promotion rounds required to expose all dependency support is a reverse eccentricity of the declared action set.

## 3. Perfect balanced family

For perfect `k=2^d` compiler and one highest pre-output helper action, the dependency subtree has helper height

\[
d-1.
\]

The action itself is distance zero, the first hidden helper layer distance one, and the bottom helper layer distance `d-2`. Therefore

\[
\boxed{
H_{supp}=d-2=\log_2k-2.
}
\]

The reverse shells have sizes

\[
1,2,4,\ldots,2^{d-2},
\]

and the balls are

\[
\boxed{
|Q^{(t)}|=2^{t+1}-1,
\qquad
0\le t\le d-2.
}
\]

This reproduces Stage156's exact sequences `1->3`, `1->3->7`, `1->3->7->15`, ...

## 4. Two equivalent semantics

The same integer `H_supp` has two interpretations:

1. **operation-language horizon** — how many times one can promote the currently exposed prerequisite state into executable actions before support closes;
2. **relation-geometry horizon** — maximum reverse dependency distance from the declared action set to its hidden helper support.

Hence a future-language closure process can be represented as finite relation geometry.

## 5. Boundary

Horizon/depth is not the same as support cardinality. Branching can make one additional dependency layer expose many new helper coordinates. Stage 158 should separate support radius from support volume.

## 6. Prior-art boundary

Breadth-first search, graph distance, eccentricity and dependency DAG depth are classical. No generic novelty claim is made. P025 contributes the exact equivalence between future-operation support promotion and dependency-ball geometry inside the current precision architecture.
