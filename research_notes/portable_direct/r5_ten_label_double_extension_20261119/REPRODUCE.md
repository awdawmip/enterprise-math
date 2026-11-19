# R5 ten-label pair census: exact reproduction

Frozen scientific source: awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551. Original 256×101 centers file EXACT_R5_ALL_101_BUDGETS.json; SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. Stage file stages_18.json fixes tau=58182461585441404127941754879.

The **complete executed** source/input/result package was created locally in this Chat run, named EnterpriseMath_R5_TenLabel_DoubleExtension_20261119.zip (27 files), ZIP SHA-256 25f8644b990e006d7ef284cc796a51305e7fb48674ccffff302cbf063870ee15. This GitHub directory contains the proof, structured results and independent executable entry; the full raw CSVs, 1.55 MB frozen input and every executed source version are in that local ZIP, not represented as GitHub files by this statement.

The complete archive contains:
- EXACT_R5_ALL_101_BUDGETS.json, stages_18.json, make_adj.py and input hashes;
- R5_TWO_MORE_F01_CENSUS.cpp (all 30,628 pairs, f0/f1);
- R5_TWO_MORE_EXTENDED_CENSUS.cpp (all 30,628 pairs, f0 through f6);
- R5_TWO_MORE_HIGH_F_CENSUS.cpp and R5_TWO_MORE_F_PARTITION.cpp (all 1,490 priced signature classes, f7/f8);
- R5_EXCEPTIONAL_TEN_FULL.cpp (all nine budgets for named exception representatives);
- VERIFY_TEN_INDEPENDENT.py (exact doubled-endpoint oracle, 492 cross-checks);
- R5_TWO_MORE_F08_RESULTS.csv (all 30,628 named pairs × f0..f8, SHA-256 b61c928c99dd0a7e6b5d81852f82ba701848e97b6c9a4430b6987d871782dad7);
- the complete F06 pair table, f7/f8 representative-class tables, count/multiplicity map, stderr logs, and SHA256SUMS.txt.

Reproduce from the ZIP, within its content directory:

\`\`\`sh
sha256sum EXACT_R5_ALL_101_BUDGETS.json
python3 make_adj.py
g++ -O3 -std=c++17 R5_TWO_MORE_EXTENDED_CENSUS.cpp -o ten_extended
./ten_extended 6 > F06_REGENDATA.csv
g++ -O3 -std=c++17 R5_TWO_MORE_HIGH_F_CENSUS.cpp -o ten_high
./ten_high 7 > F7_REGEN.csv
./ten_high 8 > F8_REGEN.csv
g++ -O3 -std=c++17 R5_EXCEPTIONAL_TEN_FULL.cpp -o single_ten
./single_ten 18 24 8
# To run the separate Python oracle, generate R5_TWO_MORE_F04_RESULTS.csv:
./ten_extended 4 > R5_TWO_MORE_F04_RESULTS.csv
python3 VERIFY_TEN_INDEPENDENT.py
\`\`\`

The original f8 high-budget pass was partitioned into four disjoint row blocks, with class IDs 0..600, 601..899, 900..1199 and 1200..1489; output blocks are part of the archive. Its complete 1,490-class reassembly was checked for unique IDs 0..1489, multiplicity total 30,628 and no failed/unknown classes. F7 also covered exactly 1,490 classes. The lower stages f0..f6 were evaluated for all 30,628 named unordered pairs and agreed at class-signature identity. The independent Python oracle obtained PASS_TEN_INDEPENDENT pairs 244 checks 492 rare 4.

This is an **author finite exact calculation**, not an independent scientific review. The predecessor source-to-count transformation from the 954-event data is an upstream pinned dependency and was not repeated; the mathematical claim is exactly the finite query game defined by the frozen 256×101 integer centers and fixed noise endpoint. Do not transfer its scalar compression to signed native X6 or Port observables without a separate observer-and-future-operation certificate.
