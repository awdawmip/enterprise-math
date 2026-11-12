# EC49FMI — first 600 exact radius-three seven-key signed-X6 prefix optima

Date: 2026-11-12. Research mode: author-side exact finite computation, independent Driver review and formal native Task binding pending. Frozen scientific pin: **fc0f038e7bfd12c886b4d37f900bfb770c0f61ab**. P000 and ACTIVE worldview unchanged.

## Precise theorem and domain

Keep the original frozen nine-state BRC catalogue, 178,850 legal labeled operation words, 94 complete three-coordinate raw cache keys, 24 observer demands and original *ordered, signed six-axis native microstep* paths. For each seven-key set K, define C(K) as the minimum cardinality of the union of all nonempty native signed microstep prefixes of legal words selected to cover all 24 demands, using only keys in K.

Use the original 84-prefix witness key set:

K* = {(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}.

Enumerate exact three-key replacements by lexicographically sorted removed triples of K* and added triples from the 87-key complement. There are exactly **C(7,3)C(87,3)=3,709,825** distinct seven-key replacements. Exhaustive 24-bit key-support union finds **38,169** that can cover every observer demand and **3,671,656** that cannot. Index the coverable ones K_i by their original nested-loop order, i=0,...,38168.

**Theorem EC49FMI.** For the complete, explicitly identified first 600 support-coverable radius-three instances,

\[
\boxed{\min_{0\le i\le599} C(K_i)=102}.
\]

The minimum 102 is attained only at indices **32** and **93**. The complete first-600 cost range is 102–194; 272 instances have three distinct first signed-native roots and 328 have four. Therefore this entire 600-instance finite family excludes any solution using at most 101 native prefixes.

The two attaining cache-key sets are:
- Index 32: {(2,1,1),(2,2,1),(3,0,1),(4,0,1),(4,2,1),(6,3,1),(6,4,1)}.
- Index 93: {(2,1,1),(2,2,1),(3,0,1),(4,0,1),(4,2,1),(5,4,1),(5,5,1)}.

## Proof and actual numerical evidence

The frozen generator exhausts every original BRC legal word, its full raw key, observation label, and literal signed X6 path. For each cache key, take the OR of its 24-bit label masks. A proposed keyset can cover all labels exactly when the OR of its keys' masks equals all 24 bits: each demand chooses its legal word independently. Complete enumeration yields the 38,169 coverable three-key replacement sets.

For fixed K, insert *every* eligible legal word into literal signed-native prefix tries, grouped by the first signed microstep. At each node the exact integer min-plus demand-subset DP selects terminal labels and merges descendant mask coverage by OR, summing distinct prefix-node costs and charging one for every used nonempty node. Superset relaxation allows excess observed labels. First-microstep-root tries share no nonempty prefix. Enumerate all allocations of the 24 demands to eligible roots, minimizing summed exact root costs. Every legal word selection induces a DP choice of no larger cost; every DP optimum is realizable by legal terminal words. Trie induction and root additivity establish exactness of each computed C(K).

Two uninterrupted, nonoverlapping cached-C++17 solver batches actually completed all indices **0..149 and 150..599**. The original 6,315-case cached trie engine's *input-case count assertion only* was adapted to 38,169; the integer DP and signed native path computation were unchanged. All 600 case IDs are present exactly once, and the saved 600-byte cost vector is lossless. Its exact raw SHA256 is **73baec37195854b372f6acc8568d3a3f4e5e0cd9f2318d8660bbd0086dd2c3bb**. The complete regenerated master input SHA256 is **cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e**.

Independent Python standard-library prefix-trie/subset DP was *actually executed* on indices **0=>116, 32=>102, 93=>102, 149=>138**; every result matches the cached engine. The original noncached C++17 program was independently executed with its own per-case input protocol for **32=>102, 93=>102, 599=>167**, also matching.

## Reproduction and provenance

- **BUILD_EC49FMI.py** was executed to regenerate all 3,709,825 support masks and all 38,169 feasible case indices, reproducing the frozen C++ master SHA256 above. It uses the sibling frozen generator EC49FGW_RADIUS5_SCREEN.py.
- **EXACT_VECTOR_EC49FMI.json** stores the full 600-case uint8 exact cost vector in zlib+base64, with source-counts, histogram, minimum positions, and SHA256s.
- **VERIFY_EC49FMI.py** checks the full vector's exact digest, minimum, maximum, histogram, and sampled checks. Optional --solve recompiles the existing GitHub EC49FMG cached C++ solver with the necessary case-count change and recomputes all 600.
- Actual raw outputs, two completed logs, adapted cached C++ source, unchanged native DP, independent-check logs, master input, original frozen generator and manifest are in the separate author evidence package. The remote generator's scientific core (DFA, native steps, key and word generation) matches the archived executable's core; the two whole-file Git blobs are not represented as byte-identical.
- Previous independently published milestones: EC49FKX (84-prefix witness), EC49FKY (trie DP), EC49FMB (full seven-key coverability), EC49FMH (complete radius-two minimum 84), EC49FMC (radius-five minimum 114).

## Unfinished unit and actual Source state

The next exact interval is **radius-three feasible indices 600..38168** (37,569 configurations). Radius-four still has 62,620 coverable cases; previously verified radius-five minimum is 114. Seek a lawful 83-prefix-or-lower witness or an exact reusable lower-bound cut. The unrestricted seven-key mother problem retains upper bound **C_min(7)<=84** and remains open.

Source-native exact Task lookup RS-EC49AS returned **CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION** in this run. A fresh native Researcher session registration was pending when this manuscript was drafted. No unrelated active owner was claimed or displaced, and no native CLAIM/open, Result or independent Driver admission is asserted by this GitHub author-side publication. The research PR remains unmerged.
