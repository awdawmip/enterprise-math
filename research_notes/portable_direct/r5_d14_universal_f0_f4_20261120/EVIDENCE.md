# D14 low-error f0–f4 evidence ledger

**Freeze:** `enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. Input SHA256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`.

**Complete independent C++ root enumerations, separate f=0..3:**
- 1,906 price-aware joint-observer signatures / 29,646 named pairs; no state-cap exits
- f0 `735` on 1,906/1,906 signatures; f1 `1685`; f2 `2635`; f3 `3585`
- exact complete output file `D14_F0_F3_1906.csv`, 67,914 bytes, SHA256 `0ab8429ec26cdffbf461527fc6185521acf83e43c9e4398fe8ea6419fb99beea`

**Exact f=4 root solves and finite preorder propagation:**
- 334 distinct roots: 50 older witness classes + 6 new references + 278 maximal unresolved classes
- all 334 values `4535`, with visited nonterminal states in [38,354,210,514], total 26,147,116 across separate exact computations
- 221 roots with seven priced actions, 3 with eight, 110 with nine
- root table `D14_F4_ROOTS_334.csv`, 17,793 bytes, SHA256 `e1c075755e978829933f45b0f0dc97541ac0ab09858a15ec5ee171d69429d8d6`
- `dominance_edges_1906.bin` exact size 3,632,836, SHA256 `c5c7c38b678aa5e3830e05895fc59f781bf72f926e5b3c19ea9aeeb262776fa6`; 38,127 directed entries
- matrix readback and 334 root class IDs establish `forall i in [0,1906), exists j in roots: dominance[i,j]=1`; prior 12-label baseline `V4(W)=4535` supplies the lower bound

**Author-run different endpoint construction (not independent mathematical review):**
- directly rebuilt exact doubled-coordinate interval supports from the frozen large-integer centers
- ten (class,f) checks passed: (0,3), (699,3), (1905,2), (35,2), (200,1), (1000,1), (1800,0), (35,4), (699,4), (1504,4)
- verification log `D14_INDEPENDENT_LOW_BUDGET.log` SHA256 `56e07fd41e825a3faf38a76b338eb181532de59f8148eb8dccbd3da164e08eec`

**Full local reproduction and SHA-256 checked custody bundle** (original research conversation attachment): `EnterpriseMath_R5_D14_Universal_F0_F4_20261120.zip`, 22 files, 128,918 bytes, SHA256 `722f09eb9fd3e79cb07746497e3c0d5648096ded9ed36805de741079db839674`. The package contains the frozen 1.55MB JSON, full matrix, class table, result rows, all C++ and Python sources and SHA256 manifest. It was tested by ZIP decompression and per-file manifest equality.

This Git branch publishes theorem, derivation, an executable C++ Bellman implementation, endpoint generator, independent-check and preorder-verification scripts, root IDs and evidence hashes. It does not repin/mutate predecessor scientific sources. Publication is **research evidence, not formal Task Result or independent Review**. f8 unresolved root states are unchanged.
