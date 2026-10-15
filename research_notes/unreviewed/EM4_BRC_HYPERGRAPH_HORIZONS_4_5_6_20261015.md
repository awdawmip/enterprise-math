# Enterprise Math — unreviewed auxiliary BRC research: four-source hypergraph horizons 4, 5, 6

Status: SELF_CHECKED / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM / NO_FOUNDATION_PROMOTION.
Read pins: GLOBAL_KNOWLEDGE_V1 main@3a87cfbe9c653752ac394742ae3e17f535fd04aa; Enterprise Math main@6370cd86865a585b1508dc1bd98fcc8995181ace.
This note is a noncanonical, branch-only mathematical candidate, not a Researcher Task Result, RA checkpoint, or Driver review.

## Exact auxiliary model

Four hidden labeled sources i=0,1,2,3 with integer seeds s_i>=1, x_i>=s_i. Each public group G is nonempty; a strictly positive hidden branch resets exactly one i in G to s_i. After an operation the public bit is 1[total mass>=tau]. There is no initial bit. Public adaptive policies may stop. Their Boolean terminal safety is universal over all strictly-positive hidden branches: total>=q. Put S=sum s_i, d_i=x_i-s_i>=0, and require S<q<tau. For reset support R, total M(R)=S+sum_{i not in R}d_i, f(R)=1[M(R)>=q], g(R)=1[M(R)>=tau]. Define x~_h y when all adaptive policies with at most h operations have identical universal safety. Define H(G) as the least uniform sufficient depth for all seed/threshold/state pairs.

## Computation-assisted statements, awaiting independent review

Exact universal horizons for these particular action families:

* {{0,1},{1,2},{2,3}}: H=4.
* {{0,1,2},{1,2,3}}: H=5.
* {{0,1,2},{0,1,3},{0,2,3}}: H=5.
* ALL FOUR three-element subsets: H=6.

These assertions quantify over every integer S<q<tau and every x_i>=s_i>=1 in the stated auxiliary model; there is NO transfer to native P000 6D/slice dynamics.

The prior exact four-source realizability certificate independently checked 7413 abstract nested antitone (f,g) signatures: 3137 with integer (d,Q,T) witnesses, 4276 excluded by explicit two-pair integer balanced-trade contradictions. Canonical compact entries SHA256: 17fc1dd110ef946a3eb825b07a208497f1a5c6e38be7e39604254a1f1509890d. Exhaustive comparison of ALL 3137x3136=9,837,632 ordered distinct realizable signatures is stronger than comparing only pairs co-realizable at a common threshold, so it proves the stated UPPER bounds.

The directed BFS node (B_X,r_Y) contains X's entire reset-mask public belief set and ONE positive Y hidden reset path. From an initially safe X node, a public operation G is admissible for X-safe/Y-unsafe separation only if every resulting X reset state is safe. For a chosen Y source i in G, retain only X reset states with the same observed Y feedback g_Y(r_Y union {i}); all other feedback branches of the public strategy stop safely. Y unsafe with X belief safe is a witness; an X-unsafe belief is discarded by monotone reset. Search both orientations. Each direction has at most 16*2^16 states; a visited-state BFS is exhaustive over any finite policy depth, not merely depth<=6.

For all four triples (action bit masks 7,11,13,14), complete directed-pair counts:
equivalent at ALL finite depths 33716; first separation depths 0,1,2,3,4,5,6 respectively 6272,2835500,6056754,880794,24560,24,12. Sum 9837632; maximum 6. Other listed families were separately checked on the full 9837632-pair finite graph and yielded maxima 4 or 5 as listed above. Scope is exact Boolean support/terminal safety; probability, path-multiplicity observables, and exact-weight histograms are NOT quotiented as equivalent.

## Common-threshold positive-integer lower-bound witnesses

For G={012,123}, s=(1,1,1,1), q=5, tau=9, X=(2,3,3,2), Y=(2,2,4,2). Exact signatures (32767,259),(32767,263). Complete two-belief DP gives X~_4Y but not X~_5Y. Five-operation Y witness spine groups 012,123,012,012,123 with chosen sources 1,1,0,2,3 and prior feedback continuation 1,1,0,0. Terminal histograms preserving multiplicities: X={7:2,8:3} safe, Y={4:2,5:8,6:6,7:3,8:5,9:1} unsafe.

For all four triples, s=(1,1,1,1), q=7, tau=11, X=(3,3,4,4), Y=(3,3,5,4). Exact signatures (8191,279),(8191,287). Complete two-belief DP gives X~_5Y but not X~_6Y. A six-operation policy follows groups 012,013,023,123,012,013, with continuation feedback 1,1,1,1,0; any other feedback branch stops. The Y secret source path 0,0,0,1,2,3 has full feedback 1,1,1,1,0,0, finally M=4<7. The exact path histograms are X={8:1,9:10,10:4} (15 safe branches) and Y={4:4,7:13,8:6,9:5,10:5,11:8} (41 branches, four unsafe). The same thresholds were checked against every one of the 16 reset masks using exact integers; no separate-threshold signature pairing is used for the lower bound.

For G={01,12,23}, s=(1,1,1,1), q=5,tau=6, X=(2,2,2,2),Y=(2,2,2,3), all policies <=3 are safe on both; three actions 01,12,23 followed by 23 only if third feedback=1 distinguish at depth4. Terminal histograms X={5:8,6:4}, Y={4:1,5:7,6:2,7:3}.

## Evidence boundary and next unit

Local full reproducibility ZIP SHA256: f2d4a69d81b45a6eee6df2ba919a95129f3601bf62d2cf5ca7c1ee59cdebd206. It contains C++17 exact full finite-pair BFS, original four-source realizability certificate and independent checker, exact 4/5/6 step witness checkers, 4200 independent sample-orientation oracle comparisons, JSON outputs, SHA256 manifest, and a full proof report. The ZIP is locally preserved as a chat research attachment only until an authorized immutable Source publish is achieved. Do not cite this branch-only note as a frozen Result, formal owner evidence, or an independent audit.

Native Researcher session_start for this turn was rejected with STATIC_READONLY_SCOPE_DENIED; no CLAIM/RA-native checkpoint or authorized Result was acquired. The canonical fresh dispatch selected RS-X6-LEGACY-PLANE-RECONCILIATION for a NEW owner claim, which is unrelated to this independent BRC line; no takeover was made.

Next test: find structural hypergraph invariants controlling H_n, starting with n=5 and all (n-1)-subsets; seek common-threshold strict witness before a general uniform bound. A separate authorized research identity/Driver must independently review this candidate and attach complete code/certificate bytes to immutable Source.
