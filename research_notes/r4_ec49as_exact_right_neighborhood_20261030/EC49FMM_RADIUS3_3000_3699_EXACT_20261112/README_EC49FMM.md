# EC49FMM — full native BRC seven-key radius-three exact costs, indices 3000–3699

Date: 2026-11-12. Parent: EC49FML (#0–2999), PR #1730. **Science input frozen** at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; never rebase to changing task/control versions. Author-side exact finite computation, not an independently admitted Result.

## Exact finite theorem

Nine-state typed BRC model; 178,850 lawful operation words, 94 complete cache keys, 24 distinct observer demands, signed ordered six-axis native microsteps. Seven-key support-coverable radius-three cases are numbered 0..38168 by the existing frozen lexicographic replacement generator; master stream SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.

For a permitted seven-key set K_i, let C(K_i) be the least count of **distinct nonempty ordered signed X6 word prefixes** needed by a selection of legal witness words collectively satisfying all 24 demands.

**Exact scope and result:** `min_{3000<=i<=3699} C(K_i)=128`, with exact minimizing indices **3408, 3422** and maximum **138**. Cost histogram: 128:2, 129:1, 132:48, 133:3, 134:1, 135:3, 136:4, 138:638. Among the 700 complete cases, 170 have three first-microstep roots and 530 have four. Complete consecutive output was checked for precisely #3000..3699, no missing or duplicate cases.

Combining already verified author evidence from EC49FMI–FML gives `min_{0<=i<=3699} C(K_i)=102`, achieved in the earlier #32 and #93. This cannot establish the global optimum; the already constructed **84-prefix seven-key witness** continues to give only `C_min(7)<=84`.

## Finite exactness and independent crosschecks

For each fixed K_i and each distinct signed first microstep, collect *all* legal witness words from the frozen generator, build the complete native prefix trie, and compute integer DP `mask -> min counted prefixes` bottom-up. Child demand masks combine by bitwise OR and prefix counts by addition; any selected nonempty subtree incurs the present prefix vertex exactly once. Superset closure permits assigned demands to be covered with extras. The outer recursion enumerates each of the 24 demand labels assigned to every eligible first-step root. Every legal word selection maps to one such allocation; each DP allocation yields legal selected words. Thus the obtained integer minimum is exact in this finite typed model, without endpoint substitution, random selection, or approximate numerics.

Unchanged archived C++17 solver and frozen 38,169-case master used in EC49FML; input SHA as above. Run #3000–3199 completed 200 rows. A following process completed #3200–3699, 500 complete rows, and was stopped by execution timeout *before* completing #3700. No partial row enters the theorem. SHA256 of all concatenated 700 native solver rows: `fc7b7bf00a7b8abc1ecabd5c463860f4bbf9b1917f05387f1dbb5f42defe29f8`. SHA256 of the complete 700-byte exact-cost vector: `1729312ccfb44df9737f865cb7f2564f0f7eb1b22fd6f97bebbac4d4db70ae35`.

Independent Python prefix-trie integer optimizer (recreates original 178,850 words from the frozen generator, not C++ DP intermediate states) passed **#3000=138, #3408=128, #3422=128, #3699=138**. These checks cover both minima and both range boundaries, not all 700 cases.

## Reproduction and present limitation

The compressed 700-byte cost vector is lossless in `EXACT_VECTOR_EC49FMM.json`, with full histograms, SHA256 and independent cases. `VERIFY_EC49FMM.py` validates all the published vector commitments and optionally validates raw solver rows if supplied. Reconstruct original legal generator and case order from frozen source and predecessor EC49FML at commit `a43666605351d744570ef34250cdd5765368e166`. Recompute using the source semantics in `SCAN_EC49FML.cpp` with `./scan 3000 3700 < master_and_radius3_cases.txt`. The current-turn evidence tarball additionally preserves exact local source, raw 700-row output, master input, independent verification code and complete SHA256 inventory. Exact byte-level replay requires that underlying frozen master stream rather than an arbitrary current HEAD catalogue.

The native `RS-EC49AS` task query in this turn returned `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION`. No formal CLAIM/Result was claimed and no other owner's work was occupied. Research session registration was queued at the time of this report; a session request is not a registered identity. Next uncomputed index **3700**; 34,469 more radius-three support-coverable cases remain, with global 84-prefix optimum still unresolved.