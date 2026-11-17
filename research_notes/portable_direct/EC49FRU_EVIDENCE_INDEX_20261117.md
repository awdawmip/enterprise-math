# EC49FRU research evidence / reproducibility index — 2026-11-17

**Original frozen scientific pin:** fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Native BRC category 16943, original 310 configurations / 141 complete named states / all 228 distinct *physical* observations (no quotient removal). Parent EC49FRS–FRT: [GitHub PR #2648](https://github.com/awdawmip/enterprise-math/pull/2648) at 4f745adfb05c8dea4e4436cc24ecc4832870aeaf.

**New proven result:** the exact all-real four-coordinate optimal cost for surcharging original physical terminal observations q32,q34,q140,q142 independently, for all nonnegative real prices (a,b,c,d), is

\[
V/t=\min(296/141+a,\ 296/141+b,\ 298/141+c,\ 298/141+d,\ 299/141).
\]

Five fixed original full native identifying trees are necessary and sufficient to cover all four-dimensional positive price regions. Exact finite Bellman anchors on the two-pair diagonal plus analytic concavity and monotonicity prove the continuum theorem; six full native trees have been re-played over all 141 states.

**Research files:**

- [Complete theorem, proof and exact scope](EC49FRU_FOUR_INDEPENDENT_PRICES_EXACT_PARETO_20261117.md)
- [Full original-native Bellman and witness-tree replay verifier](EC49FRU_FOUR_INDEPENDENT_NAMED_SURCHARGES_VERIFY_20261117.py)
- [Independent original native-data Bellman implementation](EC49FRU_INDEPENDENT_ORIGINAL_NATIVE_ANCHORS_20261117.py)
- [Compact 12-case machine certificate with all 3 independent proof anchors and six witness SHA256 digests](EC49FRU_FOUR_PRICE_MACHINE_CERTIFICATE_20261117.json)

**Reproduce:** Extract the preceding EC49FRS–FRT complete original-BRC source archive, place the verifier scripts into its code/ directory, then run both scripts. All 228 observation response vectors are compared across the original two source-reconstruction modules with the native root-key alignment; each exact Bellman case covers 13,063 reachable subset states. Raw master SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e; original profile CSV SHA256 a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f.

**Full self-contained machine evidence (separate user-facing archive):** EC49FRU_FOUR_INDEPENDENT_PRICES_COMPLETE_EVIDENCE_20261117.tar.xz; SHA256 **0e29cab4e7dcab782d4b6293391adb748ad07e586324a687aa1bbde0f2f2dc0b**. The archive includes 58 inherited/new files plus hash manifest, including original full data, all complete decision trees, two independent source reconstruction routes, exact Bellman programs and results, full proof and prior scientific sources. GitHub stores the proof, verifier code and the compact certificate; the user's separate archive stores the raw source and all original full-tree JSON witnesses.

**Status:** AUTHOR_PROVED / EXACT_FINITE_BELLMAN_CHECKED / NOT_REVIEWED. Independent portable mathematical material; no formal Source CLAIM, Result, Review or Activity checkpoint is asserted here. Current Task publication availability is to be read from actual Source control, independent of the GitHub archive. No P000 modification and no change to frozen original scientific input.

**Next frontier:** introduce a fifth independently priced named original physical query such as q46, prove or refute persistence of this five-tree Pareto menu, and locate the first additional exact affine-incidence vertex if it appears.
