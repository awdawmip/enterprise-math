# EC49FOU — Exact finite classification of three native BRC legal-root classes

2026-11-15 · `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`

**Immutable scientific input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Original complete source SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. Original corpus: 94 signed-byte-prefix families, 178,850 words, 38,169 seven-key configurations, 24 named demand labels and roots 03,05,06,07.

## Finite theorem and proof

For configuration K, E(K) is its 24-label vector of *named legal root sets*. For root r and a reachable required label subset S, D^K_r(S) is the exact integer minimum prefix-cover cost produced by the native byte-Trie dynamic program. P(K) is the ordered vector of every reachable, named rooted D^K_r(S). T(K) is the ordered vector of the total cost sum_r D^K_r(S_r(rho)) over every full legal assignment rho.

Let C_j be **all** configurations in the pinned original corpus whose E(K) equals E(j). For each j in {10836,10845,10853} we prove by exhaustive exact computation:

**For every A,B in C_j, T(A)=T(B) if and only if P(A)=P(B).**

Every C_j has exactly 99 configurations and 192 complete assignments. Results:

| Representative j | |C_j| | Root costs/config | Distinct T / P vectors | Equal unordered T pairs = P pairs |
|---|---:|---:|---:|---:|
| 10836 | 99 | 152 | 50 / 50 | 601 |
| 10845 | 99 | 148 | 58 / 58 | 404 |
| 10853 | 99 | 148 | 63 / 63 | 325 |
| **Combined** | **297** | **44,352 root entries** | — | **1,330** |

Across these three *separate* complete classes: 14,553 within-class unordered configuration pairs, 57,024 full-assignment integer evaluations, and **zero** terminal-equal/rooted-unequal pairs.

**Exhaustiveness:** Independently parse each of the original 38,169 configuration records and union the per-key named legal-root masks for each label; the complete corpus has exactly 625 signatures, and each of the three selected signatures has exactly 99 members. For every member and each root, the native Trie forms per-node label-mask minima using union convolution of child states, with one cost per covered nonempty prefix, and then takes minimum over supersets. Export all root coordinates with original label bitmasks; per-representative coordinate counts are 99×152, 99×148 and 99×148. Verify exact presence and uniqueness of every expected (config,root,optional subset) coordinate.

Each of the three signatures has six binary optional labels plus one ternary optional label; their 2^6×3=192 allocations are completely enumerated. The total vector for each configuration is constructed by exact integer sums of the four rooted costs and compared as a full tuple, not by floating point or collision-prone hash alone. Identical P necessarily yields identical T; the verified equality of pair counts (601,404,325 respectively) establishes the reverse implication over each complete finite class.

**Implementation crosschecks:** a separately implemented Python *byte*-Trie directly reconstructs all 896 rooted coordinates for configurations 10836,10840,10845,10846,10853,10857 and compares them to C++17 exports. The C++ extractor built with -O2 and -O3 produced byte-identical 896-row exports on these six configurations. The exact finite theorem is supported by all 44,352 exported coordinates and 57,024 assignment evaluations; the six-case Python reimplementation is a distinct implementation check.

**Evidence:** `EC49FOU_THREE_99_CLASSES_EVIDENCE_20261115.tar.xz`, SHA256 `8a399d8f4bc60ffcdbe2f9b4939a077920936ce85805d82e433a444c8f310f3b`, provided with the research conversation. Archive contents: immutable original input, original C++17 extractor, a self-contained Python exact checker with byte-Trie recalculation, all **44,352** signed-root-profile rows in three CSV files, full checker output, O2/O3 comparison, and per-file SHA256 manifest. The compact numeric report and profile hashes are committed alongside this theorem. The archive can be independently checked without network access. This PR is durable original research material; no Result/Review admission is implied.

**Frontier:** EC49FOT independently completed 147 original classes of size 5–64, including two genuine degree-four subset-dependent native gauges; this study completes three disjoint size-99 classes. The next useful search is the remaining as-yet-unclassified original legal-root classes, especially higher-degree conditional cross-root gauges. P000 and frozen science are unchanged.

**Control attribution:** one exact native topic continuation returned `CANONICAL_REJECTED: unknown current immutable task publication`; a later backend operation reported `BACKEND_IDENTITY_CHECK_UNAVAILABLE` and `operation_sent=false`. Accordingly no active formal CLAIM, authenticated RA checkpoint or formal Result is claimed for this independent portable research.