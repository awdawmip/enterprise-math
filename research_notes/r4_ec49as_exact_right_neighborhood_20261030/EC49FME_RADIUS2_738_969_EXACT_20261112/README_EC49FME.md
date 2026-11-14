# EC49FME — 232 additional exact seven-key BRC prefix minima (radius-two)

Date: 2026-11-12. Author-side finite exact computation. Original frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Not an independently reviewed or admitted Result.

## Exact statement

For the nine-state automaton and original ordered, signed six-axis microsteps, retain all 178,850 lawful words, all 94 complete raw cache keys, and the 24 distinct (window, DFA-signature) demands. Let C(K) be the minimum size of the union of nonempty **native signed-microstep prefixes** of a set of lawful words meeting all demands with complete cache keys confined to K.

Take the seven-key 84-prefix seed of EC49FKX,
`S={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}`.
For each pair of keys deleted from S (lexicographic order), and each pair added from the 87 external keys (lexicographic order), retain the resulting K exactly when its demand-support union contains all 24 labels. This enumerates 6,315 coverable double-key replacements; their zero-based indices and the earlier first 738 optima are fixed in EC49FKZ/EC49FMD.

**New finite theorem:** All **232** configurations with global coverable indices **738..969** have their exact integer native-prefix minima in **[98,112]**. The histogram is:
`98:3, 104:6, 106:6, 108:2, 110:2, 112:213`.
The minimum 98 occurs only at global indices **757, 840, 922**. Of the 232 instances, 136 have three nonempty first-microstep roots, 96 have four. Every case in this block deletes the two keys `(5,3,1)` and `(5,4,1)`.

In particular, no instance in this specified finite block permits 97 or fewer native prefixes. The known 84-prefix witness remains an upper bound for the **unrestricted** seven-key minimum.

## Exact algorithm / finite proof

Enumerate **all** words from the pinned native nine-state generator; preserve each full raw key, the DFA label, and all ordered signed X6 prefixes. For a fixed K, form each first-native-step prefix trie. At each node, a terminal word can cover its demand; combine child demand subset masks by OR and sum their independently optimum costs; count a selected non-root prefix once. Induction on trie height proves exactness for every root's supported demand subset. Distinct first-step roots cannot share any nonempty prefix. Enumerate all assignments of the 24 required labels to supporting roots and take the minimum sum. Thus there is no heuristic search cutoff *inside a completed case*.

The unmodified C++17 exact solver is `EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp`; its frozen-word generator is `EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py`. This run generated the 6,315 coverable keysets in their existing order and produced a full C++ optimum record for each of the 232 indices. All full rows (including allocation multiplicity, roots, and root metadata) are losslessly preserved in `EXACT_VECTOR_EC49FME.json`, with the SHA256 of their newline-delimited decompression bytes.

A separately authored Python standard-library trie/subset DP, not invoking C++, independently checked **738=112** (three roots), **757=98**, **840=98**, **922=98**, and **969=112** (four roots). Results agreed with all five C++ optima. The finite result covers the 232 **completed** instances: the longer 738..1399 attempt was interrupted at the next case, index 970, whose partial line was **excluded**.

## Reproduce

Use `REPLAY_EC49FME.py` and the frozen generator/solver files in the prior cited research directories. It regenerates the entire 178,850-word catalogue and sorted coverable index, checks the stored 232-row compressed vector and hash, and optionally recompiles/runs the exact original C++ solver on exactly these 232 cases. `VERIFY_SELECTED_INDEPENDENT_EC49FME.py` independently checks five designated instances. The source model pin must remain unchanged.

## Frontier / governance

Together with EC49FKZ 0..399 and EC49FMD 400..737, the contiguous coverable radius-two optimum frontier is **0..969**, i.e. **970 of 6,315**. At least 5,345 double-key coverable sets remain unsolved by this contiguous scan; other verified local/distance results remain separately reusable. Next reproducible contiguous case: **970**. Alternative value-oriented route: seek an 83-prefix witness across other radius-two/three/four families, using valid support screens first.

GitHub user `awdawmip` created this author-side computation; native researcher session issuance returned `SESSION_ISSUANCE_QUOTA` and no current matching formal CLAIM was established. This document is scientific evidence preservation, not a task-owner change, Result, independent Driver review, or P000/worldview modification.
