# Random cell-count lines: equal-value seam transfer in a six-field candidate

Progress-Event-ID: random-cell-count-lines-20260913-a8d47f21
Research-Activity-ID: RA-20260912-gap-origin-a8d47f21
Researcher-ID: EM-CHAT-A8D47F21
Session: local-chat-gap-origin-a8d47f21 (local key, not platform authenticated)
Status: CONDITIONAL_PROOF_AND_EXECUTED_LOCAL_CANDIDATE; NOT_FOUNDATION; NOT_FULL_X6_ATLAS
Source snapshot: awdawmip/enterprise-math@63146ee0c2238eb84458355cab4b063ed7736f31.
Prior frontier consumed: NONNEGATIVE_ADDRESS_EQUAL_VALUE_CROSSING_20260913_A8D47F21.md. No prior trial is rerun as a new result.

## 1. Question and actual scope

User requests several random lines checked by counting Cells. Final address digits must be nonnegative, inactive fields zero, and crossing a display boundary need not increment the retained counts. Test these on a two-native-axis restriction of the existing X6 graph; the four omitted native coordinates are fixed, not erased from arbitrary states. The square-grid drawing is an incidence/counting schematic, not a native angle, metric or Cell-footprint claim. The address slots below have regional meanings; they are not automatically the six fixed native E_i components. This is an explicit candidate chosen for the test, not a recovered final user atlas.

Ground truth is the 12 by 12 integer Cell patch (x,y) with 1<=x,y<=12, signed unit steps along the two selected native axes, and no diagonal primitive edge. Display seams are at x=y=6.5. Their intersection is not a vertex or intermediate step. The finite box contains all shortest monotone paths between its vertices. No old global zero Cell is deleted by choosing a finite patch.

## 2. Count-first encoding

Let a=7-x for x<=6 and a=x-6 for x>=7; define b similarly from y. Each is the counted row/column index starting at 1 next to the gap. Use these six-field codes:
A (x<=6,y>=7): (a,b,0,0,0,0).
B (x>=7,y>=7): (0,b,a,0,0,0).
C (x<=6,y<=6): (0,0,0,0,b,a).
D (x>=7,y<=6): (0,0,0,a,b,0).

The nonzero supports {1,2}, {2,3}, {5,6}, {4,5} uniquely identify the region since a,b>=1. Read a,b from that region's declared slots and invert with x=7-a or 6+a, and y=7-b or 6+b. Thus encoding/decoding are mutual inverses on the valid domain; every final digit is nonnegative and four inactive slots are zero. Six output fields suffice for this two-axis candidate only. No claim of a complete fixed-axis X6 implementation follows.

First-layer fixture S={6,7}^2 has L=1+dist_G(P,S)=a+b-1. Hence its four Cells all have layer 1 but different full codes. The scalar layer and the coordinate counts are not arithmetic units or physical time.

Code-side motion is implemented independently without calling encode/decode: toward a seam, decrement a count above 1; at count 1, switch region and retain 1; away from a seam, increment. Repack into the new support pattern. Each case satisfies D(T_enc(c))=D(c)+/-e_i. Thus it is a genuine old unit edge even when counts remain equal; no ghost origin edge is added. For a seam step the pair (a,b), its sum, and L are unchanged. This equality follows from the specified candidate rule, not a universal law inferred from random samples.

## 3. Random generation and counted results

Python Random seed 20260913; take the first six pairs of independently uniform endpoints in [1,12]^2, with no filtering for crossing or success. Construct an exact monotone digital line by sorting crossing times (2k-1)/(2*abs(delta_i)); tie order is first selected axis before second. This is one staircase realization of the endpoint segment, not a new primitive straight direction. At an exact corner the side Cell depends on this convention; both orders remain distinct native paths. Literal Euclidean chord-interior intersection counts are not claimed.

ID | start | end | counted steps | visited Cells | seam crossings | shortest path count
1 | (2,10) | (4,4) | 8 | 9 | 1 | 28
2 | (6,7) | (7,6) | 2 | 3 | 2 | 2
3 | (1,6) | (7,4) | 8 | 9 | 1 | 28
4 | (9,12) | (3,12) | 6 | 7 | 1 | 1
5 | (3,12) | (1,8) | 6 | 7 | 0 | 15
6 | (8,3) | (7,8) | 6 | 7 | 1 | 6

Total 36 actual steps and 42 path visits including six starts (not necessarily 42 globally distinct Cells); six seam steps, all count-preserving. Line 4 horizontal a-sequence is 3,2,1,1,2,3,4 with b=6. Its seam transfers (0,6,1,0,0,0) to (1,6,0,0,0,0) in one old step. Line 2 has codes (1,1,0,0,0,0) -> (0,1,1,0,0,0) -> (0,0,0,1,1,0), all layer 1, two real steps. Its other shortest order visits region C instead of B.

## 4. Independent checks and negative controls

Executed with exact integer/Fraction arithmetic. The unchanged original geometry.py was extracted from the prior attachment, and its Git blob a1a8dc4d1ca53fde2ca00d9b944c1b8aa346a152 matches current remote metadata. Its graph_distance was called on both native and code-side graphs for each random line: 12 calls. Code adjacency was built by independent count/region transition rules, not merely relabeling the native edge list.

PASS: 144 roundtrips and distinct full codes; 528 directed edges; all 20736 ordered endpoint pairs have identical BFS distances AND shortest path counts on the independently built graphs; six path traces have no skipped/repeated Cell, correct endpoint and N+1 visits; all path counts agree with the existing binomial specialization of native BRC; seven invalid inputs rejected. Six separate plotted trace files and full JSON records are provided in the Chat bundle.

Negative controls: keeping only (a,b) gives 36 values for 144 Cells, each with four different positions. A mandatory +1 to the transferred seam count skips a Cell: all six tested boundary steps decode to distance 2 instead of 1. Raw six-digit L1 is also not the native metric: line 4 seam digits differ by L1=2 while actual graph distance is 1. Equal observed counts cannot erase the real event or make the two-step corner a one-step diagonal.

BRC REUSE_APPLIED: labeled primitive paths and existing N_min/binomial shortest-count formula. Full support pattern preserves spatial identity; edge identity/order are not merged. BRC REUSE_EXECUTED boundary: original graph_distance backend; independent BFS count code is a test oracle, not a replacement toolbox family. No signed/phase cancellation is inferred.

## 5. Evidence and remaining obligations

Checker SHA256: f6055cf12baaed07a82ea0635b7f9b72cf3622f607991dcf0aa080dc5b107090
Full results SHA256: 35deaed5d54e38527ecd49e68164a0f6a23cbfd949c498c5ade4292b38343611
The local reproducible bundle includes checker, hash-verified original backend, results, six diagrams and full Chinese trace report. This source note preserves rules, proofs, random selection and exact outcomes. Numerical tests support the candidate implementation; no full repository tests, Lean build, physical geometry validation or full six-axis atlas adoption is claimed.

Conclusion: on this explicit two-axis grid candidate, nonnegative six fields + inactive zero + value-preserving seam relocation are jointly compatible with the existing graph and path counts. The exact region/support table is trial-specific, not uniquely selected by old theory. Extending all six native axes while keeping fixed E_i slot semantics and complete hidden state remains a separate obligation. No P000, Foundation, worldview, production source, time law or native transition is changed.
