# EC49FMN — BRC exact seven-key radius-three continuation, indices 3700–4699

Date: 2026-11-12. Parent: EC49FMM (0–3699). Research branch: PR #1730. Status: AUTHOR-SIDE EXACT FINITE COMPUTATION / UNREVIEWED / NOT ADMITTED. A native research session/task read was requested, but neither CLAIM nor Result authorization is inferred.

## Fixed scientific input and proposition

Pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Frozen nine-state BRC, 178,850 lawful words, 94 complete cache-key types, 24 distinct observation demands, and signed ordered six-axis native microstep prefixes. The complete lexicographically ordered list of 38,169 seven-key configurations at replacement radius 3 is fixed by the source catalog `master_and_radius3_cases.txt`, SHA-256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.

For each candidate key configuration K_i, C(K_i) is the minimum cardinality of the union of *distinct nonempty complete native prefixes* of a selection of lawful witness words that jointly covers all 24 demands. The key set is fixed within each case; identical endpoint displacements but different ordered signed paths remain different prefixes.

**Finite exact result:** `min_{3700 <= i <= 4699} C(K_i) = 116`, achieved precisely at indices `4300, 4459, 4616`. The maximum is `168`. Every integer index in this interval is covered exactly once, with 1,000 consecutive complete solver rows. The histogram is:
`116:3, 122:6, 123:3, 129:2, 130:6, 132:12, 133:1, 137:3, 138:772, 144:6, 146:11, 150:2, 151:1, 152:6, 154:9, 157:1, 160:7, 162:13, 165:1, 166:59, 167:2, 168:74`.
Three signed first-step roots occur in 294 configurations and four in 706. Combined with previously verified 0–3699: `min_{0 <= i <= 4699} C(K_i)=102` (indices 32, 93). The parent seven-key unrestricted objective has a separate known constructive upper bound `C_min(7) <= 84`.

## Exact algorithm and completeness

For each fixed configuration, enumerate all lawful witness words of its seven complete keys, grouping by the first signed native microstep. Build the complete trie of their ordered full-prefix sequences. At each trie node, demand-subset integer dynamic programming takes the minimum number of selected nonempty prefix vertices for each attainable demand mask: combine all children via bitwise OR, add integer subtree costs, and charge one for the current selected prefix. At each root, exact superset closure provides the cheapest realization of any assigned required mask. The outer recursion assigns each of the 24 demands to every possible supporting root and minimizes the sum of root costs. Every witness set induces an admissible assignment; conversely each root-mask solution is realizable by lawful witness words. These two directions establish exact equality for each fixed K_i.

The source was unchanged from EC49FMM: `scan_cached_radius3.cpp` in the EC49FMM full-evidence package and its corresponding frozen master catalog. Two full runs completed 3700–3899 and 3900–4699; a requested 3900–4899 run was stopped after its 800 complete lines, and **only** 3900–4699 were admitted. Rows beyond 4699 were not computed. The preserved 1,000 complete raw rows have SHA-256 `fd50474763af061e33389fcc28dd3b218058cb659ad977655d54e605ea137c06`. The 1,000-byte unsigned-integer cost vector has SHA-256 `b6ef80a52b41b6ae8a19c035ef3b190fa0fbb05085ea6db3dd885528d4daae3b`. See `EXACT_VECTOR_EC49FMN.json` and `VERIFY_EC49FMN.py`.

Independent Python native-prefix-trie DP, constructing lawful words anew from the frozen generator rather than using C++ results, verified `#3700=138`, `#4300=116`, `#4459=116`, `#4616=116`, `#4699=168`. This is a five-case independent crosscheck of the larger full C++ enumeration, not a 1,000-case independent re-exhaustion.

## Reproduction and continuation

To recompute exactly: with the full evidence package's `scan_cached_radius3.cpp`, `master_and_radius3_cases.txt` and frozen BRC generator, run `g++ -std=c++17 -O3 scan_cached_radius3.cpp -o scan`; then `./scan 3700 4700 < master_and_radius3_cases.txt > native_output.txt`; compare 1,000 contiguous IDs, vector values, histogram and raw SHA-256 above. To independently verify chosen cases: `python VERIFY_RADIUS3_SELECTED.py cases.json 3700 4300 4459 4616 4699`. This exact script and generator are preserved in the downloadable full evidence package.

Scientific next unit: index 4700 onward (34,469 of the 38,169 coverable radius-3 configurations remain). Also explore whole-root and cross-key reusable integer lower-bound certificates, and search for an explicit 83-or-fewer prefix seven-key witness, retaining the frozen ordered native path semantics and P000.
