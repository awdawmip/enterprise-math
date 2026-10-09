# U13 — finite-lived stored arrivals and a single-use first-ready law

Event: EM-20261009-CELL-U13-FIRST-READY-4C8A21
Status: CONDITIONAL_ROUTING_MODEL / ACTUAL_TYPED_BRC / UNREVIEWED / NOT_NATIVE_FORCE
Global read: awdawmip/chatgpt-global-knowledge@9944ec5937a4024fbdad0c6de6d3f0bd6f33e5f0.
EM intake: 2a563624c36515fdf38f93a7b78b62833c93ea6a.
Logical conversation: chatgpt-heartbeat-cell-attraction-20261006-8b74f0 (not platform attestation).
Research-Activity-ID: null. Earlier platform-blocked registration remains unresolved. No blocked request was repeated or rerouted, no historical session borrowed, and no new formal Task/CLAIM/Result or pre-final authority is claimed. These are user-authorized portable research notes, not registration or mathematical admission.

## 0. Exact continuation and declared changes

Consume U12@497b5f10406ca0bf72eab896b9c15018419da7a5: independent-depth spatial overlap is not a common-clock event; the sourced A/R/C preparation has five native transport edges and fresh arrivals can be scheduled at tick3. The previous fresh-arrival gate did not implement stored actions or a first-firing process. Do not redo U1-U12.

The present alternative is a specified routing protocol with one-use occurrences, capture at a common target, a finite residence window, and termination on first readiness or expiry. It implements neither a native TRIADIC_CLOSURE_E relation nor F_E/material reaction. An arrival-direction label persisting in a register is not a proof that a physical action persists. The lifetime, prescribed routes and advance probabilities below are new assumptions, not consequences of P000, the U8 score, or the old response lambda.

Use full native X6 raw charts and twelve ports; protocol ticks are separately typed, not calibrated physical time. A fixed path preparation does not assert a lower-dimensional world. No square shell, primality indicator, external confinement wall or force-as-negative-mass operation is introduced. Current bootstrap/manual, project router, P000, world/residual contracts and BRC-only rules were reused after immutable comparisons showed no changes in those files. The new default-branch changes were not treated as changes to the frozen U12 model.

## 1. A complete one-attempt protocol

Use the same original-four leaf preparation as U12. Its actor A starts at x=0, target y=E3 is vacant relative to the four material actors. The record R starts at x. The separate support C starts at y-E5. They have distinct occurrence IDs and fixed routes

    A: (+E3); R: (-E4,+E3,+E4); C: (+E5).

Each word first reaches y at its last edge, and the three last axes differ. A is a material actor; R and C are distinct auxiliary resources, not additional co-occupying material actors. C is an explicitly prepared extra source, never generated as the negative sum of other inputs.

On each common protocol tick, an unarrived source i independently advances one edge along its specified word with probability a_i, or holds with probability 1-a_i, where 0<a_i<=1. These normalized trial weights are NEW; they are not U12's lambda/eta all-neighbor weighted populations. After arrival, the occurrence is captured at y and ceases transport. Its source, first-arrival tick, route and last-edge label remain. Capture/stay has unit trial weight; this does not assign zero physical storage cost.

An occurrence first arriving at T_i is eligible at integer times T_i through T_i+H inclusive. At a tick, process new arrivals first. If all three have arrived before the oldest expires, emit READY_RESERVED exactly once and reserve those same three IDs for a candidate event. Otherwise, at the earliest arrival time plus H, emit EXPIRED_RETAINED. Neither output fires native force, releases a source, restarts the attempt or deletes its historical state. H=None is the declared infinite-lifetime comparison; H=0 requires fresh simultaneous arrivals. The original pre-firing head mismatch and the missing native successor remain open, not silently committed.

Holding the fixed routes and advance coins on a common probability space gives independent first-arrival variables T_i. For route length ell_i,

    f_i(t)=P(T_i=t)=choose(t-1,ell_i-1) a_i^ell_i (1-a_i)^(t-ell_i), t>=ell_i.

The formula chooses the earlier ell_i-1 advance ticks, with the final tick necessarily an advance. The implemented first-arrival family is built by positive BRC propagation, not by substituting this closed form for a second numerical solver.

## 2. First readiness is a range condition, not an occupation sum

THEOREM. A one-attempt run succeeds exactly when

    max_i T_i - min_i T_i <= H,

and then its first-ready tick is tau=max_i T_i. For infinite lifetime it succeeds with probability1 and E[tau]<=sum_i ell_i/a_i<infinity.

Proof: once first arrival occurs, every stored occurrence remains at y, and the earliest expiry is min T_i+H. New arrivals at that deadline are permitted. All sources are simultaneously eligible precisely when the final one arrives by this deadline. On success there was no earlier all-present state. Each finite route completes almost surely since a_i>0, and max T_i<=sum T_i proves integrability. For finite H, expiry occurs no later than max T_i on failure, so termination is also integrable.

A positive formula for the complete first-ready mass at tick t is

    g_H(t)=SUM_(nonempty I subset {1,2,3})
              PRODUCT_(i in I) f_i(t)
              PRODUCT_(j notin I) SUM_(u=max(1,t-H))^(t-1) f_j(u).       (1)

For infinite H use lower limit1. I is the EXACT set of last-arriving source IDs. Every successful history has one and only one such I; ties do not multiply the event. All products/sums in the checker actually use unchanged BRC serial/recoalescence. Independence is used only in the explicitly independent source preparation; after the age gate, the joined population is not replaced by independent conditioned marginals.

For infinite storage, a nonstopped occupancy observer counts the same reserved triple at every tick after tau. Thus through h it counts max(0,h-tau+1), whereas the one-use first-event observer counts 1{tau<=h}. The infinite occupation sum diverges even though total first-ready probability is1. This is a change of observable, not creation of resources. In the deterministic schedule, readiness first occurs at3 and is visible four times at ticks3..6, but is one event.

## 3. The minimal fixed schedule and the exact random-arrival results

If a_i=1, A and C arrive at1 and R at3. The retained ages at3 are (2,0,2). H=0 or1 fails, and H>=2 succeeds at3. Total spatial work remains five native edges. Four source-ticks are spent CAPTURED, not fresh arrivals and not erased zero-time operations. This is the minimum window for this fixed immediate-launch/no-transport-hold schedule, not for every possible launch strategy: U12 could instead delay A and C to obtain fresh arrivals at3.

Now declare a_1=a_2=a_3=1/2. Exact all-time first-ready probabilities are

    H=0:    1/343
    H=1:    41/1372
    H=2:    849/5488
    H=3:    7463/21952
    H=4:    46087/87808
    H=8:    20639019/22478848
    H=None: 1.

These include termination on missed deadlines and are not probabilities conditioned on success. No force, empirical frequency or prime pattern is inferred from these fractions. With infinite storage the exact mean completion tick is56902/9261, below the simple bound10.

For equal general a and b=1-a, the fresh law has the independent positive identity

    g_0(t)=choose(t-1,2) a^5 b^(3t-5), t>=3;
    P_fresh=a^5 b^4/(1-b^3)^3, 0<a<1.                    (2)

Set t=n+3; choose(n+2,2) counts the decompositions of n into three nonnegative integers. Three positive geometric closures yield (2). At a=1, unequal deterministic route lengths give probability0 separately. Conditional on fresh success the mean tick is3/(1-b^3). These formulas are checked at a=1/2 and1/3 with actual BRC closures.

## 4. Finite state plus recurrent total observer covers all time

For the first-ready question store source progress j_i and, once an arrival has occurred, only the oldest captured age d. Source paths/IDs and fixed end-port labels are in the immutable input. At a new tick, update unarrived progress. If this was the first capture set d=0; otherwise increment d. Check readiness BEFORE deadline expiry. With finite H, pending states have d<H; before any capture use d=None. Infinite lifetime needs only whether any capture has occurred.

All non-self transitions increase total progress, or increase d at unchanged progress. Thus the finite transient graph is acyclic after removing self-loops. The only loops are all-unarrived-hold trials before first capture (or all-active-hold trials with infinite lifetime); their probability ell is strictly less than1. The code invokes one_state_recurrent_cwm on these loops and uses its geometric total closure. It does not run a matrix inverse or truncate time.

If S_x is eventual success mass, q_xy are non-self row weights, and ell_x is the loop mass, then

    S_x=(SUM_(y!=x) q_xy S_y)/(1-ell_x).

For M_x=E_x[tau_terminal * 1_success], counting ticks from x,

    M_x=(S_x+SUM_(y!=x) q_xy M_y)/(1-ell_x).

Failure has the same formulas. The code keeps these as TOTAL observers. A rational recurrent closure re-lifted for observer composition is NOT claimed to be a finite count of the infinitely many raw histories. In contrast, prefixes at each fixed tick retain exact finite count/total/dominant data. All first-hit prefixes through14 ticks agree with (1) in ALL three fields; full first-step equations are checked for every solved transient state.

## 5. Arrival age is necessary; the whole age vector is not always necessary

At tick2 compare two positive-weight preparations of the same sources/routes:

    old: tick1 all three advance; tick2 only R advances;
    new: tick1 only R advances; tick2 all three advance.

Both now have progress (1,2,1), the same actual cells, IDs, paths and remaining R edge. In old, A and C arrived at1, so oldest age is1. In new, they arrived at2, so it is0. Their prefix trial masses are positive but need not be equal; the test compares subsequent laws conditioned on these explicitly prepared states.

With H=2 and a_i=1/2, old has one remaining tick before expiry, whereas new has two. Therefore

    P(ready | old)=1/2;
    P(ready | new)=1-(1/2)^2=3/4.

The binary eventual-ready observations have EXACT TV=1/4. Both histories are actually executed. Current geometry, resource count and direction labels do not suffice for this future question.

Conversely, the maximum stored age and progress vector ARE sufficient for the stated common-window first-ready language. Every old captured age advances identically, new captures start at0, and both readiness and failure depend only on the captured set and its largest age. Equal reduced states have identical next reduced rows, hence identical observations after every future composition by induction. The checker compares this reduction with a full source-specific age-vector automaton for H=0..3.

This is not permission to erase all timestamps universally. Source-specific lifetimes, phase relaxation, age-dependent reaction, individual-age outputs, release or new event candidates can distinguish the omitted data. The input and labelled transition grammar remain available to reconstruct full histories; the reduced state is a scoped observer quotient, not a physical deletion law.

## 6. A complete finite-memory error bound

Couple every H to the same independent arrival histories. The success events are nested and tend to the infinite-window event. For the (1,3,1), a=1/2 preparation, put n=H+1. A failed window has max T_i>n because min T_i>=1. A union bound and positive Bernoulli word counts yield

    1-P_H <= min(1, [3+n+n(n-1)/2]/2^n).                 (3)

The two one-edge paths contribute 2*2^-n. The three-edge path contributes P(Binomial(n,1/2)<=2)=[1+n+n(n-1)/2]/2^n. Formula (3) bounds the WHOLE future loss caused by limiting the stored lifetime, not just a finite simulation tail. At H=32 it is141/2147483648, below6.567e-8. A real finite storage budget or a native decay law still needs its own source and cost; the bound does not select a physical H.

## 7. Actual execution, attribution, and next unit

Final check_u13.py:6247 assertions; actual BRC calls edge28073, propagate96042, recoalesce98059, recurrent116. Twenty-one complete parameter/window combinations, exact all-time self-loop closures and their equations; fixed-time C/W/M first-event checks through14; deterministic age thresholds and one-use refusal; two positive prepared histories; full-age to oldest-age intertwining; and all-time lifetime-loss bounds for H2/4/8/16/32. A same-author isolated process replay reproduced results and compressed trace byte-for-byte. This is not independent review, a native reaction experiment or a rerun of U1-U12 counted as new work.

Unchanged dependency chain: synchronized_events.py4ba3187b38bba59d55eb00974de4f71a6e39938e -> resource_lift.py0a7e0890eb08dc722d2e85fb3ad1a7b2d6b29621 -> local_latent.py67408af5b977bed7295f7225cdd3f550c41b9729 -> connected_retention.py569e6171d0052fbfd41cf007b09a8327b339228b -> packet_router.py7465f5aa16cbb8fba61ba4be80f8a6884b879c53 -> brc_weighted.py3f205696709e847909958a153f8fe10d3f6b70f0. Mounted bytes were checked before execution. Existing scientific function bodies were not changed; the inherited two-unused-import adapter remains unchanged.

Prior art: first-hitting times and finite-time Markov observations are standard. Aldous/Fill, Reversible Markov Chains and Random Walks on Graphs, author-hosted section1.2 was actually read, especially its distinction between first visits and mixing times: https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch1.S2.html . The present protocol/age quotient/exact finite examples are self-contained; no general first-passage-method novelty is claimed. No blocked dedicated provider or registration operation was retried or claimed completed.

Smallest unfinished unit: a source-justified retained-action state law and native event/successor map, specifying whether an old direction tag still corresponds to an eligible action, how age changes its strength or phase, and what happens to C and the unmatched prefix head at firing/expiry. Our READY_RESERVED output gives an exact input and a non-reusable source tuple for that test; it does not supply the native certificate itself. Do not repeat the parity proof, U11 inventory count, or the current first-ready fractions. No unique integer landing, autonomous force-maintained aggregate or prime criterion has been obtained.
