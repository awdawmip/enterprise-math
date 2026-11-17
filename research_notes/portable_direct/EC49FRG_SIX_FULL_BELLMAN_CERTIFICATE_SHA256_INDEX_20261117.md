# EC49FRG original certificate and reproducibility index (2026-11-17)

Parent: [EC49FRF PR #2610](https://github.com/awdawmip/enterprise-math/pull/2610), commit `e3633f0d819888a13e430d66828a5f94d2310bf2`.
Original frozen science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Mathematical status `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`.

## Immutable source-input SHA256

- `source/frozen_original_master.txt`: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`
- `source/EC49FPG_PROFILE.csv`: `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`

The full bundle contains both source files, the prior native solver, a second independent weighted-subset DP, six full machine certificates (including all 228 first-action costs and complete optimal tree representations), two independent replay check results, individual native execution logs, a geometry checker, an exact node plan and the full self-contained EC49FRF inherited evidence archive.

| x | lambda | Raw JSON certificate path relative to bundle root | SHA256 |
|---|---|---|---|
| 105/64 | 8990/155301 | `new_certificates/105_64_8990_155301.json` | `55822a25acdd11e3fa79f1f59c42280b8f3482ce979b51a6dc1efc9c1beb6173` |
| 103/64 | 27590/466241 | `new_certificates/103_64_27590_466241.json` | `4775ab99e39816c1078f5f20223549b5a604290cbb5d6070e052dc9668c7b0c3` |
| 101/64 | 28210/466579 | `new_certificates/101_64_28210_466579.json` | `cac3cb35d549d247879f6fe242f493e7e7031014a0a0fb7f4c01f16f06fb232e` |
| 99/64 | 9610/155639 | `new_certificates/99_64_9610_155639.json` | `f3f11f7c2287a00d48e2fa586163f7538a863541057edf070b9df14aaeea8282` |
| 97/64 | 5890/93451 | `new_certificates/97_64_5890_93451.json` | `b5506fb8f45dbdc0cde73ecaf2326d002d21282b48dc3eda273ec21888b9d6dc` |
| 275/96 | 4030/678997 | `new_certificates/275_96_4030_678997.json` | `fa6e116005a8bcaeeb6d3e936542a62f1fd18c15be7446052cfa6ae4dd801443` |

## Exact execution and validation

```sh
python EC49FRG_GEOMETRY.py
PYTHONPATH=code python code/EC49FRG_INDEPENDENT_VERIFY.py 0 3
PYTHONPATH=code python code/EC49FRG_INDEPENDENT_VERIFY.py 3 6
```

Both independent verifier batches returned three `EXACT_INDEPENDENT_PASS` lines then `ALL_NEW_CERTIFICATES_VERIFIED`; all six exact anchor optima equal the original native results, the candidate A/B value and the complete replay cost of all four named tied optimal trees. Native unrestricted recursion visited approximately 6036–6053 subset states depending on the price; the separate independent recursion visited approximately 5904–5932 subsets. This finite completeness check covers all reachable splits for the exact pinned input and price parameters, not a machine-independent proof of the inherited continuum lemma.

The exact geometry calculation returned 116 nodes, 115 gaps, certified area at least `472935381083996446750513/473288420286142927144128`, and the unique worst regret enclosure gap `[17/6,137/48]`. It used rational arithmetic and integer outward square-root boxes of width `10^-40`, not floating point comparisons for the theorem assertions.

## Complete evidence bundle

File: `EC49FRG_SIX_SEAMS_116NODE_COMPLETE_EVIDENCE_20261117.tar.xz` (conversation artifact delivered alongside PR).
SHA256: **`a156306454093a2d5c164fc1aa936d54915e490415bee4007216c066983186c8`**.
Self-contained archive includes 29 manifest-indexed files, all 29 sizes and SHA256s rechecked after re-extraction. The raw original JSON certificates are in that bundle; this Markdown file provides GitHub-durable scientific results, original certificate hashes and the full recreation contract. In this project connector, the raw compressed bundle is not asserted to be a GitHub blob. A later executor can retrieve the conversation artifact or reproduce the six files from pinned source inputs using the included native script and parameters.

Sources and scripts contain no credentials. Formal `RS-EC49AS` task directory was not found on canonical main during this run; activity, CLAIM, Result and Review are distinct outstanding control association tasks, not properties of these files.

**Next scientific unit:** a parametric unrestricted Bellman lower certificate for one of the 115 narrow price-prior strips, with `[17/6,137/48]` the largest current gap-upper-bound interval. The four-corner bilinear lemma and quadratic seam comparison in the theorem note give two exact-checking reductions.