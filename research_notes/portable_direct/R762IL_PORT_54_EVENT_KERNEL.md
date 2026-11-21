# R762IL — 54-event witness kernel for the six-axis composite Port Euler observer

Date: 2026-11-22 (Asia/Shanghai). **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

## Provenance and precise scope

Frozen scientific task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, scientific pin \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Main predecessor: **R762IK**, research commit \`a8d8488b137cd090dbde3d3c07c3d5ffa6a9c57c\`, [source proof](https://github.com/awdawmip/enterprise-math/blob/a8d8488b137cd090dbde3d3c07c3d5ffa6a9c57c/research_notes/portable_direct/R762IK_PORT_55_EVENT_KERNEL.md), [exact checker](https://github.com/awdawmip/enterprise-math/blob/a8d8488b137cd090dbde3d3c07c3d5ffa6a9c57c/research_notes/portable_direct/R762IK_CHECK.py), [component scan](https://github.com/awdawmip/enterprise-math/blob/a8d8488b137cd090dbde3d3c07c3d5ffa6a9c57c/research_notes/portable_direct/R762IK_COMPONENT_SCAN.cpp).

Let \(\mathcal P=\binom{[6]}2\) be the 15 Port vertices and \(\mathcal S=\binom{[6]}3\) the 20 support types. A support \(S=\{a,b,c\}\) permits a named event on one edge of the triangle with vertices \(ab,ac,bc\). A legal closed Port history is an Euler tour through a connected even-degree assigned multigraph; its nonisolated vertex set \(V\) and start \(p\in V\) are part of the claimed observer.

## New theorem — 54 events

For every nonzero support histogram \(n=(n_S)_{S\in\mathcal S}\), every legal Euler realization of \(n\) with active vertex set \(V\), and every designated starting Port \(p\in V\), there is another histogram \(h\le n\) and a legal Euler realization of \(h\) such that

\[
\boxed{\sum_{S\in\mathcal S}h_S\le54}
\]

and simultaneously \(\{S:h_S>0\}=\{S:n_S>0\}\), \(h_S\equiv n_S\pmod 2\) for every \(S\), and the active vertex set and start \(p\) are exactly \(V,p\). Therefore all deleted events can be reinstated as same-support pairs on an occupied permitted edge, preserving Port-Euler existence. The witness is realization-dependent, not a fixed componentwise truncation. This asserts the composite Port Euler observer only; no native P000 time, force, rotation or signed Cell lift is claimed.

## Proof: all remaining cases in R762IK

Invoke the already established R762IK pair-removal terminal reduction. It preserves support presence, all support parities and the original active Port set, reduces every support count to at most four, and calls a support **critical four** if its surviving four events occupy two different simple-graph bridge edges, twice each. Write \(k\) for the number of critical four-supports and \(T\) for the number of three-count supports. The established bound for \(k\ge1\) is \(40+T+2k\), with table (for \(k=1,\ldots,7\)) \(55,54,53,52,52,53,54\). Thus only the equality case \(k=1,T=13\), with all 20 types present (one count-four, thirteen count-three, six count-two), could exceed 54. When \(k=0\), each support count is at most three, so only terminal histograms of total at least 55 need attention.

### A. The \(k=1,T=13\), 55-event extremum always has a 53-event replacement

Delete the two critical support's distinct underlying Port bridge edges. This leaves exactly three connected components; all thirteen three-count support triangles lie within these components. Let \(F\subset\mathcal S\) denote their thirteen support types and \(G(F)\) the union of the corresponding *full allowed triangles* on all 15 Port vertices, with isolated unused vertices retained. Thus \(G(F)\) has at least three components.

Exhaustive integer DSU calculation over the entire \(\binom{20}{13}=77,520\) finite domain establishes:

* Exactly **60** thirteen-support subsets give three components; all remaining 77,460 give one or two.
* Each of those 60 has exact component size multiset **(1,1,13)**. The two singleton pair-Ports intersect in one axis.
* Every such subset consists of precisely the thirteen supports avoiding both singleton Port vertices. There are \(6\binom52=60\) unordered pairs of intersecting pair-Ports.

Consequently, the original 55-event terminal history has two singleton vertices \(u,v\) and a connected 13-Port core. Its critical support connects the three original components by two bridge edges, and necessarily contains both \(u,v\) as pair-Port vertices. There are six further support types outside \(F\), three incident to \(u\) and three incident to \(v\); each is count-two. (The critical support is the seventh outside \(F\).)

For the replacement, assign each of the thirteen count-three supports to its entire three-edge triangle. Assign all seven other supports **two copies of one permitted Port edge** each. Choose, among the noncritical supports, one doubled edge from \(u\) into the 13-Port core and a different support's doubled edge from \(v\) into the core. Choose arbitrary permitted edges for the remaining five doubled supports. The resulting graph is connected, all 15 Ports are active and all vertex degrees are even. Its counts are thirteen threes and seven twos, hence exactly \(13\cdot3+7\cdot2=53\) events. Support presence/parity and active Ports match the original extremum. The checker also exhaustively constructs/verifies this witness for all 60 possible critical configurations.

### B. The \(k=0\), 55-event boundary

Regard 20 three-count supports (60 events) as the baseline. Let \(U\) be count-one, \(E\) count-two and \(M\) missing types, and let all other supports have count three. A total of 55 means the deficit \(2|U|+|E|+3|M|=5\). The exhaustive five families are:

| Family | Histogram count | \(S_6\) orbit count | Verified output |
|---|---:|---:|---:|
| E5 | 15,504 | 43 | 53 events |
| U1E3 | 19,380 | 48 | 53 events |
| U2E1 | 3,420 | 12 | 53 events |
| M1E2 | 3,420 | 12 | 53 events |
| M1U1 | 380 | 3 | 53 events |
| **Total** | **42,104** | **118** | **53 events** |

The accompanying standard-library integer checker constructs the exact 118 orbits under all 720 axis permutations. Each representative is given an explicit supportwise edge-multiset witness. The checker validates exact support counts, even degree at every Port, graph connectivity and all 15 active Ports. Every other histogram is its corresponding axis-permutation image.

There is an active-set subtlety. Each Port lies in exactly four support triangles, so only E5 and U1E3 can permit a 14-active-Port original terminal graph: all four incident support types must be non-three. The checker additionally constructs 53-event, exactly-14-active-Port witnesses for every such case: E5 has \(15\cdot16=240\) port/extra-type choices, and U1E3 has \(15\cdot4=60\), **300 independent exact checks** in all. No 55-event terminal histogram can omit two Ports, since five non-three types cannot cover the incident supports of two distinct Ports. Thus the original active Port set is preserved.

### C. The \(k=0\), 56–60-event cases

R762IK already establishes 54-event witnesses for the seven even-length high-count families T20, E2, E4, U1, U2, U1E2 and M1E1. The only cases for which its constructed witness had length 55 are the four odd-length families E1, E3, U1E1 and M1. We now construct 53-event witnesses for **all 1,560** such histograms using their **12** complete \(S_6\) orbits:

| Family | Histograms | Orbits | Verified output |
|---|---:|---:|---:|
| E1 | 20 | 1 | 53 |
| E3 | 1,140 | 7 | 53 |
| U1E1 | 380 | 3 | 53 |
| M1 | 20 | 1 | 53 |

At least seventeen count-three supports remain in each family, so all original terminal realizations have 15 active Ports. Each orbit representative is independently checked by the finite exact witness verifier.

Cases with \(k\ge2\) were already bounded by 54. Cases with \(k=1\) are now at most 54, including their unique 55-event extremum. Cases with \(k=0\) of length at most54 need no change, and all larger ones have a 54-or-smaller replacement. This exhausts the terminal reductions, proving the theorem for arbitrary original history length.

## Certificate algorithm and reproducibility

The source \`R762IL_CHECK.py\` uses only Python 3 standard-library integer operations. For odd-support replacements, it chooses target three-count triangles to shorten from three events to one. The resulting two-Port boundary is routed through two edges belonging to remaining full-triangle supports; each helper triangle uses an exact \(\mathbb F_2^{15}\) XOR boundary mask and converts (1,1,1) to a (1,2,0) allocation when needed. The program then explicitly checks all support counts, degree parities, connectivity and active vertex sets; this is an exact Port boundary certificate, not a floating-point experiment or a claim about positive BRC masses.

Run from the repository root:

\`\`\`bash
python3 research_notes/portable_direct/R762IL_CHECK.py
\`\`\`

Author-run exact result, 2026-11-22: \`PASS R762IL\`. It checks 42,104 length-55 histograms represented by 118 axis orbits, 1,560 odd high-count histograms represented by 12 orbits, all 300 possible 14-active-Port exceptions and all 77,520 thirteen-support masks with 60 three-component / critical cases. The earlier R762IK exact finite certificates are reused for the terminal reduction and even high-count families, at the immutable predecessor revision above.

**Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. The finite-domain theorem is conditional on the cited earlier structural reduction, whose independent mathematical review remains outstanding. No formal Result, native PROGRESS, P000 promotion or physical interpretation is asserted.

**Next research:** Test whether 53 events suffice globally, particularly the \(k=2\) or \(k=7\) terminal upper-bound 54 cases and \(k=0\) even 54-event families; alternatively construct a histogram requiring exactly 54. Separately build a histogram-only algorithm returning a Port Euler realization or a verifiable infeasibility certificate; preserve the separate type-faithful P000 triadic/time/rotation lift obligation.
