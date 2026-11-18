# EC49FMG — Exact signed-X6 prefix minima for radius-two indices 1420–1619

Date: 2026-11-12. Status: author-side exact finite evidence; independent Source Driver review pending.

## Frozen question and statement

The native nine-state BRC generator is fixed at scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, with 178,850 admissible operation words, 94 distinct *complete* raw cache keys, and 24 observation requirements. Every operation word carries its original **ordered signed six-axis microstep path**, including all nonempty native prefixes. A seven-key configuration permits words only from its seven complete raw keys.

The baseline seven-key set is `{(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}`. For each two-key deletion and two-key addition from the other 87 keys, retain the keysets with full 24-demand coverage. The lexicographically enumerated coverable set family has 6,315 members; indices are 0-based (EC49FKZ).

**Finite theorem EC49FMG:** for every integer `1420 <= i <= 1619`, the exact minimum union cardinality of all ordered signed-X6 nonempty prefixes from lawful words covering every required observation under keyset `K_i` equals `EXACT_VECTOR_EC49FMG.json["exact_prefix_costs"][i-1420]`. The distribution is **98:3; 104:35; 106:5; 111:2; 112:155**. In particular,

```
min_{1420 <= i <= 1619} C(K_i) = 98,
argmin = {1468, 1542, 1615}.
```

The two fixed keysets `K_1452`, `K_1460` have **odd** minimum 111; the file contains full legal 24-word witnesses for each, as well as a 98-prefix witness for `K_1468`. These explicitly disprove any proposed universal *evenness* invariant of this exact fixed-key prefix cost over this family. Such a parity rule was not an accepted prior theorem.

## Mathematical proof mechanism

For any fixed keyset, enumerate **every lawful word**. Partition them by their first native signed microstep. Build the finite prefix trie in each first-step root. A terminal word supplies its exact observation label. An induction on trie height computes, for every local label subset, the minimum number of selected prefix nodes covering it: combine child subset masks by bitwise union, add one for each nonempty selected current prefix, and minimize over alternatives. Superset closure allows a root to satisfy a demand assigned to it together with extra labels. Enumerate all assignments of the 24 required labels to roots that contain them; take the smallest sum of independent root costs. Since different first-step roots have disjoint nonempty native prefixes, both the lower-bound and construction directions are exact.

All operations use integer arithmetic. No floating-point tolerance or optimization-solver status is an input to the proof. Each instance includes its entire exact allowed-word catalogue. Exact finite coverage therefore establishes the stated instance-wise minima.

## Actual execution and replication

The existing frozen `EC49FGW_RADIUS5_SCREEN.py` generated the 178,850-word catalogue. The previous `EC49FMF` cached C++17 trie/subset-DP implementation (unchanged engine bytes, SHA256 `8639af8a3c72f3dd38690fd0a537124a4a10f84478efc3e1595d78c39ca0219e`) processed the requested indices 1420..1719. The executable completed **exactly 200 consecutive records 1420..1619** before its local wall-time limit. Only those 200 completed records enter this theorem.

Original 200 detailed root-DP records: SHA256 `895c1bb96c1339ea9cf500c4cf9ec7f3266cb341c4b81155c64019dd12cdd010`. Original master/case input SHA256 `8db9447f5d9ad52e9cc919f2418a629eb0b0f7250b7acec93357ddc215d033ab`. Cost-byte vector SHA256 `a70b2bed66e35ce6a7179aa5cb5de743119267f7963dc686f8c191dd16bd1ff3`. These refer to actual local original files, not to GitHub blobs.

An independently implemented Python prefix-trie/subset-DP recomputed indices **1420,1452,1460,1468,1542,1615,1619**, obtaining respectively `104,111,111,98,98,98,106`; all matched the main C++ computation. Separate Python traceback reconstructed complete legal 24-word witnesses for 1452, 1460, 1468, and checked their exact native prefix unions (111, 111, 98).

Use adjacent `REPLAY_EC49FMG.py` for portable witness/vector verification and optional fresh exact recomputation. The same immutable model and prior reproducibility sources are in sibling research-note directories: `EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py`, `EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp`, and `EC49FMF_RADIUS2_970_1419_EXACT_20261112/REPLAY_EC49FMF.py`. No newly invented scientific input is used.

## Actual current research frontier

The prior contiguous exact radius-two interval was 0..1419. The present contiguous interval is **0..1619**: **1,620 of 6,315** coverable two-key replacement configurations, with 4,695 remaining. Next uncompleted index: **1620**. Independently validated fifth replacement radius minimum is 114, and the previously constructed unrestricted seven-key solution still gives `C_min(7) <= 84`; the unrestricted global optimum and any 83-or-smaller construction remain open.

This is an author-side research artifact on PR #1730, not an admitted canonical Result. The original native session-start request ultimately returned `SUCCEEDED`, registering actual Researcher-ID `EM-DIRECT-6D12A3` and Research-Activity `RA-CD6C5F36B37D4328F5F58C5A`, verified on canonical Source main `3adc911cc5c7e15938da74f360e83423eabc436e`. The original bounded native task-inventory request also returned `SUCCEEDED`; it did not establish a current EC49AS task-owner/CLAIM binding for this science, and no CLAIM, Result, or independent Driver review was written. An earlier transient `BACKEND_IDENTITY_CHECK_UNAVAILABLE` read error is superseded by these actual original-request receipts. Activity metadata is canonical; its scientific source checkpoint remains to be attached. Keep P000, ACTIVE worldview, signed microstep provenance and frozen scientific pin unchanged.
