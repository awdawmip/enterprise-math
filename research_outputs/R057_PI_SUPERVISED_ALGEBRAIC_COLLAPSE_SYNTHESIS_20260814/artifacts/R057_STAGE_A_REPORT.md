# R057 Stage A — TD000 Teacher Corpus / Cyclic Oriented-D6 Packet Census

Researcher-ID: `EM-R057-6A31F2`

Status: `STAGE_A_FROZEN / AWAITING_DRIVER_REVIEW / NO_GRAMMAR_SCORING`

## Immutable Stage-0 anchors

- `R057_DISCOVERY_PROTOCOL_SHA256 = 65f678619c8dbf8c8e0588356d0fb8a713f94edcb517271de600f846063c8296`
- `R057_INITIAL_TEACHER_DATA_REGISTRY_SHA256 = 7e1491a14538ce455bb4c9bf49461431f184c485987566395069cf02d322e1cf`
- `R057_GRAMMAR_META_PROTOCOL_SHA256 = 6a6a559774311a91b7192f482cebbdf3a33c679ae5ebf914f8bb2e3ce9c681e5`

## TD000 corpus

- circles: **108**
- exact generated cluster cells: **4,914,461**
- exposed boundary edges / cyclic starts per k: **138,380**
- boundary edge range: **330..3106**
- observed closed-boundary turn alphabet: `[-1, 1]`
- corpus integrity stream: `2a3463381d2e9f3296ab2e5a23dda3337afde6e7c2c82694102e9b41188486e0`

All 108 full cyclic boundary direction words are persisted losslessly using packed nibble/base64 encoding. Interior cell lists are not duplicated: each cluster is deterministically regenerable from TD000 and committed by exact `cell_count + sorted-membership SHA256`; the independent checker regenerated every cluster and boundary exactly.

## Oriented-D6 reflection semantics

The canonical object is a CCW boundary with occupied cluster on the left. A spatial reflection reverses orientation, so reflection canonicalization reflects directions and then reverses traversal/edge direction to restore the same CCW occupied-left convention. Free path reversal is not a spatial symmetry, because it would incorrectly identify convex `++` and concave `--` packets.

Regression guard: K=3 convex `++`, mixed, and concave `--` remain three distinct classes while reflection invariance passes.

## Census K=1..8

| k | cyclic packets | raw direction words | oriented-D6 classes | turn alphabet |
|---:|---:|---:|---:|:---|
| 1 | 138,380 | 6 | 1 | `[]` |
| 2 | 138,380 | 12 | 2 | `[-1, 1]` |
| 3 | 138,380 | 24 | 3 | `[-1, 1]` |
| 4 | 138,380 | 37 | 5 | `[-1, 1]` |
| 5 | 138,380 | 62 | 7 | `[-1, 1]` |
| 6 | 138,380 | 92 | 11 | `[-1, 1]` |
| 7 | 138,380 | 140 | 15 | `[-1, 1]` |
| 8 | 138,380 | 190 | 21 | `[-1, 1]` |

Every class stores its canonical direction/turn words, exact endpoint displacement and `Q`, center-normalized squared chord length `Q/3`, total frequency, teacher presence, radius/phase frequencies, and an observed representative.

## Independent exact checker

- status: **PASS**
- regenerated cells: **4,914,461**
- regenerated boundary edges: **138,380**
- packet D6 orbit cases: **6,756**
- failures: **0**
- cyclic-start invariance: PASS
- all six rotations + six orientation-restored reflections: PASS
- packet catalog histogram exact recount: PASS
- class chord/turn invariants: PASS
- R054 sequential reflection-defective parser: not imported

## Explicit Stage-A exclusions

No grammar scoring, operator fitting, symbolic regression, program synthesis, post-selected best mapping, algebraic compression, or scale stress was run. No R057-G selected geometric rules, fitted collapse counts, or fitted coefficients were read or consumed.

## Frozen Stage-A hashes

- `R057_TEACHER_CORPUS_TD000_SHA256 = 177306592b41eaf5140ee562ff216effb287cedf2599626f5bbfa993395fdf3c`
- `R057_PACKET_TYPE_CATALOG_SHA256 = 316c58072cfd6035fe11ca385f543cdd949d49a6960b4d0110868b5f49b96b69`
- `R057_STAGE_A_EXACT_CHECK_RESULTS_SHA256 = 30721a1180a5bacc041ac79b1dd2f8244b875e2b95a7dfbd58d6ab9c03c963b6`
