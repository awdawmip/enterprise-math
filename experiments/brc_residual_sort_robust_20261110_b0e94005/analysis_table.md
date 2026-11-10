# Measured robust residual sorting results

Microseconds per complete sort, including input copy, model construction, allocation, output and destruction.
The strongest control is the fastest median among all 15 preceding candidates plus official pdqsort; it is a retrospective reference, not an executable selector.

| Stage / origin | Condition | n | Strongest control | Control µs | Previous recursive µs | Dense µs | Trim µs | Combined µs | Compact µs | Compact/control speedup |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| calibration / calibration | uniform_1e6 | 100 | full_shift_local | 0.566 | 0.576 | 0.612 | 0.607 | 0.614 | 0.565 | 1.001× |
| regression / calibration | uniform_1e6 | 100,000 | sampled_shift_1024 | 981.996 | 1020.030 | 992.859 | 1014.016 | 1038.837 | 1019.557 | 0.963× |
| regression / regression | uniform_1e6 | 1,000,000 | offset_radix | 12864.132 | 17674.730 | 17616.946 | 17184.619 | 17256.904 | 17777.366 | 0.724× |
| regression / calibration | uniform_1e12 | 100,000 | sampled_recursive_1024 | 1617.058 | 1617.058 | 1717.740 | 1720.688 | 1826.778 | 1674.387 | 0.966× |
| regression / regression | square1e6_s0 | 10,000 | sampled_shift_1024 | 36.143 | 38.401 | 38.708 | 37.376 | 40.589 | 39.457 | 0.916× |
| regression / calibration | square1e6_s0 | 100,000 | sampled_shift_4096 | 245.405 | 443.580 | 457.101 | 279.699 | 276.736 | 445.365 | 0.551× |
| regression / regression | square1e6_s0 | 1,000,000 | sampled_recursive_1024 | 2887.660 | 2887.660 | 2898.184 | 2850.101 | 2851.780 | 2795.650 | 1.033× |
| regression / regression | jitter1e6_B20_D8 | 10,000 | sampled_recursive_1024 | 27.782 | 27.782 | 28.648 | 27.759 | 28.583 | 29.876 | 0.930× |
| calibration / calibration | jitter1e6_B20_D8 | 100,000 | sampled_shift_1024 | 221.112 | 226.673 | 238.762 | 218.324 | 230.780 | 224.509 | 0.985× |
| regression / regression | jitter1e6_B20_D8 | 1,000,000 | sampled_recursive_1024 | 2824.474 | 2824.474 | 2830.748 | 2889.805 | 2979.952 | 2846.955 | 0.992× |
| regression / regression | square900_s0 | 100,000 | sampled_recursive_1024 | 227.477 | 227.477 | 401.436 | 229.792 | 400.839 | 256.373 | 0.887× |
| regression / regression | jitter900_B20_D8 | 100,000 | sampled_recursive_1024 | 228.017 | 228.017 | 419.875 | 224.079 | 412.165 | 282.759 | 0.806× |
| regression / regression | square900_s1790 | 100,000 | sampled_shift_1024 | 233.441 | 242.443 | 399.812 | 223.150 | 421.672 | 269.022 | 0.868× |
| regression / regression | square1e6_s1999990 | 100,000 | sampled_recursive_1024 | 222.665 | 222.665 | 227.155 | 221.101 | 233.894 | 223.512 | 0.996× |
| calibration / calibration | square1e6_B256_D8 | 100,000 | sampled_shift_4096 | 328.291 | 426.727 | 429.110 | 419.032 | 427.634 | 456.236 | 0.720× |
| regression / calibration | square1e6_B256_D512 | 100,000 | sampled_recursive_1024 | 1367.613 | 1367.613 | 1373.460 | 1383.642 | 1397.587 | 1406.073 | 0.973× |
| regression / calibration | unique1e6_B256_D512 | 100,000 | affine_square_local | 1017.962 | 1338.525 | 1378.332 | 1398.792 | 1343.268 | 1374.887 | 0.740× |
| regression / regression | square3e9_B20_D8 | 100,000 | sampled_shift_1024 | 230.143 | 236.764 | 230.535 | 235.371 | 232.989 | 235.466 | 0.977× |
| regression / regression | square900_anchor7 | 100,000 | sampled_recursive_1024 | 227.933 | 227.933 | 417.293 | 231.853 | 438.581 | 269.378 | 0.846× |
| calibration / calibration | uint64_top_window | 100,000 | offset_radix | 878.478 | 1422.994 | 1428.049 | 1432.320 | 1383.552 | 1416.410 | 0.620× |
| regression / regression | heldout_jitter_K8 | 100,000 | sampled_shift_1024 | 228.310 | 229.960 | 230.727 | 233.674 | 233.571 | 230.735 | 0.989× |
| regression / regression | heldout_jitter_K2 | 100,000 | sampled_recursive_1024 | 224.347 | 224.347 | 229.687 | 232.649 | 223.269 | 230.789 | 0.972× |
| regression / regression | heldout_jitter_3K4 | 100,000 | sampled_shift_1024 | 227.681 | 231.173 | 225.619 | 222.491 | 232.597 | 242.454 | 0.939× |
| regression / regression | positive_jitter_5K4 | 100,000 | sampled_shift_1024 | 223.208 | 229.134 | 227.853 | 221.730 | 226.796 | 227.941 | 0.979× |
| regression / heldout | new_jitter_quarter_seeds | 100,000 | sampled_shift_1024 | 226.024 | 237.483 | 238.291 | 223.207 | 231.343 | 234.649 | 0.963× |
| regression / heldout | new_jitter_threequarter_seeds | 100,000 | sampled_shift_1024 | 224.036 | 231.811 | 230.120 | 223.180 | 226.113 | 230.814 | 0.971× |
| regression / heldout | skew90_cluster0 | 100,000 | sampled_recursive_1024 | 226.328 | 226.328 | 225.018 | 220.218 | 232.958 | 224.612 | 1.008× |
| calibration / heldout | rare_far_cluster | 100,000 | frequency_sort | 446.093 | 1196.696 | 1186.999 | 240.942 | 246.588 | 248.428 | 1.796× |
| calibration / heldout | two_uint64_outliers | 100,000 | sampled_recursive_1024 | 352.486 | 352.486 | 363.971 | 362.300 | 345.304 | 365.579 | 0.964× |
| regression / heldout | sample_position_trap | 100,000 | sampled_shift_1024 | 1898.641 | 2011.627 | 2242.244 | 2046.956 | 2251.512 | 2050.883 | 0.926× |
| calibration / heldout | uniform_uint64 | 100,000 | offset_radix | 2551.867 | 2688.415 | 2610.221 | 2681.365 | 2645.880 | 2604.937 | 0.980× |
| regression / heldout | log_uniform_bits64 | 100,000 | pdqsort | 2591.106 | 3009.329 | 3157.828 | 3152.162 | 3180.376 | 3160.892 | 0.820× |
| calibration / heldout | uniform_4096 | 100,000 | range_count_or_radix | 419.793 | 1088.545 | 452.566 | 1086.758 | 443.107 | 307.932 | 1.363× |
| regression / heldout | power2_separated_clusters | 100,000 | sampled_shift_1024 | 228.061 | 235.439 | 241.499 | 228.701 | 228.241 | 234.646 | 0.972× |
| regression / mechanism | mechanism_quarter_hidden | 100,000 | pdqsort | 173.532 | 429.903 | 565.556 | 425.468 | 572.911 | 419.237 | 0.414× |
| regression / mechanism | mechanism_half_hidden | 32,768 | pdqsort | 68.308 | 187.445 | 257.785 | 192.051 | 262.187 | 194.357 | 0.351× |
| regression / mechanism | mechanism_half_plus_one | 32,768 | pdqsort | 66.798 | 1301.600 | 1314.253 | 1274.156 | 1356.956 | 1274.504 | 0.052× |
| regression / mechanism | mechanism_four_level_chain | 131,072 | flat_frequency | 379.424 | 958.765 | 1323.546 | 932.921 | 1304.422 | 815.653 | 0.465× |
| regression / mechanism | mechanism_child_cell_reject | 16,384 | pdqsort | 38.535 | 164.346 | 196.415 | 181.028 | 217.378 | 181.484 | 0.212× |
| heldout / new_20261110 | fresh_narrow_offsets | 131,072 | sampled_recursive_1024 | 291.856 | 291.856 | 296.549 | 300.721 | 309.326 | 305.040 | 0.957× |
| heldout / new_20261110 | fresh_tail_0p01pct_high | 100,000 | frequency_sort | 587.259 | 651.674 | 677.993 | 251.189 | 243.289 | 233.546 | 2.515× |
| heldout / new_20261110 | fresh_tail_0p3pct_both | 100,000 | flat_frequency | 594.646 | 3761.274 | 3817.455 | 425.139 | 427.488 | 443.525 | 1.341× |
| heldout / new_20261110 | fresh_tail_1pct_high | 100,000 | flat_frequency | 558.025 | 3657.879 | 3941.674 | 318.980 | 310.626 | 319.815 | 1.745× |
| heldout / new_20261110 | fresh_tail_2pct_high | 100,000 | flat_frequency | 659.181 | 4246.394 | 4069.129 | 4293.698 | 4365.929 | 4235.181 | 0.156× |
| heldout / new_20261110 | fresh_tail_5pct_both | 100,000 | flat_frequency | 852.760 | 3689.435 | 3829.409 | 3716.285 | 3827.721 | 3797.304 | 0.225× |
| heldout / new_20261110 | fresh_dense4096_two_extremes | 100,000 | frequency_sort | 987.685 | 1108.746 | 1316.869 | 1022.736 | 1371.213 | 436.354 | 2.263× |
| heldout / new_20261110 | fresh_dense8192_0p3pct_extremes | 131,072 | frequency_sort | 1991.239 | 3640.191 | 3713.692 | 1557.903 | 1590.021 | 859.924 | 2.316× |
| heldout / new_20261110 | fresh_interior_contamination | 100,000 | flat_frequency | 345.837 | 1981.431 | 1937.196 | 2145.847 | 1987.161 | 2055.009 | 0.168× |
| heldout / new_20261110 | fresh_heterogeneous_widths | 100,000 | range_count_or_radix | 577.422 | 764.442 | 738.928 | 743.094 | 732.716 | 734.354 | 0.786× |
| heldout / new_20261110 | fresh_skew97_24clusters | 100,000 | sampled_recursive_1024 | 263.904 | 263.904 | 267.450 | 254.590 | 254.153 | 254.058 | 1.039× |
| heldout / new_20261110 | fresh_uniform_uint64 | 131,072 | pdqsort | 3897.084 | 3927.272 | 4131.997 | 4020.769 | 4010.780 | 4067.269 | 0.958× |
| heldout / new_20261110 | fresh_actual_sampler_trap | 131,072 | pdqsort | 3907.064 | 4490.820 | 4737.244 | 4530.631 | 5150.662 | 4369.280 | 0.894× |
| heldout / new_20261110 | fresh_128clusters_0p3pct_tail | 250,000 | frequency_sort | 1327.369 | 6132.043 | 6009.240 | 1411.611 | 1346.266 | 1361.079 | 0.975× |
| mechanism / new_20261110 | witness_dense_budget_exact | 8,192 | range_count_or_radix | 23.214 | 61.404 | 34.141 | 62.531 | 35.679 | 34.739 | 0.668× |
| mechanism / new_20261110 | witness_dense_budget_plus_one | 8,192 | range_count_or_radix | 23.391 | 60.312 | 77.815 | 62.911 | 77.799 | 36.509 | 0.641× |
| mechanism / new_20261110 | witness_trim16_tail_success | 100,000 | flat_frequency | 334.590 | 3310.798 | 3317.620 | 259.265 | 255.161 | 256.007 | 1.307× |
| mechanism / new_20261110 | witness_trim17_tie_reject | 100,000 | flat_frequency | 336.723 | 3389.235 | 3297.772 | 3350.905 | 3316.790 | 3250.535 | 0.104× |
| mechanism / new_20261110 | witness_sample_constant_extremes | 16,384 | pdqsort | 21.725 | 78.250 | 101.640 | 82.251 | 105.761 | 80.377 | 0.270× |
