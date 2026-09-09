# X6 triadic-incidence families: conditional amplification, minimal connectivity, and dynamical confinement

Event: `NS-NATIVE-INCIDENCE-FAMILY-20260909-D5C00D-12`  
Researcher: `EM-DIRECT-D5C00D / TASK_RESEARCH`  
Activity: `RA-D5C00DF7D77F4AA2ACE0`  
Status: **TESTING: ordinary finite/algebraic proofs and executed exact checks, not a primitive force realization.**

## 1. Question and source scope

The unresolved question from event 11 is how admissible ternary relations can constrain the density-port candidate, rather than being attached after its desired amplification has been observed. This note does not invent a force reservoir. It treats the permitted ternary incidence as an explicit parameter, proves results uniformly in that parameter, and identifies a concrete danger in using a carrier atlas as if it were a physical relation.

Native source snapshot: `awdawmip/enterprise-math@cf224163a9fe5ea4f3ac6d8dd5e13f1b771daf44`. Relevant exact sources:

- `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`: signed Z6 Cell torsor, full coordinates, path/observer separation;
- `definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md`: four STAR triples, carrier/readout status, S6 versus atlas-preserving S4;
- `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`: primitive force arity and independently typed closure;
- `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`;
- event 10 at `6f119ea99021f83141321a5241dcb33b70f5af44`, and the locally executed event-11 package.

The new executable imports the unchanged event-10 and event-09 programs and verifies their SHA256 values. It uses their complete collision calculation, count checks, signed-coordinate operations and primitive streaming. A veto wrapper is added; no old score, tie or collision rule is silently rewritten. This is a research specialization, not a new general toolbox or admitted Foundation definition. The existing BRC fiber-constancy and same-trajectory distinctions are applied below.

Axis labels in the mathematics are 1-based; Python indices are 0-based. No classical carrier rank is used to redefine the six-dimensional native space. A native triadic force relation is not identified with an additive zero vector or a carrier triangle.

## 2. Freeze a family, not a fitted new force law

Let Gamma be any set of distinct unordered three-element subsets of {1,...,6}. It is fixed in space and time for this diagnostic family. It records candidate permitted axis incidences, NOT a certified TRIADIC_CLOSURE_E relation.

Keep the event-10 rule exactly: a Cell containing C_l(j,sigma)={sigma E_j,+E_l,-E_l}, j!=l, reads the four old-state scores A_m=N(z+E_m)+N(z-E_m), m outside {j,l}. A unique score maximum proposes m. A tie proposes no change. The new rule accepts the proposed event if and only if {j,l,m} belongs to Gamma. Otherwise it does nothing. Stream each channel one primitive signed-axis step afterward. Denote this complete map F_Gamma.

**Veto is not reselection.** Maximizing over only the incidence-permitted axes would be a different rule. For example, one permitted axis would then win even in a homogeneous environment where all original scores are tied. That would destroy the stationary background used below. No such change is made here.

The full parameterized state is (Gamma,n), with update (Gamma,F_Gamma(n)). Positivity, finite-particle count, global additive channel first moment, radius-two dependence, and the initial per-channel upper bound follow from the unchanged parent collision/streaming proof: every accepted event is a parent event, and every veto is identity.

Translations commute with F_Gamma. For an axis permutation p, the exact covariance is

    F_{p Gamma}(p n) = p F_Gamma(n).                         (2.1)

It is generally NOT F_Gamma(p n)=p F_Gamma(n) with Gamma frozen. A material relation and a mere change of observational chart are distinct semantics.

## 3. Uniform amplification theorem for all Gamma

Fix distinct j,l and let

    M_Gamma(j,l) = {m : {j,l,m} in Gamma},   d=|M_Gamma(j,l)|.

Use the homogeneous count background b=C_l(j,+). Move one +E_j packet from E_j to the chosen Cell anchor 0, giving initial deviation of L1 norm 2 and zero relative count/moment. Write D_t=||F_Gamma^t(n)-b||_1.

**Theorem.** For every Gamma and every integer t>=0,

    D_t = 2 + sum_{a=1}^t ||w_a||_1 >= 8 d t + 2,          (3.1)

with all channel occupations at most two. Here w_a is the age-a transverse wake generated once by the travelling excess packet. If d=0, exactly D_t=2 for all t.

**Proof, first generation.** At each of the 2d Cells +/-E_m with m in M_Gamma(j,l), the unique maximum is in direction m and the event passes the veto. Every other proposed transverse event is vetoed. Each accepted pair-axis replacement contributes four channel difference units after streaming. The surplus/depletion contribute two, hence D_1=8d+2.

**Layer separation.** In a normal layer perpendicular to E_j, every Cell has exactly one +E_j packet and no -E_j packet. Any eligible three-packet configuration in that layer must have spectator j; its cancelling pair and every score it reads are transverse. The filter does not change this property. The travelling extra packet has two +E_j packets at its Cell and is ineligible. The hole is one layer ahead, visits a pristine layer, and neither its two-packet center nor its tied-maximum neighborhood creates a transverse change. The extra packet therefore enters a fresh layer at each tick. After it leaves, all transverse evolution stays in that layer. This gives independent, translated wake copies.

**Protected frontier.** For each m in M_Gamma(j,l) and epsilon,sigma in {+1,-1}, the first wake has a missing sigma E_l packet at epsilon E_m+sigma E_l. At age a, these 4d distinct missing slots are at

    (epsilon E_m+sigma a E_l, sigma E_l).                 (3.2)

Induct on a. The wake is supported in |z_l|<=a. Outside the old slab, local state is b and its candidate score axes exclude l, so every score still ties. At an upper boundary hole the local population is two and cannot collide. A non-hole boundary Cell is b; it can retain or remove its l-pair, not add an above-baseline +E_l packet there. Streaming advances upper holes once in +E_l; no other altered channel can reach the new upper boundary. The lower boundary is identical. Vetoing events creates no exception to this proof.

Relative transverse count is zero, so 4d surviving negative units require at least 4d positive units. Thus ||w_a||_1>=8d. Wakes occupy different j-layers and the two longitudinal defects occupy separate layers, proving (3.1). If d=0 there is no first wake; the same travelling two-slot pattern repeats, proving equality D_t=2. QED.

For any prescribed finite T, truncate the background to the cube [-R,R]^6 with R=3T+3, and evolve both finite systems with their free boundaries under the same F_Gamma. Radius-two dependence protects the 4dT transverse missing witnesses and the one longitudinal hole until T. The finite populations are equal, so

    ||F_Gamma^T(n^(T))-F_Gamma^T(b^(T))||_1 >= 8 d T + 2. (3.3)

The initial distance is two. This is forall T exists finite initial pair, not one fixed finite population with unbounded all-time L1 difference. No velocity blowup, viscosity, energy growth or primitive force claim follows.

## 4. What the current four-STAR atlas does and does not permit

The source carrier atlas is

    A={136,145,235,246},

where 136 abbreviates the unordered set {1,3,6}. Treating this as Gamma is a diagnostic constitutive restriction, NOT an identification of the carrier with native physical incidence.

For the original event-10 background C_2(1,+), M_A(1,2) is empty. Hence its exact amplification disappears: D_t=2 for all t. The original lower bound 32t+2 cannot be copied into this different rule.

For C_3(1,+), M_A(1,3)={6}; therefore D_t>=8t+2. The first five exact distances are 10,34,66,110,162.

**Chart-versus-material obstruction.** There is an S6 relabelled atlas B={123,146,256,345}. Keeping the native initial count field C_2(1,+) and seed fixed, F_A produces first distance 2 while F_B produces first distance 10. Thus changing only a proposed observer atlas changes count dynamics if that atlas is used as this gate. This is not acceptable as a pure observer change. Either Gamma must be independently justified as material/state information, or the physical law must be independent of the arbitrary observer convention. Equation (2.1), which transforms state and relation together, does not cure this distinct issue.

No claim is made that the sixteen non-STAR coordinate selections are physically prohibited. Their native force realization remains open in the source definitions.

## 5. Link graphs expose static channel confinement

For a fixed spectator j, define the link graph L_j(Gamma) on the five remaining axes, with edge l--m exactly when {j,l,m} belongs to Gamma. A collision retaining spectator j moves the pair along one edge of this graph.

Thus for normal layers initially using pair axes in a single component Q of L_j, all subsequent pair axes remain in Q. For the homogeneous single-move seed above, deviations in both position and channel are confined to the coordinate subspace on {j} union Q, where Q contains the original l.

To justify spatial confinement, suppose deviations are already within that subspace. Inside it, every accepted new pair axis belongs to Q. A Cell outside it is background; if its scores see a deviation at all, it is one step away along an outside axis q. A unique elevated q maximum would propose {j,l,q}, forbidden because q is outside l's component; a depressed q score leaves the other maxima tied. Streaming inside the allowed axes preserves the subspace. Longitudinal markers obey the layer argument in Section 3. This proves confinement by induction.

Every link of the four-STAR A is 2K2 plus an isolated vertex. Consequently these seeds either do not amplify at all, or their disturbance remains in a genuine three-axis native slice. Merely labeling the ambient field Z6 does not make this perturbation fully six-axis coupled.

## 6. Sharp static threshold: eight triples

Ask the purely combinatorial interface question: how few three-axis incidences can make every L_j connected on all five remaining axes? This is a possible-route requirement, not yet a same-trajectory result.

Each such link needs at least four edges. Each triple contributes one edge to each of its three vertex links. Therefore

    3|Gamma| = sum_j |E(L_j)| >= 6*4,
    |Gamma| >= 8.                                        (6.1)

The bound is attained by G8=A union B, with A,B as above. The j=1 link is the path 2--3--6--4--5; every other link is likewise connected. B is an S6 relabeling of A. This is a combinatorial union of incidence templates, not a claim that both are simultaneously the four geometric triangles of one unchanged FCC carrier.

An exact enumeration checks all binomial(20,8)=125970 possible sets. The equality case forces each vertex into exactly four triples; 780 sets satisfy that necessary condition, and exactly 120 have all links connected. These 120 are exactly the connected unions of two distinct four-STAR atlases. The S6 orbit of A has 30 elements; for each A there are eight suitable second atlases. These classification counts are finite exact-check results, not historical novelty claims.

**Additional ordinary proof: every minimal eight-triple system has pair degree at most two.** Equality in (6.1) gives degree four at each vertex. Suppose pair12 occurs four times. The four triples 12m exhaust vertices1,2; the remaining four must be all triples on {3,4,5,6}. Each other link has an isolated edge12 and a triangle, contradicting connectedness.

If pair12 occurs exactly three times, relabel these triples as 123,124,125. To attach vertex6 in links1,2, their remaining triples must be 1a6,2b6 with a,b in {3,4,5}. The remaining three triples lie on {3,4,5,6}. Each vertex belongs to two or three of those triples. Degree four forces a!=b; writing c for the third of {3,4,5}, the remaining triples must be abc,ac6,bc6. The link of c again has edge12 disconnected from triangle a-b-6. Contradiction. Larger pair degree is excluded by degree four. Hence all pair degrees are at most two. Connected five-vertex four-edge links therefore are paths. QED.

## 7. A stronger dynamical obstruction: two unseen axes keep tying

Static connectivity does not guarantee that the fixed score rule will traverse a link path.

Let M=M_Gamma(j,l) and H={j,l} union M. If d=|M|<=2, then for the homogeneous single-move seed,

    every position/channel deviation stays within span{E_i:i in H}           (7.1)

for every integer time. This is stronger than Section 5 when the link graph is connected.

**Proof.** There are at least two axes q outside H. In a normal layer, at a Cell inside H's coordinate subspace, its +/-q neighbors remain homogeneous for every outside q. Each such score equals six. The current eligible pair axis is inside H, so at least two outside scores compete equally; no outside q is the unique maximum. At an outside Cell, the only potentially changed score samples a deviation along an outside axis q, while the local pair is the original l. If that score is elevated, the proposed event is vetoed, since q is not in M_Gamma(j,l). If it is depressed, the other three candidate maxima tie. Thus no new deviation is created outside H and no inside collision introduces an outside channel. Primitive streaming closes the induction. The two longitudinal markers are covered by Section 3. QED.

Combine Sections 6 and 7: **every minimum eight-triple all-link-connected incidence set still confines each of these seeds to at most four coordinate axes.** This is an all-time theorem, not an observation limited to five ticks.

The example G8 with (j,l)=(1,2) stays on axes {1,2,3}; with (j,l)=(1,6) it stays on {1,3,4,6}. Exact five-tick distances in the latter case are 18,98,322,754,1474. Therefore a growing L1 norm and a connected incidence diagram can coexist with permanent missing-axis confinement.

This result does not rule out full six-axis coupling from richer initial states, dynamic Gamma, a changing spectator, different legal constitutive rules, or larger incidence sets. A separate exploratory nine-triple probe hit the 45-second execution limit; no universal conclusion about nine triples is made.

## 8. Executed checks and scope

The new program imports unchanged parent collision/streaming helpers and checks their exact SHA256 values. It executes all 125970 eight-subset candidates with sound degree pruning; 4560 rooted-pair first-step cases over the 30 atlases, 120 minimal connected sets, empty set and complete set; 720 full S6 covariance cases with Gamma transported; two translations; five five-tick trajectories and independent wake decomposition/frontier predicates.

A first wrapper draft misused the parent's signed unit() helper to construct a nonunit translation. The parent's input guard rejected it. Only the wrapper was corrected to use a six-integer displacement tuple; parent code and all mathematical rules were unchanged.

No fixed-time numerical pattern was extrapolated to an asymptotic exponent. The all-time claims are Sections 3,5,7. No primitive-force admissibility, physical force law, viscosity model, natural-law uniqueness, continuum NS solution, Lean build or independent review is claimed. No P000, README, Foundation or another researcher's task was changed.

**Next smallest unresolved physical unit:** give an independently specified native ternary incidence/exchange mechanism, including its state and evolution, and determine whether it belongs to this filtered family. Neither the presence of three labels nor a carrier atlas nor static connectivity supplies that certificate. The current result makes the consequences of one proposed interface calculable without pretending the missing mechanism is already known.
