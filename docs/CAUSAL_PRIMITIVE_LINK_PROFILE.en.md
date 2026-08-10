# Causal Primitive Link Profile — Finite causal uniformity for minimum-resolution directions

Status: `ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE GRAPH RESULTS + PRIOR-ART MAPPING IN PROGRESS`

Ownership: the geometry theorem-home should be consumed by P022/A5. The current `research/core/relation-quotient` branch carries only a cross-route reference implementation and causal-quotient interface; it does not move geometry ownership into A3.

## 1. Correction of direction

A minimum-resolution geometry should not be selected by a single criterion such as:

- maximum packing density;
- maximum primitive coordination;
- minimum higher-shell orbit count;
- visual closeness to a continuous sphere.

P019 already supplies a counterexample: the graph-radius-two shell of `A_3/FCC` has three integer orbit types, while `Z^3` has only two. Therefore naive orbit-count minimization is not a valid standalone isotropy rule.

A more native Enterprise Math question is:

> Within the currently declared minimum relation horizon, do primitive directions have the same causal continuation possibilities?

## 2. Primitive direction link

Let `Phi` be a finite set of primitive integer displacement vectors. Define

\[
\alpha\sim\beta
\iff
\beta-\alpha\in\Phi.
\]

This produces the pure-integer first-shell relation graph `L(Phi)` around the origin.

No angle, square root, or packing-density primitive is required.

The first typed profile includes:

- number of primitive directions;
- link-degree histogram;
- connected components;
- graph diameter;
- rooted primitive-edge common-neighbor graph;
- `(link distance, common-neighbor count)` histogram for direction pairs.

## 3. Compatible-direction flags

An `r`-flag is an `r`-clique in `L(Phi)`: an `r`-set of directions that remain pairwise primitive-compatible.

For a flag `C`, define its one-step continuation capacity

\[
\boxed{
Ext(C)
=
\#\{\alpha:\alpha\text{ is compatible with every direction in }C\}.
}
\]

Collect the `Ext(C)` histogram over all `r`-flags.

If the histogram has one value, then all `r`-flags remain indistinguishable under the future query "how many primitive directions can extend this local relation?"

The first order at which multiple extension counts appear is a **flag continuation split**.

Caution: extension count is only a one-step continuation shadow. In a general graph equal counts need not imply equal full future signatures. Later work must refine it through the contextual quotient. For the highly symmetric low-order A/D/E cases it is already a strict falsifiable diagnostic.

## 4. Finite-horizon isotropy contract

Propose the following research gate, not a physical axiom.

For a declared flag horizon `h`, a candidate primitive geometry passes when:

1. its primitive link is connected;
2. primitive directions have one degree type;
3. rooted primitive-edge contexts have one type;
4. for every `r<=h`, the flag-extension histogram is a singleton.

Interpretation:

\[
\boxed{
\text{isotropy at precision horizon }h
=
\text{local causal continuation indistinguishability through }h.
}
\]

No claim is made that relation contexts must remain identical beyond `h`.

This is compatible with the earlier negative boundary that perfect all-distance transitivity is too strong for a locally finite polynomial-growth geometry.

## 5. A family

For `A_p`,

\[
|\Phi|=p(p+1),
\qquad
\deg L=2(p-1).
\]

For every primitive edge the common-neighbor graph is

\[
\boxed{K_{p-1}\sqcup K_{p-1}.}
\]

Hence `A_3/FCC` has:

- 12 primitive directions;
- link degree 4;
- four common neighbors per primitive edge;
- a common-neighbor graph consisting of two disjoint edges.

Its flag extension laws begin

\[
A_3:\quad4\to1\to0,
\]

\[
A_4:\quad6\to2\to1\to0.
\]

No continuation-count split occurs inside these maximal compatible flags.

This does not make `A_p` universal.

## 6. D-family pressure test

The `D_n` primitive roots are

\[
\pm e_i\pm e_j.
\]

Direct integer enumeration and elementary counting give

\[
|\Phi|=2n(n-1),
\qquad
\deg L=4(n-2).
\]

A rooted primitive-edge context has `4(n-2)` common-neighbor vertices.

- `D_3` is the same 3-dimensional structure as `A_3/FCC`;
- `D_4`: 24 directions, link degree 8, rooted edge context with 8 vertices / 12 internal bonds / connected;
- `D_5`: 40 directions, link degree 12, rooted edge context with 12 vertices / 30 internal bonds / connected.

However `D_5` first splits at triangular flags:

\[
\boxed{
80\text{ triangles have }Ext=0,
\qquad
320\text{ triangles have }Ext=2.
}
\]

Thus larger coordination does not imply higher-order continuation uniformity.

## 7. Exceptional E family

Use the integer-scaled `E_8` roots:

- 112 roots of the form `(±2,±2,0,...,0)`;
- 128 `±1` roots with an even number of minus signs;
- total 240.

The selected subsystems have

\[
|E_6|=72,
\quad
|E_7|=126,
\quad
|E_8|=240.
\]

Low-order link profiles:

| family | directions | link degree | rooted edge context |
|---|---:|---:|---|
| `E6` | 72 | 20 | 20 vertices, 9-regular, connected |
| `E7` | 126 | 32 | 32 vertices, 15-regular, connected |
| `E8` | 240 | 56 | 56 vertices, 27-regular, connected |

Flag continuation enumeration gives

\[
E_6:\quad20\to9\to4\to1\to0,
\]

with all maximal five-flags uniform.

`E_7` first splits at size five: some five-flags are maximal while others admit two further primitive continuations.

For `E_8`,

\[
56\to27\to16\to10\to6\to3
\]

remains uniform through six-flags. Seven-flags first split:

\[
\boxed{Ext=0\quad\text{or}\quad Ext=1.}
\]

The full targeted enumeration gives 207360 seven-cliques: 69120 maximal and 138240 extendable to an eight-clique; there are 17280 eight-cliques.

This agrees with Winter--van Luijk's classification of two Weyl orbits of color-1 seven-cliques in `E_8`, distinguished equivalently by being maximal or non-maximal. That prior work must be recorded in canonical lineage; Enterprise Math does not claim the E8 clique-orbit classification as new.

## 8. Candidate geometries form a Pareto frontier

Same-rank candidates are often incomparable.

At rank four:

- `A_4`: 20 directions, lower local relation capacity, compatible flags uniform through size four;
- `D_4`: 24 directions and richer local edge context, but maximal compatible flags stop at size three.

At rank six:

- `A_6` has a longer maximal compatible flag;
- `E_6` has much larger primitive/local relation capacity while remaining uniform on its own maximal flags.

At rank eight:

- `A_8` has a more regular flag-count law;
- `E_8` has enormous local relation capacity and stays uniform through six-flags, but exhibits a genuine seven-flag split.

Therefore neither "more neighbors is better" nor "later split is always better" should be collapsed into one isotropy score.

The native object should remain typed:

\[
\boxed{
(\text{direction capacity},
\text{edge context},
\text{flag continuation spectrum},
\text{first split order},
\text{pair-context spectrum}).
}
\]

A physical or geometric future language must specify what horizon and distinctions matter before a natural candidate can be selected.

## 9. FCC / HCP placement

External Common Neighbor Analysis literature reports for perfect structures:

- FCC: all 12 nearest-neighbor bonds have 421 context;
- HCP: six 421 and six 422.

This supports the relation-first interpretation: both have coordination 12, but FCC has one primitive bond-context type while HCP already splits into two local types.

This only strengthens FCC as a minimum-horizon uniformity candidate; it does not prove that physical space must be FCC.

## 10. Link to causal signatures

A flag continuation split should not be called a failure of high-order geometry.

Instead:

- below the split horizon, relation states remain future-indistinguishable;
- at a split, the old local summary becomes insufficient and a new continuation type is required;
- whether that new type must actually be retained depends on the declared physical future language.

Thus high-order direction geometry can enter the existing mother mechanism directly:

`raw flag -> future/context quotient -> minimum relation type`.

## 11. Implementation

Added:

- `src/enterprise_math/causal_primitive_link_profile.py`
- `tests/test_causal_primitive_link_profile.py`

Default CI bounds E8 flag enumeration at low order, rather than turning the targeted 400k-plus clique enumeration into a routine gate. Full counts remain a targeted research computation.

## 12. Next

1. Replace one-step `Ext` cardinality with the full finite-horizon flag continuation signature.
2. Reconstruct the HCP coordination link combinatorially and compare it to `A_3/FCC` in the same profile.
3. Build rank-wise Pareto frontiers for `A4/D4`, `A6/D6/E6`, and `A8/D8/E8`.
4. Connect primitive-link unit-cost transport to the graded future-revelation tower.
5. Only after a physical future language is specified may the Pareto frontier select a candidate "natural" minimum-resolution geometry.
