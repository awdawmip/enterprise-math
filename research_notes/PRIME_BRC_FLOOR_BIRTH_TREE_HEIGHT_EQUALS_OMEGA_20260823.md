# Prime-BRC Floor-Birth Tree Height = Omega - 1

Status: `L3 OWNER-LOCAL / PROVED ELEMENTARY THEOREM / NOT LEGENDRE`
Date: `2026-08-23`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

Depends on:

- `PRIME_BRC_FLOOR_QUOTIENT_BRANCH_BIRTH_MULTIPLICITY_20260823.md`;
- `PRIME_BRC_FLOOR_BIRTH_TREE_LEAST_FACTOR_DESCENT_20260823.md`.

## 1. Birth tree

For every integer `n>=2`, define its proper floor-birth children by

\[
\mathsf B(n)=
\{d:d|n,\ \sqrt n\le d<n\}.
\]

Equivalently,

\[
\mathsf B(n)=
(\mathcal F(n)\setminus\mathcal F(n-1))\setminus\{n\}.
\]

Create a rooted directed tree/finite DAG by placing edges

\[
n\to d
\qquad(d\in\mathsf B(n))
\]

and repeating at every child.

Let `h(n)` be the maximum number of edges on a path from `n` to a leaf. Prime nodes have no proper birth child, hence height `0`.

## 2. Main theorem

For every integer `n>=2`,

\[
\boxed{h(n)=\Omega(n)-1,}
\]

where `Omega(n)` is the total number of prime factors with multiplicity.

### Proof

Proceed by induction on `Omega(n)`.

If `Omega(n)=1`, then `n` is prime, `B(n)=empty`, and `h(n)=0`.

Now let `Omega(n)=m>=2`. Every proper divisor `d|n` satisfies

\[
\Omega(d)\le m-1.
\]

Thus every birth child has, by induction,

\[
h(d)=\Omega(d)-1\le m-2.
\]

Hence

\[
h(n)\le1+(m-2)=m-1.
\]

On the other hand, if `p=spf(n)`, the canonical maximum birth child is

\[
d_*=n/p.
\]

It has

\[
\Omega(d_*)=m-1,
\]

so by induction

\[
h(d_*)=m-2.
\]

Therefore the path through the max child has length

\[
1+h(d_*)=m-1,
\]

which attains the upper bound. ∎

## 3. Exact P_j hierarchy

For every fixed `j>=1`,

\[
\boxed{
\Omega(n)\le j
\iff
h(n)\le j-1.
}
\]

Thus the classical almost-prime hierarchy becomes an intrinsic floor-branch depth hierarchy:

\[
\boxed{
P_1\leftrightarrow h=0,
\qquad
P_2\leftrightarrow h\le1,
\qquad
P_3\leftrightarrow h\le2,
\quad\ldots
}
\]

Repeated prime factors require no separate definition: they increase birth-tree height automatically.

## 4. Relation to max-child descent

The maximum-child path

\[
n\to n/\operatorname{spf}(n)\to\cdots
\]

has maximal possible depth in the birth tree and realizes the full height exactly.

Therefore the P017 least-factor recursion is not merely one convenient path. It is a **height-realizing geodesic** in the intrinsic floor-birth tree.

## 5. Relation to adaptive Prime-BRC P2 credits

The adaptive pair/repeat P2 detector can now be interpreted as a cheap local surrogate for the event

\[
h(n)\ge2.
\]

- distinct pair interactions detect multiple independent first-layer branches;
- repeat events detect hidden depth when current branch count alone is ambiguous (e.g. `pq` versus `p^3` birth multiplicity);
- the exact tree theorem shows why these corrections target `Omega>=3` and leave `P2` states unpenalized.

## 6. Campbell / switching interpretation

A square-interval P3 theorem says that some basin state has

\[
h(n)\le2.
\]

The P3 -> P2 problem is therefore exactly a one-level height reduction:

\[
\boxed{
\exists h\le2
\quad\Longrightarrow?\quad
\exists h\le1.
}
\]

The owner-local balanced/outer switching constructions identify explicit arithmetic certificates for height-2 states and reindex them into lower-complexity factor windows.

## 7. Boundary

This theorem is an exact semantic re-expression of factor depth, not a new bound on the distribution of almost primes. It does not by itself force a height-zero node in every square basin.

Freeze:

`FLOOR_BIRTH_TREE_HEIGHT_EQUALS_TOTAL_PRIME_FACTOR_COUNT_MINUS_ONE = true`.

`P_j_EQUALS_BIRTH_HEIGHT_AT_MOST_j_MINUS_ONE = true`.

`P017_MAX_BIRTH_DESCENT_REALIZES_TREE_HEIGHT = true`.
