# R284GI — Sharp four-phase capacity down to q >= 3u; exact q=5,u=2 boundary

Date: 2026-11-24 (Asia/Shanghai). Informed portable TASK_RESEARCH. Author proof and exact computation, NOT independently reviewed. No formal CLAIM or Result. Same frozen Boolean auxiliary observer as R284GH/R284GG/R284FM/R284GE; P000 and ACTIVE worldview unchanged.

## Main results

For all integers u>=1, q>=3u,

    n_min(q,u) = 4q+8u+2.

Additionally n_min(5,2)=38 by a complete finite calculation. Earlier u=1 q>=2 result remains in force. This moves the general q threshold from 4u-1 to 3u and closes the first lower layer for u=2. The next line q=3u-1 genuinely admits non-two-heavy histograms satisfying both diagonal stable cuts and all four exact no-rollback conditions, for every u>=2 (see section 4).

The model is the frozen four fixed distinct binary tags in cyclic order; each nominally changing bit attempted once per edge in a fixed order, at most q failed attempts per edge, arbitrary persistence of omissions, at most u adversarial bit flips per read, stateless decoder, correct stable reads, no third-phase success during a prefix and no newer-then-older successful read along an edge. Complement columns to make c0=0 and discard constants as in R284GG. Type p is the nonzero 3-bit tuple (c1,c2,c3) with c1 the least significant bit, multiplicity x_p.

## 1. Exact two-heavy completeness for q>=3u

Reuse the R284GG six disjunctions, replacing its q>=4u+1 by q>=3u. Variables x1,...,x7,q,u are nonnegative, u>=1, sum x<=4q+8u+1. A physical non-two-heavy histogram must have both x_p<=2q+2u-1 in at least one of the pairs (3,5),(3,6),(5,6). For each diagonal, with four edge types {3,6,a,b} (a,b=2,7 or 1,4), require one of the following: a single type >=2q+2u+1, a pair of incident types >=3q+2u+1 (one from each of {3,6},{a,b}), or the four-type sum >=4q+2u+1. For each adjacent edge use GE1: sum_e (N_e-q)_+ >= q+4u+1. Its seven affine disjuncts are the nonempty subsets of the three source groups {1},{3},{5,7}; {2},{6},{1,5}; {4},{3},{2,5}; {7},{6},{4,5}, respectively. A subset J requires sum_{e in J} N_e >= (|J|+1)q+4u+1.

All three real-relaxed nonheavy systems are impossible. Adaptive branching (choose the remaining disjunction with fewest feasible children, cover ALL its children) yielded 191,187,191 contradictory leaves respectively. Every leaf has nonnegative rational multipliers with sum lambda_i A_i=0 and sum lambda_i b_i<0 for A_i v<=b_i. Maximum denominators 13,14,13. SciPy/HiGHS was used only to find multipliers and choose branch order; Python Fraction replay checked every leaf and complete coverage. No upper bound on q or u. Explicit nonnegativity rows prevent hidden LP-bound assumptions. Full embedded data (41268 bytes uncompressed, SHA256 3e45c1bd608ba253edf3a3731ece721d2a4e9f706038a3b803e7356078fdd679) and a standard-library verifier are at commit 2df8c2d0f48a9ab713e85c480d3569abfc11ab27:research_notes/portable_direct/R284GI_q3u_exact_certificate.py. Generated tree replay was actually executed locally, returning (191,13),(187,14),(191,13); the remote embedded compressed data was read back and matched the local encoded data by length and FNV-1a64 (5b5018e7aad710c). The verifier itself checks decompressed SHA256. Run without -O.

Consequently at least two of {3,5,6} have x>=2q+2u.

## 2. Stronger source-resolved obstruction of the whole two-heavy sector

Write n=4q+k, k<=8u+1, two heavy sizes 2q+a,2q+b with a,b>=2u, and residual total R=k-a-b. For disjoint groups of total M their combined overflow beyond q is at most (M-q)_+. (Any positive overflow subtracts at least one q.)

If the pair is {3,6}, on edges 0 and 1 only one heavy changes and it is alone in its source group. GE1 and R<=4u+1, q>=3u yield a,b>=4u+1-(R-q)_+>=3u. Hence R<=2u+1<=q and the same constraints sharpen to a,b>=4u+1, contradicting k<=8u+1.

Otherwise by cyclic phase rotation it suffices to use g=3,h=5, a the offset of g, b of h. (Rotating the old {5,6} case by one phase and complement-normalizing maps it to {3,5}, preserving the omission/read model.) On edges 1 and 3 only h changes among the two heavies; the h source group includes x1 and x4 respectively. GE1 implies

    b + max(x_i,R-q) >= 4u+1,  i in {1,4}.              (1)

Indeed the heavy group contributes q+b+x_i and all other groups contribute at most (R-x_i-q)_+.

If b=2u, then 4u+1-b=2u+1>R-q (which is <=u+1); (1) requires x1+x4>=4u+2>R. Thus b>=2u+1 and R<=4u. If a=2u, the diagonal (0,2) differs on g and at most R residual columns, not on h. No single-type cut works: g is exactly 2q+2u, residual sizes <=4u. No four-vertex cut works since total differing mass <=2q+6u<4q+2u+1. A three-vertex cut must use g and one residual type of size >=q+1>=3u+1. Then R>=3u+1, b<=8u+1-2u-R<=3u, and (1), using R-q<=u, gives x1,x4>=u+1. At most u-1 residual columns lie outside that one large type, contradicting two distinct such types. Therefore a>=2u+1. If b=2u+1, R<=4u-1, R-q<=u-1, so (1) forces x1+x4>=4u>R. Hence b>=2u+2 and R<=4u-2.

The new idea is to retain individual comparison last-change slots instead of reserving the entire residual R against each heavy budget. For edge 0->1, g-only third phase is 2, h-only third phase is 3. Last-change edge indices of p=1,...,7 at these phases are respectively (1,1,0,3,1,1,0) and (1,2,2,2,2,1,0). At both phases x1 and x4 are in distinct groups. Every residual group has mass <=q: if R<=q this is immediate; otherwise b<=k-a-R<=6u-R<=3u-1, so (1) and R-q<=u-2 force x1,x4>=u+2. A group can contain at most one of these types and thus has mass <=R-(u+2)<=3u-4<=q.

Use actual thresholds

    T_g = a+x7-2u,        T_h = b+x4-2u.                (2)

They are positive, and each is at most the corresponding heavy size (x7,x4<=q). Moreover T_g<=2u: if b>=4u+1 then a+x7<=k-b<=4u. Otherwise s=4u+1-b>0 and s-(R-q)>=q-2u+1>0 because b+R<=6u. By (1), x1,x4>=s, so a+x7<=k-b-2s<=b-1<=4u-1. Always T_h<=k-a-2u<=4u.

Follow an arbitrary fixed attempted order until one heavy threshold is first hit. Keep the residual source initially pristine. At the h-first prefix, omit all attempted g bits (fewer than T_g<=2u<=q). All h attempts succeed. Comparison with phase 3: h differs on x_h-T_h unwritten bits; its source last-change group can correct up to q of these and the comparison group e2 can correct up to q-x4 more. Among residual types sharing e2, p2 has source, target and comparison value 0, hence no mismatch; p4 accounts for at most x4 errors. Other residual groups each have capacity q, enough to correct all their own mismatches. g can be pristine and omitted, matching phase 3. Remaining physical distance is at most max(0,x_h-T_h-2q+x4)=2u.

At the g-first prefix let H<T_h be the number of attempted h bits. Omit min(q,H) of them; the excess e=(H-q)_+ succeeds. All g attempts succeed. Comparison with phase 2: g's comparison group e0 shares only residual p7, so q-x7 remains available for correcting g; its source group corrects up to q other unwritten g bits. Every residual mismatch can be corrected in the comparison phase, and the e successful h bits also fit in their distinct comparison group e1. To see this when e>0, that group's residual mass is <=R-x4, and

    (R-x4)+e <= R-x4+(T_h-1-q)
              = b+R-2u-1-q <= 4u-1-q <= q.

When e=0 the residual-group bound already suffices. The source h is pristine, the g and h comparison groups are distinct, and the exact last-change group product guarantees all selected masks attainable. Remaining distance <=max(0,x_g-T_g-2q+x7)=2u. Thus in either first-threshold case the noisy balls intersect a third phase's stable noisy ball; stable correctness forces the forbidden recognition. The witness works even if T_h>q+1, by spending the unavoidable extra h successes in the distinct comparison source slot rather than conflating it with g's budget.

This excludes every two-heavy candidate under q>=3u. Section 1 supplies completeness. R284FE two-group Gray construction attains 4q+8u+2, proving the formula.

## 3. Exact finite result q=5,u=2

Enumerate every nonnegative seven-type histogram with total 0..37 (including all possible widths after constant deletion). Number C(44,7)=38,320,568. Two diagonal separation checks retain 3,891,030, and the four GE1 tests retain 315 (312 two-heavy, 3 nonheavy). For each retained histogram use the exact R284GE/R284FT fixed-order prefix test, with changing-type attempted counts as a mixed-radix monotone lattice. At each reachable node test all success counts obtained by allocating at most 5 current omissions among the attempted types; no third-phase read is allowed.

For a third comparison j and each successful-overwrite count s_p (zero for unchanged types), a differing unwritten coordinate has access to its source or comparison last-change slot; a differing overwritten coordinate has only its comparison slot. The exact distance is max over all 256 subsets U of the eight labeled slots of contained demand minus q|U|. This is the same integral capacitated cut as R284FM/FT/GE. The program precomputes affine cut forms in s, dropping only forms whose global maximum on the full success-count box is <=2u. The attempted-count lattice is exact since coordinates of a fixed type are exchangeable; all predecessors decrease one count, and mixed-radix indexing is topological. A prefix is admissible iff both third comparisons have distance >2u for every allowed omission allocation. A candidate needs a full safe path on all four edges.

Actual C++17 run: 159 candidates fail edge 0; remaining 156 fail edge 1; zero pass. 17,295 attempted lattice nodes considered, 17,295 unique per-edge success-count evaluations (memoized). Therefore no valid code of width <=37; repeated Gray attains 38. Three nonheavy survivors of the necessary conditions have (x3,x5,x6)=(12,12,13),(13,11,13),(13,12,12), all others zero. All are also excluded by the prefix test.

Program and full source readback: f50588b020106368b09965c987b12cdfe6ad2381:research_notes/portable_direct/R284GI_q5_u2_finite_prefix.cpp. Run g++ -O3 -std=c++17 without NDEBUG, then execute. Actual local implementation had identical operative statements (only two comments differ from the published version).

## 4. Exact new obstruction to the next proof route

For q=3u-1 and every integer u>=2, take x3=x6=7u-1, x5=6u-1, all other types zero. Width 20u-3=4q+8u+1. Neither x3 nor x6 nor x5 reaches 2q+2u=8u-2. Each adjacent edge has two source groups of sizes 7u-1 and 6u-1, so their total overflow is 7u=q+4u+1. On either diagonal the sum of the four edge types is 14u-2>=4q+2u+1=14u-3, giving a four-vertex separating cut. Thus this is an exact integer counterexample to extending the six-condition two-heavy implication to q=3u-1, not a counterexample to the full sharp capacity formula. For u=2 it is the (13,11,13) finite excluded case. Next investigate the pure-three-mode family and additional mixed candidates on q=3u-1 with the full third-phase prefix condition or a direct three-heavy witness. Do not just repeat the nonheavy completeness proof at that boundary.

## Frozen sources and control scope

- R284GH c3617898cea2157702d79e68ee0117cd333cd310:research_notes/portable_direct/R284GH_SHARP_BOUNDARY_Q4U_MINUS1_20261124.md.
- R284GG 32c7e5c164557424558fc6128503d17e232e7dad:research_notes/portable_direct/R284GG_ALL_U_HIGH_OMISSION_SHARP_CAPACITY_20261124.md.
- R284GE a112519ea319ef0e0bdf10ee01d817e10fd3dcd5:research_notes/portable_direct/R284GE_EXACT_ADJACENT_ROLLBACK_CAPACITY_20261124.md.
- R284GF 85801535d3b34cca713f28703b4984baf80975f3:research_notes/portable_direct/R284GF_UNIFORM_TWO_HEAVY_DIAGONAL_BARRIER_20261124.md.
- R284FM 1d1c5dd412719c7aaf016187b6493b77253cd9f9:research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md.
- R284FT and R284FE frozen sources as identified by GE and GG.
- Owner read r1-20261124-0600-r284-boundary-owner-read SUCCEEDED, snapshot INV-ec15f1d66f5e2f522545ace537f73e8d (as of 2026-11-23T22:04:06Z), LEASED filter empty; source advanced before completion, no execution authority. Prior RA-B82240E8488EF5A1DA5186C4 is provenance only until own current session possession is confirmed. Initial em_status returned BACKEND_IDENTITY_CHECK_UNAVAILABLE (operation_sent=false). Research is independent new non-overwriting portable material, not protected task-state mutation.
