# Actual local execution evidence (2026-11-09 Asia/Shanghai)

All arithmetic decisions in the sourced checker used integer operations or Python standard-library `Fraction`. The locally reconstructed source was checked using `git hash-object` and matched the immutable published checker blob `261d7e22da0e62d667009cb50acfe77ac4e35c3f`.

The 401 one-index run completed:
```
CERTIFIED_PLATEAU 401 H 152517291 M 832465522 narrow 124 beta_bound 402 critical_cells 78170 witnesses_used 50
PASS_S23_AV_ANALYTIC_PLATEAU_401
```

The process requesting 402–410 emitted the eight complete endpoint rows 402–409 appearing in `RUN_EVIDENCE.csv`, then **timed out** before completing index 410. No combined PASS is attributed to that process. A separate 410 run completed:
```
CERTIFIED_PLATEAU 410 H 155940420 M 851141153 narrow 126 beta_bound 411 critical_cells 81568 witnesses_used 52
PASS_SEGMENT_410_410
```

The complete ten records cover **798271 feasible critical cells**; maximum narrow types at an endpoint: **126**. The independent rational endpoint audit printed all ten start/end intervals and:
```
PASS_10_EXACT_FLOOR_ENDPOINT_CONTIGUITY
```

The two-candidate inverse implementation run printed:
```
PASS_TWO_CANDIDATE_INVERSE_10000_SMALL_1640_BOUNDARY_2000_RANDOM
H_400 152136996 H_410 155940420 example_at_155940420 410
NONTRIVIAL_SECOND_CANDIDATE 380806 naive_k 1 correct_i 2
NONTRIVIAL_SECOND_CANDIDATE 761180 naive_k 2 correct_i 3
NONTRIVIAL_SECOND_CANDIDATE 1141475 naive_k 3 correct_i 4
```
A separate exact rational check verified identical `floor(i*Gamma_-)` and `floor(i*Gamma_+)` for every `1<=i<=411`.

Local executed script SHA-256 values for provenance: `s23_401_verify.py` = `84ea49b19b51961710e4f10f5d3ef60cf4546ead36b8d55bd3d399bb5d90cb59`; `s23_401_run.txt` = `9925aa9a91a628c572dec13e81ef4a5e1b009`. Published verification wrappers expose the same pinned checker and mathematical predicates for future reruns.