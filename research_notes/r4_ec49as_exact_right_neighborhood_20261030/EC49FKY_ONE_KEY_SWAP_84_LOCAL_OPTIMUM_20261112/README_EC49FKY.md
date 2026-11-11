# EC49FKY — Exact one-key-swap local optimality of the 84-prefix seven-key BRC construction

Date: 2026-11-12. Status: AUTHOR_EXACT_FINITE_PROOF, cross-checked on selected instances; independent Driver mathematical admission pending. Frozen scientific input pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The underlying original nine-state signed-X6 BRC problem and all 24 (window, signature) observer demands are unchanged.

## New finite theorem

Let K* be the seven **complete raw signed-microstep keys** of the explicit 84-prefix witness EC49FKX:

`{(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}`.

Let U be all 94 full raw keys appearing in the complete frozen 178,850-word catalogue. For every seven-key set K' with either K'=K* or

`K' = (K* \ {k}) union {k'}`, where `k in K*` and `k' in U\K*`,

allow *any number* of frozen legal operation words whose full raw key belongs to K', covering all 24 observer labels, and charge the number of distinct **nonempty ordered, signed six-axis native microstep prefixes**. Then:

**If K' is feasible, the exact optimum C(K') >= 84.** Equality is achieved for K* and precisely two of its 609 one-key swaps. The 84-prefix construction is thus a finite, certified one-key-replacement local optimum. This theorem does not assert global seven-key optimality or optimality after two-key replacements.

Of the 609 distinct one-key swaps (7 times 87), exactly 417 fail the necessary test that the union of all allowed word labels covers all 24 requirements. The remaining **192 feasible swaps were all solved exactly**, including the 76 cases with four distinct first-byte native roots. Including unchanged K*, 193 exact fixed-key optimizations were executed.

## Complete exact cost histogram (193 key sets)

| exact minimum | count |
|---:|---:|
|84|3|
|86|1|
|90|1|
|92|3|
|94|2|
|96|87|
|98|83|
|100|2|
|104|2|
|108|1|
|126|1|
|129|2|
|137|2|
|145|2|
|178|1|

The three optima attaining 84 are K* itself; replacing (5,4,1) by (6,3,1); and replacing (6,4,1) by (5,5,1). Among 193 solved instances, 117 have exactly three occupied first-byte native roots and 76 have exactly four. No additional native first-root case was silently discarded.

## Exact finite proof and representation

1. Enumerate all 178,850 legal (observer label, native operation word) pairs from the frozen EC49FGW generator. Compute the *complete* raw key and every ordered signed native microstep. Its 94-key set is U. For each of 609 distinct replacements, union the observation masks of **all** words belonging to the seven allowed keys. Coverage of all 24 labels is necessary; this rejects exactly 417 sets.
2. For each of the remaining 192 plus K*, partition every allowed word by its literal first signed native step (encoded by its native signed byte, not by the underlying operation name). The resulting nonempty prefix trees have pairwise-disjoint prefix sets.
3. For root r, build the *complete* literal trie of allowed words. A node's exact attainable observer masks are computed bottom-up: select or omit complete words ending at the node; combine disjoint child masks by bitwise OR and prefix costs by addition; add one for every selected nonempty node. Taking the minimum over supersets yields g_r(D), the exact least native prefix cost satisfying at least the root-local demand subset D.
4. Assign each one of the 24 required labels to one first-step root that has at least one legal word for that label. For each allocation, sum the relevant g_r(D_r). Minimize over the finite allocations. This equality is exact: any legal global family admits an allocation of each satisfied label to a root it uses, and conversely its root-local selected solutions join to a legal global family. Roots have disjoint native prefix sets and thus additive costs.
5. The separately compiled C++17 integer solver exhausts every root-local subset state (at most 2^12 per root), every complete candidate word and every allocation for all 193 instances. It reports the exact minima above; `SCAN_SETS_ALL.json` ordering and the `costs_in_order` array of `EXACT_SUMMARY_EC49FKY.json` specify the full scan and provide reproducible checksums.

The existing EC49FKX standalone 84-prefix witness certifies the upper bound at K*. An **independently written Python subset-mask trie implementation** reran six chosen instances: IDs 0,119,180 (all three 84-minimum sets), 107 (four-root cost 96), 182 (four-root cost 100), and 192 (four-root cost 178). Every exact minimum matched the C++ output; its coverage includes both 3-root and 4-root cases. This is an author-side independent implementation cross-check, not an independent Driver review.

## Reproduction, original scientific sources, and evidence

Predecessor source is at `../EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py`, `../EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGJ_SEVEN_KEY_94_WITNESSES.json`, and the explicit FKX witness at `../EC49FKX_84_PREFIX_COUNTEREXAMPLE_20261112/`. The frozen catalogue, signature table, signed operation microsteps and full-key definition were not changed. The local verification copied the preceding original scientific definitions from EC49FKS evidence; the current branch source has equivalent enumerator/observer/native-step definitions and the same frozen pin. Those local archive copies do not have the identical full Git blob bytes as the current repository's reproduction files, so the result is stated on the matching explicitly checked scientific definitions, not asserted to use identical surrounding file formatting.

Executed code in this directory: `MAKE_SCAN_7KEY_ALL.py`, `SCAN_7KEY_GENERAL.cpp`, and `VERIFY_SCAN_INDEPENDENT.py`. Generate `SCAN_ALL_DATA.txt` and `SCAN_SETS_ALL.json` with `python3 MAKE_SCAN_7KEY_ALL.py`; compile `g++ -O3 -std=c++17 SCAN_7KEY_GENERAL.cpp -o scan_general7`; run `./scan_general7 < SCAN_ALL_DATA.txt > SCAN_ALL_RESULT.txt`; run the independent Python verifier after generating the input and result files. Python uses its standard library only, the C++ program uses integer exact arithmetic; no MIP solver or numerical tolerance establishes this theorem.

Expected exact outcome: 193 solution lines; scan histogram as above; minimum 84 and exactly three key sets attaining it. The `EXACT_SUMMARY_EC49FKY.json` holds all 193 optimal costs and the original local raw result SHA256. A complete evidence archive, including generated inputs and logs, is retained as a local research handoff.

## Next discriminating question

Search *two-key replacements* from K* that preserve the 24 exact demands. A <=83 signed-prefix witness would improve the global upper bound. Otherwise establish certified finite exclusion for specified two-key families, reusing the exact multi-first-root decomposition. The 84 bound is an established explicit upper bound, not the global minimum.

Activity/CLAIM: the new native session/EC49AS control reads were queued during this author computation; no authenticated current CLAIM or formal Result was asserted. Scientific input and P000 / protected ACTIVE worldview are unchanged.
