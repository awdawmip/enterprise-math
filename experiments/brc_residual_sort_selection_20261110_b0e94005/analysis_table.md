# Residual sorting selection and fused output: full measured table

Microseconds per complete sort, including copy, setup, allocation, full output and destruction.
The reference is the fastest median among all twenty-three frozen controls measured in this same run.

| Stage | Condition | n | Best control | Control µs | Previous adaptive µs | Fused-only µs | Selection-only µs | Combined µs | Combined/control speedup |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| calibration | adaptive_fresh_tail_2p5pct_high | 1,000,000 | flat_frequency | 3475.193 | 3653.032 | 2886.648 | 2558.584 | 2502.213 | 1.389× |
| calibration | adaptive_fresh_tail_7pct_high | 100,000 | flat_frequency | 669.846 | 1082.782 | 1059.472 | 366.905 | 366.621 | 1.827× |
| calibration | adaptive_fresh_tail_20pct_high | 100,000 | flat_frequency | 802.874 | 1236.244 | 1251.199 | 519.292 | 508.387 | 1.579× |
| calibration | adaptive_fresh_tail_30pct_high | 100,000 | flat_frequency | 816.917 | 1350.611 | 1352.161 | 631.170 | 621.727 | 1.314× |
| calibration | adaptive_fresh_tail_12pct_both | 100,000 | adaptive_trim_1024 | 883.318 | 978.295 | 816.135 | 647.106 | 581.584 | 1.519× |
| calibration | adaptive_fresh_tail_40pct_both | 100,000 | adaptive_trim_1024 | 1176.868 | 1225.611 | 1130.467 | 766.073 | 702.182 | 1.676× |
| calibration | adaptive_fresh_interior_contamination | 100,000 | flat_frequency | 276.361 | 303.429 | 259.914 | 301.953 | 253.827 | 1.089× |
| calibration | adaptive_fresh_128clusters_8pct_tail | 250,000 | frequency_sort | 772.116 | 3267.737 | 3153.872 | 892.647 | 876.820 | 0.881× |
| heldout | selection_fresh_tail_8pct_high | 1,000,000 | flat_frequency | 4170.163 | 11507.801 | 10587.601 | 4549.790 | 3672.129 | 1.136× |
| heldout | selection_fresh_tail_8pct_low | 1,000,000 | flat_frequency | 3891.658 | 11077.612 | 9548.952 | 4350.936 | 3554.626 | 1.095× |
| heldout | selection_fresh_tail_12pct_asymmetric | 1,000,000 | flat_frequency | 4217.593 | 10361.257 | 9302.245 | 4466.111 | 3676.470 | 1.147× |
| heldout | selection_fresh_tail_15pct_high | 100,000 | flat_frequency | 695.010 | 1166.095 | 1106.989 | 476.597 | 453.157 | 1.534× |
| heldout | selection_fresh_tail_15pct_low | 100,000 | flat_frequency | 722.676 | 1248.164 | 1139.292 | 488.185 | 427.334 | 1.691× |
| heldout | selection_fresh_popular_wide | 100,000 | offset_radix | 749.460 | 1249.779 | 1221.747 | 876.838 | 862.616 | 0.869× |
| heldout | selection_fresh_rare_wide | 100,000 | offset_radix | 738.552 | 779.228 | 774.084 | 789.038 | 806.245 | 0.916× |
| heldout | selection_fresh_interior_contamination | 100,000 | flat_frequency | 342.276 | 427.300 | 390.517 | 469.573 | 399.230 | 0.857× |
| heldout | selection_fresh_128clusters_12pct_tail | 250,000 | frequency_sort | 862.283 | 3600.656 | 3395.423 | 1014.543 | 971.157 | 0.888× |
| heldout | selection_fresh_narrow_offsets | 1,000,000 | adaptive_prune_1024 | 2351.757 | 2485.504 | 2518.247 | 2338.243 | 2358.804 | 0.997× |
| heldout | selection_fresh_uniform_uint64 | 1,000,000 | sampled_recursive_1024 | 14189.564 | 15162.839 | 15069.093 | 14871.747 | 15104.661 | 0.939× |
| heldout | selection_fresh_tail_40pct_asymmetric | 100,000 | flat_frequency | 1078.943 | 1310.732 | 1306.887 | 812.769 | 762.750 | 1.415× |
| mechanism | witness_density_mass_width | 100,000 | adaptive_combined_1024 | 593.346 | 593.346 | 528.023 | 717.304 | 610.834 | 0.971× |
| mechanism | witness_gap_300_sample_tails | 100,000 | frequency_sort | 260.641 | 1096.238 | 1067.742 | 302.136 | 287.551 | 0.906× |
| mechanism | witness_density_hidden_majority | 100,000 | pdqsort | 118.238 | 760.353 | 737.029 | 774.737 | 742.490 | 0.159× |
| mechanism | witness_fused_tail_position | 100,000 | sampled_shift_4096 | 254.594 | 307.353 | 262.301 | 311.781 | 262.248 | 0.971× |
