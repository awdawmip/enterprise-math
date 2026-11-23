# R284GE — Exact all-parameter adjacent no-rollback capacity and a sufficient full-cycle test

Date: 2026-11-24 Asia/Shanghai. Informed portable TASK_RESEARCH, same R284CO/R284FM/R284FT frozen auxiliary four-phase binary observer. P000 and ACTIVE worldview unchanged; no native BRC numerical computation is required by this auxiliary Boolean model. Author-derived, exact finite crosschecks, NOT independently reviewed. No shared CLAIM.

## 1. Audit of R284FM reachability

For any phase i, assign each nonconstant coordinate k to its last nominal changing edge ell_i(k). Constant columns retain their fixed values. A stable error relative to c_i requires failure of the last changing attempt: a success on that edge sets the bit correctly and no later attempt changes it before i. Thus each group contains at most q errors. Conversely take any such error subset. Start at pristine c0, make every attempt succeed up to a visit to phase i, then make one full cycle from i to i, omitting exactly the desired coordinates at their respective last changing edges of that cycle. For each designated bit, its previous nominal change within or before that cycle has succeeded (no other omission on that bit); immediately before its last changing attempt it has the opposite binary value. Omit that last attempt. All other attempts succeed. The desired stable word is obtained. This proves the product of last-change group error balls, with a uniform finite reachability horizon: at most 7 edges from pristine c0 (i+4). No indefinite age assumption is used to fabricate extra errors. This is a reconstruction of R284FM, not a new independent Review.

For any word w, its exact distance to S_i is the sum over last-change groups of max(0, mismatch_count_to_c_i - q), plus mismatches on constant columns. Correcting up to q mismatch coordinates independently in each group attains the lower bound. R284FM's pairwise eight-source cut also follows by assigning each differing coordinate to a correcting budget vertex; its integral cut dual subtracts q times the number of chosen budget vertices. Radius-u read balls of two sets intersect iff their minimum physical Hamming distance is at most 2u. This uses one global read budget on each side, not one per source group.

## 2. New exact no-rollback theorem (all integer q,u >= 0)

Fix one adjacent edge i -> t=(i+1) mod 4. Let D be the nominal number of changing coordinates and N_e the number of those coordinates whose last nominal change before i was edge e. Put

    D = sum_e N_e
    B = sum_e min(q,N_e).

All changed coordinates have the same last-change group (the current edge) in phase t. The other coordinates' values and last-change groups remain unchanged. In particular the exact stable adjacent distance is max(0,D-B-q).

**Theorem GE1.** Stable read separation of i and t, together with the absence of any forced newer-then-older successful read during this edge, is possible if and only if

    D >= q + B + 4u + 1.                         (GE1)

This statement ignores third-phase recognition, which is a separate full-cycle requirement. If GE1 holds, *every* attempt order is free of forced old/new rollback under the minimal forced decoder (defined below); if it fails, either stable separation fails, or *every* attempt order has a rollback witness even when all current-edge attempts succeed. In the single-source case with D>=q this reduces to 2q+4u+1, the earlier nominal adjacent distance bound. Extra changing columns in other small source groups can contribute zero to the left side of the equivalent condition sum_e (N_e-q)_+ >= q+4u+1.

**Exact fixed-prefix test.** Let s_e be the number of successfully overwritten changing bits in source group e at any prefix (current omissions may be arbitrary within budget). Write

    O = sum_e (s_e-q)_+
    P = sum_e min(s_e,(N_e-q)_+)
    r = D-q-B-2u.

There exists a physically reachable word at this prefix from which both phase i and phase t can be forced by (possibly different) noisy reads iff

    O <= 2u, P >= r, r <= 2u.                    (GE2)

Proof. A noisy read from a physical word w can force phase j by intersecting the stable noisy-read set B_u(S_j) iff dist(w,S_j)<=2u. A rollback witness at the same paused word requires both inequalities. Source errors on unchanged coordinates are never helpful for this pair; both nominal bits and source group labels agree there, and removing the errors weakly decreases both distances. On a changed coordinate, the source initial error is already the new target bit. Let h_e count such errors on the non-overwritten bits of source group e, so 0<=h_e<=min(q,N_e-s_e); all choices are physically attainable by section 1. After overwriting, let z_e=s_e+h_e. Then

    dist(w,S_i) = sum_e (z_e-q)_+
    dist(w,S_t) = (D-sum_e z_e-q)_+.

These equalities hold when unchanged errors are set to zero; for any other source word the changed-coordinate terms are lower bounds on the two distances. The two inequalities can thus hold iff there is an integer z_e with s_e<=z_e<=A_e=min(N_e,s_e+q), sum (z_e-q)_+<=2u, sum z_e>=D-q-2u. The feasible region is nonempty iff O<=2u. Given feasibility, start at z_e=s_e, fill every available free slot to q, and allocate remaining overflow budget among groups. The maximum attainable sum z is min(sum A_e, B+2u), because min(q,A_e)=min(q,N_e). All increments are unit integers. Also sum A_e=B+P. The exact joint test follows.

For an arbitrary fixed initial physical state, actual successful overwrites only move changed bits toward c_t and away from c_i (or leave a bit already correct for t unchanged). Consequently dist(w,S_i) is nondecreasing along the edge, and dist(w,S_t) is nonincreasing; this follows directly from the group overflow formula. If an earlier prefix permits new success and a later prefix permits old success, the earlier prefix also permits old success. Thus all forced rollback along a single trajectory reduces exactly to the simultaneous ambiguity in GE2, including a paused writer. Conversely such a simultaneous ambiguity itself permits two adversarial reads in the forbidden order.

If r>2u, GE2 never holds, and adjacent stable separation holds. If r<=0, stable separation fails by the adjacent distance above. If 1<=r<=2u, follow any attempt order with zero current omissions. P starts at 0, ends at D-B>=r and increments by at most one, so there is a prefix with P=r. For every s_e<=N_e we have (s_e-q)_+<=min(s_e,(N_e-q)_+), hence O<=P=r<=2u. GE2 now gives a reachable source history and forced rollback witness at that prefix. This proves GE1, with no finite q or u cutoff.

## 3. An exact full-cycle decision reduction

Assume all six stable noisy-read sets are disjoint. Choose the stateless **minimal forced decoder**: output j iff the observed word belongs to B_u(S_j), otherwise return failure. Every correct decoder must agree on these sets, and additional successes outside them cannot repair a forbidden recognition or rollback. The following conditions are then necessary AND sufficient for existence of a safe fixed-order four-phase protocol in the frozen model:

* all six stable noisy-read sets are disjoint (R284FM cuts);
* each adjacent edge satisfies GE1;
* for each edge there exists a monotone attempted-count path through its changing coordinate types, from zero to full counts, such that every prefix and every allowed current omission allocation avoids forced recognition of both third phases.

For the last condition use the R284FT exact prefix-flow distance: demand for an unwritten differing bit may use either its source/target last-change budget, and demand for a successfully overwritten differing bit may use only the comparison phase budget. The maximum over all eight-vertex subsets of contained demand minus q times subset cardinality equals the minimum physical distance (unassigned demand). A third-phase distance <=2u creates a forced success; distance >2u excludes it. Permuting identical coordinate types preserves all histories and observations, so the attempted-count lattice is exact for fixed orders. Each edge's full-write endpoint with at most q omissions lies in the target stable set by section 1; unchanged errors retain their last-change group. GE1 deals with all rollback, not just prefixes with <=2u successful writes. This gives a complete existence test, whereas the older R284FT early-prefix no-rollback test was only necessary. No claim that an arbitrary third-phase-safe code exists at a new capacity is made.

## 4. Application to the previous u=1 all-q boundary

Reuse the 7 and 66 stable two-heavy families from R284GA, with q>=5 and n=4q+8 or 4q+9. The source groups for the changing types on edges 0,1,2,3 respectively are:

    edge 0: {1}, {3}, {5,7}
    edge 1: {2}, {6}, {1,5}
    edge 2: {3}, {4}, {2,5}
    edge 3: {7}, {6}, {4,5}.

Apply GE1 to all four edges. Exactly 2 of the 7 families at 4q+8 and 16 of the 66 at 4q+9 survive. Thus 55 of the 73 stable candidates can be excluded by source-count inequalities alone, with no prefix-lattice computation. All survivors contain alternating type 5 as one of the two heavy types; the {3,6} heavy pair is fully excluded at these widths.

The reduction is uniform: for a two-heavy histogram x_p=2q*1[p in G]+z_p, sum z=k<=9 and z_g>=2. Every group containing no heavy type has N_e<=5<=q, hence contributes zero to sum(N_e-q)_+. Every group with one heavy type contributes q plus its fixed offset. Every edge has at least one heavy type; when both change they lie in different groups and the two offsets total >=4, so the condition 2q+offset>=q+5 is automatic for q>=5. When only one changes GE1 is exactly an offset threshold >=5. Thus the q=5 enumeration of 2016 offsets (630+1386) covers the entire q>=5 sector without extrapolation. The survivor count was additionally reproduced at q=6,7,10,100.

This does not supersede the full R284GC/R284GD theorem dependencies; the remaining 18 families still require third-phase barriers. It supplies a new all-(q,u) analytic filter and a sufficient full-cycle search interface useful for u>=2. In particular, no blanket claim of a new sharp capacity at u>=2 is made.

## 5. Executed checks and evidence

Standard-library companion checker R284GE_exact_adjacent_rollback_checker.py:
- direct complete binary word enumeration over all ordered partitions of n<=6 changing coordinates into three source groups, q=0,1,2 and u=0,1,2, all success masks: 25,335 comparisons of GE2 against physical-word distances; all passed;
- explicit unbounded-history BFS over all normalized ordered distinct 4-tag tuples for n=2,3, q=0,1,2: 2,592 phase-level reachability-set comparisons against the product of last-change group balls; all passed;
- complete two-heavy offset enumeration at q=5,6,7,10,100 and both widths: 7 -> 2 and 66 -> 16 every time. The unlimited parameter result is by the proof, not finite regression.
The local checker output is recorded above; no native experimental result or independent formal Review is asserted.

Frozen sources:
- R284FM: 1d1c5dd412719c7aaf016187b6493b77253cd9f9:research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md
- R284FT: b654d9bbb0ac5f7083afe24076a8bb24dc4ab1f0:research_notes/portable_direct/R284FT_Q3U1_SHARP_TWENTYTWO_BIT_FLOW_PREFIX_CYCLE_20261123.md
- R284GA: 0c3284aec3e378b384beb43f232018d7978455da:research_notes/portable_direct/R284GA_TWO_HEAVY_UNIFORM_STABLE_CONVERSE_20261124.md
- R284GB: f6297d304ff04ad6de7d2050b1625e52a348cc14:research_notes/portable_direct/R284GB_TWO_HEAVY_ALL_Q_FIRST_EDGE_BARRIER_20261124.md
- R284GD: 84a477be418f97d8d113c79dca27dd2ac930ffc0:research_notes/portable_direct/R284GD_EXACT_RATIONAL_FARKAS_CERTIFICATES_ALL_Q_20261124.md

## Next

Apply GE1 to the general u>=2 high-omission boundary and the exact third-phase-only decision test; derive short explicit barriers for the 18 remaining u=1 families and independently audit R284GB/R284FW lifting. Keep independent Review and shared task acceptance separate from the author's proof and scientific-file preservation.
