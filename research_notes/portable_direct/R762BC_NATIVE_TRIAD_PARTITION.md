# R762BC — Signed-X6 relational triad incidence, exact decompositions, and resource-constrained hidden-Port lifts

Date: 2026-11-15. Task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`. Author-side research; NOT_REVIEWED.
Scope: an explicitly constructed **candidate typed Cell/Port/Link triad model** satisfying P000's arity and equal-quantum pairwise-\`PERP_E\` requirements. The arity/angle axioms are assumed; physical admissibility, V17/V29/V39 integration and non-candidate native event admission remain open.

## Source and frozen science

- Frozen taskbook and continuation: \`awdawmip/enterprise-math@d5eb171f15801f54c0659a2bbf4e42844ba2d527:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md\`, publication \`TP2-8B7E13C5904A2D6F1142\`.
- Frozen P000: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`, plus \`definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md\` and \`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md\`.
- Prior frontiers: R762BA (four hidden third axes for ordered visible pair), R762BB (eight full-source records for unordered visible pair), PRs #2468 and #2471; R762AY/AZ exact BRC path representations. This note solves a new **global-resource constrained triad partition** problem rather than repeating those fiber calculations.
- Current behavioral rules read separately from frozen scientific pins: \`docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context\`, \`docs/PORTABLE_RESEARCH_PROTOCOL.md\` and \`research_priorities/research_method.json\`.

## Candidate typed event (explicit construction)

Let \`C\` be the affine X6 Cell torsor for \`Z^6\` with no distinguished origin. A named primitive nonzero force quantum attached to a Cell \`c\` is a record
\[
f=(\mathrm{id},c,p,\ell,\varepsilon E_i,w),\quad
i\in\{1,\ldots,6\},\ \varepsilon\in\{+,-\},\ w\in\mathbb Q_{>0}.
\]
Here \`p\` is a named signed native-axis Port at \`c\`, \`\ell\` is its named Link attachment, and the identity remains part of the state. This is a **relational force record**, not a coordinate displacement; a force event does not assert \`c\mapsto c+\varepsilon e_i\`.

Define the candidate ternary closure predicate \`C_E(f,g,h)\` to hold exactly when the three distinct records (i) attach to the same \`c\`, (ii) have equal weight \`w\`, (iii) occupy three pairwise distinct **unsigned** native axes, and (iv) participate in a named 3-uniform Port/Link hyperedge \`H=(id_H,c,\{f,g,h\})\`. Its sign pattern and three named Links are retained. One atomic relation update \`U_H\` marks the three records jointly \`CLOSED\`, leaves Cell coordinates unchanged, and retains the full hyperedge history (an inverse unmark is available only if declared by a later protocol). A two-record input never yields \`CLOSED\`; zero records mean quiescence. A union of multiple hyperedges is composite, not a new primitive force.

The six-axis rotation skeleton \`S_6\` acts by relabelling unsigned axis \`i\mapsto\sigma(i)\`, transports signed Port/Link names and the Cell chart accordingly, and preserves \`C_E\` and \`U_H\`. Pairwise distinct axes satisfy P000's \`PERP_E\` with native angle 120 degrees by the frozen axiom. This is an explicit **consistent realization family** of a typed closure relation, not a claim that every such hyperedge has already been admitted by the project's physical native scheduler. It avoids replacing triadic closure with a classical vector-sum-zero premise and avoids reading a local carrier triangle as a native Cell return.

## Exact discrete disjoint triad decomposition

Fix one Cell \`c\`, one common weight \`w\`, and \`3n\` **distinct named quanta** (their +/- signs are retained and arbitrary). Let \`a_i\` count quanta with unsigned axis \`i\`; thus \`a_i\in\mathbb N_0\`, \`sum_i a_i=3n\`. Only partitions into \`n\` unordered **disjoint** \`C_E\` hyperedges are considered; each hyperedge contains three different axes. Let \`D_n(a)\` be the exact number of such labelled partitions, with \`D_0(0)=1\`. Higher force populations that use overlapping hyperedges are a separately typed future model.

**Theorem BC1 (sharp existence).** For every \`n>=0\`,
\[
D_n(a)>0\quad\Longleftrightarrow\quad \max_{1\le i\le6}a_i\le n.
\]
Proof: every hyperedge uses any one axis at most once, giving necessity. For sufficiency, choose one quantum from each of the three most populated axes, form an allowed hyperedge, and recurse. At least three axes are positive when \`3n>0\` and \`max a_i\le n\`. At most three axes have population \`n\` because the total is \`3n\`; all such axes appear among the three chosen maxima. After deletion the remaining counts sum to \`3(n-1)\` and have maximum at most \`n-1\`. Induction starts at \`n=0\`. QED.

Let \`e_3(x_1,\ldots,x_6)=sum_{i<j<k}x_ix_jx_k\`.

**Theorem BC2 (exact named-source positive BRC multiplicity).**
\[
\boxed{D_n(a)=\frac{\prod_{i=1}^6 a_i!}{n!}\,[x_1^{a_1}\cdots x_6^{a_6}]\,e_3(x)^n.}
\]
Proof: the coefficient enumerates ordered sequences of \`n\` three-axis patterns. For each axis \`i\`, its \`a_i\` named force records are bijectively assigned to the \`a_i\` occurrences, in \`a_i!\` ways. Every unordered labelled partition has exactly \`n!\` orderings of its distinct hyperedges; division yields the formula. All terms and multiplicities are exact nonnegative integers. QED.

**Corollary BC3 (two saturated axes).** If \`a_i=a_j=n\` for two distinct axes, then for every distribution of the other \`n\` tokens over the remaining four axes,
\[
\boxed{D_n(a)=(n!)^2.}
\]
Every hyperedge must contain an \`i\` and a \`j\` quantum. Assign the \`n\` named \`j\` records bijectively to the \`n\` distinct \`i\` records (\`n!\` choices), then assign the remaining \`n\` distinct quantum records bijectively to those \`n\` pairs (\`n!\` choices). Each resulting triple has three distinct axes; no quotient remains because the \`i\` records already label the hyperedges. QED. In particular \`D_2(2,2,2,0,0,0)=4\`, \`D_3(3,3,3,0,0,0)=36\`; whereas \`D_2(1,1,1,1,1,1)=10\`.

## Exact two-visible-force -> hidden-third lift

Fix two **named** observed quanta \`u,v\` with different axes \`r,s\`, at the same Cell/weight. Denote \`e_i\` the standard count vector. Let \`L_n(a;u,v)\` count complete labelled partitions in which \`u,v\` belong to the same hyperedge.

**Theorem BC4 (exact resource-constrained lift).** For \`n>=1\`,
\[
\boxed{L_n(a;u,v)=\sum_{k\notin\{r,s\}}a_k\,
 D_{n-1}(a-e_r-e_s-e_k).}
\]
The set of **possible unsigned hidden axes** is exactly
\[
\boxed{J_{r,s}(a)=\{\,k\notin\{r,s\}:a_k>0,\quad
  \max_i(a_i-\delta_{ir}-\delta_{is}-\delta_{ik})\le n-1\,\}.}
\]
Proof: in a complete partition with \`u,v\` together, the unique third named quantum has an axis \`k\` distinct from \`r,s\`; there are exactly \`a_k\` choices. Removing the three records leaves an independent labelled disjoint partition of \`3(n-1)\` records counted by \`D_{n-1}\`. Cases are disjoint and exhaustive. The existence predicate is precisely BC1 applied to this remainder. QED.

**Sharp examples (six axes; indices below are 1-based):**
- \`n=2\`, \`a=(2,1,1,1,1,0)\`, observing one named axis-3 record and one named axis-4 record: candidate axes with remaining stock are 1,2,5, but **only hidden axis 1** can complete the population. There are two named third-quantum choices, and \`L_2=2\`.
- \`n=2\`, \`a=(2,2,1,1,0,0)\`, same observed axes 3,4: \`D_2(a)>0\`, yet \`J_{3,4}(a)=empty\` and \`L_2=0\`; a population can have valid triadic decompositions while this particular visible pair cannot belong to one triad.
- Under the fully occupied, symmetry-unbroken one-triad model, four hidden third axes remain possible for an ordered visible pair (and eight source tuples if first-leg order is also hidden), agreeing with R762BA/BB. Here the **resource ledger is extra visible state**, so resource-constrained fibers may shrink; there is no conflict with the original S6-stabilizer result.

**Observer consequence BC5.** The vector of six axis populations is sufficient to predict \`D_n(a)\` and \`L_n(a;u,v)\` when only the axes of \`u,v\` are queried. It is not sufficient for future named-Link membership queries: even with \`a=(1,1,1,1,1,1)\`, the same population count has ten distinguishable hyperedge partitions. The exact BRC family must retain the partition/Link provenance until the declared future observation factors through a coarser quotient.

## Reproduction and next scientific question

Run \`node research_notes/portable_direct/R762BC_NATIVE_TRIAD_PARTITION_VERIFY.js\` (no dependencies). The JSON evidence is an exact BigInt run: every one of 2521 six-axis count profiles for \`n<=3\` checked against an independent recursive enumeration of named partitions, all 13,860 possible pair-lift checks, 875 saturated-axis cases through \`n=4\`, and 1,260,720 coefficient permutation checks for \`S6\` at \`n=4\`. All assertions passed. The symbolic proofs cover all \`n\`; the finite test domain is explicit.

Next: obtain the authenticated native event/Port schema for \`TRIADIC_CLOSURE_E\`, determine admissible signed patterns and time ordering, and test whether V17 frame and V29 PASS/TRANSFER events act on the named hyperedge carrier; then check V39 loop transport preserves/rearranges the predicted \`D_n\` and \`J_{r,s}\` fibers. The current construction gives a testable candidate and a resource-sensitive observer obstruction while the genuine native incidence predicate remains to be established.
