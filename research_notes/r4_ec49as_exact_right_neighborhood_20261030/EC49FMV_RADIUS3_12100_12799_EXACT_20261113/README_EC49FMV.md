# EC49FMV — Exact BRC seven-key three-replacement configurations 12100–12799

2026-11-13 (Asia/Shanghai). Author-side TASK_RESEARCH result; formal CLAIM, Result and independent admission are separate.

## Frozen scientific object

Continue EC49FMU, PR #2198 at immutable source commit `aea7b8412985ada526c24385a7b969f28ee16f47`. Scientific pin **`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`**; nine-state BRC; 178,850 legal operation words; 94 complete raw keys; 24 observed demand labels; 38,169 deterministically indexed coverable seven-key cases of the three-key-replacement family. A cost counts **distinct nonempty, ordered, signed native X6 microstep prefixes**, not unsigned axes, word endpoints, or raw-key quantity.

For each case K_i, define C(K_i) as the minimum prefix-union cardinality among collections of frozen legal operation words whose full raw cache keys belong to K_i and whose labels cover all 24 observations.

## Exact result and proof method

The unchanged integer C++17 root-trie/subset DP solved all **700 indices 12100–12799**, with exactly one result per index and no gap:

```
min_{12100 <= i <= 12799} C(K_i) = 110,
argmin = {12396}.
max = 205, achieved at {12109,12139,12324,12352,12436,12672,12698}.
```

First-root counts: three roots in 168 cases, four roots in 532. The losslessly compressed complete cost vector, histogram, frozen SHA256 hashes and original 700-line output hash are in `EXACT_VECTOR_EC49FMV.json`.

Exactness for a fixed K: group the *original legal words* by their first signed primitive step. A finite trie node represents one nonempty ordered prefix. For every observation-mask, recursively combine child-subtree mask costs by union and integer addition; include a node exactly once when a selected word below it is used, and allow selecting words terminating at that node. Induction on tree height proves the minimal cardinality for every mask. Take subset/superset closure to enforce required observations; assign the 24 demands to every compatible root in all possible ways, sum independent root minima, and minimize. Every legal word lies in exactly one first-root trie. Thus this exhaustive integer dynamic program computes the exact finite-catalogue optimum; it neither approximates the cost nor ignores branch/order/sign data.

The distinct case `K_12396=[0,4,5,14,19,24,26]` has 24 **actual frozen catalogue operation words** in `WITNESS_12396_EC49FMV.json` covering all 24 demand labels. Its root prefix costs are **48+50+12=110**, attaining the matching DP lower bound. The witness verifies against full raw-key membership and the original nine-state legal-word generator in the companion evidence archive.

A separate Python native-prefix trie/demand solver confirmed:
- index 12100: 130;
- index 12396: 110;
- index 12799: 148.

The verified previously completed prefix 0–12099 had minimum 102, so the cumulative exact finite restricted-family minimum on **0–12799 remains 102** (12,800/38,169). The separate unrestricted seven-key problem retains its previously constructed 84-prefix upper bound `C_min(7)<=84`; this finite restricted-family minimum is not a lower bound for that mother problem.

## Reproduction and material locations

`VERIFY_EC49FMV.py` checks vector length/SHA256/histogram, argmins/argmaxs, root counts from optional original raw rows, the native signed-prefix construction, and—when original frozen inputs are available—full legal-word/raw-key membership.

The full companion tar.xz evidence was created and locally verified, containing `EXACT_NATIVE_OUTPUT_12100_12799.txt` (all 700 original output lines), unchanged `scan_cached_radius3.cpp`, `master_and_radius3_cases.txt`, `cases.json`, `EC49FGW_RADIUS5_SCREEN.py`, `EC49FGJ_SEVEN_KEY_94_WITNESSES.json`, `VERIFY_RADIUS3_SELECTED.py`, three independent-check results, full optimal witness reconstruction, `VERIFY_EC49FMV.py` and SHA256 manifest. The original source inputs and solver are frozen and unchanged from prior EC49FMU; local full package is linked in the corresponding research conversation.

Full package replay:
```sh
g++ -O3 -std=c++17 scan_cached_radius3.cpp -o scan
./scan 12100 12800 < master_and_radius3_cases.txt > replay.txt
cmp replay.txt EXACT_NATIVE_OUTPUT_12100_12799.txt
python VERIFY_RADIUS3_SELECTED.py cases.json 12100 12396 12799
python VERIFY_EC49FMV.py
sha256sum -c SHA256SUMS_EC49FMV.txt
```

## Ownership and next frontier

Prior control checks for `RS-EC49AS` did not establish current immutable publication/CLAIM ownership. This author-side mathematical material does not claim task ownership or native Result. Before formal task acquisition check the exact current Source publication and active owner. An independent Driver review is still needed for mathematical admission.

Next deterministic configuration index **12800**, with **25,369** uncomputed cases remaining. Explore cross-case lower-bound certificates, further low-cost restricted constructions, and genuine unrestricted sub-84 constructions. Preserve the pinned science and avoid recounting 0–12799.
