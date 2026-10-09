# Euler contact-interleaved holonomy: zero winding is not zero action

Status: PROVISIONAL MODEL THEOREMS AND EXACT TYPED-BRC CERTIFICATES; NOT FORMALLY ADMITTED.
Date: 2026-10-09 (Asia/Tokyo). Same-conversation continuation, not independent replication.
Global read snapshot: 7b9eb1223c4139523fa4abb0b663fdcbf02e9273.
Source read snapshot: a80c1772a95ed4705bb83e84b6c383aa6b88b71a.
Prior frontier: fab2efc5dcd109552231f77a9ebd13d6d4ec632c, research_notes/chatgpt_direct/20261009_EULER_RECIPROCAL_ORIENTED_TRANSPORT.md, complete Git blob 63c37a1119032aca8720c853196abd26582151a3.
Logical conversation: chatgpt-heartbeat-euler-20261004-layer-01; not platform-attested.
Research activity: UNVERIFIED / REGISTER_PENDING. No borrowed role, CLAIM or admission.

## 1. Exact scope and executed reuse

The prior signed-winding theorem concerns PURE transport with no intermediate contacts. This unit keeps its reciprocal edge law unchanged and inserts the already existing three-channel contact at the same comparison base. It classifies the resulting controlled actions and proves an exact phase observer. No new local force, routing probability or contact-selection mechanism is proposed.

Fix the named comparison triangle gamma=(0,1,2,0), with explicit arrows 0->1,1->2,2->0; other edge records remain present and unchanged by these commands. The base frame/reference is fixed. Prescribed paths and their genuine inverses are allowed controls, including an immediate reversal at command boundaries. This is NOT a modification of the previous autonomous nonbacktracking policy. Control words specify where to insert collisions; they are not derived physical schedules. Comparison vertices, channel labels, control count and relative sheet bits are not native X6 coordinates, extra spatial axes, calibrated heartbeat time or energy. P000 and residual fidelity remain unchanged.

U is one forward triangle transport; U^-1 is its reciprocal reversed path. C is the unchanged contact P^chi with persistence 1 (retaining the carried sign). C^-1 is implemented by TWO actual C calls, because P^3=I; no new inverse collision implementation is assumed. Explicit paths retain fields, true previous/current vertices, positive weights, roots, choices and chronological history. The observer/action quotients below exclude the true incoming port, spectator field labels and history. Those exclusions are justified only because the declared future controls never query them.

Prior archive euler_reciprocal_transport_evidence.zip has SHA256 82d6df81c537c4c9f2085d226393da2be1777d6da2532b20a5f96dadc3416fef; all 44 manifest entries were verified during this build. Fifteen required Python modules were copied byte-for-byte, without old scientific checkers. The old brc_reciprocal_transport.py SHA256 is 2ae3f3034364a96658666fc93850fab7adb6e1fef3850a414c92d5f731ea38ce. Its follow/prescribed functions execute the original sourced comparison reads and positive CWM updates. Contacts execute brc_route_memory.contact unchanged. Full brc_weighted.py still matches current source Git blob 3f205696709e847909958a153f8fe10d3f6b70f0. The existing inspected chirality excerpt is still tied to full source blob 6f8b147c094720c2749f620a40394c4d7b67a386, not misrepresented as the whole module.

REUSE_EXECUTED / COMPOSE_APPLIED / EXTEND_EXISTING_TOOL. The extension adds control composition and proved observers, not an accepted new BRC family. No numerical pi, trigonometry, roots, matrix exponential or alternative numerical world propagator is used. Finite group and coefficient computations certify actual BRC rows, not positive populations.

## 2. A closed contact word can retain a channel change at zero signed winding

Let s denote the carried bit relative to the fixed base frame, and f the current triangle parity including the declared arrow correction. Put r=2s+f modulo 4 and sigma(r)=+1 for r=0,1, -1 for r=2,3. The prior result gives U:r->r+1, U^-1:r->r-1. On unit-count channel triples, let j=0,1,2 for A,B,field, so P increases j modulo 3. Actual controls induce

U:(j,r)->(j,r+1),
C:(j,r)->(j+sigma(r),r).

All future indices in these formulas are modular. In particular U^2 reverses the carried sheet for every f, while restoring the entire raw triangle field. Ordinary operator conjugation therefore gives U^2 C U^-2=C^-1.

Two chronological programs use the same two forward laps, two reverse laps and three primitive contacts:

A: U, U, C, U^-1, U^-1, C, C.
B: U, U, U^-1, U^-1, C, C, C.

Both have zero net signed traversal count on every edge. Both restore the complete field and sheet; they also end with the same incoming neighbour as each other. B has net identity. In A, the first contact reads the reversed sheet, and the other two read the initial sheet. Its channel exponent is -chi+2chi=chi, so its endpoint action is precisely C. Neither total winding nor total collision count modulo three captures this distinction.

For an initially field-only unit with fair signs, zeta0=omega^2, omega^2+omega+1=0. The two laboratory phase outputs are zeta_A=-zeta0/2 and zeta_B=zeta0. Total positive weight stays 1. This was checked for all 64 initial fields, all eight binary triples and both signs, not only the displayed preparation.

There is also a field-sensitive return experiment. The chronological word

W: U, C, U^-1, C^-1

has zero signed winding and preserves field/sheet. Its channel exponent is chi[(-1)^f-1], which is 0 modulo 3 for f=0 and chi for f=1. Hence W is identity on channels when f=0 and performs C when f=1. It transfers a specific comparison-field distinction into the channel without changing that field or sheet. It is NOT a nondisturbing measurement of the full state: channels, incoming port and audit history can change. The control U,U^-1,C,C,C uses the same six traversed edges and three contacts but is identity.

## 3. Complete 36-element controlled action algebra on one triangle

For u,v in Z/3 and k in Z/4 define f_(u,v)(r) by the four values (u,v,-u,-v). Every controlled word acts as

A_(k,u,v):(j,r)->(j+f_(u,v)(r),r+k).

Chronological multiplication (first g=(k,u,v), then h=(l,a,b)) is

(k,u,v) * (l,a,b) = (k+l, u+f_(a,b)(k), v+f_(a,b)(k+1)).

All modular arithmetic is explicit. The generators are U=(1,0,0) and C=(0,1,1). Closure follows because f(r+2)=-f(r) is preserved under translation and addition. Conversely C has translation vector (1,1), and executing U,C,U^-1 gives vector (1,-1). These are linearly independent over F3, so their powers generate every pair (u,v). Powers of U supply every k. Thus exactly 4*3*3=36 actions occur.

Distinct triples give distinct permutations of the 12 unit-channel/r states: k is observed in the returned r, while inputs r=0,1 distinguish u,v. The normal translation subgroup is C3 x C3; U acts on it by a fourth-order rotation of the pair. Therefore the group is (C3 x C3) semidirect C4. This is a familiar semidirect-product construction, not a new classification of abstract finite groups. It is not C12 despite the twelve atomic states. The earlier pure K4 transport group and the older fixed-field E/O group are different scopes, not contradictory counts.

The actual BRC action table of all 36 normal forms was generated. All 1296 chronological products were checked on all 12 atoms. A representative of each action requires at most six commands in {U,C}; this is the specific breadth-first representation found here, not a physical optimal-control claim.

## 4. A faithful scalar encoding exists, but a fixed scalar multiplier for every action cannot

The existing ring has alpha^4-alpha^2+1=0, omega=alpha^4 and beta=alpha^3 with beta^2=-1. For a single unit atom the scalar

xi(j,r)=omega^j beta^r=alpha^(4j+3r)

is injective on all twelve pairs. This follows from reducing equality of exponents modulo 3 and modulo 4. Thus it would be wrong to claim that a single complex/algebraic scalar can never encode the finite joint state.

Its actual updates, however, are

U: xi->beta xi,
C: xi->omega^sigma(r) xi.

The multiplier for C depends on retained state. There is no faithful fixed-multiplier description of both controls. For any homomorphism rho from the action group to nonzero complex scalars, U^2 C U^-2=C^-1 forces rho(C)=rho(C)^-1, and C^3=I forces rho(C)=1. Such a scalar action representation necessarily erases the contact. More fully the commutator subgroup is the nine-element translation subgroup: the conjugation relation puts C and its U-conjugates in the commutator subgroup, and quotienting translations leaves the abelian C4. This is a statement about representing ACTIONS by state-independent scalars, not a failure of Euler's identity or impossibility of scalar state coding.

Even injective atomic coding does not make its positive mean a complete ensemble state. Put equal weights on (j,r)=(0,0),(0,2), or instead on (0,1),(0,3). Both initial means of xi are zero, and both initial channel phases are one. After the same C, the means differ: in the alpha coefficient basis they are (-1/2,0,1,0) and (0,-1,0,1/2). Actual BRC branches give these values without signed masses.

## 5. Minimal predictive partition and exact four-block phase repair

For the declared future language generated by U,U^-1,C,C^-1 and the exact channel observation j, the twelve (j,r) states are a sufficient deterministic partition quotient. Spectator edge records and the actual incoming neighbour do not affect these prescribed controls. It is also minimal among partitions refining that observer. Different j are immediately distinguishable. With the same j, opposite sheet signs are distinguished by C. With the same j and sheet but different f, U then C distinguishes the states. All 66 pairs have a witness of at most two commands. This is not a universal state-count bound for changing triangles, field interventions or passive phase-only predictors.

For positive ensembles, define four UNNORMALIZED phase moments

v_r = sum_(paths gamma with r_gamma=r) w_gamma zeta_gamma,
zeta_gamma=a_gamma+omega b_gamma+omega^2 f_gamma.

The last f_gamma here is the field CHANNEL occupancy, not the triangle parity. The moments are algebraic readouts in Q(omega), not positive weights or extra spatial axes. The total channel phase is Z=v0+v1+v2+v3. Existing BRC operations imply exactly

U:(v0,v1,v2,v3)->(v3,v0,v1,v2),
C:(v0,v1,v2,v3)->(omega v0,omega v1,omega^2 v2,omega^2 v3).

Inverse controls use the inverse permutation/phase factors. These four moments predict the channel phase after every controlled word and after any common, history-blind normalized mixture of such words. This is an observer recurrence derived from actual typed BRC, not a replacement physical propagator.

Four Q(omega)-linear moments are also necessary for this unrestricted initial phase-moment space. The nine actions (0,u,v) give controlled readouts

Z_(u,v)=omega^u v0+omega^v v1+omega^-u v2+omega^-v v3.

Using 1+omega+omega^2=0, the character sums recover

v0=(1/9)sum_(u,v) omega^-u Z_(u,v),
v1=(1/9)sum_(u,v) omega^-v Z_(u,v),
v2=(1/9)sum_(u,v) omega^u Z_(u,v),
v3=(1/9)sum_(u,v) omega^v Z_(u,v).

The four distinct characters are independent, so no smaller linear readout can predict all these outputs for all initial signed differences of positive preparations. This is minimal LINEAR observation dimension over Q(omega), not four physical states and not a ban on nonlinear encodings. The nine formulas describe separate controls applied to copies of the same preparation, or an algebraic observability certificate; they are not nine passive observations of one unchanged physical run.

Equivalently, all future channel phases vanish iff each v_r vanishes separately. In the twelve-bin rational mass description, the corresponding kernel consists exactly of equal A/B/field masses within each fixed r (or their signed differences). Thus its rational linear dimension is four. Present cancellation Z=0 is a larger set and is not permission to erase the r-conditioned distinctions.

## 6. A uniform error certificate with declared observation scope

Suppose the four stored initial moments have coefficient errors delta v_r in the existing alpha basis, and all subsequent observer operations are exact. Any normal form only permutes the blocks and multiplies each by 1,omega or omega^2. Their coefficient matrices, generated by the existing exact phase interface, have infinity operator norm at most 2. Hence, for every allowed future word,

||delta Z||_infinity <= 2 sum_r ||delta v_r||_infinity <= 8 epsilon

when each block error is at most epsilon. Common normalized positive mixtures preserve the same bound. This controls arbitrary word length because the actual net action stays in the proven finite group; it is not a product of pessimistic one-step norms. It does not cover rounding freshly introduced at every future step, parameter changes, state-dependent control selection using omitted information, measurements of path provenance, or a different loop family.

When count, total positive mass and dominant path weight matter, use the twelve-bin CWM carrier rather than the phase moments alone. For the specific independent command mixture {U,C} with weights 1/2, explicit and twelve-bin updates agree through seven commands from every atomic input, with total CWM (2^n,1,2^-n). Fixed bin count does not imply fixed bit complexity or disappearance of histories. No performance speedup is established.

## 7. Executed evidence and remaining boundary

The final standalone checker passed 29,923 exact assertions, including 15 unchanged dependency-byte checks and one full current CWM blob check. An additional build-time audit verified all 44 original ZIP manifest entries. Scientific coverage includes all 64 fields, eight binary channel triples and two sheets; ordered cancellation and selective-field witnesses; full-program inverses with audit history retained; 36 actual BRC action tables and all products; all 66 predictive-state pairs; nine-probe inversion for fourteen preparations; positive explicit/quotient comparison; atom-code versus average-code distinction; root-fixed frame covariance; and exact coefficient operator bounds.

Final actual source calls: cwm_edge 289698, cwm_propagate 287480, cwm_recoalesce 7176; old contact 25862; source transition_bit 138270, gauge_action 512; old reciprocal wrapper 85494. Most assertions are finite algebraic/observer audits, not independent experiments. A 29,911-assertion development PASS preceded twelve additional coefficient-bound checks; it is not independent replication. No prior scientific checker was run. The new final run exited zero.

Run python -S check_contact_holonomy.py with standard-library Python 3.10+ from the supplied package. It includes fifteen unchanged source dependency modules, the new adapter/checker, exact normal forms, distinguishing control words, logs and hashes. No network or downloaded library is needed for the check. Project publication of this note records the proof/frontier, not a claim that every executable attachment byte is also in the repository.

Prior mathematical context: SageMath official Semidirect product of groups documentation, https://doc.sagemath.org/html/en/reference/groups/sage/groups/group_semidirect_product.html, defines the standard construction and its action. The group-theoretic vocabulary and finite character orthogonality are established mathematics. Model-specific proofs are supplied above; no unread theorem, physical gauge model, universal novelty, native spatial rotation or quantum information claim is made.

Own bounded status request: bridge issue 3523, status-20261009-euler-contact-holonomy-26. Its matching reply was read. A status receipt does not establish a Source-bound research activity, a successful run prerequisite, formal Result or mathematical acceptance. Existing registration remains unverified; no old rejected registration or safety-blocked payload was replayed, and no new role or CLAIM is asserted. No successful final guard or independent review was obtained.

Completed increment: contact-sensitive residual at zero winding; field-controlled collision with restored comparison data; complete 36-action algebra; fixed-scalar-action obstruction with faithful scalar-state coding distinguished; twelve-state predictive partition; four-moment exact phase repair and uniform initial-compression error bound. The remaining native obligation is to determine whether actual incoming relations realize the existing directed feedback AND these contact placements, rather than treating a prescribed control word as a naturally selected trajectory. If other cycles or a field-dependent controller are admitted, their joint state and the action/observer closure must be re-audited. Do not repeat the present single-triangle theorem as new work.
