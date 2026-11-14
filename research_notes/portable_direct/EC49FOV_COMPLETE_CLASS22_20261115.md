# EC49FOV — Exact full-class census for original BRC legal-root domain 22

Date: 2026-11-15. Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Scope and frozen sources
The original scientific pin is `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (not repinned). The frozen source text has SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`, comprising 94 original key families, 178,850 labeled signed-byte-prefix words, 38,169 seven-key configurations, named labels 0..23, and roots 03/05/06/07. All 38,169 configurations were grouped by *all 24 exact named legal-root masks*. There are 625 groups.

Let `C22={K : E(K)=E(22)}`, where `E(K)` is the 24-label named legal-root signature. Exactly 307 configurations satisfy this predicate. Each has exactly 576 complete legal root assignments and 292 reachable rooted subset-cost coordinates.

## New exact finite theorem
For a configuration K and root r, `D^K_r(S)` denotes the exact minimum signed-byte Trie prefix-cover cost for the required demand subset S (plus all demands mandatory at root r). Let `P(K)` be the vector of all reachable named `(r,S,D^K_r(S))` coordinates. Let `T(K)` be the 576-vector indexed by all complete legal assignments rho, with
`T_K(rho)=sum_r D^K_r(S_r(rho))`.

For every `A,B in C22`,
`T(A)=T(B)  <=>  P(A)=P(B)`.

Proof: The forward check is the exact exhaustive census below. The reverse implication is immediate from the sum definition, as `P(A)=P(B)` gives each assigned root the same cost. Thus equality classes of P refine equality classes of T. In the exhaustively verified class C22, both partitions have the same number of equal pairs, 1594; hence no T-class can merge distinct P-classes. The two partitions are equal, and the equivalence is established for all 46,971 unordered original pairs in C22.

## Exact certificate
- 307 complete class members from exhaustive 38,169-input legal-mask grouping. SHA256 of ascending comma-separated original class IDs: `4f69a5750832759e1116426d1b5e2336974f847728f145e1d34b88d1216ead28`.
- 89,644 exact minimum rooted costs, each tied to config, named root, mandatory/optional named label masks, optional subset, and integer cost. CSV SHA256: `700e1649bb395c3f1f3e73ee9d773d36954c47e6bd1faed0332c397c12da3649`.
- 176,832 exact terminal total costs (=307 x 576), checked over complete allocation product. Two vector partitions each have exactly 175 equality classes, with exactly 1594 equal unordered pairs. Nonzero all-allocation gauge pairs: **zero** in C22.
- C++17 exact native byte-prefix Trie extractor produces identical CSVs with `-O2` and `-O3`. Independent Python byte-Trie reconstructs all 292 reachable coordinates of each original configuration 22, 31 and 32987: 876 checked values, all identical to extracted costs.
- The result is a complete *finite input and full-class* theorem. Previously found nonzero native gauge pairs in other legal-root classes (EC49FOR) remain valid.

### Algorithmic reproduction
1. Parse the frozen original master `94 178850 38169`. For each of 94 key families read every labeled signed-byte codeword, including the root in its first byte and the remaining ordered byte-prefix sequence. Read all 38,169 seven-key configurations.
2. For every config, union the per-key root masks per demand label. Classify using the resulting 24-component ordered signature and select all IDs matching config 22 (not a sampled subset).
3. At each named root, assemble a byte Trie from the selected seven key families; terminal nodes carry the OR-mask of their named demands. Compute exact mask-costs using child union convolution, charging one unit for every nonempty retained trie prefix; take superset minima to obtain the optimal coverage cost for any required mask. Export every reachable subset in named-label coordinates, including mandatory roots. Validate that each expected `(config,root,subset)` appears once.
4. Enumerate all 576 products of each nonmandatory label's eligible root choices. For each allocation sum the four rooted costs. Form full tuples, group by exact equality (not hash-only), and count group sizes as n(n-1)/2. Compare with exact root-tuple equality groups.
5. Independently verify three configurations using a separate Python byte-Trie solver and compare O2/O3 extractor bytes.

## Provenance / status / next problem
Predecessors: EC49FOR PR #2426 (nonzero gauge witnesses), EC49FOS PR #2430 (largest 2368-config domain), EC49FOU PR #2434 (three complete 99-config classes). This EC49FOV unit preserves frozen scientific input and does not supersede predecessors.

Original complete evidence bundle: `EC49FOV_COMPLETE_CLASS22_EVIDENCE_20261115.tar.xz`, SHA256 `83e072688adc92104c57a78dc6bf6963175297c0eccbf0d704bc9b6d43b12757`. It contains the original input bytes, the 89,644-row CSV, complete C++17 extractor, Python checker and independent byte-Trie validator, logs, exact JSON result and SHA256 manifest. Source-file CSV SHA256s above allow artifact cross-verification.

Next: classify another previously uncompleted named-root class, and search for nonconstant subset-dependent cost changes that cancel for every complete allocation. Partial early computations in classes 0/1 and 25 are exploratory and are not represented as a completed class.

Mathematics: EXACT_FINITE_CHECKED / NOT_REVIEWED. GitHub publication of this note is scientific-source preservation, not formal CLAIM/Result or Foundation acceptance.
