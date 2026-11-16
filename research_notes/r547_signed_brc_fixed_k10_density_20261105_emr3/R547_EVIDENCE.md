# R547 scientific execution evidence — 2026-11-05

Frozen R462: `18783e01e3646c72b7aab3b16d3f565e83e6446f`. Previous R546: `38e4af26eceed759fe12110032bb3b630e0fe449`.

Run `python R547_VERIFY.py && python R547_INDEPENDENT.py`. Independent test requires SymPy.

```
R547_EXACT_ROUCHE_PASS k 10 degree 19 Catalan 16796 p2 8855
disk_count 19 disjoint_pairs 171 radius 1/1000
max_rouche_ratio_lt_1/39 True
dominant_y_gt 9 other_y_lt 5 dominant_X_gt 79695 other_X_lt 44275
first_1025 514 511 zero 0 adjacent_changes 298 first_changes [5, 8, 12, 15, 19, 22, 25, 29, 32, 36, 39, 43, 46, 49, 53, 56, 60, 63, 67, 70, 73, 77, 80, 84]
```

```
1 +
2 +
3 +
4 +
5 -
6 -
8 +
10 +
12 -
16 +
20 -
24 +
R547_INDEPENDENT_RAW_PASS k 10 raw_H_matches 20 matrices 12
```

The root disks are rational centers checked with exact Fraction/isqrt bounds; floating roots were used solely to propose centers. Infinite-sign and >=1/6 density results follow from the proof and certified simple-root separation, not finite observations. This is an author-side result pending independent mathematical review.
