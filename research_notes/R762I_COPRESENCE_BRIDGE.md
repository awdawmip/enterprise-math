# R762I addendum — three persistent source carriers and exact co-presence schedule census

Date: 2026-11-13 Asia/Shanghai. **AUTHOR-SIDE EXACT COMBINATORICS / NOT_REVIEWED**; same frozen input and Task as R762I_TIMED_PORT_CODE.md. This gives a candidate Cell/Link/Port incidence carrier with **three independently persistent source labels** instead of R762H's one sequential walker. It is not a newly admitted native force law.

## Event model

Fix one chart-relative X6 Cell, three distinct signed neighboring ports p_1,p_2,p_3, and three independently named source carriers i=1,2,3, each preassigned to its port. Source i has exactly two primitive signed spatial updates, O_i (outbound from the root to p_i) and I_i (return to root), subject only to O_i preceding I_i. Global order of the six source-tagged updates is sequential; after every update, the current occupancy set of all three carriers is retained. The event index here is order, **not measured heartbeat time**. All source-branched schedules have the same final position and multiset of six moves.

**Theorem (three-carrier source-preserving co-presence).** There are exactly **90** legal interleavings of these six named updates. Classifying each by the maximum number M of distinct simultaneously occupied signed ports at any intermediate global state gives:

- M=1: **6** schedules.
- M=2: **48** schedules.
- M=3: **36** schedules.

Thus 36 histories visit a state where all three source carriers occupy their distinct ports together, and 54 do not. The exact co-presence predicate is determined by whether all three outbound moves occur before the first return; in that case all three are present together precisely at the intermediate state after update 3.

For n independently named carriers (pure combinatorial generalization, not an n-force primitive balance axiom), with one outbound and one return update per carrier, the total number of valid serial histories is

N_n = (2n)! / 2^n,

and the histories attaining full n-port co-presence number

C_n = (n!)².

The proportion is exactly 2^n / binomial(2n,n). In the true P000 primitive stable-force case, specialize to n=3.

## Proof

All 2n moves are distinct as source-tagged events, giving (2n)! raw permutations. The n disjoint precedence constraints O_i<I_i are independent binary order relations. Swapping O_i and I_i independently is a free size-2^n action on all permutations, with exactly one representative satisfying all precedence comparisons, so N_n=(2n)!/2^n.

At any intermediate state, source i occupies its port iff its outbound step occurred and its return has not occurred. Every port is simultaneously occupied at some state **iff** no return has occurred before all n outbounds. Because there are exactly n outgoing events, this means the first n steps are the n distinct outgoing events (n! orders) and the last n are the n distinct return events (n! orders), giving C_n=(n!)².

For n=3, having M≤1 requires each outbound update be immediately followed by its own return, as an interposed unrelated outbound would create two active sources. Three complete pairs can be ordered in 3!=6 ways, so M=1 occurs 6 times. M=3 occurs 3!²=36 times. The remaining 90−6−36=48 schedules have M=2. Every one of the 90 histories returns all carriers to the root, showing that spatial endpoint and the source-tagged action multiset do not determine co-presence.

## Consequences and verification

A three-force *same-state* incidence can now be represented by a candidate source-preserving carrier: three different source states on three signed ports at a common operation boundary. R762I's single-walker result instead has distinct visits at indices 1,3,5; that representation alone cannot certify the same-state incidence. Here the additional state is the **joint three-source occupancy set**; dropping it loses the distinction between the 36 co-present and 54 other histories. For the Boolean co-presence query alone, one bit suffices after the history is evaluated; for a future update that reads source order, the actual source-branched history may still be required.

The program R762I_COPRESENCE_VERIFY.py independently filters all 6!=720 event permutations by the three precedence relations, obtains 90 histories, computes their full state-by-state source occupancy and histogram 6/48/36, and runs subset-mask exact dynamic programming for n=1,...,6, checking N_n and C_n. Exact evidence is R762I_COPRESENCE_EVIDENCE.json. All operations are integer/string/set combinatorics, no physical BRC residual, phase, trig, continuous dynamics, V29 transfer, V39 transport, or independent native heartbeat-time law is computed.

A true legal TRIADIC_CLOSURE_E event requires additional source-backed force quantum, angle/closure, Cell/Link/Port admission and state-transition rules. The above concurrency carrier is a candidate interface that can be tested against those rules. Source-scoped P000, ACTIVE worldview and scientific pins are unchanged; no CLAIM, formal Result or Driver review is inferred.
