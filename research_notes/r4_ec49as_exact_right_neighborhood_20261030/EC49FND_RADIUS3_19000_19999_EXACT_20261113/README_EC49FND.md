# EC49FND — exact 1,000 BRC radius-three cases and a six-configuration cost plateau

Author-side research, 2026-11-13. Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, retained without modification. This work continues the *non-overlapping* frontier 18000–18999 from [PR #2230](https://github.com/awdawmip/enterprise-math/pull/2230). [PR #2234](https://github.com/awdawmip/enterprise-math/pull/2234) has distinct structural work and an overlapping 18000–18499 span; do not count that span twice.

## Mathematical definition and exact method

The frozen nine-state original BRC catalogue consists of 178,850 legal operation words, 94 complete cache keys, 24 observation labels, and 38,169 radius-three seven-key configurations. An operation word expands into a path of *ordered signed native X6 microsteps*. For a selected set K of seven complete keys, C(K) is the minimum number of distinct nonempty ordered signed microstep prefixes in a collection of original legal words covering every one of the 24 labels. No endpoint-only, unsigned, or coordinate-collapsed equivalence is taken.

For every eligible first microstep r, form the original-word prefix trie and define f_r(S) as the minimum number of nonempty trie nodes in selected lawful word paths covering required root-label subset S. Finite trie DP enumerates endpoint label masks and minimum node counts. Superset closure permits a candidate to cover extra labels. Exhaustively assigning all 24 observation labels to available roots and minimizing the sum of their f_r yields C(K). Every eligible word selection induces an assignment and a trie realization; conversely each DP subtree yields lawful words. This establishes matching finite lower and upper bounds, with the completeness of the frozen candidate catalogue part of the input assumption.

Compiled original C++17 trie/subset optimizer evaluated all **1,000** configurations i=19000,...,19999 on the original frozen master input. Minimum **98** occurs exactly at indices **19128,19291,19313,19553,19890,19947**; maximum **220** at **19371**; 95 distinct attained costs. All 1,000 costs and six full 24-word witnesses are preserved losslessly in the compact certificate (base64 + xz-encoded JSON); the exact vector decodes to one unsigned-byte cost for each consecutive index. Source input SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. The raw 1,000-line C++ output SHA256 `fde4d51f9a76809441f964ed85156b7c8347fde0bfb11f1c51f60771f006aca4`. Cost-byte vector SHA256 `44cdea5f32ebb0483833e80ec5ad48220bd7a8a20e6ef6e614d19a586adea9d9`.

Independent Python native prefix-trie DP recalculated selected indices: 19000→160, 19128→98, 19291→98, 19313→98, 19371→220, 19553→98, 19890→98, 19947→98, 19999→159, all agreeing with C++. The 24-lawful-word witnesses of all six minimizers independently realize exactly 49+49=98 nonempty signed prefixes in first-microstep roots 05 and 06; root 07 is unused.

## Finite theorem 1: exact 2×3 plateau

For A∈{8,9} and B∈{{14,26},{32,49},{34,49}} define

`K(A,B) = {0,4,5,11} ∪ {A} ∪ B`.

The six configurations are respectively 19128,19291,19313,19553,19890,19947 and **C(K(A,B))=98** for all six. These are exactly the six interval minimizers, each using 49+49 root prefixes. This is a complete finite six-case proposition on the frozen model, not an assertion about arbitrary key substitutions.

## Finite theorem 2: root-function dominance versus global optimum equality

For each of the three fixed B, compare the corresponding configurations A=8 and A=9. The first-root domains are identical and comprise 12,12,8 labels (4096+4096+256=8448 root-subset masks). Independently recomputing every root function from the frozen lawful-word set produces the following counts (A=8 strictly cheaper / equal / A=9 strictly cheaper):

| B; pair of indices | root 05 (4096 masks) | root 06 (4096 masks) | root 07 (256 masks) |
|---|---:|---:|---:|
| {14,26}; 19128→19553 | 2 / 4094 / 0 | 326 / 3770 / 0 | 21 / 235 / 0 |
| {32,49}; 19291→19890 | 1 / 4095 / 0 | 110 / 3986 / 0 | 11 / 245 / 0 |
| {34,49}; 19313→19947 | 0 / 4096 / 0 | 0 / 4096 / 0 | 0 / 256 / 0 |

Thus in the first two pairs A=8 weakly dominates A=9 at **every** requirement mask on every root, strictly on some masks, while both full 24-label optima are equal at 98. In the third pair *all 8448 entries are identical*. These establish two mechanisms of cost invariance: global equality despite strict rootwise differences, and full root-function identity. This also refutes the finite-model converse `C(X)=C(Y) ⇒ f_r^X(S)=f_r^Y(S) for all r,S`. (No floating-point calculations appear.)

General lemma: given identical label domains and feasible assignments, if f_r^X(S)≤f_r^Y(S) on all root masks for every root, then C(X)≤C(Y), because the inequality survives summing each assignment and taking minima. Equality of the global minima does not require equality of the component functions, as shown above.

## Reproducibility, source and next work

The committed compact certificate stores all 1,000 costs, all six 24-word witnesses, source hashes and keys. Root-function comparison counts above can be regenerated from the frozen source by the attached independent native Python root-trie algorithm; expanded inputs, the C++ solver, original output, six full native paths, independent Python tests, root-function comparison with hashes, and SHA256 manifest are separately available in the complete local evidence archive. Full-window C++ rerun reproduces the claimed *1,000-case* optimality vector; the committed vector checksum alone is not the proof of its optimum.

The previous minimum for this 38,169-case radius-three family remains **96** at index 17965. Contiguous verified coverage, if combining published author-side artifacts, reaches indices 0–19999: **20,000/38,169 (52.40%)**. The distinct unrestricted seven-key mother problem retains its prior 84-prefix feasible upper bound.

**Next unfinished index: 20000**, with 18,169 configurations remaining. Further question: identify checkable sufficient conditions at the level of native prefix tries that predict root-function identity or weak dominance for replacements, and test beyond the six enumerated cases. Immutable formal Task/CLAIM/Result and independent Driver acceptance require their own authority; this is scientific author evidence, not a formal completion claim.

### Recover the full compact certificate

Store the companion `EXACT_CERTIFICATE_EC49FND.json.xz.b64` as plain base64 text, then:

```bash
base64 -d EXACT_CERTIFICATE_EC49FND.json.xz.b64 | xz -d > EXACT_CERTIFICATE_EC49FND.json
```

It contains `cost_base85` as zlib/base85 of exactly 1000 unsigned integer costs; in Python: `zlib.decompress(base64.b85decode(cert["cost_base85"]))`. Full expanded evidence and source code are retained in this research turn's downloadable archive.
