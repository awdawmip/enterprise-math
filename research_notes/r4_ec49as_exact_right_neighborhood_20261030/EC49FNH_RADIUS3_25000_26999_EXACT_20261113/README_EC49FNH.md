# EC49FNH — 2,000 exact BRC configurations and an eight-prefix root-transfer gap

Date: 2026-11-13. Continuation of EC49FNG PR #2248. Seven-key, radius-three three-replacement configurations **25000–26999**, all under immutable scientific pin **fc0f038e7bfd12c886b4d37f900bfb770c0f61ab**.

## Frozen model and exact computation

The original nine-state BRC catalogue contains 178,850 lawful original operation words in 94 complete cache keys and 24 labelled demands. The cost C(K) is the number of different nonempty **ordered, signed native-X6 microstep prefixes** of a lawful selected-word cover of all 24 labels. The exact C++17 program applies a bottom-up root-prefix-trie subset DP followed by exhaustive allocation of demand labels to permitted first-step roots. Root-specific DP lower bounds and lawful word reconstructions give matching lower and upper bounds for each fixed configuration.

The interval was computed as seven non-overlapping finished C++ runs, with actual FINISHED exit receipts for each slice, covering exactly 2,000 consecutive indices; no result from a stopped run is counted. The lossless 2,000-byte cost vector is included in the companion certificate. The minimum in this interval is **92**, reached precisely at indices **26955 and 26966**; the maximum is **219** (index 26323), with 102 distinct cost values. The previous best for the cumulative radius-three family is **86** at 21524 and 21525 (PR #2243). The unrestricted seven-key mother family independently has an 84-prefix feasible witness.

| Index | Complete cache-key indices | Exact C(K) | Native root-prefix partition |
|---|---|---:|---|
| 26955 | 0,4,5,11,26,32,34 | 92 | root 05:46, root 06:46, root 07:0 |
| 26966 | 0,4,5,11,26,32,46 | 92 | root 05:46, root 06:46, root 07:0 |

Both cases have fully reconstructed 24-word lawful original BRC witnesses. Independent Python trie/subset DP agreed with the C++ optima at indices 25000=162, 26323=219, 26955=92, 26966=92 and 26999=112.

## Finite structural theorem: strict root-07 shadow gap

In each of these two cases, the required labels available at first roots 05 and 06 are disjoint sets L05 and L06, of 12 labels each, with union all 24 demands. Root 07 may receive only the eight labels Q={5,7,11,13,15,17,19,21}. Let f_r(S) be the exact minimum cost of the corresponding root trie needed to cover label subset S, allowing incidental coverage. Every legal first-root allocation is determined by a transfer set T subseteq Q, with total optimal cost

F_K(T) = f05(L05 \ T) + f06(L06 \ T) + f07(T).

For both K26955 and K26966, complete finite root-function tables (4,096+4,096+256 subset values each) establish:

F_K(empty) = 46+46 = **92**;
min over nonempty T subseteq Q of [F_K(T)-92] = **8**.

Exactly one of the 256 transfer masks is zero-margin: the empty set. Any nonempty assignment to the third root costs at least 100. This is a **strict** certificate of uniqueness of the optimal root allocation, not a claim of uniqueness of the selected original words.

Replacing complete cache key **34 by 46** preserves exact cost 92 and the strict margin 8, while the margin functions differ: among the 256 transfer masks, 26955 has a smaller margin on 145, the margins tie on 106, and 26966 has a smaller margin on 5. Thus equality of global optimum and of the exchange gap is compatible with unequal internal root-function vectors.

Proof: the first-root tries have disjoint nonempty prefixes. Each label not sent to 07 belongs to exactly one of L05 and L06. Thus a feasible cover induces some T subseteq Q and has at least the displayed sum of exact root costs. Conversely the root-trie optimum words for the three required subsets jointly form a lawful cover attaining that sum. Exhaustive 256-mask integer evaluation then proves the strict gap.

## Verification

The accompanying lossless JSON certificate contains the exact 2,000-case compressed cost vector, two lawful 24-word witnesses, exact shadow-margin distributions, and SHA256 identities of frozen input/solver/output. The supplied offline verification code, original C++17 solver, generator, 9.6 MB frozen master, complete original C++ output, seven FINISHED logs and complete root-function dumps are included in the full local evidence bundle delivered to the user. The certificate alone verifies the preserved output identity and feasible witnesses; the lower-bound proof for all 2,000 cases is reproducible by the provided exact C++ optimizer.

Frozen master SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e.
Original 2,000-line output SHA256: 88a686450da4233093f0d93f6285b813fa78de29f73112da7f59abf7ac7500eb.

Coverage of the contiguous radius-three family reaches 27,000/38,169 (70.74%). **Next index: 27000**, remaining 11,169. The next scientific target is finding inexpensive sufficient inequalities certifying the eight-prefix margin in key-swap families without enumerating every transfer mask. This is author-side finite science; formal CLAIM/Result and independent Driver admission are separately controlled.
