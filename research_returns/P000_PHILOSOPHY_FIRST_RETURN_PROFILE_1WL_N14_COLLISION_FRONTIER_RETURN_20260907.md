# P000 Q30 — Return-Profile + ordinary 1-WL n=14 collision frontier — terminal return

- Task: `RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N14-COLLISION-FRONTIER`
- Publication: `TP2-8969646E7FF5FB8A9F5D`
- Claim: `CLAIM-P000Q30-20260907T0800Z-CHATGPT-02`
- Researcher-ID: `EM-P000Q30-D67DE2`
- Execution record: `ER-9EF9871C713F5C79FA92`
- Terminal state: `RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N14`

## Result

Under the **bit-for-bit frozen Q22/Q25/Q27/Q28/Q29 observer** — primitive-cycle first-return profile as the initial Cell color, followed by ordinary 1-WL using exact neighbor-color multisets until stabilization — the exact n=14 search is collision-free.

The recovered exact certificate contains:

- 1,267 cubic-kernel types across residual sectors r = 2,4,6,8,10,12,14;
- **56,972** exact graph representatives;
- **56,972** exact anonymous stabilized packets;
- **0** equal-packet nonisomorphic collision fibers;
- **26,406,647,416,800** normalized connected labeled realizations in the seven degree sectors.

Therefore the accepted finite lower frontier extends from n<=13 to **n<=14**, and Q30 terminates. No continuation to n=15 is made inside this task.

## Exact evidence pin

The terminal mathematics is recovered from immutable source commit:

`b90378c332e0dbf80aad0c09d363047abb2ee2f3`

Certificate:

`research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N14_COLLISION_FRONTIER/P000_Q30_RETURN_PROFILE_1WL_N14_EXACT_KERNEL_ORBIT_CERTIFICATE_V2.json`

Git blob SHA-1: `9ed536a327dda4d9d6e3a21d31bb90383bf7ddc9`.

The certificate's exact method suppresses maximal degree-2 paths to connected cubic multigraph kernels, exhaustively expands weak compositions of the 14-r subdivision vertices, rejects precisely nonsimple expansions, recomputes the frozen primitive-return-profile + ordinary 1-WL packet, compares packets by **exact semantic equality**, and closes each sector by an automorphism-weighted orbit sum against an independently evaluated connected degree-state count.

The current recovery audit independently rechecks all seven persisted sector histograms: `sum_G r!(14-r)!/|Aut(G)|` equals the recorded independent count in every sector, and it rechecks all persisted global totals.

## r=14 persistence repair

Certificate V2 names a monolithic persistence file `P000_Q30_N14_KERNELS_R14_V1.json`. That filename is absent from the pinned final source tree and is therefore recorded here as **SUPERSEDED**, not silently treated as present.

The final source tree instead contains the deterministic replacement package:

- `P000_Q30_N14_R14_RECONSTRUCTION_REPLAY_SUPPLEMENT_V1.json` (blob `78c162e4e8d4103ac6fa2bd983153c640de1ced7`);
- five reconstruction shards `P000_Q30_N14_KERNELS_R14_RECON_P1_V1.json` through `...P5...`, totaling 509 representatives;
- `research_checks/P000_Q30_N14_R14_RECONSTRUCTION_REPLAY_CHECK_20260905.py`.

That r=14 replay recomputes primitive-cycle return profiles, full ordinary 1-WL stable packets, automorphism orders and an independent connected labeled cubic count from the 509 persisted graph encodings. It reports 509 representatives, 509 distinct exact packets, 0 collisions and orbit/count total **19,491,385,914,000**.

This repair changes only a stale persistence pointer. It does not strengthen the observer and does not alter the mathematical terminal state.

## Current recovery checker

Run:

`python scripts/check_p000_philosophy_first_return_profile_1wl_n14_collision_frontier.py`

Expected terminal line:

`PASS Q30 n=14 recovery audit: representatives=56972 normalized_connected=26406647416800 stable_packets=56972 collision=0; legacy_r14_pointer=SUPERSEDED`

The current checker is deliberately a **recovery/provenance and exact-arithmetic checker**. It does not pretend to regenerate the 56,972 graphs. Graph-level enumeration/replay authority remains the immutable pinned source certificate and replay code above.

## BRC discipline

This closure preserves the BRC information-loss boundary:

- primitive-return-profile initial colors remain typed data;
- every ordinary 1-WL neighbor-multiset refinement remains part of the observer;
- the anonymous stable packet is compared exactly;
- hashes are used only as integrity pins, never as mathematical identity;
- kernel/orbit coordinates certify exhaustive coverage and provenance, not a stronger observable.

## Boundary

This result proves only exact graph-level injectivity on the accepted `U_BR(n)` prefix through **4 <= n <= 14** for the frozen observer. It makes **no statement for n >= 15** and grants no universal reconstruction theorem, canonical labeling theorem, Working Truth, Foundation, L4 promotion, novelty claim, or permission to substitute 2-WL, spectra, zeta data, full cycle incidence, canonical labels or another strengthened observable.

Driver/independent review is required before merge or promotion.
