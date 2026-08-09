# P019 — Causal Local Isotropy: Primitive Direction Links, FCC/HCP, and Higher-Dimensional Competition

Status: `ACTIVE CROSS-ROUTE RESEARCH / EXACT DISCRETE THEOREMS + CANDIDATE AXIOMS`

This file deliberately avoids the sequential Supplement numbers currently used by concurrent P019 work. It records an independent minimum-precision geometry line for later semantic replay.

## 1. Research correction

The intuition that simple cubic geometry may be a poor minimum-resolution model while FCC/HCP are more natural must not be justified only by packing density or hidden Euclidean angles.

The stricter question is

\[
\boxed{
\text{what finite relation structure do primitive directions themselves form inside the minimum adjacency language?}
}
\]

The comparison now uses primitive-neighbor sets, primitive-direction links, primitive-edge common-neighbor contexts, higher-shell orbit profiles, graph-ball growth, relation boundaries, and graded future-resolution behavior.

## 2. The A_p primitive-direction link

For

\[
A_p=\{x\in\mathbb Z^{p+1}:\sum_i x_i=0\},
\]

primitive moves are

\[
e_i-e_j,\qquad i\ne j.
\]

Represent a direction by the ordered pair `(i,j)`. Two first-shell endpoints are still primitive neighbors exactly when

\[
\boxed{(i,j)\sim(k,l)\iff i=k\ \text{or}\ j=l.}
\]

Hence

\[
\boxed{N_1=p(p+1)},
\qquad
\boxed{\deg L_p=2(p-1)},
\]

and

\[
\boxed{|E(L_p)|=p(p+1)(p-1)}.
\]

For `p>=2` the direction link is connected and has graph diameter three.

Low dimensions:

- `A2`: six directions, degree two, a six-cycle link;
- `A3`: twelve directions, degree four, 24 link edges, eight triangles, and six chordless row/column rectangles.

The latter are the finite graph counts of the cuboctahedral local link. The identification of root lattice A3 with the three-dimensional FCC lattice is established prior art, not a project novelty claim.

## 3. A_p primitive-edge context theorem

Fix the primitive edge

\[
0\leftrightarrow e_i-e_j.
\]

Its common primitive neighbors are exactly

\[
\{e_i-e_k:k\ne i,j\}
\]

and

\[
\{e_k-e_j:k\ne i,j\}.
\]

Each group is a clique `K_(p-1)` and there are no primitive edges between the two groups. Therefore

\[
\boxed{\operatorname{CN}_{A_p}(e_i-e_j)\cong K_{p-1}\sqcup K_{p-1}.}
\]

Every primitive edge has the same integer signature

\[
\boxed{
\left(2(p-1),2\binom{p-1}{2},(p-1,p-1)\right).
}
\]

For A3 this is

\[
\boxed{(4,2,(2,2))},
\]

the graph-theoretic 421 common-neighbor pattern.

Established common-neighbor analysis of ideal close-packed structures identifies FCC as 12×421 and HCP as 6×421 + 6×422. Thus FCC and HCP have the same first coordination number twelve but already split at the level of nearest-neighbor relation context.

## 4. Simple-cubic pressure test

The standard-axis `Z^p` primitive directions are

\[
\pm e_i,
\]

so there are `2p` first neighbors. No pair of distinct first-shell endpoints differs by another primitive axis step. Hence

\[
\boxed{|E(L_{Z^p})|=0.}
\]

Simple cubic can still have first-shell transitivity under coordinate symmetries, but its primitive directions are mutually disconnected at the minimum adjacency layer.

## 5. Higher-shell orbit minimization is rejected as a standalone isotropy rule

The diagnostic

\[
a_\Lambda(r)=|S_\Lambda(r)/\operatorname{Stab}(0)|
\]

cannot simply be minimized and called isotropy.

At graph radius two, `Z^3` has two orbit types,

\[
(2,0,0),\qquad(1,1,0),
\]

so

\[
\boxed{a_{Z^3}(2)=2},
\]

with orbit sizes `6,12`.

`A3` has three types under coordinate permutations plus global sign:

\[
(2,-2,0,0),
\]

\[
(2,-1,-1,0)\text{ and its negative},
\]

\[
(1,1,-1,-1),
\]

so

\[
\boxed{a_{A_3}(2)=3},
\]

with orbit sizes `12,24,6` and shell size 42.

Thus naive higher-shell orbit minimization would rank simple cubic above A3 at radius two. That standalone rule is explicitly rejected.

## 6. Candidate causal local-isotropy axioms

These remain hypotheses under pressure test.

### CLI-1 primitive-direction transitivity

All primitive directions should be structurally equivalent under the origin stabilizer.

### CLI-2 direction-link connectedness

For dimension at least two, primitive directions should form a connected relation link at the minimum adjacency layer rather than an unrelated set of axis labels.

### CLI-3 primitive-edge context uniformity

Every primitive edge should have an isomorphic finite common-neighbor context.

A_p satisfies CLI-1/2/3. Standard-axis simple cubic fails CLI-2. Ideal HCP has two nearest-neighbor CNA contexts, so if CLI-3 survives later pressure tests, HCP would not qualify as a single-context primitive lattice in the same way as FCC/A3.

These conditions do not uniquely define A_p.

## 7. D_n pressure test: the axioms do not hard-code A_p

For root lattice `D_n`, primitive roots are

\[
\pm e_i\pm e_j,\qquad i\ne j.
\]

Pure integer root-difference adjacency gives

\[
\boxed{N_1=2n(n-1)},
\qquad
\boxed{\deg L_{D_n}=4(n-2)}.
\]

For `n>=3` the direction link is connected and the primitive-edge context is uniform.

### D3

Twelve directions, degree four, 24 link edges, edge common-neighbor signature

\[
(4,2,(2,2)),
\]

matching the A3/FCC local data and the low-dimensional D3/A3 equivalence.

### D4

\[
\boxed{N_1=24},
\qquad
\boxed{\deg L=8}.
\]

Every primitive edge has eight common neighbors whose induced graph is connected with twelve internal edges:

\[
\boxed{(8,12,(8))}.
\]

A4 has only twenty primitive directions, link degree six, and edge context `K3 sqcup K3`. Thus the success of FCC/A3 in three dimensions cannot be extrapolated into a rule selecting A_p in every dimension. A/D/E families must compete under the same causal diagnostics dimension by dimension.

Executable assets:

- `causal_lattice_direction_link.py`
- `causal_d_lattice_direction_link.py`
- corresponding tests.

## 8. FCC/HCP should first be seen as trajectories of one close-packed support law

Let close-packed layer registries be

\[
s_n\in\mathbb Z/3\mathbb Z,
\]

with adjacent layers using different registries. Define the relative step

\[
\delta_n=s_{n+1}-s_n\in\{+1,-1\}\pmod3.
\]

Given two consecutive layers, there are exactly two close-packed continuations:

\[
\boxed{F:\delta\mapsto\delta}
\]

for continuing to the third registry, and

\[
\boxed{H:\delta\mapsto-\delta}
\]

for returning to the registry used two layers earlier.

With the first two registries fixed,

\[
\boxed{\{F,H\}^{N-2}\longleftrightarrow\text{length-N close-packed stacking sequences}}
\]

is a bijection.

- `FFFF...` gives `ABCABC...`: FCC stacking;
- `HHHH...` gives `ABAB...`: HCP stacking;
- arbitrary words give stacking-fault/polytype support sequences.

Thus the cleaner ontological order is

\[
\boxed{
\text{one local close-packed support law}
+\text{continuation trajectory}
\to\text{FCC/HCP/polytype}.
}
\]

Absolute registry phase changes under a global `+1 mod 3` relabeling while the relative `delta` sequence and F/H word remain unchanged, so registry phase behaves as a coordinate/gauge-like label rather than a minimum relative continuation state.

Executable assets:

- `causal_close_packed_stacking.py`
- `tests/test_causal_close_packed_stacking.py`

## 9. Support complexity and physical observation complexity remain distinct

A two-state relative support continuation does not imply that real material energy, entropy, or other grades depend on only two layers. If a physical observation reads longer stacking context, `CAUSAL_OPERATION_CLOSURE_CORE` automatically refines the continuation state.

Therefore

\[
\boxed{\text{support complexity}\ne\text{physical observation complexity}.}
\]

## 10. Current comparison vector

Do not collapse the comparison into one scalar yet:

\[
\boxed{
\mathcal I(\Lambda)=
(N_1,\mathrm{orbit}_1,\mathrm{LinkConnectivity},\mathrm{EdgeContextTypes},\mathrm{ShellOrbitProfile},\mathrm{BallGrowth},\mathrm{RelationBoundary},\mathrm{FutureStateComplexity}).
}
\]

This is more compatible with the Enterprise Math causal/discrete discipline than a single packing-density or Euclidean-angular-variance score.

## 11. Status

Internally proved here:

- closed A_p direction-link formulas;
- A_p edge common-neighbor context `K_(p-1) sqcup K_(p-1)`;
- edgeless simple-cubic first-direction link;
- A3 radius-two orbit count three versus Z3 count two;
- D_n local-link pressure-test formulas;
- close-packed F/H continuation bijection.

External established facts:

- A3/FCC correspondence;
- common-neighbor analysis;
- ideal FCC 12×421 versus ideal HCP 6×421+6×422.

Still hypotheses:

- whether CLI-1/2/3 should become minimum-precision axioms;
- the best candidate family in each dimension;
- the final bridge from primitive direction links to Voronoi precision domains;
- the physical falsification contract for local isotropy.

## 12. Next work

1. compute the same local comparison vector for E8 and other high-symmetry candidates;
2. construct structures satisfying CLI-1/2/3 that are nevertheless physically implausible, to pressure-test the axioms;
3. minimize higher-order close-packed observation states with the general operation-language quotient;
4. test whether direction-link data can be recovered combinatorially from finite Voronoi/Delaunay incidence;
5. promote FCC/A3 beyond candidate status only if these pressure tests survive.
