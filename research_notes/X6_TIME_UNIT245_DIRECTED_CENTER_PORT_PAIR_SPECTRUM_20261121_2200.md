# X6 native time — Unit245: sharp one-way centre-Port ingress/egress cost spectrum

Date: 2026-11-21 22:00 Asia/Hong_Kong. Status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.
Parent: PO-X6-UPPER-STRUCTURE-20260906; task: RS-X6-NATIVE-TIME-DYNAMICS / TP2-91D4A7C2F63805BE21A3.
Author-source attribution: Researcher EM-X6-FB6990, original own SID MCP-082892eb480e45dea6d4b9fcc0491034, on-hour Research lane. No current live CLAIM or native semantic PROGRESS is asserted.

## Object, frozen scientific base and conditional transition law

Freeze the X6 P000 native signed-axis Cell torsor at `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`. In a chosen three-axis slice with chart-relative centre Cell P, take the twelve *original* OUTER Cells
[
x_{2r}=P+a_r,qquad x_{2r+1}=P+a_r+a_{r+1},quad
(a_0,ldots,a_5)=(e_1,e_2,e_3,-e_1,-e_2,-e_3),
]
where r runs from 0 to 5, cyclically. There are 24 directed signed primitive ring links, two per undirected ring neighbour pair. Each is one signed native axis step. The six even x_p, p∈{0,2,4,6,8,10}, are the only chosen ring vertices at one native axis step from P.

The original conditional *whole triad*, serial, target-empty movement law of Units242–244 remains in force. Exactly **two directed centre links** are granted: a one-way ingress `x_i → P` and a one-way egress `P → x_j`, with i,j chosen independently from the six even indices. No reverse spoke follows by implication. The two labelled intact triads A and B start at (x0,x2), every Cell admits at most one, all original ring links are usable in either direction, and the target is simultaneous labelled return to (x0,x2) with original-ring signed winding counters (L_A,L_B)=(-12,+12). Centre moves contribute zero to ring winding and are genuine signed primitive events.

This is a **resource/Port availability discrimination within a declared model**. P000 identifies the native Cell adjacency, not the actual physical permission of a whole-triad Port move or an independent C12/C24 precision update.

## Theorem — complete 6×6 sharp directed-pair spectrum

Let N(i,j) be the least number of serial native events under that exact directional gateway. Rows are ingress i and columns are egress j, ordered 0,2,4,6,8,10.

| i \\ j | 0 | 2 | 4 | 6 | 8 | 10 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 30 | 38 | 36 | 38 | 38 | 46 |
| 2 | 38 | 30 | 46 | 38 | 38 | 36 |
| 4 | 32 | 36 | 32 | 48 | 38 | 32 |
| 6 | **28** | 30 | 40 | 36 | 44 | 34 |
| 8 | 30 | **28** | 34 | 44 | 36 | 40 |
| 10 | 36 | 32 | 32 | 38 | 48 | 32 |

All 36 instances are reachable and have displayed *sharp* costs. The minimum is **28**, attained precisely at (i,j)=(6,0) and (8,2); the maximum is **48**, attained precisely at (4,6) and (10,8). Thus a single *oriented ingress/egress pair at distinct positions*, without a bidirectional spoke at any one position, suffices to match Unit243's all-spokes 28-event global minimum. The earlier Unit244 diagonal N(i,i)=[30,30,32,36,36,32] is recovered exactly. A single directed spoke with no reverse or alternate egress cannot occur in a closed history that visits P: its target P has no departure (or P has no arrival).

### Witness coding, exact native interpretation

The accompanying certificate records a complete chronological shortest history for **every one** of the 36 cases. Each route character `A..M` moves triad A, and `a..m` moves triad B; the character's index gives its destination Cell `x0..x11,P` (index 12). The source is that triad's immediately preceding Cell, initialized A=x0,B=x2. Thus route strings losslessly encode: labelled occupancy, ordered BRC events, every precise original Cell transition, the six-axis signed primitive direction (recovered from its two Cell coordinates), and the exact per-triad ring winding increments. The three force-token identities in each intact labelled triad are preserved; the route never splits a triad.

For i=6,j=0, one 28-event shortest route is:
`LKJIHGMALKJIHGMdefghijklabAc`.
Its four centre events are A:x6→P, P→x0, x6→P, P→x0. The remaining 24 events are original signed ring primitives; the labelled final Cell and winding requirements hold. Another optimal pair is i=8,j=2 (a shortest route in the certificate).

## Exhaustive sharpness proof and independent validation

The finite state is (position_A,position_B,L_A,L_B), with 13 original/native Cell addresses, distinct positions, integer signed original-ring counters, target-empty guard, original 24 directed ring edges and only the specified directed ingress/egress. Every legal chronological native step is explicitly enumerated. FIFO breadth-first search begins (0,2,0,0), returns the first exact goal (0,2,-12,+12), and retains each predecessor, signed axis and triad ID. It excludes occupied targets, not unrecorded positional or branch history. Each certificate replays its entire path to verify labelled return, primitive axis displacement and enabled directed Port.

The exhaustive search retains states with |L_A|, |L_B|≤48. It constructs, for every pair, a valid witness of length at most 48. Any shorter hypothetical path has fewer than 48 native events and therefore **cannot** attain a ring counter of absolute value above 48, since each native step changes one counter by 0 or ±1. Hence every possible shorter path is included. The first-goal FIFO depths are exact global minima within the declared transition graph; this is not an assumed upper bound on unsearched dynamics. The known general all-spokes lower bound 28 from Unit243 is attained independently in two directed pairs.

Executed Node checker: `research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_CHECK_20261121_2200.js`. Complete machine certificate: `research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json`, all 36 compressed lossless signed-Cell/BRC witnesses. Local Node: 36 cases, 794,486 cumulative state discoveries, 1,312 chronological witness events, 1,743,775 exact assertions, 0 failures. A separately implemented Python FIFO solver reproduced the full 6×6 matrix. The checker's actual source and certificate are linked under this same GitHub repository; their immutable commits and content hashes are recorded in the author continuation/Activity.

## Interpretation and next genuine source test

This narrows the actual Port experiment: one inward and one outward **directed** native centre spoke suffice; they can attach to different original ring Cells. The position pair changes the exact event budget from 28 to 48; do not assume native adjacency automatically means a permitted physical Port transfer. Inspect the Source-admitted whole-triad transfer guard, conservation, environmental response and genuine Port orientations. If it grants a pair (i,j), replay the exact witness for that pair against the real updates; if it restricts directions, record the rejecting transition and consider the graph of all Source-accepted ports. Independent same-Cell C12/C24 precision readings remain a separate missing experiment. No new primitive directions, no P000 revisions, no inferred physical H=6, no replacement of the separate R063 six-file benchmark.

Parent scientific frontier: Units233–244 and their existing Activity245 are consumed. Native semantic PROGRESS for Units233 onward requires a *new current winning own Claim/Run*; the previous typed prepare terminal failures are preserved under support #2903 without replay. Driver review and Result admission remain pending.
