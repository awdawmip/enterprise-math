# P025 Supplement 137 — Optimal binary-helper compilation of a pure k-way conjunction

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-closure-basis-stage130`

## 1. Problem

Stage 136 showed that the pure raw law

\[
a_1\wedge\cdots\wedge a_k\Rightarrow z
\]

cannot reduce its premise arity below `k` on the fixed raw alphabet, while auxiliary labels allow a binary compilation. Stage 135 used a sequential helper chain of depth `k-1`; that depth is not optimal.

We now allow sound positive single-head rules of maximum premise arity two, fresh helper labels, and a distinguished output `z`. The compiler must preserve the pure raw closure for every raw-only initial seed.

## 2. Helper lower bound

Consider a derivation of `z` from the full raw seed `A={a_1,...,a_k}`. Because the compiler is sound for the pure conjunction, every raw antecedent is necessary: if some `a_i` had no dependency path to `z`, the same derivation would survive after deleting `a_i`, contradicting the raw semantics.

Take the ancestor DAG of one successful derivation of `z`. It has

- `k` necessary raw source vertices;
- `m` derived/gate vertices, one of which is `z`;
- indegree at most two at every derived vertex.

The underlying ancestor graph is connected, so it has at least

\[
k+m-1
\]

edges. But the indegree bound gives at most `2m` edges into derived vertices. Hence

\[
2m\ge k+m-1,
\]

so

\[
\boxed{m\ge k-1.}
\]

Since one derived vertex is `z`, at least

\[
\boxed{k-2}
\]

auxiliary helper labels are required.

## 3. Depth lower bound

At parallel derivation depth zero, each available raw label depends on one raw source. Under binary rules, one derived label created at depth `t` can depend on at most

\[
2^t
\]

raw sources.

Because soundness requires `z` to depend on all `k` antecedents,

\[
2^d\ge k.
\]

Therefore

\[
\boxed{d\ge\lceil\log_2k\rceil.}
\]

## 4. Balanced construction

Pair the currently live signals as evenly as possible in each parallel round. Each pair produces one fresh helper, with at most one unpaired signal carried forward. Continue until two live signals remain, then combine them directly into `z`.

Every pairing reduces the number of live signals by one. Reducing `k` raw signals to one output therefore uses exactly

\[
\boxed{k-1}
\]

binary rules/gates, of which

\[
\boxed{k-2}
\]

are helpers and the final gate is `z`.

Maximal parallel pairing gives depth exactly

\[
\boxed{\lceil\log_2k\rceil.}
\]

The executable compiler verifies that forward chaining from every raw-only seed, followed by projection to the raw alphabet, equals the pure k-way closure.

## 5. Exact optimum

Within this positive binary-helper compiler model, the balanced construction simultaneously attains both lower bounds:

\[
\boxed{
(\max\text{ premise arity},\#\text{helpers},\#\text{rules},d)
=
\left(2,k-2,k-1,\lceil\log_2k\rceil\right).
}
\]

Thus the sequential Stage-135 compiler was correct but depth-suboptimal; balancing improves depth from `k-1` to logarithmic while using the same minimum helper count and rule count.

## 6. Architectural consequence

Once auxiliary state is admitted, relation-law compilation itself has an optimization problem over several independent resources. Even fixing premise arity two does not determine execution depth; internal topology matters.

The raw semantic closure is therefore insufficient to specify implementation precision. One must also declare at least:

- allowed auxiliary-state dimension;
- rule fan-in / premise arity;
- rule count/storage;
- parallel derivation depth.

## 7. Prior-art boundary

Fan-in-two circuit size/depth lower bounds and balanced AND trees are classical circuit theory. No generic novelty claim is made. The project-side value is the exact placement of these classical resources inside future-relative relation-law precision accounting.
