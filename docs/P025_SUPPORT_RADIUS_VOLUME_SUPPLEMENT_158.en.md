# P025 Supplement 158 — Dependency-support radius and volume are independent resources

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-state-support-stage155`

## 1. Setup

Consider one declared helper action `q` in an acyclic helper dependency graph where every helper gate has at most two helper predecessors.

Let

\[
h=H_{supp}(\{q\})
\]

be the Stage157 reverse dependency horizon, and let

\[
V=|\downarrow q|
\]

be the number of helper coordinates in its full dependency support.

The same radius `h` can correspond to very different support volumes.

## 2. Universal lower bound

By definition of horizon `h`, some helper lies at reverse dependency distance exactly `h` from `q`.  A shortest path from that helper to `q` contains

\[
h+1
\]

distinct helper vertices.

Therefore

\[
\boxed{V\ge h+1.}
\]

A sequential helper chain attains equality.

## 3. Binary-fan-in upper bound

At reverse distance zero there is one action `q`.  Because every helper has at most two helper predecessors, the reverse shell at distance `t` contains at most

\[
2^t
\]

helpers.

Hence

\[
V
\le
\sum_{t=0}^{h}2^t
=
2^{h+1}-1.
\]

Thus

\[
\boxed{
h+1
\le
V
\le
2^{h+1}-1.
}
\]

A perfect binary helper subtree attains the upper bound.

## 4. Both bounds are sharp for every horizon

For any `h>=0`:

### Lower extreme

Use a sequential helper chain with top helper at reverse distance horizon `h`. Its support contains exactly the `h+1` helpers on the chain:

\[
\boxed{V_{chain}=h+1.}
\]

### Upper extreme

Use the highest helper of a perfect balanced compiler with

\[
k=2^{h+2}
\]

raw antecedents. Its support is a perfect helper tree with shells `1,2,...,2^h`, so

\[
\boxed{V_{tree}=2^{h+1}-1.}
\]

The radius is the same in both examples.

## 5. Exact separation example

At

\[
h=4,
\]

the chain support has

\[
V=5,
\]

whereas the perfect binary support has

\[
V=31.
\]

As `h` grows, the ratio between the two sharp extremes is exponential up to the linear denominator.

## 6. Precision consequence

A relation/support horizon measures **how many dependency layers** must be traversed.  Support volume measures **how many labelled coordinates** live inside those layers.

They therefore describe different resources:

\[
\boxed{
\text{support radius}
\neq
\text{support volume}.
}
\]

Any precision cost model that keeps only dependency depth can underestimate branching support dramatically.

## 7. Prior-art boundary

Tree branching bounds and radius/volume growth are classical graph/combinatorial facts. No generic novelty claim is made. P025 contributes their exact interpretation as separate future-operation support resources.
