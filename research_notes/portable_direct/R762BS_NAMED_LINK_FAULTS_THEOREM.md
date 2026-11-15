# R762BS — Exact unrestricted noisy Link observers and frame-covariant BRC panels

Date: 2026-11-16 (Asia/Shanghai). Status: **AUTHOR-PROVED WITH COMPLETE EXACT FINITE ENUMERATION; NOT_REVIEWED**.
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5). Preserve six named signed axes, native 120-degree PERP_E and primitive three-force closure arity.
Conditional predecessors: R762BP (PR #2517, commit 131bd4d77341d0fc16e9a25c85fe44ac4d5ce726), R762BQ (PR #2520, b8599c9dd36fac458a7c0f6b23010aa5d5f07295), R762BR (PR #2523, 71f02cf36023088d0f24d2ea30be55ee10856df3).

## Carrier, oracle, and claim scope

Use the explicitly labelled positive-rational BRC branch basis indexed by the 40 permutations of six named Ports with cycle type (3,3), each encoding two unordered directed triads. Branch weights are 1/1 and represent counts, not signed amplitudes or physical force. Condition on the already observed arrow 1→2. Its fiber U consists of eight branches. A primitive atomic Link query Q_(a,b) returns the Boolean 1{sigma(a)=b}, for a != b. Among the 30 possible named queries, twenty are nonconstant on U and sixteen distinct truth sets occur (four truth sets have two distinct names). Each query name is used at most once in the nonadaptive Link panel. A constant query carries no discrimination and is omitted. The already observed 1→2 is free in this comparison.

For a fixed named panel H, define the binary word C_H(sigma) indexed by the chosen query names, and let
d(H)=min_{sigma != tau in U} Hamming(C_H(sigma), C_H(tau)).
An arbitrary adversary can corrupt t answer bits and erase e other known positions. Unique decoding of all eight labelled sources is possible exactly when 2t+e < d(H). This is an exact finite code criterion, not a stochastic noise model.

## Theorem 1 — Complete sharp named-query resource function

For q=1,2,3,4,5,6, let N(q) be the least number of nonadaptive, distinct named informative Link queries giving d(H)>=q. Then

| Required minimum distance q | N(q) | Number of optimal named panels | Number of S4-transport orbits |
|---:|---:|---:|---:|
| 1 | 5 | 1,944 | 81 |
| 2 | 6 | 52 | 4 |
| 3 | 10 | 2,270 | 112 |
| 4 | 12 | 551 | 49 |
| 5 | 15 | 224 | 16 |
| 6 | 16 | 16 | 5 |

The maximum attainable distance using all twenty distinct names is exactly six; hence no panel under this atomic nonrepetition contract has distance >=7. The panels achieve every corresponding minimum, with explicit examples in the JSON certificate. For example, distance-three is achieved by
{2→4,2→5,2→6,3→4,3→5,3→6,4→5,4→6,5→3,5→4}
(ten named calls), and distance-five by
{2→3,2→4,2→5,2→6,3→4,3→5,3→6,4→3,4→5,4→6,5→3,5→4,5→6,6→3,6→4}
(fifteen named calls).

**Exact proof certificate.** The complete finite domain is specified algorithmically, without probabilistic sampling or numerical approximation. Enumerate all 6!=720 permutations of the six named Ports, retain the 40 whose cycles have lengths (3,3), then the eight whose image of Port 1 is Port 2. Generate all 30 ordered names (a,b) with a!=b, retaining exactly those twenty for which the eight-bit truth vector is nonconstant. For each unordered pair of distinct source states (28 pairs), form the 20-bit mask of query names that distinguish this pair. Enumerate every H in the integer interval [0,2^20), each integer being a unique panel bitmask. For each H, its exact distance is the minimum of popcount(H AND pairMask) over the 28 pair masks. All comparisons are exact integers. Track the shortest size and its count for each threshold q; derive S4 orbit counts by transporting all selected names under all 24 permutations fixing 1 and 2.

The published verifier executes this finite algorithm with explicit assertions, checks that exactly 1,048,576 panels were evaluated, and independently checks the number of panels of every size against the binomial coefficient C(20,k). It validates all six lower bounds (no shorter panel can meet each q), all six attained upper bounds, every displayed optimal-panel count, and S4-orbit coverage. The maximum distance is also checked from the full query mask. This exhaustive, fully delimited Boolean enumeration is a finite proof of the displayed numbers. It does not assume that a sampled finite window represents an infinite family.

A structural explanation for the distance is available: identifying each of the eight sources with a vertex of K4,4 as in R762BQ, a named query is an edge between its two positive states. Four distinct edge predicates have a second named representative. Let m_H(u,v) be the number of chosen query names true on both states u and v, and deg_H(u) the number of chosen queries true at u. Then for distinct states
d_H(u,v)=deg_H(u)+deg_H(v)-2m_H(u,v).
The enumerator evaluates this same exact distance through bit masks and also accounts for the duplicated names; a simple-graph count alone would miss the named-call multiplicities.

## Theorem 2 — Sharp nonadaptive signed-source fault budgets

Extend U to U × {±1}^4, with four independent hidden signs on Ports 3,4,5,6. The known signs of Ports 1 and 2 are not charged. In addition to a named Link panel H, sign i has an atomic query S_i that may be repeated r_i times; no combined Link-plus-sign query is supplied. The complete code is a concatenation of the Link word with four repeated sign bits. Its distance is exactly

d_total=min(d(H),r_3,r_4,r_5,r_6).

For t arbitrary corrupted Boolean answers, distinct Link names and independent repeated signs therefore give the sharp total

M(t)=N(2t+1)+4(2t+1).

| Corrupt answers t | Link calls | Sign calls | Total atomic calls |
|---:|---:|---:|---:|
| 0 | 5 | 4 | **9** |
| 1 | 10 | 12 | **22** |
| 2 | 15 | 20 | **35** |

**Proof.** The pair of states differing only in one hidden sign attains distance r_i; the pair differing only in their triadic branch attains d(H). Any other distinct pair differs in at least one of these disjoint code blocks, giving the displayed minimum. The distance criterion thus forces at least 2t+1 measurements of each of the four signs and at least N(2t+1) named Link queries. Equality follows from the corresponding panels and sign repetitions. Even when sign readings are repeated arbitrarily, three arbitrary Link-answer corruptions are not uniformly correctable with twenty nonrepeated named Links, because their entire Link subcode has distance six.

For a mixed budget of t unknown flips and e known erased answers, set q=2t+e+1. Whenever q<=6, the sharp total is N(q)+4q. Examples: a single erasure costs N(2)+8=14; one flip plus one erasure costs N(4)+16=28; two flips plus one erasure costs N(6)+24=40. The statement is for predetermined nonadaptive panels and the declared atomic-interface budget.

## Theorem 3 — Covariant transport of optimal asymmetric panels

Let G=S_{3,4,5,6} be the stabilizer of the known named arrow 1→2. Its action on branch permutations is conjugation and its action on a query is Q_(a,b) -> Q_(g(a),g(b)). The exact Boolean identity

Q_(g(a),g(b))(g sigma g^-1)=Q_(a,b)(sigma)

implies C_{gH}(g sigma g^-1)=C_H(sigma) after the corresponding coordinate reindexing. Thus d(gH)=d(H): every optimal panel transports to another optimal panel without losing its fault tolerance, provided that its chosen frame/query names are retained or jointly transported. Invariance of one fixed panel (the stronger requirement of R762BR) is unnecessary for covariance of the observer-plus-frame pair.

The complete S4 classification of optimum panels at q=3 has orbit-size histogram 6:3, 8:10, 12:17, 24:82, for 112 orbits and 2,270 panels. At q=5 it is 4:2, 12:10, 24:4, for 16 orbits and 224 panels. The certificate gives all six histograms; orbit size times its number of orbits sums to the optimal-panel count.

The cost comparison with R762BR is now exact under the stated distinct-name and four-independent-sign interfaces: S4-invariant signed panels use 16/24/36 calls for t=0/1/2, while transported asymmetric panels use 9/22/35. This identifies the operational cost of requiring a fixed invariant panel rather than explicitly recording an observer frame.

## Validation, provenance, and next frontier

The companion Node.js verifier is deterministic and self-contained. Run it as
node R762BS_NAMED_LINK_FAULTS_VERIFY.js > out.json
and compare the exact JSON structure with R762BS_NAMED_LINK_FAULTS_EVIDENCE.json. Integer/Boolean arithmetic and finite bit masks only; no floating point, classical trigonometry, external data, or native dynamical simulation. The q-optimum counts, orbit counts and signed budgets are independently reproducible from the source states rather than asserted as trusted inputs.

Scientific inputs are frozen at the Task's P000 V5 pin; current behavioral protocol is docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context and portable research. The theorem concerns a conditional directed-Link incidence candidate. Native TRIADIC_CLOSURE_E permission, V17/V29/V39 transport semantics, physical readout and independently reviewed admission remain unresolved. This paper is author-side scientific evidence, not a formal Result or Review; control identity/CLAIM is separately checked.

**Next discriminating question:** for each genuinely permitted native signed Cell/Port/Link triad event, determine which of the twenty named Link tests is an allowed observable and which sign queries are available. Calculate the induced subcode and its real error/erasure trade-off. If the native transport only moves frames rather than preserving a fixed panel, apply Theorem 3 and explicitly retain the query-frame residual. If native operations discard branch identity, test the exact observer fibers against their full future-operation horizon before quotienting the BRC carrier.
