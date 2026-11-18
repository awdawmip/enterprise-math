# EC49EXZ — Native exact DP of the remaining 12,356 double-collision schedules

Input: Frozen EC49EXJ native signed X6 operation words and nine-history T2/T4 observer signatures; complete key family H=8/M=5/S<=6; EC49EXY exact cross-fiber signed-prefix cap matrix and 12,356 complete survivor schedule rows. Frozen pins Global `773d538180bfb49e24cffeb35c3ee75eb0628e2e` and EM `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` remain unchanged.

Known: EC49EXX excluded all 123,147 triple-collision schedules at cost <80. EC49EXS excluded all but 44,234 double collisions by coarse BRC histogram prefix cap; EC49EXY improved the cap to exact observer-admissible signed-native LCP, leaving 12,356. This does not close global E*=80.

Next independent unit: scan the exact survivor TSV by minimal native word count and high-bound lower constraints. For each candidate, construct the full typed native trie and solve the integer OR-mask cover with cutoff E<80. Reuse EC49EXJ generator and EXACT_OR_MASK_DP.cpp and EC49EXW/EXX staged seven-window lower bound; cache exact immutable H7 inputs and retain per-case signed observer signatures, case identity, full input hash, stdout and timeout. A successful E<80 requires actual explicit primitive-prefix edge set/witness verified against all required T2/T4 signatures; a cutoff-infeasible result is an individual exact certificate. Deduplicate and publish a finite result batch; do not silently treat timeout as proof.

Source/authority: This is a portable author-side next unit, not a native CLAIM or accepted theorem. P000 and ACTIVE Heartbeat World unchanged. Formal native publication requires live authorized owner/session and independent Driver as applicable. GitHub Draft PR #1730 is the current science handoff surface.
