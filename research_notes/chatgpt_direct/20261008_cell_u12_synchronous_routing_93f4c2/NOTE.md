# U12 — common-clock rendezvous before a sourced triadic binding event

Event: EM-20261008-CELL-U12-SYNCHRONOUS-ROUTING-93F4C2
Status: CONDITIONAL_ROUTING_AND_COINCIDENCE_THEOREMS / ACTUAL_TYPED_BRC / UNREVIEWED / NOT_NATIVE_FORCE
Global read snapshot: awdawmip/chatgpt-global-knowledge@552f8bb63a7205e55f6878f3a0573234c2641259.
EM intake: 671bbbb2a46f08f62cad08060adb682d647533d5.
Logical conversation: chatgpt-heartbeat-cell-attraction-20261006-8b74f0 (not platform attestation).
Research-Activity-ID: null. Prior platform-blocked session registration remains pending. No blocked registration request was repeated or rerouted this turn; no old session/role was used. Research-note persistence is not activity registration or formal Result admission. No current-session pre-final was invoked without registration.

## 0. Exact advance and source boundary

Consume U11@58fb61830110c9cec0508fb32c355742e04fd818: a finite identified resource can be reserved, moved and bound to a material path prefix, but resource bookkeeping is not reaction. Consume U9's source-to-meeting paths and U10's clock/readout distinction. Do not rerun their full suites or describe their earlier no-go results as new.

The new question is whether the source-labelled inputs of a proposed equal-canonical-frame event can actually reach one Cell in the same declared clock stage, with distinct required arrival axes. An overlap summed independently over every source's path depth did not impose that requirement.

NEW MODEL ASSUMPTIONS: a common integer protocol clock; each signal either traverses one native edge or, if explicitly allowed, holds at its current Cell; the proposed arrival-direction readout is the FINAL transport edge; this test requires fresh arrivals at the event tick. These assumptions are not forced by BRC, P000, or a calibrated physical clock. Persistent stored actions, a different force/transport direction map, or asynchronous source epochs change the test. Even a positive equal-quantum three-axis routing result is NOT a native TRIADIC_CLOSURE_E certificate. The current native occurrence, context, action-incidence and F_E/reaction maps are still required.

P000, all six native spatial axes and twelve directed neighbors, separate time, the raw-chart/final-address distinction and protected worldview remain unchanged. Holds are not a thirteenth spatial direction. A direction detour is a composite native path, never a new primitive diagonal. No square shell or prime/composite label is used.

Current authority was refreshed by immutable compares: 00_BOOTSTRAP.md, OPERATING_MANUAL.md, project Task router, P000 and BRC-only contracts were unchanged and reused; current worldview, native world/residual contracts and the exact TEST_ONLY triad note were read. The triad note explicitly forbids treating three distinct axis labels alone as native evidence. A bounded current search returning no matches is not a repository-wide nonexistence claim.

## 1. A common-clock parity invariant

Use the affine X6 graph, in a chosen raw chart. Write chi(x)=sum_j x_j mod2. Every spatial edge toggles chi. A signal starting at x_i at integer epoch tau_i, moving on EVERY subsequent tick, has at global tick t

    chi(z_i(t)) = chi(x_i) + t - tau_i mod2.                (1)

Therefore any common-Cell simultaneous rendezvous necessarily has equal values chi(x_i)-tau_i mod2 for all inputs. This is also sufficient for eventual unconstrained rendezvous on Z6: choose a common Cell z and a sufficiently late t with the compatible parity; each distance |z-x_i|_1 is at most t-tau_i and has the same parity. Follow a shortest native word and add backtracks to reach precisely that length. No external Euclidean angle is used.

In particular, simultaneous moving-only emissions from neighboring Cells can NEVER meet at one common later tick. Their independent static spatial overlap can be strictly positive nonetheless. Under a chart translation every chi changes by the same bit, leaving the condition invariant.

With w_i(t) explicitly recorded holds, the equation becomes

    chi(z_i(t)) = chi(x_i) + t - tau_i - w_i(t) mod2.       (2)

Hence source epoch and holding history are not optional when testing a same-time event. For neighboring sources, one relative epoch offset or an odd difference in hold counts removes this specific parity obstruction. This is not proof of a physically allowed delay operation.

Example without holds: from 0 emit (+E2,+E1) at epoch0; from E1 emit (+E2) at epoch1. Both have fresh distinct-axis arrivals at E1+E2 at global tick2. The equal-epoch version has no simultaneous rendezvous at any tick.

## 2. Static overlap versus the diagonal of a common clock

U8's spatial observer was

    G(r)=sum_n lambda^n A^n(0,r),
    K(r)=sum_z G(z)G(z-r)
        =sum_n (n+1) lambda^n A^n(0,r).

The factor n+1 records ALL split positions of a combined path: its two source paths may have DIFFERENT lengths. That formula and its previous proofs remain valid. It is not automatically a simultaneous-action observer.

For a moving-only common-clock pair the correct coincidence family is

    H_0(r)=sum_t sum_z lambda^t A^t(0,z) lambda^t A^t(r,z)
          =sum_t lambda^(2t) A^(2t)(0,r).                 (3)

Reverse the second source word and concatenate it to the first. There is one split, at the midpoint, not 2t+1 alternatives. The bijection preserves count, total and dominant weight. Thus H_0(r)=0 for odd chi(r), while K(r)>0 for every r. Also sum_r H_0(r)=1/[1-(12lambda)^2]. No signed-mass transform or trigonometric computation is needed.

Explicitly allow a hold of weight eta>=0 and native edges of weight lambda>0, with s=eta+12lambda<1. Let B=eta I+lambda A and p_t(x,z)=B^t(x,z). B is notation for the ACTUAL positive word grammar, not an ordinary matrix propagator substituted for BRC. The same midpoint bijection, including ordered holds, gives

    H_eta(r)=sum_t B^(2t)(0,r),
    sum_r H_eta(r)=1/(1-s^2),
    0<=H_eta(r)-sum_(t=0)^h B^(2t)(0,r)
          <= s^(2h+2)/(1-s^2).                           (4)

For eta>0 every H_eta(r)>0: use a shortest word with suitably placed holds to obtain an even total length. Waiting is a genuine new operation/weight, not a passive relabelling of U8's kernel.

At lambda=1/48: the whole-space H_0 sum is16/15, while at eta=1/48 the H_eta sum is2304/2135. The executed neighbor interval at h=12 is approximately[0.0008945792535557413,0.0008945792535576616]. These are positive family readouts, not physical probabilities or forces.

## 3. Consequence for the original four-unit preparation

For X=(0,E1,E1+E2,E2), the source parity classes are {0,E1+E2} and {E1,E2}. If one tries to lift U8's tree construction using simultaneous moving-only pair factors H_0, every spanning tree includes an edge across these classes and hence has zero weight. The ENTIRE resulting four-unit score is exactly0 at all depths, not a small truncation artifact.

This does NOT falsify U8, prove that squares cannot form, or establish a native forbidden shape. It falsifies the specific identification of its independent-depth overlap with this synchronous moving-only event model.

With the explicit eta=1/48 holding operation the pairwise-clock tree score becomes positive; the executed all-tail interval is approximately[1.1444225451193112e-8,1.1444225451266827e-8]. Distinct tree edges here can still use DIFFERENT event times t_e. A product of pairwise synchronized factors is NOT one global simultaneous N-body event. Native action occurrences must not be independently reused in multiple pair factors.

## 4. A genuine joint space-time population and its finite normalizer

For N source identities, define a single common event-time/common-Cell population

    J_N(X)=sum_(t>=0) sum_z product_i p_t(x_i,z).          (5)

For unrestricted source positions with x_1=0,

    sum_(x_2,...,x_N) J_N(X)=sum_t s^(Nt)=1/(1-s^N).     (6)

Proof: choose N ordered timed words, each of length t. The first word from0 determines z. For i>1 its word uniquely determines x_i=z-displacement(word_i). Conversely every common rendezvous has exactly these words and sources. Their positive joint weight sums to s^(Nt). Alternatively sum source positions one at a time using translation invariance. No preferred physical anchor is introduced.

Source exclusion and any valid additional event gate can only decrease this sum. Nonemptiness must still be demonstrated. If diameter(X)>2h, its common rendezvous needs t>h, so the unnormalized mass of these configurations is at most s^[N(h+1)]/(1-s^N). A probability tail requires division by a verified POSITIVE excluded/gated normalizer; no upper denominator is substituted.

For a FRESH three-axis routing gate, use incoming p_1,p_2,p_3 with pairwise distinct axes and multiply the three LAST native edge weights, retaining source occurrence identity and the same event clock/Cell. Its permissive ordered signed port set has12*10*8=960 members. This does NOT claim960 legal native action incidences. More generally an actual certified subset can replace the test set.

Before source exclusion, the exact all-relative fresh-candidate sum at time t>=1 is

    960 lambda^3 s^[3(t-1)].

All prefixes have length t-1 and are unconstrained timed words; the anchored-coordinate reconstruction is again one-to-one. Consequently the all-time total is

    960 lambda^3/(1-s^3),                               (7)

and its time>h tail is960 lambda^3 s^(3h)/(1-s^3). The t=1 candidate sources are all distinct, so they supply a positive excluded lower bound960lambda^3. For eta=lambda=1/48 the unrestricted upper is192/21679 and that lower is5/576. These are preparation-population measures, not repeated firings of the same quantum. Event-time-labelled terminated histories are alternatives, not instructions to reuse an input occurrence after firing.

This provides a positive common-clock, whole-event carrier without confusing independent pair matches with one compatible event. It does not determine native force, material successor dynamics or stationary physical matter.

## 5. Exact triple check on three original square corners

Emit from(0,E1,E2) at the same epoch. Moving-only coincidence and routing-gated coincidence are both zero for every t by(1). With eta=lambda=1/48, complete finite BRC populations give:

    tick1: co-location count1; fresh distinct-axis count0;
    tick2: co-location count236; fresh distinct-axis count32;
    tick3: co-location count115092; fresh distinct-axis count29328.

At tick1 the source at0 holds while the other two arrive. It is a three-source co-location, not three fresh arrivals. Accepting a stored input is a DIFFERENT event semantics and must be declared. At tick2 the32 candidates have exact total weight32/48^6=1/382205952. Their weight is not an event probability; no normalization or first-hit law is inferred.

The computation uses three independent input families only at the explicitly independent preparation, and then joins them by the COMMON clock, COMMON Cell and joint incoming-port gate. The joined object is not replaced by independent marginals for a later query. Positive products and alternative merging call the unchanged BRC.

## 6. A minimal three-source route for one original-square prefix

Choose the original square's leaf actor A at x=0, moving outward to y=x+E3. A record resource R is explicitly free and ready at x. A separate support resource C is explicitly present at y-E5; it is NOT drawn from an unspecified global field or created as a negative sum.

Use the following common three-tick schedule:

    A: HOLD, HOLD, +E3;
    R: -E4, +E3, +E4;
    C: HOLD, HOLD, +E5.

All arrive at y at tick3, with fresh last ports+E3,+E4,+E5. The record route is a native detour, not a diagonal step. A and R have the same initial Cell but different identities and roles; this is not two material actors occupying one Cell. C has its own prepared inventory and its changed location is retained.

The gate checks three distinct source occurrences, equal DECLARED positive candidate quanta, same clock, same Cell and different arrival axes. It ALWAYS returns native_closure_certified=false and requires the genuine native action/context and successor/reaction interface. A caller-provided label does not upgrade it.

Directly carrying A and R along the same one-edge route to y instead gives identical arrival axes. Thus merely adding a third participant does not satisfy this particular canonical-frame/last-edge gate. A different force/transport direction map could change that result, but must be supplied rather than presumed.

**Sharp routing cost under these assumptions.** A path from x to y=x+E_j with final port+/-E_k, k!=j, must first reach y-/+E_k. Its graph distance from x is2. Hence it needs at least3 spatial hops. Material delivery needs at least1, and the specified neighboring third-source delivery needs at least1. Total hop count is at least5; the schedule attains5. With at most one hop per tick it requires at least3 ticks; the parallel schedule attains3. Four holds occur in total. No statement about physical time, minimal energy, or all possible native implementations is made.

All120 ordered signed distinct-axis choices(j,k) were checked. For a fixed outward direction, enumerating every native word of lengths1..3 gives0,0,20 candidates ending at y along another axis; our chosen detour avoids y until its final arrival. The minimum bound itself is a proof, not extrapolation.

The implemented trace retains original record-resource IDs in disjoint free/held/bound partitions at EVERY delivery tick. Existing bound paths and remote meeting Cells remain unchanged. At tick3 the material is at y while the old path head is still at x: the pending head mismatch is explicitly present, not falsely reported as a committed U11 state. The new record R and support C remain reserved. A CONDITIONAL data output shows the inherited U9 prefix(-E3)gamma and assigns R to it; native firing is not performed. C is held at y and cannot be reset to its old source or reissued without a declared release. This is source-accounted preparation, not a completed mechanical reaction.

Missing third source, duplicate source IDs, different clocks, holds mistaken for fresh incoming edges, and same-axis co-carry are all rejected by the applicable routing checks. Old U11 finite-inventory effects remain applicable; adding C is an explicit additional resource input, not an unchanged total B or a free catalyst.

## 7. Exact execution and limits

Final new checker:18498 assertions. Actual unchanged BRC calls: edge3121, propagate99436, recoalesce81723, recurrent15. Coverage:three parameters; complete endpoint layers through4 ticks;72 direct pair-join/midpoint checks; all timed single words through3 ticks; complete one-tick joint cohorts forN2/3; geometric all-clock closures forN2..4; all16 square trees; nested infinite pair intervals through horizon12; two three-source preparations through3 ticks; explicit source/clock failure cases; all120 signed detour cases and all native words through length3 for one final-point gate; per-phase resource partitions and one epoch-offset witness. Counts are implementation assertions, not independent experiments.

No first-firing process, repeated autonomous triadic reaction, complete force-to-motion map, physical clock or prime criterion was implemented. Infinite parity, midpoint, joint-normalizer, tail and minimal-route claims are proved above, not inferred from finite observations. No prior U1-U11 full suite was rerun and counted as new work.

Pinned dependency chain: resource_lift.py0a7e0890eb08dc722d2e85fb3ad1a7b2d6b29621 -> local_latent.py67408af5b977bed7295f7225cdd3f550c41b9729 -> connected_retention.py569e6171d0052fbfd41cf007b09a8327b339228b -> packet_router.py7465f5aa16cbb8fba61ba4be80f8a6884b879c53 -> brc_weighted.py3f205696709e847909958a153f8fe10d3f6b70f0. All mounted source bytes were checked. The inherited loader only removes its two unused imports; no old scientific function was changed. Wait events, clock-indexed composition and routing joins are the explicitly proved new BRC interface.

A development check found that an exact zero endpoint must use CWM_ZERO rather than cwm_edge(0), which only accepts positive edges; this was fixed before final runs. Source-to-resource ID and pending-head records were made explicit before delivery. These are implementation corrections, not structural residuals. Same-author isolated replay is reported only after actually running it. It is not independent review.

Prior art: Aldous and Fill, Reversible Markov Chains and Random Walks on Graphs, author-hosted HTML section3.2, especially bipartite periodicity and the directed-edge state. Page read at https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch3.S2.html . Only this section was used for general attribution; the finite-graph text is not substituted for our infinite-lattice proofs. No claim of inventing parity, Green functions, synchronous products or graph rendezvous is made. The blocked dedicated provider/registration paths from previous turns were not retried, disguised, or counted as completed queries.

## 8. Smallest unfinished scientific unit

Given the explicit event-ready three-source trace, provide one SOURCE-JUSTIFIED native action-incidence certificate and its F_E(state,event,boundary) output, including the fate/reaction of C and the previously unmatched path head. Alternatively specify and test a persistent-action rather than fresh-arrival readout, retaining arrival age and one-use occurrence ownership. Do not infer native force from the port checklist, three participants, or endpoint arithmetic. Do not rerun U7 spreading or U11 inventory counts. The new deliverable is the shared-clock/source-aware preparation interface and its precise necessary conditions; unique integer landing and the original prime hypothesis remain open.
