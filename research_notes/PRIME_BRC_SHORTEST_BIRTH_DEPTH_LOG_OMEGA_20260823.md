# Prime-BRC Sharp Shortest Birth Depth in Factor Count

Status: `L3 OWNER-LOCAL / PROVED ELEMENTARY THEOREM / NOT LEGENDRE`
Date: `2026-08-23`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

Depends on the floor-birth tree

\[
\mathsf B(n)=\{d:d|n,\sqrt n\le d<n\}.
\]

Let `delta(n)` be the minimum number of birth edges from `n` to a prime leaf.

## 1. Factor-count balanced child

Let

\[
n=p_1p_2\cdots p_m,
\qquad p_1\le p_2\le\cdots\le p_m,
\]

with multiplicity retained, so `m=Omega(n)`.

Put

\[
t=\left\lceil\frac m2\right\rceil
\]

and define the product of the largest `t` factors

\[
d=p_{m-t+1}\cdots p_m.
\]

Let

\[
a=n/d=p_1\cdots p_{m-t}.
\]

Pair every factor occurring in `a` with a factor occurring in the upper block `d`. Since the factors are ordered, each paired factor in `d` is at least the corresponding factor in `a`; if `m` is odd, `d` has one additional factor. Hence

\[
\boxed{d\ge a.}
\]

Since `n=ad`,

\[
\boxed{d\ge\sqrt n.}
\]

For `m>=2`, `d<n`, so `d` is a proper birth child. By construction

\[
\boxed{
\Omega(d)=\left\lceil\frac{\Omega(n)}2\right\rceil.
}
\]

Thus every composite node has a child that cuts total prime-factor depth by at least half.

## 2. Sharp logarithmic shortest-depth bound

The recurrence gives

\[
\delta(n)
\le
1+
\max_{\Omega(d)\le\lceil m/2\rceil}\delta(d).
\]

Iterating the factor-count halving yields

\[
\boxed{
\delta(n)\le\lceil\log_2\Omega(n)\rceil.
}
\]

This is stronger than the coarse `O(log log n)` numerical-depth corollary when factor count is known.

Since

\[
\Omega(n)\le\log_2 n,
\]

it independently implies

\[
\delta(n)=O(\log\log n).
\]

## 3. Exact sharpness on prime powers

Let

\[
n=p^m.
\]

Every proper birth child is `p^j` with

\[
2j\ge m,
\qquad j<m.
\]

Thus every first step satisfies

\[
j\ge\left\lceil\frac m2\right\rceil.
\]

Choosing `j=ceil(m/2)` is legal and optimal. Therefore

\[
\delta(p^m)
=1+\delta\!\left(p^{\lceil m/2\rceil}\right).
\]

With `delta(p)=0`, this recurrence solves exactly to

\[
\boxed{
\delta(p^m)=\lceil\log_2 m\rceil.
}
\]

Hence the universal factor-count bound is sharp for every factor depth `m` via prime powers.

## 4. Three distinct BRC depths on the same birth DAG

The same arithmetic birth DAG carries different task-dependent paths.

### Provenance-maximal path

Repeatedly choose the maximum child

\[
n/\operatorname{spf}(n).
\]

This removes one prime factor per step and has length

\[
\boxed{\Omega(n)-1.}
\]

### Factor-count-minimal guaranteed path

Choose a child built from the largest half of the prime factors. This guarantees

\[
\boxed{\delta(n)\le\lceil\log_2\Omega(n)\rceil.}
\]

### Numerically balanced path

The independent two-thirds theorem gives at each nonterminal stage either an immediate prime child or a child of size at most

\[
n^{2/3},
\]

producing a numerical `O(log log n)` scale descent with sharp one-step exponent `2/3`.

These are not contradictory notions of depth; they optimize different objectives on the same branch structure.

## 5. BRC interpretation

This supplies an exact example where branching is mathematically useful even though no information is invented:

```text
same exact birth support
-> choose max child for provenance
-> choose balanced factor-count child for shallow factor depth
-> choose balanced numeric child for fast scale contraction.
```

A deterministic quotient that preselects only the max-child path would hide the existence of the shorter valid routes. The branch carrier preserves them until the downstream objective chooses which path is relevant.

## 6. Boundary

This is a structural/existential theorem. Constructing the balanced child without divisor information is a separate algorithmic question; no factoring-speed claim is made.

Freeze:

`BIRTH_TREE_SHORTEST_PRIME_LEAF_DEPTH_LE_CEIL_LOG2_OMEGA = true`.

`PRIME_POWERS_ATTAIN_THE_BOUND_EXACTLY = true`.

`BRC_SUPPORTS_DISTINCT_PROVENANCE_AND_COMPLEXITY_OPTIMAL_PATHS = true`.
