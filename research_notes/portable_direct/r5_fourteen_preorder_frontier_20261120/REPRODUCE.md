# R5 fourteen-label dominance frontier reproduction

Date: 2026-11-20. Exact scalar observer only; status NOT_REVIEWED.

## Pin and prerequisites

- Frozen scientific input: enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551, file EXACT_R5_ALL_101_BUDGETS.json, SHA256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b.
- Companion: stages_18.json. Do not replace either with newer data.
- Retain code in ../r5_fourteen_dominance_20261120/ from parent source commit c328562411f49bd9981d54b2eeb9b0220a66986c. It defines canonical maximal 14-way joint masks and original physical prices.
- g++ supporting C++17 and Python 3. No scientific floating-point operations.

Prepare a working copy of the two pinned input files and the existing ../r5_fourteen_dominance_20261120/make_adj.py inside the current working directory (the Python script resolves inputs relative to its own location). Run:

~~~sh
python3 make_adj.py
g++ -O3 -std=c++17 CHECK_PREORDER.cpp -o check_preorder
./check_preorder
~~~

Expected exact line:

~~~text
classes=1906 edges=38127 scc=1066 sink_scc=333 sink_classes=367 old_classes=836 old_pairs=20159 new_classes=876 new_pairs=21301
~~~

All counts include equality/self edges in the graph. SCCs and sinks are computed under full 14-name observation masks, exact prices and either identity or exchange of the two new-name slots. If the prior file layout is reorganized, adjust only the include path while retaining the immutable parent code bytes and pin.

## Exact new Bellman checks

Compile the immutable parent solver and test three pairs:

~~~sh
g++ -O3 -std=c++17 ../r5_fourteen_dominance_20261120/R5_FOURTEEN_F8_ONE.cpp -o r5_fourteen_f8
./r5_fourteen_f8 window_adj.bin 19 88 12000000
./r5_fourteen_f8 window_adj.bin 21 85 12000000
./r5_fourteen_f8 window_adj.bin 19 81 12000000
~~~

Expected exact f8 values: 8335, 8335, 8335. Observed author DP visited states in that order: 5102830, 6099014, 5723293. These are complete finite recursions, not extrapolations. The previous source's solver may report a slightly different memo count if compiled with different equivalent optimizations, but the value is exact.

For the first two pairs independently build all 101 integer left-endpoint masks using the parent's BUILD_ORACLE_14_ACTIONS.py and run its distinct nibble-counter INDEPENDENT_ORACLE_14.cpp:

~~~sh
cp ../r5_fourteen_dominance_20261120/BUILD_ORACLE_14_ACTIONS.py .
cp ../r5_fourteen_dominance_20261120/INDEPENDENT_ORACLE_14.cpp .
python3 BUILD_ORACLE_14_ACTIONS.py 19 88
python3 BUILD_ORACLE_14_ACTIONS.py 21 85
g++ -O3 -std=c++17 INDEPENDENT_ORACLE_14.cpp -o oracle14
./oracle14 ORACLE_14_ACTIONS_U19_V88.txt 8
./oracle14 ORACLE_14_ACTIONS_U21_V85.txt 8
~~~

Both independently return V=8335 with 5,102,830 and 6,099,014 memo states respectively. The third pair has no independent f8 recursion claim in this publication.

The previous 22 benchmark classes all have source-specific published DP results; CHECK_PREORDER.cpp consumes their exact class IDs and adds three new ones. It verifies the resulting union coverage, not merely the count of classes dominated by each new reference in isolation.

## Actual result boundary

20,159/29,646 old certified pairs -> 21,301/29,646 certified pairs (new +1,142). Unresolved after this exact certificate: 1,030 classes and 8,345 named pairs. Structural condensation has 333 sink SCCs, a sufficient group of possible harder benchmark targets under this particular action-level dominance preorder. The original full-256 R5 bound remains 8335<=C8*<=8343. No native X6/BRC/Port equivalence or formal Result/Review is claimed.
