# R71 — Wrap-aware absolute phase-class source certificate (author-side research)

Date: 2026-11-11. Predecessor R70 commit 1ca0973af8bdc9af1283c003265110d53aa8c85f. Original frozen S23/AV science pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34 **unchanged**. Real researcher activity RA-21993D058A901C7791A9270D (session issuer EM-DIRECT-F6E9BD). Independent author-side mathematical derivation, not a shared-task CLAIM/Result/Review, not a native X6/BRC dynamical result.

## 1. Domain, observer, and retained state

Finite multiset E of distinct source **identities** e=(t,b), with integer source time t and branch identity b. Observation has integer j and fixed rational phase x. For real parameter theta and integer a,b0, source e belongs to the ORIGINAL-LABELLED target arc if

P_e(theta) : {x+(t-j)theta} in A(theta)=[{a theta},{b0 theta}).

Curly braces mean fractional part, with the lower boundary included and upper excluded. Fix a rational anchor theta0=p/q in lowest terms and a nonempty rational closed I=[L,U] containing theta0. Assume floors floor(a L)=floor(a U)=k_a, floor(b0 L)=floor(b0 U)=k_b and {a theta}<{b0 theta} throughout I (it suffices to check endpoints after the floor hypotheses). This is a stable, nonwrapping arc; this theorem does not silently include arcs crossing zero or varying original-label order. Time, branch, original label and observation signature remain separately typed.

The **full event collection E is preserved** for insertions/deletions and any future operation. The phase-class data below is a derived, observer-specific query accelerator and is not a replacement for E.

## 2. Anchor-independent-of-observer phase grouping

For each e=(t,b) set rho_t={t theta0}. Let C_rho be every event whose time has this same exact anchor phase. For each nonempty group retain the pair (t_min,t_max), and separately retain all identities. There are g groups, with g <= min(|E|,q), because theta0=p/q reduced, t integer, and equality of residues depends only on t mod q. The collection of groups depends on theta0 and the actual source times, but **not** on observation j or x.

For a query (j,x), define beta_rho={rho+x-j theta0}, and delta=theta-theta0. Every e in group C_rho satisfies the exact circle congruence

{x+(t-j)theta} = { beta_rho + (t-j) delta }.

This identity is valid through arbitrarily many integer phase crossings; the lift on the right need not remain in [0,1). A change of j or x rotates each group by the same observer offset, and subtracting j from both time extrema adjusts the slope bounds. Thus one absolute-phase group index supports all exact rational observations without regrouping events. Query signature is still needed to cache any resulting certificate.

## 3. Sound all-real-parameter exclusion certificate

Let d_min=t_min-j, d_max=t_max-j, D={L-theta0,U-theta0}. Form the four products d_min D_lo,d_min D_hi,d_max D_lo,d_max D_hi and their minimum h_- and maximum h_+. The entire lifted phase of every group member at every theta in I lies in the closed range

S_rho=[s_-,s_+]=[beta_rho+h_-, beta_rho+h_+].

The extremal interval is the exact range envelope of the affine family over the rectangle of real slopes [d_min,d_max] and deltas [L-theta0,U-theta0]; both times actually occur in the finite group, so the range extrema are also attained by group members at endpoints. Internal anchor phase order is not needed.

Because the arc boundary floors are constant on I, every member of A(theta) can be represented by the unwrapped interval [a theta-k_a,b0 theta-k_b). Enclose every such interval by

Q_I=[q_-,q_+], with
q_-=min(a L-k_a,a U-k_a), q_+=max(b0 L-k_b,b0 U-k_b).

Every membership event would force an integer k such that the closed ranges S_rho and [q_-+k,q_++k] intersect. The eligible integers would satisfy

s_--q_+ <= k <= s_+-q_-.

Hence the **sufficient exact exclusion condition** is

ceil(s_--q_+) > floor(s_+-q_-).    (R71-EXCLUDE)

When it holds, P_e(theta) is false for EVERY e in C_rho and EVERY REAL theta in I, including endpoints and wrap points. Repeating for each group proves whole-subtree OUT without checking individual events. Using closed bounding boxes is intentionally conservative at exclusive upper endpoints; a failed certificate means UNKNOWN, not membership.

For a constant latest-source readout, if candidate e* is independently proved to qualify throughout I and all events with time t>t* are covered by the above exclusion certificates, then max qualifying time equals t* throughout I. This does not select a unique branch among equal-time branches; if branch-specific output is needed, retain and certify its tie rule.

Proof: (i) the displayed circle congruence follows by substituting rho={t theta0}, (ii) a bilinear product of one variable in [d_min,d_max] and one in [delta_min,delta_max] is bounded by its four corners, (iii) a hypothetical membership would imply an integer shift k in the derived closed overlap interval, contradicting the strict ceil/floor test. Candidate constancy then follows from max-time ordering.

## 4. Strict improvement and infinite verified family

Take theta0=1/4, a=1,b0=2. For N>=1 define

C_N = {(4k,branch_k),(4k-1,branch'_k) : 1<=k<=N},
I_N=[1/4-1/(100N),1/4+1/(100N)].

The 2N source events lie in **exactly two** anchor phase groups, rho=0 and rho=3/4. For every theta in I_N, the first group's lift lies in [-1/25,1/25] and the second in [3/4-1/25,3/4+1/25], while the target arc has lower endpoint at least 6/25 and upper endpoint at most 13/25. Both group intervals are disjoint modulo integers from the target bounding interval; R71-EXCLUDE succeeds twice, for all N. Each source group may wrap through 0 inside the interval.

A single old four-extrema hull merges both groups into one range spanning the target arc, so its sufficient exclusion test fails. This is a constructive family where ONE preprocessing pass of 2N sources yields TWO exact all-real interval group tests per repeated query. There is no claim of universal speedup or a lower bound for all possible algorithms.

In the small R70 wrap witness theta0=1/4, I=[249/1000,251/1000], the events (3,b3),(4,b0),(4,b1) are all excluded by the group certificate, while source (1,winning) is always in the arc, proving latest qualifying time 1 throughout I. Adding (6,recent) changes the latest time: 6 at theta=249/1000, 1 at theta=1/4 and 251/1000. The algorithm correctly declines an all-interval certificate. Deleting only branch (4,b0) retains (4,b1); any update must use a new immutable-version group index or an identity-aware maintained multiset.

## 5. Sharp four-extrema incompleteness witness

At theta0=1/10 and I=[99/1000,101/1000], target arc [{4theta},{6theta}), compare source sets C1={1,9} and C2={1,5,9}. The four global extrema (minimum and maximum time, minimum and maximum anchor phase) are IDENTICAL: (1,9,1/10,9/10). Yet all C1 sources remain outside the arc for every theta in I, while the t=5 member of C2 remains inside. Thus the four extrema cannot **completely decide** exclusion across all source sets; they are valid only as a sufficient envelope certificate. This precise limitation leaves room for splitting by phase class, finer subtrees, or independent source tests.

## 6. Operation accounting, evidence status, and boundaries

Grouping from n source identities takes n exact modular computations and O(n) event storage plus O(g) stored group extrema (and possibly additional map/balanced structure overhead). With a precompiled group index, one exact observer-specific interval-exclusion query takes O(g) bounded rational/corner tests, where g<=min(n,q). An input family with g=2 yields O(1) such arithmetic tests after O(n) preprocessing. Full integer bit costs must separately include time/denominator bit width, modular multiplication, rational gcd, representation conversion, cache admission, persistent updates, output and verification. Deletion of a group extremum requires recomputing or maintaining a versioned ordered group structure; no unexecuted O(log n) persistent-update claim is made.

BRC relevance: exact branch support and provenance are retained at the full event layer; grouping is an observer-targeted quotient and is safe **only** for the stated membership/max-time and certified interval queries. It is not yet an ACTUAL_TYPED_BRC_ONLY native operation, and no heartbeat/X6 theorem is claimed.

Computational evidence: check_r71_min.py passes the small wrap witness, four-extrema witness, eight infinite-family sizes (up to 2048 events), and moving-observer checks. The extended local checker independently evaluated all finite critical points and midpoints in 179 valid random models (seed 20261111), accepted 11 entire-set exclusion certificates, including 6 that the single-hull test could not certify, and encountered 51 certified phase-class cases with a wrap. A separate full-interval matched benchmark for 256 events / 8 queries recorded 172.794 ms for a direct R70-style per-event critical partition and 0.857 ms including group compilation for R71, on this deliberately favorable two-class input; median of three local Python runs, not a general cross-machine or full R66/R68 cost claim. Native independent review and formal task adoption remain pending.

## 7. Next exact research unit

Build a persistent identity-preserving ordered multiset per anchor phase group, supporting deletion of an extremal branch and reuse of unchanged group certificates across immutable versions and moving observers; measure original R66/R68 tree costs on *identical* input/output obligations. Determine an input-side criterion for phase-group partition versus child-subtree splitting on wide parameter intervals. A newly selected formal task would require its own real CLAIM; this author-side note does not grant one.
