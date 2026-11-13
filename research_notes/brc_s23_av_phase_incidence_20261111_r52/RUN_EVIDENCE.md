# R52 execution evidence — 2026-11-11

Scientific input: `enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. R51 exact rank-oracle predecessor: Draft PR #2014, commit `dffc106cbf006484c1883376543f58ce345f00bf`.

**The full local executable `VERIFY_R52.py` and original 15-family JSON certificate** were run using Python standard library exact integers, together with the frozen R51 oracle. Each tested phase cell was independently reconstructed from `r=1,...,H`, comparing *every* source owner, the complete age vector and every historical interval count; certified interval endpoints were checked on small cases. The repository's independent `VERIFY_R52_COMPACT.py` instead uses direct sorted cuts / independent top-k phase scan, not R51's ranking program.

Original full 15-family log:

```text
PASS_R52 S23_m128_H225_full cells 352 moves 28672 change 290 prefix 1 counts_mask 2
PASS_R52 sqrt2_m5_H8_full cells 12 moves 35 change 8 prefix 2 counts_mask 2
PASS_R52 sqrt2_m8_H17_full cells 24 moves 128 change 18 prefix 1 counts_mask 2
PASS_R52 sqrt2_m16_H25_full cells 40 moves 388 change 39 prefix 1 counts_mask 2
PASS_R52 sqrt2_m23_H31_full cells 53 moves 690 change 50 prefix 1 counts_mask 2
PASS_R52 sqrt2_m8_H99993_lazy cells 5 moves 32 change 0 prefix 5 counts_mask 0
PASS_R52 sqrt2_m8_H999993_lazy cells 4 moves 24 change 0 prefix 4 counts_mask 0
PASS_R52 random_sqrt2_0 cells 36 moves 262 change 21 prefix 1 counts_mask 2
PASS_R52 random_sqrt2_1 cells 62 moves 477 change 20 prefix 2 counts_mask 2
PASS_R52 random_sqrt2_2 cells 47 moves 462 change 41 prefix 1 counts_mask 2
PASS_R52 random_sqrt2_3 cells 57 moves 392 change 19 prefix 2 counts_mask 2
PASS_R52 random_sqrt2_4 cells 40 moves 256 change 19 prefix 1 counts_mask 2
PASS_R52 random_sqrt2_5 cells 50 moves 481 change 40 prefix 1 counts_mask 2
PASS_R52 random_sqrt2_6 cells 61 moves 588 change 23 prefix 2 counts_mask 2
PASS_R52 random_sqrt2_7 cells 38 moves 350 change 37 prefix 1 counts_mask 2
PASS_R52_TOTAL {'case_count': 15, 'total_comparisons': 881, 'total_source_moves': 33237, 'total_change_cells': 625, 'scalar_equal_but_vector_changed': 13}
```

Independent compact executable output (separate cut-order oracle):

```text
PASS_R52_COMPACT frozen_S23 K 352 cells 352 events 28672 vector_changes 290 same_prefix 1 count_masked_changes 290 top [225, 61, 286, 122, 347]
PASS_R52_COMPACT quadratic_m5_H8 K 12 cells 12 events 35 vector_changes 8 same_prefix 2 count_masked_changes 8 top [12, 7, 2, 9, 4]
PASS_R52_COMPACT quadratic_large K 1000000 cells 4 events 24 vector_changes 0 same_prefix 4 count_masked_changes 0 top [470832, 941664, 275807, 746639]
PASS_R52_COMPACT_3_FAMILIES
```

Local full executable SHA-256 `97f51f331e47f6412bfe0262498d02a24768e39db091e8c61cfcacd23fb2deca`. Local original JSON certificate SHA-256 `2d5b026c1ce82167576d8179b0f1d724732c87b2a87961013517ce3f88bc58b3`. The JSON and full executable were additionally preserved in the user-downloadable R52 bundle. Diagnostic elapsed seconds in JSON vary across executions.

**Scope:** exact 15-family software experiment and independently proved incidence theorem. No new S23 298-risk-run compilation. The auxiliary irrational circle rotation is not native Heartbeat X6 dynamics. No independent mathematical reviewer or formal Result/Review admission has signed this author-side material.