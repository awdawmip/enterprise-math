# Frozen benchmark results

Times are microseconds per full sort, including copy, setup, allocation, output and destruction.
The ordinary reference is the fastest measured median among the eight declared ordinary candidates for each condition. It is not a deployable selector.

| Stage | Condition | n | Best ordinary | Ordinary µs | S1024 µs | S4096 µs | Recursive1024 µs | Recursive speedup |
|---|---|---:|---|---:|---:|---:|---:|---:|
| calibration | uniform_1e6 | 100 | std_sort | 0.491 | 0.545 | 0.517 | 0.583 | 0.843× |
| calibration | uniform_1e6 | 100,000 | offset_radix | 1070.620 | 1102.470 | 1022.350 | 1103.150 | 0.971× |
| regression | uniform_1e6 | 1,000,000 | offset_radix | 13289.953 | 13604.101 | 14082.482 | 17868.963 | 0.744× |
| calibration | uniform_1e12 | 100,000 | offset_radix | 1692.446 | 1790.126 | 1872.610 | 1646.632 | 1.028× |
| regression | square1e6_s0 | 10,000 | frequency_sort | 52.495 | 29.782 | 42.638 | 28.143 | 1.865× |
| calibration | square1e6_s0 | 100,000 | frequency_sort | 491.369 | 248.188 | 275.438 | 261.021 | 1.882× |
| regression | square1e6_s0 | 1,000,000 | frequency_sort | 5048.089 | 3113.436 | 3126.290 | 2981.210 | 1.693× |
| regression | jitter1e6_B20_D8 | 10,000 | flat_frequency | 48.791 | 29.167 | 43.232 | 30.077 | 1.622× |
| calibration | jitter1e6_B20_D8 | 100,000 | frequency_sort | 451.319 | 244.151 | 272.172 | 257.499 | 1.753× |
| regression | jitter1e6_B20_D8 | 1,000,000 | frequency_sort | 5350.325 | 3187.058 | 3507.420 | 3088.158 | 1.733× |
| regression | square900_s0 | 100,000 | range_count_or_radix | 424.915 | 249.022 | 261.392 | 274.084 | 1.550× |
| regression | jitter900_B20_D8 | 100,000 | frequency_sort | 426.914 | 243.543 | 254.283 | 240.457 | 1.775× |
| regression | square900_s1790 | 100,000 | range_count_or_radix | 466.620 | 261.302 | 272.216 | 240.237 | 1.942× |
| regression | square1e6_s1999990 | 100,000 | frequency_sort | 449.742 | 242.297 | 266.727 | 260.764 | 1.725× |
| calibration | square1e6_B256_D8 | 100,000 | full_shift_local | 637.296 | 1069.099 | 317.714 | 418.900 | 1.521× |
| calibration | square1e6_B256_D512 | 100,000 | offset_radix | 1442.377 | 1386.062 | 1768.072 | 1438.668 | 1.003× |
| calibration | unique1e6_B256_D512 | 100,000 | affine_square_local | 923.740 | 1387.978 | 1352.005 | 1547.005 | 0.597× |
| regression | square3e9_B20_D8 | 100,000 | frequency_sort | 445.115 | 263.918 | 271.026 | 262.471 | 1.696× |
| regression | square900_anchor7 | 100,000 | frequency_sort | 432.370 | 250.034 | 264.446 | 274.376 | 1.576× |
| calibration | uint64_top_window | 100,000 | offset_radix | 991.240 | 1091.730 | 1234.823 | 1634.461 | 0.606× |
| regression | heldout_jitter_K8 | 100,000 | frequency_sort | 472.108 | 244.154 | 269.339 | 259.318 | 1.821× |
| regression | heldout_jitter_K2 | 100,000 | frequency_sort | 464.210 | 241.734 | 289.107 | 252.519 | 1.838× |
| regression | heldout_jitter_3K4 | 100,000 | frequency_sort | 527.968 | 241.267 | 267.853 | 246.904 | 2.138× |
| regression | positive_jitter_5K4 | 100,000 | frequency_sort | 491.496 | 245.838 | 248.492 | 262.264 | 1.874× |
| heldout | new_jitter_quarter_seeds | 100,000 | frequency_sort | 456.642 | 235.828 | 255.240 | 236.328 | 1.932× |
| heldout | new_jitter_threequarter_seeds | 100,000 | frequency_sort | 470.821 | 268.523 | 252.592 | 260.526 | 1.807× |
| heldout | skew90_cluster0 | 100,000 | flat_frequency | 393.264 | 247.750 | 270.840 | 229.808 | 1.711× |
| heldout | rare_far_cluster | 100,000 | frequency_sort | 464.068 | 1177.061 | 1969.468 | 1113.852 | 0.417× |
| heldout | two_uint64_outliers | 100,000 | frequency_sort | 499.678 | 378.337 | 939.108 | 384.190 | 1.301× |
| heldout | sample_position_trap | 100,000 | range_count_or_radix | 2065.870 | 1987.881 | 1888.171 | 1971.023 | 1.048× |
| heldout | uniform_uint64 | 100,000 | offset_radix | 2505.581 | 2508.021 | 2902.832 | 2615.660 | 0.958× |
| heldout | log_uniform_bits64 | 100,000 | offset_radix | 3120.825 | 3386.598 | 3045.803 | 3371.152 | 0.926× |
| heldout | uniform_4096 | 100,000 | range_count_or_radix | 460.565 | 935.273 | 1108.608 | 1255.203 | 0.367× |
| heldout | power2_separated_clusters | 100,000 | frequency_sort | 459.997 | 235.339 | 292.140 | 247.682 | 1.857× |
| mechanism | mechanism_quarter_hidden | 100,000 | flat_frequency | 282.320 | 3802.466 | 3781.989 | 441.761 | 0.639× |
| mechanism | mechanism_half_hidden | 32,768 | flat_frequency | 100.322 | 1255.017 | 1262.964 | 200.339 | 0.501× |
| mechanism | mechanism_half_plus_one | 32,768 | flat_frequency | 88.146 | 1134.699 | 1177.968 | 1242.732 | 0.071× |
| mechanism | mechanism_four_level_chain | 131,072 | flat_frequency | 356.539 | 5681.373 | 4905.754 | 975.017 | 0.366× |
| mechanism | mechanism_child_cell_reject | 16,384 | flat_frequency | 61.954 | 556.106 | 600.237 | 167.673 | 0.369× |
