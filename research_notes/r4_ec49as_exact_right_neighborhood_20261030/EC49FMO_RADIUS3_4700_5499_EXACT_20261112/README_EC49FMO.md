# EC49FMO — Exact seven-cache-key BRC radius-3 continuation, cases 4700–5499

Date: 2026-11-12. Predecessor: EC49FMN (completed radius-3 indices 0–4699). This is author-side exact finite research pending independent Driver admission.

## Frozen mathematical object

Scientific input pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. The model is the same nine-state BRC with 178,850 lawful operation words, 94 complete cache-key types, 24 observation demands and native signed ordered six-axis microstep prefixes. The catalogue master_and_radius3_cases.txt enumerates 38,169 coverable seven-key radius-three configurations in a fixed order, with SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e.

For a fixed seven-key set K, C(K) is the least cardinality of the union of all distinct nonempty **ordered signed native prefixes** of lawful witness words that together cover the 24 observations. Equal net displacements do not identify distinct ordered prefixes.

**Finite theorem for this exact interval:**

    min_{4700 <= i <= 5499} C(K_i) = 104,

with unique minimizer index **5079**. The largest optimum in this interval is 168. Exactly 219 configurations have three first-step roots and 581 have four.

All 800 sequential case identifiers were fully emitted by the unchanged C++17 exact optimizer; none was skipped or duplicated. Raw solver rows SHA256: 5a50f7c37c696896c86fc44ddc6a99aa0d6abf44fb4087537cfc67493ce14d05. The lossless 800-byte cost vector, histogram, and explicit 24-word witness are in [EXACT_DATA_EC49FMO.json](EXACT_DATA_EC49FMO.json). Cost-vector SHA256: fbc72842722f0a97601d387e336a76b677caba4d88f0380054eeaf3b3e63fd3c. A requested scan to index 5699 stopped after 800 complete cases; no index 5500 or later is claimed as finished.

## Exactness of the optimization algorithm

For each signed first-step root r, insert every lawful witness word of the selected seven complete keys into a full ordered-prefix trie. Terminal positions mark all observation labels they can witness. Nonempty trie vertices represent distinct native prefixes, and cost one if a selected terminal is below them. The artificial empty root costs zero.

At every vertex v, integer dynamic programming stores the minimum charged-prefix cost for each attainable mask of observation labels. Combine child masks with bitwise OR and costs by integer addition; optionally include the terminal observations at v; add one to a nonempty selected subtree when v is non-root. An induction on tree height establishes that these are the exact minima for every mask. Superset closure converts an exact observed mask into the minimum cost for at least a requested mask.

For all 24 demands, assign each to a root capable of witnessing it and minimize the sum of the corresponding root-mask costs. Every lawful witness selection induces an assignment with no greater computed cost. Conversely, each minimizing assignment has lawful realizing witnesses in each root and roots have disjoint nonempty prefixes, so their costs add without overlap. Therefore this outer minimization equals C(K) exactly. Exhausting the consecutive 800 indices proves the stated finite-family result.

## Independent cross-check and constructive witness

A separate Python native-prefix-trie solver regenerated lawful words from the frozen generator, without consuming C++ cost values. It returned:

| Index | C++ exact result | Independent Python |
|---|---:|---:|
| 4700 | 168 | 168 |
| **5079** | **104** | **104** |
| 5499 | 160 | 160 |

An independent traceback for case 5079 produced 24 label-distinct lawful words, all belonging to that case's permitted cache keys. Twelve start with signed root 5 and have 51 distinct nonempty prefixes. Twelve start with root 6 and have 53 such prefixes; they cover all 24 demands. The combined union has exactly 104 native prefixes. The explicit labeled full-word byte strings are preserved in the JSON file. The verifier checks membership against the frozen catalogue, all 24 observations and the union's exact size.

Verification (Python standard library for the vector; frozen generator for the word certificate):

    python VERIFY_EC49FMO.py
    python VERIFY_EC49FMO.py /path/to/unpacked/EC49FMN_RADIUS3_3700_4699_EXACT_20261112

Independent root-DP reproduction:

    python VERIFY_RADIUS3_SELECTED.py cases.json 4700 5079 5499

Full 800-case recomputation using the predecessor evidence archive's unchanged solver and catalogue:

    g++ -std=c++17 -O3 scan_cached_radius3.cpp -o scan
    ./scan 4700 5500 < master_and_radius3_cases.txt > EXACT_NATIVE_OUTPUT_4700_5499.txt
    sha256sum EXACT_NATIVE_OUTPUT_4700_5499.txt

Check all row IDs, compressed vector and the hash of the raw rows, rather than only the minimum. The checking script is [VERIFY_EC49FMO.py](VERIFY_EC49FMO.py).

## Scientific consequence and next question

Prior EC49FMI–FMN had exact minimum 102 over indices 0–4699, attained at indices 32 and 93. Accordingly the new *cumulative* range 0–5499 still has exact minimum 102. A separate legal seven-key construction uses 84 prefixes; the unrestricted mother problem retains C_min(7) <= 84. The present 800 configurations give a new finite-family exact certificate and a lawful 104-prefix witness.

Next: begin index **5500**; 32,669 coverable radius-three configurations remain outside the completely solved initial range. Explore a cross-configuration integer lower-bound certificate or a new seven-key construction using at most 83 ordered native prefixes.

## Control and admission

Material is preserved on the existing author-side PR #1730 branch, not on canonical main. Current native query for RS-EC49AS returned CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION. Therefore no formal CLAIM, Result or independent Driver mathematical review is asserted. Any still-pending research-session or inventory request must be checked by its own original receipt. Original frozen scientific inputs, P000 and ACTIVE worldview are unchanged.
