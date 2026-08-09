# LEGO Causal Composition Core — Generating Dimension, Geometry, Coupling, and Future State from Unit Laws

Status: `ACTIVE CROSS-ROUTE RESEARCH ORIENTATION / STAGE-2 CONSOLIDATION / NOT CANONICAL FOUNDATION`

This document is the short recovery entry for causal-absorption stage 2. It does not create a new canonical problem number and does not modify `我眼中的世界.md`. Older P011/P012/P019 documents and research supplements remain proof/history sources.

## 1. Current causal order

The candidate foundation no longer begins with vector spaces, metrics, matrices, tensors, semirings, or precision. It begins with

\[
\boxed{
\text{unit possibilities}
\to
\text{LEGO composition}
\to
\text{causal coupling/witness}
\to
\text{continuation type}
\to
\text{observation/grade}
\to
\text{traditional shadow}.
}
\]

The unit value `1` stays `1`. Increasing dimension changes placement relations, composable futures, and distinguishable structure, not the numerical identity of the unit.

## 2. Free fiber as the first mother object

For `m` slots and total unit count `c`,

\[
\mathcal F_m(c)=\{(a_1,\ldots,a_m)\in\mathbb N^m:\sum_i a_i=c\}.
\]

Its count is

\[
H_m(c)=|\mathcal F_m(c)|=\binom{c+m-1}{m-1},
\]

but the closed form is not primitive. The primary law is

\[
\boxed{
\mathcal F_{m+n}(c)
\cong
\bigsqcup_{a=0}^{c}
\mathcal F_m(a)\times\mathcal F_n(c-a).
}
\]

This precedes convolution or semiring language.

## 3. One-slot dimension raising and lowering

Because `H_1(c)=1`, adjoining one free slot gives

\[
\boxed{H_{m+1}(c)=\sum_{a=0}^{c}H_m(a).}
\]

Removing one placement freedom gives

\[
\boxed{H_m(c)=H_{m+1}(c)-H_{m+1}(c-1)},
\]

with `H(-1)=0`. These are exact LEGO slot operations, not approximations to integration/differentiation.

Repeated differences strip hidden slot freedom one integer step at a time.

## 4. General added-block occupancy law

If a newly added block has `k(b)` admissible causal states at occupancy `b`, and this rule does not inspect hidden identity inside the older block, then

\[
\boxed{G_{m+1}(c)=\sum_{b=0}^{c}k(b)G_m(c-b).}
\]

If `G_m(0)=1`, the occupancy law is recovered without division:

\[
\boxed{k(c)=G_{m+1}(c)-\sum_{b=0}^{c-1}k(b)G_m(c-b).}
\]

If different dimension steps recover different `k`, the hypothesis of one ambient-dimension-independent single-block law is falsified.

Special cases include unrestricted occupancy (`k(c)=1`), hard single occupancy (`k(0)=k(1)=1`, higher `k=0`), and occupancy-dependent internal relation degeneracy (`k(c)>1`).

## 5. Coupling field modifies free composition

For a lower-dimensional fine pair `(u,v)`, define joint multiplicity

\[
\boxed{\kappa(u,v)\in\mathbb N_0.}
\]

Its causal meaning is typed:

- `0`: forbidden pairing / missing support;
- `1`: unique free composition;
- `>1`: several joint causal states above the same lower-dimensional pair.

At fixed coarse total,

\[
\boxed{H_\kappa=H_{free}-M+S},
\]

where `M` counts removed free pairings and `S` counts extra joint-state multiplicity. They must remain separate because they can numerically cancel.

## 6. Minimal future-safe state of coupling

Anonymous `kappa(r)` is generally too coarse for multi-stage composition, while raw witness identity is too fine. Let `tau` be the complete remaining-future continuation-signature class of a current witness and keep

\[
\boxed{\kappa(r,\tau).}
\]

Then

\[
\boxed{N(r,z)=\sum_\tau\kappa(r,\tau)p(\tau,z).}
\]

If every `r` contains exactly one represented `tau`, anonymous `kappa(r)` is further collapsible. For finite deterministic systems, `tau` is compiled by stable future partition refinement.

## 7. Memory as an insufficient-current-state shadow

If a current coarse label `r` contains several continuation types,

\[
\#\{\tau:\kappa(r,\tau)>0\}>1,
\]

then past distinctions still affect the future. The minimal memory repair is

\[
\boxed{r\mapsto(r,\tau)},
\]

not recovery of the complete history.

## 8. Identity-free future state as type inventory

Let

\[
n_\tau=\#\{\text{current witnesses of type }\tau\}.
\]

Witness names inside one continuation type are causally irrelevant. If an operation is additive over disjoint witness families and one `tau` witness has output profile `P_tau(upsilon)`, then

\[
\boxed{n'_\upsilon=\sum_\tau n_\tau P_\tau(\upsilon).}
\]

Nonnegative-integer matrix evolution is a coordinate shadow of this inventory propagation.

## 9. Multi-witness interaction without Taylor expansion

For a type-count vector `n`, any finite integer response has the exact multi-binomial expansion

\[
\boxed{
\phi(\mathbf n)
=
\sum_{\mathbf k\le\mathbf n}
a_{\mathbf k}
\prod_i\binom{n_i}{k_i}.
}
\]

`a_k` records irreducible LEGO co-presence effect. Only `|k|=1` gives the additive/matrix regime. A largest nonzero order `q` gives an exact q-body response, not a truncation. The simple traditional function `min(n,m)` has nonzero coefficients at arbitrarily high orders, so analytic simplicity is not the same as causal LEGO simplicity.

## 10. Interaction criterion for type collapse

When fine continuation types are merged into coarse types, a fine multi-index `k` leaves only the selected-unit totals `K` inside each coarse block. A response descends exactly when

\[
\boxed{a_{\mathbf k}\text{ depends only on the coarse }\mathbf K.}
\]

Thus future-safe quotienting can be read directly from whether irreducible interactions still distinguish the proposed-to-be-merged types.

## 11. Graded LEGO fiber unifies graph/radial/minimum readings

Give one slot a nonnegative integer grade `g(x)`. Multi-slot composition only adds labels:

\[
c=\sum_i x_i,\qquad E=\sum_i g(x_i).
\]

Define

\[
\boxed{
K_{N,g}(c,E)=
\#\{(x_1,\ldots,x_N):\sum x_i=c,\ \sum g(x_i)=E\}.
}
\]

Dimension raising is the one-slot recurrence

\[
\boxed{K_{N+1,g}(c,E)=\sum_x K_{N,g}(c-x,E-g(x)).}
\]

Then shell, ball, minimum cost, and minimizer multiplicity are simply different readings of the same graded fiber.

For `N=p+1`, `c=0`, `g(x)=|x|` exactly reproduces the P012 `A_p` graph balls with grade budget `2r`, while `g(x)=x^2` exactly reproduces the P019 quadratic shells at grade `2q`. P019 `Psi_(m,s)(c)` is simply the lowest occupied grade of the `g(x)=|x|^s` fiber.

## 12. Coupled graded fiber

A joint pair may also carry an integer cross-grade shift

\[
\gamma(u,v)\in\mathbb Z.
\]

The joint graded fiber is

\[
\boxed{
K_{AB}(c,E)=
\sum_{u,v}
\kappa(u,v)
\mathbf1[c=c_u+c_v,\ E=E_u+E_v+\gamma(u,v)].
}
\]

`kappa` is admissibility/multiplicity; `gamma` is the effect of cross interaction on the chosen grade. Support disappearance and grade change are not one scalar phenomenon.

## 13. Traditional-tool status

Current causal-derivation/shadow routes include convolution/semiring laws, matrix multiplication, finite bilinear pair tables, graph/radial integer balls, min-plus minima, finite Markov-like states, finite interaction order, counting measure, and collision spectra.

Arbitrary real tensor spaces, Hilbert tensor products, continuous manifolds, calculus as foundation, arbitrary probability measures, and quantum amplitudes are not promoted to core ontology by this work.

## 14. Current close-packed geometry entry point

This document does not prove or reconstruct physical FCC/HCP selection. The current combinatorial pressure test says that states with the same local packing/registry support can belong to different continuation types when buried stacking relations change future admissible operations or observations.

The candidate route is

\[
\boxed{
\text{free LEGO fiber}
+\text{local packing coupling }\kappa
+\text{continuation type }\tau
}
\]

rather than assigning the primitive unit a cubic/FCC/HCP coordinate ontology in advance.

## 15. Current main attack

The current problem is continuation closure of coupled graded fibers: under `kappa + gamma + continuation type`, determine exactly when arbitrary-dimensional futures are generated recursively from lower-dimensional typed inventories and when genuinely new higher-order compatibility data is required.
