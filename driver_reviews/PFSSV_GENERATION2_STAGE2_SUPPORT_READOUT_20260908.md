# PFSSV Stage2 executed-output readout

Researcher-ID: EM-PFSSV-E500C7

Read-only aggregation of the sole published-source execution. This is not a new null simulation or a formal Result. All six actual output files remain unchanged.

All 21 cells have exact occupancy-capacity witnesses. Eighteen also have witnesses after retaining only positive-total-count rows; three currently exhibit only zero-total-target witnesses. Both categories are kept separate.

| X | width | raw pairs | zero-total rows | violating channels | positive-target | zero-target |
|---:|:---|---:|---:|---:|---:|---:|
| 100000 | 1/100 | 237 | 15 | 25 | 14 | 11 |
| 100000 | 3/1000 | 74 | 34 | 4 | 0 | 4 |
| 100000 | 1/1000 | 25 | 30 | 1 | 0 | 1 |
| 300000 | 1/100 | 610 | 7 | 122 | 106 | 16 |
| 300000 | 3/1000 | 183 | 49 | 30 | 7 | 23 |
| 300000 | 1/1000 | 65 | 59 | 8 | 0 | 8 |
| 1000000 | 1/100 | 1960 | 5 | 248 | 231 | 17 |
| 1000000 | 3/1000 | 585 | 58 | 209 | 105 | 104 |
| 1000000 | 1/1000 | 196 | 99 | 113 | 40 | 73 |
| 3000000 | 1/100 | 5826 | 0 | 304 | 304 | 0 |
| 3000000 | 3/1000 | 1743 | 45 | 681 | 516 | 165 |
| 3000000 | 1/1000 | 583 | 135 | 475 | 182 | 293 |
| 10000000 | 1/100 | 18161 | 0 | 723 | 723 | 0 |
| 10000000 | 3/1000 | 5472 | 26 | 1137 | 1012 | 125 |
| 10000000 | 1/1000 | 1832 | 146 | 1506 | 854 | 652 |
| 30000000 | 1/100 | 52396 | 0 | 916 | 916 | 0 |
| 30000000 | 3/1000 | 15664 | 13 | 1381 | 1343 | 38 |
| 30000000 | 1/1000 | 5201 | 136 | 2715 | 1953 | 762 |
| 100000000 | 1/100 | 167952 | 0 | 941 | 941 | 0 |
| 100000000 | 3/1000 | 50326 | 0 | 3270 | 3270 | 0 |
| 100000000 | 1/1000 | 16827 | 89 | 3281 | 2883 | 398 |

The 18,090 counts are cell/target/residue channels, which can overlap across widths; they are not independent trials or p-values. Of these, 15,400 target channels have positive total row counts and 2,690 have zero total row counts. The JSON gives one explicit witness of each present kind per cell, including exact windows, counts, capacities and specified-assignment probabilities.

For X=100000, width=1/100, source p=193 and target p=163 each have total row count 2. In coarse band 6, p mod30=13, q mod30=11, source channel count1 can move to target interval [614,619] of residue capacity0 with probability1/2, also within the positive-total subset. This is not caused by adding a zero-total row.

Successful observations do not license the suspended scientific screen. The scalar surrogate remains a defined distribution, but cannot universally be interpreted as admissible factor-window occupancy. No theorem about all conditional randomization or absence of genuine residual structure follows. Corrected/signed/null vectors remain unavailable, not zero. The two old holdout scales remain post-exposure.

Source execution: f662d48f4615fe6d08a55225c7c36ecd15f91518. Exact precompute SHA256: 7a7e8fe1a11fe157130c4fdf93638db08f54095f6ae5adf20be663d10edf036b.
Readout JSON SHA256: 37991c535f70111bec3f8e37218561a12ab7b7f8bfee0997d27a50e99bc64fb9.
Original actual-output manifest SHA256: 8c5db3a9ea21b5a43324051066b786cb92872afce80970c4bd567cb1b24dc5a5.

No formal Result or Driver review was written by this readout. The owner decides the next bounded handoff.
