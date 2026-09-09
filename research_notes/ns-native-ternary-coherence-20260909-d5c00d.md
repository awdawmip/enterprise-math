# Native X6 coherence: ternary channel classification, necessary port information, and six-step spatial lifts

Progress-Event-ID: NS-NATIVE-TERNARY-COHERENCE-20260909-D5C00D-09
Researcher-ID: EM-DIRECT-D5C00D
Research-Activity-ID: RA-D5C00DF7D77F4AA2ACE0
Session: local-chat-ns-openai-audit-d5c00df7d77f4aa2ace0 (existing local key, not an authenticated platform identifier).
Status: ORDINARY_FINITE_ALGEBRA_PROOFS / EXECUTED_EXACT_CHECKS / NOT_INDEPENDENTLY_REVIEWED.
No Foundation promotion, P000 modification, native fluid law, instability theorem, or classical NS solution is asserted.

## 1. Question and source boundary

The user requires the dynamics to be self-consistent with discreteness and Enterprise coordinates. The previous checkpoint identified a missing native interaction/observer bridge; it did not establish that a quantized classical Fourier recurrence is native dynamics.

We now classify a tempting *test implementation* before choosing any growth experiment. The goal is to determine what it can express, what information it necessarily loses, and how a primitive-step spatial realization can retain the missing relation. This is not a claim to have selected nature's collision law.

Frozen project source: `awdawmip/enterprise-math@e16c5a875d4098f260f3d17283368b20b02c774c`.
Frozen global-entry source: `awdawmip/chatgpt-global-knowledge@530c67e561b34c3dad75ede2879895dcf876b963`.

Exact project authorities used:
- `definitions/00_CURRENT_NATIVE_FOUNDATION.md`;
- `p000_reality_foundation.json`;
- `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`;
- `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`;
- `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`;
- parent `research_notes/ns-native-coordinate-coherence-20260909-d5c00d.md`.

The triadic definition explicitly leaves the admissible Cell/direction incidences for `TRIADIC_CLOSURE_E` to further construction. The consumed sources do not supply a fully specified native fluid collision table. Two scoped code searches returned no results; that is not proof that no relevant law exists anywhere in the repository. The findings below do not depend on such a global absence claim.

We use the chosen project framework: spatial Cell centers form an affine torsor over Z^6, primitive moves are +/-e_i, and native component length squared is the sum of squares. Native 120-degree orthogonality is not converted into Euclidean cosine entries. Primitive force quanta, channel labels, spatial displacements, and conserved observables retain different types.

## 2. A parity obstruction to an invalid identification

Define the parity observer of an integer displacement z by chi(z)=sum_i z_i modulo 2. Every primitive step +/-e_i flips chi. Therefore a closed primitive-step path has even length. In particular,

    v_1+v_2+v_3 != 0,  for v_a in {+/-e_1,...,+/-e_6}.

This is a finite algebra theorem about the declared coordinate graph. It does NOT refute P000's ternary force balance. It refutes identifying that force relation with the sum of three equal unit coordinate moves. P000 itself forbids silently replacing its native relational closure by a classical vector-sum condition.

Thus three participating force terms need not mean three spatial edges or three unit particle velocities. Any bridge making those identifications bears a separate proof obligation.

## 3. Complete classification of bare ternary unit-channel states

### 3.1 Additional test-model assumptions

A local state is an *unlabeled multiset of exactly three packets*. Its channel alphabet is the twelve signed coordinate directions; no rest channel, variable speed, internal charge, ordered port, history, or surrounding field is included. Multiple occupancy is permitted.

Write nonnegative integer channel counts n_i^+,n_i^-. Impose conservation of packet count and the separately declared additive first moment

    m=sum_i(n_i^+ + n_i^-)=3,
    P_i=n_i^+ - n_i^-.

P is an algebraic channel observable. It is not identified with physical momentum or primitive force balance without a bridge. The quantity sum_i(n_i^+ + n_i^-)*L_E(e_i)^2 equals 3 automatically, so this toy alphabet cannot introduce an independent kinetic-energy constraint.

### 3.2 Fiber classification theorem

Set t_i=min(n_i^+,n_i^-). Direct integer arithmetic gives

    n_i^+=max(P_i,0)+t_i,
    n_i^-=max(-P_i,0)+t_i,
    3=||P||_1+2 sum_i t_i.                              (1)

Since ||P||_1 is odd and nonnegative, exactly two cases occur.

**Case A: ||P||_1=3.** Every t_i is zero. P uniquely determines the entire channel-count state. A count- and P-preserving collision cannot change it. Permuting packet identities would require a richer labeled state and is not a change of this observer.

**Case B: ||P||_1=1.** There are unique j and sign sigma such that P=sigma e_j, and sum_i t_i=1. There are precisely six states in that fiber:

    C_l(j,sigma)={sigma e_j,+e_l,-e_l}, l=1,...,6.        (2)

Every nonidentity transition is consequently

    C_l(j,sigma) -> C_m(j,sigma).                        (3)

It redistributes a neutral signed pair and retains the spectator first-moment contribution sigma e_j. This is a classification of channel counts, not a proof that the underlying causes would be physically two-body: a richer interaction rate could depend on all three packets. Conversely, the mere presence of three packets does not establish a primitive ternary force event.

There are binomial(14,3)=364 multisets, partitioned into 292 singleton moment fibers and twelve six-state fibers. There is no zero-P state. The checker independently exhausts all 364 configurations and verifies (1)-(3).

## 4. Symmetry determines all deterministic bare collision maps

Suppose a map T on these 364 states conserves P and commutes with every permutation of the six axis labels. This is S6 equivariance with *no hidden anisotropic parameter*. For a law with an orientation parameter, that parameter must be included in the transformed state; the theorem would have different assumptions.

The singleton fibers force identity. Fix P=+e_j. The stabilizer of j is S5 acting on the six possible pair axes l. C_j is its unique fixed point, so T(C_j)=C_j. For l!=j, the stabilizer of both j and l permutes the remaining four axes. Its only fixed pair-axis outputs are j and l. Thus T(C_l) can only be C_j or C_l. Transitivity on the five l!=j makes the choice common to all five.

There are exactly two maps on this fiber:

    identity, or collapse all C_l to C_j.                (4)

The same choice must hold for every positive spectator axis by S6 symmetry. Negative spectators form a separate S6 orbit, with an independent identical choice. Consequently there are exactly FOUR global S6-equivariant deterministic count/P-preserving maps. Only the global identity is bijective. The other three collapse one or both sign sectors.

Reversibility is NOT a project requirement: Enterprise Math explicitly allows collapse. The useful stronger point is that even the irreversible options cannot route a neutral pair to a *third distinct axis* without extra information. We do not prohibit dissipative or history-bearing laws with a different state space.

The checker exhausts all 6^6=46,656 maps on one fiber using generators of S5, then verifies the resulting four global maps under all 720 S6 permutations (1,048,320 exact equivariance equalities).

## 5. A sharp information lower bound and an explicit repaired interface

Fix an input C_l(j,sigma) with l!=j, and require the outgoing pair axis m to be distinct from j and l. The unused axes form a four-element S4 orbit under the stabilizer of the bare input. There is no fixed output axis. A deterministic invariant selector based only on that input therefore does not exist.

More precisely, suppose a nonempty decoration fiber H over the fixed bare input carries this S4 action, and a deterministic equivariant selector q:H->{unused axes} is defined. Its nonempty image is S4-invariant, hence is the whole four-element orbit. Thus

    |H| >= 4.                                          (5)

This is a cardinality requirement, not a claim that four unstructured numbers supply a physical interaction law. It applies exactly to deterministic, symmetry-respecting selection of a third distinct axis. Set-valued alternatives or stochastic kernels have different semantics; a uniform probability is not automatically supplied by the axioms.

The bound is attained by retaining m itself as a relational port label. The 240 decorated states are

    a=(j,sigma,l,m), all j,l,m distinct,
    pi(a)=C_l(j,sigma).

Define the diagnostic interface

    W(j,sigma,l,m)=(j,sigma,m,l).                        (6)

W is an involution; it preserves count, P, and the fixed unit-channel squared-length total; it commutes with S6 when the port label transforms as well. It does not add forcing or discard count. However it remains a neutral-pair routing interface, NOT a completed primitive force law, a viscosity mechanism, or a choice of physical dynamics.

The port cannot be dropped while retaining this deterministic update. For example, (1,+,2,3) and (1,+,2,4) have the same bare observation. Their W-images have pair axes 3 and 4, respectively. Therefore

    pi(s)=pi(t) but pi(W(s))!=pi(W(t)),                  (7)

violating the precise BRC observer-descent condition. All 240 states, involution identities and 172,800 S6 covariance identities were checked exactly.

A bare relational representation may instead retain all four outgoing branches with their distinct labels and integer multiplicity one. That is an equivariant BRC relation, not a secretly chosen deterministic law and not a probability distribution. The physical rule selecting or jointly evolving these relations is still open.

## 6. A native spatial lift: ternary relational incidence need not be a forbidden three-step triangle

Select three distinct axes i,j,k and a Cell anchor c. Use the three actual neighboring Cells

    A=c+e_i, B=c+e_j, C=c+e_k.

The A-to-B displacement e_j-e_i has two ordered shortest primitive realizations:

    (-e_i,+e_j) via c,
    (+e_j,-e_i) via c+e_i+e_j.

Each leg has native displacement squared length 2 but primitive transition count 2. It is a composite path, not a new primitive diagonal direction. Use analogous choices for B-to-C and C-to-A. The concatenation contains SIX primitive steps and closes in full Z^6, not merely in a carrier projection. No native 120-degree force angle is attributed to these composite legs.

There are 2^3=8 path realizations per ordered (i,j,k). A simple example is

    A -> c+e_i+e_j -> B -> c+e_j+e_k
      -> C -> c+e_k+e_i -> A.                           (8)

All edges are signed unit-coordinate moves. Any closed path using each of three distinct axes needs both a positive and a negative occurrence for each axis, hence at least six steps. Thus this lift meets a sharp six-step lower bound under that scope. Four-step loops using two axes remain allowed; no claim of universal minimum six is made.

There are 120 ordered triples and 960 ordered lifts including all eight intermediate-path choices. Of these 480 are simple cycles (the rest revisit an intermediate Cell). Repeated Cells do not invalidate the allowed path, but repeated edge/visit multiplicities remain explicit. For fixed three axes there are 720 minimum-length closed primitive words using all three, beyond this particular grouped-leg family.

Anchor changes translate every vertex and leave primitive increments unchanged. Axis permutations relabel all data. Reversing the cyclic order and reversing the three binary path choices reverses the spatial path. This supplies a concrete geometric representation for the ordered third-axis port in Section 5; it does not assert that a fluid collision must execute that loop. Reversal of a route descriptor is not a claim that physical time runs backward.

### 6.1 Count balance, with no false force interpretation

A chosen oriented walk defines a finite integer edge current J: count each directed edge with its actual traversal multiplicity. Its incidence boundary is

    (partial J)(z)=sum_{y->z}J(y,z)-sum_{z->y}J(z,y).

For a closed walk partial J=0, by cancellation of consecutive endpoints. Scaling by any nonnegative integer retains count balance. With occupations sufficient to supply each outgoing edge count, the simultaneous routing identity

    n'(z)=n(z)+(partial J)(z)                            (9)

is legal and preserves total packet count. Equal occupancy before and after may coexist with nonzero internal traffic. This is a kinematic count-transport certificate, NOT proof of momentum balance, primitive triadic force equilibrium, dissipation, autonomous rule selection, or NS.

This distinction is essential: a source-free count current is not itself the statement f=0 for a force equation. No arbitrary flux-to-force identification is made.

The checker verifies closure, native primitive steps, intermediate vertices, all five generating axis transpositions, three anchors, path reversal, and source-free integer incidence for all 960 lifts.

## 7. What has actually advanced

We no longer have only a request to check self-consistency. We have a complete classification theorem for the smallest tempting additive ternary implementation, an exact obstruction to unlabeled deterministic new-axis scattering, a sharp four-state relational-port requirement, and a six-primitive-step spatial lift that retains the required coordinate/path distinctions.

All proofs are finite integer algebra, finite set/group actions, or incidence telescoping. There is no continuum limit, Taylor flatness, smoothness assumption, numerical differential equation integration, or chosen singular profile. These facts do not establish historical novelty; no such priority claim is made.

The next native-law specification should therefore include, at minimum:

    spatial Cell z in X6
    + integer channel population n
    + admissible triadic incidence relation Gamma
    + oriented port/path data lambda
    + ordered event history when required by future updates.

This is a necessary state/interface proposal, not an admitted ontology extension. A concrete rule must determine which Gamma/lambda configurations are legal and how they update, state whether P above is a genuine conserved readout or must be repaired by an internal exchange variable, prove coordinate covariance, and account for count/charge/energy exchanges before any instability claim. Relations must come from the declared state/history, not be chosen after seeing a desired result.

Without that rule, optimizing a growth experiment is premature. The classical Fourier results remain valid at their original effective-model scope. The native-to-classical NS bridge and physical calibration remain separate obligations.

REUSE_APPLIED: current signed-X6 coordinate/path law; P000 force/displacement type separation; BRC fiber constancy and relational-port preservation.
COMPOSE_APPLIED: integer moment-fiber decomposition + stabilizer symmetry + port lower bound + primitive-path incidence lift.
EXECUTED: included standard-library exact checker and JSON output.
NOT_PERFORMED: native fluid simulation, native force-law selection, instability proof, continuum NS proof, Lean build, independent review, P000/README edits, changes to another researcher's assignment.
