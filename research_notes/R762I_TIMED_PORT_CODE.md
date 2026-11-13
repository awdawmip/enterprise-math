# R762I — Lossless time-ordered port code for shortest X6 three-port loops

Date: 2026-11-13 Asia/Shanghai. Status: **AUTHOR-SIDE EXACT PROOF + COMPUTATION / NOT_REVIEWED**. Mother Task RS-X6-TRIADIC-CLOSURE-DYNAMICS; immutable publication TP2-8B7E13C5904A2D6F1142. Scientific input remains pinned to awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Builds directly on R762H PR #2288 (24 shortest source-distinct signed-port path traces).

## 1. Exact model and theorem

Fix any chart-relative Cell origin in the six-dimensional native X6 signed-axis Cell torsor, three distinct signed unit directions u_a, u_b, u_c, and their three neighboring target Cells. Let W be the source-distinct *six-step sequential coordinate walks* that begin and end at this Cell and visit each target. The step index t ∈ {0,...,6} records sequence order, not independently measured physical heartbeat time.

Define o(γ) as the permutation of the three **named** ports in first-visit order. Define the two-bit return signature r(γ)=(r_2,r_4), where r_t=1 exactly when the walk has returned to the starting Cell at step t. The chosen signed ports and starting Cell are fixed as observer context; physical force-source and field labels are not part of this graph carrier.

**Theorem.** For each of all C(6,3)·2³=160 signed target configurations:

1. The three target visits occur at step indices **1,3,5**, in a source-dependent order. A single sequential six-step coordinate walk never visits all three targets at the same step index.
2. The map γ↦(o(γ),r(γ)) is an exact bijection W ≅ S₃×{0,1}². Each of the six visit orders and four return patterns occurs exactly once together, giving 24 traces.
3. Given signed port context, (o,r) recovers the entire ordered signed six-step trace. Since |W|=24, the minimal *fixed-width* exact path code is ceil(log₂24)=**5 bits**. Given the full first-visit order alone, exactly two more return bits are needed. Given the chirality χ(o) and the two return flags, each observation fiber has exactly three cyclic source orders, so two more bits are needed.
4. The rooted signed edge-current j_X6 together with full first-visit order o is also injective on W. This sharpens R762H's (j_X6,χ) observer, whose largest path fiber has size three.

## 2. Constructive proof (valid for every signed port choice)

Use independent signed-axis reflections and index relabeling as a **coordinate graph-counting isomorphism**, not an assertion about the full native rotation group. The target neighbors become weight-one vertices {a},{b},{c} of the 3-cube. A shortest closed walk visiting them uses each of ±e_a, ±e_b, ±e_c exactly once; no other axis occurs. The walker therefore stays in this cube.

The cube is bipartite: each weight-one target is visited only at odd step index. Among the six steps, the only possible odd visit times are 1,3,5. Since each of the three distinct targets must be visited, these are precisely its three distinct first visits, each appearing exactly once.

Now fix a named visit order (a,b,c), and write 0 for the root. The walk must have states

0 → {a} → X₂ → {b} → X₄ → {c} → 0.

The step-2 state must be adjacent to *both* singleton Cells {a} and {b}, which in the cube leaves exactly the two possibilities 0 or {a,b}. Similarly, X₄ is 0 or {b,c}. The two choices are independent: every resulting seven-Cell chain is a valid primitive signed-axis six-step closed walk. This yields a constructive inverse:

- (r₂,r₄)=(1,1): X₂=0 and X₄=0, three independent spoke returns;
- (1,0): X₂=0 and X₄={b,c}, early spoke and later square;
- (0,1): X₂={a,b} and X₄=0, early square and later spoke;
- (0,0): X₂={a,b} and X₄={b,c}, no intermediate root return.

There are exactly 6·4=24 walks, proving a product factorization by named visit order and return choices. Every signed coordinate step in the constructed sequence is primitive, and the three omitted native X6 axes have zero *step occurrences* in a shortest witness; they remain native axes of the ambient six-dimensional space.

For fixed order, the four return patterns are distinct and all occur, establishing the exact conditional lower/upper bound of two fixed-width bits. For fixed return pattern and parity χ, three cyclic permutations of named ports share the same readout. Therefore the eight (χ,r) fibers have exactly three members; a two-bit cyclic-order repair is necessary and sufficient. Overall 24 distinct traces require ≥5 fixed-width bits, and the named S₃ order index (3 bits) plus r (2 bits) attains it.

The R762H rooted edge-current census supplies another exact certificate: six three-spoke paths have zero current but six different first-visit orders; six signed square currents each have exactly two paths, with different orders (spoke earlier/later); the six hexagon currents are all different. Accordingly (j_X6,o) has 24 singleton fibers. The current is a path-graph observation, not an asserted V39 physical current.

## 3. Interface consequence for TRIADIC_CLOSURE_E

A six-step *single sequential coordinate walk* has its three target visits at distinct step indices. Such a trace alone cannot assert a single same-step three-source force event. P000's admissible equal-quantum triadic closure is a separately typed **force incidence relation**, so a native event may require multiple concurrent carriers/channels or an internal-state synchronization predicate. A legal force-event-to-coordinate-path map must specify the source assignment, time relation and transition/admission law rather than identify a three-port sequential visitation with simultaneous primitive-force balance.

The exact (o,r) compression is safe for any future computation whose complete relevant input is the six-step ordered spatial trace on this fixed domain: decode the trace first, then perform the original computation. It does not erase independent force-source, field, link, V29 ledger, V39 frame, phase or physical-time data. Step number is operation order, not demonstrated physical heartbeat elapsed time. Source branches and provenance are retained via the bijection, consistent with the Joint Relation Observer Preservation constraint.

## 4. Reproducibility

Full Python 3 standard-library checker: research_notes/R762I_VERIFY.py. Expected exact output: research_notes/R762I_EVIDENCE.json. It examines all 6!=720 balanced three-axis signed-letter words at the canonical positive-sign configuration, filters precisely 24 port-covering traces, verifies step times [1,3,5], proves the inverse reconstruction by exhaustive check, calculates the 24 singleton order-return fibers, all eight size-three chirality-return fibers, and the independent (j_X6,o) injectivity check. It embeds all 24 traces across C(6,3)·2³=160 signed X6 configurations and checks their source distinctness. This is finite exact integer/symbolic enumeration and the independent constructive proof above applies to all 160 signed configurations; no floating-point, pi, trig or native physical BRC propagation is used.

## 5. Next unfinished scientific question

Obtain an explicit source-legal TRIADIC_CLOSURE_E Cell/Link/Port *force* incidence with three named equal-quantum sources and a typed temporal relation. Test which source states, if any, permit a valid mapping to one of the 24 shortest coordinate witnesses; if one exists, check whether the event can repeat and whether second-step V29 PASS/TRANSFER and V39 based-loop transport obey their actual source contracts. Preserve missing field/source context and every path branch until observer safety is established. This study does not change the frozen P000 or ACTIVE worldview, grant CLAIM, publish a formal Result or establish independent Driver review.

**Source trail:** R762H PR #2288; frozen Foundation definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md and definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md.
