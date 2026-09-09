# Phase rigidity, parallel shape charts, and the cost of forgetting a residue

Status: RESEARCH_NOTE / ELEMENTARY_DERIVATIONS_AND_EXACT_FINITE_CERTIFICATES / NOT_PROMOTED
Progress-Event-ID: NOLLM-PHASE-RIGIDITY-CHARTS-20260909-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Session: local-chat-nollm-hecke-20260909-c6c82 (locally assigned, not an authenticated platform ID)
Mode: TASK_RESEARCH / direct user continuation / no Task-ID or CLAIM
Date: 2026-09-09
Source snapshot: enterprise-math@141f8e547192b6ae9448c614664cc5023eca3ecd
Parent note: research_notes/nollm_two_inert_5_11_boundary_field_20260909_c6c82.md at f3118d5bdbceca07bcc4f1395db19c676c109713
Pinned predecessor: experiments/nollm_two_inert_511_20260909_c6c82.py at c49d46d33ee9a5103b608bcc02713c0b11c8bdfe
Predecessor SHA256: db00742a81241d10883299253307fb1ee7831b7703bf710f88288606998f53b4
New code: experiments/nollm_phase_rigidity_charts_20260909_c6c82.py

## 1. Question and scope

Can changing the initial 11-chain or adding an adaptive phase avoid the parent's reachable unit-thin 55 lattices while preserving the original quotient/refinement and address semantics?

All geometry is the ordinary rank-two axial lattice with Q(q,r)=q^2+qr+r^2. This is a comparison/research slice, not a P000 or Nollm runtime change. Quotient capacity multiplication is not scalar multiplication of ordinary integer labels. The six preceding checkpoints are consumed, not restarted. New work distinguishes: a fixed sublattice chain; a parallel chart observer; an explicitly transported CRT label; and an ambient residue with its missing coordinate restored.

## 2. Changing the initial chain cannot remove the bad states in the frozen family

Use G7=[[1,-2],[2,3]], G13=[[1,-3],[3,4]], G19=[[2,-3],[3,5]]. Write the inverse G7 cycles starting at horizontal slope 0 as

F5: (0,1,infinity,3,4,2),
F11: (0,3,5,7,10,8,9,4,infinity,6,1,2).

Their cycle positions (i,j) lie in Z/6 x Z/12. Direct exact calculation on every line gives translations

7: (1,1); 13: (3,11); 19: (2,9).

The first and third already generate the full group: (2,9)-2(1,1)=(0,7), and 7 is invertible modulo 12. This supplies every vertical translation and then every horizontal translation. In a finite group inverses are nonnegative powers, so restricting to positive-length refinement words does not remove reachability.

Therefore ANY initial pair of index-5 and index-11 lines has the same 72-state orbit. Changing a basis of the same index-11 lattice does nothing, and choosing a different index-11 lattice merely changes the starting point. This covers every first intermediate index-11 lattice, not only a bounded matrix search. Later even/odd chain choices cannot prevent a bad continuation while both first odd phases remain active.

The three unit-thin line pairs are (0,0),(-1,-1),(infinity,infinity). The executable builds shortest positive words to this SET from all 72 states and verifies every returned word. Maximum shortest distance is 5 using {7,13,19}, and 8 using {7,19}. Distance histograms are respectively

0:3, 1:9, 2:18, 3:24, 4:15, 5:3;
0:3, 1:6, 2:9, 3:12, 4:12, 5:12, 6:9, 7:6, 8:3.

This means EVERY start has SOME bad continuation of at most five steps, not that every five-step path is bad. It rules out a uniform avoidance guarantee for arbitrary permitted words in the frozen family. It is not a no-go for all choices of split generators, nonnested models, extra state, or all memory fields.

## 3. A phase is not freely steerable during a coprime refinement

Let L' subset L have finite index m with gcd(m,p)=1. Since m L subset L', their images modulo p^r agree for every r>=1: choose t with tm=1 mod p^r, and represent x mod p^r by tm x in L'. Hence a coprime-index refinement cannot change the inherited p-primary constraint.

For an active one-line condition modulo 5 or 11 this fixes the physical line. Removing a prescribed split similarity E forces the normalized line to become E^(-1)l. Replacing it by a preferred line while claiming the same ambient nested quotient would change the operation. The code checks 1,152 active-line inheritance cases across the full finite atlas and the five active directions.

A rigid rotation of the camera leaves intrinsic aspect unchanged. Changing a matrix basis leaves the lattice unchanged. The new obstruction concerns an actually different phase/lattice, not either of those harmless changes of presentation.

## 4. Parallel charts can improve geometry substantially

Keep the mod-5 starting line fixed and retain several alternative mod-11 initial lines. Their cycle offsets d are fixed in Z/12; every split operation transports all charts by the same j increment, so relative offsets remain constant. This uses existing parent geometry/selector rules unchanged in each individual chart.

Use a basis-independent geometric quantity

rho_V(H) = R_cover(H) / r_in(H),
r_in(H)^2 = lambda_1(H)^2 / 4,
R_cover(H)^2 = max Q(v) over exact Voronoi vertices.

This is NOT the singular-value ratio and NOT the point-cloud covariance axis ratio. A regular hexagon has rho_V=2/sqrt(3), not 1. Both numerator and denominator scale equally, so a finite normalized certificate holds under all common scales and rotations.

For each of the 72 doubly active shapes, shortest length and Voronoi vertices are computed using the unchanged predecessor's exact Gauss/Voronoi arithmetic. For k charts minimize

max_(i,j) min_(d in D) rho_V(H_(i,j+d)), |D|=k.

Translation symmetry permits 0 in D without loss for this worst-state objective. All 1,11,55,165 normalized offset sets for k=1,2,3,4 are checked using rational squared values. Results:

charts | example optimal offsets | squared worst ratio | worst ratio
1 | {0} | 20593444/9075 | 47.63664584695
2 | {0,1} | 172/25 | 2.62297540972
3 | {0,1,5} | 13468/3025 | 2.11003113839
4 | {0,1,2,3} | 364/121 | 1.73443491167

These are exact restricted minimax optima within the 12 specified relative 11-line choices, NOT optima over all lattice embeddings. The bound is for the doubly active 5/11 portion. In particular, when the 11 phase is inactive these alternative charts do not change an isolated mod-5 shape. No global all-parity roundness bound is silently inferred.

A chart chosen by this finite cost table depends on the current phase, not the individual memory. Each selected complete section remains a valid 55-element hole-free centrally symmetric section. Switching between such sections is a separate semantic/transport problem; the geometry bound alone does not solve it.

## 5. Naive chart switching actually loses distinguishability

Take source L0 = Z(1,0)+Z(0,55) and target
L1 = { (q,r): r=0 mod5, r=3q mod11 }.

For an index-p line of finite slope l let chi_l(q,r)=r-lq mod p; for the vertical line use q mod p. The joint label is (chi_l5 mod5, chi_l11 mod11), with 55 values.

Reduce each of the source's 55 canonical representatives directly into the target quotient, without retaining a source label. Only 27 different target classes remain. Multiplicities are four singleton classes, eighteen double classes and five triple classes. An explicit collision is

(-2,5), (0,0), (2,-5),

which are THREE different source classes but the SAME target class. Thus this is more than a question of moving points: identity-by-ambient-reduction merges memories.

The precise obstruction: a natural map [x]_L0 -> [x]_L1 is well-defined iff L0 subset L1. Distinct equal-index lattices are not nested. The source port lacks the information needed for the intended future observer.

## 6. Two different repairs, with different promises

### A. Explicit CRT-label transport: 55 states remain 55, but ambient meaning changes

On each canonical section the joint label chi is a bijection to F5 x F11. Define

T_(A->B) = chi_B^(-1) chi_A.

Then T_(B->C) T_(A->B)=T_(A->C), and every transport is a permutation. This is an explicit small quotient-coordinate transport, not a proof of ordinary-number multiplication. At the source/target pair above all 55 labels survive, but only 3 physical points stay fixed: 52 of 55 addresses move. Maximum squared hex displacement is 475.

The executable checks every ordered chart pair for all six mod-5 rows: 47,520 point transports. It also checks all ordered chart triples: 570,240 composition identities. Endpoint labels are path-consistent at this FIXED squarefree-index chart interface.

The new rule does NOT preserve the class of the same ambient x in both quotients. It declares equality of their numerical CRT labels instead. No all-depth intertwining with every previous p-power refinement is asserted. A fixed-index cyclic quotient must not be confused with the noncyclic quotients at completed p-pairs. Future global address stability fails when active chart positions change; stable payload IDs could remain separate from geometric caches, but that is an architectural proposal, not an implementation.

### B. Preserve all ambient readouts: retain the missing residue

For arbitrary ambient x and the original observer meaning, keep x modulo
J=L0 intersect L1=11Z x 55Z.

Its index is 605. Each source class lifts to 11 states, distinguishable by the target observer. Every lossless carrier supporting BOTH ambient readouts must distinguish these 605 joint equivalence classes. This is a lower bound for this declared population/future-observer contract, not a universal memory-cost lower bound.

The whole set of 12 mod-11 direction readouts needs no further multiplicative growth: keep the complete (q,r) modulo 11, plus the one mod-5 residue. This gives 5*11^2=605 states. Two distinct mod-11 linear forms already determine both coordinates, so all other line readouts follow. The code enumerates all 605 states, checks joint uniqueness, all source fiber sizes 11, and recovery of every one of the 12 readouts.

If only a predetermined 55-element lifted population is permitted, a chosen transversal or explicit label transport can avoid the 605-state count. Such a choice changes the population/identity contract; it does not recover the old arbitrary-ambient information for free. Similarly, a known full integer coordinate may already provide the required extra data. No blanket claim of '11 times more storage per memory' is made.

In the original refinement language this common lift is precisely an extra factor 11 of capacity: completing the missing 11 coordinate, not just rotating a picture.

## 7. Reuse, tests and boundaries

REUSE_EXECUTED: predecessor SHA256-pinned atlas H, projective actions, exact Gauss reduction, exact Voronoi vertices, existing boundary selectors and integer hull checks, without modifying predecessor files. EXTEND_EXISTING_TOOL: task-local finite orbit/shortest-word certificate, restricted chart minimax and explicit observer/transport audit. No new global BRC family is claimed.

Retained carrier is explicitly different in A and B. A retains an abstract CRT label and chart identity; B retains the ambient joint residue. Roundness, covariance, and one chart's support are observers. The 55->27 collision is the BRC fiber-nonconstancy witness; the 605-state lift is its exact repair for the ambient contract.

Executed: 72 complete base sections / 3,960 point appearances; 232 normalized chart-set candidates; 144 explicit bad-path witnesses (72 for each generator set); 1,152 inheritance checks; 47,520 bijective transports; 570,240 transport compositions; the full 605-state ambient joint observer.

No Monte Carlo or floating tolerance decides these checks. Decimal ratios are display readouts of rational squared-radius certificates. This remains research with elementary derivations and exact finite verification, not Lean formalization, Working Truth, Foundation or Nollm runtime integration.

## 8. Next bounded research unit

Do not continue searching for a universally safe fixed initial 11 line under the unchanged generators: that route is now closed by the transitive action. The next useful unit is a typed interface choice: test whether a separate geometric cache with explicit label transport can preserve enough useful neighborhoods while payload addresses stay fixed, OR measure the required retained local residue in a fuller ambient carrier. For all-depth transport, establish an actual commuting square with the noncyclic prime-power refinement maps before transferring the fixed-index cocycle claim. Do not count arbitrary conjugation of scalar-label multiplication as a geometric solution.

Classical comparison only: Natarajan, Hong and Viterbo, Lattice Index Coding, arXiv:1410.6569; Li, Gan and Ling, Coprime Sensing via Chinese Remaindering over Quadratic Fields, arXiv:1808.07505. CRT, lattice quotient codes and coordinate changes are classical. The exact frozen-family obstruction, restricted chart tradeoffs and information-loss witness above are the present project synthesis; no priority claim is made for the classical ingredients.
