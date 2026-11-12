# EC49FMJ — 400 more exact three-key-replacement BRC/X6 prefix optima

Date: 2026-11-12. Researcher: **EM-DIRECT-C78DFA**; registered native research activity **RA-766725EB2D88F5B3B179B28A**. Native Task publication and CLAIM remain unavailable for RS-EC49AS; author-side scientific evidence is published in the existing Draft PR. No independent Driver admission. Frozen nine-state BRC science pin: **fc0f038e7bfd12c886b4d37f900bfb770c0f61ab**; P000 / ACTIVE worldview unchanged.

## Domain and exact result

Use precisely the original 178,850 lawful nine-state BRC operation words, 94 **complete raw cache keys**, 24 exact observation demands and literal **ordered signed-X6 native microstep prefixes**, as in EC49FMI. The baseline seven-key 84-prefix construction is:

K*={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}.

Among all C(7,3)C(87,3)=3,709,825 distinct exact three-key replacements, exactly 38,169 satisfy the full 24-label support-union condition. Index these **coverable** sets from zero in the original sorted drop-triple/add-triple nested-loop enumeration. Let C(K) be the exact minimum cardinality of the union of *nonempty literal ordered signed native microstep prefixes* from valid words satisfying all 24 demands with only the seven full keys in K.

**Exact finite theorem (EC49FMJ):**

\[
\boxed{\min_{600\le i\le999} C(K_i)=110},
\]

attained exactly at indices **865, 871**, with range [110,168] among all **400** specified instances. They have exact retained full-key index tuples respectively [0,4,5,6,7,8,36] and [0,4,5,6,7,15,36] in the 94-key frozen sorted catalogue. Both have three distinct first signed-native roots.

Combining with the exact prior **EC49FMI** indices 0..599 (minimum 102 at 32,93) gives the new contiguous **1000-instance theorem**:

\[
\boxed{\min_{0\le i<1000} C(K_i)=102}.
\]

The first 1000 are a precisely specified finite subset of the 38,169 coverable radius-three configurations. The global seven-key mother problem retains the known constructive upper bound C_min(7)<=84; its exact optimum remains open.

## Proof mechanism and executed checks

The complete frozen source generator gives each legal word's full cache key, label and literal signed-native path. Per-key 24-bit support masks classify all three-key replacements by exact OR. For each supported seven-key set, include every legal operation word with that key. Partition word paths by their *first signed microstep*, which defines pairwise prefix-disjoint rooted tries. Every trie node has an integer min-plus DP over exact unions of demand-label bitmasks, combining child subtrees additively and charging one for each selected nonempty prefix. At each root compute the least cost for every demand mask, allowing extra demands through the superset transform. Minimize the sum of exact root costs over allocations of the 24 demands to capable roots. Every legal witness induces one DP allocation, and every finite optimal allocation has legal witness words, proving equality to C(K) by induction and converse construction.

**Actually executed this run**: the same previously checked C++17 signed-native-prefix cached solver used in EC49FMI, with only its expected input-case count changed 6315 to 38169 and mathematical DP unchanged, computed the complete uninterrupted integer block 600..999 from the *same* immutable master input SHA256 **cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e**. The solver emitted exactly 400 consecutive ordered lines and completed with an explicit FINISHED log.

The separately written original noncached C++17 prefix solver recomputed four selected complete cases: **600=167, 865=110, 871=110, 999=138**, in agreement with all cached outputs. A structurally independent Python standard-library native-prefix trie DP, run with the original frozen generator rather than the C++ solver's per-node tables, recomputed **those same four cases** with identical minima. The four tests span 3-root and 4-root inputs and include both global local minima.

In the block, **183** instances have three first-step roots and **217** have four. The complete histogram and compressed vector are in EXACT_VECTOR_EC49FMJ.json. Lossless exact raw 400-byte SHA256: **cbb479d4d6161571888a582fff9a543d628e6cc74761b8ab7425745d72647e32**. Full 400-line solver output SHA256: **d14cabd564049a1323b0cc5db2e64b5eab54b72ac4fd6bcb4f44feea8333e2bd**. No floating-point comparisons or solver optimality assertions are used.

## Reproduction, source and next unit

- Existing EC49FMI/BUILD_EC49FMI.py exhaustively rebuilds the full 38,169 supported three-key indices and the native C++ master input from the frozen EC49FGW generator.
- This directory's EXACT_VECTOR_EC49FMJ.json preserves all new 400 optima with zlib/base64, complete histogram, checks and SHA256s.
- VERIFY_EC49FMJ.py checks lossless vector/digest/histogram and crosschecks adjoining 600 entries from EC49FMI to prove contiguous 0..999 coverage. Its optional --solve argument recompiles the already-published cached C++ engine and recomputes all 400 original native-prefix optima from the pinned master.
- The accompanying local research evidence archive contains complete raw 400-case output, runtime log, original noncached input/output, independent Python program/log, frozen original generator, master input and checksums.
- Previous completed exact finite families: EC49FMH radius-two **6,315** configurations with minimum 84; EC49FMC radius-five **1,137** with minimum 114.

**Next unfinished scientific unit:** continue exact radius-three supported indices **1000..38168** (37,169 instances), or prove a useful global-prefix lower bound for a broader family; explicitly test whether any legal seven-key construction can beat the known 84-prefix witness. Radius-four has 62,620 support-coverable configurations. Reuse this established exact finite evidence rather than rerunning completed cases.

**Native Source state:** service session-start successfully registered Researcher EM-DIRECT-C78DFA, Activity RA-766725EB2D88F5B3B179B28A and verified their remote Source records at commit 0872afa37dad9289b88139d4febb14b5b53f50fd. RS-EC49AS exact task lookup returned CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION; no unrelated active owner, CLAIM/open, formal Result or independent Driver admission is asserted. GitHub publication here is author-side evidence, not the formal task lifecycle.
