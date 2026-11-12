# R5 — exact labeled-prefix LOUDS code for the minimal 1,065-pair dual-zero cover

**Source and scope.** Author-side mathematical/engineering certificate in the same frozen *external* P/Q–BRC Blackwell auxiliary model. Its inputs are the complete collision census from [PR #2149](https://github.com/awdawmip/enterprise-math/pull/2149) (commit \`f40960e285be90937aad827ce46446a1f777f1bc\`) and the two new theorems in this branch's \`RESEARCH.md\`: right-persistence and exact minimum 1,065-mask / 6,379-operation dual-zero pair cover. Original 28-coordinate/15-atom frozen fixture is EM \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`, science pins Global \`a01383f825ef9d43b4b754254303298c64041568\` and EM \`86149263e38c22292c9def1e0f69092efa1be77e\`.

## Construction

For each collision pair \`(q,n)\` admitting a dual-zero mask, select the smallest-cardinality mask (ties broken by integer mask order), and reconstruct the deterministic legal ordering by last-step predecessor recursion with ascending atom-label selection. Check all 28 rational prefix nonnegativity inequalities at \`r_(q,n)\`; the preceding interval theorem extends the chosen ordered word to all real \`r\` between its collision and \`1/23\` (with zero scale at the latter endpoint). There are precisely **1,065** distinct chosen words, containing **6,379** atom-label occurrences, each label in \`{1,...,15}\`.

Build a rooted prefix trie. Each edge stores the exact original atom label, each node represents the exact complete prefix, and terminal nodes indicate chosen complete words. Sort each node's child edges by integer label and use breadth-first traversal. The LOUDS degree stream consists of \`1\` for each outgoing edge followed by \`0\` for its parent node. Store four bits per edge label (since labels are 1 through 15) and one terminal bit per node in the same breadth-first node order.

Exact completed finite counts:

| Quantity | Count |
|---|---:|
| Complete dual-zero pair certificates | 1,065 |
| Flat labeled operation occurrences | 6,379 |
| Trie nodes, including root | 2,880 |
| Trie labeled edges | 2,879 |
| Shared prefix occurrences eliminated | 3,500 |
| LOUDS structural bits = edges + nodes | 5,759 |
| Four-bit edge labels | 11,516 |
| Terminal flag bits | 2,880 |
| **Packed trie payload** | **20,155 bits = 2,520 bytes** |
| Flat comparator (4 bits/label + 4 bits/word length) | 29,776 bits = 3,722 bytes |
| **Byte saving against that flat comparator** | **1,202 bytes (≈32.29%)** |

Payload bit lengths and byte padding are defined exactly; this comparison excludes shared model constants, Python object overhead, runtime indexes and any external metadata. The 4-bit word lengths suffice because the maximum chosen word length is 10. Neither size is asserted to be information-theoretically minimal.

## Exact decoding and observer provenance

Read the actual packed payload bit by bit (big-endian within bytes), separate the LOUDS stream, 4-bit edge labels and terminal bits using the known node/edge counts, and breadth-first reconstruct each prefix as an ordered labeled tuple. The decoder derives each terminal pair without a pair-to-node dictionary from the **full labeled operation vector**:

\[
n=-\sum_{a\in w}P_{\{a\},k0},\qquad
q=-\frac1{36}\sum_{a\in w}P_{\{a\},k1},
\]
with \`k0=(target0,source3)\` and \`k1=(target1,source3)\`. Reconstructed pair keys are checked to be unique, in the original collision census, and exactly equal to the complete original map \`(q,n) → ordered word\`. Thus trie sharing does not erase ordered labeled prefix provenance, and every individual word can be checked against the 28-coordinate source operation vectors.

**Correctness.** For any finite set of distinct words over the 15-label alphabet, the rooted prefix trie has a bijection between terminal paths and its inserted words; fixed-order LOUDS with child labels reconstructs its unique ordered labeled root-to-node paths. Because the 1,065 selected words have pair-distinct signed port-weight sums, the terminal-to-pair map is injective. The code checks surjectivity by equality with all 1,065 original pairs. Frozen exact legality comes from the source recursion and right-persistence theorem. This establishes exact reversible compression for this declared finite witness corpus.

## Reproduction and next question

Run \`python3 VERIFY_TRIE_CODEC.py\` in the same directory as \`VERIFY_RIGHT_PERSISTENCE.py\` using Python 3 standard library. The new script imports the sibling frozen 28-coordinate verifier, exact-reconstructs the 1,065 chosen words, packs and unpacks the trie bitstream, checks full word/pair equality and reports exact bit and byte counts. Local execution passed; independent clean-environment remote-byte execution remains an additional check.

Next: evaluate random-access retrieval and incremental updates as events activate, measuring total encoding/decoding and indexing costs at larger operation counts. The static representation here proves an exact reversible compression result, not yet a claim of optimal dynamic cost. Formal Source Result, independent review, and native X6 transport stay under their established separate contracts.
