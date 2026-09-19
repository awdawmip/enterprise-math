# Native X6 joint exchange: integer remainders, encounter coverage, and a finite relaxation theorem

Event: `NS-NATIVE-INTEGER-EXCHANGE-20260910-D5C00D-15`  
Researcher: `EM-DIRECT-D5C00D / TASK_RESEARCH`  
Activity: `RA-D5C00DF7D77F4AA2ACE0`  
Status: **TESTING — ordinary finite/algebraic proofs and executed exact checks, not primitive-force admission or a Navier–Stokes theorem.**

## 0. Exact question, assumptions, and recovered frontier

The parent problem is native discrete dynamics compatible with the six-axis Cell coordinates, followed only subsequently by a justified physical or classical-fluid interpretation. Event LINE-TRANSPORT-14 established that binding a carried axial quantity to its streaming direction locks a separate total on every coordinate line. Its joint carried-quantity/path interface avoids that obstruction, but it did not supply an exchange law for the carried quantities.

This note asks a precise conditional question: can an explicitly stated integer exchange among three actually gathered participants, coupled to a provenance-preserving native path, conserve the carried total and yield a provable finite quadratic-loss budget? Which encounter information is necessary for that local operation to relax the full finite population?

**The exchange law is a constitutive test choice, not a consequence of P000.** Its quadratic is a diagnostic chosen on integer carried labels. Those labels are not identified with physical momentum, and the quadratic is not identified with total physical energy. No hidden heat reservoir or residual force is added. Choosing a dissipative operation cannot then be counted as independent evidence that nature dissipates in this fashion. A conservative comparison is provided in Section 9.

Source snapshot read in this turn: `awdawmip/enterprise-math@a12be839318bded31998207ee18ef76762b7a856`. Global entry snapshot: `2b27c41bbc488ceb1a0b0f7c53afad9df12abe16`.

Relevant source reuse:

* `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`: signed Cell torsor, primitive spatial steps, decorations distinct from spatial coordinates;
* `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`: force arity is not particle count, and native force closure is not an additive-vector identity;
* joint-observer preservation and T7 stabilizer/fiber principles, applied before erasing role assignments or controller state;
* the published `experiments/ns_native_event_capacity_d5c00d.py`, current Git blob `70e5cec37847d34fe0c4bcc4f5305fd224fca08d`. Its `frame_axes` and `macro_step` are executed through the unchanged, explicitly marked callable extract from the supplied LINE-TRANSPORT package (extract SHA256 `a06546610f5e8b2679cc426007c54a6458e6874197a45d436606b981e8a9ab34`). This is not described as a full rerun of the upstream program;
* new remote CAUSAL-RETURN-14 is consumed as a separate existing result, not confused with the locally delivered LINE-TRANSPORT-14. Full event IDs, not numeric suffixes, identify frontiers.

A bounded source search for integer balancing returned no hit; this is not an absence or novelty certificate. Integer load balancing/quantized consensus are established external topics: Kashyap, Başar and Srikant, *Quantized consensus*, Automatica 43 (2007), 1192–1203, DOI 10.1016/j.automatica.2007.01.002; Feuilloley, Hirvonen and Suomela, *Locally optimal load balancing*, DISC 2015. We do not claim priority for convex integer balancing. The present contribution is the exact application to the declared ordered-frame/native-path interface, including its counterexample and scoped minimal controller extension.

All axes in formulas are 1-based; Python uses 0-based indices. No Euclidean angle substitution, continuous limit, or infinitely smooth extension is used.

## 1. A linear integer mixing obstruction

Let T be an integer n-by-n matrix. Suppose for every integer vector x it preserves the coordinate sum and does not increase the component-square sum:

    1^T T x = 1^T x,      ||Tx||_2^2 <= ||x||_2^2.       (1.1)

**Theorem 1.** T must be a permutation matrix.

**Proof.** Apply the norm condition to each unit vector. Each integer column has square sum at most one and coordinate sum one, so it is a positive unit vector. Two columns cannot be equal: applying (1.1) to the sum of their two corresponding unit inputs would give output square sum four but input square sum two. Hence the columns are the distinct unit vectors. QED.

For three participants, if in addition the rule commutes with every participant permutation, the only such matrix is identity: a permutation commuting with all transpositions of three labels fixes all three labels. Thus a universally integral, sum-conserving, quadratic-nonincreasing linear map cannot supply strict averaging. The rational averaging matrix J/3 is valid as a rational map, but is not an integer-valued update on all integer inputs.

This is an obstruction within (1.1), not a ban on nonlinear exchange, a relation-valued update, explicit remainders, or a separately specified changed precision.

## 2. Exact integer three-participant exchange

For x=(x1,x2,x3) in Z^3, set S=x1+x2+x3 and write the Euclidean division

    S=3a+r,       a in Z, r in {0,1,2}.                  (2.1)

Among integer triples with sum S, the minimum square sum is

    Phi3_min(S)=3a^2+2ar+r.                              (2.2)

Its minimizers are exactly the permutations of r copies of a+1 and 3-r copies of a. To prove this, if a largest and a smallest entry differ by at least two, transferring one unit from the former to the latter lowers the square sum by 2(largest-smallest-1)>0. A minimizer must therefore have range at most one, and (2.1) determines its values. Conversely those values attain (2.2).

Define R on an **ordered triple of retained participants**:

* if max(x)-min(x)<=1, leave the complete triple unchanged;
* otherwise assign a+1 to the first r ordered participants and a to the rest.

This rule is fixed before the exchange tests. The participant order comes from the existing material frame, not an arbitrary numerical particle-ID ordering. This choice is not claimed to be the unique native rule.

The exact loss is

    d(x)=sum_i xi^2-Phi3_min(S) in 2 Z_{>=0}.             (2.3)

The parity follows from xi^2=xi modulo two. Moreover,

    d(x)=0 iff R(x)=x iff max(x)-min(x)<=1.               (2.4)

Thus a changed load costs at least two quadratic units. Input min/max bounds and nonnegativity, when present, are preserved. The rule works for negative as well as positive integers; no truncation toward zero is substituted for (2.1).

The exact remainder identity is

    3 Phi3_min(S)-S^2 = r(3-r).                         (2.5)

For r=1 or 2 the residual variance is nonzero. R does not pretend to put S/3 into every integer slot or erase the indivisible remainder. Coordinatewise application defines an exchange on three labels in Z^6, preserving every carried-component total and giving the sum of the six losses (2.3).

The minimizer assignment is not participant-symmetric without its ordered-role data. For example (0,0,2) has the swap of the first two participants as a stabilizer, while assigning a singled-out remainder to one of them would need additional information. No such information is manufactured from the unordered observation.

## 3. Actual pair encounters are the global criterion

Consider a fixed finite population of N identifiable tokens, whose encounters are a recurrent prescribed-by-state sequence of ordered triples. Labels remain attached to token identities between exchanges. Assume every encountered triple is updated by R and leave already balanced component triples unchanged as above.

Let G be the graph on **token identities** having an edge whenever a pair co-participates in a triple in a recurring period. It is not the static graph of resource slots or event types.

A scalar assignment is stationary under all these exchanges iff each edge of G has endpoint difference at most one. Indeed every triple is a clique in G, and (2.4) is exactly its range-at-most-one condition.

**Theorem 2 (necessity).** If G is not complete, there is a nonglobally-balanced stationary assignment: choose two nonadjacent tokens u,v, put x_u=0, x_v=2, and put one on every other token. No triple contains both u,v; each triple is already integer-balanced. The global range remains two.

If G is connected, every such stationary assignment has global range at most diameter(G), by summing the edge inequalities along a shortest path. This upper bound is sharp: distances from a vertex with maximal eccentricity give an integer assignment whose adjacent values differ at most one. Connectedness therefore gives local balancing, not generally the global integer minimum.

For a quantitative sufficient condition assume **every block of W consecutive actual encounters covers every token pair**. Let

    Phi=sum_alpha,a q_{alpha,a}^2,
    S_a=sum_alpha q_{alpha,a},
    S_a=N b_a+r_a, 0<=r_a<N,
    Phi_min=sum_a [N b_a^2+2 b_a r_a+r_a].                (3.1)

Every exchange conserves S and decreases Phi by a nonnegative even integer. In a block with no decrease no token label changes. If the assignment at that block's start were not globally balanced, a component would have a pair differing by at least two; the pair occurs in that block and would cause positive loss. Contradiction.

**Theorem 3 (finite relaxation).** With W-block complete pair coverage, the integer label field reaches its global minimum Phi_min by at most

    W (Phi(0)-Phi_min)/2                                 (3.2)

macro-events, with zero events needed when the difference is zero. Thereafter all labels are fixed on identities and each component differs by at most one across the population. The exact cumulative loss telescopes:

    Phi(T)+sum_{s<T} d_s=Phi(0),
    sum_s d_s=Phi(0)-Phi_min.                            (3.3)

Proof of the bound: before reaching the minimum each W-event block loses at least two; the initial nonnegative even excess permits at most (Phi(0)-Phi_min)/2 such blocks. QED.

All statements are about finite integer operations. If labels carry a fixed quantum delta>0, quadratic quantities gain a factor delta^2 and the minimum positive loss is 2 delta^2. No uniform delta-to-zero or growing-population conclusion is asserted.

## 4. The previously published 24-frame router fails the criterion

The supplied four event types are A=136, B=145, C=235, D=246. These remain a resource template, not a force-incidence identification. At event frame h=(a,b,c,d), the active axes are the three pairwise intersections of a with b,c,d in that order. The existing macro route cyclically permutes the three participating tokens among these resource slots; the old controller rotates h to (b,c,d,a).

Start with identities 1,...,6 in slots 1,...,6. The recurring **identity triples** are

    136, 456, 126, 356, 246.                             (4.1)

Their period is five although the full frame/token boundary state has period twenty. Identity 6 participates in every event; the other five form the cycle 1-3-5-4-2-1. Only ten of the fifteen possible pairs ever meet.

Take identity loads

    (0,1,1,2,1,1).                                      (4.2)

Every triple in (4.1) has range at most one. R never changes it. Its total is six and Phi=8, while Phi_min=6. An endlessly recurring fair event schedule can therefore keep a strictly nonminimal integer load assignment forever.

This is a provenance-sensitive failure: all four event types occur, all six tokens move or participate, and the static template is connected, but the actual pair encounters still omit the pair (1,4). No later equilibrium conclusion may replace token-level encounters by those coarser facts.

## 5. A scoped minimal 48-state order extension

Keep the frame-to-route interface and require an order controller that does not inspect carried charges or numerical token names. The frame set is the free transitive S4 set of all 24 ordered frames. Any equivariant deterministic update on this set alone is right multiplication by a fixed permutation r:

    h'_i = h_{r(i)}.                                    (5.1)

For its first entry to recurrently visit every event label, r must be a four-cycle. There are exactly six. Computing the existing route gives:

| zero-based r | full macro-period | identity pairs encountered |
|---|---:|---:|
| (1,2,3,0) | 20 | 10 |
| (1,3,0,2) | 12 | 9 |
| (2,0,3,1) | 20 | 10 |
| (2,3,1,0) | 12 | 9 |
| (3,0,1,2) | 12 | 9 |
| (3,2,0,1) | 20 | 10 |

This finite table exhausts (5.1) under the specified recurrence condition. None has complete pair coverage, hence all have a stationary counterexample from Theorem 2.

Now retain one additional order bit b, distinct from the already necessary flight phase, and fix

    r0=(1,2,3,0), r1=(2,0,3,1),
    (h,b) -> ((h_{r_b(0)},...,h_{r_b(3)}),1-b).           (5.2)

The token boundary permutation is still the published macro_step. The controller is autonomous and S4-equivariant when frame labels are relabelled; arbitrary S6 coordinate relabelling transports the template too. The bit is a declared current-state coordinate, not an external time-dependent selector.

The repeating identity triples, starting at the chosen base state, are now

    136,456,235,246,134,126,356,125,234,145.              (5.3)

Each pair occurs exactly twice in these ten triples. More strongly, every eight consecutive triples, including windows crossing the period boundary, contain all fifteen pairs. Eight is sharp for this schedule: some windows of seven omit a pair. The full order/frame/token state has macro-period thirty (native-flight period sixty), while (5.3) has period ten. Frame conjugacy, identity relabelling and time shift prove the same coverage from every valid frame/bit/token state. The checker verifies all 48 frame/bit starts explicitly.

**Minimality scope.** For a finite equivariant extension E of the *same complete frame interface* with a surjective equivariant frame map E->Frames, all fibers have equal cardinality k. Hence |E|=24k. k=1 reduces to (5.1), which fails. k=2 is realized by (5.2). Therefore 48 is minimal in this frame-extension class. This is not a lower bound on all possible physical controllers, charge-dependent routing, arbitrary new event orientations, or state stored outside the controller. Flight phase gives 96 order-and-flight control states; positions, labels and provenance are additional state, so total system state is not 48.

The rule (5.2) was selected by a disclosed finite search over 36 pairs of the six four-cycle updates; six satisfy complete coverage. This search is design, not independent experimental validation or proof of a natural law. Recurring visitation is not a claim of equal event-label frequencies.

## 6. A spatially local gather–exchange–scatter realization

Use one labelled token at each resource Cell c+e_i. Retain source-slot->token identity, ordered event frame, order bit, and flight phase.

For active ordered axes (i,j,k), the first tick gathers:

    c+e_i -> c,   c+e_j -> c,   c+e_k -> c.              (6.1)

Inactive tokens rest. Three tokens at a common Cell are allowed in this explicitly stated test interface; exclusion is not assumed. Carried labels do not change during this tick.

At the start of the second tick, apply the coordinatewise operation R to these three actually co-located tokens in their retained order. Then scatter cyclically:

    token from i: c -> c+e_j,
    token from j: c -> c+e_k,
    token from k: c -> c+e_i.                            (6.2)

Commit the macro boundary permutation and (5.2). Each nonzero spatial move is exactly one signed native-axis step. This is the inward-through-anchor realization, different from the source's outward midpoints c+e_i+e_j, but with the identical boundary token permutation. Both paths are separately typed; we do not claim that one is the unchanged other.

The common Cell makes the label exchange local in space. It does not certify primitive force legality, a physical signal/controller implementation, or bounded physical action per primitive force event. The arithmetic load exchange can move more than one label quantum; refinement into elementary physical exchanges remains an obligation.

**Source-role memory is necessary.** At the midpoint, swapping which of two active tokens came from two source slots leaves all current token positions and all carried labels unchanged. The next destination assignment differs. Therefore the midpoint position/label observer does not determine the next state unless the source-slot role mapping is retained. This is an executed BRC fiber counterexample; co-location is not a safe erasure of provenance.

Theorem 3 now applies with N=6, W=8. For arbitrary initial integer six-component labels, global componentwise balance occurs within 4(Phi(0)-Phi_min) macro-events, or 8(Phi(0)-Phi_min) native moving ticks. The charges then stay fixed on identities, while paths/controller continue their recurrent motion. This is not global quiescence or a uniform physical velocity state.

For (4.2), the first four exchanges are neutral; the fifth encounters 0,1,2 together and replaces them by 1,1,1. At macro-event five/native tick ten:

    (0,1,1,2,1,1) -> (1,1,1,1,1,1), Phi:8->6.          (6.3)

The old 24-frame schedule leaves the same loads unchanged forever.

## 7. Exact local joint-flux and loss accounts

For token alpha let its carried vector be q_alpha and its current/next Cells be x_alpha,x'_alpha. Define the local carried density Q_a(z)=sum_{x_alpha=z}q_{alpha,a}. All changes of q take place at c and have zero sum there.

For an actual native movement z->z+sigma e_j, define

    J^sigma_{a;j}(z)=sum of post-exchange q_{alpha,a}
                      on exactly those moved tokens.  (7.1)

Then, using the actual incidence of each finite edge,

    Q'_a(z)-Q_a(z)=sum_{j,sigma}
       [J^sigma_{a;j}(z-sigma e_j)-J^sigma_{a;j}(z)].     (7.2)

There is no carried-quantity source. Post-exchange values are used because exchange precedes second-tick scattering. The vanishing local exchange source is checked at the common Cell, not inferred merely from a global sum.

Define e(z)=sum_{x_alpha=z}||q_alpha||^2 and define the analogous edge flux using post-exchange squared labels. At an exchange tick,

    e'(z)-e(z)=incoming quadratic flux-outgoing flux
                         -d_event * 1_{z=c}.            (7.3)

The loss is exactly (2.3), summed over components. It is computed from the actual specified exchange; it is not tuned to cancel a target trajectory. Nevertheless (7.3) is a mathematical loss account, not total physical-energy conservation. An identification with kinetic energy would require an independently specified destination of that energy or a valid coarse-observer derivation. This note adds no such reservoir by definition.

## 8. Residues and why exact equal mean is generally wrong

For the full population, (3.1) gives the exact identity

    N Phi_min - sum_a S_a^2 = sum_a r_a(N-r_a).          (8.1)

If any S_a is not divisible by N, the best integer state has a nonzero remainder spread. A statement that all N labels become S/N in the same unchanged integer state space is false. Changing precision, replacing individuals by a mean observer, or retaining a quotient/remainder structure has different semantics.

For N=6 and total S=1 in one component, the minimum is one label1 and five labels0, with square sum1, not six labels1/6 with square sum1/6. The latter is a valid rational readout but not an executed integer terminal state.

## 9. Conservative counter-control: loss is not forced by discreteness

For a scalar triple x with total S divisible by three, define

    C(x)_i=2(S/3)-x_i.                                 (9.1)

For other totals leave x unchanged. This is an integer, participant-equivariant involution, preserving S and the full square sum. It can be used coordinatewise at the same common-Cell exchange site, without changing the spatial route or adding an external input.

Example:

    (0,3,3) -> (4,1,1),    total6, square sum18.          (9.2)

A component maximum can increase while the exact finite quadratic total is unchanged. Applying (9.1) again restores the original triple. No unbounded growth or instability claim follows from this single redistribution.

Thus the chosen dissipative R and conservative C are different constitutive choices compatible with these algebraic/transport constraints. Neither their existence nor the absence of continuum assumptions determines which, if either, has native physical meaning. Local three-participant exchange also does not guarantee three nonzero primitive force terms: some participants or components may be unchanged. TRIADIC_CLOSURE_E remains a separate semantic and dynamical obligation.

## 10. Executed evidence and remaining boundary

The included standard-library checker executed:

* 2,197 signed scalar triples, with independent forward enumeration of all square minima, remainder identity, even losses and conservative involutions;
* 512 candidate integer sum-conserving 3x3 matrices under unit/pair contraction tests, leaving exactly six permutations (finite regression for Theorem 1, not its universal proof);
* all six fair 24-frame updates and the disclosed 36 two-update controller search;
* all 48 selected frame/bit starts, complete eight-window coverage and the ten-block pair design;
* all 15,625 scalar six-token states in [-2,2]^6, 55,968 executed exchanges, 39,752 positive-loss events, and the bound (3.2); maximum observed time to balance was twelve macro-events;
* 48 vector-valued microstep runs, 986 executed ticks and 2,958 moving native edges, checking the exact local quantity flux and quadratic-loss equations; the longest tested vector run settled by tick30;
* 2,160 comparisons under all 720 transported S6 coordinate permutations, and a midpoint role-erasure failure;
* (6.3), including its sole quadratic loss of two at native tick10 at c.

Finite checks supplement the finite/algebraic proofs. They do not establish physical validity, uniformity under growing population or changed resolution, historical novelty, independent review, or Lean verification. A clean-directory rerun and content hashes accompany the release.

The substantive next gap is not another numerical growth test: specify what carried labels mean physically, how admissible native ternary events exchange them and supply/update the routing state, and how any quadratic loss relates to a full energy or observer budget. This packet makes those obligations explicit while providing a complete integer/path test interface rather than assigning them an unproved answer.
