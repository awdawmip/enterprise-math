# Native X6: labeled exchange lifts, conservative directional transfer, and mean-velocity amplification

Progress-Event-ID: `NS-NATIVE-EXCHANGE-LIFT-20260909-D5C00D-11`
Researcher-ID: `EM-DIRECT-D5C00D / TASK_RESEARCH`
Research-Activity-ID: `RA-D5C00DF7D77F4AA2ACE0`
Status: `ORDINARY_PROOFS + EXECUTED_EXACT_CHECKS / CANDIDATE_MODEL / NOT_FORCE_ADMISSION`

## 1. Frozen problem and sources

Continue the existing autonomous count law `X6-DENSITY-PORT-1` without changing its eligibility, score, tie, or streaming rules. Its source is `awdawmip/enterprise-math@6f119ea99021f83141321a5241dcb33b70f5af44`, especially:

- `research_notes/ns-native-density-port-20260909-d5c00d.md`;
- `experiments/ns_native_density_port_d5c00d.py`, blob `6139c2e444f656e1b62169b6cf14c48f2f3e2405`;
- `experiments/ns_native_ternary_coherence_d5c00d.py`, blob `5dd5e0bce49c5d37360d34e0f9013830f7600357`.

Both parent Python files are imported unchanged. The current source-control read is `6a2006821783c558761d17049cd0d07fc51d47d0`; P000 V5, signed X6 Cell anchors, and the joint-observer preservation contract retain their scope. BRC is applied to the exact count projection, matching-history multiplicity, and the failure of density/moment-only descent. This is an application-specific extension, not a newly admitted shared tool family. A bounded repository search for particle/collision/provenance methods returned no matches; that does not establish absence of related work or historical novelty.

The mathematical axes here are 1-based. Code axes are 0-based. For algebraic budgets, write `[x,y]=sum_i x_i*y_i` and `|x|_c^2=sum_i x_i^2`. This is the declared component pairing and squared-component readout, NOT a Euclidean-cosine reinterpretation of the native 120-degree relation.

A collision at Cell z has input channels

    {sigma E_j, +E_l, -E_l},  j != l,

and chooses m distinct from j,l only if it uniquely maximizes

    A_m(z)=N(z+E_m)+N(z-E_m),  N(z)=sum_v n_v(z).

Ties wait. The output count multiset is `{sigma E_j,+E_m,-E_m}`. All Cells use the same old field. Each resulting packet then moves one actual signed-axis step. Denote this fixed count update by F.

The parent has an ordinary induction proving, for the constant count background b=`{+E_1,+E_2,-E_2}` and a single +E_1 packet moved from E_1 to 0,

    D_t=sum_{z,v}|F^t(n)_v(z)-b_v| >= 32t+2.

This note consumes that durable induction and checks new consequences against the unchanged full six-axis implementation. It does not rebrand the parent proof as new work.

## 2. Complete microscopic matching census at one collision

Give the three incoming packets distinct identities. Only the channel sigma E_j occurs in both the input and output sets. A bijection between the three incoming identities and three outgoing channels has 3!=6 possibilities.

Exactly two bijections leave the sigma E_j packet on that same channel. The other two particles both change their axes. Exactly four bijections move all three particles to different axes. No matching moves only one particle.

If Delta_a is the change of channel vector of particle a, every nonzero change has two components of magnitude one. Consequently:

    two changed particles: sum_a |Delta_a|_c^2 = 4;
    three changed particles: sum_a |Delta_a|_c^2 = 6.       (2.1)

All six matchings have identical input/output counts, conserved additive channel moment, and conserved unit-channel kinetic readout. The checker exhausts 240 signed ordered ports and all six matchings per port (1,440 instances), obtaining 480 two-change and 960 three-change instances.

This is a statement about particle-channel changes. It is NOT a classification of primitive force arity: three changed identities are not, by themselves, a certificate of `TRIADIC_CLOSURE_E`.

## 3. Two explicit lifts of the unchanged count dynamics

Write the input identities in their channel-defined order:

    A: sigma E_j, B: sigma E_l, C: -sigma E_l.

Define lift L2 by

    A -> sigma E_j, B -> sigma E_m, C -> -sigma E_m,

and lift L3 by

    A -> sigma E_m, B -> sigma E_j, C -> -sigma E_m.        (3.1)

The label names themselves play no part in either rule. At an eligible Cell there is exactly one packet in each of the three incoming channels, so the rule specifies a unique routing. At all other Cells retain the packet channels. Then stream each packet along its assigned signed primitive direction. The old count field supplies the same port in both lifts.

Let pi forget identities and retain the complete count field. For every legal labeled state s,

    pi(L2(s)) = F(pi(s)) = pi(L3(s)).                     (3.2)

Proof: at each eligible Cell both bijections have precisely the prescribed output multiset; at other Cells neither changes a count. Streaming and count projection commute because both count the same packets at the same destination slots. Induction gives (3.2) for every finite iterate. There is no sampled-trajectory extrapolation here.

The lifts commute with translations, S6 axis relabeling, global simultaneous spatial/channel reversal, and arbitrary renaming of the particle identities. We do not claim covariance under every independent signed-basis reversal; a stronger sign-frame contract would have to transform an appropriate matching decoration or retain the full matching relation. Nor is either full lift asserted to be reversible merely because a local matching is a bijection: the density-driven selection may erase information.

Thus the parent amplification trajectory has an explicit all-three-particles-change lift. No forcing, count correction, future trajectory, or desired growth rate was inserted into F to obtain it. Selecting L3 as the actual physical realization would nevertheless be an additional constitutive decision, not a theorem from P000.

### 3.1 Exact BRC matching-history count

Fix the initial identities and a finite count trajectory containing c collision events. At every event all six matchings remain count-compatible. Independent choices yield exactly 6^c event-matching histories. The count refers to FULL HISTORIES; some terminal labeled states could coincide after different histories.

The cost-generating polynomial is

    (2 x^4 + 4 x^6)^c.                                  (3.3)

The coefficient of x^(4c+2k) is binomial(c,k)*2^(c-k)*4^k. No probability distribution or physical amplitude is assigned by this integer enumeration. For the first eight collisions of the parent witness there are 1,679,616 matching histories, including 256 all-two-change and 65,536 all-three-change histories.

The matching can be erased for future COUNT observations because (3.2) proves exact descent. It cannot be erased for a query asking which particles changed or which matching-history cost occurred. Over the union of these compatible lifts, the same complete count trajectory has different costs. Once a particular matching law has separately been fixed, some aggregate costs can of course be reconstructed from that law and the count event history; the obstruction is not promoted beyond its observer scope.

## 4. A three-edge internal exchange ledger, and its precise limitation

For L3 the channel changes are

    Delta_A = sigma(E_m-E_j),
    Delta_B = sigma(E_j-E_l),
    Delta_C = sigma(E_l-E_m).

They admit the incidence ledger

    q_AB=sigma E_j, q_BC=sigma E_l, q_CA=sigma E_m;
    Delta_A=q_CA-q_AB;
    Delta_B=q_AB-q_BC;
    Delta_C=q_BC-q_CA.                                   (4.1)

Every exchange entry is axis-typed; each of the three packet identities has a nonzero net channel change; summing the incidence equations cancels all internal exchanges exactly. This improves on merely attaching a triangle label: the ledger reproduces the actual three channel changes of a count-compatible lifted trajectory.

It does NOT supply the missing physical incidence law. The vertices in (4.1) are packet identities at a collision, not three spatial Cells. An exchange entry is an algebraic ledger entry, not a proof that a material momentum token was physically present and transferred. A three-edge incidence cycle does not claim to be a three-step spatial loop, and its zero total additive increment does not define P000 force closure. The actual spatial motions still use individual signed primitive steps.

The unresolved bridge must state how legal native force events produce these exchanges, how the neighboring scoring information is communicated, and whether the proposed events meet `TRIADIC_CLOSURE_E`. Count conservation alone supplies none of those identifications. This note adds no P000 clause, no force axiom, and no physical force-admission certificate.

## 5. The turning-square ledger is not dissipated energy

All incoming and outgoing packet channels have component squared length one. Therefore each collision has

    E_kin = (1/2) sum_a |v_a|_c^2 = 3/2

both before and after it. Direct expansion gives the EXACT work identity

    0 = sum_a [v_a,Delta_a] + (1/2)sum_a |Delta_a|_c^2.   (5.1)

The first term is -2 for the two-change matchings and -3 for the three-change matchings. The positive turning-square term in (2.1) is compensated, not lost. Calling it heat generation or viscous dissipation without another energy account would be wrong.

More generally, each allowed collision preserves the entire local multiset of the twelve occupation numbers: precisely three distinct slots contain one, the other nine contain zero, both before and after. All other configurations are unchanged. Streaming permutes spatial-channel slots. Hence for every function phi with phi(0)=0 and every finite-particle configuration,

    H_phi(n)=sum_{z,v} phi(n_v(z))

is conserved. For a finite deviation from the constant background, the same proof conserves the finite relative sum `sum(phi(n)-phi(b))`, without any convergence argument. In particular the parent perturbation has

    sum_{z,v} (n_v(z,t)^2-b_v^2)=2                       (5.2)

for all t. Occupations >=2 never occur in a changed collision and stream on their original channels; the protected double-occupation carrier in the parent proof is therefore a genuine SPECIAL FEATURE of this constitutive rule, not a generic mechanism forced by native geometry.

Microscopic kinetic conservation does not rule out an emergent coarse dissipative law. It does rule out equating the present positive turn ledger with a loss of this conserved kinetic readout. A separate bulk/fluctuation/interaction energy bridge is required.

## 6. Exact directional energy transfer along the parent trajectory

In the parent's invariant layer class the +E_1 field differs from b only by one excess and one hole; there is no -E_1 channel. All other slots have occupation zero or one. The only positive deviations in a background-occupied channel are the single longitudinal excess. Put

    B_t = sum_z sum_{i=3}^6 (n_{+E_i}(z,t)+n_{-E_i}(z,t)).

All terms are zero in b and B_t is finite for each finite t. Every positive difference is either the single excess or a packet counted by B_t. Relative count zero makes the negative and positive totals equal. Therefore

    D_t=2+2B_t,
    E_perp(t):=B_t/2=(D_t-2)/4 >= 8t.                  (6.1)

This is a directional unit-channel kinetic READOUT, not total energy creation. The relative longitudinal energy is zero and the relative axis-2 energy is exactly -E_perp(t). Existing background traffic supplies the transverse population.

Let C_+(r) count collisions in step r routing the pair from axis 2 to axes 3--6, and C_-(r) those routing back. Transverse-to-transverse reroutings change neither total. Collision changes B by +2,-2,or 0; streaming preserves global directional counts. Thus

    E_perp(t)=sum_{r<t}(C_+(r)-C_-(r)).                  (6.2)

The checker retains both signed directions; it does not assume C_- is always zero. In the first five executed steps the net transfers are 8,72,368,1416,4328. No eventual monotonicity or exponential rate is inferred from those values.

## 7. Strengthening the parent result to density and mean-velocity observers

Define the finite local readouts

    rho(z)=sum_v n_v(z),
    P_i(z)=n_{+E_i}(z)-n_{-E_i}(z),
    ubar(z)=P(z)/rho(z) if rho(z)>0; ubar(z)=0 otherwise.

For any nonnegative channel state, `sum_i |P_i| <= rho`; hence

    |ubar(z)|_c^2 <= 1.                                 (7.1)

This is a finite inequality, not a smoothness hypothesis. The baseline is ubar_b=E_1/3.

The parent's protected-hole lemma is stronger than merely asserting that a channel is absent: at each of its sixteen distinguished boundary Cells in every wake, the COMPLETE local state is

    {+E_1,-sigma E_2}.

Thus rho=2, P=E_1-sigma E_2, and

    |ubar-ubar_b|_c^2
      = |E_1/6-sigma E_2/2|_c^2 = 5/18.                (7.2)

At time t these 16t Cells occupy distinct layers/positions. The longitudinal hole is another negative density unit; total relative density is zero. Consequently, for all integer t>=0,

    sum_z |rho(z,t)-3| >= 32t+2,
    sum_z sum_i |P_i(z,t)-(E_1)_i| >= 16t+2,
    U_t:=sum_z |ubar(z,t)-E_1/3|_c^2 >= 40t/9.           (7.3)

All sums are finite deviations at each finite t. Density and moment statements use their declared coarse observers; they are not obtained by assuming every channel discrepancy survives averaging. Equation (7.2) is the explicit surviving fiber contrast.

The initial mean-velocity difference is

    U_0=(1/2-1/3)^2+(0-1/3)^2=5/36.

Uniformly bounded pointwise velocity therefore coexists with unbounded TOTAL squared mean-velocity discrepancy in this infinite-background model. It is spatial proliferation, not an unbounded local speed.

### 7.1 Finite-particle, finite-horizon theorem

For every T>=1, reuse the parent's finite cube of radius R=3T+3 and the same single-packet move. Evolve BOTH finite initial configurations by F with a freely evolving zero exterior; do not freeze the boundary or add particles. The radius-two dependency lemma proves that all 16T protected witness Cells match their infinite-background counterparts at time T.

For the two finite evolutions, with the vacuum convention for ubar,

    U_T^finite >= 40T/9,
    U_0^finite = 5/36,
    U_T^finite/U_0^finite >= 32T.                        (7.4)

This is `for each T there exists a finite initial pair`, with one fixed law. It is NOT unbounded growth in one fixed finite population and not a fixed-resolution Lyapunov-instability statement. The increasing population is an explicit resource in this quantified result. These bounds do not solve classical NS or establish a physical instability theorem.

## 8. An exact finite moment system; what density and mean velocity erase

Let q_i=n_{+E_i}+n_{-E_i} and p_i=n_{+E_i}-n_{-E_i}. The constraints

    q_i>=|p_i|, q_i==p_i (mod 2)

are necessary and sufficient for nonnegative integer reconstruction:

    n_{+E_i}=(q_i+p_i)/2, n_{-E_i}=(q_i-p_i)/2.           (8.1)

Thus the six p_i and six q_i are an EXACT alternative state, not a closure approximation. Also rho=sum_i q_i. At collision p is unchanged and

    q_i^c=q_i+2(1_{i=m}-1_{i=l})

for an event; otherwise q^c=q. The port scores use the neighboring rho from the old q field. Streaming then gives

    p_i'(z) = [q_i^c(z-E_i)-q_i^c(z+E_i)
                +p_i(z-E_i)+p_i(z+E_i)]/2,
    q_i'(z) = [q_i^c(z-E_i)+q_i^c(z+E_i)
                +p_i(z-E_i)-p_i(z+E_i)]/2.              (8.2)

These are finite shift identities on the original six-axis lattice. The parity constraints make their reconstructed occupation outputs integers. No continuum limit or differential equation is invoked. The diagonal second channel moment changes by `2(diag_m-diag_l)` and has zero trace; it has not been identified with a physical stress law.

Density and p ALONE do not determine the future. Two isolated Cell states C_2(1,+) and C_3(1,+) have identical density and p fields everywhere, and zero neighbor scores so no collisions. After one streaming step one has a packet at E_2 and the other does not. Thus their next density fields differ. This is an exact BRC descent failure, not a numerical closure error.

A scalar kinetic readout adds no information because it equals rho/2. Direction-resolved q, or an adequate proven replacement, must remain. Arbitrary bit packing into fewer integers is not excluded; the point is the information needed by the particular declared observer and future update.

## 9. Executed validation

Run beside the two unchanged parent files:

    python ns_native_exchange_lift_d5c00d.py --steps 5 --output results.json

Executed checks include 1,440 matching/work identities, 240 exact exchange cycles, 2,400 S6-generator covariance checks, 480 global-reversal checks, the eight-event history polynomial, and 729 exact integer moment reconstructions.

A four-packet zero-background witness is evolved for eight ticks under BOTH labeled laws and the original count-law implementation; all count fields agree, while identities differ. A free-boundary 2,187-packet witness is evolved for four ticks, again with exact agreement; its first step has 288 collisions, turning-square budgets 1,152 versus 1,728, and 576 different tagged states. Later tested steps in this small witness have no additional collisions; no repeated-collision evidence is attributed to them.

The full infinite-background sparse count solver runs five ticks, checking (7.2), histogram conservation, the exact directional budget, and the following new observers:

| t | channel L1 | density L1 | moment L1 | transverse kinetic readout |
|---|---:|---:|---:|---:|
| 0 | 2 | 2 | 2 | 0 |
| 1 | 34 | 34 | 26 | 8 |
| 2 | 322 | 322 | 242 | 80 |
| 3 | 1794 | 1794 | 1346 | 448 |
| 4 | 7458 | 6994 | 5610 | 1864 |
| 5 | 24770 | 22258 | 18658 | 6192 |

The last distinction matters: starting by the fourth tick, channel discrepancy and density discrepancy are NOT equal. The proof never assumes they are. Mean-velocity squared sums are retained as exact rational numbers in the result JSON, not rounded certificates. The finite p/q shift system is checked independently of direct streaming on five selected states.

## 10. Frontier and scope

Completed: two all-time count-compatible labeled lifts; a concrete three-edge internal additive exchange ledger; an exact observer/arity underdetermination theorem and matching-history count; conserved occupation/kinetic budgets; signed directional transfer; finite moment equations; density and mean-velocity amplification with finite-population horizon witnesses.

Still missing: an admitted native force-incidence and interaction-energy law that selects or restricts such lifts and yields the density-dependent port rule. Merely renaming (4.1) as `TRIADIC_CLOSURE_E` would be circular. Three changing packets, zero total additive increment, and a graph cycle are not substitutes for that law. The higher-occupancy ballistic protection also needs physical justification or replacement in any claimed fluid realization.

Next exact mathematical unit: specify an independently typed local interaction state and energy/communication ledger for the port, then test whether its actual induced count transition is F, a constrained subrelation of F, or requires a revised candidate. Retain all current proofs at their frozen scope whichever branch survives. No physical viscosity, classical f=0 theorem, Foundation admission, independent review, Lean verification, or historical priority is claimed. No README, P000, or another researcher's assignment was changed.
