# Reproduce the R5 D14 residual-order reduction

This work uses the original **frozen scalar R5 model**, not newly generated science inputs.

1. Obtain the predecessor evidence bundle `EnterpriseMath_R5_D14_SixRoots_26388_20261120.zip`, preserved in the original R5 research conversation. Its scientific sources and the root results are linked from `awdawmip/enterprise-math@6c23d330d900a6bf29451832fb0e05e4ad777a2f`. The bundle provides the five specific required files: `EXACT_R5_ALL_101_BUDGETS.json`, `classes_1906.tsv`, `dominance_edges_1906.bin`, `CERTIFIED_52_CLASSES.csv`, and `NEW_R5_D14_SEEDS.json`. The predecessor's `make_adj.py` and `SCAN_FRONTIER_MATRIX.cpp` regenerate the matrix from frozen integer windows, if a fresh matrix audit is desired.
2. Place those five unchanged files beside this directory's `RESULT.json` and `VERIFY_R5_D14_POSET.py`.
3. Run `python3 VERIFY_R5_D14_POSET.py`. It requires **Python standard library only**. Expected output: `PASS unresolved 641 SCC 468 maximal 278 minimal 133 maximal_action_counts {7: 166, 8: 3, 9: 109}`.
4. To regenerate the original observation matrix instead of consuming the pinned predecessor copy, run `python3 make_adj.py`, then compile `g++ -O3 -std=c++17 SCAN_FRONTIER_MATRIX.cpp -o matrix`, then `./matrix window_adj.bin` within the predecessor bundle. Independently check that `dominance_edges_1906.bin` has 3,632,836 bytes, SHA256 `c5c7c38b678aa5e3830e05895fc59f781bf72f926e5b3c19ea9aeeb262776fa6`, and 38,127 one-bits/entries. Regeneration overwrites the local derived matrix, not the frozen input.

The script verifies 278 representative IDs and all finite combinatorial claims, but **does not** prove new Bellman root values. Its main conclusion is conditional: 278 distinct root value certificates would suffice and are minimal under this *static-preorder-only proof mechanism*. Every such root remains mathematically unresolved until it has an exact strategy/value certificate. The old 8335..8343 full-game interval remains unchanged.

Provenance: source input SHA256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`; prior reference bundle and GitHub frontiers are separate from the new research branch; no source-bundle byte is silently repinned. The source author's finite recomputation is not independent project Review.
