# EC49FRK — Exact evidence and recovery index (2026-11-17)

Scientific parent: EC49FRJ [PR #2624](https://github.com/awdawmip/enterprise-math/pull/2624). Frozen original scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. The native response table retains all 141 complete named profiles, 310 configuration multiplicities, 144 terminal and 84 root original physical queries.

## Verified new author result

* Original full terminal signatures: 139 equivalence classes; 137 singletons, residual pairs [8,139] and [46,140].
* Exactly 9868 of the C(141,2)=9870 named-state pairs are terminal-distinguishable.
* All C(144,3)=487344 three-terminal fixed physical query palettes were enumerated using exact bitset unions. Their maximum coverage was 9866/9868 distinguishable pairs.
* Four terminals [31,36,102,142] cover all 9868/9868 such pairs. **Four is the exact minimal nonadaptive fixed terminal palette cardinality** for preserving the original 139-class terminal-equivalence partition.
* Adding original physical root query 148 after those four queries, only when terminal responses leave one of the two residual pairs unresolved, identifies all 141 original named profiles. Root is queried only on profiles 8,139,46,140. Worst-case five total observations.
* Exactly 144/144 single-terminal deletions preserve the 139-class equivalence partition.
* Exactly 16/84 root physical observations, IDs 148 through 163, when **hypothetically re-priced as terminal** with original responses unchanged, remove both residual terminal collisions; all remaining 68 retain the two collisions.
* A general exact weighted terminal-fiber Bellman decomposition is proved in the theorem: the minimum total weighted root-query count in any finite static-response identifying tree equals the sum of the minimal root-only Bellman costs of each terminal equivalence fiber, for **arbitrary positive weights**. Here the exact aggregate root counts are 4 for both uniform and original multiplicity-weighted measures. For prior p_i(lambda)=(1-lambda)/141+lambda*m_i/310, the price slope floor is 4(1-lambda)/141+4lambda/310.

## Original data provenance and locally executed evidence

Original source master SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e.

Original named-profile CSV SHA256: a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f.

The delivered **self-contained** evidence archive is named EC49FRK_FOUR_QUERY_PALETTE_WEIGHTED_FIBER_FULL_EVIDENCE_20261117.tar.xz. Archive bytes SHA256: **966589660bd1a72a0e32a29b545c72cb6b8808dbdbee0720759f9797bcb1e493**; size **195760 bytes**. It was unpacked anew; all **8 manifest files** matched original byte length and SHA256; its original native response loader and EC49FRK verifier were executed again from the unpacked archive with all checks PASS. The exact JSON derived certificate SHA256 is **97f436205728edf530da9ba9c6bbf3b6d91789e3c294f90edc2d0f638c4db69d**.

Archive contents include the complete theorem text and README; original 9.6 MB master and 1.5 MB original profile table; exact native source response reconstruction Python; independent fixed-terminal-palette verification Python; generated exact JSON certificate; execution log; and full manifest. **The archive is delivered as a conversation artifact, not represented as having been uploaded as a GitHub binary blob.**

The repository includes a separately inspectable textual theorem and exact executable checker at research_notes/portable_direct/EC49FRK_MINIMUM_TERMINAL_PALETTE_VERIFY_20261117.py. For local reproduction place the checker in a code/ directory with the prior EC49FRJ native response reader, and the two original frozen source files in source/, then run python code/EC49FRK_MINIMUM_TERMINAL_PALETTE.py (the archive supplies that already assembled layout).

## Scope and open work

New conclusions concern exactly the frozen static named-BRC observer model; the universal Bellman decomposition concerns any **finite static-response** state/query system with individually positive weights. Re-priced-root sensitivity is a labeled counterfactual; no alteration of the frozen source is claimed. No theorem acceptance, active Task claim, native Result/Review or protected Source Activity mutation is asserted.

Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Next: mixed-cost minimal fixed palettes and root-floor-constrained adaptive terminal-count Pareto frontier.
