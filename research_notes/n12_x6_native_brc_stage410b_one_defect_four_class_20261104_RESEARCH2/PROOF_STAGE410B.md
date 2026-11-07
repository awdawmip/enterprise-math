# Stage410-B — Exact four-state quotient in a one-defect P / two-defect Q native-X6 fiber

Date: 2026-11-04 (Asia/Shanghai). Research2 continuation from Stage409-B at commit `61074f94eb0dde9dbb252f01d12dab030ecf2ac7`; Draft PR #1736. Classification: AUTHOR_PROVED / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Frozen inputs and exact scope

Scientific inputs remain global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current behavioral rules were read separately from their current main branches. Spatial basis is the complete native signed six-axis X6 alphabet `D={±E_1,...,±E_6}`, not a separate two-dimensional plane. Fix `A=+E_1`, `B=-E_1`, the initial supports of the test fiber. The other ten directions are available in every future paired APP. No native physical time calibration or extra spatial axis is asserted.

For ordered words P,Q, observe at **every** intermediate state the lengths, two native six-axis endpoints, their full *labelled directed* adjacency histograms J_P,J_Q, and `K(P,Q)=sum_{i<=min(|P|,|Q|)}[P_i=Q_i]`, with action enabledness. Endpoint-derived positive native BRC weights/counts and inherited direction-local commutative signed products follow the same observations. Allowed future action traces are any finite sequence of `APP(a,b)` (all 144 ordered native-direction pairs), up to one `POP_Q`, and up to one `CANCEL`, which simultaneously removes the last inverse adjacent pair of **each** source, only when both pairs exist. Budgets and action order are observable.

## Theorem 410.1: a complete six-path fiber with exactly four future states

Fix both original lengths at 6, endpoints `z_P=4E_1, z_Q=2E_1`, joint count `K=5`, and directed adjacency counts

`J_P(AA)=3, J_P(AB)=J_P(BA)=1; J_Q(AA)=1, J_Q(AB)=J_Q(BA)=2`,

with every unspecified directed edge count zero. The complete full-X6 observation fiber consists **exactly** of six path pairs, partitioned as

- `C0 = {(ABAAAA,ABABAA), (AAABAA,ABABAA)}`;
- `C1 = {(ABAAAA,ABAABA), (AABAAA,AABABA)}`;
- `C2 = {(AAAABA,ABAABA)}`;
- `C3 = {(AAAABA,AABABA)}`.

For the declared unbounded finite future language, two histories are equivalent if and only if they lie in the same C-class. Therefore

`q(F)=4`, with source-pair multiplicities `[2,2,1,1]`.

The sufficient raw `(suffix_3(P),suffix_4(Q))` carrier has six keys on this fiber, so observer-safe minimization reduces six raw suffix states to four true states. The fixed-length binary bound is reduced from `ceil(log2 6)=3` bits to `ceil(log2 4)=2` bits. This is an exact, scope-typed future-observer quotient, not erasure of native path provenance outside the declared observer language.

### Complete-fiber proof

The P histogram enforces exactly five A letters and one B, starting and ending A, so `P=A^iBA^(5-i)` for i=1,2,3,4. The Q histogram enforces exactly four A letters, two separated B letters, starting and ending A, thus Q is exactly one of `ABABAA`, `ABAABA`, `AABABA` (the three positive compositions `u+v+w=4`). Since P contains one B and Q contains two, equality at five of the six positions occurs exactly when the P B aligns with one of the two Q Bs. Each of the three Q paths has two admissible choices for P. This produces precisely the six listed pairs. All have the stipulated endpoints and adjacency counts. No paths using the other ten native directions satisfy those fully labelled J constraints.

### Bisimulation proof for the two non-singleton classes

Write a future state after any common action trace as `(P[1:6-d_P] U, Q[1:6-d_Q] V; spent_POP, spent_CANCEL)`, where U,V are the surviving stacks of letters appended by the trace. For C0 or C1 initial histories, both original P paths end in AA. A CANCEL can therefore remove at most one original P letter: to reach it the CANCEL must encounter a previously appended inverse letter; direct erasure of two original P letters is impossible. Thus `0<=d_P<=1`, and if `d_P=1`, the unique CANCEL was spent.

At most two original Q letters can be removed. If POP_Q erases an original Q letter, a subsequent CANCEL that reaches the original P boundary needs a paired APP first; that APP also puts a letter on Q, so CANCEL can erase at most one further original Q letter. If POP_Q erases an appended Q letter instead, no original Q letter was removed by POP; the sole CANCEL can remove at most two original Q letters. Without POP, any APP needed to expose the P cancellation boundary also leaves a Q appended letter, so this case is no larger. Therefore `0<=d_Q<=2`; a configuration with `d_Q=2` has exhausted both destructive budgets.

For **both** C0 and C1 the following exact finite original-boundary certificate holds for all six combinations `d_P∈{0,1}`, `d_Q∈{0,1,2}` (12 checks across the two pairs):

1. The truncated original source-pair observations (length, X6 endpoints, full J_P,J_Q, absolute-position K) are equal.
2. The retained P original prefixes have equal final two letters at `d_P=0`, and equal final one letter at `d_P=1` (no CANCEL remains). The retained Q prefixes have equal final two letters at `d_Q<=1`, and equal final one letter at `d_Q=2` (no destructive operation remains).
3. Original positions 5 and 6 of P are A for both members of either class. In C0 the Q original is identical across the two paths; in C1 Q original positions 5 and 6 are respectively B,A for both. Hence any appended-versus-original overlap arising from unequal retained original lengths sees the same original labels.

The 12 certificates are exact integer/string identities, rechecked in the executed source. In particular, K is compared on truncated **paired** originals, not inferred from separate source counts. For arbitrary identical surviving appended words U,V, individual J/endpoints are obtained by joining the certified original prefixes to U,V, using their equal final letters. Joint K decomposes into original-original, appended-original and appended-appended overlaps; all three contributions match by (1)–(3). Enabled POP and CANCEL depend only on the same boundary letters and remaining budgets. Every enabled common operation yields another paired state of the certified type. This defines a full-12-direction bisimulation by induction over arbitrary finite traces.

**Important boundary nuance:** after erasing one P original letter, the two P *penultimate* original labels can differ (C0), but CANCEL is already spent. Comparing those penultimate labels would impose an unnecessary and false condition. Likewise Q after two original erasures needs only its terminal label, since both erasers are exhausted. The proof uses budget-sensitive boundary information, not a globally equal last-two-tag claim.

### Necessity: explicit shortest distinguishing actions

The initial observations agree by construction. Between C0 and C1, one `POP_Q` yields different directed Q adjacency histograms (compare `ABABA` and `ABAAB`, for example). Between either C0/C1 and either C2/C3, immediate `CANCEL` is disabled for the former (P ends AA) but enabled for the latter (P ends BA, Q ends BA). C2 and C3 are separated by `POP_Q; CANCEL`: their resulting Q words are respectively `ABA` and `AAB`, with distinct labelled J. All distinguishing traces use legal operations and require no newly introduced native direction, so they are also valid in the full twelve-direction language. Thus the four classes cannot be merged.

## Exact executable evidence and complexity

`REPRO_STAGE410B.js` was actually executed as JavaScript using its saved source text. It constructs the six full histories by independent direct enumeration and verifies uniform current observation. A separate remaining-directed-edge Euler/K integer transfer starts from A on each source, updates both residual J counters together with K and raw suffix keys, and independently obtains six path pairs / six raw safe suffix keys, each with multiplicity one. Its state counts by extension depth are `[1,4,6,12,12,12]` (ending with the K=5 filter). The 12 budget-sensitive prefix cases and all six interclass distinguishing pairs pass.

The complete twelve native-direction positive BRC recurrence `N_{t+1}(z)=sum_{d∈D}N_t(z-d)`, `W_{t+1}(z)=sum_{d∈D}w(d)W_t(z-d)` with `w(A)=2, w(B)=3`, and w(other)=1 yields at t=6:
`N_6(4E1)=156, W_6(4E1)=2976; N_6(2E1)=4665, W_6(2E1)=32760`. These counts refer to the *full native endpoint populations*, not the six-path J/K fiber. They are not signed-amplitude cancellation claims.

This code checks a finite certificate; the all-horizon assertion follows from the budget-sensitive bisimulation proof, not finite trace exhaustion. For fixed signed alphabet and fixed suffix budget, residual-Euler/K state counts are polynomial in the **numeric** path length/edge counts; no polynomial-time claim is made for bit-encoded multiplicities or general unbounded direction alphabets. The verifier is evidence for this one six-step fiber, not a general Stage411 quotient solver.

## Governance and next discriminating question

The GitHub storage/portable-author proof does not grant native CLAIM, Result or review authority. Native session creation was actually denied `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`), and active owner listing returned `CONTROL_QUOTA`. Formal Driver independent acceptance remains open. P000 and ACTIVE Heartbeat World remain unmodified.

Stage411-B should calculate and prove the exact quotient for n=7, J_P(AA)=4, J_P(AB)=J_P(BA)=1; J_Q(AA)=2, J_Q(AB)=J_Q(BA)=2, and joint K=6, then seek a uniform formula for the n-variable one-defect P family. Exact bridge to native BRC carriers and information-retaining provenance remains explicit.
