# Gregory–Machin continuation: leaf-prime sieve and bounded exact three-denominator Pareto census

Status: `FREE_RESEARCH / EXACT_PRUNING_THEOREM + EXECUTABLE_BOUNDED_CENSUS / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-B2817C / FREE_AXIOM_DISCOVERY`
Issue: `#1160`
Depends on: `research_notes/GREGORY_MACHIN_GAUSSIAN_VALUATION_LATTICE_20260903.md`
Checker: `research_notes/experiments/gregory_machin_gaussian_triple_census_20260903.py`

## 1. Purpose

The Gaussian valuation-lattice theorem converts exact signed reciprocal-turn endpoint identities into integer linear relations. This note asks the first finite Pareto question:

> among **three distinct reciprocal denominators** `2 <= D <= H`, which denominator sets admit an exact diagonal endpoint certificate, and which has the best Lehmer completion measure?

This is a bounded exact census, not a global classification theorem and not a claim of historical novelty for the identities found.

The endpoint search itself uses exact integers only. Floating-point logarithms appear only after exact feasibility is established, to order the classical Lehmer measure.

---

## 2. Leaf-prime elimination theorem

For a finite denominator universe \(S\), let

\[
n_p(D)
=v_{\pi_p}(D+i)-v_{\bar\pi_p}(D+i)
\]

be the oriented Gaussian valuation coordinate for each split prime \(p\equiv1\pmod4\).

An exact endpoint certificate has coefficients \(c_D\) satisfying

\[
\sum_{D\in S}c_D n_p(D)=0
\quad\text{for every }p.
\]

### Theorem 2.1 — leaf-prime obstruction

If a split prime \(p\) occurs with nonzero coordinate in exactly one denominator \(D_0\in S\), then every exact endpoint certificate supported in \(S\) has

\[
\boxed{c_{D_0}=0.}
\]

#### Proof

The \(p\)-row of the endpoint system is

\[
c_{D_0}n_p(D_0)=0.
\]

Since \(n_p(D_0)\ne0\), it forces \(c_{D_0}=0\). ∎

### Corollary 2.2 — recursive prime-incidence core

After removing \(D_0\), another prime may become a leaf. Recursively eliminate such denominators until every surviving split-prime node has degree at least two.

Every exact endpoint certificate over the original finite universe is supported entirely inside this residual bipartite incidence core.

Freeze:

\[
\boxed{
\texttt{ENDPOINT_SUPPORT}\subseteq\texttt{SPLIT_PRIME_2_CORE}.
}
\]

This is an exact pre-linear-algebra sieve. It depends only on prime support of \(D^2+1\), not on angles, \(\pi\), or floating-point approximation.

---

## 3. Exact Plücker span hashing for triples

After leaf elimination, a naive three-denominator scan is still cubic. The valuation columns allow another exact reduction.

Let \(v_D\in\mathbf Z^r\) be the free split-prime valuation vector of \(U_D\). Three columns can have a nontrivial free-coordinate relation only when

\[
\operatorname{rank}(v_a,v_b,v_c)\le2.
\]

For two linearly independent columns, their two-dimensional rational span is determined by the exterior product

\[
v_a\wedge v_b\in\bigwedge^2\mathbf Z^r
\]

up to nonzero scalar. Normalize all nonzero \(2\times2\) minors by their gcd and an overall sign. This gives an exact **Plücker span hash**.

Pairs with the same normalized wedge lie in the same rational 2-plane. Therefore only denominator triples collected inside one repeated span hash need a rank-two check.

Rank-one columns are handled separately by normalizing each valuation vector by gcd and sign.

This replaces the full cubic scan by:

1. quadratic pair span hashing;
2. a very small set of exact candidate triples;
3. direct integer kernel verification.

No probabilistic hash or floating rank decision occurs.

---

## 4. Rank-two torsion criterion

Suppose a triple \((D_1,D_2,D_3)\) has free-coordinate rank exactly two. Its primitive integer kernel is one-dimensional; let

\[
c^{(0)}=(c_1^{(0)},c_2^{(0)},c_3^{(0)})
\]

be the primitive kernel vector, with all three coordinates nonzero.

Let \(\varepsilon_j\in\mathbf Z/8\mathbf Z\) be the torsion coordinate of \(U_{D_j}\), and put

\[
e=\sum_jc_j^{(0)}\varepsilon_j\pmod8.
\]

A scaled vector \(t c^{(0)}\) hits the diagonal torsion target iff

\[
te\equiv1\pmod8.
\]

Hence:

\[
\boxed{
\text{the denominator triple is endpoint-feasible iff }e\text{ is odd}.
}
\]

Every odd residue is its own inverse modulo eight, so the least-absolute scale is obtained from

\[
t\equiv e\pmod8.
\]

The checker stores this least-\(\ell_1\) representative for reporting. Larger scales \(t+8k\) give further endpoint words on the same denominator set and may have different winding lifts.

---

## 5. Reproducible bounded census

The dedicated task-local checker is

`research_notes/experiments/gregory_machin_gaussian_triple_census_20260903.py`.

It uses only Python's standard library. Exact operations include:

- integer factorization by trial division for the bounded norms;
- sum-of-two-squares construction of Gaussian primes;
- exact Gaussian division;
- exact `C8 + split-prime valuation` signatures;
- recursive leaf-prime elimination;
- normalized integer Plücker span hashes;
- exact integer kernel and mod-eight target checks.

The only floating operation is the final ranking

\[
\mu(D_1,D_2,D_3)
=\sum_{j=1}^3\frac1{\log_{10}D_j},
\]

applied after exact feasibility has been certified.

### 5.1 Height `H=5000`

For the complete denominator universe

\[
2\le D\le5000,
\]

the exact checker returns:

- raw denominators: `4999`;
- removed by recursive leaf-prime obstruction: `3086`;
- surviving prime-incidence core: `1913` denominators;
- split-prime coordinates remaining in the core: `446`;
- exact rank-two candidate triples after Plücker span hashing: `9433`;
- rank-two three-denominator sets admitting the diagonal torsion target: `86`;
- unique rank-one group of size at least three: `[2,3,7]`.

Thus the structural sieve reduces a nominal

\[
\binom{4999}{3}
\]

search to 9433 exact rank-two candidate triples, plus one rank-one family.

The checker contains regression assertions for all these counts.

---

## 6. Gauss remains the exact bounded three-denominator Lehmer leader through `H=5000`

Among the 86 rank-two endpoint-feasible denominator triples at height `H=5000`, the minimum Lehmer measure is

\[
\boxed{(18,57,239)}
\]

with least-absolute endpoint coefficient vector

\[
\boxed{(12,8,-5)}.
\]

This is the classical Gauss-type identity

\[
\boxed{
\frac\pi4
=12\arctan\frac1{18}
+8\arctan\frac1{57}
-5\arctan\frac1{239},
}
\]

whose exact native endpoint certificate was already verified in the predecessor note.

Its Lehmer measure is approximately

\[
\boxed{\mu\approx1.786607534019316.}
\]

### Theorem-status boundary

The statement

> `Gauss is the Lehmer-minimal rank-two three-distinct-denominator endpoint set for 2 <= D <= 5000`

is an **exhaustive finite computational result backed by the exact checker**, not an unbounded theorem.

It also does not say Gauss is globally best among arbitrary support sizes. Classical four- and higher-term Machin-like formulas can have lower Lehmer measures.

---

## 7. The bounded runner-up is the classical Simson/Klingenstierna-type refinement

The second-smallest Lehmer measure through `H=5000` is

\[
(D_1,D_2,D_3)=(10,239,515)
\]

with endpoint vector

\[
(c_1,c_2,c_3)=(8,-1,-4).
\]

Thus

\[
U_{10}^{8}U_{239}^{-1}U_{515}^{-4}=\tau.
\]

At analytic completion the principal lift is

\[
\boxed{
\frac\pi4
=8\arctan\frac1{10}
-\arctan\frac1{239}
-4\arctan\frac1{515}.
}
\]

Its Lehmer measure is approximately

\[
\mu\approx1.789208869239722,
\]

very close to but still above Gauss.

Prior-art audit identifies this as an old formula (modern sources trace it to the 18th century, commonly to Simson/Klingenstierna traditions). No novelty is claimed for the identity.

The endpoint/winding branch can also be fixed without numerical \(\pi\): the total absolute principal-angle bound is

\[
8/10+1/239+4/515<1,
\]

so an endpoint congruent to the positive diagonal cannot differ from the principal \(\pi/4\) lift by a full \(2\pi\) turn.

---

## 8. Further leading bounded certificates

The next few rank-two endpoint sets at `H=5000`, ordered by denominator-only Lehmer measure, begin:

| rank | denominators | least-absolute endpoint coefficients | approx. `mu` |
|---:|---|---|---:|
| 1 | `(18,57,239)` | `(12,8,-5)` | `1.7866075340` |
| 2 | `(10,239,515)` | `(8,-1,-4)` | `1.7892088692` |
| 3 | `(7,53,4443)` | `(5,4,2)` | `2.0373953957` |
| 4 | `(8,57,239)` | `(6,2,1)` | `2.0972771288` |
| 5 | `(5,577,1393)` | `(4,-2,-1)` | `2.1109122128` |

These are endpoint certificates. Historical/prior-art status of each lower-ranked identity is not inferred from the census and must be audited separately before any novelty statement.

---

## 9. A structural interpretation of the sieve

The denominator-prime incidence picture gives a useful exact obstruction hierarchy:

1. **leaf split prime** -> its unique denominator coefficient must vanish;
2. recursively remove the denominator;
3. only the split-prime incidence core can support a relation;
4. within that core, Plücker span hashing detects possible rank-two three-column circuits;
5. torsion parity decides whether the free cancellation can actually hit the diagonal target;
6. finite winding remains a separate certificate;
7. completion cost is evaluated last.

So the search architecture is now

\[
\boxed{
\text{prime support}
\to
\text{incidence core}
\to
\text{valuation span}
\to
\text{integer endpoint relation}
\to
\text{winding}
\to
\text{completion Pareto cost}.
}
\]

This is much sharper than searching arctangent identities numerically.

---

## 10. Next frontier

The remaining bottleneck is support size four and above. A direct \(H^4\) enumeration is unnecessary: the same valuation representation suggests meet-in-the-middle and higher exterior-power / circuit enumeration.

The next target should be:

\[
\texttt{SIGNED_GAUSSIAN_VALUATION_PARETO_FRONTIER_SUPPORT_4_PLUS}.
\]

The principal questions are:

1. how far the leaf-prime core and exact span/circuit hashing can reduce four-column search;
2. at what smallest denominator height a four-or-more-term certificate first beats Gauss's \(\mu\approx1.7866075\);
3. whether the resulting completion gain is Pareto-efficient against native coefficient \(\ell_1\), support size, denominator height, and winding complexity.

No single untyped “best formula” should be promoted: the earlier exact no-go already shows native shortest and analytic fastest are different optimization problems.
