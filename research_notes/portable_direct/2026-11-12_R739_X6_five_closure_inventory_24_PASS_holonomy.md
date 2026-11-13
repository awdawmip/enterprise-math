# R739 — Five-certificate X6 triad channel, 24-PASS fixed-ledger separation and 180-member S6 orbit

Date: 2026-11-12 (Asia/Shanghai). Classification: author-side exact combinatorial construction and finite verification; independent research review pending.

Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS; immutable publication TP2-8B7E13C5904A2D6F1142. Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, specifically p000_reality_foundation.json; definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md; definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md; and definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json. This study does not re-pin scientific inputs. Additional declared auxiliary interface: V29 nonnegative PASS event grammar, awdawmip/enterprise-math@30fb16d39465708fd1b54c70a58d06ad20f310f8, research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md. Prior derived material: R730/731/731b (masks and PASS codes), R735/736 (positive rooted return monoid and fixed-count census), R737 (conditional triad frame). Contemporary R738 studies a different signed path-observer question.

## Typed model and explicit conditional assumption

Fix one Cell C in the affine signed X6 torsor over Z^6. In a reservoir select five distinctly sourced, nonzero signed-axis unit force tokens

Q_i=(Cell=C,direction=+E_i,quantum=1,source=i), i=0,...,4.

The six-dimensional native space remains intact; the unused sixth native axis is not removed. At any instant **exactly three** of these tokens are active. For an inventory H of unordered three-subsets of {0,...,4}, assume that each active triad T={i,j,k} in H has its own explicit, admissible P000 typed incidence witness

Close(C;T) := TRIADIC_CLOSURE_E(C;Q_i,Q_j,Q_k).

The triples are equal-quantum and pairwise PERP_E at native angle 120°, but *arbitrary* triples are not presumed to close solely from their names. The five selected certificates are declared candidate local premises. Inactive reservoir tokens do not constitute simultaneous extra primitive force actions.

Each macro-step consists of (i) two genuine, ordered, off-diagonal V29 PASS count events at C using **four local channel ports** 0..3; then (ii) a declared simultaneous replacement of the active closure triad S by T, with V17 source-slot transfer. Between the first and second PASS the old triad remains active. The new triad is admitted only if T is in H. Port labels are not spatial directions; the macro-step's force-triad switch is an additional **candidate coupling**, not an update already entailed by V29's count-event grammar. The model retains its chosen Cell, active triad, source/slot map, previous vertex, event-boundary phase, ordered event word and positive BRC branch provenance.

## Existing exact carrier and four-port code

The ten three-subsets of five formal labels, lexicographically, are

012, 013, 014, 023, 024, 034, 123, 124, 134, 234.

The ordered universe consists of all 60 pairs S>T sharing two labels, enumerated first by S then T. Select the fifteen arcs indicated by the binary masks

A=211733226574, B=5363347296468.

For the fifteen selected arcs of each network, index i=0,...,14 in this induced order. Enumerate all 12 off-diagonal four-port symbols PASS(a>b) lexicographically, indexed 0,...,11. Encode the arc index i by two ordered PASS symbols

j(i)=(floor(i/12), i mod 12).

These fifteen codewords are distinct. Each authentic PASS increment adds +1 to exactly one nonnegative M[a,b]; the 12-symbol pair boundary permits source-arc recovery. A legal m-arc macro-history is thereby lifted to exactly 2m PASS events, and

ΔΓ = Σ_(a,b) ΔM[a,b] = 2m.

A nonempty history has a growing native V29 cumulative grade. The full ordered PASS stream retains the arcs and their provenance, whereas final M forgets serialization order.

## R739-A: exact minimal five-closure inventory

A complete root-012 three-step cyclic-nonbacktracking return has shape 012>U>V>012 with U,V among the nine non-root triads. Exhaustive checking of all 9×9 ordered choices against the exact fifteen-arc masks yields precisely these three returns per carrier:

| Carrier | I: identity | P: first transposition | Q: second transposition |
|---|---|---|---|
| A | 012>014>013>012 (012) | 012>023>013>012 (021) | 012>023>123>012 (102) |
| B | 012>123>124>012 (012) | 012>023>013>012 (021) | 012>123>013>012 (210) |

Parenthesized triples are the V17 named holonomies. The three-root-return generators are unique **in the fixed directed carriers**. Their first non-root vertices and last non-root vertices are disjoint in both networks, so every pair of returns, including repetitions and seams, concatenates without cyclic backtracking. In particular every word in {I,P,Q}* has an authentic positive-BRC rooted cyclic-nonbacktracking source history.

**Theorem.** Among closure inventories supporting exactly these three distinct rooted three-step I/P/Q generator types at the chosen Cell, the minimum number of certified active triads is five. The unique minimal inventories are

H_A = {012,013,014,023,123};
H_B = {012,013,023,123,124}.

**Proof.** Each of the three generator loops must be present, since the complete finite root-loop enumeration has exactly one loop of each required relation. Supporting a loop requires the root and its two intermediate active-triad certificates. The union of these vertices is exactly H_A or H_B, and has cardinality five. Hence five are necessary. They are sufficient because every vertex of every generator and of every concatenation lies in that same union. This is a sharp finite-domain statement for the two given carrier masks and this three-step generator family, not a universal minimum for all X6 dynamics. ∎

## R739-B: three distinct relation outcomes after exactly 24 authentic PASS events, with identical native M

Take the four-generator words W0=PPQQ, W1=PQPQ, W2=QPQP. Each is a legal rooted cyclic-nonbacktracking history of twelve abstract arcs. The R731b code executes twenty-four authentic same-Cell V29 PASS events, with initial M=0 and Rin=Rout=0 and final ΔΓ=24. Within a given carrier, all three words have the same two-P/two-Q generator multiset, thus the same total counter increments. The complete final native four-port passage matrices computed directly from the code are

M_A =
[ [0,10,8,0],
  [2, 0,0,0],
  [0, 2,0,2],
  [0, 0,0,0] ]

M_B =
[ [0,14,2,4],
  [0, 0,0,0],
  [2, 0,0,0],
  [0, 0,2,0] ].

Both matrices have entry sum 24 and every entry is a nonnegative integer.

| Fixed-count history | A terminal relation | B terminal relation |
|---|---|---|
| PPQQ | 012 | 012 |
| PQPQ | 120 | 201 |
| QPQP | 201 | 120 |

**Proof.** On each abstract arc, the two native PASS symbols have a uniquely decodable index. V17 moves the source slot of the leaving label to the entering label. Direct transport along the 12 arcs gives the table, equivalently ordered multiplication of P and Q as two distinct transpositions of S3. The terminal ledger is unchanged by reordering the same P/P/Q/Q blocks, since PASS increments are additive. Every intermediate active triad is certified by the five-element inventory, and the prior-nonbacktracking rule holds at all seams. Therefore all three named holonomies are genuinely supported by complete ordered PASS event traces and retain positive BRC branch identity in the explicitly declared coupled model. ∎

This supplies a minimal fixed-inventory witness that final V29 PASS counts are not sufficient to recover an observable named ordered-triad relation. The previously established three-valued online k∈Z/3Z residual is sufficient for this generator family when full edge/port counts also retain the parity. The full event trace remains stronger than terminal relation information.

## R739-C: closure inventory conjugacy, 180-member orbit and inequivalent directed transports

**Theorem.** H_A and H_B belong to the same S6 axis-label-permutation orbit. The explicit 3-cycle σ=(0 1 2), fixing 3,4,5, maps H_A onto H_B. Each inventory has stabilizer of order four and orbit size

|S6.H_A| = |S6.H_B| = 6!/4 = 180.

**Proof.** Substitution of σ in the five A triples gives exactly the displayed B triples. For H_A, the occurrence degrees of native-axis labels 0,...,5 in the five three-subsets are respectively 4,4,3,3,1,0. An inventory automorphism must fix the unique degree-one label 4 and unused label 5, and may only permute 0/1 and 2/3. Therefore stabilizer size is at most 2!*2!=4. Each swap (0 1) and (2 3), independently, actually preserves H_A, giving exactly four automorphisms. Orbit-stabilizer gives 720/4=180, and conjugacy transfers the count to H_B. ∎

**Network-distinction certificate.** The full selected 15-arc directed network A has maximum indegree 4, while B has maximum indegree 3. Indegr​ee is invariant under all directed graph isomorphisms, in particular under native axis permutations. Thus two rotation-equivalent *closure-inventory hypergraphs* support nonisomorphic **ordered transition laws**. A closure-incidence observer alone does not determine the BRC event scheduler.

**S6 covariance of the explicitly declared lift.** Rotate the Cell chart, each signed force direction, the closed inventory, active triad and source-attached frame together by σ∈S6. The four channel ports and formal arc identifiers stay typed independently of spatial axes. PASS counts commute with that axis relabeling, and slot updates satisfy σ(f◦h)=(σ◦f)◦h for every h∈S3. The incidence-carrying model is therefore S6-equivariant for all finite macro-histories. The chosen H is transported as input data; the theorem does not choose an unmarked unique H from a completely symmetric input.

## Exact validation and next native test

The companion Python-standard-library verifier reconstructs the sixty ordered arcs and both bitmasks; enumerates the root three-arc loops; checks that all three generators are forced and require five active-triad certificates; checks all nine seam pairings; builds and inversely decodes the four-port code; executes and checks the three full 24-PASS histories; checks Cell triad token types, all 720 S6 permutations against all three terminal relations (2,160 cases per network); and independently enumerates stabilizer/order/orbits of both hypergraphs. The exact finite checker returns PASS and writes R739_TRIAD_PASS_REALIZATION_RESULTS.json. The all-length statements arise from loop concatenation, elementary integer counter addition and S6/S3 action identities, not inference from a numerical trend.

**Next scientific unit:** Derive an independently native-authorized X6 Cell/Link/Port relation-change rule that consumes a signed force-triad closure witness and carries its source/axis frame, replacing the currently *declared* post-code macro-switch. Then test event inventory/capacity and admissible independence relations on the five certificates. The X6 native rotation-dynamics interlock, canonical Source CLAIM/Result and independent mathematical review remain open. The current construction is an exact conditional candidate mechanism, not a completed original mother objective.

Local validation: exact standard-library computation; no float arithmetic and no classical Euclidean vector-sum-zero balance substituted for P000. Research branch persistence does not imply Source scientific acceptance.
