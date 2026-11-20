# X6 native time: guarded triadic configurations, event-order traces, and sharp observer memory

Date: 2026-11-21. Task: `RS-X6-NATIVE-TIME-DYNAMICS`. Publication: `TP2-91D4A7C2F63805BE21A3`.
Researcher provenance: `EM-X6-FB6990`; own historical SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. This is an explicit **conditional model** of resource-guarded events, not a physical Cell/Link/Port admission or a change to P000.

## Frozen basis and incremental question

Consume the existing resource-conflict result at `f41c2690daba467ecbde99615a1337e67be46ffd:research_artifacts/mcp/RS-X6-NATIVE-TIME-DYNAMICS/MCP-456b8f22a648400585024ffbcc1c2c94/5a04daccb6795e494dbc/X6_TIME_GUARDED_TRIADIC_RESOURCE_CONFLICT_20261118.md`: each of m mutually disjoint native Cell resources contains one intact declared TRIADIC_CLOSURE_E frame, and exactly one of three labeled outgoing candidate ports can fire; the first event consumes that resource. That result counted **unordered configurations** with K_m(x)=(1+3x)^m. This note answers the separate native-time question: how many **ordered legal traces** give each configuration, and what information is minimally needed for future legality, branch-provenance, or chronology observers?

All sources are distinct and labeled. A port choice r in {0,1,2} preserves the existing intact triad and its token identifiers. Distinct footprints, non-replenishment and mutual commutation of different sources are assumptions of this conditional model. Event index counts ordered occurrences, not physical duration; time is not a seventh spatial axis.

## Exact event system

For each source i=1,...,m let q_i be in {bottom,0,1,2}. Initially q_i=bottom. Labeled action (i,r), r in {0,1,2}, is enabled iff q_i=bottom, and updates only q_i:=r. Existing signed native ports, source/target, frame and token provenance live inside each label; here (i,r) is their abbreviated label, not a new P000 primitive type.

Theorem 1 (sharp chronology/configuration count). At depth k, 0<=k<=m, the number of distinct q configurations is
    C(m,k)=binom(m,k)*3^k,
while the number of complete labeled ordered event prefixes of length k is
    H(m,k)=binom(m,k)*3^k*k! = m!/(m-k)! * 3^k.
Every configuration at depth k has exactly k! chronological realizations. Thus
    K_m(x)=sum_k C(m,k)*x^k=(1+3x)^m,
    T_m(x)=sum_k H(m,k)*x^k,
    total distinct event-prefix histories=sum_k H(m,k).
Proof: choose the k used distinct source labels, choose one of 3 ports for each, then permute those k mutually commuting event occurrences. The resource guard forbids any repeated source; every such permutation is legal by disjointness. The map history -> q has uniform k!-element fibers. This refines, rather than repeats, the earlier configuration theorem.

Theorem 2 (minimal future-legality Markov quotient). Define two reachable q and q' equivalent when they admit the same language of every future labeled action word, including the empty word. Then q~q' iff {i:q_i=bottom}={i:q'_i=bottom}. Indeed equal unused sets give identical legal continuations; a source in their symmetric difference supplies a one-letter word enabled from precisely one state. Therefore there are exactly 2^m future-legality equivalence classes and a fixed-length encoding needs at least m bits. The m-bit per-source used/unused vector achieves this bound. This statement is relative to **future enabled-event observations only** and does not say that port provenance is dispensable for other observables.

Theorem 3 (provenance and chronological lower bounds). If a present-state observer must distinguish which of the three ports was chosen at each used source, its observation map must be injective on all 4^m configurations; a fixed-length code needs at least 2m bits, achieved by the four-value q register. If an observer instead must reconstruct the *entire ordered event prefix* from a single code over all reachable prefixes, it must distinguish
    N_m = sum_{k=0}^m binom(m,k)*3^k*k!
histories, so requires ceil(log2 N_m) fixed bits; straightforward ranking achieves this bound. At known q with k used sources, the additional order-choice ambiguity has precisely k! alternatives. In particular the endpoints and event count do not determine chronology.

Witness m=2: [(1,0),(2,1)] and [(2,1),(1,0)] both yield q=(0,1), event count 2 and identical future legal continuations; the full ordered relation-change trace distinguishes them. At m=2 there are 16 configurations but 25 distinct legal prefixes across depths. P000's time/branch residual is the ordering witness, not an additional spatial coordinate or precision-refinement bit.

## Exact independent tests

Standard-library Python executable `research_checks/X6_TIME_GUARDED_TRIADIC_TRACE_COUNTER_20261121.py` applies dynamic programming over 4^m explicit resource states for m=1..8; checks every layer and every state's history multiplicity against binomial/factorial formulae; also separately exhaustively traverses every ordered prefix for m=1..5 and tests one-step future-language signatures. All operations use exact integers. No mismatch found.

| m | present q configurations | legal ordered prefixes across all depths | minimum future bits | minimum port bits | minimum full-history bits |
|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 1 | 2 | 2 |
| 2 | 16 | 25 | 2 | 4 | 5 |
| 3 | 64 | 226 | 3 | 6 | 8 |
| 4 | 256 | 2713 | 4 | 8 | 12 |
| 5 | 1024 | 40696 | 5 | 10 | 16 |
| 6 | 4096 | 732529 | 6 | 12 | 20 |
| 7 | 16384 | 15383110 | 7 | 14 | 24 |
| 8 | 65536 | 369194641 | 8 | 16 | 29 |

## Scientific consequence and next test

A precedence-only poset count cannot replace the resource guard, and an unordered configuration count cannot replace a history count. The *same actual resource model* supports three different exact sufficient carriers depending on future observer: m used-bits (future legality), 2m q-bits (port provenance), or a ranked event-prefix trace (chronology). In the general native task, identify an admitted signed triadic event with real environmental/port update laws, determine which observers are required, and test whether two traces with the same q diverge under rotation, external response or later observation. Such divergence invalidates the m-bit or 2m-bit quotient for that enlarged observer while leaving these scoped theorems intact.

No native R063 six-file benchmark executed. No physical calibration, independent Driver review, Result freeze or Foundation promotion claimed.
