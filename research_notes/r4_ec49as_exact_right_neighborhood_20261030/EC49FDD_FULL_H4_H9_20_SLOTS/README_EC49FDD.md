# EC49FDD — complete 20-variable H4–H9 exact obstruction

**Date:** 2026-11-07. **Frozen scientific pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Status:** AUTHOR_FINITE_EXACT_PROOF / TWO_IMPLEMENTATIONS_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Exact theorem

Fix the original 24 designated slots, nine-state observer, literal ordered signed native-primitive-step prefixes, and BRC cache keys `L=(4,2,1)` and `M=(7,3,2)`. Let `P(w)` be the set of nonempty literal signed primitive prefixes of word `w`. The four original H2/H3 slots remain fixed. Each of the **20 H4–H9 slots** may choose any word from its **entire** frozen multiset-and-observer-signature language.

**Theorem.** The exact minimum `|∪ P(w_slot)|` over all twenty simultaneous independent choices is **158**. The original 24-slot assignment is a legal 158-prefix witness. It follows that **every subset** of these twenty slots also has exact optimum **158**, because relaxing more slots cannot increase the minimum. The resulting family of `2^20=1,048,576` subset problems is covered *by a single exact superset proof*, not by separately executing one million searches.

In particular all **1,152 ordered** A/B nine-slot instances (all H4/H6/H7 signatures with a distinct extra H6 and H7 signature) are subsumed. This finishes the EC49FDD nine-slot neighborhood without duplicating the 1,134 cases not previously solved separately.

The theorem concerns the declared **finite frozen typed model** with fixed key and observer. It does not state that the nine-window **93-edge mother objective** is unreachable after changing a valid BRC cache key or the candidate construction.

## Exact proof kernel

Let `F` be the literal prefix union of the unchanged four H2/H3 words. The executed checker establishes `|F|=16`. Generate all legal signature-preserving native words for every H4–H9 label, insert each signed primitive string into a prefix trie, and put the full terminal **label bitmask** on its terminal node. The trie contains **109,973 nodes**, from **16,152 labelled candidate words**. Charge an incoming edge 0 if its complete prefix belongs to `F`, otherwise 1.

For node `v` and label-mask `M`, define `D_v(M)` as the least cost for realizing exactly those labels using terminal words in the subtree. Initialize cost 0 for every subset of terminal labels at `v`. For each child `u` combine disjoint masks `A,B` by

`D_new(A∪B) = min(D_new(A∪B), D_old(A) + D_u(B) + edge_cost(u) * [B≠∅])`.

Different child subtrees have disjoint proper prefixes, and each used incoming edge is paid once. Induction on height proves exact enumeration of all legal labelled word choices and exact prefix-union cost. At the root choose the full 20-bit label mask and add `|F|`. This preserves sign, primitive order, branch label and multiplicity at the permitted observer.

The C++ implementation stores only reachable masks; the Python implementation independently constructs a literal prefix trie from the frozen words and uses a dictionary recurrence rather than consuming the C++ serialized trie. Both evaluate the **entire** candidate languages. A 158-cost cap is justified by the known legal witness and nonnegative edge costs; an **unrestricted-for-this-instance cap of 1000** gives the same optimum 158. At cap **157** no full-mask state exists, excluding every legal 157-or-lower configuration.

## Actual results and reproducibility

| Property | Executed exact result |
|---|---:|
| Variable labels | 20 |
| Fixed H2/H3 prefix edges | 16 |
| Legal candidate words, labelled | 16,152 |
| Trie nodes | 109,973 |
| Minimum additional edges | 142 |
| **Total optimum** | **158** |
| C++ inspected reachable-state pairs | 76,591,210 |
| Disjoint compatible pairs | 15,993,316 |
| Peak single-node mask states | 1,048,576 |
| Independent Python full-language optimum | **158** |

Generated serialized input trie SHA-256: `0283d45e91952560f8830eaa49d00313e8ee1b43329363fee2b3b3c7299db855`. Both exact solvers produced identical trie-size, fixed-edge, optimum, transition and root-state counts. Previously published dense nine-label solver independently returned 158 for a representative nine-slot case; sparse DP returned 158 on the same full input. Eight additional 13-label A/B dominator instances (all H4 signatures) were each independently solved with optimum 158; they are now superseded by the stronger 20-label theorem.

The unchanged model is sibling `EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py` (Git Blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`), and exact trie builder is sibling `BUILD_EC49FCZ_TRIES.py` (Git Blob `4c74b4ee243c939494d9f7eedb3f61255e16f91f`). The published scripts import them directly. To reproduce:

```sh
g++ -O3 -std=c++17 SPARSE_PREFIX_TRIE_DP.cpp -o exact_sparse_dp
python RUN_EC49FDD_20.py
python VERIFY_EC49FDD_INDEPENDENT.py
```

The runner writes a C++ JSON report and independently recreates the byte-identical trie; the Python program writes a separately constructed exact result. Both executable programs were run before publication and yielded **158**. The original assignment's literal union was independently checked as **158**. The source pin is a frozen research model, not an assertion about native physical dynamics or a new Foundation theorem.

## Next and admission

The fully varying H4–H9 **fixed-key** route is closed at 158. Next **EC49FDE**: introduce **one explicitly admissible alternative BRC multiset cache key**, verify native word/signature feasibility, seek a signed primitive-word witness with **≤157** prefixes, and then calculate its exact bounded optimum or its feasibility obstruction. The 93-edge mother target stays open.

This is **GitHub author-side research material**. The native Enterprise Math service returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH` with `operation_sent=false`. A current Owner, native CLAIM/Result and independent Driver mathematical review were not confirmed. P000 and protected ACTIVE worldview are unchanged.
