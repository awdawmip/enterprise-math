# 5/11 phase control: single-chart obstruction and an exact two-chart roundness bound

Status: RESEARCH_NOTE / DERIVATIONS_AND_EXACT_FINITE_CERTIFICATES / NOT_PROMOTED
Progress-Event-ID: NOLLM-511-PHASE-CONTROL-20260909-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Session: local-chat-nollm-hecke-20260909-c6c82 (local key, not server identity)
Date: 2026-09-09
Source snapshot: enterprise-math@141f8e547192b6ae9448c614664cc5023eca3ecd
Parent: research_notes/nollm_two_inert_5_11_boundary_field_20260909_c6c82.md at f3118d5bdbceca07bcc4f1395db19c676c109713
Executed parent: experiments/nollm_two_inert_511_20260909_c6c82.py at c49d46d33ee9a5103b608bcc02713c0b11c8bdfe
Parent SHA256: db00742a81241d10883299253307fb1ee7831b7703bf710f88288606998f53b4

## 1. Question and scope

Can a different initial 11 direction, or a retained adjustable phase, avoid the parent's reachable very elongated states without hiding a loss of arithmetic identity? We do not add another prime. The six previous activity checkpoints are consumed, not restarted as new research.

This is ordinary rank-two lattice mathematics with Q(q,r)=q^2+qr+r^2, a research/comparison slice. P000 and Nollm runtime are unchanged. Index/refinement multiplication is NOT intrinsic multiplication of ordinary scalar labels. Results concern the frozen 5/11 chains and selected split generators, not every possible memory-field construction.

## 2. Replacing the initial lines cannot solve the fixed-generator problem

Index the inverse G7 cycles by i modulo 6 and j modulo 12:

F5 slopes: 3,4,2,0,1,infinity.
F11 slopes: 8,9,4,infinity,6,1,2,0,3,5,7,10.

With G7=[[1,-2],[2,3]], G13=[[1,-3],[3,4]], G19=[[2,-3],[3,5]], split steps translate (i,j) by

7: (1,1); 13: (3,11); 19: (2,9).

All translations are checked exactly on every line. Already 7 and 19 generate all C6 x C12: subtract twice (1,1) from (2,9) to get (0,7); since 7 is invertible modulo 12 this generates the vertical factor, then (1,1) supplies the horizontal factor. Negative powers can be replaced by positive powers because each translation has finite order.

Thus from EVERY initial line pair all 72 pairs remain reachable. The three unit-thin pairs are (i,j)=(3,7),(1,11),(5,3). Exact directed BFS from all 72 starts shows there EXISTS a path using only 7 and 19 of length at most eight to one of them. Distance frequencies 0..8 are 3,6,9,12,12,12,9,6,3. This is an adversarial/existence statement, not a claim that every input sequence becomes thin within eight steps.

Nor can one simply change an active p-line during a coprime q-refinement while retaining the same nested lattice interpretation. If L' is contained in L with [L:L']=q, q!=p, their p-saturations agree: the finite quotient has no p-primary part. Equivalently their Z_p spans agree. Removing the prescribed new similarity forces the normalized p-line to transform by that similarity's inverse. A replacement direction requires a representation change, a changed generator family, or weakened nesting; it is not a free local correction. This argument does not prohibit other prime-chain designs or additional representations.

## 3. Exact best-basis cost, rather than a poor choice of basis

For C=[[a,b],[c,d]], det C=n>0, reuse the integer conformal defect

Delta(C)=Q(-(b+c),a+c-d).

Its Euclidean singular-value ratio is

K(C)=(sqrt(3n+Delta)+sqrt(Delta))/(sqrt(3n+Delta)-sqrt(Delta)).

For each of the 91 normalized lattices H, minimize Delta over ALL oriented integer bases of H. An initial basis supplies Delta0. Any improving basis has each column of squared hex length no greater than its Euclidean squared Frobenius norm 2n+4Delta0/3. Enumerate every H-lattice vector with Q<=floor(2n+4Delta0/3), and every ordered pair of determinant n. This finite search is complete; determinant n and membership in H prove it is a basis. The initial small unimodular search supplies only the bound, not a restriction on the final optimum.

For the 72 index-55 lattices, minimum-defect frequencies are:
4:9, 7:12, 16:6, 27:3, 28:6, 31:6, 43:6, 52:6, 103:6, 247:6, 676:3, 2187:3.
The last value yields K=55 exactly. Single active 5 costs are Delta=1 or 12; single active 11 costs are 3,16,75. These must be included: optimizing only the doubly odd phase would give a misleading all-prefix bound.

Use the exact common score D=55 Delta_min/n for n in {1,5,11,55}. It is an integer, and K is obtained from D by substituting n=55 in the displayed formula. This allows exact minimax comparisons over all 288 parity/line states without floating-point ranking.

## 4. Two distinct quotient charts give a uniform shape bound

Keep chart 0 and add chart 1 with phase offset

(i,j) -> (i+1,j-1) modulo (6,12).

The two charts generally represent DIFFERENT planar lattices. This is not a camera rotation or a unimodular basis change of the same lattice.

Choose the chart with smaller D, retaining chart 0 on a tie. Exhaustive integer comparison of all 72 fixed phase offsets, over all 288 states, gives minimum worst score 52. The six optimal offsets are (1,9),(1,11),(3,5),(3,7),(5,1),(5,3); the implementation uses (1,11). Hence

K_*=(sqrt(217)+sqrt(52))/(sqrt(217)-sqrt(52))=2.9178930157468606.

One fixed chart has worst K=55. For three fixed translated charts, all C(71,2)=2485 offset pairs were checked after setting the first offset to zero; minimum all-parity score is 31 and K=2.32059031611661. The three-chart selection bound is an additional finite comparison, not a separately implemented three-chart transport. Minimax optimality is only within this declared family of fixed phase translates, not among all geometric embeddings.

The per-state bound is valid at every depth of the declared family: the full lattice is T H, where T is a similarity, so the optimal basis condition ratio of H is unchanged by T. The finite atlas is exhaustive, not a sampled limit.

It also bounds genuine continuous cell roundness. A unit hex lattice has inradius 1/2 and covering radius 1/sqrt(3). For an index N lattice admitting K<=K_*, singular values are sqrt(N/K) and sqrt(NK). Its CLOSED Voronoi cell therefore contains the disk of radius sqrt(N)/(2sqrt(K_*)) and is contained in the disk of radius sqrt(NK_*)/sqrt(3). Numerically these are 0.29270849 sqrt(N) and 0.98622057 sqrt(N). Circumradius/inradius is at most 2K_*/sqrt(3)=3.3692926362. Boundary representative conventions do not affect this continuous bound. It is not a theorem that finite cloud covariance equals this bound or that points are Poisson distributed.

## 5. Exact residue transport: no integer-label decode/re-encode

Let the total index be N=5^a 11^c 7^b 13^d 19^e. Define the chart-0 to chart-1 linear residue map locally by

at 5: y=G7^(-1) x;
at 11: y=G7 x;
at 7,13,19: y=x.

The inverse matrices exist in the respective local rings: 7 is a unit modulo 5^a and 11^c. The Chinese remainder theorem combines these coordinatewise into one matrix D_N modulo N. Using moduli p^exponent is sufficient because N Z^2 is contained in either index-N lattice. The map sends the source lattice onto the target lattice modulo N, is invertible, and induces a bijection between their quotient groups. Local maps commute with W and all selected split similarities. Both quotient transport and the finite phase translation commute with refinement projections. Exact phase commutation is rechecked in 4896 cases.

Select the target chart's existing canonical nearest representative after transporting. No scalar integer address or arbitrary numbering is decoded. This is a local-matrix/CRT isomorphism of the typed residue carrier. Chart ID and exponent/quotient state must be retained; discarding them is not an authorized compression.

If visible refinement is defined using these natural quotient isomorphisms, both factor orders have the same endpoints and corresponding parent fibers. This does NOT preserve a chosen zero-child lift or a fine-grid distance across a chart switch.

### At most nine candidates for a single canonical readout

Use the unchanged parent Gauss reducer. For a reduced basis u,v, write A=Q(u)<=B=Q(v), <u,v>=-h with 0<=h<=A/2. The two Voronoi slab inequalities imply that coordinates s,t in this basis satisfy

|s|<=B(A+h)/(2(AB-h^2))<=1,
|t|<=A(B+h)/(2(AB-h^2))<=1.

For example the first inequality follows from B(A-h)-2h^2 >= A(A-h)-2h^2=(A-2h)(A+h)>=0. Thus after flooring the exact rational coordinates of the transported vector, only the nine coefficient offsets in {-1,0,1}^2 can contain a canonical representative. The parent membership/tie predicate selects exactly one. The prototype additionally checks the rational vertex-coordinate bounds on all 256 physical bases encountered and compares every tested readout with complete-section residue lookup.

The nine candidates are ADDITIONAL representation-readout work, not a replacement for the old five/eleven/etc. child counts or a bound on bit complexity. This is a bounded int64 research prototype; the mathematical CRT/nearest-point argument is not a claim of arbitrary-size software validation.

## 6. The measurable price: rounder display can destroy neighborhood continuity

For the horizontal unit-thin index-55 lattice, chart 1 changes the normalized lines from (0,0) to (1,2). Both complete 55-point sections are lattice-convex and centrally symmetric. The cloud standard-deviation axis ratios are 49.5959329091 before and 1.28296843295 after. These cloud ratios are NOT the best-basis K values.

Preserve each residue label through the exact transport. Of 55 labelled points, 54 change coordinates. The source has 54 undirected unit-distance neighbor pairs. NONE remains a unit-distance pair in the target. Maximum squared displacement is 676; mean squared displacement is 204.36363636. Content identity and invertibility therefore do not imply semantic or geometric neighbor preservation.

An actual prefix witness: at exponents (0,0,0,0,1), index 19, the selector uses chart 0. After an 11 refinement it switches to chart 1. The original base-chart zero-child continuation of (-2,0) is displayed at (-3,8); 14 of the 19 such zero-child continuations move. Their difference (-1,8)=G19(1,1), so the old 19-residue is still correct. In the tested finite family the occupied support sets happen to remain included across these edges; this does NOT imply labelled addresses are stable. We record label movement rather than claiming an unsupported support-inclusion failure.

The consequence is a tradeoff, not a finished Nollm architecture: each chart separately retains the parent's compatible, stable sections; a chosen visible chart can keep bounded roundness, but changing chart re-embeds residue labels. Two views need not mean two copies of payload, yet transport and chart metadata are real costs.

## 7. Executed checks

- Complete minimum-basis searches for all 91 normalized lattices.
- All 72 two-chart offsets and 2485 three-chart pairs compared on 288 states.
- Directed reachability from all 72 starts using 7/19 only; maximum shortest thin-hit distance 8.
- 4896 exact phase-transport/refinement commutation checks.
- 182 paired atlas sections at scalar 1 and 5; 107198 full residue round trips; lattice-basis transport inclusions checked in both directions.
- All selected atlas sections have zero hull lattice holes and central symmetry. Maximum numerical cloud axis ratio in THESE TWO SAMPLED SCALES is 2.55415728852; no asymptotic cloud bound is inferred from that statistic.
- 53 complete actual exponent states; 107 refinement edges with 21755 parents.
- 60 full factor-order runs, including three- and four-factor cases from several starts; both endpoint sets and per-parent descendant fibers match.
- The 55-point neighborhood destruction and index-19 labelled-lift movement witnesses are reproduced.
- The packaged scripts were freshly rerun; control_results.json matched the development run byte-for-byte. Do not count replays as additional independent checks.

## 8. BRC resolution and next research boundary

REUSE_EXECUTED: unchanged hash-pinned two-inert predecessor and its exact quotient, Gauss/Voronoi, membership, hull and child-fiber functions. EXTEND_EXISTING_TOOL: task-local exact basis minimizer, phase-translate observer and local CRT transport, not a new global toolbox family. COMPOSE_APPLIED: finite phase state, full quotient identity, chart marker and branch provenance are retained. Cost/covariance are readouts; minimized anisotropy cannot replace the residue or establish neighborhood preservation.

Closed in this unit: initial-direction-only avoidance fails for the frozen generators; two compatible residue representations provide an explicit all-depth basis/continuous-cell roundness bound; exact transport is executable; the loss of fixed geometric labels/neighbors is quantified.

Not closed: simultaneous roundness AND useful semantic-neighborhood continuity; other inert-prime families; original scalar-label multiplication as intrinsic planar geometry; arbitrary-prefix uniformity; actual physical fanout/runtime integration. A next meaningful test should constrain transport displacement or neighborhood distortion, instead of treating a round display as proof of a good memory field.

Classical background: finite-field group actions, lattice CRT and nearest-vector/Gauss reduction are established mathematics. Compare Li-Gan-Ling, Coprime Sensing via Chinese Remaindering over Quadratic Fields, arXiv:1808.07505 and 1808.07511. No priority claim for these ingredients; this note records the explicit phase-control tradeoff and finite certificates for the declared model.
