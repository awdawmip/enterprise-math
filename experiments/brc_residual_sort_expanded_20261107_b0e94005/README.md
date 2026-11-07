# BRC residual-aware numerical sorting: expanded experiment

Date: 2026-11-07 (Asia/Hong_Kong).

**实测摘要：** 完整基准在受控平移样本上提速约3.74倍，一步校正在根跨度60样本上提速约2.28倍；65个扩大条件中，较强的普通整数排序整体仍占优。配对扰动已把下一瓶颈定位到全局残差跨度及后续输出路径。详见文末完整结果表。

## Question and retained frontier

The user requested a larger actual test after the residual-anchor assessment.
The output remains the full numerical ascending array, with every occurrence
preserved. The record experiment additionally preserves original IDs and checks
stability for the BRC/counting/radix algorithms.

Scientific inputs:

- Original native benchmark: `bd3701324833762da5da40f7367f4cefff1a27e9`,
  `experiments/brc_residual_sort_native_20261105_b0e94005/brc_sort_bench.cpp`.
  Its remote and local Git blob was verified as
  `d1acbf5b4e116ddca63cfd2d300db4f4b441bcb5`.
- Prior residual-anchor derivation:
  `42af1ffcc68a49bbd6ced3658eda4731cc18c692`,
  `research_notes/BRC_SORT_ITERATION_PROSPECTS_AND_RESIDUAL_ANCHOR_20261107_b0e94005.md`.

This work extends the existing exact square-root/residue interface. The carrier
is the joint state `(floor_sqrt(x), x-floor_sqrt(x)^2)`. Its observed output is
the complete numerical order and multiplicity. The pure-value experiment does
not request original-index provenance; the record experiment retains it.
Marginal root and residue histograms are not substituted for joint counts.

## Mathematical increment: one-step recovery on a wider family

Let the actual minimum be `m=K^2+a`, where `K=floor_sqrt(m)>=1` and
`0<=a<=2K`. For each input write `x=(K+j)^2+r`, with `j>=0` and
`0<=r<=2(K+j)`. The complete-anchor prediction is

```text
p = K + floor((x-m)/(2K)).
p - floor_sqrt(x) = floor((j*j+r-a)/(2K)).
```

Because `a<=2K` and `j*j+r>=0`, the error is at least `-1` on the entire
domain `x>=m`, without a small-span assumption. With `s=p*p` computed in a
sufficiently wide integer type:

```text
if s <= x:
    k = p + (x-s >= 2*p+1)
else if s-(2*p-1) <= x:
    k = p-1
else:
    k = exact_integer_sqrt(x)
```

The first branch is exact because the predictor can be at most one below the
true root. The second branch uses `x<p^2` and `(p-1)^2<=x`. The last branch
retains exact recovery for larger overestimates. `K=0` uses the explicit exact
root route.

If the actual root span is `B` and actual residue span is `D`, the anchor residue
is one of those residues, so `r-a<=D-1` and `j<=B-1`. Hence

```text
-1 <= p-floor_sqrt(x) <= floor(((B-1)^2+D-1)/(2K)).
```

Therefore **`(B-1)^2+D-1 < 4K` guarantees that one upward or downward correction
recovers every root**, requiring one complete root for the anchor and no
per-element exact-root fallback. The preceding note's `<2K` condition is the
smaller family on which only an upward correction can be needed. For `K=900`,
`D=8`, the new sufficient condition covers `B<=60`; `B=100` is a useful
out-of-family fallback test. This is an algebraic author derivation, supported
by finite executed checks and shared-context collaborative review.

## Implementations and accounting

### Controlled record interface

`record_bench.cpp` uses 8-byte `uint32 value + uint32 id` records with values
in `[0,1000000]`. Its `brc_fused_old` kernel is inherited unchanged. The new
`brc_residual_direct` changes the origin from `K^2` to the actual minimum;
`brc_residual_correct` additionally applies the exact one-step rule. Both retain
the same representation, counting, output recovery, and 16-probe pilot
(keep the predictor when at least 12 probes succeed). Successful corrections
count as successes for that pilot.

Comparators are `std_sort`, `radix20`, and stable `range_count`. BRC and counting
algorithms are checked for stable equality with a reference. `std_sort` is
checked for order, values, and exact preservation of original record IDs.

### Pure-value interface

`pure_bench.cpp` uses 8-byte `uint64` values. Every algorithm receives only the
array. All four BRC variants use the same joint-count/output implementation:

| Algorithm | State extraction / behavior |
|---|---|
| `brc_fullroot` | Exact restoring integer root for each element |
| `brc_old_onecorrect` | Old square origin, hardware division, one downward correction |
| `brc_residual_div` | Complete origin, hardware division, one up/down correction |
| `brc_residual_recip` | Complete origin, exact reciprocal quotient, one up/down correction |
| `std_sort` | Standard comparison sort |
| `offset_radix` | Radix passes selected by actual `max-min` effective bit width |
| `range_count_or_radix` | Dense range counting, with recorded radix fallback above the cap |
| `frequency_sort` | Hash frequency counts, sort distinct values, output every occurrence |
| `affine_range_local` | Range/n-derived buckets, observed per-bucket ranges, local counting |
| `affine_square_local` | Internally compute `K`, centered width-`2K` buckets, observed local ranges |

The exact reciprocal is `floor(2^64/d)`. Its product estimate is a quotient
underestimate by at most one; a remainder comparison repairs it. Candidate
squares, full-range spans, and grid products use `u128`. The root array uses
`uint32`, which can represent every true `uint64` integer square root.

Joint BRC counting is selected when `B*D<=4194304` and
`B*D<=max(4096,4*n)`. Larger grids use lossless relative root/residue keys and
radix sorting. If such a key needs more than 64 bits, the original values are
radix sorted after the state-construction work; this path is explicitly recorded.
Only occupied joint cells are reconstructed into output values.

The dense counter cap is 4,194,304 cells. Affine counting has at most 65,536
buckets, learns actual local minima/maxima, and uses a density budget of
`max(4096,8*n)`; otherwise it falls back to offset radix. The square-scale affine
baseline computes its own anchor root and receives no generating parameters.
Its counts provide a strong competitor for large numeric gaps and compact
local clusters. No baseline is forced to scan the full large universe.

When the joint grid is used, the full numerical output costs
`anchor setup + state extraction + O(n+B*D)`. Under the stated one-correction
condition, fixed-word state extraction is linear with one complete anchor root.
Fallbacks and representation construction remain part of measured costs.

## Inputs and methodology

The record matrix contains 26 conditions; the pure-value matrix contains 39.
Sizes extend from 100 to 1,000,000 elements. They include uniform inputs, paired
translations, root spans 20/60/100/256, several residual widths, one-basin and
zero-anchor cases, reversed input, sparse values near `10^12` and `9*10^18`,
and a 100,000-distinct-value sample without replacement.

Translations use identical label sequences. Jitter controls preserve actual
minimum/maximum, numeric span, ranks, and multiplicities while moving internal
clusters away from their square alignment. The unique-value generator uses an
odd-multiplier permutation of a power-of-two label domain and includes both
endpoints; it does not obtain uniqueness by sorting the timed input in advance.

Both programs use eight deterministic input banks, seven rounds, and shuffled
algorithm order in each round. Calibration selects repetitions, aiming for
15 ms per record algorithm/round and 12 ms per pure algorithm/round. Large runs
can exceed that target because a round always visits all eight banks. Every
timed call includes input copying, all local allocation and initialization,
model/state construction, sorting, full output, and destruction. Input
generation, correctness checks, and diagnostic counters are outside timing.
Instrumented and uninstrumented implementations are both checked on each bank.

Actual environment: AMD EPYC 9V74 80-Core Processor; Linux x86-64;
GCC 13.3.0; C++20 `-O3 -DNDEBUG -Wall -Wextra`. Both performance programs run
sequentially pinned to CPU 0. The reported quantiles describe seven batch
averages; they are not confidence intervals or cross-machine estimates.

The two interfaces both occupy eight bytes per element but have different value
widths and semantics. Their separate results support within-interface algorithm
comparisons; a cross-interface ratio also includes arithmetic and pipeline
changes. Pure `direct_hits` includes minimum/single-basin reuse; the record
counter excludes it. `prediction_misses` may include subsequently corrected
predictions and is not disjoint from all other diagnostics.

## Validation and reproducibility

- Record optimized validation: 1,000,001 root/codec points; 6,007,006 exact
  quotient points; 142,903 correction-law points; 8,000 paired translation
  points; 5,624 input arrays; six algorithms in both code paths.
- Pure optimized validation: 1,010,025 points against an independent root
  oracle; 100,050 exact quotient checks; 1,576 input arrays; ten algorithms
  in both code paths; paired jitter/translation banks and a 100,000-unique case.
- AddressSanitizer and UndefinedBehaviorSanitizer verification passed for both
  programs. The first record sanitizer process reached a LeakSanitizer `/proc`
  task-enumeration error. Its actual failure is preserved in the receipt;
  rerunning with `ASAN_OPTIONS=detect_leaks=0` passed. Leak checking is therefore
  excluded; address and undefined-behavior checking remain enabled.

Reproduce from this directory with an installed C++20 GCC toolchain:

```bash
python run_experiments.py --max-n 1000000
python run_experiments.py --sanitize --verify-only
python summarize.py
```

The actual original-run receipts and CSVs are retained separately from the
reproduction helper. The CSVs contain every round, not only medians.
`auxiliary_vector_bytes` and `counter_cells` describe named data structures;
they are not measured peak RSS and omit hash node/allocator overhead.

## Source and research status

Current-rule pins: global `c36e525df5094cce80698b9603021922c92588a2`,
Enterprise Math `822c7965917f8dfcc35d5d29cc7de6b9c0c9f105`.
The research session's canonical identity/activity remains unconfirmed. The
current native `em_status` attempt returned
`BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false`; the existing
read-only status request in bridge issue 6696 still had no comments on this
turn's read. No formal CLAIM, independent review, or theorem admission is
asserted. These artifacts preserve the actual author-side implementation,
derivation, validation, and performance results.

## Measured results

### 核心结果

两套程序全部完成：**65个输入条件、546组算法测量、520个真实规模输入银行、每组7轮**。全部基准银行的统计版和实际计时版输出均通过核对。

1. **完整基准修复了平移退化。** 记录接口中，10万个数整体平移1790后，旧版耗时2687.934微秒，完整基准直接命中版718.538微秒，约3.74倍提速；完整求根由平均99368次降到1次。
2. **一步校正扩大了适用范围。** 根跨度60、残差跨度8的10万记录，旧版2512.776微秒，一步校正版1102.641微秒，约2.28倍提速；平均28295.125次向下校正取代逐元素求根，最终只有一次完整求根。
3. **强对照仍整体更快。** 大量重复值时，哈希计频加不同值排序占优；10万个不同值时，最快BRC约804.758微秒，偏移基数排序723.014微秒，标准比较排序5052.157微秒。BRC已接近较强的整数排序实现。
4. **一处基本持平。** B=256、D=8的10万纯值中，最快BRC为682.561微秒，平方尺度仿射局部计数684.632微秒；差约0.3%，七轮有4轮更快，波动区间重叠，按持平解读。
5. **扰动暴露了表示成本。** K=1000000的配对扰动保持秩序、重复结构及实际总跨度，完整基准除法版耗时由669.528升到1404.193微秒。完整求根仍为1次，但全局残差跨度由8升到1986233，使联合矩形从160格膨胀到39724660格，触发坐标基数排序。普通仿射局部计数仍只用160格。
6. **64位倒数乘法没有稳定优于硬件除法。** 相同完整基准/校正/输出代码下，硬件除法版在35/39个条件的中位耗时更低。保留两种实现便于复现；下一步优先减少扫描、状态数组和坐标范围的成本。

### 记录接口：受控公式比较

单位为每次完整排序微秒。old为原融合版；direct为完整基准直接命中版；correct为完整基准加一步校正版。

| family | n | std_sort | radix20 | range_count | old | direct | correct |
|---|---:|---:|---:|---:|---:|---:|---:|
| uniform | 100 | 0.549 | 1.442 | 582.057 | 3.189 | 3.164 | 3.572 |
| uniform | 1000 | 20.873 | 4.116 | 664.645 | 43.481 | 46.031 | 47.861 |
| uniform | 10000 | 468.658 | 41.126 | 648.953 | 494.674 | 481.588 | 482.867 |
| uniform | 100000 | 5608.658 | 362.288 | 1143.157 | 4693.297 | 4669.840 | 4758.661 |
| uniform | 1000000 | 63185.743 | 8218.967 | 16545.683 | 54317.374 | 52249.697 | 53881.846 |
| square_shift0 | 100 | 0.592 | 1.571 | 19.964 | 0.888 | 0.836 | 0.882 |
| square_shift0 | 1000 | 13.651 | 5.058 | 22.641 | 7.261 | 7.239 | 7.508 |
| square_shift0 | 10000 | 308.485 | 34.495 | 44.488 | 74.915 | 70.177 | 68.561 |
| square_shift0 | 100000 | 2981.250 | 327.977 | 295.148 | 726.702 | 693.695 | 717.895 |
| square_shift900 | 100 | 0.529 | 1.467 | 18.832 | 0.874 | 0.840 | 0.863 |
| square_shift900 | 1000 | 13.094 | 4.584 | 20.561 | 6.834 | 6.505 | 6.880 |
| square_shift900 | 10000 | 299.474 | 32.551 | 44.261 | 67.958 | 65.986 | 69.280 |
| square_shift900 | 100000 | 3024.807 | 320.614 | 292.099 | 704.075 | 702.252 | 695.952 |
| square_shift1790 | 100 | 0.516 | 1.418 | 18.023 | 1.322 | 0.834 | 0.856 |
| square_shift1790 | 1000 | 12.330 | 4.488 | 20.744 | 21.524 | 6.648 | 6.610 |
| square_shift1790 | 10000 | 298.277 | 33.761 | 44.375 | 251.498 | 65.742 | 67.646 |
| square_shift1790 | 100000 | 3275.550 | 330.768 | 319.818 | 2687.934 | 718.538 | 789.677 |
| square_shift0 | 1000000 | 35439.405 | 8115.375 | 8044.177 | 14291.546 | 13442.458 | 13597.202 |
| square_shift1790 | 1000000 | 33360.246 | 8125.114 | 7710.105 | 31135.945 | 11849.334 | 11681.500 |
| square_B60 | 100000 | 3796.718 | 372.576 | 374.593 | 2512.776 | 2659.912 | 1102.640 |
| square_B100 | 100000 | 3859.148 | 392.616 | 428.805 | 3553.737 | 3852.648 | 3700.321 |
| full_basin20 | 100000 | 5568.703 | 365.498 | 403.678 | 1356.313 | 1355.328 | 962.668 |
| single_basin | 100000 | 4452.239 | 448.766 | 300.244 | 544.423 | 546.697 | 531.638 |
| zero_anchor | 100000 | 5557.057 | 381.981 | 1170.227 | 4806.355 | 5020.929 | 4865.237 |
| matched_scattered | 100000 | 2943.491 | 350.534 | 851.561 | 3470.774 | 3536.065 | 3588.747 |
| reverse_square1790 | 100000 | 800.810 | 306.995 | 259.868 | 1172.648 | 677.384 | 718.296 |

### 纯数字接口：各条件的实测前沿

每行的BRC列取四个BRC实现中最低的中位耗时，普通对照列取六个普通对照中最低的中位耗时。它们是本实验有限实现集合的比较。各算法全部七轮数据、分位数及处理路径见 `pure_results.csv`。

| family | n | 最快BRC变体 | BRC µs | 最快普通对照 | 对照 µs |
|---|---:|---|---:|---|---:|
| uniform_1e6 | 100 | brc_fullroot | 3.787 | std_sort | 0.614 |
| uniform_1e6 | 1000 | brc_fullroot | 45.932 | offset_radix | 4.846 |
| uniform_1e6 | 10000 | brc_fullroot | 479.928 | offset_radix | 44.005 |
| uniform_1e6 | 100000 | brc_fullroot | 4745.666 | offset_radix | 576.578 |
| uniform_1e6 | 1000000 | brc_fullroot | 51262.039 | offset_radix | 5938.523 |
| square900_s0 | 100 | brc_old_onecorrect | 0.794 | std_sort | 0.615 |
| square900_s0 | 10000 | brc_old_onecorrect | 57.605 | frequency_sort | 38.850 |
| square900_s0 | 100000 | brc_old_onecorrect | 637.033 | range_count_or_radix | 320.724 |
| square900_s900 | 100 | brc_old_onecorrect | 0.821 | std_sort | 0.633 |
| square900_s900 | 10000 | brc_old_onecorrect | 62.928 | frequency_sort | 41.731 |
| square900_s900 | 100000 | brc_old_onecorrect | 643.524 | range_count_or_radix | 315.436 |
| square900_s1790 | 100 | brc_residual_div | 0.857 | std_sort | 0.580 |
| square900_s1790 | 10000 | brc_residual_div | 57.588 | offset_radix | 42.971 |
| square900_s1790 | 100000 | brc_residual_div | 645.504 | range_count_or_radix | 302.051 |
| square1e6_s0 | 10000 | brc_old_onecorrect | 58.336 | frequency_sort | 34.352 |
| square1e6_s0 | 100000 | brc_old_onecorrect | 645.472 | frequency_sort | 261.529 |
| square1e6_s0 | 1000000 | brc_old_onecorrect | 6450.270 | frequency_sort | 2789.455 |
| square1e6_s1999990 | 10000 | brc_residual_div | 69.260 | frequency_sort | 38.294 |
| square1e6_s1999990 | 100000 | brc_residual_div | 708.912 | frequency_sort | 290.851 |
| square1e6_s1999990 | 1000000 | brc_residual_div | 7320.465 | frequency_sort | 2868.810 |
| square1e6_B64_D8 | 100000 | brc_old_onecorrect | 699.593 | frequency_sort | 445.207 |
| square1e6_B256_D8 | 100000 | brc_old_onecorrect | 682.561 | affine_square_local | 684.632 |
| square1e6_B20_D64 | 100000 | brc_old_onecorrect | 676.589 | frequency_sort | 425.366 |
| square1e6_B64_D512 | 100000 | brc_old_onecorrect | 947.806 | offset_radix | 726.031 |
| square1e6_B256_D512 | 100000 | brc_old_onecorrect | 1503.828 | offset_radix | 842.860 |
| unique1e6_B256_D512 | 10000 | brc_residual_div | 99.624 | offset_radix | 73.813 |
| unique1e6_B256_D512 | 100000 | brc_old_onecorrect | 804.758 | offset_radix | 723.014 |
| jitter900_B20_D8 | 10000 | brc_old_onecorrect | 107.768 | frequency_sort | 35.213 |
| jitter900_B20_D8 | 100000 | brc_old_onecorrect | 978.266 | frequency_sort | 294.865 |
| jitter1e6_B20_D8 | 10000 | brc_residual_div | 113.598 | frequency_sort | 40.914 |
| jitter1e6_B20_D8 | 100000 | brc_old_onecorrect | 1284.642 | frequency_sort | 338.951 |
| jitter1e6_B20_D8 | 1000000 | brc_old_onecorrect | 13118.119 | frequency_sort | 2999.692 |
| uniform_1e12 | 100 | brc_residual_recip | 6.687 | std_sort | 0.777 |
| uniform_1e12 | 10000 | brc_fullroot | 859.659 | offset_radix | 83.564 |
| uniform_1e12 | 100000 | brc_residual_div | 9133.610 | offset_radix | 1000.893 |
| square3e9_B20_D8 | 100000 | brc_old_onecorrect | 669.674 | frequency_sort | 344.212 |
| square900_B60_D8 | 100000 | brc_old_onecorrect | 1094.932 | range_count_or_radix | 399.536 |
| square900_B20_D1801 | 100000 | brc_residual_div | 1119.388 | offset_radix | 644.369 |
| square900_anchor7 | 100000 | brc_old_onecorrect | 733.989 | frequency_sort | 297.522 |

### 下一问题

优先研究能保留局部残差窄区间的表示，减少全局矩形中的空格子，以及状态提取过程中的额外扫描和数组。扰动数据已经给出明确的区分实验：相同秩序、重复次数和数值跨度下，预测仍然有效，损失发生在残差跨度与后续排序路径。局部残差表、分段/居中基准以及已有BRC状态输入应分别与同样利用局部区间的普通分桶作端到端比较。

对原始均匀随机小数组，当前标准排序仍是合适的基线。当前母目标继续保持为：从自然数输入出发，构造有明确条件、成本和实际收益的专用数值排序方法。

