# EC49FMF — 450 more exact native signed-X6 seven-key minima (radius-two)

Date: 2026-11-12. Research mode: author-side, exact finite mathematics; independent Source Driver admission pending.

## Model, theorem, and frozen inputs

Science pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The nine-state BRC automaton has 178,850 lawful operation words, 94 full raw cache keys and 24 (window, automaton-signature) observation requirements. A word is represented by its **ordered signed six-axis native microstep sequence**; cost is the number of **distinct nonempty microstep prefixes** used by chosen lawful words. This preserves path and observation provenance under P000.

Let `S={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}` be the 84-prefix seed's seven keys. Enumerate all sets `K=(S\deleted_pair) union added_pair`, lexicographically by two deleted keys of S and two added keys outside S; retain only the **6,315** sets whose legal-word demand-support union covers all 24 labels. The zero-based index is this fixed coverable-set order from EC49FKZ.

**New finite theorem.** For every coverable double-key replacement with indices **970 through 1419 inclusive**, the exact minimum native-prefix cost C(K) is given by `EXACT_VECTOR_EC49FMF.json`. Across all 450 cases:

- 92: 2 cases (global indices **1376 and 1393**)
- 98: 6 cases
- 100: 2 cases
- 104: 49 cases
- 106: 10 cases
- 112: 381 cases.

Consequently, `min{C(K_i):970<=i<=1419}=92`. All 450 finite instances exclude 91-or-fewer prefix solutions, including the 83-prefix threshold. The two 92-prefix optima have independently reconstructed **explicit 24-word solutions**, present as `witnesses` in the JSON data. Their six-axis signed native prefix unions each contain exactly 92 elements.

## Why the computation is exact

For a fixed full keyset, enumerate all lawful words and build a trie of their nonempty *native microstep* prefixes. Split the trie by the first microstep; distinct roots have disjoint nonempty prefix sets. On each rooted tree, a node's DP records the **least number of selected prefixes** yielding each exact subset of its local observation labels. Terminal words contribute their declared labels, child subsets compose by bitwise union, and every selected non-root trie node contributes one prefix. Induction over finite trie height proves that each local DP is exact.

To combine roots, enumerate all root assignments for the 24 mandatory labels and minimize the sum of the roots' superset-closed DP costs. This is finite exhaustive integer optimization, not a stochastic search or a floating-point optimum report. Every completed case uses the entire legal-word catalogue and every allowed prefix.

The standard verified reference implementation is `EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp`; the frozen generator is `EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py`. `REPLAY_EC49FMF.py` checks the entire persisted vector and the two explicit witnesses using that immutable scientific model. Its `--run-all` mode independently regenerates the full 450-case input, compiles and executes the existing exact C++17 engine, and checks **each** optimum against the JSON.

## Actual verification

A caching extension of the identical exact root-DP equations solved all 450 indices. The output's full newline-delimited original record (including all root metadata) has SHA256 `03f030de7ff545c38832f33a97dcd79cc0593f92c541cb616dd70a26c4668e13`, retained in the local execution evidence bundle. In a second run, the unchanged original engine produced **byte-for-byte identical** output for the first **382** of the 450 cases (global 970..1351), while the remaining 68 were completed by the cached engine. A separately implemented standard-library Python prefix-trie integer DP checked 12 selected cases, including both new 92 minima: 970, 1003, 1083, 1119, 1120, 1162, 1240, 1317, 1376, 1393, 1400 and 1419. The explicit 92 witnesses were independently extracted by Python bottom-up DP with traceback and checked against all 24 native observations and all ordered native prefixes.

The original long run stopped after **300 complete records** for the 1120..2499 requested range; all uncompleted indices beyond 1419 are excluded from this theorem.

## Current research frontier

With preceding EC49FKZ (0..399), EC49FMD (400..737) and EC49FME (738..969), the complete **contiguous exactly solved** radius-two interval is now **0..1419**, i.e. **1,420 of 6,315** coverable configurations; the next global index is **1420**, and **4,895** coverable radius-two sets remain outside that contiguous interval. The previously validated 84-prefix seven-key witness still gives the unrestricted bound `C_min(7)<=84`. A full global lower bound or an 83-prefix witness remains open. Other radius families retain their independently recorded scope.

Current GitHub execution account is `awdawmip`. Source query for EC49AS returned `NO_CURRENT_IMMUTABLE_PUBLICATION`; new service session issuance returned `SESSION_ISSUANCE_QUOTA`. This author-side scientific deposit does not create a shared TASK CLAIM, canonical Result or independent Driver review. P000, the ACTIVE worldview and original science pins remain unchanged.
