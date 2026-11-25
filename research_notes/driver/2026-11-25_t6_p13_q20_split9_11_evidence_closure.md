# T6 p13 q20 split(9,11): scoped evidence closure for c451–500

2026-11-25. Existing Driver lane EM-DVR-DEBB5E, author-side repeat verification of missing evidence only; NOT_REVIEWED. This is not independent contributor review. Previous checkpoint r569 records 8,103,693,407 source-backed profiles and historical author-reported 859,902,502 profiles in original modulo-four P-index groups 0,2,3 with missing raw logs. Targeted repository search for the latter count returned no results; the present runtime had no prior local log. Re-execute only those three groups to close the missing collision evidence. Preserve valuation-one, cancellation-normalized p13-smooth domain, side caps 2331, Q9 B=810, Q11 B=472, c=810-w(P), and necessary k=4,5,6,1 congruences. No repeated credit for mathematical discovery.

Reproduction: exact definitions preceding int main in [original source](https://github.com/awdawmip/enterprise-math/blob/f7f9693709f9ca2e89870561bd093b16e6786a40/research_notes/driver/2026-11-25_t6_p13_q20_split9_11_budget301_400_four_residues.md), with [hash-index main](https://github.com/awdawmip/enterprise-math/blob/b39de77e9995f6e5ae11968065e12c1a900edf1c/research_notes/driver/2026-11-25_t6_p13_q20_split9_11_c582_600_hash_index.md). Set lo=451, hi=500, iterate z in {0,2,3} rather than all four classes; assert total==859902502 instead of total==expect&&ps==np. The actual equivalent implementation removed unused expect and ps counters. Same descending-j ascending-r positive enumeration, nondecreasing atom indices, horizontal prefixes by weight, 61-bit exact packed residues, 2^28 table storing key+1, linear probing, 2^32-bit filter, full target insertion count checked. No group1 replay. For any target key the insertion sets its filter bit, so no present key is rejected; exact probing to an empty slot is complete since no deletions occur. The four groups partition all positive indices; each group only pairs with horizontal profiles whose residual mass is <=c. Prior independent integer DP counts retained.

Actual local compilation: g++ -O3 -march=native -std=c++17 -pthread verify.cpp -o verify. /usr/bin/time -v ./verify, complete output:

```
Q=9 full=8963595909 P=186647 H=128402
Q=11 full=100750914 P=246181 H=87579
targets=100750914 unique=100750914
group 2 P=3374 profiles=290119119 filter=6728691 hits=0
group 0 P=3245 profiles=281266215 filter=6524198 hits=0
group 3 P=3358 profiles=288517168 filter=6694153 hits=0
TOTAL 859902502 hits=0
User 45.63s; system 1.87s; wall 22.34s; peak RSS 2640344 KiB; swaps 0; exit status 0.
```

All original three group counts match prior reported counts. New exact membership checks 859,902,502, filter survivors 19,947,042, zero hits. Add these new verified logs to the source-backed evidence count, not to the historical discovery count. Source-backed union now 8,963,595,909/8,963,595,909. Complete split(9,11) exclusion at the previously defined necessary-residue scope. No new claim of independence, formal Result, Review, Task or parent closure. q20(10,10) remains; both sides in that split have B=641 and equal domain, so diagonal matches must be excluded before any no-go conclusion; cannot simply apply the asymmetric zero-hit criterion. Prior complete c621–810 source: [final bands](https://github.com/awdawmip/enterprise-math/blob/e9ec4c51cb05a52e0a97d9cfe47a699b6b31d0f5/research_notes/driver/2026-11-25_t6_p13_q20_split9_11_c651_810_hash_index.md).
