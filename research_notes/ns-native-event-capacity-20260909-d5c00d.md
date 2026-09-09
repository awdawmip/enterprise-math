# X6 joint-event capacity, integral closure, and an autonomous 24-frame router

Event: `NS-NATIVE-EVENT-CAPACITY-20260909-D5C00D-13`  
Researcher: `EM-DIRECT-D5C00D / TASK_RESEARCH`  
Activity: `RA-D5C00DF7D77F4AA2ACE0`  
Status: **TESTING: ordinary finite proofs and executed integer checks; NOT a primitive-force or Navier--Stokes theorem.**

## 0. Frontier and scope

Parent objective: a self-consistent native discrete dynamics, not a growth profile selected first and repaired afterward. This packet addresses simultaneous-event compatibility and endogenous event ordering. It does not modify X6-DENSITY-PORT-1 or infer physical legality from three labels.

Current source snapshot: `awdawmip/enterprise-math@c6afd5639e3dc42699af392bd527aecf8f79fb6f`. Exact inputs are the signed X6 Cell torsor, the four-STAR FCC carrier convention, the P000 direction/triadic-balance contract, and joint-observer preservation. The carrier remains a readout. The following use of its four incidence sets as a resource template is an **additional, explicitly declared test-interface choice**, not a derivation of physical incidence.

The remote activity already contains the recovered MICRO-CLOSURE event11 and a distinct INCIDENCE-FAMILY event12. The separately delivered ATLAS-CLOSURE event12 is a different full event ID and is not overwritten or conflated with it. Its local package supplies the signed closure ledger. No prior enumeration is claimed as newly discovered here.

Reuse: apply the existing T7 stabilizer-fixed-lift theorem (`src/enterprise_math/equivariant_section.py`, blob `0257fb7eaa95b2f88e772636d3ae2068d9ce42c0`) and the BRC scoped-fiber discipline. The T7 program itself is not claimed executed. The new standalone checker specializes integer resource allocation and packet transport; it is not a new admitted toolbox family. A bounded code search found no matches; this is not a comprehensive absence or novelty certificate.

## 1. Complete joint-event rather than marginal specification

Supply the four distinct incidence types

    A=136, B=145, C=235, D=246.

There are six resource classes, associated with the existing axis labels. Resource tokens are individually identifiable when paths matter. Let n_i be the nonnegative integer number available for a **single reservation phase**, and x_S the number of events of type S reserved. Each event reserves one token in each of its three classes; one token may not serve two events in that same phase. This is a stated resource interface, not an axiom equating an axis or particle with a force.

The exact legal aggregate batches are

    X(n)={x in Z_{>=0}^4 : A x <= n},

where the incidence matrix acts as

    A x=(x_A+x_B, x_C+x_D, x_A+x_C,
         x_B+x_D, x_B+x_C, x_A+x_D).                (1)

A full event branch also records which specific tokens instantiate each event and the selected ordered paths. Ax<=n prevents double reservation. Reserved tokens are not destroyed: a reservation state keeps both free and reserved inventories, with their union equal to the original inventory. Returning or rewriting tokens requires an explicitly given completion rule; availability is never replenished by assertion.

If separately specified local rewrites act on disjoint reserved tokens, and their read conditions are invariant under the other rewrites, their order commutes. Disjoint token writes alone are not sufficient when another event can change a read condition. Therefore a valid joint-event record must include read dependencies or an invariant-read certificate as well as the write/reservation set.

## 2. Exact full-utilization criterion

Write n=(a,b,c,d,e,f). There exists x>=0 integral with Ax=n iff

    a+b=c+d=e+f,
    a+c+e is even,
    a+c-e, a+e-c, c+e-a, 2b-c-e+a are all nonnegative.   (2)

When it exists it is unique:

    x=(a+c-e, a+e-c, c+e-a, 2b-c-e+a)/2.               (3)

Proof: the three equations a=x_A+x_B, c=x_A+x_C, e=x_B+x_C give the first three coordinates of (3); b then gives x_D. The two opposite-pair sum equalities give the remaining equations. The four numerators have the same parity. Conversely substitution proves sufficiency. This is an integer inverse, not a limiting approximation.

In particular, for n=(q,q,q,q,q,q), complete utilization is possible exactly when q is even; then every x_S=q/2. The parity of n_1+n_3+n_5 and the two opposite-sum differences are invariant under subtraction of whole event columns. This statement applies to reservation/one-use decomposition, not arbitrary physical evolution with token returns or changed species.

## 3. Fractional allocation can certify a nonexistent integer batch

For q=1, any two different STAR types share one resource. The only legal integer batches are the empty batch and the four singleton events. In particular their maximum event count is one. Nevertheless the fractional vector

    x=(1/2,1/2,1/2,1/2)

satisfies Ax=(1,1,1,1,1,1) and has total event count two. It is outside the convex hull of all legal integer batches, because every such batch satisfies sum x<=1. It cannot even be interpreted as an average of legal same-phase integer batches with those event marginals. A valid probability mixture of the four singletons instead has sum x=1; it is a distribution over alternatives, not simultaneous fractional execution.

For arbitrary q>=0 the exact maxima are

    fractional maximum = 2q,
    integer maximum = 2q              if q even,
                      2q-1            if q odd.         (4)

Sum all six inequalities in (1): 3 sum x<=6q. Equality forces all six inequalities to be equalities and thus x_S=q/2. Even q attains it. If q=2r+1, x=(r+1,r,r,r) and its four type placements attain 4r+1=2q-1.

These are the only odd-q maximizers. If their maximum coordinate were <=r the sum would be <=4r. If the maximum b were >=r+2, each other coordinate is <=2r+1-b, so the sum is <=3(2r+1)-2b<=4r-1. Thus the maximum is r+1 and the other three must be r.

This is a limitation of a fractional relaxation as an executable certificate. It is not a claim that the relaxation is an invalid mathematical theorem, or an allegation about an external proof.

## 4. Symmetric selection and persistent fairness are different information tasks

Every permutation of the four event labels induces a unique permutation of the six resource classes: resource i is the unique intersection of a pair of event types. The automorphism group is S4. A fully symmetric capacity input q*1 is fixed by this action.

A deterministic equivariant batch selected from that input alone must be fixed by S4, so all four x_S=k. The largest such batch contains

    4 floor(q/2) events.                                (5)

For q=1 it is empty. For odd q it is one event short of the unrestricted integer optimum. No deterministic symmetry-preserving rule using only these symmetric capacities can always select a maximal legal batch: any odd-q invariant batch leaves at least one event addable. This does not prohibit a full state containing material orientation or distinguishable environmental relations.

At odd q the four optimal batches form one S4 orbit without a fixed point. T7's fixed-lift criterion therefore rules out a section over this symmetric observation. A decoration selecting one optimal branch needs at least four states over that observation, with the appropriate group action. Retaining all four branches is an equivariant relation, not a deterministic selector and not an automatically justified probability measure.

Now require an autonomous deterministic controller H with equivariant update V and output q:H->{A,B,C,D}. Suppose the future of a control state eventually selects every event type. If g fixes h, equivariance makes g fix V^t(h) and every future output. Since all four types occur, g fixes all four labels and is the identity. Thus the stabilizer of h is trivial and its S4 orbit has 24 states:

    |H|>=24 on any fair orbit.                          (6)

This is stronger than the four-state one-shot selector bound. It also permits infinite H: a fair orbit still has at least 24 distinct symmetry images. External tie breaking, random updates, or storing asymmetry in the surrounding field are different contracts, not counterexamples.

The bound is attained by ordered frames h=(a,b,c,d), all 24 permutations, with V(h)=(b,c,d,a) and output a. It visits all four types every four macro-events and commutes with relabeling. The frame includes cyclic order as well as phase; it is not merely a four-state clock. It is an explicit initial relational state, not information spontaneously manufactured from a symmetric count observation.

## 5. Token provenance survives even when aggregate event counts are unique

For x in X(n), write d=Ax. The exact number of token-labelled, unordered event collections with aggregate x is

    L(n,x) = [product_i n_i!/(n_i-d_i)!] / [product_S x_S!].   (7)

Proof: temporarily order the x_S copies of each type. At each resource class assign distinct available tokens to its d_i incident event slots, in (n_i)_{d_i} ways. Removing the auxiliary order of each type divides by x_S!. The action is free because disjoint events have different token sets. This leaves actual token incidence, not just marginal counts.

For n=2*1 and x=(1,1,1,1), aggregate allocation is unique but L=2^6=64. Each resource chooses which of its two tokens serves which incident event. Omitting this assignment while later asking for particle paths is an uncertified quotient. Conversely (7) is a legitimate count observer for the declared one-phase counting question; it does not supply probabilities or erase future path distinctions.

As a control, admitting all 20 triples on six resources at unit capacities permits two complementary disjoint events, with ten maximal partitions. These ten form a transitive S6 orbit. Enlarging the palette fixes this particular capacity shortfall but still does not produce a canonical deterministic partition at a fully symmetric state. It also does not justify declaring all 20 triples physically admissible.

## 6. Relate, but do not confuse, signed spatial closure and unsigned capacity

The previously fixed signed carrier paths are

    r_A=e1-e3-e6, r_B=e1-e4-e5,
    r_C=e2-e3+e5, r_D=e2-e4+e6.

Each has zero FCC readout but is a nonzero native displacement. Component elimination gives

    sum_S q_S r_S=0 iff q=lambda*(1,-1,-1,1).            (8)

The smallest nonzero net relation uses each type once. Under the **additional same-phase single-use resource contract**, its unsigned demand is A*|q|=2|lambda|*1. Thus at least two tokens per resource are needed to reserve that whole nonzero net block at once, and two suffice for reservation.

This is not a lower bound on inventory for all sequential executions. The same token may be used again after a completed event; doing so requires the completion/release record and time ordering. Nor does (8) define force balance. Repeated opposite paths with zero net type vector lie outside the nonzero-net minimality statement.

## 7. A fully specified two-tick spatial router attaining the 24-frame bound

This is a new, explicitly typed packet-routing **test interface**, not a replacement of the density-port collision law and not an admitted force model. Supply a Cell anchor c, the four incidence types, one distinctly labelled packet at each of the six Cells c+e_i, and an internal ordered frame h=(a,b,c_0,d). Also retain whether the current event is at its boundary or its in-flight stage.

The current event is a. Its three axes are the pairwise intersections of a with b,c_0,d, in that order; call them i,j,k. Thus the stored frame also determines its orientation, without a second external sign selector.

First native tick:

    c+e_i -> c+e_i+e_j,
    c+e_j -> c+e_j+e_k,
    c+e_k -> c+e_k+e_i.

Second native tick:

    c+e_i+e_j -> c+e_j,
    c+e_j+e_k -> c+e_k,
    c+e_k+e_i -> c+e_i.

Other packets stay. Commit rotates the frame to (b,c_0,d,a). The in-flight state retains the active frame and token identities, so the next tick is determined internally. All nonzero moves are primitive +/-e_i; the three intermediate Cells are distinct and none is another resource Cell. Three packet paths each use two primitive steps, not a forbidden three-step native triangle. Token number and identity are conserved, no token is double-reserved, and no force or residual variable is added.

The native sum of packet positions increases by e_i+e_j+e_k at the midpoint and returns at the boundary. This change is recorded explicitly and is NOT called a conserved physical momentum or paid for by an invented reservoir. Conservation of mechanical energy, force admissibility and viscosity are not established.

Every macro-event restores the same spatial count pattern (one packet at each resource Cell), although identities move. The full update is equivariant under the atlas S4; an arbitrary S6 coordinate change is covariant only when the incidence template is transported with it. Anchor translations commute with both ticks. A fixed carrier choice is never imposed as an invariant physical interaction under arbitrary relabeling.

For frame (A,B,C,D), the successive current-axis orders are

    (1,3,6), (5,4,1), (2,3,5), (6,4,2).

Starting with packet labels (1,2,3,4,5,6) in resource slots, after four macro-events their slot list is

    (4,5,2,3,1,6).

This permutation is a five-cycle plus one fixed point. The frame has period four; consequently the full state with distinct token identities has exact macro-period 20, or 40 native ticks. All frames are S4 conjugates and all initial token placements are relabelings, proving the same exact period for the entire stated state family. The checker additionally exhausts all 24*720=17,280 boundary states.

This supplies an autonomous, fair, conflict-free, provenance-preserving event-order example. It supplies a recurrent control, not an instability example. The unchanged boundary count pattern cannot determine the next intermediate spatial count: different active frames move different triples. Retaining phase/frame is essential for the microstep observer even though boundary counts are constant.

## 8. Executed checks and next frontier

The standalone standard-library checker runs with no network, floating point, continuum limit, or imported source modifications. It verifies:

- all 5^6=15,625 capacities in {0,...,4}^6 against independently generated exact decompositions (117 fully decomposable);
- 13 symmetric capacities q=0,...,12, all 13,447 allocations and 40,341 generator covariance equalities;
- independently enumerated token-batch counts 64,4,1,486;
- ten complete-palette maximal partitions and 7,200 S6 correspondence checks;
- 2,401 bounded signed-relation coefficient vectors;
- 576 controller covariance equalities, 480 sample macro-events with 2,880 nonzero native moves, all 17,280 boundary states' exact period, 720 arbitrary-axis transported-template checks and three nontrivial translations.

The formulas for arbitrary q, controller-state lower bound and exact recurrence have ordinary proofs above; finite enumeration is a regression check, not their substitute. These calculations use familiar integer allocation and group-action methods; no historical priority claim is made.

The next physical gap is narrower: a material triadic event mechanism must specify token eligibility, read dependencies, shared-resource reservation, actual intermediate exchanges, and completion/release, and show its relation/frame evolution respects those contracts. The current router demonstrates logical/coordinate compatibility, not that this mechanism is nature's law or that it reproduces F_Gamma. An invariant allocation, a three-label event, spatial return, and count conservation each solve different obligations. None alone proves TRIADIC_CLOSURE_E, physical f=0, dissipation, or NS regularity/blowup. No P000, README, accepted theorem or another researcher's assignment is changed.
