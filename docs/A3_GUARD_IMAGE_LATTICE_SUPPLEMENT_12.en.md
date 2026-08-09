# A3 Guard-Image Lattice Supplement 12 — Guard Quotient Modules, Smith Torsion, and the Predicate-Precision Exact Sequence

Status: `RESEARCH WIP / EXACT FINITELY-GENERATED ABELIAN QUOTIENT PROFILE`

## 1. Generalizing the two-guard quotient

Supplement 11 proved that for two guards and a rank-one hidden image,

\[
\mathbb Z^2/\mathbb Z h\cong\mathbb Z\oplus\mathbb Z/d\mathbb Z.
\]

For a general finite guard family,

\[
W:\mathbb Z^k\to\mathbb Z^r,
\]

and a partition kernel `K_A`, define the hidden guard image

\[
\boxed{L_A=W(K_A)\le\mathbb Z^r.}
\]

The natural coarse predicate-information object is the quotient module

\[
\boxed{\mathcal Q_A:=\mathbb Z^r/L_A.}
\]

This is a finitely generated abelian group, not a scalar precision level.

## 2. A3-G42 — Free rank is dual to hidden rank

If

\[
\operatorname{rank}_{\mathbb Q}L_A=d,
\]

then

\[
\boxed{\operatorname{rank}_{free}\mathcal Q_A=r-d.}
\]

Refinement shrinks the hidden lattice, so the quotient free rank can only stay the same or increase.

## 3. Smith invariant factors

Let an integer generator matrix of `L_A` be

\[
G\in\mathbb Z^{m\times r}.
\]

Define determinantal divisors

\[
\Delta_j=\gcd\{\text{all }j\times j\text{ minors of }G\},
\qquad \Delta_0=1.
\]

If the hidden rank is `d`, the nonzero Smith invariant factors are

\[
\boxed{s_j=\Delta_j/\Delta_{j-1},\qquad j=1,\ldots,d}
\]

with

\[
\boxed{s_1\mid s_2\mid\cdots\mid s_d.}
\]

Hence

\[
\boxed{
\mathcal Q_A
\cong
\mathbb Z^{r-d}
\oplus
\bigoplus_{j:s_j>1}\mathbb Z/s_j\mathbb Z.
}
\]

Predicate precision therefore naturally contains both free integer coordinates and finite torsion coordinates.

## 4. A3-G43 — Torsion order

The finite torsion subgroup has order

\[
\boxed{|\operatorname{Tor}(\mathcal Q_A)|=\prod_{j:s_j>1}s_j=\Delta_d.}
\]

If every `s_j=1`, the hidden lattice is primitive/saturated in its rational span and the quotient has no finite torsion. Nontrivial factors encode finite residue information required to identify hidden score cosets completely.

For Supplement 11's rank-one two-guard case, `Delta_1=gcd(|h_1|,|h_2|)=d`, reproducing

\[
\mathbb Z\oplus\mathbb Z/d\mathbb Z.
\]

## 5. A3-G44 — Refinement exact sequence

If `R` refines `P`, then

\[
K_R\subseteq K_P
\]

and therefore

\[
\boxed{L_R\subseteq L_P.}
\]

There is a natural surjection

\[
\pi:\mathbb Z^r/L_R\to\mathbb Z^r/L_P
\]

with kernel `L_P/L_R`. Thus

\[
\boxed{
0\to L_P/L_R\to\mathcal Q_R\to\mathcal Q_P\to0.
}
\]

The exact predicate detail exposed by refinement is therefore precisely the hidden-image quotient

\[
\boxed{L_P/L_R.}
\]

For rank-one modulus refinement,

\[
L_P=\mathbb Z h,
\qquad L_R=q\mathbb Z h,
\]

so the newly exposed detail is

\[
\boxed{L_P/L_R\cong\mathbb Z/q\mathbb Z.}
\]

This is the algebraic source of the finite residue precision used by Supplements 05 and 06.

## 6. Do not merge unrelated gcd/index scales

A3 now contains several distinct arithmetic scales:

1. the structural relation quantum `gcd(m_i)` of weighted relation capacities;
2. Smith torsion factors of the guard hidden-lattice quotient;
3. finite subgroup indices such as `[L_P:L_R]` in rank-preserving refinement.

They may be related for a specific observable map, but they are not interchangeable merely because all involve gcds or indices. Precision state must remain typed.

## 7. A3-G45 — The predicate quotient class is the complete base object for branch geometry

Two fine guard-score vectors `x,x' in Z^r` lie in the same hidden score coset iff

\[
\boxed{x-x'\in L_A,}
\]

i.e. iff

\[
\boxed{[x]=[x']\in\mathcal Q_A.}
\]

Any future query depending only on threshold reachability / branch geometry inside the current coarse fiber should therefore use the quotient class `[x]` as its base state rather than an arbitrary fine representative.

Low-dimensional work can use explicit free/torsion coordinates such as Supplement 11. General implementations should use established Smith/Hermite transformation tools; the A3 reference code currently computes only invariant factors.

## 8. Implementation

Added:

- `src/enterprise_math/guard_quotient_module.py`;
- `tests/test_guard_quotient_module.py`.

The profile records guard count, hidden rank, free rank, Smith invariant factors, torsion factors, and torsion order.

Tests cover the two-guard `(6,-4)` example, primitive rank-one lattices, `Z^2/< (2,0),(0,3) >`, redundant generators, zero/full hidden lattices, and a three-dimensional diagonal Smith profile `(2,4,8)`.

## 9. Prior-art boundary

Smith normal form, determinantal divisors, finitely generated abelian groups, and exact sequences are standard algebra. A3 does not claim these tools as original.

The project-specific interface is

\[
\boxed{
\text{partition hidden motion}
\to W(K_A)
\to \mathbb Z^r/W(K_A)
\to \text{future predicate precision state}.
}
\]

Novelty of the integrated precision architecture remains unverified.

## 10. Next

1. build a typed `A3PrecisionCertificate` combining relation rank/quantum and guard quotient free/torsion data without scalar weighting;
2. record `L_P/L_R` explicitly as exposed predicate detail in refinement certificates;
3. keep the combinatorial-minor implementation as a research reference and use production HNF/SNF tooling when dependencies are appropriate;
4. use the quotient module as the symbolic state space of global branch programs;
5. build theorem-level bridges to P018 typed scale and P023 minimum state without duplicating their mother theories.
