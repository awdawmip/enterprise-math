# Certified whole-bin selection: full measured table

Microseconds per complete sort, including copy, setup, allocations, selection, full output and destruction.
All26 preceding candidates are measured in the same binary. Speedup is control/candidate.

| Stage | Condition | n | Best control | Best µs | Previous combined µs | Certified µs | Previous/certified | Best/certified |
|---|---|---:|---|---:|---:|---:|---:|---:|
| calibration | selection_fresh_popular_wide | 100,000 | robust_dense_1024 | 773.687 | 902.526 | 899.387 | 1.003× | 0.860× |
| calibration | selection_fresh_rare_wide | 100,000 | offset_radix | 714.619 | 855.361 | 772.026 | 1.108× | 0.926× |
| calibration | selection_fresh_tail_12pct_asymmetric | 1,000,000 | selection_combined_1024 | 3651.986 | 3651.986 | 3791.577 | 0.963× | 0.963× |
| calibration | selection_fresh_tail_15pct_high | 100,000 | selection_combined_1024 | 447.946 | 447.946 | 469.836 | 0.953× | 0.953× |
| calibration | selection_fresh_tail_15pct_low | 100,000 | selection_combined_1024 | 435.225 | 435.225 | 440.276 | 0.989× | 0.989× |
| calibration | selection_fresh_uniform_uint64 | 1,000,000 | sampled_recursive_1024 | 14338.578 | 15284.393 | 14875.762 | 1.027× | 0.964× |
| calibration | selection_fresh_narrow_offsets | 1,000,000 | sampled_shift_1024 | 2217.293 | 2270.025 | 2291.137 | 0.991× | 0.968× |
| calibration | selection_fresh_interior_contamination | 100,000 | flat_frequency | 315.313 | 367.552 | 404.733 | 0.908× | 0.779× |
| calibration | selection_fresh_128clusters_12pct_tail | 250,000 | frequency_sort | 892.070 | 975.220 | 1002.480 | 0.973× | 0.890× |
| calibration | witness_density_mass_width | 100,000 | selection_fused_1024 | 492.913 | 585.131 | 672.972 | 0.869× | 0.732× |
| heldout | certified_fresh_three_bins_balanced | 100,000 | offset_radix | 722.863 | 1535.793 | 1468.052 | 1.046× | 0.492× |
| heldout | certified_fresh_three_bins_shifted | 100,000 | sampled_shift_1024 | 730.233 | 1466.617 | 1497.673 | 0.979× | 0.488× |
| heldout | certified_fresh_three_bins_low_dominant | 100,000 | offset_radix | 724.459 | 1080.851 | 1067.713 | 1.012× | 0.679× |
| heldout | certified_fresh_three_bins_high_dominant | 100,000 | sampled_shift_1024 | 715.100 | 1451.234 | 1431.950 | 1.013× | 0.499× |
| heldout | certified_fresh_eight_bins_infeasible | 100,000 | offset_radix | 712.120 | 1020.959 | 1086.307 | 0.940× | 0.656× |
| heldout | certified_fresh_three_bins_million | 1,000,000 | sampled_shift_4096 | 7722.246 | 13211.992 | 14642.752 | 0.902× | 0.527× |
| mechanism | witness_exact_mass_dp | 100,000 | offset_radix | 603.660 | 704.591 | 784.365 | 0.898× | 0.770× |
| mechanism | witness_exact_mass_hidden_majority | 100,000 | pdqsort | 117.911 | 694.404 | 720.089 | 0.964× | 0.164× |
| mechanism | witness_best_singleton | 100,000 | sampled_shift_4096 | 341.078 | 349.518 | 343.887 | 1.016× | 0.992× |
| mechanism | witness_fractional_mass_reject | 100,000 | robust_trim_1024 | 620.809 | 681.289 | 686.400 | 0.993× | 0.904× |
