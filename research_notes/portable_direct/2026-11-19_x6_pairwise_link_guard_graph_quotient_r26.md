# X6 R26 — Pairwise Link-guard graph and exact joint future-language quotient

Date: 2026-11-19. Scope: RS-X6-NATIVE-TIME-DYNAMICS, publication TP2-91D4A7C2F63805BE21A3.
Scientific pins: P000 V5 `a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`; taskbook `f41c2690daba467ecbde99615a1337e67be46ffd:research_tasks/RS_X6_NATIVE_TIME_DYNAMICS_20260906.md`.
Predecessors: R24 `dd7ce659188d391651500ac46dcf12db74979b72`; R25 `9ceb49d28bd52651e4b887bddc904595ea8cbf60`.
Status: CONDITIONAL_AUTHOR_PROOF / EXACT_BOOLEAN_BRC_PASS / NOT_REVIEWED / NATIVE_EVENT_ADMISSION_PENDING. Existing Research2 scientific lineage `EM-X6-214D9C`; publication of this standalone note is not a new native CLAIM or formal PROGRESS.

## Controller and complete observer

Take any finite simple undirected graph G=(V,E), |V|=m >= 1. Every i in V identifies an intact triadic source B_i in a separate two-Cell lane of the six-axis affine X6 Cell torsor, and each edge e in E identifies a separate intact one-use consumer A_e. Independent B_i signed-native-Port events alternate B_i^+ (outbound +E1) and B_i^- (return -E1). Each source has a conserved hidden frame bit theta_i in {0,1}; its first successful return sets a typed Link flag l_i=theta_i, but neither direction's eligibility depends on theta. Later B_i cycles remain legal and do not reset l_i.

The one-use A_{ij} event is eligible exactly when the returns of BOTH B_i and B_j have occurred, l_i=l_j=1, and A_{ij} has not already acted. A_{ij} does not alter B lanes, the frame bits, the flags of other links or other consumers' permissions. Cells/lanes are disjoint, and all events move complete triads along a declared signed native Port. No geometric diagonal and no seventh spatial axis are introduced. This is a DECLARED feedback/Link rule, not yet an authenticated native TRIADIC_CLOSURE_E admission predicate.

Initial public Cell positions, all Link-flag initialization, and all consumer-used bits agree for all 2^m choices theta. The observer retains the complete SUCCESSFUL word of source identities and signed Ports, including order, for any future horizon. It does not read hidden frame bits, failed attempts or Link flags directly. Put S(theta)={i:theta_i=1}; E[S]={ij in E:i,j in S}, and W(S)=the vertices incident to edges of E[S]. L_h(theta) is the set of all successful words of length at most h.

## Theorem R26.1 — Exact first exposure and permanent joint quotient

For every finite simple G:

1. If h <= 4 then L_h(theta) is independent of theta.
2. For every h >= 5, L_h(theta)=L_h(theta') **if and only if** E[S(theta)]=E[S(theta')]. Equivalently, W(S(theta))=W(S(theta')). Thus the quotient stabilizes at depth 5.
3. The exact number of initial-fiber future-language classes and minimal fixed-length information are
   C(G)=|{ W subset V : G[W] has no isolated vertex }|,
   b_min(G)=ceil(log2 C(G)).
   The empty W is counted as valid. For h<=4 the class count is 1 and b_min=0.
4. For a valid W define its closed neighborhood N[W]=W union all graph-neighbors of W. The exact size of its equivalence fiber is
   |{S:W(S)=W}| = I(G[V\\N[W]];1),
   where I(H;1) denotes the number of independent vertex sets of H, including empty.
5. The typed state (B phases, returned flags, consumer-used flags, E[S]) is a sufficient Markov state at every intermediate reachable state under this declared observer. This does not assert global minimality outside the initial public fiber.

**Proof of (1)–(2).** An A_{ij} can fire only after both B_i and B_j have completed a two-event signed excursion, so any word containing an A action has length at least 2+2+1=5. All B-only words have identical legality for every theta. For each graph edge ij, the five-event word B_i^+ B_i^- B_j^+ B_j^- A_{ij} succeeds precisely if theta_i=theta_j=1. Hence L_5 recovers the entire induced edge set E[S]. Conversely, if E[S]=E[S'], pair the two controllers at states with identical B phases, completed-return flags and used A masks. Every available B action agrees, and an A_{ij} is enabled in both exactly when ij belongs to E[S] and both source returns and its unused status agree. Successors preserve the relation. This exact labeled bisimulation proves equivalence for every finite/infinite future word and every h >= 5.

**Proof of (3).** Every W(S) is empty or has no isolated vertex in G[W(S)], because each vertex of W(S) touches an induced active edge. Conversely every W with that property is obtained by S=W. From any induced edge set E[S] one recovers W(S) as its endpoint union; conversely E[S]=E[W(S)]. Therefore these W are in bijection with all possible observer signatures. Counting and fixed-length information follow.

**Proof of (4).** Fix valid W. Any S with W(S)=W must contain W. Its other active vertices I=S\\W cannot be adjacent to W or they would add a new active edge; I must also have no internal edge or its vertices would join W(S). Thus I ranges exactly over independent subsets of the induced graph on V\\N[W], proving the formula and an explicit joint-fiber safety certificate.

## Consequences and non-redundancy

- Complete graph K_m: C(K_m)=2^m-m (all supports of cardinality 0 or 1 merge; every larger support is distinct). This recovers the R25 count for u=1 and q*=2, but R26 uses explicit pairwise Link eligibility rather than an untyped shared credit threshold.
- Star K_{1,m-1} (m>=2): C=2^{m-1}, exactly m-1 bits. The empty edge signature contains 2^{m-1}+1 different support sets (all leaf-only supports and the center-only support).
- Edgeless graph: C=1 and b_min=0; path P_4: C=7 and b_min=3; complete K_4: C=12 and b_min=4.
- Adding a previously missing edge strictly refines the quotient: the empty support and the two-endpoint support of that edge were previously equivalent and become distinguishable. Accordingly C(G) increases strictly (at least one) under every edge addition.
- A mere count of positive frame bits is not sufficient for general G: the joint graph incidence, source labels and future operations determine which hidden supports can be safely merged. The quotient is certified only for the stated success-language observer and this declared non-feedback-consuming A behavior; direct Link/failed-attempt observability would alter it.

## Reproducible exact Boolean-BRC check

The accompanying JavaScript implements a deterministic source/signed-Port successful-word signature recursion: depth zero has the empty word; at depth h, each enabled distinct label is paired with the depth-(h-1) successor signature. Structural interning gives equality of finite Boolean word languages exactly because action labels are unique and transitions deterministic. Every graph with 1,2,3,4 labeled vertices was checked (1+2+8+64=75), plus four explicit five-vertex graphs. For EVERY initial theta and h=0,...,5, the implementation compares all pairs of exact language signatures with the predicted edge-set partition. It separately checks class counts and the independent-set fiber formula. Result: 79 graphs, 7356 initial state/horizon signatures, 59406 pairwise equivalence comparisons, all PASS. The general h>=5 statement follows from the above bisimulation, not from extrapolating the finite check.

Examples: m=2: empty=1, star=2, path=2, complete=2; m=3: empty=1, star=4, path=4, complete=5; m=4: empty=1, star=8, path=7, complete=12; m=5: empty=1, star=16, path=12, complete=27; m=6: empty=1, star=32, path=21, complete=58; m=7: empty=1, star=64, path=37, complete=121.

Files: `x6_pairwise_link_graph_brc_verify_r26.js` and `x6_pairwise_link_graph_brc_results_r26.json`.

## Next frontier

Extract a genuine frozen-scope TRIADIC_CLOSURE_E/Cell/Link/Port event admission rule and determine whether it permits source-indexed pairwise Link guards, repeated signed triad returns and the A_{ij} irreversible action. If so, publish an exact source-to-source event morphism retaining origin, Port, frame and provenance. If not, identify the smallest admitted alternative guard and recompute its Boolean-BRC quotient. Also consider bounded observation of failed attempts, or Link feedback after an A action, where the five-step quotient may no longer suffice. Preserve the negative native-admission finding until exact source bytes support transfer.
