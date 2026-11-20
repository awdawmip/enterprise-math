# X6 R57 — Collision-pair transport and sharp future-language classes

Date: 2026-11-20 (Asia/Shanghai). Lineage: RS-X6-NATIVE-TIME-DYNAMICS, R44–R56. Status: CONDITIONAL_AUTHOR_PROOF / EXACT_FINITE_BRC_AUTHOR_CHECK / NOT_INDEPENDENTLY_REVIEWED. Historical researcher EM-X6-214D9C and Activity RA-545183ADD4EF71C3E4698AEE are provenance, not new-session authority.

## Frozen foundation and conditional model

Scientific pin: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5, triadic balance, joint-observer retention), preserving the six-axis X6 Cell torsor and time as separately typed event order. Current behavioural protocols are read separately. R56 finished one conditional measurement-radius problem. This unit considers how a Port relabelling could carry a source-specific shared-Cell collision.

Fix p>=1 and J={0,...,p-1}. Two named sources A,B each carry one indivisible balanced three-force frame and may fire once through one of p named Port alternatives. A geometry is the **ordered collision pair** g=(j_A,j_B) in J²: exactly A_{j_A} and B_{j_B} target the same chosen Cell c; all other targets are distinct. State (a,b,o,t): a,b in {-1} union J (spent Port or -1 unused), o in {empty,A,B} (occupant of c), t in {0,1} (whether T used). Root (-1,-1,empty,0). Named events:

- X_i transfers the whole source triad iff X unused and either i!=j_X or c empty; records Port i and occupies c iff i=j_X.
- R clears c iff occupied; it does not restore either source or reset t.
- T fires iff exactly one source used, c empty, t=0. It sets t=1 and reoccupies c with the fired source iff its original Port equals that source's collision index j_X.

Every successful event word is one labelled **positive BRC branch** of unit mass. The complete future observer is the set of successful named suffix words, including the empty suffix. No signed cancellation, additional primitive force, or physical heartbeat duration is asserted. Each fixed g is isomorphic to the original R44 grammar by independent Port index relabelling.

## Theorem R57.1: exact joint future quotient

Disjointly unite the reachable state graphs for every g in J²; identify two states iff their complete named future languages are equal. Then, for all integers p>=1,

\[
\boxed{N(p)=\begin{cases}11,&p=1,\\p^2+10p+2,&p\ge2.\end{cases}}
\]

For p=3, the moving-collision family has **41 classes / 6 bits**, versus **13 classes / 4 bits** for one fixed geometry in R44. This is extra structural observer information, not an extra spatial axis.

**Proof.** Separate states by the number of fired sources.

(0 fired) Each g has one root. If g=(i,k), the two-letter word A_i B_k is forbidden because A_i occupies c and blocks B_k. In every distinct g' that same word is legal because at least one of its two Ports is noncollision. Thus the p² roots have pairwise distinct future languages.

(1 fired) Let X be fired, Y still unused, and j_Y its collision Port. For p>=2, all future behaviour is determined by Y, j_Y and exactly one of five roles: O_before (occupied, T unused); O_after (occupied, T used); C0_before (empty, T unused, X originally fired its collision Port); Cn_before (empty, T unused, X fired a noncollision Port); C_after (empty, T used). Each role occurs for each Y,j_Y, and the exact used index matters only through its collision/noncollision status. For fixed Y,j_Y: occupied vs clear are separated by immediate R; O_before vs O_after by suffix R T; C0_before vs Cn_before by T Y_{j_Y}; C_after vs either clear-before role by immediate T. Different j_Y are separated, for occupied roles, by the one blocked Y_i action, and for clear roles by the suffix Y_i R, legal exactly when i=j_Y. Different remaining source names are distinguishable by named transfer letters (for p=1, first clear c with R when needed). Hence there are exactly 2·5p=10p one-fired classes. When p=1, Cn_before is absent, leaving 2·4=8 classes.

(2 fired) Only R may remain, depending on c occupied/clear. These give two classes independent of geometry, separate from the one-fired and root classes because they contain no future unused-source transfers. The earlier stages are distinguished by availability of transfers from two versus one sources. Sum gives p²+10p+2 for p>=2, and 1+8+2=11 for p=1. QED.

## Theorem R57.2: sharp equivariant collision-memory repair

The independent Port-renaming group G=(S_p×S_p)⋊C₂ acts on the entire **family** of geometries and event graphs by exact labelled transition isomorphisms. Under (π_A,π_B), carry g=(j_A,j_B) to (π_A(j_A),π_B(j_B)); carry the two spent indices, action Port names and occupant source consistently. The C₂ may swap sources. Every transfer, R and T commutes with this action, because its incidence guard uses the invariant equality (used Port index = corresponding collision index). Thus the positive-BRC branch multiplicities transport exactly.

Within a *single fixed* geometry, however, the typed relabelling automorphism group is exactly

\[
\boxed{(S_{p-1}\times S_{p-1})\rtimes C_2,\qquad |Aut_{\rm typed}(g)|=2((p-1)!)^2.}
\]

Proof: c is the unique target of incidence multiplicity two. Its source Ports must be held fixed, or exchanged together with the sources; all other Ports can permute freely within their own sources. Those and only those relabellings preserve the collision graph and R/T guards.

The root distinguishing words A_i B_k prove that an exact deterministic representation of an unknown initial geometry g must retain **at least p² distinguishable collision configurations**, or ceil(log₂(p²)) fixed bits. Keeping g itself achieves this geometry bound; keeping the complete dynamic future quotient requires ceil(log₂(N(p))) bits. If only the diagonal source-common permutation is allowed and g is constrained to (j,j), the corresponding geometry bound is p configurations, ceil(log₂ p) bits.

Accordingly, a proposed source-specific Port rotation that moves a collision Port cannot be an automorphism of the old hard-coded Port-0 collision graph *without transporting its incidence relation*. An admissible native mapping must carry collision metadata or supply a different observer-safe realization. This is a necessary condition on the conditional model's equivariance, not a claim that native X6 rotations equal G. QED.

## Verification and native open problem

The companion Python verifier constructs all positive labelled BRC histories, reachable decorated states, complete successful suffix languages and geometry-root distinguishers for p=1,...,8, checking R44 counts 4p²+16p−3 successful words and 2p²+8p+5 states per geometry. It also exhaustively checks every (S_p×S_p)⋊C₂ element over every geometry/state/event for p=1,2,3. Counts of joint future classes p=1,...,8: 11,26,41,58,77,98,121,146, all PASS. These are author exact checks; the preceding combinatorial proofs cover every p>=1.

The P000 frozen foundation does not itself certify R44's proposed release R or reoccupation T as an admitted native TRIADIC_CLOSURE_E transition. The next discriminating test is to extract a real native Cell/Link/Port event/rotation signature, compute how it carries collision incidence, and test whether the T Y_collision and A_i B_k witnesses survive an event- and provenance-preserving map. A failed specific lift is a scoped obstruction; alternative lifts stay open.

Source references: R44 current file Git blob 70bdc396c7e9ab22081c27f28f4e48f598852157; R56 proof at immutable commit 15aea34d00036d098b51a709306e94987ff3961e. No native PROGRESS, Result, independent Review or physical prediction is claimed.
