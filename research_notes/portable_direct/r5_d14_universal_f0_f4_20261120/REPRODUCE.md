# Reproducing R5 D14 f=0..4 exact universal plateau

This folder contains the theorem, exact integer C++ Bellman code, the original endpoint-adjacency constructor and the 334 reference-class IDs. The full source evidence packet \`EnterpriseMath_R5_D14_Universal_F0_F4_20261120.zip\` is available with the originating R5 research conversation and includes the large frozen input and matrix plus all 1906×4 and 334×1 output rows, independent endpoint checks, and SHA-256 manifest. Those large frozen scientific inputs are **not duplicated** in this Git branch.

## Source custody

Frozen science: \`awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551\` with \`EXACT_R5_ALL_101_BUDGETS.json\` SHA-256 \`50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b\`.

Immediately preceding D14 files and certified roots: \`enterprise-math@6c23d330d900a6bf29451832fb0e05e4ad777a2f\`, including \`classes_1906.tsv\`, \`dominance_edges_1906.bin\`, \`CERTIFIED_52_CLASSES.csv\`, \`NEW_R5_D14_SEEDS.json\`. Previous exact 278 maximal basis: \`enterprise-math@a3595f6855c7ad94a1cc0a1b7219db2f160c305f\`.

Required input files, available in the frozen evidence ZIP, are \`EXACT_R5_ALL_101_BUDGETS.json\`, \`stages_18.json\`, \`classes_1906.tsv\`, \`dominance_edges_1906.bin\`. Hashes:
- class table \`0d39bca7ea3d9b6a644fc1a7a4571ef8a688944fc515df5850d0d2d5a78dfdaf\`
- preorder matrix \`c5c7c38b678aa5e3830e05895fc59f781bf72f926e5b3c19ea9aeeb262776fa6\`, 3,632,836 bytes, 38,127 directed edges
- f0..3 complete table \`0ab8429ec26cdffbf461527fc6185521acf83e43c9e4398fe8ea6419fb99beea\`
- f4 exact root ledger \`e1c075755e978829933f45b0f0dc97541ac0ab09858a15ec5ee171d69429d8d6\`

## Run

Place the immutable input files alongside \`make_adj.py\` and \`EXACT_D14_BELLMAN.cpp\`.

\`\`\`sh
python3 make_adj.py
c++ -std=c++17 -O3 EXACT_D14_BELLMAN.cpp -o exact14
./exact14 window_adj.bin classes_1906.tsv 0 all > f0.csv
./exact14 window_adj.bin classes_1906.tsv 1 all > f1.csv
./exact14 window_adj.bin classes_1906.tsv 2 all > f2.csv
./exact14 window_adj.bin classes_1906.tsv 3 all > f3.csv
./exact14 window_adj.bin classes_1906.tsv 4 F4_ROOT_IDS_334.txt > f4roots.csv
python3 VERIFY_D14_ORDER_CERT.py
python3 VERIFY_D14_ENDPOINT_SAMPLES.py
\`\`\`

The f4 root set is 334 classes, exactly 50 old reference witnesses + 6 newly added reference witnesses + 278 prior unresolved maximal components; all 334 produce 4535. The preorder coverage verifier requires the produced \`f4roots.csv\`, immutable \`classes_1906.tsv\`, \`dominance_edges_1906.bin\` and all four \`f0.csv\`–\`f3.csv\` files. The independent endpoint verifier reads the frozen input and the class table directly, not \`window_adj.bin\`.

This is a finite model author proof by exact computation, **not** a formal X6 theorem or independent project Review. No unverified f8 result is inferred.