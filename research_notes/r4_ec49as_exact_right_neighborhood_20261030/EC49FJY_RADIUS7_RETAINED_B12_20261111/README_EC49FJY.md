# EC49FJY — exact B=12 retained-key radius-seven native-BRC optimum

Date: 2026-11-11. Status: author-side exact finite theorem, independently checked by literal-word enumeration on all background classes; independent Driver review pending. Immutable scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.

## Theorem: 16,040 new sharp 94-prefix subproblem optima

Fix either original EC49FGJ witness A or B: 24 distinct labeled BRC observation demands, exactly seven full raw cache-key identities, and 94 distinct nonempty **ordered, signed six-axis native microstep prefixes**. Choose seven labeled word positions Q for replacement and leave the other 17 original words unchanged. Let F(Q) be their literal prefix union and K(F) their full cache-key set. Consider exactly the Q for which K(F) retains all seven original keys and |F(Q)|=81. The incremental budget for a 93-prefix construction is B(Q)=93-81=12.

The complete 24-choose-7 census gives 346,104 seven-position subsets per witness, 153,408 of which retain all seven original raw keys. Among those, 8,020 per witness have B=12. They form exactly ten distinct deleted-prefix (equivalently fixed-F) classes per witness, of sizes 934 eight times and 274 twice. All 16,040 targeted subproblems have **minimum total native-prefix cost exactly 94**.

For witness A, 7,746 selections are excluded by two-label union certificates, and 274 require a three-label union certificate (the tenth background class). For witness B, all 8,020 selections are excluded by two-label union certificates. The original witness paths give a legal 94-prefix solution for each fixed background, making each lower bound sharp.

These B=12 selections are disjoint from EC49FJU–FJX. Cumulative retained-key radius-seven certificates become 113,316 per witness, 226,632 across both profiles; 40,092 retained-key contexts per witness remain, together with 192,696 contexts per witness releasing at least one original key.

## Finite proof

Each pinned legal nine-state BRC operation word w has a labeled demand ell(w), a literal signed-prefix set P(w), and a **complete raw** cache key k(w). For a fixed prefix-closed F, define:

A_F(ell,12) = { P(w) minus F : w is one of the 178,850 legal words, ell(w)=ell, k(w) in K(F), and |P(w) minus F| <= 12 }.

Because the 17 unchanged paths already use seven complete keys, every legal replacement must use an original one. Every hypothetical total-cost-at-most-93 completion must select one member of A_F for each of the seven omitted labels. Any single word with more than 12 new prefixes cannot be in such a completion.

For each of the ten distinct F classes per profile, EXACT_SUMMARY_EC49FJY.json names either two or three omitted labels shared by every seven-position Q in that class. The direct full-catalog verifier enumerates **all** budget-eligible raw BRC words for these labels (no prefix-set antichain, endpoint quotient, or sample-based pruning), forms the literal union for every eligible pair or triple whose partial union could fit the budget, and finds no union of size at most 12. Thus every completion for every Q in the class has at least 13 additional prefixes. The pinned original witness supplies exactly 13, so the optimum is 81+13=94.

The selected labels, group sizes and complete-catalog eligible word counts are in EXACT_SUMMARY_EC49FJY.json. Nine background classes for each profile have two-label certificates; witness A's tenth class has a triple, and B's tenth class has a pair. Crosschecks: an independent prefix-antichain solver obtained the same 20 obstructions, and direct raw-word enumeration confirmed all 20.

## Reproduce and evidence

The executable VERIFY_EC49FJY_PORTABLE.py is published alongside this proof. It uses the unmodified frozen EC49FGW generator and the exact A/B witness JSON **already published in this PR**, at sibling directory EC49FGW_RADIUS5_EXACT_SCREENS_20261110/. Place those two inputs in an EC49FJR subdirectory beside the verifier and run Python 3. The checker asserts 178,850 legal words, 94 raw keys, 9,838 allowed seven-key words per witness, 8,020 B=12 contexts and ten complete background classes for each profile. It checks that each stated obstructing pair/triple belongs to every omitted-label Q in the associated class and then enumerates all eligible raw-word unions. Success line: EC49FJY_ALL_16040_EXACT_PASS. It writes EXACT_REPORT_EC49FJY.json with the checked group records.

During this research turn, the complete scientific generator and exact A/B witness words were independently transcribed from the immutable GitHub references into an executed local script. That script checked native word legality, end-cell displacement, all keys and prefix counts. The direct verifier ran successfully against this equivalent transcription; the above publication path reuses the original checked source files and is independently reproducible.

The full local evidence bundle also includes the exhaustive local B12 singleton, pair/triple antichain programs, the direct-check program, executed JSON reports and captured source-scope explanation. SHA-256 in the bundle describes bytes, not a formal mathematics admission.

## Next

Study retained-key radius-seven B=13 (8,564 contexts per witness) with exact group-wise joint unions and full-key-aware dynamic programming for key-releasing contexts. The global mother question C_min(7) ?= 94 stays open. No current EC49AS formal CLAIM/Result is asserted; review and task admission remain governed by their own native controls.
