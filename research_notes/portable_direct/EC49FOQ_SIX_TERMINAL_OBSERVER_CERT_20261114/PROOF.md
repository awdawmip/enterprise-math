# EC49FOQ — Six exact terminal observers separate 178 native BRC classes

Date: 2026-11-14. Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Independent portable research, not an authorized formal TASK/CLAIM/Result/Review.

## Frozen input and domain

Preserve scientific pin \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`, master source \`master_and_radius3_cases.txt\` SHA256 \`cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`. Source is the exact native signed-prefix root trie-cover model, **not** a new choice of model, a physical-time dynamics, or a change to P000.

Continue [EC49FOP, PR #2419](https://github.com/awdawmip/enterprise-math/pull/2419) @ \`367828d89c411a3f73c919c4ee9a31c1292b5669\`: its fully checked same-domain radius-two population \`N_2\` consists of exactly **411** original seven-key cache configurations (radius counts 1, 73, 337). All preserve the named legal root domains for 24 labels; 17 labels are forced and the seven free labels in fixed order are

\`\`\`
labels  = (5, 7, 13, 15, 17, 19, 21)
choices = ((05,07),(06,07),(06,07),(03,05,07),(03,06,07),(03,05,07),(03,06,07)).
\`\`\`

There are 648 complete legal assignments, in the lexicographic Cartesian-product order above. For each \`K\`, let \`T_K(rho) = sum_{root in {03,05,06,07}} D_root^K(S_root(rho))\` be the exact integer rooted-trie cost. The original \`D\` table covers 168 legally reachable root masks per configuration and is computed by trie DP, not floating point. The input \`EC49FOP_PROFILES.csv\` (69,048 data rows) is the previously independently reproducible \`-O2/-O3\` result, SHA256 \`122f1ee6716df4b37913ec3920130a97993c7abd2b1d8c02b03fcaf5b940f5c3\`.

## Finite theorem: six coordinates suffice

In the 0-based lexicographic enumeration of all 648 complete assignments, set

\`\`\`
J = (439, 314, 342, 8, 42, 266).
\`\`\`

Their named root-choice vectors in the fixed label order are

\`\`\`
439: (07,06,07,05,03,07,06)
314: (05,07,07,07,06,07,07)
342: (07,06,06,03,07,03,03)
  8: (05,06,06,03,03,07,07)
 42: (05,06,06,05,06,07,03)
266: (05,07,07,03,07,05,07).
\`\`\`

**Theorem.** For every pair \`K,K' in N_2\`,

\`\`\`
(T_K(j) for j in J) == (T_K'(j) for j in J)
       if and only if
(T_K(j) for j in [0,648)) == (T_K'(j) for j in [0,648)).
\`\`\`

Thus the restriction of the terminal observation to these six named assignments is injective on the **178** distinct full-terminal equivalence classes of this frozen population. Of all \`binom(411,2)=84,255\` unordered configuration pairs, exactly **4,068** are equal under the full 648-observation vector; the same 4,068 are equal under the six-observation vector, and there are zero six-observer collisions between different full classes. This is an exact observer-fiber factorization on the declared finite population, giving an **upper bound of six** on the number of terminal coordinates needed to classify these classes. Minimality is not asserted.

## Proof/certificate

The implication from full equality to six-coordinate equality is coordinate restriction. The reverse is proven by **exhaustive finite equality of fibers**:

1. Enumerate the 411 original IDs from the radius-two domain selector, and read all 69,048 named rooted cost records, preserving the mandatory/optional named root masks and checking 168 records per configuration.
2. Enumerate the 648 lexicographic choices for every \`K\`; sum the four exact integer trie-cover costs for each assignment to obtain its complete terminal vector. Partition all 411 cases by exact full-vector equality, obtaining 178 fibers.
3. Extract precisely coordinates \`J\` from every vector. Partition the same 411 IDs by equality of these six integer costs. The machine verifier asserts that both partitions contain 178 groups and that their **complete member-ID lists** are identical. It also independently computes the 4,068 equal pairs.
4. \`EC49FOQ_COSTS.csv.gz.b64\` holds the entire 411-row six-observer CSV, deterministically gzip-compressed then base64 encoded. The verifier decompresses it and compares all canonical rows **byte-for-byte** against the values newly computed from the prior original rooted profiles. The decompressed CSV SHA256 is \`c28d0714437436df53b3773069ba403b34b9b1a0dd96cf0c862db171d9cdba7b\`.

This checks all 84,255 pairs without relying on floating-point tolerances or hashes as equality oracles. The original rooted-trie DP proof, frozen input, and fully enumerated costs are preserved in [PR #2419](https://github.com/awdawmip/enterprise-math/pull/2419) and its previously recorded full evidence archive; the current certificate is a verified **additional observer-compression result** over those pinned data, not a recomputation or replacement of the science.

Reproduce after obtaining \`EC49FOP_PROFILES.csv\` from that original evidence archive:

\`\`\`sh
python3 VERIFY_EC49FOQ.py EC49FOP_PROFILES.csv EC49FOQ_COSTS.csv.gz.b64
\`\`\`

Expected: \`EC49FOQ PASS: 411 configurations, 648 full assignments, 178 classes, 4068 equal pairs; six observers separate all classes\`.

## Future-observer scope and remaining question

The six-coordinate quotient preserves the **full cost observer** \`T\` on this exact \`N_2\` population: the equality of its fibers proves exact factorization of the complete terminal-vector map through the six-coordinate map on \`N_2\`. No blanket safety statement is made for new configurations, future cache changes, full rooted prefix states, full X6 cells, or other operations. Original native paths, signed prefix provenance and frozen input remain available.

Next: inspect whether these same six coordinates separate the **966 same-domain radius-three** configurations and if not produce the first explicit collision and repair set. Seek a direct rooted-prefix cost update capable of evaluating the selected assignments without generating all 168 rooted masks; include preprocessing in any claimed speedup. The prior full radius-three native cost extraction exceeded its execution boundary and supplied no complete classification.

Researcher attribution: this portable artifact was computed in the current independent research continuation; historical author IDs and activity IDs remain provenance only. No formal CLAIM, Result, Review, or activity update is asserted by this document.
