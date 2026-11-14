# EC49FMA addendum — exact native-prefix minima for the first 91 three-key-swap cases

Date: 2026-11-12. Same frozen nine-state BRC and signed-X6 native-prefix model, original full catalogue pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.

Following the complete 38,169-case *label-support* three-key census, three small nonempty dropped-key classes were completely solved with the **unchanged original exact EC49FKY C++17 signed-prefix trie dynamic program**. For each of the 91 coverable seven-key sets in classes #25, #26 and #28 (0-based order of C(sorted(K0),3)), include **every** legal original word with any of the seven complete raw keys. Serialize each word's full ordered signed native microsteps using the existing EC49FGW generator, preserve its exact observation label, and compute its literal distinct nonempty-prefix optimum. Each root trie is evaluated by exhaustive subset-label DP and root assignments. These are full finite minima for each fixed seven-key set, not merely feasible upper bounds.

| Dropped-key class | Number of coverable sets | Exact prefix-cost histogram | Smallest exact cost |
|---|---:|---|---:|
| #25: remove (3,1,1),(4,2,1),(5,3,1) | 3 | 116:1, 126:1, 150:1 | 116 |
| #26: remove (3,1,1),(4,2,1),(5,4,1) | 3 | 116:2, 142:1 | 116 |
| #28: remove (3,1,1),(5,3,1),(5,4,1) | 85 | 102:1, 108:2, 110:2, 116:80 | 102 |
| **Total** | **91** | **All costs >=102** | **102** |

An initial ten-case subset produced the corresponding same exact values. A full 91-case run then finished in 7.92 seconds (peak approximately 9.4 MB for the original C++ solver process in this execution environment). An independently written portable reproduction entry, REPLAY_FIRST91_EC49FMA.py, rebuilt every case and regenerated *identical exact 91 cost bytes* from the original frozen catalogue and untouched EC49FKY solver; it printed EC49FMA_NINETY_ONE_SIGNED_PREFIX_EXACT_PASS. Cost bytes are in lexicographic deleted-triple class and inserted-triple order with class order (25,26,28). Their SHA256 is f5ac7bb47e2a838e02dbb1403864279184d7a213104ea10342652620e0e44c8d.

Thus no one of these 91 specific three-key replacements improves the known 84-prefix seven-key construction. After this round 38,078 of the 38,169 label-coverable radius-three replacements still need native-prefix optimization. The fully unrestricted seven-key objective remains C_min(7) <= 84, with 83-prefix existence open.

Execution and validation: source is the prior published frozen EC49FGW_RADIUS5_SCREEN.py with PIN retained; the C++ solver is the previously published EC49FKY SCAN_7KEY_GENERAL.cpp unchanged. The PR replay entry generates and checks all 91 optimal costs, and EXACT_EARLY91_EC49FMA.json carries the cost vector and case/class histogram. This is author-side finite computational evidence; no independent Driver acceptance or formal Source Result is asserted.