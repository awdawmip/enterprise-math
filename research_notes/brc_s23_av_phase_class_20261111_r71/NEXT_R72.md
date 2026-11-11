# R72 — Identity-preserving phase-class updates and mixed strategy selection

Continue author-side R71 on unchanged S23/AV frozen pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34; preserve P000, ACTIVE worldview, source firewall, actual role/owner claims.

First precise question: construct a persistent map from exact anchor phase to a versioned identity-aware ordered time multiset. A deletion of (t,branch) must remove only that branch. For every immutable version, prove extrema readback and membership/index equality under arbitrary insertion and deletion, including when the deleted event was the unique minimum or maximum time for its class. Define the signature and invalidation boundary of certificates across (version,anchor,j,x,a,b0,I).

Second question: use the source subtree's four-extrema hull first, refine its failure into exact anchor-phase groups only when the input-side number of nonempty phase classes is small, then fall back to exact per-event finite critical partition. Compare this hybrid against original R66 persistent subtree, R68 anchored cache and R70 direct fallback on the SAME exact all-real interval output. Include preprocessing, index update, parameter bit width, full-precision rational gcd/multiplication, cache memory, source identity retention, and output recovery.

Test inputs: R70 wrap witness (3,4,4), add source time 6; R71 strict two-class family C_N of 2N events, theta0=1/4, I_N halfwidth=1/(100N); four-extrema negative pair {1,9} and {1,5,9}; moving (j,x) with changed original labels; wide parameter intervals where groups overlap the arc.

Return exact theorem/counterexample, runnable code, independent oracle, finite validation scope, evidence pointers, unresolved input-to-native BRC typed interface. No new formal task or claim is implied by this note.
