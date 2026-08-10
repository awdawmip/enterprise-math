# P025 Supplement 52 — Catalan Boundary for Simultaneously Low-Capacity Unit Blocks

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-certificate-index-stage34`  
Depends on: P025 Supplement 51  
External prior art: Mihailescu's theorem on Catalan's conjecture  
Hard block: `NONE`

## 1. Pasten's exceptional unit-prime family

Pasten's Small Derivatives Conjecture excludes, up to order, triples of the form

\[
(1,N,q)
\]

with `q` prime.

Thus in a **nonexceptional** unit relation

\[
1+b=c,
\]

neither nonunit entry may be prime.

This external exception convention is inherited exactly; P025 does not change it.

## 2. P025-T121 — capacity below five forces a proper prime power in the nonexceptional unit slice

Supplement 51 proves

\[
C(n)<5
\Longrightarrow
n=p^e,
\qquad
C(n)=e.
\]

For a nonexceptional unit triple, `e=1` would make one nonunit entry prime and therefore fall into Pasten's excluded family.

Hence

\[
\boxed{
C(n)<5
\quad\text{on a nonexceptional unit side}
\Longrightarrow
n=p^e,
\qquad
2\le e\le4.
}
\]

So simultaneously very low capacity forces both consecutive integers to be proper perfect powers.

## 3. P025-T122 — the only simultaneously sub-five nonexceptional unit point is `8,9`

Assume

\[
1+b=c
\]

is Pasten-nonexceptional and

\[
C(b)<5,
\qquad
C(c)<5.
\]

By P025-T121,

\[
b=x^u,
\qquad
c=y^v
\]

with

\[
x,y>1,
\qquad
u,v>1.
\]

Mihailescu's theorem (Catalan's conjecture) states that the only positive consecutive proper perfect powers are

\[
\boxed{8=2^3,
\qquad
9=3^2.}
\]

Therefore

\[
\boxed{
(b,c)=(8,9).
}
\]

Indeed

\[
C(8)=3,
\qquad
C(9)=2.
\]

This theorem belongs entirely to external prior art after the project-specific capacity reduction.

## 4. General fixed-capacity consequence

Fix an integer horizon `H`.

Supplement 51 says every integer with

\[
C(n)\le H
\]

is either:

- a prime power `p^e` with `1<=e<=H`; or
- one of finitely many non-prime-power integers dividing the finite universe
  \[
  Q_H=\prod_{p\le H}p^H.
  \]

Consider nonexceptional unit triples with

\[
C(b)\le H,
\qquad
C(c)\le H.
\]

If either side belongs to the finite non-prime-power core, only finitely many consecutive pairs occur.

Outside that finite core, both sides are prime powers. Nonexceptionality removes exponent-one prime sides, and Mihailescu's theorem leaves only `8,9`.

Hence:

\[
\boxed{
\text{for every fixed }H,
\text{ there are only finitely many Pasten-nonexceptional unit triples with }
C(b),C(c)\le H.
}
\]

This is a genuine finiteness statement obtained by composing an elementary P025 reduction with a deep external theorem.

## 5. What this does and does not remove

The theorem eliminates the branch where **both** consecutive blocks remain at uniformly bounded derivative capacity.

It does **not** eliminate the more important asymmetric hard branch:

\[
\boxed{
C(b)\text{ small},\qquad
C(c)\to\infty,\qquad
m(c)/C(b)\text{ large},
}
\]

or its symmetric counterpart.

The working example

\[
1+239^2=2\cdot13^4
\]

has

\[
C(239^2)=2,
\qquad
C(2\cdot13^4)=21,
\]

and therefore lies exactly in this surviving asymmetric branch.

So Catalan does not solve unit PCC. It removes the misleading possibility that both capacities can stay tiny indefinitely outside the known exceptional/finite core.

## 6. Infinite-sequence consequence

Let

\[
1+b_j=c_j
\]

be an infinite sequence of pairwise distinct Pasten-nonexceptional unit triples.

Then for every fixed `H`, only finitely many terms can satisfy

\[
\max\{C(b_j),C(c_j)\}\le H.
\]

Equivalently,

\[
\boxed{
\max\{C(b_j),C(c_j)\}\to\infty.
}
\]

This is weaker than what PCC needs: the dominant cross-ratio may still divide a large residual by the **smaller** neighboring capacity. The result should therefore be treated as a structural pruning theorem, not a projective bound.

## 7. Prior-art discipline

Mihailescu's proof of Catalan's conjecture is external prior art:

Preda Mihailescu, *Primary cyclotomic units and a proof of Catalans conjecture*, Journal fur die reine und angewandte Mathematik 572 (2004), 167–195, DOI `10.1515/crll.2004.048`.

Registered source: `sources_p025_unit_capacity.json`.

P025 owns only the preceding capacity reduction and the composition of that reduction with the known theorem.

## 8. Architectural meaning

At any fixed capacity horizon, the infinite unit state space decomposes as

\[
\boxed{
\text{finite composite core}
\cup
\text{bounded-exponent prime-power branches}.
}
\]

When both neighboring blocks are restricted to the same bounded horizon, external Diophantine rigidity collapses the nonexceptional tail completely.

This is a concrete example of a finite-precision state exposing exactly which parametric families require deeper mathematics.

## 9. Next frontier

No hard block exists. Continue with the asymmetric branch:

1. fix a low-capacity prime-power side `p^e`, `e` bounded;
2. analyze multiplicity residual and capacity of `p^e±1`;
3. use congruence / cyclotomic factorization to bound how powerful the neighboring integer can be;
4. prioritize the prime-square shell `C=2`, which contains the strongest current unit PCC example;
5. do not confuse bounded-capacity finiteness with a uniform PCC exponent.
