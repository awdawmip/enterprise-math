# R747 — Framed C1 port connection: exact S3 BRC holonomy and a scope-safe orientation quotient

Date: 2026-11-12, Asia/Shanghai.
Status: author-side conditional theorem with executed exact verifier; independent Driver review pending.
Parent Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Immutable task publication: TP2-8B7E13C5904A2D6F1142.
Frozen scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Current applicable normative rules were read independently; frozen science was not rebased.

Exact predecessors: R744 rooted BRC graphs at 9f266f4d182abf7c6c0bdb3c3fed621987b9be80; R745 oriented signed C1 port triads, PR #2154 head 8ad5921d5fddf0c2bd69eb65595f554bc8818bf5; R746 two-visible-port C1 lifts, PR #2157 head bb255c6776b51041ecc0f47853910938b06eb6c9; R746 V29 time-contrast observer, commit 9b82046dfd61c2255faba1680d1a75307ca9e586. These predecessors are author-side candidate results and have not been promoted to independent native Result acceptance.

## 1. Mathematical problem and typed inputs

P000 V5 fixes six signed native spatial axes, a six-dimensional affine Cell torsor, three as the minimum nonzero stable force-quantum arity, and native pairwise PERP_E at 120 degrees. The R745 C1 candidate realizes a primitive equal-quantum triad at a selected Cell c by three distinct signed-axis ports, each with one nonzero quantum q>0 and its native coordinate link from c to c+s_i e_i, plus a directed port-incidence three-cycle W. The internal cycle is a port relation, not a three-step spatial return. No classical vector-sum-zero equation is used.

For fixed c and q, an unordered signed triad T has three distinct port labels p=(c,i,s_i). An oriented C1 triad adds one of two three-cycles W on T. Define a **framed C1 triad** to add one named internal slot arrangement

    F=(p_0,p_1,p_2).

The corresponding cyclic wiring is W(F): p_0 -> p_1 -> p_2 -> p_0, and the distinguished anchor is a(F)=p_0. Slots 0,1,2 are internal relational labels, not new X6 axes. Given T and W, exactly three frames differ by cyclic rotation. Thus a full frame is equivalent to (T,W,a).

**Question:** Can a natural provenance-preserving C1 port reconfiguration recover R744's six named S3 BRC holonomies, while establishing the exact future-operation scope where only the two orientations W must be retained?

## 2. Retained-slot overlap connection

An admissible candidate edge A -> B consists of two signed C1 sources attached to the same Cell c and carrying the same positive q, with precisely two *identical signed ports* in common. The third signed port is replaced by a signed port on an axis not already in A. Surviving port identities, signed link information, nonzero quanta, and source provenance are retained. A valid C1 directed wiring always exists on B.

For every frame F of A define T_{A->B}(F) by keeping the two common ports in their previous internal slots and placing the unique new port in the now vacant slot.

**Theorem A (unique incidence lift, reversibility and S6 covariance).** For every declared edge A -> B, this is the unique frame update that preserves the slot of each common signed port. It is a bijection with inverse T_{B->A}. It commutes with every axis-label permutation sigma in the frozen S6 rotation skeleton, provided the Cell, signed force sources, links, and edge are relabeled together.

Proof. The two retained ports occupy two distinct slots; the remaining slot is unique. Reversing the edge replaces the newly introduced port with the removed original port in exactly that same slot. Axis permutation preserves identity of common ports, intersection cardinality, and the replaced slot, so sigma(T_edge F)=T_{sigma(edge)}(sigma F). No continuum approximation enters. The proof applies by induction to every finite path of allowed candidate edges. QED.

An edge between signed sources is a **candidate incidence update**, not a license to execute a native V29 PASS or V39 Link/Port event. This distinction identifies the precise next interface to test, rather than withholding the conditional mathematics.

## 3. Theorem B: S3 holonomy on two rooted BRC carriers

Use the two R744 seven-directed-arc subgraphs. Labels below are positive native-axis triples and each arrow replaces exactly one axis:

| Carrier | I loop | P loop | Q loop |
|---|---|---|---|
| A | 012 -> 014 -> 013 -> 012 | 012 -> 023 -> 013 -> 012 | 012 -> 023 -> 123 -> 012 |
| B | 012 -> 123 -> 124 -> 012 | 012 -> 023 -> 013 -> 012 | 012 -> 123 -> 013 -> 012 |

Start from the named frame F*=012 with all positive sources at the same Cell. Apply the unique retained-slot lift on each of the three arcs of a loop.

**Theorem B (exact rooted holonomy).**

| Carrier | I final frame | P final frame | Q final frame |
|---|---|---|---|
| A | 012 | 021 | 102 |
| B | 012 | 021 | 210 |

Proof by explicit local substitution. For A, I replaces axis 2 by 4, then by 3, then restores axis 2, hence returns 012. For A/P, the sequence 012 -> 032 -> 031 -> 021 swaps 1 and 2. For A/Q, the sequence 012 -> 032 -> 132 -> 102 swaps 0 and 1. For B/I, 012 -> 312 -> 412 -> 012 is identity. For B/P, 012 -> 032 -> 031 -> 021 swaps 1 and 2. For B/Q, 012 -> 312 -> 310 -> 210 swaps 0 and 2. Thus in each carrier the P,Q loops are two distinct transpositions of the three named root ports and hence generate the full S3 holonomy. Conversely every loop fixes the unordered root source, so its frame action is a permutation of the three ports, necessarily in S3. The holonomy is exactly S3. QED.

All six root-frame values occur at fixed generator length 3:

| Word | Carrier A | Carrier B |
|---|---|---|
| III | 012 | 012 |
| IIP | 021 | 021 |
| IIQ | 102 | 210 |
| IPQ | 120 | 201 |
| IQP | 201 | 120 |
| PQP | 210 | 102 |

Let R(k) denote the number of distinct root frames obtainable using exactly k generator loops, with the identity generator I permitted. Then

    R(0)=1, R(1)=3, R(2)=5, R(k)=6 for all k>=3.

At k=2 the products give I, P, Q, PQ, QP but not the third transposition PQP. At k=3 this transposition is available, and padding by I preserves all six thereafter. This is a universal-in-k algebraic statement for the two declared rooted carrier grammars, independently of the finite checker.

If R744's **separately declared** four-PASS encoding is attached to these loops, the six length-three histories share terminal PASS counter M01=M10=6 and the same final Cell and unordered C1 source, while retaining the six named frame values. This combines the typed C1 update with R744's source-count observer; existence of the optional physical/helper PASS is a separate native event question.

## 4. Theorem C: exact future-operation-specific quotient

Let rho act on frames by cyclic slot rotation:

    rho(p0,p1,p2)=(p1,p2,p0).

The orientation-only observer F -> W(F) identifies precisely the three frames {F,rho F,rho^2 F}. There are two oriented C1 states per unordered signed source and six frames.

**Theorem C (infinite-horizon orientation quotient).** Consider future operations generated by any *externally declared* sequence of signed one-port-overlap updates T_edge, and readings of W or Next_W(p) for a named existing port p. The orientation-only observation F -> W(F) is an exact safe quotient for this class for all finite future sequence lengths (unbounded horizon).

Proof. The unique signed port removed by an externally given edge occupies a specific slot; rotating all slots before the update also rotates the vacated slot. Therefore T_edge(rho F)=rho(T_edge F). This commutation remains true under all compositions. The directed successor map on the three ports is identical for cyclic rotations of the frame. Hence if W(F)=W(G), every declared future edge word produces identical W and Next_W readouts, proving descent on quotient fibers. QED.

The claim is scoped to edge choices independent of the discarded anchor. A slot-directed edge-choice policy or an observation querying Slot0 requires retaining that field.

**Theorem D (sharp anchor repair).** If future outputs may include a(F) or a designated slot, the three cyclic frames above any fixed W have three different outputs. Thus precisely three anchor values are required and sufficient to recover full F given W. For fixed-width binary coding, two additional bits are needed for that three-valued anchor, or three bits total to represent all six full-frame states of one unordered source.

The obstruction is realized on valid BRC rooted histories, not just an abstract counting fiber. The three length-four words PPQQ, PQPQ and QPQP have the *same even cyclic wiring W* but yield three distinct anchors:

| Carrier | PPQQ | PQPQ | QPQP |
|---|---|---|---|
| A | 012 | 201 | 120 |
| B | 012 | 120 | 201 |

This simultaneously supplies (i) an exact scope-aware compression certificate for successor-only C1 updates, and (ii) a concrete information-loss witness for slot-addressable BRC provenance.

## 5. Finite S6 state census

For fixed Cell c and quantum q:

- 20 choices of three distinct native axes times eight sign assignments give 160 signed unordered C1 sources.
- Two cyclic orientations per signed source give 320 oriented C1 states.
- Three cyclic choices of the anchor per oriented state give 960 framed C1 states.

Under S6 axis-label permutation, the ordered sign word (s0,s1,s2) of the frame's three named slots is invariant. Each of the eight possible ordered sign words forms exactly one orbit of size 6*5*4=120 because any ordered distinct three-axis tuple can be mapped to any other. Each point stabilizer permutes the three unused axes and has size 3!=6. Therefore there are exactly eight framed S6 orbits of size 120. This refines, rather than replaces, R745's coarser sign-count orbit classification of unordered/oriented C1 states.

## 6. Reproducible exact evidence and scope

Companion program R747_C1_FRAMED_HOLONOMY_VERIFY.js runs with Node.js and uses only discrete integer indices, finite sets, finite permutations and assertions. The JSON output is R747_C1_FRAMED_HOLONOMY_RESULTS.json, actually computed in this research turn and returned PASS. It checks:

- All 160 signed triads and 960 distinct framed states, eight S6 orbits of size 120.
- 51,840 quotient/one-port-replacement commutation checks and 51,840 successor invariance checks.
- 1,935,360 covariance checks: two carrier graphs, seven arcs each, 32 assignments of signed values to the five used axes, six source frames and 720 axis permutations.
- 19,682 generator words: two carriers times all 9,841 three-symbol words of lengths 0 through 8; exact group holonomies and distinct end-frame counts.
- Explicit length-three six-frame witnesses and the orientation-only length-four anchor-loss witnesses.

The all-length transport/quotient statements follow from the proven commutation and group-generation laws, not extrapolation from a finite range. No floating point, trigonometric, or Euclidean vector cancellation is used.

BRC applicability and reuse: COMPOSE_APPLIED. Carrier = named ordered rooted BRC paths and signed C1 framed port incidences; branch identity and paths are retained. Observer = terminal frame, or oriented W/successor as a future-operation-specific quotient. Declared operations = signed overlap-port updates and the named readouts specified above. The loss/residue certificate is the six-state fiber with a threefold anchor repair. Positive BRC counts are not used as cancellation amplitudes.

## 7. Next unresolved native event test

The mathematical state/update interface is now explicit. The next unit is to check the *actual frozen V29/V39* event guards against the signed C1 retained-slot edge operation and the R744 inverse-first helper PASS. Test whether an authorized Cell/Link/Port event can replace one incident nonzero force quantum while preserving the two shared quanta, the signed source IDs, its TRIADIC_CLOSURE_E witness, and the named frame or its safe oriented quotient. Then try the first-hop reverse PASS under the actual source event permission. Record its original request, exact failed guard or successful event receipt, subsequent counter/timestamp readout, and whether S6 covariance is maintained.

An admitted native path would realize this candidate. A failed guard restricts this exact candidate transition and motivates a permitted refined interface; neither outcome revises P000 by itself. No new Source CLAIM, formal Result, independent review or physical force law is asserted by publishing this author-side proof.
