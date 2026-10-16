# X6 future-contact memory: Phase A original freeze

Candidate-ID: EM-FREE-CF1677-X6-CONTACT-MEMORY-20261016
Researcher-ID: EM-FREE-CF1677
Mode: FREE_AXIOM_DISCOVERY
Activity: RA-FREE-CF1677-20261016
Session: LOCAL-CODEX-SUBAGENT-root-native-free-discovery-20261016-CF1677
Session type: locally assigned stable key for the actual current Codex subagent; no platform chat identity attestation and no Native Task session/claim.
State at freeze: BLIND_CANDIDATE_FROZEN, RAW and unaudited; the state name does not assert clean blindness.
Blindness-status: ANCHOR_EXPOSED.

## Origin and substrate

The question was generated after the actual lightweight activity startup guard returned activity_allowed=true, persistence_allowed=true and CONTINUE_ACTIVITY. Its authorized field correctly remains false: this activity grants no formal Task execution authority.

Before question generation I read P000, Heartbeat X6/time, the FREE substrate and their mandatory observer/residual/weighted companion contracts. No downstream result, Task or route body was loaded to select the question. An overly broad initial AGENTS filename search exposed historical path names, and the mandatory registration parent Git-commit metadata exposed its upstream commit message. These are incidental exposures and cannot be unread; I do not claim CLEAN independent discovery. The original exposures are retained in this conversation and are not converted into mathematical premises. After the question had formed, the native torsor contract was loaded for its exact spatial typing and the candidate state machine for this freeze. The torsor document includes downstream explanatory sections; their appearance is disclosed and does not turn this freeze into a clean-context replication.

Foundation snapshot refs (Git blob identities from actual connected GitHub full-file responses):

- p000_reality_foundation.json: bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.
- definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json: 94a02d067be2b039ca4c0f7ffedb5ebde8430e08.
- definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md: c83a4fab017a819f7adac1d037946730a8d16d67.
- definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json: 3923890d77a02d84b772f789e6912dd14f220d14.
- definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json: de980f972de840c55d2535dbf4e40be7e03659ed.
- definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json: f375a059fa4af8c6eefaddb4d4a8689a0c063674.
- definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md: e266c103cae02550c8bbaa794958f3423b41d151.

Worldview snapshot: the locked P000 and Heartbeat contracts above; no additional worldview premise. P000 has no proof obligation and is not a falsification target.

Primitive dependencies: the native affine Z^6 Cell torsor, the twelve signed unit coordinate steps, separately typed discrete step order, and the exact observer/future-language preservation requirement. The positive-weight carrier is respected but not needed: each history and probe here is deterministic; no signed/amplitude cancellation, triadic-force dynamics, physical calibration or stochastic ensemble is asserted.

Semantic layer: a conditional theorem about a declared path observer and its sufficient memory over the full native X6 coordinate graph. This is not a new axiom, not a claim of full packet-state completeness, not a native plane or a lower-dimensional world. All six spatial axes remain present. Raw signed proof coordinates are internal chart displacements, not exported final public Cell addresses.

## Self-generated question

If a native walker must label at each future step whether its new Cell has occurred anywhere earlier in its history, what exact old-history information is sufficient for a horizon H, and can a bounded internal state do this uniformly in H even when the current Cell and clock are supplied separately?

The structural motivation is intrinsic: endpoint equality does not preserve all ordered-path distinctions, but retaining an entire ordered history may also retain more than this particular future observer needs. I seek the exact scope-typed compression and a matching resource obstruction, without presupposing a dynamical law.

## Declared population and future language

A past is any finite native coordinate walk p=(x_0,...,x_T), with x_{i+1}-x_i one signed unit step. Repeated Cells are allowed. Its visited set is V(p)={x_0,...,x_T}, and its current Cell is x=x_T.

Time is the separately typed integer step order t. It is not a seventh spatial coordinate and has no physical-time calibration. The lower bound below compares histories at exactly the same T.

A continuation u=(s_1,...,s_k), 0<=k<=H, is any word in the twelve native signed steps, including after earlier contact events. Let y_0=x, y_j=y_{j-1}+s_j. The observer returns the complete bit word

  b_j=1 iff y_j belongs to V(p) union {y_1,...,y_{j-1}}.

Thus contacts are reported step by step and do not absorb or stop the walk. Current Cell x, clock T, and remaining horizon are separately supplied. No other past-dependent observer or future operation is admitted into this lease.

Write B_H(x)={z: ||z-x||_1<=H}; this is a reachability ball in the coordinate graph, not the P000 quadratic-length ball.

## Candidate theorem A: exact quotient and online update

For pasts p,q with the same current Cell x, their future contact words agree for every continuation of length <=H if and only if

  V(p) intersect B_H(x) = V(q) intersect B_H(x).

Proof of sufficiency. Every continuation position lies in B_H(x). Equal retained membership gives equal old-history contact bits; membership in the new continuation prefix depends only on the common continuation. Hence every bit agrees.

Proof of necessity. If c is in the symmetric difference inside B_H(x), then c!=x, since both pasts include their current Cell. Take a shortest native coordinate path from x to c. It has length <=H and no repeated Cell. At its final step c has not occurred in the continuation prefix, so its bit is exactly the old-history membership of c. The two output words therefore differ, whether or not earlier bits already differed.

For online use with r steps remaining retain S=V intersect B_r(x). On step s, first report membership of x'=x+s in S. Then update

  S'=(S union {x'}) intersect B_{r-1}(x'),  x:=x',  r:=r-1.

This is exact because B_{r-1}(x') is a subset of B_r(x). The fixed fact x in V can be implicit. Therefore at most |B_H|-1 history bits suffice, in addition to the separately retained Cell, clock and horizon. No old path order or multiplicity is needed by this declared observer. This is a scoped safe quotient, not permission to erase those data for other observers.

The exact ball cardinality is

  N_6(H)=sum_{j=0}^{min(6,H)} 2^j * binom(6,j) * binom(H,j).

To count: select the j nonzero axes, select their signs, and distribute a positive total <=H among those j absolute coordinates. The latter number is binom(H,j). In particular N_6(H)=Theta(H^6).

## Candidate theorem B: same-Cell, same-clock lower bound

For H>=1 put q=floor((H-1)/12)+1 and K=q^6. There are 2^K actual past walks, all with the same start Cell, the same final Cell x=0 and the same length T<=12K-4, whose H-horizon future contact signatures are pairwise distinct. Consequently every exact retained-state encoder needs at least K bits in the worst case, even when Cell, clock and H are free side information. Combined with A, the worst-case history-memory order is Theta(H^6).

Construction, entirely inside X6. Choose a raw chart anchored at the common final Cell 0. Index z in {0,...,q-1}^6 and define

  c_z=e_1+2z,   a_z=c_z+e_2,   d_z=a_z+e_3.

The K target Cells C={c_z} all lie in B_H(0), because ||c_z||_1=1+2 sum_i z_i<=1+12(q-1)<=H. They have first coordinate odd and all other coordinates even. Attachments a_z have second coordinate odd, so do not lie in C. Dummies d_z also do not lie in C.

Make a fixed connected attachment graph by joining neighboring z indices. An index edge in coordinate j!=2 is realized by the two signed unit steps in axis j between its attachments; every intermediate Cell has second coordinate odd. An index edge in coordinate 2 is realized, in its positive orientation, by

  a -> a+e_3 -> a+e_3+e_2 -> a+e_3+2e_2 -> a+2e_2.

Its interior avoids C because either the second or third coordinate is odd; reverse traversal has the same property. This embeds a spanning tree on the attachments with each edge length at most four. A fixed depth-first traversal returns to its starting attachment and has length at most 8(K-1). Reach a_0=e_1+e_2 from 0 by steps e_2,e_1, and return by the reverse route; these four total steps avoid C.

At every attachment, on its designated first visit, first execute the fixed dummy excursion a_z->d_z->a_z. Then for the selected bit epsilon_z execute either a_z->c_z->a_z when epsilon_z=1, or a_z->d_z->a_z when epsilon_z=0. Each choice has length two. The two excursions contribute exactly 4K steps and all non-target visits are independent of epsilon. No skeleton or dummy step visits C. Thus the final visited set intersects C in exactly {c_z:epsilon_z=1}, the total time is independent of epsilon, and T<=4+8(K-1)+4K=12K-4.

For different bit strings choose a target c_z where they differ. A shortest probe from 0 to c_z has length <=H, has no repeated Cell, and reports different final contact bits. Hence all 2^K histories require distinct retained states at the identical current Cell and clock. A binary encoding of at most m bits has at most 2^m states, giving m>=K. The six-dimensional exponent is an actual full-X6 construction: all six components of z vary.

## Immediate consequences and discriminating outcomes

1. A fixed finite horizon admits an exact finite local residual; retaining the whole ordered history forever is unnecessary for this language.
2. No fixed finite number of internal states can answer this language exactly for all H and all finite histories. Endpoint and clock do not repair that obstruction.
3. A claimed horizon-independent exact local-state model must either restrict the history population or future operations, change the observer, admit approximation, or retain growing memory. The theorem does not prohibit such restricted models.
4. The original question produces both a positive compression theorem and a negative uniform-memory obstruction, not merely an endpoint counterexample.

## Obvious falsifiers, kill conditions and exclusions

- An actual counterexample to A, its update, the target-avoiding connector construction, or the same-time count kills the corresponding claim.
- Absorbing first-hit detection, continuations forbidden after contact, only a final aggregate bit, a fixed history-length cap, extra non-coordinate jump actions, approximate answers or different future observers are different scopes. No lower bound here is silently exported to them.
- The number H is a step budget; replacing graph reachability by quadratic distance without a bridge would invalidate this exact formula.
- The candidate is derived from the stated primitives and definitions, not a proposed replacement of P000 or an independent physical law.
- Before any novelty or new-tool claim, Phase B must inspect exact current coverage and prior work. A known result closes as reuse/duplicate or a classical analogue. No such comparison has yet occurred at this freeze.

Resource/evidence status: paper proof only; no scientific program, enumeration, floating calculation or formal proof execution has run. Discovery evidence is not independent validation. No RA/session/task/claim is inherited. The mandatory bootstrap expanded beyond the routine three-source soft guideline because P000/X6/FREE explicitly trigger companions; no budget PASS is claimed.
