# X6 Unit258 - Context-dependent negative-edge refusals and shortest-history fallback

2026-11-22 10:00 Asia/Hong_Kong. Task `RS-X6-NATIVE-TIME-DYNAMICS`; publication `TP2-91D4A7C2F63805BE21A3`; parent `PO-X6-UPPER-STRUCTURE-20260906`.

**Status: AUTHOR_PROVED / EXACT_FINITE_EXECUTED / NOT_REVIEWED / NOT_ADMITTED / NO_NATIVE_PHYSICAL_EXECUTION.**

## Immutable scientific scope
This consumes Unit257 all-optimal-history evidence, rather than restarting Unit245. Frozen P000: `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Original complete directed-port BRC evidence: `enterprise-math@f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json`. Unit257: `f20c9f085ecf7c081f033c660455e98d6ed82031`. No physical force law or new Source transfer authority is introduced.

State is `(posA,posB,wA,wB)`, initial `(0,2,0,0)`, target `(0,2,-12,+12)`, positions 0..11 are OUTER and 12=P. Two labeled intact triads move serially, one signed primitive BRC edge at a time; the destination occupied by the other triad is forbidden. The directed center pair is either (ingress,egress)=(6,0) or (8,2). OUTER +/- steps change the relevant winding +/-1; center passages change it by 0. This is the frozen **conditional** discrete model.

We test a precisely declared hypothetical guard for the mandatory signed edge `A:x0->x11,-e2`: when its pre-event BRC state belongs to a refused context set, the move is unavailable; other original moves remain unchanged.

## Exact new result: denial changes the frontier non-uniformly

| Context-dependent refusal | Port (6,0): shortest steps, histories | Port (8,2): shortest steps, histories |
|---|---|---|
| No refusal | 28; 2,832 | 28; 2,832 |
| Refuse only in initial (0,2,0,0) | 28; 632 | 28; 2,200 |
| Refuse at four early A-winding-zero contexts E4 | 30; 10,712 | 28; 928 |
| Refuse at sixteen early A-winding-zero contexts E16 | 30; 9,212 | 30; 1,036 |

The four early contexts are exactly `(posA=0,wA=0;(posB,wB)=(2,0),(3,1),(4,2),(5,3))`. E16 adds twelve BRC precontexts in the certificate. An initial refusal alone leaves 28-event alternatives on both Ports. For the declared E4 refusal, 28-event optima disappear at Port (6,0), while Port (8,2) still has 928. For the declared E16 refusal, the minimum rises to 30 for both. Counts refer to distinct ordered labeled event histories, not probabilities.

## Minimal context-cover theorem for 28-event routes

For Port (6,0), each shortest history visits the mandatory directed edge twice, at two of ten exact BRC contexts. Exhaustive shortest-DAG enumeration of all 2,832 histories followed by examination of all 2^10 context subsets proves that the **unique** minimum set of context-specific refusals blocking every 28-event history is E4, with cardinality four.

For Port (8,2), each of its 2,832 shortest histories visits the edge exactly once, in one of sixteen contexts; every context occurs in at least one history. Hence **all sixteen contexts** must be refused to exclude every 28-event history. This is a sharp minimum and its cover is unique. A single initial rejection does not satisfy either cover. E16 also contains E4, so is a single 16-context certificate against the 28-event class for both Ports.

## Proof and checker
The checker constructs the original allowed serial signed moves exactly, then counts each case in two independently implemented finite algorithms: breadth-first shortest-state dynamic programming and a full depth-indexed integer path-count recurrence. The two minimum lengths and exact integer path counts agree in every tested case. Separately, it constructs the unguarded 28-layer shortest-path DAG, counts viable suffixes, enumerates all 2,832 histories per Port and audits context occurrence and minimum hitting sets. No floating-point mathematical approximation is used; all counts stay inside exact JavaScript integer range. A separate local Python layer DP/BFS calculation returned the identical table.

## Native consequence and precise limitation
The direct next Source question remains the actual signed, intact-three-token movement `A:x0->x11,-e2` with true force closure, occupancy and environment/time response. If the true guard refuses the initial state, the finite model predicts that the next candidate to test is an existing B-first 28-event route, not immediate abandonment of both Ports. Under the additional *testable assumption* that admission is determined entirely by the listed BRC prestate and not a hidden environment component, E4 and E16 are exact contextual exclusion certificates for the 28-event class. Physical Source may depend on additional state, so preserve actual native event and observer ledgers before applying such a certificate.

The current Gateway control read was still not authorized for a live CLAIM. The original terminal failed continuation requests remain unchanged and protected Native PROGRESS is pending. Engineering support: https://github.com/awdawmip/enterprise-math/issues/2903 . The original R063 native benchmark is outside this experiment.
