# EC49FOJ reproduction and evidence ledger

Frozen scientific input is the **exact existing** 94-key, 178850-word source at original scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The source filename `master_and_radius3_cases.txt` has SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. The 84 original edge records in `FIRST_NEUTRAL_EDGES_EC49FNS.txt` have SHA256 `db8d3b9232f4ff31ffd2bf7ed81237625ecb6491f7883f4b03263728d6ecdc41`.

The current PR contains the full proof, a source-native complete C++17 verifier, an independent Python verifier, and both original edge pairs and exact first separating budgets. The companion complete evidence archive `EC49FOJ_FULL_THRESHOLD_FILTRATION_EVIDENCE_20261114.tar.xz` also contains the original pinned master input, all **34344** exact complete assignment records, all **84** detailed witness rows, the full partition-membership table at eight budgets, executed logs and SHA256 manifest. Archive SHA256: `78186d360262615294558693698cf95e5a23e1537470fa55df4c139cd3655284`.

## Reproduction

With the original source bytes saved as `master_and_radius3_cases.txt`:

```sh
g++ -std=c++17 -O2 VERIFY_EC49FOJ.cpp -o verify_foj
./verify_foj FIRST_NEUTRAL_EDGES_EC49FNS.txt 210 full_edges.csv partitions.csv complete_51.csv < master_and_radius3_cases.txt
python VERIFY_EC49FOJ_INDEPENDENT.py master_and_radius3_cases.txt FOJ_EDGE_FIRST_SEPARATION_84.csv
```

C++ proof checker asserts that each of the 51 configurations is exhaustively covered, all 34344 legal complete assignments are present and maximal cost is 195; the exact first-separation histogram and class counts must match. It outputs **84 complete witness records** and the full 51-class filtration. The independent Python checker reconstructs native rooted prefix DP and independently verifies all six finite transition thresholds and all-budget equality across nine edges (11 cases).

The compressed full archive is provided as a conversation attachment alongside this PR. The input hash is the same as the prior EC49FOI evidence; it is not a refreshed scientific configuration.

Status: authored and computationally checked, `NOT_REVIEWED`. Original provenance: Researcher-ID `EM-DIRECT-204C14`, Activity `RA-6893088D0A7347CE7F4D8720`. The unpublished topic metadata `RS-EC49AS` is not a formal CLAIM or Result.
