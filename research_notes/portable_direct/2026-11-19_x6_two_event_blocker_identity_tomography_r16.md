# X6 R16 — Two-event blocker-source tomography in full signed Port vacancy semantics

Date: 2026-11-19 (Asia/Shanghai). Research line: RS-X6-NATIVE-TIME-DYNAMICS / TP2-91D4A7C2F63805BE21A3. **Conditional, exact author-side theorem; independent mathematical review NOT_REVIEWED.** Frozen P000 scientific source remains \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. This is **not** an admitted native TRIADIC_CLOSURE_E transition.

## New question and relation to earlier results

R12 and R15 show that next-step permitted source/Port events can conceal blocker identity, with hidden histories becoming distinguishable after two steps. R14B gives the exact first difference depth for two mobile sources. The new question is **when two steps actually reconstruct the complete labelled nearest-neighbour obstruction relation for any finite number of sources**, and what follows for finite-future state compression.

## Precise typed Boolean-BRC model

Choose an arbitrary anchor Cell of the six-native-axis spatial torsor; relative coordinates lie in \`Z^6\`. Fix a finite label set \`S\`, \`|S|=n\`, with an injective placement \`x:S→Z^6\`. The signed Port alphabet is \`D={+e_1,-e_1,...,+e_6,-e_6}\` (12 directions, not 12 dimensions). A labelled action \`(s,v)\` translates \`x_s\` to \`x_s+v\` if and only if that destination is vacant. All other sources stay put. \`L_h(x)\` comprises every successful *ordered and labelled* word of length ≤h, including the empty word. Rejected events are seen only by absence of successful words, not by a blocker oracle. Time here is event order, not physical duration. Boolean BRC branch support is exact for this declared observer, and no signed amplitudes are collapsed.

For each immediately blocked action \`(s,v)∉L_1(x)\`, there is a unique actual source \`b_x(s,v)∈S\\{s}\` at \`x_s+v\`. Write \`Mov_x(t)={u∈D:(t,u)∈L_1(x)}\`. Define the *two-event unblocking candidate set*, computed entirely from observed successful languages:
\`\`\`
T_x(s,v) = { t≠s : exists u∈D with (t,u)∈L_1(x)
                            and ((t,u),(s,v))∈L_2(x) }.
\`\`\`

## Theorem R16.1 — Exact blocker reconstruction with a movable blocker

For **every** finite injective six-component configuration \`x\` and every initially blocked \`(s,v)\`,
\`\`\`
T_x(s,v) = {b_x(s,v)}    if Mov_x(b_x(s,v)) is nonempty;
         = ∅             if Mov_x(b_x(s,v)) is empty.
\`\`\`

**Proof.** Denote by \`b\` the unique occupant of \`z=x_s+v\`. The first legal action \`(t,u)\` with \`t≠s\` changes only the occupied Cell of \`t\`. If \`t≠b\`, the occupant \`b\` of \`z\` does not move and the second \`(s,v)\` remains blocked. If \`t=b\` and \`(b,u)\` is legal, \`b\` leaves \`z\`; no other source moves into \`z\` during that single event, because only the moving \`b\` changes position and \`u≠0\`. Hence the second \`(s,v)\` is permitted. A legal \`b\` move exists precisely when \`Mov_x(b)\` is nonempty. Thus the candidate set is either exactly \`{b}\` or empty. QED.

This decodes blocker **identity**, not merely the Boolean next-step permission, using only two successful labelled events. No rejected-event identity is inserted by assumption. The criterion is local to each blocker and applies even when other sources cannot move.

## Theorem R16.2 — Two events recover the entire signed labelled adjacency graph

Assume **every** source has at least one legal outgoing signed Port move. Define the directed, Port-labelled nearest-neighbour graph \`G(x)\` by the edges
\`\`\`
s --v--> t   iff   x_t=x_s+v .
\`\`\`
Then \`G(x)\` is computable exactly from \`L_2(x)\` alone: \`L_1(x)\` identifies blocked \`(s,v)\`, and Theorem R16.1 identifies the unique \`t\` for each such edge.

If \`G(x)\` is also **connected as an undirected graph**, then \`L_2(x)\` reconstructs the full labelled placement \`x\` **up to a common translation**. In particular, for any two configurations \`x,y\` with connected nearest-neighbour graph and all sources mobile in both,
\`\`\`
L_2(x)=L_2(y)  iff  y_s=x_s+c for one c∈Z^6 and all s∈S.
\`\`\`
Consequently \`L_2(x)=L_2(y)\` implies \`L_h(x)=L_h(y)\` for **every finite h**, and for the complete unbounded finite-word language.

**Proof.** For every edge \`s --v--> t\`, the displacement is exactly \`x_t-x_s=v\`. Fix a root source \`r\`; along any graph path from \`r\` to \`s\` the sum of six-component signed edge increments equals \`x_s-x_r\`. Since the graph is connected, all relative positions are determined, with path-independent sums because the graph arose from an actual placement. Any two placements with this graph therefore differ by the same translation. Equality of \`L_2\` yields identical L1 and candidate sets; in the mobile class it yields identical graph. Conversely, common translation preserves every vacancy guard and hence every full source/Port future word. QED.

The hypothesis is checkable using \`L_1\` for mobility and the reconstructed graph for connectivity. If the graph is disconnected, the theorem still reconstructs each component internally but not its mutual offsets; distinct component separations can affect sufficiently distant future events. If a blocker has no legal first move, R16.1 reports an empty set, so its blocker identity is not reconstructed by the specified two-event unblocking test.

## Optimality and exact examples

**Sharpness at horizon one.** With four labelled sources on consecutive Cells \`0,e_1,2e_1,3e_1\`, fix endpoint labels 0 and 3; interchange the interior labels B,C. All four sources are mobile (they can move transversely, for example along \`+e_2\`) and their occupied adjacency graph is connected. All one-event source/Port permission patterns agree under this swap, so \`L_1\` is identical. The two-event word \`((B,+e_2),(0,+e_1))\` is legal exactly when B is the left interior neighbour. Thus \`L_2\` distinguishes them, and the two-event bound is universally sharp in the connected locally mobile class. This explicit R15 predecessor witness is reused, not claimed to be a new counterexample.

**Boundary witness for the mobility assumption.** Place label \`o\` at the anchor and 12 other labelled sources at each \`±e_j\` for \`j=1,..,6\`. All 12 neighbours of \`o\` are occupied, so \`Mov_x(o)=∅\`. For a shell source with inward blocked move into \`o\`, the candidate set \`T\` is empty exactly as Theorem R16.1 predicts. This is a statement about the two-event *reconstruction rule*, not a claim that the complete \`L_2\` cannot distinguish every possible alternative configuration.

## Exact reproducible checks

Companion checker: \`research_notes/portable_direct/x6_port_blocker_two_event_brc_verify.py\`. Result: \`research_notes/portable_direct/x6_port_blocker_two_event_brc_results.json\`.

The local checker independently generates every permitted word of length one or two with source label and one of all twelve signed axes. Tested **630** labelled placements: every ordered two- or three-source placement in a 3×3 selected-coordinate patch (all other four components explicitly zero, with all six signed directions still allowed); all permutations of labelled four-source line and square cells; and the six five-source line permutations with fixed endpoints. It checks the exact \`T\` formula, complete blocker graph, 210 connected configurations, and the sharp L1/L2 aliases. Totals: 1,440 blocked directed edges, 21,096 legal one-event words, and 747,064 legal two-event words across these repeated configurations. PASS on all assertions. The separate 13-source full signed shell witness tests the immobile-blocker boundary. These are finite checks, while the arbitrary-\`n\` result is proved symbolically above.

## Scientific status and next decisive question

This establishes an exact source-identity readout threshold for the **declared conditional vacancy-only X6 Boolean event model**. The six component coordinates remain native spatial chart-relative displacements; this work does not turn a two-coordinate test patch into an ontological two-dimensional plane, and time is independent of the spatial axes. It does not establish native force-stable three-action closure or a Link/Port admission predicate.

Next: (1) determine which actual admitted \`TRIADIC_CLOSURE_E\` source/Port transitions support a legal blocker-vacating first move and a legal vacated-target second move; (2) if the native gate forbids either, characterize the resulting residual; (3) for immobile enclosed sources, determine the smallest future depth at which blocker ownership becomes testable after neighbouring releases. Preserve R12/R15/R14B provenance and any existing owner/run boundaries; neither a GitHub commit nor an Activity checkpoint is a formal PROGRESS or independent review.
