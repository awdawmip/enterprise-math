# EC49FOP — Frozen native BRC two-key neighborhood: exact terminal/root-observer injectivity

Date 2026-11-14. **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.** This is independently preserved portable research, not a formal CLAIM/Result/Review. Continues the EC49FON hub-kernel theorem ([PR #2406](https://github.com/awdawmip/enterprise-math/pull/2406)) and the constructed nonzero native-prefix gauge ([PR #2415](https://github.com/awdawmip/enterprise-math/pull/2415)). The previous 73-one-key-neighbor calculation is preserved in [PR #2411](https://github.com/awdawmip/enterprise-math/pull/2411).

## Source, domain and proposition

The original scientific source pin is \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`; \`master_and_radius3_cases.txt\` SHA256 is \`cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`. That frozen file consists of 94 coded cache-key families, 178,850 native prefix words, and 38,169 distinct seven-key configurations. The current census does not change that source. The earlier source can be obtained using the pinned EC49FOM/EC49FON evidence.

Fix case 32315, with seven-key set \`K0={0,4,5,11,37,39,81}\`. For case \`i\`, let \`K_i\` be its seven-key set, and \`E_i(l)\` the exact named legal-root set read from the first byte of every native codeword assigned to demand \`l\`. Define

\`N2={i in [0,38169) : |K_i\K0|<=2 and E_i(l)=E_32315(l) for all 24 named demands l}\`.

All demands are retained, including forced demands. The seven optional demands have legal roots:

- \`5:{05,07}\`; \`7:{06,07}\`; \`13:{06,07}\`;
- \`15:{03,05,07}\`; \`17:{03,06,07}\`; \`19:{03,05,07}\`; \`21:{03,06,07}\`.

The other 17 demands each have a forced root. Thus every configuration in \`N2\` has exactly \`2^3·3^4=648\` complete named root assignments. For root \`r\`, \`D^i_r(S)\` is the exact minimum number of used non-root trie-prefix vertices of selected native codewords covering the named demand subset \`S\` (with its forced demands included). \`P(i)\` is the deterministic tuple of all 168 *reachable rooted* costs; \`T(i)\` is the 648-vector of complete costs \`Σ_r D^i_r(S_r(ρ))\`.

**Exact finite theorem.** The set \`N2\` has **411** cases, at exact key-replacement distances 0/1/2: **1/73/337**. Among these 411 cases are exactly **178** distinct complete-cost vectors \`T\` and **178** distinct reachable-root vectors \`P\`. For every pair \`i,j ∈ N2\`,

\`T(i)=T(j)  <=>  P(i)=P(j)\`.

Of all \`C(411,2)=84,255\` unordered same-domain pairs, **4,068** satisfy both equalities and **80,187** satisfy neither. The baseline 32315 has exactly **38** neighbors including itself with the same complete-cost vector and exactly those same 38 have the same reachable-root profile. Consequently there is **no nonzero globally invisible cross-root cost gauge** among these 411 original native configurations.

## Proof and executable finite certificate

1. Parse the frozen 94 keys and all 38,169 seven-key rows; compute every configuration's exact 24-component named legal-root tuple. Select exactly those with the baseline's full tuple and key replacement distance at most two. The exhaustive selector \`VERIFY_EC49FOP_CHECK.py\` asserts the counts \`411=(1+73+337)\`; it also finds 625 different full legal-domain tuples across the entire original 38,169-case corpus. The ordered selected case-ID list is pinned by SHA256 \`24970eb78b8c8aa6e9cb52bfd5a84ed5e45aca2341efc0febe72e74cda974cf3\`.
2. Insert all relevant native codeword paths for each named root into a byte-trie. At each vertex, a min-plus/bitwise-OR dynamic program gives the minimum vertices required to cover any exact label set. The child subproblems are independent conditional on the node, so induction over the trie proves the recurrence. Take the downward-closed minimum over supersets to represent demand coverage with possible incidental labels. Enumerate every forced-plus-optional root mask. The native C++17 source in this directory produces **69,048 exact cost records** (=411×168); the full CSV SHA256 is \`122f1ee6716df4b37913ec3920130a97993c7abd2b1d8c02b03fcaf5b940f5c3\`.
3. The independent Python checker reconstructs all **648** assignment costs by summing the four named rooted DP values and compares **whole tuples** of exact integer costs. Group by \`T\` and \`P\` separately. It checks directly that no \`T\`-equivalence class contains two distinct \`P\` vectors: 178 \`T\` classes, 178 \`P\` classes, exactly 4,068 equal pairs in each. This proves the implication \`T(i)=T(j) ⇒ P(i)=P(j)\` by complete finite coverage; the reverse implication follows from the definition of sum over roots.
4. Independent C++17 \`-O2\` and \`-O3\` executions produced **byte-identical** complete root-profile CSVs. For the 45 cases in this set overlapping the previously preserved EC49FON rooted-cost inventory, the newly generated **7,560** source cost records match its original saved entries. The Python comparison uses exact integers without numerical tolerance. The original named source constraints, P000, and the finite native prefix operator are preserved.

A locally verified full artifact archive also contains the original 9.3 MB frozen input, the exact selector ID file, all 69,048 CSV rows, locally executed source files, logs, JSON output, and SHA256 checksums. The verified archive uses a non-self-referential SHA256SUMS manifest, with all checks passing. Its archive SHA256 is \`4ac2bb7a247a9133377818939f5217c903a3f0b1b63f161ee08787b127e32aa7\`. Archive publication to a remote binary destination is separate from this repository-native proof, source and machine summary.

## Reproduction

Obtain the exact original \`master_and_radius3_cases.txt\`. Run the Python checker with \`--select-only\` first, then compile the native exporter and run the checker:

\`\`\`sh
python3 VERIFY_EC49FOP_CHECK.py --select-only master_and_radius3_cases.txt
g++ -std=c++17 -O2 -Wall -Wextra -pedantic VERIFY_EC49FOP_EXTRACT.cpp -o ec49fop_extract
./ec49fop_extract EC49FOP_IDS.txt < master_and_radius3_cases.txt > EC49FOP_PROFILES.csv
python3 VERIFY_EC49FOP_CHECK.py master_and_radius3_cases.txt EC49FOP_PROFILES.csv
\`\`\`

The archived results and source code were actually executed locally on the frozen bytes; this remote source is a reproducible representation of the same calculation. An optional radius-three extension was started, but terminated before finishing a larger extraction. No conclusion is asserted from the partial radius-three output.

## Scientific interpretation and next question

The abstract hub-kernel has nonzero quadratic gauge directions and EC49FOO constructs a native trie operator instance realizing one. The observed **411 original** cases have an injective terminal observer on their reachable-root profile family. The next discriminating research question is to extend from this 411-case block to the **966** same-domain configurations at at most three key replacements, then across all 625 domain blocks, looking for an actual frozen-cache pair \`T(i)=T(j)\` and \`P(i)≠P(j)\`. To prove corpus-wide absence, one must cover all domain-compatible pairs or produce a structural exclusion certificate. Keep source identity and all signed-path provenance attached before any observer quotient. This is a typed restricted BRC prefix observation in the native X6 Heartbeat World research framework, not a collapse of X6 state identity.

**Authority:** historical Researcher-ID \`EM-DIRECT-204C14\` and Activity \`RA-6893088D0A7347CE7F4D8720\` are provenance. Current Source task lookup on 2026-11-14T13:35:04Z returned \`NO_CANONICAL_PUBLICATION_DIRECTORY\` for \`RS-EC49AS\` (pinned source \`d4dce3eccc7761afa235331fe0ade23be243b48e\`). This independent proof note is not a new formal Task, CLAIM, Activity write or Result.