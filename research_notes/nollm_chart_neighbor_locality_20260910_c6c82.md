# Chart locality audit: exact identity does not preserve nearby memories

Status: RESEARCH_NOTE / ELEMENTARY_DERIVATIONS_AND_EXACT_FINITE_CERTIFICATES / NOT_PROMOTED
Progress-Event-ID: NOLLM-NEIGHBOR-LOCALITY-20260910-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Session: local-chat-nollm-hecke-views-20260909-c6c82 (locally assigned continuity key, not a server ID)
Mode: TASK_RESEARCH / direct user continuation / no formal Task-ID or CLAIM
Date: 2026-09-10
Source snapshot: enterprise-math@89f8ed2df9e7d5ebe42612e063b50f6be5ee315e
Parent note: research_notes/nollm_prime_power_chart_transport_20260910_c6c82.md at cc63021fd1c4f1bc762f409c8f242651b1db5a72
Unchanged executable dependency: experiments/nollm_prime_power_chart_transport_20260910_c6c82.py at c019c1dee6f52fec6db913f47672d4821e3d0414
Dependency SHA256: f6f80926e626944203e4537345737bc64c470190d9da32f14290b907fbe2cb47
New executable: experiments/nollm_chart_neighbor_locality_20260910_c6c82.py

## 1. Scope and exact question

The eight recorded activity events are consumed, not restarted. The parent constructed additive transports between rotating prime-power towers. The present question is what these transports do to geometric neighbor relations and displacement, and whether a bounded two-way alternative exists.

All statements use the ordinary rank-two integer lattice with Q(q,r)=q^2+qr+r^2. This is a research/comparison slice, not P000-native geometry and not a change of Nollm runtime, physical layers, or direction rules. Geometric nearest neighbors are an explicit proxy; no semantic memory corpus was tested. Capacity/refinement multiplication remains distinct from ordinary scalar-label multiplication.

The fixed population for the primary comparison is an even checkpoint X_m=(Z/mZ)^2, m=p^t, p=5 or 11, with ALL m^2 classes. Periodic boundary conditions remove artifacts of cutting open a torus. The physical unit directions are D={(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)}. Graph distance is min over lifts of max(|q|,|r|,|q+r|). Squared Euclidean distance is min Q over lifts. No covariance or matrix singular ratio is substituted for these distances.

## 2. Reused transport, exact edge destruction, and a seven-point witness

Reuse the parent's normalized source-line 0 to target-line 3 map

U=(1/13)*[[1,-3],[3,4]],

interpreted modulo m by inverting 13. At even levels it is an additive permutation of X_m. An edge x -> x+d maps to Ux -> Ux+Ud. Thus all vertices have the same image step set UD; full edge statistics factor through SIX generators, not through the total occupied support.

For p=11:

period m | states m^2 | original unit edge becomes (graph hops) | squared Euclidean edge length
11       | 121        | 6                                      | 28
121      | 14641      | 37                                     | 1117
1331     | 1771561    | 717                                    | 409129

All six directions have equal cost because U commutes with W. Original one-hop edge retention is exactly ZERO in these cases. U^-1=[[4,3],[-3,1]] is integral and has unit-edge graph cost 4 for m>=11: the forward and inverse distortion are asymmetric.

The growth is not merely observed. Every integer lift v of U(1,0) satisfies 13v=(1,3)+m z for an integer z != 0. Therefore its graph distance is at least (m-3)/13. An elementary choice of periodic representative gives an upper bound O(m). This specific normalized forward edge stretch is Theta(m).

There is also a modular obstruction independent of the particular lift. By the parent's three-rotating-line argument, ANY all-depth additive natural isomorphism V between two charts reduces modulo p to a nonzero scalar times the corresponding nonsplit-torus matrix. If target line b is not in the three-line W orbit of a, V cannot send even ONE unit direction to a unit direction modulo p: commuting with W modulo p would then identify V with a hex unit rotation, forcing b into that orbit. Hence none of the six physical neighbors survives at any even depth for such a cross-orbit chart pair. This does not apply to all chart changes; unit rotations are an important counterexample to an unqualified claim.

The concrete seven-site patch {0} union D has 12 internal undirected unit edges. Under U modulo 11, its seven distinct images have ZERO internal physical unit edges. All 12 edges survive under transported directions UD. The entire 121-site occupied geometry is unchanged; only attaching labels to it changed. This is why occupancy and shape do not certify preservation of memory relations.

## 3. Migration distribution is uniform, even after alignment by hex rotations

For distinct rotating charts, the parent's rigidity argument gives det(V-I) a p-adic unit. Consequently x -> (V-I)x permutes X_m. Thus the displacement of a uniformly counted class is exactly uniform over the torus, independently of the detailed admissible additive V. In particular only one local class is fixed and

mean squared periodic migration = (1/m^2) sum_(z in X_m) min_(k in Z^2) Q(z+mk).

For the cross-rotation-orbit pair 0 -> 3 the same applies to V-W^j for every j=0,...,5. The effect is not eliminated by aligning the output through a global hex rotation. The executable verifies the exact displacement bijection and second moment for all six alignments through m=121.

After scaling the regular Voronoi hexagon by 1/m, its continuous mean squared radius is 5/36. A Riemann-sum limit, with only O(m) boundary sites, gives

RMS migration / m -> sqrt(5)/6 = 0.372677996...

The constant follows by integrating r^2 over the six congruent triangles of the regular hexagon; it is not a fitted physical law. Exact finite means for p=11 are 186/11, 246060/121, and 327492846/1331 at m=11,121,1331. Their normalized RMS values are about 0.3738242, 0.3726855, and 0.3726781.

RMS migration alone is also insufficient: even a rigid hex rotation may move almost every point while preserving neighbors. The cross-orbit condition and the edge observer must be retained.

## 4. A sparse relational repair preserves the graph, not physical locality

Retain D as relation labels and change its embedded offsets to UD. Then

U(Cay(X_m,D)) = Cay(X_m,UD)

is an exact graph isomorphism. If f is a signal and g(Ux)=f(x), the unnormalized neighbor aggregation satisfies

(A_(UD) g)(Ux) = (A_D f)(x).

Thus graph distances, connected patterns, and the corresponding adjacency/Laplacian operators are preserved under relabeling. This is ordinary generating-set transport, not a new Cayley-graph theorem. The whole additive relation graph can be specified by the two transported basis columns; the six offsets are derived. No list of m^2 individual edge records is required.

A deterministic integer-signal test on all 121 vertices gives exact equality at every vertex with transported offsets; retaining the old physical offsets gives different aggregates at 113 vertices. The seven-site patch recovers all 12 original relations. This is a geometric/synthetic test, not measured semantic quality.

Degree six plus an optional self-message is NOT proof of compatibility with a physical fanout-seven implementation: long offsets still require routing, address computation or nonlocal accesses. Keeping the same physical six-neighbor stencil loses the relation, while moving the relation to long offsets preserves it but pays locality cost.

The parent's ambient look-ahead route is a different identity contract. Retaining all natural observations can avoid relabeling the underlying ambient object, with one extra base-p digit at odd depth. It does not make an occupied coarse cell a one-to-one ID for all hidden joint states, nor make different projected neighbor sets equal. No same-population claim comparing those projections to the transported-ID experiment is made.

## 5. Two-sided bounded physical stretch is equivalent to an integer-unimodular lift

Consider a compatible additive family on all even X_(p^t). Such a family is given by one V in GL2(Z_p). Suppose there is a depth-independent graph-hop bound B on images of all six unit directions under both V and V^-1.

For t sufficiently large, each bounded image of e1,e2 has a unique integer lift inside [-B,B]^2. Compatibility between moduli forces these lifts to become constant: two such vectors differing by a multiple of p^t must agree once p^t>2B. Let their two columns form C in M2(Z). Applying the argument to the inverse yields D in M2(Z). Since CD=I modulo every p^t, CD=I in integers. Hence det C=+1 or -1.

Conversely a fixed C in GL2(Z) and its integer inverse have fixed finite D-word lengths. If its mod-p action maps the three rotating source lines to the three target lines, C maps every lattice in the source tower exactly onto the corresponding target lattice. It is therefore an additive natural tower isomorphism with a uniform two-sided hop bound.

This gives an exact criterion, not an unbounded search. For the SAME numerical first-layer label normalization as the parent, mod-p three-line compatibility determines V modulo p exactly. Its determinant is 2 mod5 and 6 mod11 for the pair 0 -> 3, neither of which is +/-1. Thus neither normalized transport can have uniformly bounded TWO-WAY physical edge stretch at all depths. This is stronger than observing growth for the displayed rational U, but only under the stated additive/natural/normalization contract.

Allow an invertible first-layer scalar relabeling c instead. The possible determinant residue becomes c^2 det(U). For p=5 it is always 2 or 3, never 1 or -1=4. Therefore even that relaxation cannot yield a uniformly two-sided bounded additive natural map for this 5-chart pair.

For p=11 the possible residues are {2,6,7,8,10}; the only available unimodular sign is -1=10, attained at c=3 or 8. Orientation reversal is REQUIRED for a bounded integer lift of this pair. This is a local modular determinant obstruction, not a no-go for all memory fields, all chart pairs, nonadditive maps, higher-dimensional layouts, or changing the tower definition.

## 6. Explicit 11 rescue: 26 hops, independent of depth

A feasible integer matrix is

C=[[-4,1],[21,-5]], det(C)=-1,
C^-1=[[5,1],[21,4]],
C mod11 = 3 U mod11.

It maps the three rotated source lines to the three target lines. Therefore C L_(0,k)=L_(3,k) at EVERY depth k. It preserves addition and all coarse projections. Its numerical first-layer label is multiplied by 3, so it is not an unchanged continuation of the parent's fixed numerical label convention. This is an explicit new coordinate convention, not information loss; multiplication by 3 is invertible modulo 11.

Forward unit directions require at most 26 hex steps, and so do inverse directions. The attained direction costs on the infinite lattice are 21,5,26 (plus their negatives) in one direction and a permutation of 26,5,21 in the other. At periods 11,121,1331, maximum forward periodic costs are 5,26,26. The all-depth bound follows from the fixed integer words, not from those samples.

The bound 26 is optimal in this declared class. Any competing bound <=25 would put all four entries of its integer-unimodular lift in [-25,25]. Modulo 11, three-line compatibility restricts it to cU, and determinant +/-1 leaves only (c,det)=(3,-1),(8,-1). The executable enumerates every permitted first-three-entry triple, solves for the fourth entry using the determinant equation, and finds NO candidate of two-sided D-hop cost <=25. Repeating at bound26 finds the displayed matrix and other witnesses. No claim of optimality over nonadditive or history-dependent transports is made.

The new map still retains zero original one-hop neighbors for this cross-orbit pair, and it still has the same macroscopic displacement distribution. It prevents the edge span from growing with depth; it does not leave addresses fixed, make neighboring points adjacent, or reduce the global migration RMS.

It uses shear and reflection rather than pure rotation/scaling. Also the 26-hop statement is for the SINGLE 11 component's periodic hex plane. It must not be transferred to a common global coprime layout with other prime components held fixed. For example, demanding identity on an entire mod5 vector factor fixes determinant +1 modulo5, whereas the local 11 bounded lift here requires determinant -1; one common global integer-unimodular matrix cannot meet both determinant signs. Prime-local CRT transport remains algebraically valid, but joint physical locality needs its own analysis.

## 7. Digitwise alternative and measurements

The unchanged parent's digitwise alternative is also evaluated on the SAME even population. For p=11, physical unit-edge retention is 1/3 at depth2 and 100/363 at depth4. At depth4 its maximum image edge span is 68 steps, versus 37 for the normalized additive map and 26 for the new integer lift. It can keep more literal nearest neighbors and still have worse extreme edge displacement. The parent's exact nonadditive carry witness remains applicable. No optimization claim is made for the digit map.

Finite validation from the executable:
- 540 chart-pair/depth generator rows; 378 cross-rotation-orbit instances have zero unit-edge retention.
- Ten fully enumerated same-population cases: 45,586 class appearances and 273,516 directed physical-edge checks. 181,044 transported additive/lift edges are checked pointwise.
- Exact entire-torus displacement moments through periods125 and1331 for 5 and11 respectively, computed rowwise; no million-vertex graph adjacency matrix is allocated.
- Full 11 integer-lift bijection/naturality checks for 16,104 classes at depths1..4.
- 24 exact lattice-generator inclusions, forward/inverse at both parities, including depth101; these are matrix checks, NOT enumeration of 11^101 states.
- Complete integer-lift exclusions at hop budget25 and attained witnesses at26.
- 1,542 metric checks against a larger translate enumeration.
- The seven-site disconnected-patch witness and complete 121-vertex message aggregation comparison.
- Two fresh executions of the final source produce byte-identical results and lift-certificate JSON.

Counts across cases are appearances, not that many independent memories.

## 8. BRC reuse and next frontier

REUSE_EXECUTED: unchanged SHA256-pinned prime-power matrix, canonical representatives, all-depth tower bases, projection and digitwise transport functions. EXTEND_EXISTING_TOOL: task-local geometric distance/edge audit and finite lift certificate. COMPOSE_APPLIED: edge differences reduce the translation-invariant observer to six generators; this reduction is proved before compression. Full class identity and the identity convention remain in the state. Counts, occupancy and radius scores do not establish neighbor preservation. Positive mass, deterministic relabeling and semantic quality are not identified.

The useful new frontier is a three-way tradeoff: exact normalized labels versus bounded two-way geometric locality versus allowable coordinate changes. Transporting a six-port relation graph preserves it exactly but may use long physical edges. The single-11 reflection lift bounds those lengths after an explicit relabeling; the analogous 5 pair meets a determinant obstruction.

Still open: an optimized JOINT coprime-plane lift or routing representation; first-label conventions consistent with the intended semantics; nonadditive bounded-distortion alternatives; real semantic-neighbor tests; arbitrary-prime bounds; and the original intrinsic scalar-multiplication memory embedding. No production architecture, Foundation status or mathematical acceptance is changed.

Classical context: A. Ganesan, Cayley graphs and symmetric interconnection networks, arXiv:1703.08109; D. W. Morris, J. Morris and G. Verret, Isomorphisms of Cayley graphs on nilpotent groups, arXiv:1603.01883. The elementary generating-set transport above is classical. No priority claim is made for Cayley graphs, p-adic compatible residues or unimodular lattices; the present work is the explicit tower/locality audit, arithmetic obstruction, and certified 26-hop witness under its stated restrictions.
