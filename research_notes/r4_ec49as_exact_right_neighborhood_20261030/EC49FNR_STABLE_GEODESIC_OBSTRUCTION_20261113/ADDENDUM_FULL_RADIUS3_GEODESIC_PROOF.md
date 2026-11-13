# EC49FNR full-radius-three addendum — all eight exchange detours persist in the 38,169-case family

2026-11-13. Author-side exact finite theorem; **NOT_REVIEWED**. Extends the [original EC49FNR graph report](README_EC49FNR.md) without altering the original science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, the definition of whole-cache-key replacement or the ordered signed native BRC prefix-cost objective.

## Strengthened mathematical proposition

Let `R` be the original complete list of **38,169** radius-three, seven-whole-cache-key configurations. Define `G_R` on `R` by connecting one-key replacements exactly when their three exact original native-prefix optimizer observables `(C,m,g)` agree. Let `d_J(K,L)=|K\\L|` be the unrestricted seven-key Johnson distance.

For the **eight specific exceptional endpoint pairs** discovered in [EC49FNQ](https://github.com/awdawmip/enterprise-math/pull/2306) and counted by [EC49FNR](README_EC49FNR.md), their exact shortest paths in the **full 38,169-configuration graph** satisfy:

| Endpoint pair | Endpoint triple `(C,m,g)` | Unrestricted `d_J` | Full-radius-three `d_{G_R}` |
| --- | --- | ---: | ---: |
| 32275–32703 | (144,1,1) | 2 | **3** |
| 32276–32719 | (152,1,1) | 2 | **3** |
| 32315–32353 | (154,1,1) | 2 | **3** |
| 32318–32353 | (154,1,1) | 2 | **3** |
| 32703–32951 | (144,1,1) | 3 | **4** |
| 32703–32953 | (144,1,1) | 3 | **4** |
| 32719–32961 | (152,1,1) | 3 | **4** |
| 32719–32963 | (152,1,1) | 3 | **4** |

**Quantifier scope:** exactly these eight pairs, over the finite frozen radius-three family `R`; this theorem does not assert that they are the only obstructions among all 38,169 vertices, or that detours persist under configurations outside `R`.

## Exhaustive obstruction proof

For endpoints `A,B` with `d_J=d`, each step of a `d`-edge shortest Johnson path must remove one of the `d` keys of `A\\B` and insert one of the `d` keys of `B\\A`. The intermediate at depth `r` must therefore be one of exactly `binom(d,r)^2` complete key sets `(A\\D_r)∪I_r`. Exhaustively querying membership in frozen full `R` and evaluating their exact `(C,m,g)` is **sufficient to exclude every possible `d`-step triple-stable path**.

For each of the four `d_J=2` pairs, there are four candidate first intermediates. One is **absent from all 38,169** legal configurations, and three are present inside already-scanned indices 32000–32999 but have an unequal triple. None supports a two-step stable path.

For each of the four `d_J=3` pairs, there are nine candidate first-level and nine candidate second-level configurations. The **full-radius-three enumeration** finds at *each* level exactly four absent configurations, four present but wrong-triple configurations, and **one present matching-triple configuration**. The sole matching first and second candidates are:

| Pair | Matching first level (index) | Matching second level (index) | One-key adjacency between matching levels? |
| --- | ---: | ---: | --- |
| 32703–32951 | 37743 | 32275 | **No** |
| 32703–32953 | 37819 | 32275 | **No** |
| 32719–32961 | 37759 | 32276 | **No** |
| 32719–32963 | 37852 | 32276 | **No** |

Thus no three-edge path can exist in the full family. All eight pairs have explicit three- or four-edge triple-stable paths **already entirely contained** in the original scanned 1000-vertex graph (the prior independently checked EC49FNR BFS). That gives the matching upper bound and proves each exact full-family distance.

The global certification needs native optimizer outputs for precisely **14 previously unevaluated, distinct candidate intermediate configurations**. Their exact raw C++17 result lines and 14 `FINISHED` logs are preserved in `EXACT_14_GATEKEEPER_SCANS.txt` and `EXACT_14_GATEKEEPER_FINISHED.txt`. Frozen original native grammar, source word generator and 24 labels are unchanged. The original exact C++17 trie/subset-DP binary was compiled from the frozen original `scan_cached_radius3_gap.cpp` and run on those 14 case indices, using the original `master_and_radius3_cases.txt` science input; output scan SHA256 is `ff2b2f51b7b2d1854e10095ab84ceccbb10c7955a8e4c9a25c7d3c027117d796`. Separately, original Python `INDEPENDENT_ASSIGNMENT_CHECK.solve` constructed original lawful words and native-root cost functions **independently of C++ source tables** and exactly matched (optimum, optimum-allocation count, next strictly higher cost) for all 14 indices. 

14 exact extra configurations:

| Index | `C` | `m` | Next distinct cost | `g` |
| ---: | ---: | ---: | ---: | ---: |
| 37743 | 144 | 1 | 145 | 1 |
| 37819 | 144 | 1 | 145 | 1 |
| 37759 | 152 | 1 | 153 | 1 |
| 37852 | 152 | 1 | 153 | 1 |
| 33714 | 154 | 2 | 155 | 1 |
| 33157 | 142 | 1 | 149 | 7 |
| 33256 | 154 | 2 | 155 | 1 |
| 33716 | 154 | 1 | 155 | 1 |
| 33159 | 148 | 1 | 155 | 7 |
| 33332 | 154 | 1 | 155 | 1 |
| 33272 | 154 | 1 | 155 | 1 |
| 33854 | 154 | 1 | 155 | 1 |
| 33365 | 161 | 1 | 162 | 1 |
| 33856 | 160 | 1 | 161 | 1 |

## Frozen provenance and reproduction

- Immutable original 1000 optimizer rows: `EC49FNQ` vector (11,000 original decoded bytes, SHA256 `4d6540181b8c25a324aa701f551602ed53156be46b70170f1c104230c6443e9b`) at `f51011eaada023e9732431809ea7e2b9691e79f2`. This was already independently validated for selected original rows; no reoptimization of those 1000 occurred here.
- Complete 38,169-key case catalogue: original `cases.json` in previously archived `EC49FNN_RADIUS3_32000_32999_FULL_EVIDENCE_20261113.tar.xz`, bytes SHA256 `d18c8f3177083c5b39ef6c8ca068589042617a2a797b53f98818a427040e4f33`. It states `count=38169` and the same scientific pin.
- Original generator/word input `master_and_radius3_cases.txt` SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. 
- Reproduce the finite obstruction check: `python3 VERIFY_FULL_RADIUS3_GEODESIC.py <frozen-cases.json> <EC49FNQ-vector.b64> <EXACT_14_GATEKEEPER_SCANS.txt>`. It hashes frozen inputs; checks complete case membership, all 14 exact outputs, the precise eight forbidden shortest routes and the retained shorter-graph positive witness distances. `RESULT_FULL_RADIUS3_GEODESIC.json` preserves its output.
- Reproduce independent native microstep optimization: use frozen FNN independent Python `INDEPENDENT_ASSIGNMENT_CHECK.solve(i)` on exactly the 14 indices, assert triples equal the native C++ scan.

Scientific review remains `NOT_REVIEWED`; this is an exact finite mathematical claim tied to frozen original evidence. No formal `RS-EC49AS` Task publication, CLAIM, Result or Foundation change. The Source read-only task lookup established `NO_CANONICAL_PUBLICATION_DIRECTORY` at immutable control `616f084ec3398ccb656e3e89d41e13b45cf737a2`.

**Next research question:** derive a local criterion on signed native root-cost functions that predicts whether a one-key replacement preserves `(C,m,g)`, and test it on the eight now-global geodesic obstructions. Distinguish missing intermediate configurations from genuinely nonmatching-root alternatives; do not reduce complete cache keys to endpoint-only coordinates.
