# U10 — finite communication and the work-clock correction

Event: EM-20261008-CELL-U10-WORK-CLOCK-6D31B8
Status: CONDITIONAL_REPRESENTATION_AND_OBSERVER_RESULTS / UNREVIEWED / NOT_NATIVE_FORCE
Global read: awdawmip/chatgpt-global-knowledge@8de6086e90d954b05672cbee20a5da5eb86bb741.
EM intake: 1c1d4c19b0cfa5ab9b22cb0aae3fbfa93fefacf0.
Logical conversation: chatgpt-heartbeat-cell-attraction-20261006-8b74f0 (not platform-attested).
Current registration: PLATFORM_BLOCKED. The actual session_start request session-20261008-cell-u10-6d31b8 was blocked before an Issue/receipt was produced. No new RA/session/Researcher authority is claimed, no old session is borrowed, and no alternative registration transport is attempted. This artifact preserves user-authorized portable research; it is not a formal Task/Result or activity-registration substitute.

## 0. Exact advance

Consume U9@83168d758dd0d75090fee72587458609ca05f356, directory research_notes/chatgpt_direct/20261008_cell_u9_local_latent_4b7e62. It represents the U8 finite relative distribution using a spanning tree and two ordered source-to-meeting paths per link. Its weight is m(s)=lambda^L(s), 0<lambda<1/12. The U9 completion-step kernel preserves m/Z; it did not establish a finite-speed physical implementation.

This unit establishes a specific communication lower bound, executes an occurrence-local equality/acknowledgement protocol, and derives the change of the invariant observation when work between completions takes state-dependent duration. It also implements a clock-corrected acceptance rule, an exact two-position finite phase certificate, a full-shape marked-path observer and exponential resource-tail certificates. It does NOT solve the missing native action/reaction bridge.

P000 and six-dimensional X6 are unchanged. Raw signed coordinates, twelve ports, path graph distance, record length, work ticks, normalized trial mass and native force are distinct types. There is no squared-number shell, primitive diagonal force, physical-time calibration, or interpretation of three tree labels as TRIADIC_CLOSURE_E. The current source definition P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, blob f95fd7a935ce16c875ac2756b299dfe2b7d9c8e5, still requires an actual legal three-action event; it supplies neither the protocol below nor a clock law for it.

## 1. An explicit locality obstruction, not a universal ban on caching

Assume an **uncached occurrence-local encoding**: each word symbol is stored at the Cell visited just before its edge, with stable predecessor/successor occurrence IDs. End sentinels are explicit. A local head may know the actors, tree, path lengths and meetings, but does not contain a verified digest or equality certificate for an entire remote word. Information traverses at most one native edge per communication tick; this finite-speed communication assumption is new and conditional, not a speed-of-light assertion from P000.

Use the original four actor positions (0,e1,e1+e2,e2), tree {01,12,23}. Fix R>=0 and h=R+2. At actor1's Cell b=e1 define closed words

    w+ = (+e3)^h (+e4,-e4) (-e3)^h,
    w- = (+e3)^h (-e4,+e4) (-e3)^h.

For state P put the word w+ on the actor1 leg of BOTH links 01 and 12. For Q change only the actor1 leg of link12 to w-. Other legs are: 01 from actor0 is +e1; 12 from actor2 is -e2; 23 from actor2 is -e1 and from actor3 is empty. The first two meetings are b, the third is actor3's Cell. Every path is valid; both states have L=4h+7, identical actors/tree/meetings/individual lengths/weight.

All occurrence records inside distance R of b are byte-equivalent in the declared encoding. The first changed record lies at distance h: the two-letter excursion reverses its order there, and the two words rejoin at the same indexed suffix. Pointer identifiers themselves do not encode remote content.

Nevertheless U9 slide(0,1,2) is eligible in P and ineligible in Q, since it requires the two actor1 words to be identical. By induction on communication ticks, the local state at b after t ticks depends only on the initial t-neighborhood and corresponding random bits. Coupling the same random bits gives identical local output laws for t<h. Thus an exact uncached local eligibility decision cannot have a uniform fixed number of ticks for all allowed path states. This proves a necessary read/communication boundary for this encoding; it does NOT say every implementation must rescan every trail. A pre-established immutable shared handle or verified equality cache changes the input and may make a later query cheap, but its construction and invalidation must be counted separately.

## 2. An executed finite protocol for the equality suboperation

Freeze the two word versions. Two co-located cursors read the next symbols and, while equal, traverse the same native edge. On a mismatch or common end, record the Boolean result. An acknowledgement token then retraces the matched prefix to the initiating Cell. A forward read/hop occupies one declared tick, the decision one tick, and each return edge one tick.

If k edges were matched, this protocol uses exactly

    c_compare = 2k+1 <= 2 min(lengths)+1.

For the above P: k=2h+2 and c_compare=4h+5. For Q: k=h and c_compare=2h+1. This is a conservative finite protocol, not an optimal communication claim. Each hop is an actual signed native edge; there is no path shortcut. The implementation executes these records with unchanged positive BRC composition, unit trace weights, and separate comparison outputs.

Only equality/acknowledgement is implemented. Execution is a trace simulator over a prepared immutable slot map; constructing that map is setup, not a proved local distributed preprocessing algorithm. A complete distributed compiler still has to handle version locking, concurrent updates, resource ownership, remote endpoint notifications and commit visibility. A single quiescent readback is not an instantaneous distributed commit. The Boolean protocol neither creates a third primitive action nor supplies a mechanical reaction.

## 3. Completion frequency and work-time occupation are different observers

Let Q be a completion-step kernel on a countable state space with invariant probability pi(s). Suppose a serial implementation holds the **last committed state** fixed for an integer c(s)>=1 work ticks before making one Q transition. c is a declared computational duration, not physical time. Assume H=sum_s pi(s)c(s)<infinity.

Expand each s into phases (s,0),...,(s,c(s)-1). The transitions inside the phase chain are deterministic; from its last phase draw the next completed state from Q and enter phase zero. Direct incoming-flow calculation proves

    nu(s,k)=pi(s)/H,
    pi_work(s)=sum_k nu(s,k)=pi(s)c(s)/H.                 (1)

For a phase k>0 its unique incoming phase has the same mass. For k=0, the incoming mass is sum_t pi(t)Q(t,s)/H=pi(s)/H. This is an invariant TOTAL observer; CWM branch counts need not be stationary.

More generally, for outcome/label-dependent transaction lengths d(s,e), replace c(s) by the mean h(s)=sum_e p(e|s)d(s,e), provided the corresponding transaction kernel is stationary and its mean length finite. A marked-phase invariant assigns pi(s)p(e|s)/H to each of its d(s,e) phases. This is an analytical expansion, not a device that reveals the future outcome before verification. If material actually occupies new intermediate positions during execution, the last-committed-state readout is not the physical intermediate-position readout, and (1) does not justify ignoring those extra positions.

For U9, pi(s)=lambda^L/Z. At fixed material configuration X the new marginal is

    pi_work(X) = W_N(X) E_pi[c(s)|X] / (Z H).            (2)

Only if the conditional mean work is independent of X is the stationary position marginal unchanged. A constant slowdown is harmless to this marginal; a configuration-dependent slowdown generally is not.

The conditional serial audit profile c(s)=2L(s)+1 is especially explicit:

    pi_work(X) = [W_N(X)+2 lambda dW_N(X)/dlambda]
                 /[Z+2 lambda dZ/dlambda].             (3)

Termwise differentiation is justified below by a strictly subcritical positive exponential moment. The derivative denotes a marked-path observer, not numerical differentiation, a physical energy, or permission to use a non-BRC propagator. This audit profile is a chosen cost test, not a proved cost formula for every U9 transaction.

## 4. Exact finite example using an actual four-actor U9 inverse pair

Let s0 be U9's tree {01,12,23}, each link meeting at its higher-index actor. Its three one-edge legs give L0=3. Let s1 be the valid U9 grow move of actor0 by +e3, prepending -e3 to its incident leg; L1=4. Its inverse is the -e3 shrink. These are different labelled material configurations, not merely different internal annotations.

For this finite test restrict proposals to this reversible pair, with the ordinary U9 Barker acceptance. This two-state test is NOT the entire U9 four-channel kernel. At lambda=1/48,

    Q(0,1)=1/49, Q(1,0)=48/49;
    pi_completion(1)=1/49.

Take the specified serial audit costs c0=7,c1=9. The complete phase chain has sixteen states. Its invariant work-clock observation is

    pi_work(1) = 9/(7*48+9) = 3/115,
    TV(pi_completion,pi_work)=3/115-1/49=32/5635.         (4)

Both invariant measures and every phase balance are checked with positive BRC propagation. This difference is not arithmetic error and cannot be removed by labelling a whole transaction as one physical heartbeat.

## 5. A precise correction, and its preconditions

If the desired **work-clock** marginal is the original pi and c(s) is a fixed positive state cost, target m(s)/c(s) at completion times. For symmetric proposal labels use

    alpha_c(s,s') = m(s') c(s) / [m(s)c(s')+m(s')c(s)].   (5)

Detailed balance holds for m/c; multiplying its completion invariant by c restores m after phase aggregation. This is an actual change of acceptance law, not a passive clock relabelling. It assumes c is known or certified and does not change implicitly when acceptance is changed. If real expected work depends on the new accepted outcome, one must first solve the cost/acceptance consistency problem; plugging in an old duration is not justified.

The implementation uses only nonnegative BRC powers and positive factors c_old,c_new. In the example,

    alpha_c(0,1)=7/439, alpha_c(1,0)=432/439;
    pi_corrected_completion(1)=7/439;
    pi_corrected_work(1)=1/49.                            (6)

This gives an exactly tested correction interface. It does not derive a natural clock or select one unique physical kinetics.

## 6. Full-shape effect and an actual marked-path extension

For a positive path family keep (A,J), where A is its ordinary CWM value and J marks one of its edge occurrences. Alternative sums act componentwise and serial composition is

    (A,J)*(B,K)=(A*B, J*B + A*K).                       (7)

Each marked history has its source, word and marker position; an A-history of length n contributes n marked alternatives. For an overlap link the length-n family has n+1 split positions, so its marker observer has n(n+1) copies of the endpoint family. Formula (7) chooses the marker in one serial factor. It is applied using the unchanged BRC serial/recoalesce functions; no numerical derivative is computed.

For a finite link prefix D and a=D+1, rho=12lambda, its omitted marked TOTAL is bounded by

    rho^a [a(a+1)/(1-rho)
      +(2a+1)rho/(1-rho)^2+rho(1+rho)/(1-rho)^3].        (8)

This follows from n=a+k and positive geometric moment identities. Together with U8's ordinary tail bound, all tree products/sums give certified intervals for 1+2 E[L|X]. At lambda=1/48, link depth20 (not a dynamics cutoff), the full infinite-model conditional work intervals are:

    original square221: [7.603064510527248...,7.603064550876995...]
    four chain:        [7.611779171346740...,7.611779250482774...]
    four star:         [8.016461640417726...,8.016461706622510...].

These intervals are disjoint, so the full U9 shape marginal—not just the two-state diagnostic—changes under this declared work profile. The values are work counts, not native time, stability scores or shape-class probabilities. All rational bounds are in results.json; decimals here are only display approximations. The comparison covers these labelled configurations, not a global optimum over shapes.

## 7. Finite expected work without a false hard resource cap

For rational t>1 with 12t lambda<1, U9's positive expansion and the unrestricted tree/leg sum imply

    E_pi[t^L]=Z(t lambda)/Z(lambda)
      <= t_N(1-12t lambda)^(-2(N-1))/Z_lower.           (9)

Thus all polynomial moments of L are finite. A serial comparator costing at most 2L+1 has finite expected work under that stationary law. More generally an implementation whose mean work is bounded by a polynomial in L (and geometric edit indices with suitable finite moments) has a finite work-time normalization. Polynomial reweighting preserves exponential record/diameter tails. This is a sufficient integrability result, not a full distributed scheduling proof.

For N=4, lambda=1/48, t=2, consume U9's verified fixed-square counts 32,192,6624 at lengths3,4,5. They give

    Z_lower=311/884736,
    Z_work_lower=2333/884736,
    Z_unrestricted(2lambda)=1024,
    sum (2L+1)(2lambda)^L <=13312.

The exact whole-space stationary tail bounds at B=64 are

    pi(L>64) <=27/341948116238336 <7.896e-14,
    pi_work(L>64) <=351/2565160627601408 <1.369e-13.     (10)

These are NOT obtained by enumerating states up to64 or imposing a hard wall. A snapshot conditioned on L<=B differs from its original law in TV exactly by the omitted tail. This does not bound every future path under a permanently capped dynamics; its exit/long-time effect needs a separate argument. Small stationary tails do not prove a conserved physical inventory or that long trails never occur.

An unqualified finite per-state work assertion is too weak: c(s) approximately lambda^(-L) would cancel the summable weight and produce an infinite work normalization. The timing/representation hypothesis is mathematically substantive.

## 8. Execution, source attribution and exact continuation

Unchanged dependency chain: local_latent.py blob67408af5b977bed7295f7225cdd3f550c41b9729 -> connected_retention.py blob569e6171d0052fbfd41cf007b09a8327b339228b -> packet_router.py blob7465f5aa16cbb8fba61ba4be80f8a6884b879c53 -> brc_weighted.py blob3f205696709e847909958a153f8fe10d3f6b70f0. Actual mounted U9 package bytes were verified before reuse. No existing scientific function was changed; the inherited two-unused-import adapter remains unchanged.

Final checker: 2000 assertions; actual BRC edge521/propagate11933/recoalesce102553/recurrent6. Scope:34 admissible locality inputs for R0..16 and their actual equality-return traces; eight complete16-phase examples at four parameters, each with41 finite tick observations; three additional general phase chains; three full-shape first-moment calculations and all-tail bounds; five capacity-tail bounds. All-parameter locality, renewal and exponential-moment claims are proved above, not inferred from these finite examples. Earlier U1-U9 full suites were not rerun or counted as new research.

Development checks caught an overoptimistic loose tail tolerance, an undefined module alias, and a guessed square/chain ordering. The final bound uses the exact weighted denominator and the verified ordering. These were corrected test/implementation expectations, not structural residuals. Same-author isolated replay is recorded separately only after execution. No independent review, formal Result, mathematical admission or complete native runtime guard is claimed.

General renewal/work-occupation methods and locality-by-indistinguishability have prior art. Public primary sources checked: Robert Gallager, MIT 6.262 Lecture12 page (renewal-reward/time averages); Peter Glynn and Peter Haas, On Functional Central Limit Theorems for Semi-Markov and Related Processes, author page (2004 abstract); Birk/Keidar/Liss/Schuster/Wolff, Veracity Radius, author abstract returned by search (direct fetch failed). Only those stated scopes were read, not full papers. Model-specific equalities and lower bounds above are self-contained. The earlier blocked dedicated provider request was not retried or recast as successful evidence.

The smallest next scientific issue is a sourced native event implementation of one path-record update, including resource transfer, third-action provenance, reaction and a measured/declared clock. The present work shows where a fixed-cost equality oracle and an unchanged stationary marginal would fail. It offers a correct conditional clock interface, not a native dynamics claim. The previous U9 pre-final Issue3032 was read in this turn and is FAILED/RuntimeAuthorizationError, not still queued or passed. There is no current U10 registered session for a valid pre-final invocation. Registry writing must be retried only under actual platform permission; no old session or new transport may be used to hide this turn's registration block. No prime criterion or unique integer landing has been obtained.
