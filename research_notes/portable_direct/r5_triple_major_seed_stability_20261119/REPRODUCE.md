# R5 finite certificate reproduction and source scope

Frozen input: enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551, EXACT_R5_ALL_101_BUDGETS.json SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. Robust chamber tau=58182461585441404127941754879.

The full frozen input (gzip+base64), stages_18.json, source scripts, 40 representative certificates, 248-member exact mapping, independent Python endpoint checker, replay script and SHA256SUMS_TRIPLE.txt were executed and bundled together locally. GitHub contains the theorem, exact C++ solver, summary and full class map. The original data generation script is immutable at https://github.com/awdawmip/enterprise-math/blob/8918531323add63966eaa6a69eff15c0fb152183/research_notes/portable_direct/r5_pair_augmentation_20261119/MAKE_WINDOW_ADJ.py

To reproduce with the original frozen input and stage file in the same directory:

1. Generate `window_adj.bin` from SHA-pinned input with the prior MAKE_WINDOW_ADJ.py.
2. `g++ -O3 -std=c++17 TRIPLE_EXACT_SOLVER.cpp -o solve9`.
3. For the 40 representatives t from TRIPLE_CLASS_MAP.tsv, run `./solve9 8 t t`.
4. Compare every cost vector with `733+947f` for f=0..8.
5. Check all 248 members' original 101-action joint-support signatures against their class representative; the separate local independent Python verifier did this and also recomputed f0..f2 for all 40 classes.

Actual executed return: PASS_CPP_40_PRICE_AWARE_SIGNATURE_CLASSES_248_THIRD_LABELS_F0_TO_F8; PASS_INDEPENDENT_ALL_JOINT_SUPPORTS_248_40; PASS_INDEPENDENT_40_CLASSES_F0_F2 120.

Local complete reproducibility package SHA manifest file hashes (original exact-byte versions):
RESEARCH_TRIPLE.md c7f9f4147770b1ce7c1672c9b10753603ad92d9dca9d9f634354976df886a90f
RESULT_TRIPLE.json 65929d4b28c3dde99c57c5a999ecc232de562a5dd57c4369541daa78cb887f7c
triple_extension.cpp fb8970ca1b2674a80a85070bebf7b06d662acc8f1bfd678093d91569c8c7689e
triple_signature_groups.tsv 74d8a82e5fdafff9d984cef584d202d115f6dc2c9049d7b37560754e389a2b43
TRIPLE_CLASS_CERTIFICATES.json 42bf81599957072b9eae68cdd083baa8d20f1210ba813c52cba4dc603776117b
TRIPLE_CERTIFIED_248.csv 24ecb4ca022e3f0e1b573cc9f09db2a3757492cb4271c33855b431afdd0da705

The GitHub file text and local archive source have different names/reformatted proof text; their claims and exact algorithm are aligned, and hashes above identify only local archive bytes. The remote publication is immutable after its GitHub commit and is verified separately by that commit's readback.
