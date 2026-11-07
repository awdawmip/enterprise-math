# EC49EXH actual local computation, 2026-11-03

Input generator: exact original seven-operation signed native X6 enumeration, with fixed keys and T4/T2 signature sets, 4101 trie nodes, 20 terminal colors, 28 prepaid h2 edges.
Distinct terminal word population by horizon: [4,4,48,24,360,120,245] = 805.
Exact C++17 integer DP kernel stdout (executed):
```
PASS min_extra=62 total=90 nodes=4101 colors=20 largest_states=1048576 convolutions=4581166
```
Exact rational Python witness stdout (executed): PASS E=90 M=4 S=6; all horizon ranks_Q=9; native prefix increments [28,14,16,6,16,6,4].
Independent JS signed-path/modular-rank/native-prefix witness stdout (executed): PASS E=90 M=4 S=6; per-horizon rank 9.
Coverage: all 805 terminal words for **fixed declared keys and signature patterns** are represented in the 4101-node trie; the DP exhaustively selects arbitrary subsets of eligible words by 20-bit OR masks. Global all-key schedule enumeration is an open next unit.
Reproduce:
```
python BUILD_EC49EXH_FIXED_DP.py
g++ -O3 -std=c++17 EXACT_OR_MASK_DP.cpp -o dp
./dp < EC49EXH_FIXED_DP_INPUT.txt
python VERIFY_EC49EXH_WITNESS.py
```
Local full trace and second independent JS checker are retained in the conversation evidence archive.
