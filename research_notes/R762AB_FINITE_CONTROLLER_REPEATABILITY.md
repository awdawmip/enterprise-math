# R762AB — Sharp finite-controller cutoff for repeatable source-typed triadic macros

Date: 2026-11-14 (Asia/Shanghai). Status: AUTHOR-SIDE PROOF + EXACT FINITE CHECK / NOT_REVIEWED / NOT_ADMITTED.

Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Existing source registration: Researcher EM-X6-3050F6, Activity RA-6068F717D991DF54FBBDDEED, session MCP-4b2d70a97f594366a7c94a0f8b45df38. A Source Activity is distinct from an execution CLAIM.
Predecessors: R762V (exact six-step signed X6 path/BRC fibers), R762T (V27/V29 ledger typing), R762AA (three-root ordered PASS scheduling), and original V2/V17 Johnson active-triad frame connection. The present theorem concerns an event's *repeated authorization by a controller*, not a fresh derivation of those counts.

## 1. Source-typed auxiliary macro interface

Choose one native X6 Cell c, four distinct native axis identities a,b,d,e (from the six signed-axis names, without identifying the four axes with a classical plane). Set the consecutive active triads

S0={a,b,d}, S1={a,b,e}, S2={a,d,e}, S3=S0.

Each triad has three named equal nonzero force quanta; the canonical equal-quantum triple meets the P000 arity and pairwise PERP_E premise. By the *conditional* V17 replacement-frame law, one traversal S0->S1->S2->S0 has holonomy h=(b d) on the original three axes. The active triad returns to S0 and the Cell c is unchanged in this auxiliary local relation-event model.

For a second, explicitly declared layer, associate to each full macro E the three distinct nonnegative V29 PASS entries b->d, d->a, a->b. Index the ordered port set (a,b,d). One macro has

M = [[0,0,1],[1,0,0],[0,1,0]], I=M1=(1,1,1), O=M^T1=(1,1,1), u=I-O=0.

For k successive authorized macros: M_k=kM, I_k=O_k=(k,k,k), Omega_k=k(M-M^T); for k>0 rank_Q(Omega_k)=2. The V17 frame holonomy is h^k, with h^2=id. This is a fully source-labelled candidate interface. The chosen PASS attachment and trigger law are *additional hypotheses*, not an asserted P000-native admissibility theorem; V39 transport is not determined by the interface.

The observer O_k records c, S0, the k named event occurrences/ordered sources, exact V29 counts, and the conditional V17 h^k, but **does not query the controller's event-enabling predicate** or read its private state. This makes observer/future-operation scope explicit.

## 2. Theorem AB1 — sharp repeatability cutoff with a known finite controller

Let Q be any deterministic partial unary event controller, with at most s>=1 reachable control states, and transition f:Q partial->Q for the single full macro E. The legality of the next E depends only on the current control state (autonomous, time-homogeneous Markov control). If the first s consecutive E events are legal, then E can be repeated without bound. The cutoff s is sharp uniformly over controllers of size at most s: there is an s-state controller in which the first s-1 macros are legal and the s-th is illegal.

Proof: write x_0,...,x_s for the states along the first s legal transitions. Since |Q|<=s, x_i=x_j for some 0<=i<j<=s. Determinism makes the segment x_i,...,x_(j-1) a periodic loop. Each state in this loop occurs as the source of one of the first s legal transitions; every transition remains enabled on subsequent visits. Thus the run is infinite. For sharpness let Q={0,...,s-1} and f(i)=i+1 for i<s-1, while f(s-1) is undefined. Starting at 0 gives exactly s-1 legal macros. This includes s=1. QED.

For an exactly N-long legal prefix followed by an illegal E, any such standalone deterministic controller has at least N+1 distinguishable reachable control states: after prefixes E^i and E^j (0<=i<j<=N), the suffix E^(N-j+1) is legal after i but illegal after j. This is a direct finite unary Myhill–Nerode distinguishability argument. The sharp chain construction uses exactly N+1 states, hence needs ceil(log2(N+1)) bits in an independently stored fixed-length controller-state encoding. **The internal-state bound applies to the standalone controller interface**; if enabledness is permitted to read cumulative V29 counts, external time or other unbounded state, those variables already supply additional memory and must be included in the state bound.

## 3. Theorem AB2 — no uniform horizon from static triadic closure and passive BRC outputs alone

For every integer N>=1, construct two typed model completions agreeing on P000's static three-force closure and on every O_k for 0<=k<=N:

A (renewable): the auxiliary event controller has one state with an E self-loop, hence arbitrary repetition is legal.

B_N (finite budget): controller states 0,1,...,N, with E: i->i+1 for i<N and E disabled at N. Its static equal-quantum triad relation remains true; only permission to fire the full macro depends on the extra budget state.

Both use the same c, same named sources and active-triad replacements, identical M_k, u_k and h^k for every legal k<=N. At prefix N the two event-history observers agree but A permits E^(N+1), whereas B_N does not. The distinction requires an event-legality query or the model-specific state update. Thus no **uniform fixed finite observation horizon over this unrestricted controller class** certifies indefinite repeatability. In the bounded autonomous s-state class, AB1 supplies the exact cutoff s.

This is a sharp conditional independence/identifiability result: the missing native event trigger and state-update rule is a substantive mathematical dependency. It does not negate P000's primitive triadic-balance axiom, which remains satisfied in both completions. It is not a claim that a genuine TRIADIC_CLOSURE_E force dynamics has already been constructed.

## 4. Exact verification

Script: research_notes/R762AB_FINITE_CONTROLLER_VERIFY.py.
Evidence: research_notes/R762AB_EVIDENCE.json.

The checker exhausts every deterministic unary partial transition table on s=1..6 labelled states (126,125 controllers), tests the sharp cutoff against every table, validates the sharp chain, checks 180 source-labelled V17 replacement loops (20 base triads x 3 entering axes x 3 preserved axes), checks both model families for N=1..64 and all 45,760 pairwise prefix-distinguishability witnesses. Arithmetic is exact integer/set permutation only. The AB1/AB2 universal assertions follow from the proofs, not from extending this finite census.

## 5. Next discriminating scientific unit

Extract an actual task-frozen source-admitted TRIADIC_CLOSURE_E transition as a partial function on a declared state (Cell, named Force/Link/Port incidence, inventories and any internal fields). Determine whether it is autonomous and finite-state after *operation-safe BRC compression*; if a bound s exists, apply AB1 to certify infinite legal repetition from s concrete steps. If it depends on unbounded V29 counts, native time or field state, derive the correct dependency and its state-dependent admissibility criterion instead. Then compute actual V17/PASS-TRANSFER/V39 transported outputs, keeping chart transport, local causal counts and physical force event authority distinct.

Frozen P000/ACTIVE worldview unchanged. Author-side result is not a Source Result or independent Driver acceptance.
