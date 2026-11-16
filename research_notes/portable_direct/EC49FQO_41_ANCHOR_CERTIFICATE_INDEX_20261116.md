# EC49FQO — 41-certificate provenance and evidence index

Date 2026-11-16; native BRC class16943; frozen commit `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Scientific status: author-proved / exact finite checked / not reviewed. This companion belongs to the EC49FQO eleven-price theorem.

The local complete archive `EC49FQO_BRC_ELEVEN_PRICE_SLICES_HALVED_GAP_EVIDENCE_20261116.tar.xz` is SHA256 `73a534b0d137c0c1146df0f17f47d5cedb0d1e00e360cb83d902abf17181e1f7`. It contains 41 complete JSON certificates, verified SHA256SUMS, original native data, proof text, two Bellman programs, tree-replay functions and independent logs.

Original data: `frozen_original_master.txt` SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; `EC49FPG_PROFILE.csv` SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

## Sixteen newly computed complete unrestricted Bellman rational anchors

The `integer optimum` field is the optimal total cost under unnormalized weights `310*(b-a)+141*a*m_i` for `lambda=a/b`. Prices `r,t` are the numerator and denominator of `x=r/t`. Every certificate contains all 228 physical initial costs, a full native decision tree per optimal first index, and every original reproducibility hash. 

| x | lambda | Integer optimum | Exact optimal physical first indices | SHA256 (certificate JSON) |
|---|---|---:|---|---|
| 7/6 | 0/1 | 552420 | 32,34 | `ed1389db38c7c7301fa7a4b336a36aab3c9fd8dfcac611a70bf5115ba01f300c` |
| 7/6 | 3410/44159 | 24697286460 | 32,34,140,142 | `b72a4d192fe2fab12397beaee557e4d3650999c5b4ec8dc3271e72646fe3fb03` |
| 7/6 | 620/3299 | 1861390350 | 16,23,140,142 | `29fd2b232afd027c5fab1ab01b0a67a221e911f5fe0bfd5b6525b188d4ce84b5` |
| 7/6 | 1/1 | 584445 | 16,23 | `d2e7ed5870ce1518a6038ff94eab2c5969afb1cf21828dffce421a56e60b0872` |
| 7/4 | 0/1 | 372620 | 32,34 | `fd67963df89cf171f1b79a4f034d98089b5e3a2a61808307bc9034d4eb1755ea` |
| 7/4 | 310/5809 | 2182178040 | 32,34,140,142 | `9ce1b9928d6c3c7d9a4e5c8f742437b7a485f8e7094eb27bb51be20c4b9ee226` |
| 7/4 | 620/3299 | 1251635850 | 16,23,140,142 | `b2df7eb1376765119632f76952218cfa427c82c3cb418586e9ad02a291cee64d` |
| 7/4 | 1/1 | 391275 | 16,23 | `da66f9725e710022348f43dd5df7396e8903993baaffec2e5b2288e14ff1c12b` |
| 9/4 | 0/1 | 376340 | 32,34 | `8b04b36367e7a2391e5adb252e8e77c6d25e38ef8e4c82334d63ffe53f2c1ccc` |
| 9/4 | 310/9569 | 3618197240 | 32,34,140,142 | `61a932c21396d9425fb9f084eaa706320ab54df2f6120d91811c3205680edae9` |
| 9/4 | 620/3299 | 1260814950 | 16,23,140,142 | `8b47ac562c3326657bb750452e2d6409dd0b84e6ce72636fe9186d71f2383ae8` |
| 9/4 | 1/1 | 392685 | 16,23 | `45f4187c3d29962cb0af0a62ec95b5e07d995a798c6da1f5f3207f18677043d0` |
| 17/6 | 0/1 | 571020 | 32,34 | `984361d878d1b8beae20e27575407747493a759564c0fb110e06b7b248412b08` |
| 17/6 | 310/42469 | 24275047860 | 32,34,140,142 | `71adff25ec7574aa2a319366bdd6f838393d53f1b3efc8b1516d267f55a12d75` |
| 17/6 | 620/3299 | 1907285850 | 16,23,140,142 | `acfc2896689acbfcf4eb1ed4952df51c20707f0d7fa7e27c3ef66a1d3eebafa2` |
| 17/6 | 1/1 | 591495 | 16,23 | `35641af01c25050dae2d3cadd00150e15d2ad0df7660dcdc4d116e3397845f7f` |

The 25 previously independently computed certificates are inherited, unchanged, from **EC49FQN** (PR [#2555](https://github.com/awdawmip/enterprise-math/pull/2555)), with original four-slice predecessors EC49FQM ([#2552](https://github.com/awdawmip/enterprise-math/pull/2552)) and EC49FQL ([#2548](https://github.com/awdawmip/enterprise-math/pull/2548)). Their exact per-file fingerprints are preserved in the archive's `EC49FQO_MACHINE_SUMMARY.json` and `SHA256SUMS`. Inherited FQN proof/index is referenced by immutable commit `1100050729398bf5aa20b64f22b4274181c9b58f`; no recomputation of the historical scientific result is claimed.

## Reproduction (standard-library Python 3.10+)

After extraction, from `EC49FQO_EVIDENCE`:

```sh
sha256sum -c SHA256SUMS
PYTHONPATH=code python3 code/EC49FQO_VERIFY_41.py 0
PYTHONPATH=code python3 code/EC49FQO_VERIFY_41.py 1
PYTHONPATH=code python3 code/EC49FQO_VERIFY_41.py 22 29
PYTHONPATH=code python3 code/EC49FQO_VERIFY_41.py 29 33
PYTHONPATH=code python3 code/EC49FQO_VERIFY_41.py 3
```

The verifier rederives the 141 complete profiles and 228 full native observations from immutable source files. Its exact weighted Bellman recurrence enumerates all 209 distinct partition/price classes and all physical root-index alternatives, with a feasible two-query upper bound used only for safe branch-and-bound pruning. It checks each certificate value, every physical optimal first-index set, full stored decision tree replay, `gamma(7/6)=3410/44159`, `gamma(7/4)=310/5809`, `gamma(9/4)=310/9569`, `gamma(17/6)=310/42469`, and the exact analytical eleven-grid bound `25/57076`.

Expected terminal marker: `EC49FQO_CERTIFIED_11_PRICE_GRID_ENCLOSURE_PASS max_gap_bound 25/57076`. Total verification coverage: 41 exact anchor combinations = 25 inherited + 16 new; all 41 have been run by the current author. Verification scope is the frozen complete-profile scalar identification model and the analytical `lambda,x` continuum argument, not another project's physical dynamics or peer review.

**Control:** Independent portable research; no new formal Task/CLAIM/Result/Review or Activity checkpoint asserted. The native scoped task lookup for `RS-EC49AS` read `NO_CANONICAL_PUBLICATION_DIRECTORY` at 2026-11-16 04:29:59 UTC, source `f947bb5df96669b8c6f080287e212654890f9438`.
