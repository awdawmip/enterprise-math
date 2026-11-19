# R5 exact 14-label f=8 reproduction

The frozen input file EXACT_R5_ALL_101_BUDGETS.json and stages_18.json must be obtained from the *same scientific pin*, sha256(EXACT...json)=50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. They were included in the earlier verified R5 reproduction bundles. Set them beside the scripts.

1. python3 MAKE_ADJ.py builds window_adj.bin: for each price k=214..314 and ordered name pair (i,j), the exact byte is 1 iff 0<=N_j(k)-N_i(k)<=tau.
2. g++ -O3 -std=c++17 SOLVE_F8_14.cpp -o solve14; g++ -O3 -std=c++17 CLASSIFY_14.cpp -o classes14
3. ./classes14 window_adj.bin prints PAIRS=29646 CLASSES=1906 and writes CLASSES_14.csv. The groups are the equivalence classes under complete *priced joint* support signatures.
4. ./solve14 window_adj.bin 162 179 8 15000000 (and the other 12 representatives from RESULT.json) yields value 8335 with no state-cap exception. This program also reports best root prices.
5. The local full reproduction bundle includes the pair-membership ledger CLASS_COVERAGE_2717.csv and the independently reconstructed SIGNATURES_SELECTED_13.json. Run VERIFY_14_ENDPOINTS.py against these and the frozen inputs: PASS_R5_FOURTEEN_ENDPOINTS 13 unique_representatives 2717 covered_pairs.

Only f=8 for these thirteen priced classes is new here; f=0..3 for all 1906 classes is an inherited verified predecessor result. No independent all-class f=8 computation or native X6 equivalence is claimed.