# R762H — Exact shortest native X6 Cell-loop witnesses for three signed ports

Date: 2026-11-13 Asia/Shanghai. Status: **AUTHOR-SIDE EXACT CONSTRUCTION / NOT_REVIEWED**. Parent: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\` / publication \`TP2-8B7E13C5904A2D6F1142\`. Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Inherits P000 signed Cell torsor, six-axis native steps and BRC provenance. This contribution introduces a geometric **candidate incidence witness**, not a newly admitted physical TRIADIC_CLOSURE_E transition.

## 1. Exact question and graph

Fix a chart-relative X6 Cell \`c\` in the affine \`Z^6\` Cell torsor. Pick three distinct axes \`i,j,k\` and signs \`σ_i,σ_j,σ_k ∈ {+1,-1}\`. The signed adjacent ports are \`c+σ_i e_i\`, \`c+σ_j e_j\`, \`c+σ_k e_k\`, each with its own source label and positive force quantum when separately supplied. A *port-covering closed coordinate witness* is an ordered sequence of signed primitive axis-adjacency steps, starting and ending at \`c\` and visiting all three designated neighbor Cells. This is a **path incidence condition**, not a zero-vector definition of force balance. The prospective triadic force closure remains separately typed as \`TRIADIC_CLOSURE_E\`, consistent with P000's canonical equal-quantum triads.

The graph observer is \`(chosen c, three signed ports, ordered trace, rooted oriented-edge current j_X6)\`. Axes not selected remain present in native X6 and carry zero step counts for the shortest witnesses; this does not identify the selected three-axis coordinate observer with the whole world.

## 2. Shortest witness theorem and exact branch count

**Theorem.** For every choice of three distinct native axes and each choice of the three port signs:

1. Any port-covering closed coordinate path has length **at least six**.
2. Exactly **24** paths attain length six. Every such path has precisely one \`+e_a\` and one \`-e_a\` step for each selected axis, and no step on an unselected axis.
3. The 24 shortest witnesses split into **6 three-spoke excursions, 12 square-plus-spoke loops, and 6 no-intermediate-return hexagonal loops**, distinguished by positive return times to the original Cell.
4. All 24 traces are source-distinct; an exact full-path/BRC observer has 24 branches of unit integer multiplicity, while rooted edge-current readout has exactly **13 values** with fiber sizes: one fiber of size 6, six fibers of size 2, and six singleton fibers.

**Proof of minimum.** Each designated neighbor has a nonzero displacement on a different coordinate. To reach it along native coordinate edges and return to c, the path must contain at least one step of each sign on that coordinate. Thus all six \`±e_i, ±e_j, ±e_k\` letters are required, giving length at least six. Equality forces these six letters to occur exactly once and forbids all other letters. There are exactly \`6!=720\` balanced three-axis length-six words before the visitation filter.

**Proof of 24.** Reflect the three selected coordinate signs only as a *graph-counting isomorphism* and relabel the axes, reducing the enumeration to three positive neighbor ports of the 3-cube. During a six-letter path each coordinate lies in \`{0,1}\`: it opens once then closes once whenever that positive neighbor is visited. All three weight-one vertices of the cube must be visited. Intermediate returns to the origin can occur at t=2 or t=4 only, producing three exhaustive cases:
- returns at t=2 and t=4: three independent two-step out-and-back spokes, in \`3!=6\` orders;
- exactly one intermediate return (at t=2 or 4): one spoke on a chosen axis and one four-step square visiting the other two designated ports. There are \`3·2·2=12\` possibilities (spoke axis, order of components, square orientation);
- no intermediate return: the walk visits the three weight-one vertices without returning to zero and has level pattern \`0,1,2,1,2,1,0\`. Its three neighbor-visitation orders determine its entire six-step path, yielding \`3!=6\` hexagonal walks.

Hence \`6+12+6=24\`. The attached independent six-letter-mask dynamic program and complete 720-word enumerator verify the classification for all \`binom(6,3)·2^3=160\` signed port choices.

## 3. BRC edge-current fibers and information repair

Define \`j_X6(γ)\` on each positively oriented directed edge \`(x,x+e_a)\` as (number of forward traversals minus number of reverse traversals), retaining the chosen Cell anchor. All six star excursions have \`j_X6=0\`. For each of the three pairs of axes, the square has two circulation signs; its current is unchanged by whether its separate spoke happens before or after it, so these make **six double fibers**. Each of the six hexagonal paths has a distinct nonzero six-edge current and forms a singleton fiber. The resulting exact census is \`1·6+6·2+6·1=24\` over 13 j-values.

For the observer requiring **lossless recovery of the ordered six-step path** from the fixed signed-port configuration plus \`j_X6\`, the largest fiber has size six. A fixed-width conditional repair code therefore needs and admits \`ceil(log2 6)=3 bits\`; the square currents need one bit and singleton currents none. This is an observer-specific lower bound, not a universal force-state bit requirement. It exhibits a concrete BRC distinction that is invisible even to rooted edge current. The full ordered path/source identities remain available for future native event or ledger queries.

For a **proposed** directed three-port incidence event with an independently recorded cyclic orientation (two choices), there are \`160·2·24=7680\` orientation/witness pairs over all signed port configurations and shortest traces. These are candidate data objects, not 7,680 admitted force events or actual V29/V39 updates. Within the currently verified unsigned S6 axis-permutation skeleton the counts are invariant; coordinate sign reflection here serves only as a graph enumeration bijection, with no assertion about the full physical rotation group.

## 4. Verification and source correspondence

Exact Python 3 standard-library verifier: \`research_notes/R762H_VERIFY.py\`. Its JSON output: \`research_notes/R762H_EVIDENCE.json\`. The checker enumerates 160×720 balanced ordered words, calculates the selected-port visits and rooted integer edge currents, and independently checks 24 using mask/count DP rather than permutation enumeration. Verification uses only exact integers and tuples; no floating-point or approximate assumptions. Proof of the general 160-configuration count is the coordinate relabelling/reflection bijection plus the above exhaustive 3-axis classification.

Source foundation: \`definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md\` and \`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md\` at frozen commit. Predecessors: R762G PR #2281 (adversarial reserve of **candidate port permutations**) and R740 PR #2142 (full six-step rooted edge-current BRC census). This result narrows the open native interface by providing a **shortest explicit signed Cell/Link/Port incidence carrier** and a complete loss-of-order witness.

## 5. Next scientific test

Select one P000-legal equal-quantum signed triad with an **independently verified** true \`TRIADIC_CLOSURE_E\` predicate. Specify whether one of the 24 coordinate witness loops constitutes a valid native triadic *force* event, and check the first and repeated events against actual Cell/Link/Port incidence, V29 PASS/TRANSFER event increments and V39 based-loop current/transport. Then test whether the 13 j-fibers and their BRC repair coordinates remain observer-safe under those true updates. The current mathematical construction alone does not supply that event-selection law.

No P000/ACTIVE worldview modification, scientific-pin rebase, CLAIM takeover, official Result freeze or Driver acceptance is asserted.


## 6. Strengthening — first-visit chirality and sharper source-order repair

Let \`o(γ)\` be the permutation of the three named signed ports in the order of **first occurrence** along a shortest covering trace. Its cyclic orientation is the parity \`χ(γ)∈{+1,-1}\` relative to a declared reference ordering. Cyclic relabeling preserves parity, while an odd renaming changes the parity covariantly: no global preferred chirality is imposed.

**Exact theorem.** Each of the six first-visit permutations occurs in exactly **four** of the 24 shortest paths; the two cyclic orientations therefore have **12 paths each**. If the candidate force-event orientation must equal this path chirality, there are \`160·24=3840\` compatible orientation/witness pairs, rather than \`160·2·24=7680\` freely paired objects.

For either fixed orientation, the joint readout \`(j_X6,χ)\` has **seven** values with fibers of sizes \`(3,2,2,2,1,1,1)\`. Consequently, given fixed signed ports and this joint readout, complete ordered-path recovery requires precisely \`ceil(log2 3)=2\` worst-fiber fixed-width repair bits, improving the current-only 3-bit bound.

**Proof.** The action of S3 on the three selected port labels permutes the 24 path set and is transitive on the six possible first-visit orders; each occurs \`24/6=4\` times. Zero current consists of six star loops with all six orders (three of each parity). Each size-two square-current fiber differs only by whether the separate spoke appears before or after the square; these two first-visit orders differ by a three-cycle and have the same parity. The six hex currents are singleton. The parity involution interchanges the positive and negative halves of the square/hex fibers. Thus for either parity: one zero-current fiber of size three, three square fibers of size two and three hex singleton fibers. The updated verifier checks this complete census for all 160 signed port configurations.

This supplies an explicit native *coordinate path-order* representation for R761's two candidate cyclic port orientations. Matching this coordinate chirality to a true force event remains dependent on an actual TRIADIC_CLOSURE_E incidence/update rule.
