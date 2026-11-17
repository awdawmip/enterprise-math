# EC49FRF — provenance and exact certificate index

2026-11-17. Frozen scientific input commit: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Inherited EC49FRE: [PR #2607](https://github.com/awdawmip/enterprise-math/pull/2607) @ `e2f8e0c5f1ac33773ac4a5f714ba22ccb4da9ce9`.
Proof and the 110-node geometry: [EC49FRF paper](EC49FRF_110_NODE_MINIMAX_BUDGET_THEOREMS_20261117.md) and [exact Python checker](EC49FRF_110_NODE_EXACT_GEOMETRY.py).

## Complete machine certificates

All certificate files listed below are preserved **with their original full bytes** in the accompanying self-contained `EC49FRF_12_SEAMS_110NODE_BUDGET_ALLOCATION_FULL_EVIDENCE_20261117.tar.xz`, SHA256 `0a72208882510bb7c4cd107203abe8a9fa8045eb1ff5ab4251b9ad05f3087631`. The file names are paths **inside that archive**, not paths represented as GitHub blobs. Do not mistake a SHA index for a remote copy of the raw certificate.

| Price x | Prior λ | Raw weighted Bellman optimum | Archive file | SHA256 |
|---|---|---:|---|---|
| `107/64` | `5270/93113` | 559087966080 | `new_certificates/107_64_5270_93113.json` | `2c2c580d13214d11fdff83f26fbadc19830a1835ff4cc0fce770ae08d218bb8f` |
| `109/64` | `25730/465227` | 2794539054720 | `new_certificates/109_64_25730_465227.json` | `cc66174da6f139f7208db7b8aca5194112673916f62fbacdef1dbb08d41c2eee` |
| `111/64` | `8370/154963` | 931212759680 | `new_certificates/111_64_8370_154963.json` | `ddfa8ae306781113b90556e8ec5c14eecc79b10ef93daf06d73fcfce51100e1c` |
| `113/64` | `24490/464551` | 2792737503360 | `new_certificates/113_64_24490_464551.json` | `9fb5893bb81228ed1d4d907d5f0252f8e242fc9a6ca53c487dbb10e885955d6d` |
| `115/64` | `23870/464213` | 2791836727680 | `new_certificates/115_64_23870_464213.json` | `b46812560a6502fd1078c04ff77934b88095ed1ba058943971f190fff1f90e5d` |
| `117/64` | `62/1237` | 7442495872 | `new_certificates/117_64_62_1237.json` | `242a858e9bee5e65256b1ace148715efd3706156677d2973868cba4fd09c5d9d` |
| `119/64` | `22630/463537` | 2790035176320 | `new_certificates/119_64_22630_463537.json` | `8622c4823a4cb9d896e43f547200405684bf53815d08c1bcfd28de471cda8e7e` |
| `121/64` | `22010/463199` | 2789134400640 | `new_certificates/121_64_22010_463199.json` | `5ec07a492a32c8dd6ff1df13e4f43ad59d88234621ebe8e3a652b4bca960527c` |
| `123/64` | `230/4977` | 29981006720 | `new_certificates/123_64_230_4977.json` | `a8d998ae79ab49a023a7ce2b4f2ac8a9905d262c40ebb65002d878c1b84278e4` |
| `125/64` | `20770/462523` | 2787332849280 | `new_certificates/125_64_20770_462523.json` | `1796eb736aebb45040dc49f6a70cf09b3ac195a6105eb8e8099dc8a1413d120f` |
| `127/64` | `4030/92437` | 557286414720 | `new_certificates/127_64_4030_92437.json` | `72d3e98d3004e0ae832f5a1d1c775195096e6231889b3eecd5d85f6e4a851e52` |
| `129/64` | `6510/153949` | 928510432640 | `new_certificates/129_64_6510_153949.json` | `103a5d14d99bf0fbcce25b1f6d074be6bcef5273e2725a89f9ededc38a4a4e5c` |

All exact critical points were tested against all 228 legal physically labeled first observations, using native unrestricted integer Bellman recursion **and a separate weighted-subset dynamic-programming implementation**. The optimum and all four tied first actions `[32,34,140,142]` agree, and each tied action's complete decision tree is replayed against all 141 named profiles. Each new point's unrestricted recursive solver visited about 6,041–6,052 memoized subsets; the independent checker visited about 5,909–5,922 subsets. Logs and detailed cardinalities are in the archive; state counts of implementations need not match to prove agreement of exact minima.

## Frozen raw sources

- `source/frozen_original_master.txt` SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.
- `source/EC49FPG_PROFILE.csv` SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.
- `code/EC49FQL_ALL_FIRST_BELLMAN.py`: frozen native full Bellman implementation.
- `code/EC49FQI_NATIVE_DATA.py` and `code/EC49FRC_INDEPENDENT_VERIFY.py`: independent loader/checker.
- `INHERITED_EC49FRE_FULL_EVIDENCE_20261117.tar.xz`: the full previous scientific frontier, retained byte-for-byte.
- `EC49FRF_THEOREM.md`: extended full paper with proofs, inherited claims and explicit scientific boundaries.
- `EC49FRF_GEOMETRY.py`, `EC49FRF_GEOMETRY_RESULT.json`: exact area and all 109 outward-sqrt interval comparisons.
- `EC49FRC_INDEPENDENT_VERIFY_0_4.json`, `4_8.json`, `8_12.json`: independent verification results.
- `MANIFEST_SHA256.json`: every archive source/evidence file listed with SHA256 and byte size; 49 manifest entries verified on local re-read.

Reproduce after unpacking:

```bash
python EC49FRF_GEOMETRY.py
PYTHONPATH=code python code/EC49FRC_INDEPENDENT_VERIFY.py 0 4
PYTHONPATH=code python code/EC49FRC_INDEPENDENT_VERIFY.py 4 8
PYTHONPATH=code python code/EC49FRC_INDEPENDENT_VERIFY.py 8 12
```

Scientific status: author-proved, exact finite checked, not independently reviewed. This is an independent portable BRC sensing result; the formal task directory `RS-EC49AS` was absent at current canonical main and no CLAIM, Result, Review or Activity checkpoint is represented by this PR. The next mathematical unit is a genuinely parameterized Bellman lower bound or exact optimal-tree counterexample across the remaining 109 crossover strips, initially targeting the worst enclosure interval `[13/8,53/32]`.