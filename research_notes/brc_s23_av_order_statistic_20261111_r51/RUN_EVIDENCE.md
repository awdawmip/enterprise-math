# R51 exact execution evidence (2026-11-11, author-side)

Source scientific freeze: `enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`; predecessor Draft PR #2009 at `89f2648f990ee176e280ff30f0634d95f1544f42`.

Executable `VERIFY_R51.py` is the full source used to generate the nine tests below (Python stdlib only). It creates `R51_CERTIFICATE.json` in the working directory containing each rational enclosure, Stern–Brocot residual certificate, rank thresholds, selected source labels, labelled age vector, and run counters. `VERIFY_R51_COMPACT.py` is an independent, smaller four-family corroborating script. The downloadable local bundle preserves full JSON and observed console outputs as distinct artifacts.

```text
PASS_R51 frozen_S23_m128_H225 K 352 top_indices [225, 61, 286, 122, 347] identical_prefix 1 first_change 2 floor_calls 532 loops 9641 bits 88
PASS_R51 quadratic_m5_H8 K 12 top_indices [12, 7, 2, 9, 4, 11, 6] identical_prefix 2 first_change 3 floor_calls 826 loops 18455 bits 110
PASS_R51 quadratic_m8_H17 K 24 top_indices [12, 24, 7, 19, 2, 14] identical_prefix 1 first_change 2 floor_calls 732 loops 16386 bits 111
PASS_R51 quadratic_m16_H25 K 40 top_indices [12, 24, 36, 7, 19, 31] identical_prefix 1 first_change 2 floor_calls 750 loops 17146 bits 112
PASS_R51 quadratic_m17_H9 K 25 top_indices [12, 24, 7, 19, 2, 14] identical_prefix 1 first_change 2 floor_calls 732 loops 16315 bits 111
PASS_R51 quadratic_m23_H31 K 53 top_indices [41, 12, 53, 24, 36, 7] identical_prefix 1 first_change 2 floor_calls 746 loops 16816 bits 112
PASS_R51 quadratic_m5_H1 K 5 top_indices [2, 4, 1, 3, 5] identical_prefix 1 first_change 2 floor_calls 575 loops 12792 bits 109
PASS_R51 quadratic_K_100000 K 100000 top_indices [80782, 47321, 13860, 94642] identical_prefix 4 first_change None floor_calls 634 loops 18252 bits 123
PASS_R51 quadratic_K_1000000 K 1000000 top_indices [470832, 941664, 275807] identical_prefix 3 first_change None floor_calls 504 loops 15396 bits 126
PASS_R51_TOTAL {'passed_cases': 9, 'total_floor_sum_invocations': 6031, 'total_euclidean_iterations': 141199}
```

Validation: seven small families used *independent full phase sorting*, direct cumulative rank oracle, and both rational interval endpoints. Two large-K families used an *independent linear top-k scan* to avoid an O(K)-sized sorted atlas. All comparisons used exact Python integers. No wall-clock improvement claim has been made.

Local executable source SHA-256 `b607ac99f6fa9d49cd33bffcfb999f71c1590296413717a473ca1e868244679e`.
Observed original JSON certificate SHA-256 `768dad2ea5c62fdc4c84b36f972f8dc62c3a75e39e5b11241a4b351244282309`. It includes diagnostic elapsed_seconds, which naturally vary on rerun; compare the exact mathematical fields after rerun.

Additional compact reproduction output:

```text
PASS S23 K 352 top [225, 61, 286, 122, 347] equal-prefix 1
PASS sqrt2 K 12 top [12, 7, 2, 9, 4, 11, 6] equal-prefix 2
PASS sqrt2-m16 K 40 top [12, 24, 36, 7, 19, 31] equal-prefix 1
PASS sqrt2-m23 K 53 top [41, 12, 53, 24, 36, 7] equal-prefix 1
```

Run: `python VERIFY_R51.py` then `python VERIFY_R51_COMPACT.py`. Frozen S23 298-affine-run compiler was last verified in R50 and was **not rerun** during R51; this result concerns phase-order selection and preservation of original interval labels. Publication is author-side research evidence, not shared Result admission or independent review.
