# U15 — sequential calibration, reusable scratch, and retained side information

Event: EM-20261009-CELL-U15-SEQUENTIAL-CLEANUP-9D2F60
Status: CONDITIONAL_LOGICAL_INTERFACE / ACTUAL_TYPED_BRC / UNREVIEWED / NOT_NATIVE_FORCE
Global read: awdawmip/chatgpt-global-knowledge@7b9eb1223c4139523fa4abb0b663fdcbf02e9273.
EM intake: a80c1772a95ed4705bb83e84b6c383aa6b88b71a.
Scientific predecessor: U14@d22e0e640e1713f8772a4dd054c4d6b854a95720.
Logical conversation: chatgpt-heartbeat-cell-attraction-20261006-8b74f0, not platform attestation.
Activity: null. Prior blocked registration is not retried or rerouted; no old session or research role is borrowed. This is authorized portable research-note preservation, not formal task publication, native-event admission or a successful pre-final check.

## 0. Exact advance and assumptions

U14 supplied a reversible relative-offset exchange with two prepared blank registers. It also showed that blindly reusing the resulting nonblank records reintroduces the mismatch. Here we factor that exchange into two three-register logical interactions, explicitly retain common drift between operations, and construct reversible scratch cleanup using the already retained source-arrival records. We prove the exact condition under which such cleanup is possible, check its failure under wrong source association, and compose its duration with U13's finite residence window.

NEW computational assumptions: all involved records are present at the same target Cell; a serial controller executes one of the stated interactions per protocol tick; the three captured source registers drift together by +1 mod k before each interaction; relative scratch and immutable timestamp records do not undergo that drift. The local record access and modular update are the declared unit-work interface, not a measured physical duration or a uniform bit-cost claim for unbounded k. Record delivery, history authentication, concurrency, native interaction rates, and mechanical action/reaction are not supplied.

The source timing witness is valid only for the U14 passive-storage preparation, with initial register zero and no intervening phase-changing interaction. A supplied string, timestamp, or equality of residue values is not external authentication. The main example is taken from an actually executed upstream U14 trace. Other exhaustive finite register inputs are algebraic tests, not claims of naturally occurring states.

Six-dimensional X6, twelve directed neighbors, separate time, P000 and the residual-fidelity contract are unchanged. Three registers in a function are NOT three nonzero primitive forces. Repeated reads of R are NOT repeated firing of the same force occurrence. The material position, reserved support C, and the unmatched material/path head remain unchanged by the present register operations; no binding is performed.

## 1. Two local interactions and their timed composition

All register arithmetic below is in Z/kZ, k>=2. Let the source phases be (a,b,c), scratch be (u,v), and immutable source arrival residues be (t_A,t_R,t_C). Define

 X_A: (a,b,u) -> (b+u,b,a-b),
 X_C: (c,b,v) -> (b+v,b,c-b).

Each is an involution: applying it twice restores all three arguments. Each touches at most three register fields. They commute with each other because b is read but not changed. Let D shift a,b,c by +1 and leave scratch/timestamps fixed. Both exchanges commute with D, since their stored differences are invariant under a common shift.

A serialized two-tick exchange is D^2 X_C X_A (composition read right to left), not the one-tick map from U14. Explicitly its output is

 (a,b,c;u,v) -> (b+2+u,b+2,b+2+v; a-b,c-b).          (1)

With blank scratch, the visible source phases agree. U14's map has b+1 rather than b+2; the relative output and scratch agree, but the extra common drift is real in this protocol's clock. Algebraic commutation does not prove that two physical events may share a participant simultaneously.

## 2. Clean scratch without undoing visible calibration

For the passive captured input at common clock tau,

 a=tau-t_A, b=tau-t_R, c=tau-t_C.

Thus the two residuals have existing source-based descriptions

 d_A=a-b=t_R-t_A, d_C=c-b=t_R-t_C.                     (2)

After (1), u=d_A and v=d_C. Now apply two further local reversible shears:

 U_A: (u,t_A,t_R) -> (u-(t_R-t_A),t_A,t_R),
 U_C: (v,t_C,t_R) -> (v-(t_R-t_C),t_C,t_R).             (3)

They have inverses using addition and preserve the source records. Include common drift before each operation, exactly as for the exchanges. On the valid input with u=v=0, the complete four-tick output is

 (b+4,b+4,b+4;0,0; t_A,t_R,t_C).                      (4)

The full eight-register transformation is a bijection on ALL register inputs, not merely on valid timing witnesses: reverse the operations and reverse the four drift ticks. Equation (4) is only the passive-consistent restriction of that bijection. On arbitrary inputs with blank scratch, the final scratch is exactly

 (a-b-(t_R-t_A), c-b-(t_R-t_C)).                       (5)

This retained defect is why an incorrect side record cannot be treated as a successful reset. The high-level prepared-input checker rejects an inconsistent timestamp-only witness before starting.

This construction recycles the two temporary scratch registers, not all information. The original source record still distinguishes the formerly unequal phase tuples. It neither proves mandatory permanent retention of every history nor proves zero physical erasure cost. A smaller sufficient side record may replace the timestamps in a declared observation language.

## 3. Explicit original A/R/C continuation and intervention provenance

Consume U14's deterministic three-source trace with route lengths (1,3,1), arrivals (1,3,1), target y=E3, period k=4. At tau=3 the phases are (2,0,2), the two local scratch registers are blank. The three-source routing occurrence is retained, not natively fired. The complete actual logical trace is

 tick3 input:    (2,0,2;0,0)
 tick4 D then XA:(1,1,3;2,0)
 tick5 D then XC:(2,2,2;2,2)
 tick6 D then UA:(3,3,3;0,2)
 tick7 D then UC:(0,0,0;0,0).

All three arrival records remain (1,3,1). Each step carries a positive unit BRC trace weight; that weight is a deterministic logical branch, not energy. The two scratch identities are unchanged and available after cleanup, whereas A/R/C remain reserved for the same pending candidate; no occurrence is reissued.

At tick7, naive reconstruction from the old timestamps alone gives (2,0,2), NOT the actual (0,0,0). The exact extended readout is

 phi_i(t)=t-T_i+kappa_i(t) mod k,

where kappa_i accumulates recorded non-drift phase changes. In this example kappa=(2,0,2). The source-preparation record plus the named interventions reconstructs it. Omitting the intervention and treating old arrivals as an unchanged state law creates a new representation defect. Existing U14 phase-sensitive state therefore cannot be replaced by timestamps alone once coupling is allowed.

The code also tries an inconsistent same-residue timestamp witness and rejects it. It does not implement authenticated distributed version certificates; immutable source identification and no hidden intervening write remain input obligations.

## 4. Exact side-information capacity, with and without correlations

Fix the reference b and the desired common output. Let d=(a-b,c-b) vary over the admitted relative pairs, and let h=f(d) be preserved side information. Assume a purported reversible reset makes all other visible outputs identical and leaves only an extra residual register r available. For any fixed h, different d in f^{-1}(h) must give different r, or injectivity fails. Therefore

 |range(r)| >= max_h |f^{-1}(h)|.                       (6)

If no other varying output is allowed, blank reusable scratch is possible only when f is injective on the admitted domain. For the full k^2 pairs: no side information needs at least k^2 residual states; retaining only d_A+d_C mod k leaves k-fold ambiguity; retaining the pair leaves ambiguity one. In the middle case, retaining d_A as one extra k-state record suffices because d_C=h-d_A. These are conditional information bounds, not universal spatial-memory or energy bounds. Known correlations or a smaller input domain change the fiber sizes.

A stronger cleanup witness uses d_A,d_C independently uniform. Keep aligned source phases constant and source residues (-d_A,0,-d_C). Population P has scratch (d_A,d_C); Q has scratch (d_A+1,d_C). The entire scratch marginal and the entire source-history marginal are identical in P and Q, including finite C/W/M data. Their ASSOCIATION differs. Applying the same two shears (3) yields scratch (0,0) with probability one in P and (1,0) with probability one in Q. The blank/nonblank observation has total variation one.

These are explicitly prepared logical input ensembles, not an independently established physical ensemble. Each paired history weight is used once. The example shows that separately stored marginal summaries do not certify cleanup; it is not a claim that all conceivable individual-side summaries are insufficient.

## 5. Cost consumes residence time: an exact composition law

Assume blank scratch and correct local timing records are available when the last source arrives; all involved source records must remain eligible through the last controller stage. No extra transport or record acquisition is hidden in that assumption. Additional real costs must be included if this interface is implemented elsewhere.

Let the first arrival times be T_i, Delta=max T_i-min T_i, and let d be the specified post-arrival stage count: d=2 for alignment only, d=4 for alignment plus scratch cleanup. The controller is admitted only if

 Delta+d<=H.                                           (7)

Otherwise it retains a timing-blocked input without beginning partial mutation. An admitted transaction completes at max T_i+d. This serial policy is conservative and specific: allowing sources to be released earlier or using genuinely parallel certified operations changes the cost model.

By (7), for the unchanged U13 arrival law,

 P_complete(H,d)=0 if H<d;
 P_complete(H,d)=P_U13(H-d) otherwise.                  (8)

The exact first-completion C/W/M curve is the U13 window-(H-d) first-ready curve shifted by d ticks. Each source history has one last arrival, and the following deterministic controller trace has weight one, so there is no extra multiplicity or squared source mass. This proof covers all time, not a finite simulation extrapolation. Infinite H gives success one under the explicitly reliable blank-record/coupling assumptions, not under passive U14 phase drift.

For half-advance probabilities and lengths (1,3,1):

 d=4,H=4: 1/343;
 d=4,H=6: 849/5488;
 d=4,H=8: 46087/87808.

The deterministic arrivals (1,3,1) require H>=6 to finish all four stages; alignment alone requires H>=4. The source routing still used only its previous five spatial edges; these added ticks are logical storage/interaction stages, not spatial hops or calibrated heartbeats.

A declared short lifetime may prevent a correct repair. Merely saying that a final algebraic map exists does not authorize performing it after its inputs have expired.

## 6. Execution and provenance

The standalone checker imports the unchanged retained_phase.py blob713bf2ddcce9abd5f8b3ddbd9990f102055ce90d, hence the unchanged U13/U12/U11/U9/U8/U2 weighted-BRC chain. All 24 predecessor archive entries and eight dependency Git blobs were checked. Only the already inherited loader adaptation removing two unused relative imports is used; old scientific function bodies are unchanged. No old full suite is rerun and counted as new work.

Tests include complete eight-register permutations for k2 and k3 (6817 inputs), 783 local three-register tests, 2274 passive-consistent modular captured snapshots, the actual inherited source trace, stale-record rejection, exact side-information fibers, the association counterexample, and 17600 finite arrival/controller cases. The finite arrival population covers positive first-arrival times up to10, all H0..10 and both declared costs; its C/W/M curves are checked against the separately composed upstream first-ready interface. Exact all-time values use the original positive loop closure, not a matrix inverse or a numerical fit. Final assertion counts, calls and hashes are in CHECKPOINT.json and evidence/results.json.

Finite exhaustive tests supplement the algebraic all-k and all-time proofs. Same-author isolated replay is not independent review. The trace stores selected detailed examples and bounded population certificates, not every raw test state; all states are reproducible from the deterministic checker and its declared finite loops.

Prior art: C.H. Bennett, Logical Reversibility of Computation, IBM Journal of Research and Development 17 (1973), 525-532, primary article text hosted by Princeton (abstract/introductory construction consulted); Parent/Roetteler/Svore, Reversible circuit compilation with space constraints, arXiv:1510.00377 (official abstract consulted). Reversible cleanup with retained inputs and dependency-aware uncomputation are not claimed as general inventions. The new scope is this source-timed phase circuit, its wrong-association witness and deadline composition. No thermodynamic cost is inferred from that literature.

## 7. Exact boundary and next unit

Completed: a timed finite logical implementation that can reuse scratch without losing the information needed for its inverse, conditional on source-linked side information. The prior statement that blind reuse of uncleared U14 scratch fails is preserved; this is a different, explicitly informed process.

Still absent: source-justified primitive action incidences and a field/material successor map realizing XA/XC or UA/UC. The local triple register grammar is not a native triadic force certificate, does not move the material or bind its pending head, and does not account for the support resource's mechanical reaction. This conditional module is not an autonomous force-maintained aggregate or a prime criterion.

The next scientific target is one concrete sourced state-dependent interaction, with its available input records, admissible action occurrences, physical or declared event duration, and both material/support outputs. Current evidence reduces its computational obligations; it does not supply the native law. Preserve this distinction rather than adding more uncalibrated memory parameters and declaring that the force problem has been solved.
