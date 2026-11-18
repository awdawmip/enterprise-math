# EC49FMP — exact native signed-X6 BRC seven-cache-key radius-three configurations 5500–6499

**Date:** 2026-11-12. **Scientific input frozen pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Author-side continuation of EC49FMO. Same nine-state BRC, 178,850 lawful words, 94 complete cache keys and 24 observation demands.

## Finite theorem and full range

The frozen deterministic radius-three enumeration has 38,169 seven-key configurations whose lawful words can witness all 24 observation demands. Let (K_i) be coverable configuration (i), with the original enumeration order and exact key catalogue. Let (C(K_i)) be the minimum number of distinct **nonempty ordered, signed six-axis native prefixes** over a legal selection of witness words covering every observation. We computed **all 1,000 consecutive cases** (5500\le i\le6499), proving the finite statement

[
\boxed{\min_{5500\le i\le6499}C(K_i)=116.}
]

Equality occurs exactly at indices **5520, 5663, 5804, 5944, 6013, 6081, 6148, 6214, 6279, 6343, 6406, 6468**. Range maximum is 168. Full histogram and complete lossless 1,000-byte cost vector are in [EXACT_VECTOR_EC49FMP.json](EXACT_VECTOR_EC49FMP.json). 277 configurations have three first-step roots and 723 have four. The continuous explored range now reaches 0–6499 (6,500/38,169), and its exact minimum remains 102, realized earlier at indices 32 and 93. The unrestricted seven-key mother problem retains the separate previously constructed 84-prefix upper bound (C_{\min}(7)\le84).

## Exactness argument

At each allowed first signed-microstep root, insert *all* lawful witness words of the selected seven complete keys into their full native ordered-prefix trie. Mark every terminal with the observation labels it witnesses. For each trie node, integer dynamic programming enumerates attainable label masks and the minimum number of charged nonempty vertices of its selected subtree. Combining disjoint children takes union of label masks and sum of charges; a selected nonempty subtree charges its current vertex once; the artificial root has charge zero. An induction on the trie height proves the minimum for each exact label mask; superset closure gives the optimal value for covering any requested mask. Every full selection induces an assignment of each of the 24 demand labels to an admissible first-step root. Conversely an optimal set of root subtrees supplies legitimate witness words, and different first-step roots share no nonempty prefixes. Thus minimizing the sum of root costs over all legal assignments is exactly (C(K_i)), not a heuristic bound. We enumerated the exact finite set of 1,000 consecutive indices with no skips.

## Execution and checks

Using the unchanged C++17 native prefix-trie/bit-mask solver from the predecessor evidence archive and its frozen catalogue (`master_and_radius3_cases.txt`, SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`), we ran exactly `./scan 5500 6000 < master_and_radius3_cases.txt` and `./scan 6000 6500 < master_and_radius3_cases.txt` with the same `-O3 -std=c++17` build. Their joined exact raw output hash is SHA256 `77126ccabd9b3aab6960724dd857be6897e4e279da7f7a288ea32ea27d1df65d`; C++ solver source SHA256 is `6ea17ff267f599c69967b420ebf1a8abe151e587e57b25f599f8ecdfb9f2ecac`; cost bytes SHA256 is `da8c350589e2a611776701a28f1873fddeccf56ca18eef471b03747b0cd05160`. [VERIFY_EC49FMP.py](VERIFY_EC49FMP.py) checks the entire vector, all 1,000 row IDs and costs against raw output when available, source hashes and first-root histogram. Recomputed 178,850 lawful BRC words independently through the frozen Python generator and its separate prefix-trie DP for five selected configurations: `#5500=160`, `#5520=116`, `#6013=116`, `#6468=116`, `#6499=138`, all matching. [Independent executed output](INDEPENDENT_PYTHON_LOG_EC49FMP.txt).

The full local evidence archive includes both raw 500-row outputs concatenated to 1,000 rows, solver logs, the frozen generator/cases, original C++ source, independent Python DP and a SHA256 manifest; these large source/input materials are referred to by exact hash above. This GitHub directory preserves the complete lossless cost vector, proof, verifier and independently executed spot-check log.

## Next scientific question

Resume at **index 6500**; 31,669 coverable radius-three configurations remain outside the continuous solved prefix. Investigate reusable cross-configuration integer lower-bound certificates and search for legal unrestricted seven-key constructions with at most 83 prefixes. The exact finite result here retains its defined family; mathematical admission awaits independent Driver review.

## Native control

Author-side research material only. CLAIM/open, native Result and Activity are separate states requiring their own real authorization and receipts. P000, ACTIVE worldview and frozen science were not modified.
