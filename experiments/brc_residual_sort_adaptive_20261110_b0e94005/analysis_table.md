# Adaptive residual sorting: full measured table

Microseconds per complete sort, including copy, setup, allocation, full output and destruction.
The reference is the fastest median among all twenty frozen controls measured in this same run.

| Stage | Condition | n | Best control | Control µs | Previous compact µs | Ladder µs | Pruning µs | Combined µs | Combined/control speedup |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| calibration | fresh_tail_2pct_high | 100,000 | flat_frequency | 633.567 | 3886.634 | 521.692 | 4108.492 | 518.821 | 1.221× |
| calibration | fresh_tail_5pct_both | 100,000 | flat_frequency | 853.770 | 3871.401 | 733.429 | 4007.079 | 718.371 | 1.188× |
| calibration | fresh_interior_contamination | 100,000 | flat_frequency | 352.926 | 2014.663 | 2045.112 | 348.794 | 358.195 | 0.985× |
| calibration | fresh_dense8192_0p3pct_extremes | 131,072 | robust_compact_1024 | 810.849 | 810.849 | 775.876 | 771.972 | 774.697 | 1.047× |
| calibration | rare_far_cluster | 100,000 | robust_trim_1024 | 259.528 | 269.515 | 265.773 | 260.753 | 266.057 | 0.975× |
| calibration | fresh_uniform_uint64 | 131,072 | pdqsort | 3842.318 | 4276.718 | 4144.923 | 4160.792 | 4224.739 | 0.909× |
| calibration | fresh_narrow_offsets | 131,072 | robust_compact_1024 | 324.544 | 324.544 | 363.766 | 323.715 | 313.330 | 1.036× |
| calibration | fresh_128clusters_0p3pct_tail | 250,000 | robust_trim_1024 | 1193.150 | 1205.475 | 1040.727 | 1220.991 | 1075.229 | 1.110× |
| heldout | adaptive_fresh_narrow_offsets | 1,000,000 | sampled_recursive_1024 | 2891.949 | 3056.397 | 3155.401 | 3222.043 | 3248.876 | 0.890× |
| heldout | adaptive_fresh_tail_2p5pct_high | 1,000,000 | flat_frequency | 5046.624 | 45648.434 | 5343.660 | 46946.999 | 5180.375 | 0.974× |
| heldout | adaptive_fresh_tail_7pct_high | 100,000 | flat_frequency | 827.102 | 4241.645 | 1808.755 | 3898.520 | 1843.057 | 0.449× |
| heldout | adaptive_fresh_tail_20pct_high | 100,000 | flat_frequency | 1018.050 | 3910.766 | 2722.831 | 3777.495 | 2529.555 | 0.402× |
| heldout | adaptive_fresh_tail_30pct_high | 100,000 | flat_frequency | 1052.246 | 3828.820 | 3833.375 | 3795.989 | 3752.694 | 0.280× |
| heldout | adaptive_fresh_tail_12pct_both | 100,000 | pdqsort | 1120.242 | 3719.049 | 1375.199 | 3807.883 | 1442.574 | 0.777× |
| heldout | adaptive_fresh_tail_40pct_both | 100,000 | flat_frequency | 1682.738 | 3913.158 | 2557.660 | 4139.445 | 2564.408 | 0.656× |
| heldout | adaptive_fresh_dense8192_extremes | 131,072 | robust_compact_1024 | 802.974 | 802.974 | 727.898 | 850.608 | 790.870 | 1.015× |
| heldout | adaptive_fresh_interior_contamination | 100,000 | flat_frequency | 370.580 | 2049.262 | 2049.359 | 398.725 | 392.785 | 0.943× |
| heldout | adaptive_fresh_heterogeneous_widths | 100,000 | range_count_or_radix | 625.427 | 748.824 | 766.225 | 802.861 | 711.413 | 0.879× |
| heldout | adaptive_fresh_uniform_uint64 | 1,000,000 | pdqsort | 33232.012 | 36532.820 | 35659.665 | 35091.686 | 35126.212 | 0.946× |
| heldout | adaptive_fresh_128clusters_8pct_tail | 250,000 | frequency_sort | 1368.109 | 6931.518 | 6115.810 | 7069.252 | 5924.414 | 0.231× |
| mechanism | witness_central4_poison_prune | 100,000 | sampled_shift_4096 | 297.587 | 1169.633 | 477.386 | 370.063 | 363.240 | 0.819× |
| mechanism | witness_original_cells_plus_one | 8,192 | pdqsort | 21.993 | 120.680 | 115.427 | 117.063 | 116.915 | 0.188× |
| mechanism | witness_prune_sample_mass_reject | 100,000 | flat_frequency | 346.701 | 3347.655 | 370.109 | 3378.411 | 403.858 | 0.858× |
| mechanism | witness_pruned_actual_majority_reject | 100,000 | pdqsort | 134.385 | 1788.300 | 429.109 | 1951.214 | 1888.618 | 0.071× |
