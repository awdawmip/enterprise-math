# X6 signed rotations: temporal depth observability and six-phase stroboscopic aliasing

Status: DRIVER_MATHEMATICAL_AUDIT / EXACT CANDIDATE ALGEBRA / NOT_NATIVE_RESULT_ADMISSION
Date: 2026-11-12 (+08)
Tasks: RS-X6-NATIVE-TIME-DYNAMICS; RS-X6-NATIVE-ROTATION-DYNAMICS
Contribution: New Driver theorem on finite time-ordered observations, extending previous Driver depth-repair and signed-triad group proofs. Earlier native X6 spatial, BRC, and observer authors retain their authorship. A shared Driver proof is not an independent Native Review.

## 1. Model and exact question

Use the native chart-relative signed Cell torsor G=Z^6, diagonal D=(1,1,1,1,1,1), and min-zero observer q(z)=z-min_i(z_i) D. Every state has a unique decomposition z_0=r_0+h_0 D with r_0=q(z_0) and h_0=min_i(z_0,i).

Fix an ordered list of registered candidate spatial update events:

    z_t = g_t z_(t-1) + u_t,  1 <= t <= N,

where each g_t is a signed permutation in B6 and each u_t is a known Z^6 displacement, optionally a signed primitive unit step. Define G_0=I, b_0=0, G_t=g_t G_(t-1), b_t=g_t b_(t-1)+u_t. Hence z_t=G_t z_0+b_t. Only b_t modulo ZD needs to be registered. The finite index t denotes ordered events; it imposes no physical clock or heartbeat calibration.

Given initial min-zero readout r_0, the registered operators G_t and accumulated displacements b_t modulo ZD, and a subset of later readouts r_t=q(z_t), ask whether the initial integer common depth h_0 can be recovered exactly. This is a candidate Cell-automorphism experiment rather than a proof that every signed permutation is an admitted physical rotation.

## 2. Theorem 1: finite-trace observability criterion

Let S be a nonempty subset of registered sampling times, and define epsilon_t=G_t D, a vector with six signs.

The following conditions are equivalent:
(1) For each fixed r_0, the map h_0 in Z -> (r_t) for t in S is injective.
(2) At least one sampled t has both +1 and -1 in epsilon_t.
(3) At least one sampled prefix G_t fails to preserve the diagonal subgroup ZD.

If the conditions hold, pick a sampled t and output coordinates p,n with epsilon_(t,p)=+1, epsilon_(t,n)=-1. Then exact recovery is

    2 h_0 = (r_(t,p)-r_(t,n))
            - [(G_t r_0+b_t)_p-(G_t r_0+b_t)_n].

Only a single signed coordinate difference from the later readout is needed once r_0 and the registered event maps are known. The expression must be an even integer in valid exact data, a useful consistency test. If all sampled prefixes have uniform signs, the entire sampled relative trace is independent of h_0.

Proof: Substitute z_0=r_0+h_0 D into z_t=G_t z_0+b_t to obtain z_t=G_t r_0+b_t+h_0 epsilon_t. Subtracting the min removes only a common scalar, preserving pairwise differences. For opposite-sign p,n the difference has coefficient 2 on h_0; rearrange. For uniform epsilon_t=sD, q(v+h_0 sD)=q(v), so each measured r_t is independent of h_0. A signed permutation descends to Z^6/ZD precisely when its image of D is plus or minus D. These prove necessity, sufficiency, and the equivalence. QED.

The theorem is about **retrospective recovery with a later readout**. Predicting that readout from r_0 alone is a distinct information-budget problem.

## 3. Theorem 2: sharp six-phase C6 sampling effect

For the earlier ordered-triad candidate R_123, define

    R(z1,z2,z3,z4,z5,z6)=(-z3,z1,z2,z4,z5,z6).

R has order six. Its powers act on D by the following exact sign vectors:

    t=0  (+,+,+,+,+,+)
    t=1  (-,+,+,+,+,+)
    t=2  (-,-,+,+,+,+)
    t=3  (-,-,-,+,+,+)
    t=4  (+,-,-,+,+,+)
    t=5  (+,+,-,+,+,+)
    t=6  (+,+,+,+,+,+)

The sequence repeats modulo six. Thus sampling exclusively at t divisible by six loses all information on the original common depth. Sampling at any one registered phase t not divisible by six recovers that depth exactly from r_0 and r_t by Theorem 1.

Concrete witness: z_0=(0,0,0,0,0,0) and z'_0=D have identical r_0=0 and identical readouts after any integer number of complete C6 cycles, but at phase t=1 their readouts are 0 versus (0,2,2,2,2,2), and at t=3 they are 0 versus (0,0,0,2,2,2). Phase-separated observation is strictly more informative than whole-cycle stroboscopic observation for this prescribed action.

The same criterion and inverse formula apply when primitive displacements u_t occur, provided the ordered displacements (or resulting b_t modulo ZD) are known. In particular, full endpoint return after a complete cycle need not imply equal phase-labelled event records. Unknown or state-dependent microsteps remain part of the unresolved state and are not assumed known by the theorem.

## 4. Theorem 3: optimal predictive side-channel for finite-depth ensembles

For a fixed registered path, fixed r_0, and finite nonempty admissible set H of possible h_0 values, consider predicting the sampled relative trace before observing future r_t. If some sampled prefix has mixed signs, distinct depths in H yield distinct traces. Exactly |H| labels, or ceil(log2 |H|) fixed-length binary bits, are necessary and sufficient to encode the depth information for those readouts. If all sampled prefixes have uniform signs, exactly one label (zero bits) suffices. The proof follows from Theorem 1's injection/constancy dichotomy and an index code for H.

The previously proved unrestricted signed-primitive-word exact-length-M interval I_(r_0,M) supplies one such finite set only under that earlier theorem's parity and unrestricted-step hypotheses. No nonbacktracking or triadic-force admissibility follows automatically.

## 5. Exact computational checks and research lineage

The algebra above is universal under its stated hypotheses. Supplementary exact integer checks:
- Seven phases of R^tD and 3,000 seeded integer initial states at each of t=0,...,6, matching the quotient identity, mixed-sign inverse and uniform-sign invisibility.
- 2,000 seeded arbitrary signed-permutation / signed unit-increment paths, eight time prefixes each, 16,000 exact tests: 15,527 mixed-sign recovery cases and 473 uniform-sign readout-invisibility cases; zero mismatches.

Source provenance and original authorship: definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md at a72226e2430ffa4786321ac86e7f0c599d5f0389; definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json; definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json; prior Driver notes 2026-11-12_x6_signed_triad_c6_group_and_brc_path_fiber_action.md and 2026-11-12_x6_signed_rotation_relative_observer_depth_descent.md. The current time and rotation Tasks remain active questions, with no new Native Result acceptance, task closure or mother-objective closure conferred by this mathematical note.

## 6. Next discriminating unit

Construct a genuinely typed BRC-path and triadic-force transition having the registered affine spatial component, or provide a counterexample to its admissibility under the original frozen carrier. Explicitly determine which microsteps and forces are state-dependent. Compare full phase-labelled traces against six-step stroboscopic sampling for the same admissible history; preserve ordered branch identities, multiplicity and time/force state. Verify actual carrier realization for the selected triad instead of inferring it from arbitrary coordinate selection.
