# P019 Supplement 02 — Obstruction to Exact Discrete Isotropy and Relation Context

Status: `RESEARCH WIP`  
Scope: finite-precision relative distance, graph symmetry, local finiteness, growth  
Prior art: Macpherson's classification of infinite locally finite distance-transitive graphs; must be registered in `sources.json` / `lineage.json` before merge

## 1. Why `D=1` is still not enough

The main note defines

\[
D_p(x,y)=R_2(q_p(x,y)).
\]

In `A_3`, `q=1,2,3` all map to integer distance `1`, expanding the traditional 12 primitive contacts into 42 distance-1 states.

This enriches the available directions, but it creates a necessary consistency test:

> If two displacements both have numerical distance `1`, can the discrete relation structure still distinguish them?

If it can, then `D` is only a coarse radial value, not the complete relative-relation state.

## 2. P019-C01 — The 42-state `A_3` unit-distance graph is not edge-homogeneous

Define the precision unit graph `G_p^[1]`:

- vertices are `A_p` states;
- two vertices are adjacent iff `D_p(x,y)=1`.

For an edge `0--v`, define the number of common neighbors

\[
\lambda(v)
=
\#\{w:D(0,w)=1,\ D(v,w)=1\}.
\]

This is a pure graph invariant: every graph automorphism preserves common-neighbor count.

Complete finite enumeration in `A_3` gives:

| fine separation | number of edges in class | `lambda` |
|---:|---:|---:|
| `q=1` | 12 | 24 |
| `q=2` | 6 | 20 |
| `q=3` | 24 | 14 |

Therefore the three relation classes with the same numerical value `D=1` have different common-neighbor counts.

No graph automorphism can map a `q=1` edge to a `q=2` or `q=3` edge. Hence

\[
\boxed{
D=1\ \text{does not imply complete relational equivalence.}
}
\]

This directly falsifies the overly strong proposal that collapsing `q=1,2,3` to one automatically restores full isotropy.

## 3. Higher dimension can split even one fixed `q`

In the `A_5` `D=1` graph, `q=3` already contains two integer pattern classes:

1. `(+2,-1,-1)` and its global negative;
2. three `+1` entries and three `-1` entries.

Finite enumeration gives common-neighbor counts `54` and `58` for these two `q=3` edge classes.

Thus in higher dimensions, **even `q` need not be a complete relation type**.

The correct state hierarchy must therefore distinguish at least

\[
\text{integer distance value}
\quad\text{from}\quad
\text{discrete relation context}.
\]

## 4. Candidate correction: relative distance is “value + relation type”

Let `tau_p(v)` denote the automorphism orbit of displacement `v` in the current discrete structure. Before a complete orbit classification is available, integer invariants such as common-neighbor count, local motifs, or coordinate multiplicity patterns can serve as computable signatures.

A candidate relative-distance state is

\[
\boxed{
\mathfrak D_p(x,y)
=
\bigl(D_p(x,y),\tau_p(x-y)\bigr).
}
\]

Here:

- `D_p` is the finite-precision radial value;
- `tau_p` is relation context;
- `tau_p` must not be disguised as a finer decimal distance;
- numerical `1` remains just `1`; directional/gluing distinctions live in the context layer.

This matches the Precision Mathematics starting point `value + precision/resolution + context`.

## 5. The strongest exact discrete isotropy: distance-transitivity

A connected graph is distance-transitive if any two ordered vertex pairs at the same graph distance can be mapped to one another by a graph automorphism.

Thus, if “same distance means complete structural indistinguishability” is imposed as a hard requirement, distance-transitivity is a natural external stress test.

For infinite locally finite graphs, however, it is extremely restrictive.

## 6. External classification gives a no-go constraint

Macpherson classified infinite locally finite distance-transitive graphs of finite valency in 1982. Later literature commonly writes the classified family as `M(s,t)` / `X_(s,t)`:

1. start from a bipartite semiregular tree with degrees `s` and `t` in the two blocks;
2. take one bipartite block as the new graph's vertex set;
3. join two new vertices iff their distance in the original tree is two.

Here `s,t>1` are finite integers.

This is established prior work, not an Enterprise Math result.

## 7. P019-F01 — The classification immediately yields a growth dichotomy

For a root vertex in `M(s,t)`, the first graph sphere has size

\[
S_1=s(t-1).
\]

After the first layer, each new vertex has

\[
(s-1)(t-1)
\]

new descendants away from the root in the underlying tree. Hence

\[
\boxed{
S_r
=
s(t-1)
\bigl((s-1)(t-1)\bigr)^{r-1},
\qquad r\ge1.
}
\]

Because `s,t>1` are integers:

- `(s-1)(t-1)=1` only when `s=t=2`, giving a one-dimensional chain-type structure;
- every other case has `(s-1)(t-1)>=2`, hence exponential sphere growth.

Therefore

\[
\boxed{
\text{infinite + locally finite + exactly distance-transitive}
}
\]

is either the one-dimensional chain case or has tree-like exponential growth rather than finite-dimensional `r^p`-type lattice growth.

## 8. P019-H01 — The Enterprise Math incompatibility triangle

If `p`-dimensionality is at least partly reflected by graph-ball capacity growing polynomially with degree `p`, then for `p>=2` the following three properties cannot all be hard axioms of one fixed graph:

1. **local finiteness**: every minimum state has only finitely many primitive relations;
2. **finite-dimensional polynomial growth**: ball capacity grows like `r^p`, not exponentially;
3. **strict structural equivalence of all equal-distance pairs**: global distance-transitivity.

This does not say that a discrete space cannot be approximately isotropic. It says:

> **One fixed locally finite finite-dimensional-growth graph cannot literally reproduce the perfect rotational homogeneity of the continuum.**

This is a useful boundary condition for the current research program.

## 9. Enterprise Math therefore needs its own finite-precision isotropy

Full distance-transitivity is no longer the target; it becomes an upper-bound stress test.

A candidate hierarchy is:

### Level 0 — vertex homogeneity

All unit states have isomorphic local rules.

### Level 1 — primitive relation homogeneity

Primitive relations should occupy as few automorphism orbits as possible; one orbit is the ideal case.

### Level 2 — second-moment balance

Complete finite-precision shells have exact balanced second integer directional moments. The main note proves this for fixed `q` shells of `A_p`.

### Level 3 — orbit spread

Within one integer distance basin, measure the variation of integer local signatures across relation orbits, for example

\[
\Lambda_{p,k}
=
\{\lambda(v):D_p(0,v)=k\}.
\]

If this set has one value, the layer passes at least the common-neighbor homogeneity test. More spread means more structural direction/context survives at that precision.

### Level 4 — higher finite moments / motifs

Use finite integer fourth moments, cycle counts, ball intersections, and related tests, without making continuous angle a primitive object.

## 10. A fixed lattice need not serve every precision layer

P009 already establishes that scale tags must not be erased. There is therefore no reason to require every precision level to share one fixed adjacency graph.

We can study a typed relation system

\[
G_{p,d},
\]

where:

- `p` is structural dimension;
- `d` is the explicit precision scale;
- every layer has finitely many primitive relations;
- fine-to-coarse maps are typed projections;
- coarser layers may have different effective relation orbits instead of freezing all directions at the finest layer forever.

This avoids the impossible demand that one fixed finite-direction graph be perfectly isotropic at every scale.

## 11. Coarsening cannot simply identify overlapping distance balls

A major risk remains: defining

\[
D(x,y)=0
\]

as “the same coarse state” need not produce a transitive relation, so it need not define a valid quotient.

True scale coarsening should therefore continue to use the **explicit projection fibers** of P005/P009. Distance balls are relation/observation objects unless a valid quotient theorem is separately proved.

Thus

\[
\text{state collapse}
\neq
\text{distance collapse}.
\]

They may constrain each other, but must not be silently identified.

## 12. Current conclusion

This supplement produces three important corrections:

1. **FCC/A_p plus `D=R_2(q)` still does not have complete unit-distance homogeneity**;
2. **perfect distance-transitivity is too strong for a locally finite finite-dimensional discrete space**, because the classical classification pushes every non-one-dimensional case into tree-like exponential growth;
3. Enterprise Math therefore needs a finite-precision relation geometry with context, explicit precision tags, and integer measures of directional bias rather than a mythical perfect discrete sphere.

The better current relative-state prototype is

\[
\boxed{
\text{relative state}
=
\text{integer distance}
+
\text{precision tag}
+
\text{relation context}.
}
\]

This is more consistent with the present foundations than forcing all geometry into one integer distance value.
