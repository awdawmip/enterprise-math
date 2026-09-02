# BRC positive-rational gauge as a prime-valuation holonomy module

Status: `RESEARCH CANDIDATE / EXACT INTEGER COHOMOLOGICAL NORMAL FORM`
Date: `2026-09-02`
Research mode: `TASK_RESEARCH continuation`
Foundation baseline: `main@86f42d9ebd06dc86ad262ab794ce64cd67517b7f`
Parent research: recurrent logdet / loop-response gauge geometry

## 0. Question

The current positive Weighted-BRC recurrent layer uses rational branch weights

\[
q_e\in\mathbb Q_{>0}^{\times}
\]

and vertex gauge

\[
q'_e=q_e\frac{h_{t(e)}}{h_{s(e)}},
\qquad
h_v\in\mathbb Q_{>0}^{\times}.
\]

Log coordinates make the gauge additive,

\[
\ln q'_e=\ln q_e+\ln h_{t(e)}-\ln h_{s(e)},
\]

but `LN/LOG` are derived readouts rather than primitive native state.

Can the exact rational gauge class be represented entirely by integer number-theoretic data before logarithmic materialization?

Yes. Unique prime factorization gives a complete prime-valuation cohomology normal form.

Generic graph cohomology, spanning-tree gauge fixing, and unique factorization are classical mathematics. No generic novelty claim is made. The project-specific result is their typed integration with positive rational BRC gauge, recurrent response, and the existing `C_2/H^1` holonomy layer.

## 1. Rational weights as finite-support prime valuations

The multiplicative group of positive rationals has the exact decomposition

\[
\boxed{
\mathbb Q_{>0}^{\times}
\cong
\bigoplus_{p\ \mathrm{prime}}\mathbb Z,
}
\]

via

\[
q\longmapsto(v_p(q))_p.
\]

Only finitely many coordinates are nonzero for each rational `q`.

For every edge `e`, define the prime-valuation 1-cochain

\[
\nu_p(e):=v_p(q_e)\in\mathbb Z.
\]

For a vertex gauge `h`, put

\[
\phi_p(v):=v_p(h_v).
\]

Then

\[
\boxed{
\nu'_p(e)
=\nu_p(e)+\phi_p(t(e))-\phi_p(s(e)).
}
\]

Thus rational vertex gauge is literally integer coboundary addition, prime by prime.

## 2. Exact cohomology classification

Treat the finite directed multigraph as a one-dimensional CW complex with its given edge orientations. There are no 2-cells, so for any abelian coefficient group `A`,

\[
H^1(G;A)=C^1(G;A)/\delta C^0(G;A).
\]

Therefore the rational positive-weight gauge class is

\[
[q]\in H^1(G;\mathbb Q_{>0}^{\times}).
\]

Using unique factorization coordinatewise,

\[
C^k\!\left(G;\mathbb Q_{>0}^{\times}\right)
\cong
\bigoplus_p C^k(G;\mathbb Z)
\]

for `k=0,1`, and the coboundary acts primewise. Hence

\[
\boxed{
H^1(G;\mathbb Q_{>0}^{\times})
\cong
\bigoplus_p H^1(G;\mathbb Z).
}
\]

This is a direct algebraic classification, not a logarithmic approximation.

For a connected graph with first Betti number

\[
\beta_1=|E|-|V|+1,
\]

we have

\[
H^1(G;\mathbb Z)\cong\mathbb Z^{\beta_1},
\]

so

\[
\boxed{
H^1(G;\mathbb Q_{>0}^{\times})
\cong
\bigoplus_p\mathbb Z^{\beta_1}
\cong
(\mathbb Q_{>0}^{\times})^{\beta_1}.
}
\]

Candidate theorem name:

`BRC_POSITIVE_RATIONAL_GAUGE_PRIME_VALUATION_CLASSIFICATION`.

## 3. Spanning-tree gauge normal form

Assume the underlying undirected multigraph is connected. Choose:

- a root vertex `r`;
- an underlying spanning tree `T` consisting of `|V|-1` directed edges from the original edge set (their orientations need not point away from the root).

There exists a unique rational vertex gauge with

\[
h_r=1
\]

such that every tree-edge weight becomes

\[
\boxed{q'_e=1\qquad(e\in T).}
\]

Existence is recursive along the tree. For a tree edge `e:a->b`, the equation

\[
q_eh_b/h_a=1
\]

uniquely determines the unknown endpoint scale once the other endpoint scale is known. No consistency obstruction exists because `T` has no cycles.

Uniqueness follows because the ratio of two such gauges is constant along every tree edge and equals `1` at the root.

The remaining

\[
\beta_1=|E|-|V|+1
\]

non-tree weights

\[
\widehat q_e
\qquad(e\notin T)
\]

form a complete coordinate system for the rational gauge class.

Two rational edge-weight systems are gauge equivalent iff their tree-normalized non-tree coordinates agree.

Candidate theorem name:

`BRC_RATIONAL_SPANNING_TREE_GAUGE_NORMAL_FORM`.

## 4. Fundamental-cycle holonomy

For a non-tree edge

\[
e:a\to b,
\]

follow `e`, then follow the unique underlying tree path from `b` back to `a`. Traverse each tree edge with exponent `+1` when the path follows its stored orientation and exponent `-1` when it traverses against that orientation.

Define the algebraic fundamental-cycle product

\[
\operatorname{Hol}_T(e)
=q_e\prod_{f\in P_T(b,a)}q_f^{\epsilon_f}.
\]

Vertex-gauge factors telescope around this algebraic cycle, so `Hol_T(e)` is gauge invariant.

In the tree gauge all tree weights are `1`, hence

\[
\boxed{
\widehat q_e=\operatorname{Hol}_T(e).
}
\]

Thus the spanning-tree normal coordinates are exactly fundamental-cycle multiplicative holonomies.

Prime by prime,

\[
\boxed{
v_p(\widehat q_e)
=\sum_{f\in C_e}\epsilon_fv_p(q_f).
}
\]

This gives a concrete integer cycle basis for the abstract cohomology classification.

Candidate theorem name:

`BRC_RATIONAL_FUNDAMENTAL_CYCLE_HOLONOMY_NORMAL_FORM`.

## 5. Complete prime-valuation normal coordinates

Factor each non-tree holonomy:

\[
\widehat q_e
=\prod_p p^{\nu_{p,e}},
\qquad
\nu_{p,e}\in\mathbb Z.
\]

Only finitely many primes occur across a finite graph instance.

The finite family

\[
\boxed{
(\nu_{p,e})_{p,\ e\notin T}
}
\]

is a complete exact gauge invariant.

Two positive rational branch systems are rational-vertex-gauge equivalent iff these integers agree for every prime and every non-tree edge.

No transcendental comparison is needed.

## 6. Log holonomy is a faithful derived readout

For every normalized cycle coordinate,

\[
\ln\widehat q_e
=\sum_p\nu_{p,e}\ln p.
\]

This representation is faithful. If

\[
\sum_p n_p\ln p=0
\]

for finitely many integers `n_p`, then exponentiating gives

\[
\prod_pp^{n_p}=1,
\]

and unique factorization forces every `n_p=0`.

Therefore no information is lost when the integer valuation module is mapped to the ordinary real log-holonomy readout.

However, the image should **not** be called a Euclidean lattice in general: the additive subgroup generated by several `ln p` need not be discrete in the real topology. The exact object is an abstract free-abelian/prime-valuation module with a faithful logarithmic embedding.

Freeze:

```text
PRIME_VALUATION_MODULE != EUCLIDEAN_DISCRETE_LATTICE
LOG_HOLONOMY = FAITHFUL_DERIVED_READOUT
```

## 7. Exact m-th-power shadows

For every integer `m>=2`, reduce prime valuations modulo `m`:

\[
\nu_p(e)\mapsto\nu_p(e)\bmod m.
\]

Gauge coboundaries reduce to gauge coboundaries, so every prime induces

\[
\boxed{
\sigma_{p,m}:
H^1(G;\mathbb Q_{>0}^{\times})
\to
H^1(G;\mathbb Z/m\mathbb Z).
}
\]

Collecting all primes gives

\[
\boxed{
H^1(G;\mathbb Q_{>0}^{\times})
/mH^1(G;\mathbb Q_{>0}^{\times})
\cong
\bigoplus_p H^1(G;\mathbb Z/m\mathbb Z).
}
\]

Equivalently, this is the holonomy of rational weights modulo rational `m`-th powers.

Because graph `H^1(G;Z)` is free abelian, reduction modulo `m` is surjective. Thus every `Z/m` holonomy class has a positive rational `p`-power lift for any chosen prime `p`.

Candidate theorem name:

`BRC_RATIONAL_GAUGE_MTH_POWER_HOLONOMY_SHADOW`.

## 8. C2 / parity holonomy bridge

The case `m=2` is especially important:

\[
\boxed{
\sigma_{p,2}([q])
=[v_p(q)\bmod2]
\in H^1(G;\mathbb F_2).
}
\]

The existing canonical `C_2` flat-connection theorem identifies

\[
\mathrm{Conn}^{\mathrm{flat}}_{C_2}(G)/\mathrm{Gauge}
\cong H^1(G;\mathbb F_2).
\]

Therefore every prime `p` defines a canonical **C2 parity shadow** of a positive rational BRC gauge class.

Conversely, every `C_2` holonomy class can be lifted to a `p`-power positive rational gauge class by assigning fundamental non-tree holonomies `p^0=1` or `p^1=p` according to its cycle bits.

This is a typed bridge, not an identification:

```text
POSITIVE_RATIONAL_GAUGE_CLASS
-> p-VALUATION MOD 2 SHADOW
-> C2 HOLONOMY CLASS
```

The full positive rational class contains integer valuation information far beyond its parity shadow.

Candidate theorem name:

`BRC_PRIME_VALUATION_C2_HOLONOMY_SHADOW`.

## 9. Global square-class shadow

Collecting parity over all primes is exactly rational square class.

For one positive rational `q`, define

\[
\operatorname{sf}(q)
:=\prod_{p:\ v_p(q)\text{ odd}}p.
\]

Then `sf(q)` is a squarefree positive integer and

\[
\boxed{
q/\operatorname{sf}(q)\in(\mathbb Q_{>0}^{\times})^2.
}
\]

Note that numerator and denominator primes are treated the same modulo squares because `p^{-1}` and `p` differ by the square `p^{-2}`.

Thus every fundamental rational cycle holonomy has a canonical squarefree-integer parity representative.

At the graph level,

\[
\boxed{
H^1(G;\mathbb Q_{>0}^{\times})
/2H^1(G;\mathbb Q_{>0}^{\times})
\cong
\bigoplus_pH^1(G;\mathbb F_2).
}
\]

This gives the positive rational gauge layer a direct squarefree/C2 shadow without discarding repeated-prime information at the full integer-valuation level.

## 10. Relation to recurrent BRC observables

The current recurrent observables

- loop surplus `Gamma`;
- edge response `R_e`;
- response Hessian `H`;

are invariant under positive rational vertex gauge. Therefore they factor through

\[
H^1(G;\mathbb Q_{>0}^{\times}).
\]

On a strongly connected recurrent graph, the real log-edge Hessian kernel is exactly the real vertex-gauge coboundary space. The present result identifies the exact rational points of that gauge quotient by prime-valuation integer data before log readout.

Thus the current two descriptions are compatible:

```text
EXACT ARITHMETIC CLASS:
    direct-sum prime valuation cohomology

DERIVED LOG GEOMETRY:
    real log-holonomy quotient with exact rational Hessian metric
```

The Hessian metric is evaluated on the logarithmic image of the rational gauge class; it does not turn the prime-valuation module itself into a Euclidean lattice.

## 11. General graph versus recurrent core

The cohomology classification applies to the full underlying graph and can retain gauge-invariant multiplicative data even on feed-forward portions that participate in undirected algebraic cycles.

By contrast, `Gamma`, `R`, and the loop-response Hessian see only **directed recurrent cycles** and are blind to inter-SCC feed-forward edges.

Therefore:

\[
\boxed{
\text{full rational gauge cohomology}
\text{ can be strictly richer than }
\text{recurrent loop observables}.
}
\]

On each strongly connected recurrent SCC, directed cycles generate the relevant cycle space and the two gauge/cycle descriptions align exactly.

This distinction must be preserved; recurrent loop-zeta is not a complete invariant of the full rational edge-gauge class.

## 12. Prior-art boundary

Classical ingredients include:

- unique factorization of positive rationals;
- cellular cohomology of a graph;
- spanning-tree gauge fixing and cycle-space coordinates;
- reduction of integer cohomology modulo `m`;
- multiplicative gauge/holonomy language.

No generic novelty claim is made for these facts.

The project-specific synthesis under test is:

```text
POSITIVE RATIONAL WEIGHTED-BRC GAUGE
-> PRIME-VALUATION INTEGER 1-COCHAINS
-> DIRECT-SUM H^1(G;Z) HOLONOMY MODULE
-> SPANNING-TREE RATIONAL NORMAL FORM
-> FAITHFUL LOG READOUT
-> MOD-m POWER SHADOWS
-> PRIME-INDEXED C2 HOLONOMY BITS
-> SQUAREFREE PARITY REPRESENTATIVES
```

## 13. Hard boundaries

This candidate does not claim:

- that the prime-valuation module is a discrete Euclidean lattice after logarithmic embedding;
- that positive rational gauge exhausts arbitrary positive-real gauge classes;
- that the `C_2` parity shadow recovers full integer valuations;
- that rational multiplicative holonomy equals signed/oriented `Omega_2` holonomy;
- that recurrent loop-zeta is a complete invariant of feed-forward gauge structure;
- any new theorem about generic graph cohomology or unique factorization.
