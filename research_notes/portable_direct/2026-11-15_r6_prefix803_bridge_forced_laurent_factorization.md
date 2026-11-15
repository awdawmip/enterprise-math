# PREFIX-803 — Forced bridge transport and exact factorization of named-source Laurent fibers

Date: 2026-11-15. Research line: R6, independent portable BRC auxiliary integer-source model. Previous verified frontier: PREFIX-802 (2026-11-15), \`research_notes/portable_direct/2026-11-15_r6_prefix802_exact_memoized_laurent_suffix_fiber.md\`. Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Status: AUTHOR_PROVED / EXACT_FINITE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Model and question

Let \`G=(U,V,E)\` be a finite **named** bipartite multigraph (distinct parallel named edges are permitted) with integral edge capacities \`K_e >= 0\`, fixed nonnegative integer row demands \`R_u\` and column demands \`S_v\` of equal total, and signed integral observer vectors \`w_e in Z^d\`. A legal assignment has \`0 <= x_e <= K_e\`, row sums \`R_u\`, and column sums \`S_v\`. Its full multiplicity-preserving joint Laurent polynomial is

\`H_G(R,S;z) = sum_(legal named x) z^(sum_e w_e x_e)\`,

with \`H=0\` if there is no legal assignment. Each edge preserves its identity and weight; no factor-only projection is made.

Question after PREFIX-802: can the exact suffix calculation eliminate some residual edges **without branching**, even when the remaining graph still contains cycles?

## Theorem 803.1 — Every positive-capacity bridge is forced

Discard capacity-zero edges from the support graph, retaining their names with fixed value zero. Let \`e=(u,v)\` be a graph-theoretic bridge in the remaining support. Delete \`e\` and let \`A\` denote the connected vertex set containing its row endpoint \`u\`. Write

\`D_A = sum_(a in A intersect U) R_a - sum_(b in A intersect V) S_b\`.

Then **every** legal named source assignment has the single forced edge value

\`x_e = D_A\`.

In particular, if \`D_A < 0\` or \`D_A > K_e\`, the entire fiber is empty. Otherwise, put \`t=D_A\`, delete \`e\`, decrease \`R_u\` and \`S_v\` by \`t\`, and call the resulting graph and margins \`G-e,R',S'\`. There is a bijection of integer legal tables, preserving every remaining named edge, and the exact joint histogram identity is

\`H_G(R,S;z) = z^(t w_e) H_(G-e)(R',S';z)\`.

An isolated row/column vertex with positive residual demand makes the fiber empty.

**Proof.** Sum the row constraints in \`A\` and subtract the column constraints in \`A\`. Each internal named edge cancels once with itself. Since \`e\` is the unique crossing edge and points from the row endpoint inside \`A\` to the column endpoint outside \`A\`, the uncancelled sum is exactly \`x_e\`. This proves necessity and its capacity bound. After setting the forced value and subtracting it from the two endpoint demands, all other equations and integral box constraints are unchanged, establishing a two-sided bijection. The observer exponent decomposes additively as \`t w_e + sum_(f != e) w_f x_f\`. This proves the Laurent identity, including signed exponent vectors and multiplicities. QED.

## Theorem 803.2 — Iterated bridge peeling and cyclic-block factorization

Repeat Theorem 803.1 until no bridge remains, checking nonnegative margins and isolated vertices after each deletion. Let \`T\` be the peeled set, \`t_e\` its **uniquely determined** integer values, and let \`G_1,...,G_h\` be the nonempty connected components of the remaining graph (each component is bridgeless). The total named-source polynomial is identically zero if any forced value is out of capacity or any component has unequal residual row and column demand. Otherwise,

\`H_G(R,S;z) = z^(sum_(e in T) t_e w_e) product_(a=1)^h H_(G_a)(R_a,S_a;z)\`.

If the residual graph has no edges and all demands are zero, the empty product is \`1\`. The order of legal bridge peeling changes neither the resulting polynomial nor the set of original feasible assignments. This gives an exact preprocessing/recursive reduction for the PREFIX-802 memoized suffix recurrence, including states where a bridge appears **after a partial edge assignment**.

**Proof.** Apply the theorem 803.1 bijection inductively. Every removed edge is determined from the contemporaneous residual demands, and fixing these values preserves the complete solution set. After removing all bridges, disconnected components share no remaining edges or margin constraints. Thus their feasible assignments form a Cartesian product, and the multivariate observer monomial of a product assignment is the product of component monomials. The resulting Laurent polynomial is their product, times the forced-edge shift. Each legal peeling schedule is a composition of exact bijections to the same original fiber, establishing schedule independence of the final polynomial. QED.

**Operational scope.** Named positive-capacity support edges and exact residual margins are essential; different parallel named edges are not individually bridges unless deleting that specific edge disconnects its endpoints. A new dynamic edge or temporal operation changes the support and must be re-evaluated. This is a theorem about static integer source fibers, not an assertion of native Heartbeat/X6 event admission.

## Exact witness: two cyclic blocks linked by one forced provenance edge

On a 4 by 4 bipartite graph, retain the four unit-capacity edges of each K_(2,2) square on indices \`(0,1)x(0,1)\` and \`(2,3)x(2,3)\`, plus one unit-capacity bridge \`(1,2)\`. Set rows \`R=(1,2,1,1)\` and columns \`S=(1,1,2,1)\`. The bridge necessarily carries **one**, despite the two cyclic blocks individually having two legal permutation assignments. Observe with signed two-coordinate weights \`w_(0,0)=(1,0)\`, \`w_(2,2)=(0,1)\`, \`w_(1,2)=(-2,3)\`, all other weights zero. The precise joint histogram is

\`H(z_1,z_2)=z_1^(-2) z_2^3 (1+z_1)(1+z_2)\`

with four distinct exponent pairs \`(-2,3),(-2,4),(-1,3),(-1,4)\`, each multiplicity one. Thus a bridge changes the signed joint observer and does not erase either independent cyclic residual.

For the same capacity graph, margins \`R=(0,2,1,1)\`, \`S=(0,0,2,2)\` force bridge transport two, beyond its capacity one. The fiber is empty before branching.

## Reproducible exact finite verification

The independently enumerated source-table reference enumerates **every** named integer table for each capacity pattern and groups it by its actual row and column margins. It independently computes a two-signed-observer histogram. The bridge algorithm uses cut sums, capacity checks, recursively forced bridge deletion, connected-component Laurent factorization and free branching where cycles remain. Results are compared as entire integer-coefficient exponent dictionaries, plus coefficient totals, for **all attainable fibers**.

- 2x2, all edge capacities 0..2: 81 patterns, 1,215 fibers, 1,296 complete named tables; 2,430 exact assertions.
- 2x3, all edge capacities 0..2: 729 patterns, 39,366 fibers, 46,656 complete named tables; 78,732 assertions.
- 3x3, all edge capacities 0..1: 512 patterns, 17,840 fibers, 19,683 complete named tables; 35,680 assertions.
- Extra linked 4x4 example: four exact checks on joint histogram, multiplicity, bridge/factorization exercise and overflow infeasibility.

Totals: **1,322** capacity patterns, **58,421** attainable margin fibers, **67,635** complete named tables and **116,846** exact assertions, all passed. The bridge-aware solver encountered 341,199 forced-bridge calculation events and 71,208 non-forced branching nodes across those fibers. These are algorithmic recursion events, not distinct graph edges or a runtime comparison.

Reproduce with Python 3 standard library:

\`\`\`sh
python PREFIX803_R6_BRIDGE_FACTOR_CHECK.py > PREFIX803_R6_BRIDGE_FACTOR_RESULTS.json
\`\`\`

The verifier has no random sampling and uses arbitrary-precision integers for counts and exact signed integer tuples for Laurent exponents. General validity is established by the proofs, not finite enumeration.

## Provenance, limitations and next discriminator

Reused verified mathematical inputs: PREFIX-795 forest/cycle residual distinction; PREFIX-796 finite-capacity residual graphs; PREFIX-799 chord parametrization; PREFIX-800/801 Hall feasibility and incremental certificates; PREFIX-802 exact signed multivariate suffix recursion. P000 and ACTIVE worldview remain unchanged. This independent auxiliary construction preserves the full named joint count in its declared observer scope; a native X6 Cell/Link/Port and ordered-event bridge correspondence is a separate typed mapping problem. Shared task \`RS-X6-NATIVE-TIME-DYNAMICS\` is not claimed by this note.

Next: compare bridge-first, component-first, incremental-Hall and unmodified suffix memoization on separately specified sparse/dense capacity ensembles, measuring exact polynomial support size, peak memory, wall time and threshold where graph-reduction overhead wins. Then test whether specific native signed-Port provenance and legal event transitions truly induce bridge-like forced transport, without replacing native event identity by a static count projection.

Artifacts:
- \`research_notes/portable_direct/PREFIX803_R6_BRIDGE_FACTOR_CHECK.py\`
- \`research_notes/portable_direct/PREFIX803_R6_BRIDGE_FACTOR_RESULTS.json\`
