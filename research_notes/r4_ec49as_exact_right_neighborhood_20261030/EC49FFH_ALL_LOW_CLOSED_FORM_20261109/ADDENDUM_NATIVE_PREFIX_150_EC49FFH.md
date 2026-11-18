# EC49FFH addendum — 150-edge native-prefix lower certificate for canonical U=9 all-low BRC family

Date: 2026-11-09. Frozen science: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This is a **fixed-key, fixed-quota** exact native signed-X6 result, complementing the unbounded quota/depth formula in `README_EC49FFH.md`.

## Model and exact claim

Require 32 observation groups `(h,s)` with `h=2,...,9` and `s in {1,2,4,8}`. Assign the standard complete BRC key at each window as follows (terminal horizon -> full key):

```
3 -> (3,1,1) for h=2
4 -> (3,2,1) for h=3
6 -> (4,3,1) for h=4,5
10 -> (6,5,1) for h=6,7,8,9
```

For **every** legal selection of one ordered operation word `w_{h,s}` in each of those 32 groups, the number of distinct nonempty ordered signed-native-X6 prefixes obeys

```
                       C_native >= 150 > 93.
```

An explicit 32-word legal construction has `C_native=239`, so this fixed inventory has `150 <= min C_native <= 239`. These bounds apply to the exact assigned-key structure; other key inventories and other quota templates remain separate cases.

## Finite exact proof: 22 depth-separated packing rows

Let `G=(h,s)`, and let `P_d(G)` contain **every** length-d signed-native-X6 prefix of **every** legal original word realizing observation group `G` with its assigned full key. Only use `G` at depth `d` when **all** its candidate words are at least that long.

At each depth `d=1,...,22`, choose the groups in the following certificate. Within a row, the full sets `P_d(G)` are pairwise disjoint, as checked by exhaustively regenerating all original words. Three digits encode `h` followed by two digits of the observation signature (e.g., `404=(h=4,s=4)` and `901=(h=9,s=1)`).

```
d  chosen groups
1  404 602 701
2  404 602 701
3  404 602 701
4  404 602 701
5  208 404 602 701
6  208 404 602 701
7  301 308 404 602
8  308 404 602 701
9  308 404 602 701
10 308 404 602 701
11 404 602 608 701
12 404 504 508 601 602 608 901 902
13 404 504 508 601 602 608 901 902
14 404 504 508 601 602 608 901 902
15 601 602 608 704 901 902
16 601 602 608 704 802 808 901 904
17 601 602 608 704 802 808 901 904
18 601 602 608 704 802 808 901 904
19 601 602 608 704 802 808 901 904
20 601 602 604 608 701 702 704 708 801 802 804 808 901 902 904 908
21 601 602 604 608 701 702 704 708 801 802 804 808 901 902 904 908
22 601 602 604 608 701 702 704 708 801 802 804 808 901 902 904 908
```

For a valid full word selection each chosen group in row `d` contributes a different native prefix at length `d`. Prefixes of different lengths cannot coincide. Consequently

```
C_native >= sum_d |row(d)|
= 3+3+3+3 + 4+4+4+4+4+4+4 + 8+8+8 + 6
  + 8+8+8+8 + 16+16+16
= 150.
```

The exact verifier below recalculates all 9,460 candidate original ordered words (using the frozen operation alphabet, six-axis expansion and nine-state observer), their six-axis endpoints and cache keys, and all 22 rows. It also verifies the explicit 32-word construction (included directly in the script) and its union cost `239`. The proof is therefore an explicit finite integer certificate, not a floating-point optimization claim.

## Validation and continuation

Actually executed `VERIFY_PREFIX_150_EC49FFH.py` with Python standard library. Output: `EXACT_INTEGER_PASS`; groups `32`; original candidate words `9,460`; lower `150`; feasible upper `239`. The 22 depth contributions are

```
(3,3,3,3,4,4,4,4,4,4,4,8,8,8,6,8,8,8,8,16,16,16).
```

This shows how sharply the native-prefix union can differ from the 54-microstep **one-word-per-key** surrogate: the latter optimizes only one representative word per key, whereas this test demands 32 observation-distinct words. The next useful unit is to test alternative quota masks and noncanonical key choices against the native union observer; preserve original word order and key identity.

**Status:** author-side exact fixed-family certificate, branch-only; pending formal native CLAIM/Result and independent Driver admission. P000 and worldview unchanged.
