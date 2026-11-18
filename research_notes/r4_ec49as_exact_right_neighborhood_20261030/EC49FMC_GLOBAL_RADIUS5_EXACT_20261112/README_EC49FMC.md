# EC49FMC — Exact minimum for all radius-five seven-key BRC configurations

2026-11-12. Author-side complete finite result; frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Native CLAIM, Result, independent Driver review and Foundation admission are separate.

## Exact statement

Use the original nine-state BRC catalogue of **178,850 legal ordered operation words**, its **94 complete raw cache keys**, the same **24 (window, DFA-signature) demands**, and the original **ordered signed six-axis native microstep** prefix representation.

For a fixed set `K` of seven complete keys let `C(K)` be the fewest distinct nonempty native microstep prefixes occurring in a choice of one legal operation word for each demand, with each selected word's full key belonging to `K`.

Let the known 84-prefix seed key set be

`S={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}`.

The two global mandatory keys are `F={(2,1,1),(3,0,1)}`. The full *radius-five* family consists of `K=F ∪ T` for any five-element subset `T` of the 87 keys outside `S`.

**Finite theorem:**

\[
\boxed{\min_{T \subseteq U\setminus S,\ |T|=5} C(F\cup T)=114.}
\]

Exactly **1,137** members of this family cover all 24 demands; all other **36,948,720** members lack demand support. The 1,137 exact costs range from **114 to 217**. Precisely two attain 114, at zero-based lexicographic candidate IDs **47** and **638**:

* ID 47: `{(2,1,1),(3,0,1),(2,2,1),(3,3,1),(4,0,1),(4,4,1),(5,5,1)}`.
* ID 638: `{(2,1,1),(3,0,1),(2,2,1),(4,0,1),(5,1,1),(6,2,1),(7,3,1)}`.

This excludes **every radius-five replacement** from any construction with 84 or fewer native prefixes. Other radii and global seven-key optimality remain separate questions; the known global upper bound is still `C_min(7) <= 84`.

## Complete finite argument and checks

1. The frozen native generator supplies every legal word, its raw key, demand label and complete ordered signed-X6 prefix string. The complete word/key/label counts and scientific pin are asserted. OR-ing demand-support masks identifies all radius-five coverable keysets. Enumerating all strictly increasing five-key combinations from the 87 nonseed keys covers the entire radius-five family exactly once and yields 1,137 candidates, independently consistent with the EC49FMB global support census.

2. For each of these 1,137 keysets, use **every** legal operation word with an allowed full key. The existing exact `SCAN_7KEY_GENERAL.cpp` forms a prefix trie for each first signed-microstep root. At each node it carries the map `demand-subset -> minimum number of nonempty selected prefixes`, convolving child subsets by bitwise OR and adding one per occupied nonempty node. The terminal state records all demand labels represented by that exact full prefix. A superset transform produces the least subtree cost for any required demand subset.

3. Assign each of the 24 demands to a root able to realize it; enumerate all root assignments and add the root-optimal costs. Different first-microstep roots have disjoint nonempty prefixes. Every valid solution induces such an assignment; conversely every feasible assignment with selected trie paths gives a legal solution. Thus the solver's integer result is the exact minimum `C(K)` for the keyset, not an approximate relaxation.

4. An actual C++17 run computed **all 1,137** optima (260 cases with three roots and 877 with four). A separate Python standard-library prefix-trie implementation independently checked IDs 47, 638 and 1136, obtaining 114, 114 and 210. The remote `VERIFY_EC49FMC.py` contains the full compressed 1,137-cost vector and SHA-256 integrity check and, when executed without `--limit`, regenerates all keysets, recompiles the *unchanged* C++ solver and compares every exact output. No floating-point tolerances or MIP solver assertions are used.

Full uncompressed per-case results and independent verifier are preserved in the 2026-11-12 conversation evidence archive. The SHA-256 of the 1,137-row `r5_exact_results_all.txt` (including per-root information) is `91edda42b5f500248a2e6c7f426119f225755e04c7a80736dcee15f4c93ace11`. These rows were assembled from bounded local batches, checked for gap-free sequential IDs, matching costs and independent samples.

## Reproduce and continue

Under this research_notes parent directory, reuse:
* `EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py` — frozen legal-word generator;
* `EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp` — existing native prefix solver;
* this directory's `VERIFY_EC49FMC.py` — exact full-family enumerator and comparison driver.

Run `python VERIFY_EC49FMC.py` with Python 3 and C++17 `g++`. A `--limit 3` option offers a fast deterministic smoke test; the default checks all 1,137.

The next useful unit is exact native-prefix optimization of the **62,620 radius-four**, **38,169 radius-three**, and remaining **6,315 radius-two** demand-coverable keysets, reusing completed results before fresh computation, and testing for `<=83` or a global lower bound.

Control observation at this run: native researcher session issuance returned `SESSION_ISSUANCE_QUOTA`; a separate dispatch selected an unrelated Task, `RS-X6-NATIVE-ROTATION-DYNAMICS`. No matching authorized CLAIM or formal Result was made. The record is an author-side scientific checkpoint; no protected worldview or P000 change.
