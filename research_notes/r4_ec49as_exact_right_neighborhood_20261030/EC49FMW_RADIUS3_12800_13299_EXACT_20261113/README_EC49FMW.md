# EC49FMW — Exact BRC seven-key radius-three cases 12800–13299

Date: 2026-11-13 (Asia/Shanghai). Author-side scientific evidence; no formal CLAIM or Result.

## Scientific object and frozen input

Continue EC49FMV from [PR #2202](https://github.com/awdawmip/enterprise-math/pull/2202), commit `d7d24b4679dad94967e1a42dd9da830aa6380496`. The immutable scientific pin is `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`: a nine-state BRC system with 178,850 legal operation words, 94 complete raw cache keys, 24 required observation labels, ordered signed six-axis native microsteps, and the fixed catalogue of 38,169 coverable three-key-replacement configurations.

For each seven-key configuration `K_i`, let `C(K_i)` be the minimum cardinality of the union of nonempty ordered signed-X6 primitive-step prefixes over finite sets of original legal operation words whose *complete raw keys* belong to `K_i`, jointly covering all 24 observation labels. Count native path prefixes, not commutative net displacement or a keywise relaxation.

## Exact finite result

All 500 consecutive configurations 12800 through 13299 were evaluated by the original C++17 exact integer prefix-trie and label-subset DP, with no omissions or duplicated indices. The lossless entire 500-value cost vector and exact witness are in `EXACT_CERT_EC49FMW.json`.

```text
min_{12800 <= i <= 13299} C(K_i) = 114
unique argmin = 12875
max = 205, attained at 12862, 12873, 12983, 13261, 13268
```

At index **12875**, the exact seven-key set is `[0,4,5,19,24,32,49]`. Twenty-four original legal words, one for each required observation, yield three disjoint signed-first-step prefix subtries of sizes **50 + 52 + 12 = 114**, with root-byte IDs 05, 06 and 07. The JSON includes every selected word and its target label. Counting its full ordered signed primitive path prefixes proves the upper bound 114, while the complete DP supplies a matching lower bound.

Independent Python trie/demand-assignment computation confirmed **12800→171, 12875→114, 13299→132**, separately from the C++ implementation. The cost vector SHA256 is `2fe33f5583e5ba699fc152d308d4017ed78dc13925339f90c6c3e1c80d2adc17`. The 500 original raw solver rows SHA256 is `bdcb53f352f9e590ea294f0e58420ece9488108986627c0b332c929502006959` (in the complete evidence package).

## Exactness principle

For each allowed signed first primitive step, construct the rooted trie of permitted original operation-word prefixes. At any node, DP over bitmasks of required observations combines terminal-word selection and each child by mask union and integer cost sum, charging one unit for a selected nonempty prefix. By induction on subtree height the DP computes the minimum cost covering every mask, and a superset-min transform computes minimum cost covering **at least** a mask. Every target observation is assigned to a compatible root, and all such assignments are enumerated; independent roots have disjoint first-byte prefixes. This gives the exact optimum for each of the specified 500 catalogue configurations. The same proven frozen generator and index ordering from the previous source are used.

The cumulative restricted-family minimum for indices **0–13299** remains **102** (previously attained at 32 and 93, among others). The separate unrestricted seven-key mother problem retains the known upper construction `C_min(7) <= 84`; these two search domains are deliberately distinguished.

## Reproduction and continuation

The complete evidence package includes frozen `master_and_radius3_cases.txt`, `cases.json`, original `scan_cached_radius3.cpp`, `EC49FGW_RADIUS5_SCREEN.py`, `EC49FGJ_SEVEN_KEY_94_WITNESSES.json`, the full 500-row output, independent Python checker/log, 24-word reconstruction, the compact vector, standalone checker and SHA256 manifest. Rebuild on a suitable host:

```sh
g++ -O3 -std=c++17 scan_cached_radius3.cpp -o scan
./scan 12800 13300 < master_and_radius3_cases.txt > replay.txt
cmp replay.txt EXACT_NATIVE_OUTPUT_12800_13299.txt
python VERIFY_RADIUS3_SELECTED.py cases.json 12800 12875 13299
python VERIFY_EC49FMW.py
sha256sum -c SHA256SUMS_EC49FMW.txt
```

The requested larger run was interrupted after completing index 13299; later indices are excluded. **Next: 13300**, with **24,869** restricted cases remaining. Further scientific objectives: cross-configuration reusable integer lower-bound certificates, and an unrestricted seven-key witness below the known 84-prefix bound.

Native exact task read `emr4-20261113-0449-controltask-ec49as` returned `FAILED: CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION`, so this research has author-side Source evidence only, without an authenticated winning task CLAIM, formal Result, or independent Driver admission.
