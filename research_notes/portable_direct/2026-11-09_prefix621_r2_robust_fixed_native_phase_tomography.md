# PREFIX-621-R2 — Sharp erasure/corruption-robust fixed native BRC phase tomography

Date: 2026-11-09 (Asia/Shanghai). AUTHOR-SIDE EXACT PROOF AND EXECUTED ORIGINAL STAR/BRC RATIONAL CHECKER; independent Driver review pending.
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Reuse: PREFIX-617 full48 eight-state positive intertwiner (`00cdf3bcbea94aaa623e8b3e969f2354a5bfd21e`) and PREFIX-620 terminal sensor theorem (`a1192e0e5dd0a0f59f4d6a18571f8aab006c0410`). Actual method reuse: REUSE_APPLIED. Behavior rules read separately from current main; no change to P000, ACTIVE worldview or frozen scientific pin.

## Exact model and observer scope

For the original native X6 STAR/BRC phase-sum transition Q(g) with native weights (1,1,1,1,0,0), four-point difference input d=e4+e11+e14+e32 (zero-based phase coordinates), unknown a,b,q_i>=0 and unknown lambda>0, consider

    x_t = lambda Q(q_t) ... Q(q_1) Q(b) Q(a) d.

The terminal time t is known. A sensor reads one specified original phase coordinate; a fixed set cannot depend on t. An erasure deletes a known coordinate's reading; an arbitrary corruption changes one unknown coordinate reading. The demanded output is the **complete 48-phase sum vector x_t**. For sharp *lower bounds* take t>=4, at which time five independent positive parameters can vary in an open neighborhood. The constructive sensor sets work for all t>=0.

The previously proved eight-state representation is

    x_t = H_C c_t + H_B w_t,
    c_t = theta (e_{(t+2) mod4} + e_{(t+3) mod4}),
    theta = 4*2^t*lambda >0.

For t>=4, the four positive entries of w_t can be varied independently by four different residue-class gate parameters, holding earlier parameters fixed, while lambda controls theta. Thus the five-dimensional positive-parameter family contains an open set.

The exact original phase rows and coefficients in H are:

| state | original phase rows | nonzero coefficients |
| --- | --- | --- |
| C0 | 2,3,15 | 1,1,1 |
| C1 | 5,28,29 | 1,1,1 |
| C2 | 27,38,39 | 1,1,1 |
| C3 | 16,17,41 | 1,1,1 |
| W0 | 3,14,15 | 1,1,1 |
| W1 | 17,40,41 | 2,2,2 |
| W2 | 26,27,39 | 4,4,4 |
| W3 | 4,5,29 | 4,8,8 |

The four disjoint W-support groups are G0={3,14,15}, G1={17,40,41}, G2={26,27,39}, G3={4,5,29}. Pure W rows are 14,40,26,4 respectively; pure C rows are 2,28,38,16 (C0,C1,C2,C3). All remaining 32 native phase rows vanish on this family. At each time residue exactly two adjacent C-columns are active. All mixed members in a given W group share the *same ratio* of C to W coefficients.

## Theorem 621.1 — one erased reading, exact minimum 8

For t>=4 the minimum number of **fixed distinct phase-coordinate sensors** that reconstruct every 48-phase terminal output after any one known erasure is 8. The following single fixed set works at every t>=0:

    S8 = (3,4,5,14,17,26,27,40).

**Proof of lower bound.** Every Wj has exactly three possible phase rows, disjoint from the other W groups. If at most one member of some group is sampled, erase that member: the remaining map loses the independent Wj direction in the reachable five-dimensional open set. Hence at least two sensors per W group are necessary, giving 8.

**Construction.** S8 samples the W-only row plus one mixed row from each W group. Erasing one row leaves at least one reading per group. There are two active C groups at any t. At most one pair has a missing row, leaving at least one intact active W-only+mixed pair. Its difference uniquely gives theta, using the displayed coefficients. Substituting theta back into one surviving reading per W group yields all w_j, hence all 48 x_t entries. This proves the all-t assertion.

## Theorem 621.2 — two erased readings, exact minimum 14

For t>=4 the minimum fixed sensor count for uniform exact recovery after *any two known erasures* is 14. One all-t witness is

    S14 = (2,3,4,5,14,15,17,26,27,29,38,39,40,41).

It consists of every one of the 12 W-group rows and pure C0 and C2 rows (2 and 38).

**Lower bound.** If a W group has fewer than three sampled rows, the adversary can erase all its readings using at most two erasures; Wj is then unobserved. Hence all 12 W rows are mandatory. A set of at most 13 phase rows adds at most one pure C row (or zero/uninformative rows). Choose a time residue r where that pure C row is inactive. Now erase the W-only rows corresponding to the two active C groups. In each active group its two remaining mixed rows have equal C:W ratio, and all other surviving rows are blind to theta. The remaining observation rank is exactly 4, so a nonzero kernel displacement can be chosen small enough to stay inside the reachable positive parameter open set and changes full x_t. Thus 13 is impossible.

**Construction.** After two erasures each W group still has at least one reading. The active C pair contains exactly one of C0 and C2. If its pure C sensor survives, theta is immediately known. If it is erased, at most one other sensor is erased, so at least one of the two active W groups still possesses a W-only reading plus a mixed reading, from which theta is reconstructed. If both pure C sensors are erased, all W rows survive and likewise determine theta. Then one surviving row per W group recovers w and all 48 phase sums. Therefore every 14 choose 2 deletion and every residue yields rank 5.

## Corollary 621.3 — one arbitrary unknown-location corrupted reading

The S14 observation code has coordinate Hamming distance >=3: removal of *any two* rows is injective on its five-dimensional state family. Therefore a received 14-vector with one arbitrarily corrupted coordinate has a unique compatible codeword at coordinate distance <=1, and exactly recovers all 48 native phase sums. One exact decoding algorithm tries each possible incorrect coordinate, solves the remaining linear equations over the rationals, reconstructs the original 14-vector and accepts candidates with <=1 mismatch. The distance guarantee gives uniqueness. This is algebraic correction, not noisy sampling or numerical conditioning.

## Corollary 621.4 — three erasures impossible in this sensor class

Each independent Wj enters only three native phase coordinates. Even reading every original phase coordinate once, erasing those three locations removes the entire Wj direction at t>=4. Hence no fixed *distinct-coordinate* configuration (including all 48 rows) gives uniform recovery under arbitrary 3 phase-coordinate erasures. Repeated physical replicas or stronger labeled Port measurements are different observer contracts and may provide alternate constructions.

## Executed exact native checks

Accompanying standalone Python checker reconstructs all 48 signed STAR phases and exactly 96 nonzero native phase-sum transitions. It tests Q(g)H=H M_8(g) at g=0,1 over all 8 basis columns and all 48 rows: 768 exact coordinate equalities; gate-affinity proves it for every g. It uses rational Gaussian elimination, no floating-point tolerance, to exhaust the four time residues and all single erasures of S8 (32 rank-5 cases), all double erasures of S14 (364 rank-5 cases), and rank-4 obstruction choices for 12/13 rows. It executes 24 original gate-word trials with zero and fractional parameters (1152 full48 native output comparisons), 2376 erased sensor reconstructions, and 56 deliberate rational one-coordinate corruption decodes. **Every executed assertion passed.** Infinite-horizon validity rests on the symbolic intertwiner and exact group/rank proof, not on finite tested lengths.

Companion `PREFIX621_R2_native_phase_robust_sensors_results.json` records the exact finite cases. The raw standalone code is `PREFIX621_R2_native_phase_robust_sensors_checker.py`.

## Research continuation

The established fixed-sensor cost/fault frontier for this four-point BRC probe is 6 rows without erasure (PREFIX-620), 8 rows for one erased reading, 14 rows for two erasures or one unknown corrupted reading; four time-aware calibrated sensors or 3/4/5 time-aware uncalibrated sensors retain their own earlier exact scopes. Next, build an original native 96-port six-action history-state pair with equal 48-phase sums but differing allowed future tagged outputs, using PREFIX-544 exact port composition and PREFIX-561 port action bijections. Classify additional port-origin repair information and its bit/compute cost. Alternatively derive finite-resolution error-amplification bounds for S8/S14. No independent Driver review, formal CLAIM, Native Result, or Foundation promotion is asserted here.
