# EC49FMY — BRC seven-key radius-three exact finite scan, 14500–15399

**Date:** 2026-11-13. **Status:** Author-side finite computational result, independent Driver review pending. **Frozen scientific input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (unchanged). **Predecessor:** [EC49FMX PR #2209](https://github.com/awdawmip/enterprise-math/pull/2209) at `49b61b013a186b5b24bd77a6b6fa5c092b79c891`.

## Exact finite object and new result

The frozen nine-state BRC generator yields **178,850 lawful words**, **94 complete raw cache keys**, **24 observation labels**, and **38,169** deterministically enumerated seven-key radius-three configurations. For a fixed `K_i`, `C(K_i)` minimizes the number of distinct, nonempty, **ordered signed native-X6 microstep prefixes** of selected lawful words with keys in `K_i`, while covering every one of the 24 labels. Full ordered prefix identity, not merely endpoint displacement, is counted.

The unchanged original C++17 prefix-trie and integer subset DP emitted every configuration in the consecutive interval **14500 through 15399** (900 cases). The exact values yield:

- `min C(K_i)=104` for `14500 <= i <= 15399`, **attained only at 14750**;
- `max C(K_i)=214`, **attained exactly at 15050 and 15214**.
- The complete exact 900-element vector is stored losslessly in [EXACT_CERTIFICATE_EC49FMY.json](EXACT_CERTIFICATE_EC49FMY.json) as base64(zlib(uint8 costs)); SHA256 of uncompressed vector: `a08d673bfcfabe20c8dc4f2856e8c5edce132cc4dc28e7b14915f08953bcbb6a`.

The original command requested 14500–17499, but reached a local execution timeout after emitting the *complete* 15399 row. Only the finished 900 cases were retained. Original 900-row output SHA256: `23538219f2c406c4fc577c7813fbcf1d6002da338955e2cae163f8968f78b197`.

## Constructive witness and lower bound

For **configuration 14750** the certificate embeds 24 distinct original lawful BRC words, one per observation label, with complete cache keys and explicit ordered native prefix traces. Decompress the `witness_zlib_base64` member of the JSON to reconstruct the full witness JSON. Its three first-signed-step prefix subtrees (root hex 05, 06, 07) use respectively **39, 45, 20** distinct nonempty prefixes, for a constructive total of **104**.

The exact lower bound is obtained as follows. Partition by the first native signed microstep (disjoint nonempty prefix root families). For each root, construct the prefix trie of all available lawful words. At each node maintain the cheapest integer cost for each subset of observation labels present in the selected terminal words. Merge disjoint child subtrees by subset-union convolution and integer addition; charge a retained nonroot prefix node once. Induction on subtree height makes these minima exact. Enumerate all assignments of each required observation label to an available root and sum the root minima. The minimum therefore equals `C(K_i)` for each fixed finite `K_i`. For 14750 the computed lower bound is 104, matching the 24-word construction.

A separately implemented Python native-prefix trie/allocation solver, *not using C++ DP vectors*, returned **14500:130, 14750:104, 15399:170**, all agreeing with C++. The compact self-contained [VERIFY_EC49FMY.py](VERIFY_EC49FMY.py) verifies the complete 900-value byte-vector digest, indices, extremes, and embedded 24-word native prefix union. Full generator-membership and selected-DP independent checks were additionally run against the original scientific archive locally. This is precise finite computational evidence, not an independently admitted global theorem.

## Reproduction and scope

The unchanged source C++ solver (`scan_cached_radius3.cpp`, SHA256 `6ea17ff267f599c69967b420ebf1a8abe151e587e57b25f599f8ecdfb9f2ecac`), full 9657670-byte frozen input (`master_and_radius3_cases.txt`, SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`), deterministic `cases.json` (SHA256 `d18c8f3177083c5b39ef6c8ca068589042617a2a797b53f98818a427040e4f33`), generator, 900 original output rows, both verifier programs, native witness, and file-hash manifest are available in the **full local evidence archive**. The compact GitHub certificate holds the complete numerical and witness objects. Reproduce with the original frozen files:

```bash
g++ -O3 -std=c++17 scan_cached_radius3.cpp -o scan
./scan 14500 15400 < master_and_radius3_cases.txt > exact_14500_15399.txt
python VERIFY_RADIUS3_SELECTED.py cases.json 14500 14750 15399
python VERIFY_EC49FMY.py
```

Previously verified cases 0–14499 had a minimum of 102; the cumulative 0–15399 restricted-family minimum stays at **102**. The unrestricted seven-key mother problem retains its separate legal 84-prefix **upper bound**, `C_min(7) <= 84`.

## Control and continuation

Native read `emr4-20261113-0634-task-rs-ec49as` returned `FAILED / CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION`; no formal task CLAIM or Result is asserted. Research-session registration was requested separately and must be judged by its final actual receipt. This GitHub branch/PR stores author-side evidence; no Driver mathematical acceptance is claimed.

**Next exact computation index:** `15400`, with **22,769** uncomputed configurations. Additional directions: reusable cross-configuration lower-bound certificates and unrestricted legal constructions with fewer than 84 native prefixes. The 900 completed cases and 14750 witness should be reused, not recomputed merely to create another checkpoint.
