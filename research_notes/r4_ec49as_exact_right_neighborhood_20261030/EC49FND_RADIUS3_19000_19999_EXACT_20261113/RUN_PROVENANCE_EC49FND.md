# EC49FND exact solver execution provenance

Frozen original BRC input SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

Compiled the previously preserved original `scan_cached_radius3.cpp` with `g++ -std=c++17 -O3 -DNDEBUG` and used the unchanged original master input. The first `scan_r4 19000 21000` scan was interrupted by a local command timeout after **900 complete consecutive rows** (19000–19899) had been emitted. The recovery `scan_r4 19900 20000` completed normally and emitted the remaining **100 rows** (19900–19999) and its terminal `FINISHED` receipt. Concatenation yielded exactly 1000 strictly consecutive nonoverlapping rows, 19000–19999. No other indices were counted.

The concatenated raw 1000-row output has SHA256 `fde4d51f9a76809441f964ed85156b7c8347fde0bfb11f1c51f60771f006aca4`. Its 1000 unsigned exact integer costs encode losslessly with SHA256 `44cdea5f32ebb0483833e80ec5ad48220bd7a8a20e6ef6e614d19a586adea9d9`, stored in `EXACT_CERTIFICATE_EC49FND.json.xz.b64`.

The independent Python trie/subset optimizer matched the C++ optimum for indices 19000,19128,19291,19313,19371,19553,19890,19947,19999. Every one of six 24-word legal native witnesses was checked against the frozen original-word generator and realized 98 unique nonempty ordered signed prefixes. The independently recomputed root-function comparisons cover every one of 8448 root masks for each of the three 8→9 pairs.

Re-running `./scan_r4 19000 20000 < master_and_radius3_cases.txt` computes the entire interval from a single invocation. This artifact documents exact local evidence; native canonical publication, CLAIM, Result, and independent Driver admission are separately controlled.
