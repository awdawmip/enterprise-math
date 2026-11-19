# R5 — Addition of class 3 to fourteen-name f8 dominance frontier

Date: 2026-11-20, Asia/Shanghai. Addendum to RESEARCH.md at immutable commit 82f58de3e2f3564066544b240a588bb947438231.

The priced full-joint-observer class 3 has fixed twelve-label seed W=(0,16,32,48,1,64,17,80,18,24,34,82) and two extras (2,19). Using the frozen R5 101-budget integer-window adjacency and exact 14-counter Bellman recursion at f=8:

- V8(W ∪ {2,19}) = **8335**, 6,718,023 memoized nonterminal states; 7 exact priced action classes.
- A separately built doubled-left-endpoint action list with an independent four-bit-per-counter C++ Bellman oracle returned **8335**, also 6,718,023 states; output action-list sha256: fef393eec691483c93450079e69da625fa9334f9e302990f4a0242efe8786d8b.
- Under the same D14 exact cost-and-mask-preorder previously proved, adding class 3 to the original 22 references plus new classes 295/354/291 raises covered signatures from 876 to **891** (additional 15) and named pairs from 21,301 to **21,811** (additional 510). New certified coverage over the original 22 is **55 classes and 1,652 pairs**.
- The remaining **1,015 classes / 7,835 named pairs** are not classified at f8 by this certificate. They are not counterexamples. The 333 sink-SCC structural count and the 8335<=C8*<=8343 full-game interval are unchanged.

Reproduce with the parent's R5_FOURTEEN_F8_ONE.cpp and frozen window_adj.bin:

~~~sh
./r5_fourteen_f8 window_adj.bin 2 19 12000000
python3 BUILD_ORACLE_14_ACTIONS.py 2 19
./oracle14 ORACLE_14_ACTIONS_U2_V19.txt 8
g++ -O3 -std=c++17 CHECK_PREORDER_26.cpp -o check_preorder26
./check_preorder26
~~~

The new 26-reference graph verifier reports: \`classes=1906 edges=38127 scc=1066 sink_scc=333 sink_classes=367 old_classes=836 old_pairs=20159 new_classes=891 new_pairs=21811\`.

Proof scope: finite R5 scalar observation game, exact full-joint supports and physical prices, authored exact DP with independent implementation check. Review NOT_REVIEWED; no native X6/Port/BRC promotion, formal CLAIM/RUN or upper-bound improvement claimed.
