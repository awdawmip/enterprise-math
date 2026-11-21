# R762HR — Exact Port-realizability oracle and the first connected unsigned support obstruction

**Mode:** independent portable research, author proof plus exact exhaustive finite computation; **independent review:** `NOT_REVIEWED`. **Mother task:** `RS-X6-TRIADIC-CLOSURE-DYNAMICS` / `TP2-8B7E13C5904A2D6F1142`. This artifact is not a native CLAIM, PROGRESS, Result, Review or a primitive force-dynamics theorem. Current live researcher identity and native execution authority are unconfirmed; earlier authors retain their original contributions.

**Frozen scientific input:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json` and its observer-preservation companion. Current behavioral rules were separately refreshed. All six original signed axes remain native; event triple masks and Port triangles are *composite candidate* readouts, not primitive three-force closure or a three-dimensional slice.

## Exact model and the source-preserving Port-realization theorem HR1

Let `X={0,1,2,3,4,5}`. A Port is a named 2-subset `P⊂X`. An admissible transition `P→Q` has `|P∩Q|=1` and an associated 3-axis support `S=P∪Q`. Given an unordered **multiset of individually distinguished** support-event occurrences `M=(S_1,...,S_m)`, decide whether they can be reordered into some closed Port history `P_0→P_1→...→P_m=P_0`, with one exact support occurrence assigned to every transition.

For each occurrence `S_t={a,b,c}`, build a small triangle `T(S_t)` whose three *vertices* are the named Ports `ab,ac,bc`, and whose three possible undirected edges are the three different pairs of these Ports. Different occurrences retain distinct source IDs, even when they have the same support.

**HR1 (all lengths, exact).** The support multiset has a closed admissible Port realization **if and only if** one can choose exactly one edge of `T(S_t)` for every occurrence `t`, so that the resulting multigraph on the 15 named Ports (i) has even degree at every vertex and (ii) has connected non-isolated support. Every successful selection and Euler circuit provides an explicit occurrence-level Port history. This is a finite exact graph-factor oracle; one must test actual Port realization, not just adjacency/connectivity among the 3-axis supports.

*Proof.* A closed Port history supplies the selected Port edge `{P_t,P_{t+1}}` for each event. Its union is `S_t` by definition. Each Port has an even number of incoming-plus-outgoing incidences along a closed undirected walk, and the used graph is connected. Conversely, a connected undirected multigraph with all degrees even has an Euler circuit. Traverse that circuit, retaining the source-occurrence label of each edge; by its triangle provenance, consecutive Ports differ by one axis, and the prescribed union support is exactly the source occurrence. All occurrence multiplicities are retained. QED.

For a multiset, the six-coordinate zero-displacement sign-readout depends solely on the multiset of supports, whereas *Port-realizability and later Port/Link/time operations depend on transition provenance*. Thus support histograms are sufficient **only for the explicitly declared final sign-existence/count observer**, not for complete research-state compression.

## HR2. Sharp finite boundary for overlap-connected support multisets

Let `G_M` be the occurrence graph with one vertex per triple occurrence and an undirected edge between distinct occurrences whenever the two 3-axis supports share at least two axes. Let `H=Σ_t 1_{S_t}`. An occurrence-wise sign completion exists precisely when one may select exactly half the occurrences on every axis: `Σ_t z_t 1_{S_t}=H/2` with `z_t∈{0,1}`. The positive-source BRC coefficient is `[x^{H/2}]∏_t (1+x^{1_{S_t}})`, with temporal occurrences distinct in that product.

The adjacent C++17 checker exhausted **all unlabeled multisets** of size `m=2,4,6,8,10` drawn from the 20 distinct named 3-axis support types, then used exact integer half-incidence subset checks. It counted only coordinate-even `H` as eligible. Exact results:

| m | All 20-type multisets | Coordinate-even | Signable | Unsignable | Unsignable with connected `G_M` |
|---:|---:|---:|---:|---:|---:|
| 2 | 210 | 20 | 20 | 0 | 0 |
| 4 | 8,855 | 375 | 345 | 30 | 0 |
| 6 | 177,100 | 6,040 | 5,380 | 660 | 0 |
| 8 | 2,220,075 | 71,435 | 65,735 | 5,700 | 0 |
| 10 | 20,030,010 | 632,996 | 603,636 | 29,360 | **240** |

Therefore **ten occurrences are the exact first possible size of a coordinate-even, overlap-connected but unsignable support multiset**, within this six-named-axis 3-uniform model. This is a sharp finite theorem from exhaustive computation; no arbitrary-length connectedness sufficiency is asserted.

### Explicit ten-occurrence obstruction and short analytic certificate

Use support types, with multiplicities, in the following order (order here lists sources, not a Port history):

`012,012,013,024,134,134,035,035,235,145`.

The support graph `G_M` is connected through overlaps of size at least two; its total original coordinate incidence is

`H=(6,6,4,6,4,4)`, `H/2=(3,3,2,3,2,2)`.

Let `(a,b,c,d,e,f,g)` be the **selected numbers of occurrences** of types `(012,013,024,134,035,235,145)`. The multiplicity bounds are `0≤(a,b,c,d,e,f,g)≤(2,1,1,2,2,1,1)`. Solving the six exact incidence equalities gives *all* rational solutions:

`(a,b,c,d,e,f,g)=(2-2g,3g-1,g,2-2g,2-2g,g,g)`.

The singleton source `145` forces `g=0` or `g=1`; then the singleton source `013` would require `b=-1` or `b=2`, contradicting `0≤b≤1`. Thus the sign coefficient is **exactly zero**. Nevertheless unrestricted integer-lattice membership holds (take `g=0`), demonstrating the distinction between the HR2 bounded source problem and earlier HQ integer-lattice saturation.

**Additional Port obstruction.** For these ten individually distinguishable supports there are `3^{10}=59,049` possible choices of one edge from each associated Port triangle. An exact parity enumeration finds **zero** selections having even Port degree at every Port, before connectivity is even considered. Hence HR1 proves that this connected ten-occurrence counterexample has **no legal closed Port ordering**. This supplies a direct source-level explanation for its compatibility with R762HM's independent result that *actual* closed Port histories through length 12 are signable.

## Validation, limits and integration

- Executed the accompanying C++17 program using `g++ -O3 -std=c++17 -Wall -Wextra -pedantic`; returned `PASS R762HR`. Integer arithmetic only; all enumeration loops finite with explicit bounds. The 20 supported types are generated by the 3-bit-cardinality condition on six named axes.
- For every multiset of even sizes 2–10, exact enumeration of source subsets of size `m/2` checks all six half-degree targets. Checking connectedness uses full fixed-point BFS/closure, not a single ordered scan. Counters above refer to *unlabeled support multisets*; source-event solutions in the coefficient product distinguish occurrences.
- For the explicit witness, a separate exact `3^{10}` triangle-edge parity enumeration checks the necessary closed-Port degree condition. The analytic incidence contradiction independently proves sign unsatisfiability.
- No novel full-length parity sufficiency or counterexample to it is claimed for legal closed Port histories. The earlier HH–HQ original notes remain distinct, with their recorded authors and review states. This note contributes an exact *filter* and a boundary test for a tempting but invalid connectedness surrogate.
- This checker implements the already-proved typed combinatorial positive-source BRC coefficient for the declared candidate final Cell-readout; it does not use classical π/trigonometric or physical time propagation, nor present positive source mass as signed amplitude cancellation.

**Next scientific unit:** Search for a coordinate-even unsignable multiset that **passes HR1**, i.e. has an actual connected Eulerian selection of Port-triangle edges. If none is found, try a constructive decomposition of HR1-realizable occurrence words into sign-balancing certificates. Use exact source-level graph decisions before spending work on any full history. Keep original P000 triadic force/Cell/Link/Port/time/rotation objective open, and keep HR1's Port graph and the original occurrence/source order for future observations.

**Local evidence:** `R762HR_CHECK.cpp` and `R762HR_EVIDENCE.json`. Review status `NOT_REVIEWED`.
